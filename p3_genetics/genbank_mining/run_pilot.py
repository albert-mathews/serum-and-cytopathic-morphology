#!/usr/bin/env python3
"""P3 GenBank/RefSeq metadata mining pilot — catalog-card stats only."""
from __future__ import annotations

import csv
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

OUT = Path("/workspace/p3_genetics/genbank_mining")
AUDIT_CSV = Path("/workspace/p3_genetics/P3_type_strain_audit.csv")
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
TOOL = "serum-cpe-p3-mining"
EMAIL = "albert.mathews.research+ncbi@gmail.com"
SLEEP = 0.35  # <=3 req/s
SAMPLE_TARGET = 2000
EFETCH_BATCH = 50

BASE_QUERY = 'Viruses[Organism] AND srcdb_refseq[PROP] AND "complete genome"[Title]'

CULTURE_CLAUSE = (
    'Vero OR "Vero E6" OR MRC-5 OR "HEp-2" OR HeLa OR MDCK OR BHK OR A549 OR Huh7 '
    'OR "cell line" OR "cell culture" OR "tissue culture" OR lab_host[All Fields] '
    "OR cell_line[All Fields]"
)
CPE_CLAUSE = "CPE OR cytopathic OR cytopathogenic OR syncytia OR syncytium"
PASSAGE_CLAUSE = (
    'passage OR passaged OR plaque OR TCID OR "isolated in" OR "propagated in"'
)
CLINICAL_CLAUSE = (
    'bronchoalveolar OR BALF OR nasopharyngeal OR stool OR metagenom* '
    'OR "clinical specimen" OR patient'
)

# For text parsing (case-insensitive)
CULTURE_PAT = re.compile(
    r"\b(vero(?:\s*e6)?|mrc-?5|hep-?2|hela|mdck|bhk|a549|huh-?7|"
    r"cell\s*line|cell\s*culture|tissue\s*culture|lab[_\s]?host)\b",
    re.I,
)
CPE_PAT = re.compile(
    r"\b(cpe|cytopathic|cytopathogenic|syncytia|syncytium)\b", re.I
)
PASSAGE_PAT = re.compile(
    r"\b(passage[sd]?|plaque|tcid|isolated\s+in|propagated\s+in)\b", re.I
)
CLINICAL_PAT = re.compile(
    r"\b(bronchoalveolar|balf|nasopharyngeal|stool|metagenom\w*|"
    r"clinical\s+specimen|patient)\b",
    re.I,
)
YEAR_PAT = re.compile(r"\b(19\d{2}|20[0-2]\d)\b")
LOCUS_DATE_PAT = re.compile(
    r"LOCUS\s+\S+\s+\d+\s+bp\s+\S+\s+\S+\s+\S+\s+(\d{2})-([A-Z]{3})-(\d{4})",
    re.I,
)
MONTHS = {
    "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
    "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12,
}


def eutils_get(endpoint: str, params: dict) -> bytes:
    params = dict(params)
    params["tool"] = TOOL
    params["email"] = EMAIL
    qs = urllib.parse.urlencode(params, safe='[]"*')
    url = f"{BASE_URL}{endpoint}?{qs}"
    time.sleep(SLEEP)
    req = urllib.request.Request(url, headers={"User-Agent": f"{TOOL}/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def esearch_count(term: str) -> int:
    data = eutils_get(
        "esearch.fcgi",
        {"db": "nucleotide", "term": term, "retmax": 0, "rettype": "count"},
    )
    root = ET.fromstring(data)
    count_el = root.find("Count")
    if count_el is None or count_el.text is None:
        raise RuntimeError(f"No Count for term: {term[:80]}")
    return int(count_el.text)


def esearch_ids(term: str, retmax: int, retstart: int = 0) -> list[str]:
    data = eutils_get(
        "esearch.fcgi",
        {
            "db": "nucleotide",
            "term": term,
            "retmax": retmax,
            "retstart": retstart,
            "usehistory": "n",
        },
    )
    root = ET.fromstring(data)
    return [el.text for el in root.findall(".//Id") if el.text]


def esearch_all_or_sample(term: str, count: int, sample_target: int) -> tuple[list[str], str]:
    """Return UIDs and sampling note."""
    if count <= sample_target:
        ids: list[str] = []
        retstart = 0
        while retstart < count:
            batch = min(500, count - retstart)
            chunk = esearch_ids(term, batch, retstart)
            ids.extend(chunk)
            if not chunk:
                break
            retstart += len(chunk)
            print(f"  esearch IDs: {len(ids)}/{count}", flush=True)
        return ids, f"all {len(ids)} of {count}"
    # Systematic sample: stride through first pages or evenly
    # NCBI esearch returns by relevance/date; take first sample_target with note
    ids = []
    retstart = 0
    while len(ids) < sample_target:
        batch = min(500, sample_target - len(ids))
        chunk = esearch_ids(term, batch, retstart)
        if not chunk:
            break
        ids.extend(chunk)
        retstart += len(chunk)
        print(f"  esearch sample IDs: {len(ids)}/{sample_target} (of {count})", flush=True)
    note = (
        f"first {len(ids)} of {count} (NCBI default order; not random). "
        "For large N, pilot uses first-N systematic slice."
    )
    return ids, note


def efetch_gb(ids: list[str]) -> str:
    # POST for large ID lists
    params = {
        "db": "nucleotide",
        "id": ",".join(ids),
        "rettype": "gb",
        "retmode": "text",
        "tool": TOOL,
        "email": EMAIL,
    }
    data = urllib.parse.urlencode(params).encode()
    url = f"{BASE_URL}efetch.fcgi"
    time.sleep(SLEEP)
    req = urllib.request.Request(
        url, data=data, headers={"User-Agent": f"{TOOL}/1.0"}
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        return resp.read().decode("utf-8", errors="replace")


def split_gb_records(text: str) -> list[str]:
    parts = re.split(r"(?=^LOCUS\s)", text, flags=re.M)
    return [p for p in parts if p.strip().startswith("LOCUS")]


def metadata_only(gb: str) -> str:
    """Truncate at ORIGIN or // — keep FEATURES source region."""
    m = re.search(r"\nORIGIN\b", gb)
    if m:
        return gb[: m.start()]
    m = re.search(r"\n//\s*$", gb, re.M)
    if m:
        return gb[: m.start()]
    return gb


def extract_field(gb: str, tag: str) -> str:
    # Multi-line fields indented
    pat = re.compile(
        rf"^{tag}\s+(.+?)(?=^[A-Z]{{2,}}|\Z)", re.M | re.S
    )
    m = pat.search(gb)
    if not m:
        return ""
    lines = []
    for line in m.group(1).splitlines():
        lines.append(line.strip())
    return " ".join(lines).strip()


def extract_source_features(gb: str) -> str:
    """Collect source feature block text until next feature or ORIGIN."""
    # FEATURES section
    fm = re.search(r"^FEATURES\s+.*$", gb, re.M)
    if not fm:
        return ""
    rest = gb[fm.end() :]
    # Find source feature
    sm = re.search(r"^\s{5}source\s+", rest, re.M)
    if not sm:
        return ""
    after = rest[sm.start() :]
    # Until next feature at column 5 (non-space after 5 spaces) that's not a qualifier
    # Qualifiers start with /
    lines = after.splitlines()
    out = [lines[0]]
    for line in lines[1:]:
        if re.match(r"^\s{5}\S", line) and not line.lstrip().startswith("/"):
            break
        if line.startswith("ORIGIN") or line.startswith("//"):
            break
        out.append(line)
    return "\n".join(out)


def parse_year(gb_meta: str) -> str:
    m = LOCUS_DATE_PAT.search(gb_meta)
    if m:
        return m.group(3)
    # JOURNAL lines often have (YYYY)
    for jm in re.finditer(r"JOURNAL\s+.+?\((\d{4})\)", gb_meta, re.S):
        y = int(jm.group(1))
        if 1950 <= y <= 2026:
            return str(y)
    # CreateDate-like in COMMENT
    for ym in YEAR_PAT.finditer(gb_meta[:2000]):
        y = int(ym.group(1))
        if 1980 <= y <= 2026:
            return str(y)
    return ""


def parse_organism(gb_meta: str) -> str:
    m = re.search(r"^ {2}ORGANISM\s+(.+)$", gb_meta, re.M)
    if m:
        return m.group(1).strip()
    src = extract_field(gb_meta, "SOURCE")
    return src.split(".")[0].strip() if src else ""


def parse_accession(gb_meta: str) -> tuple[str, str]:
    acc = ""
    ver = ""
    m = re.search(r"^ACCESSION\s+(\S+)", gb_meta, re.M)
    if m:
        acc = m.group(1)
    m = re.search(r"^VERSION\s+(\S+)", gb_meta, re.M)
    if m:
        ver = m.group(1)
        if not acc:
            acc = ver.split(".")[0]
    if not acc:
        m = re.search(r"^LOCUS\s+(\S+)", gb_meta, re.M)
        if m:
            acc = m.group(1)
    return acc, ver


def flag_keywords(text: str) -> dict:
    return {
        "culture_cell": bool(CULTURE_PAT.search(text)),
        "cpe": bool(CPE_PAT.search(text)),
        "passage": bool(PASSAGE_PAT.search(text)),
        "clinical": bool(CLINICAL_PAT.search(text)),
    }


def accession_variants(raw: str) -> list[str]:
    """Extract plausible accession tokens from audit cell."""
    toks = re.findall(
        r"\b((?:NC|AC|NG|NM|NR|NZ|NW|XM|XR|YP|NP|AP|CP|BK|U|V|X|Y|Z|A|B|C|D|E|F|G|H|J|K|L|M|N|O|P|Q|R|S|T|"
        r"AY|DQ|EF|EU|FJ|GQ|GU|HM|HQ|JF|JN|JQ|JX|KC|KF|KJ|KM|KP|KR|KT|KU|KX|KY|KZ|LC|LR|LT|MF|MG|MH|MK|MN|MT|MW|MZ|"
        r"OK|OL|OM|ON|OP|OQ|OR|OS|OT|OU|OV|OW|OX|OY|OZ)"
        r"[_-]?\d+(?:\.\d+)?)\b",
        raw,
        re.I,
    )
    # Also simpler pattern for classic accessions like V01149, K01711, K03455
    toks2 = re.findall(r"\b([A-Z]{1,2}\d{5,6}(?:\.\d+)?)\b", raw)
    out = []
    seen = set()
    for t in toks + toks2:
        t = t.upper()
        base = t.split(".")[0]
        for v in (t, base):
            if v not in seen:
                seen.add(v)
                out.append(v)
    return out


def load_audit() -> list[dict]:
    rows = []
    with AUDIT_CSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    log = []

    def L(msg: str):
        print(msg, flush=True)
        log.append(msg)

    L("=== P3 GenBank metadata mining pilot ===")
    L(f"Started: {datetime.now().isoformat(timespec='seconds')}")

    # --- M0 base count ---
    L(f"M0 base query: {BASE_QUERY}")
    base_count = esearch_count(BASE_QUERY)
    L(f"M0 Count = {base_count}")

    # --- Fast esearch prevalence ---
    queries = {
        "culture_cell": f"({BASE_QUERY}) AND ({CULTURE_CLAUSE})",
        "cpe": f"({BASE_QUERY}) AND ({CPE_CLAUSE})",
        "passage": f"({BASE_QUERY}) AND ({PASSAGE_CLAUSE})",
        "clinical": f"({BASE_QUERY}) AND ({CLINICAL_CLAUSE})",
        "culture_and_clinical": (
            f"({BASE_QUERY}) AND ({CULTURE_CLAUSE}) AND ({CLINICAL_CLAUSE})"
        ),
        "clinical_not_culture": (
            f"({BASE_QUERY}) AND ({CLINICAL_CLAUSE}) NOT ({CULTURE_CLAUSE})"
        ),
    }
    esearch_counts = {"base": base_count}
    for name, term in queries.items():
        c = esearch_count(term)
        esearch_counts[name] = c
        pct = 100.0 * c / base_count if base_count else 0.0
        L(f"esearch {name}: {c} ({pct:.2f}% of base)")

    # --- Sample IDs ---
    L(f"Fetching sample UIDs (target {SAMPLE_TARGET})...")
    ids, sample_note = esearch_all_or_sample(BASE_QUERY, base_count, SAMPLE_TARGET)
    L(f"Sample: {sample_note}")

    # --- efetch + parse ---
    rows_out = []
    parse_errors = 0
    for i in range(0, len(ids), EFETCH_BATCH):
        batch = ids[i : i + EFETCH_BATCH]
        L(f"efetch batch {i // EFETCH_BATCH + 1}: {len(batch)} IDs "
          f"({i + len(batch)}/{len(ids)})")
        try:
            gb_text = efetch_gb(batch)
        except Exception as e:
            L(f"  ERROR efetch: {e}")
            parse_errors += len(batch)
            continue
        records = split_gb_records(gb_text)
        L(f"  got {len(records)} LOCUS records")
        for gb in records:
            meta = metadata_only(gb)
            acc, ver = parse_accession(meta)
            definition = extract_field(meta, "DEFINITION")
            comment = extract_field(meta, "COMMENT")
            source_feat = extract_source_features(meta)
            organism = parse_organism(meta)
            year = parse_year(meta)
            blob = "\n".join([definition, comment, source_feat, meta[:3000]])
            flags = flag_keywords(blob)
            rows_out.append(
                {
                    "accession": acc,
                    "version": ver,
                    "uid": "",
                    "organism": organism,
                    "year": year,
                    "definition": definition[:500],
                    "culture_cell": int(flags["culture_cell"]),
                    "cpe": int(flags["cpe"]),
                    "passage": int(flags["passage"]),
                    "clinical": int(flags["clinical"]),
                    "clinical_no_culture": int(
                        flags["clinical"] and not flags["culture_cell"]
                    ),
                }
            )

    # Map UIDs if possible (optional)
    csv_path = OUT / "refseq_viral_complete_metadata_sample.csv"
    fieldnames = [
        "accession", "version", "uid", "organism", "year", "definition",
        "culture_cell", "cpe", "passage", "clinical", "clinical_no_culture",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_out)
    L(f"Wrote {csv_path} n={len(rows_out)}")

    n = len(rows_out) or 1
    sample_stats = {
        "n": len(rows_out),
        "culture_cell": sum(r["culture_cell"] for r in rows_out),
        "cpe": sum(r["cpe"] for r in rows_out),
        "passage": sum(r["passage"] for r in rows_out),
        "clinical": sum(r["clinical"] for r in rows_out),
        "clinical_no_culture": sum(r["clinical_no_culture"] for r in rows_out),
    }
    for k in ("culture_cell", "cpe", "passage", "clinical", "clinical_no_culture"):
        sample_stats[f"{k}_pct"] = 100.0 * sample_stats[k] / len(rows_out) if rows_out else 0.0

    # M3 by year
    by_year = defaultdict(lambda: {"n": 0, "culture": 0, "cpe": 0})
    for r in rows_out:
        y = r["year"] or "unknown"
        by_year[y]["n"] += 1
        by_year[y]["culture"] += r["culture_cell"]
        by_year[y]["cpe"] += r["cpe"]
    m3 = {
        y: {
            "n": v["n"],
            "culture_pct": round(100.0 * v["culture"] / v["n"], 2) if v["n"] else 0,
            "cpe_pct": round(100.0 * v["cpe"] / v["n"], 2) if v["n"] else 0,
        }
        for y, v in sorted(by_year.items())
    }

    # M4 by organism (top)
    by_org = defaultdict(lambda: {"n": 0, "culture": 0, "cpe": 0})
    for r in rows_out:
        org = r["organism"] or "unknown"
        by_org[org]["n"] += 1
        by_org[org]["culture"] += r["culture_cell"]
        by_org[org]["cpe"] += r["cpe"]
    top_orgs = sorted(by_org.items(), key=lambda x: -x[1]["n"])[:30]
    m4 = {
        org: {
            "n": v["n"],
            "culture_pct": round(100.0 * v["culture"] / v["n"], 2) if v["n"] else 0,
            "cpe_pct": round(100.0 * v["cpe"] / v["n"], 2) if v["n"] else 0,
        }
        for org, v in top_orgs
    }

    # --- M6 / M7 audit ---
    audit = load_audit()
    sample_accs = set()
    for r in rows_out:
        if r["accession"]:
            sample_accs.add(r["accession"].upper().split(".")[0])
        if r["version"]:
            sample_accs.add(r["version"].upper())
            sample_accs.add(r["version"].upper().split(".")[0])

    high_rows = [a for a in audit if a.get("risk_path", "").lower() == "high"]
    low_rows = [a for a in audit if a.get("risk_path", "").lower() == "low"]

    def collect_audit_accessions(rows: list[dict]) -> list[tuple[dict, list[str]]]:
        out = []
        for a in rows:
            accs = accession_variants(a.get("ictv_refseq_accession", "") + " " + a.get("entered_public_db", ""))
            out.append((a, accs))
        return out

    high_acc_pairs = collect_audit_accessions(high_rows)
    low_acc_pairs = collect_audit_accessions(low_rows)

    # Fetch metadata for audit accessions not necessarily in sample
    all_audit_accs = []
    for _, accs in high_acc_pairs + low_acc_pairs:
        for a in accs:
            if re.match(r"^(NC|AC|NG|NM|NR|NZ|NW|AP|BK|AY|JX|JN|K|V|X|U|DQ|EF|EU|FJ|GQ|GU|HM|HQ|JF|JQ|KC|KF|KJ|KM|KP|KR|KT|KU|KX|KY|KZ|LC|MF|MG|MH|MK|MN|MT|MW|MZ|OK|OL|OM|ON|OP|OQ|OR)\d", a, re.I) or re.match(r"^[A-Z]{1,2}\d{5,}", a):
                all_audit_accs.append(a)
    # Prefer versioned RefSeq-like
    unique_fetch = []
    seen_f = set()
    for a in all_audit_accs:
        base = a.split(".")[0].upper()
        if base in seen_f:
            continue
        # Prefer NC_/AC_ style
        seen_f.add(base)
        unique_fetch.append(a)

    L(f"M6/M7: fetching {len(unique_fetch)} unique audit accessions...")
    audit_parse = {}  # base_acc -> flags dict
    for i in range(0, len(unique_fetch), 20):
        batch = unique_fetch[i : i + 20]
        L(f"  audit efetch {i // 20 + 1}: {batch[:5]}...")
        try:
            gb_text = efetch_gb(batch)
        except Exception as e:
            L(f"  audit efetch error: {e}")
            continue
        for gb in split_gb_records(gb_text):
            meta = metadata_only(gb)
            acc, ver = parse_accession(meta)
            blob = "\n".join([
                extract_field(meta, "DEFINITION"),
                extract_field(meta, "COMMENT"),
                extract_source_features(meta),
                meta[:3000],
            ])
            flags = flag_keywords(blob)
            base = (acc or ver or "").upper().split(".")[0]
            if base:
                audit_parse[base] = {
                    "accession": acc,
                    "version": ver,
                    "organism": parse_organism(meta),
                    **{k: int(v) for k, v in flags.items()},
                    "definition": extract_field(meta, "DEFINITION")[:300],
                }

    def score_audit_row(a: dict, accs: list[str]) -> dict:
        in_sample = False
        hits = None
        matched = None
        for acc in accs:
            base = acc.upper().split(".")[0]
            if base in sample_accs or acc.upper() in sample_accs:
                in_sample = True
            if base in audit_parse:
                hits = audit_parse[base]
                matched = base
                break
            # try without underscore variants
            if base.replace("_", "") in audit_parse:
                hits = audit_parse[base.replace("_", "")]
                matched = base
                break
        return {
            "audit_id": a.get("audit_id"),
            "virus": a.get("virus_name_species"),
            "risk_path": a.get("risk_path"),
            "accessions_queried": accs[:8],
            "matched_accession": matched,
            "in_sample": in_sample,
            "culture_cell": hits["culture_cell"] if hits else None,
            "cpe": hits["cpe"] if hits else None,
            "passage": hits["passage"] if hits else None,
            "clinical": hits["clinical"] if hits else None,
            "fetch_ok": hits is not None,
        }

    m6_detail = [score_audit_row(a, accs) for a, accs in high_acc_pairs]
    m7_detail = [score_audit_row(a, accs) for a, accs in low_acc_pairs]

    m6_in_sample = sum(1 for d in m6_detail if d["in_sample"])
    m6_culture = sum(1 for d in m6_detail if d["culture_cell"] == 1)
    m6_cpe = sum(1 for d in m6_detail if d["cpe"] == 1)
    m6_fetched = sum(1 for d in m6_detail if d["fetch_ok"])

    m7_culture = sum(1 for d in m7_detail if d["culture_cell"] == 1)
    m7_fetched = sum(1 for d in m7_detail if d["fetch_ok"])

    summary = {
        "pilot_date": "2026-09-19",
        "tool": TOOL,
        "email": EMAIL,
        "base_query": BASE_QUERY,
        "M0_base_count": base_count,
        "esearch_counts": esearch_counts,
        "esearch_pct_of_base": {
            k: round(100.0 * v / base_count, 3) if base_count else 0
            for k, v in esearch_counts.items()
            if k != "base"
        },
        "sample": {
            "n": len(rows_out),
            "note": sample_note,
            "target": SAMPLE_TARGET,
            "parse_errors_batches": parse_errors,
            "stats": sample_stats,
        },
        "M1": {
            "esearch_culture_pct": round(
                100.0 * esearch_counts["culture_cell"] / base_count, 3
            ),
            "sample_culture_pct": round(sample_stats["culture_cell_pct"], 3),
        },
        "M2": {
            "esearch_cpe_pct": round(100.0 * esearch_counts["cpe"] / base_count, 3),
            "sample_cpe_pct": round(sample_stats["cpe_pct"], 3),
        },
        "M3_by_year": m3,
        "M4_top_organisms": m4,
        "M5": {
            "esearch_clinical_pct": round(
                100.0 * esearch_counts["clinical"] / base_count, 3
            ),
            "esearch_clinical_not_culture_pct": round(
                100.0 * esearch_counts["clinical_not_culture"] / base_count, 3
            ),
            "esearch_culture_and_clinical_pct": round(
                100.0 * esearch_counts["culture_and_clinical"] / base_count, 3
            ),
            "sample_clinical_no_culture_pct": round(
                sample_stats["clinical_no_culture_pct"], 3
            ),
        },
        "M6_high_risk_audit": {
            "n_high": len(high_rows),
            "fetched": m6_fetched,
            "in_sample": m6_in_sample,
            "culture_keyword_hits": m6_culture,
            "cpe_keyword_hits": m6_cpe,
            "detail": m6_detail,
        },
        "M7_low_risk_audit": {
            "n_low": len(low_rows),
            "fetched": m7_fetched,
            "culture_keyword_hits": m7_culture,
            "detail": m7_detail,
        },
        "guardrails": [
            "Metrics phrase as mention of culture/CPE in metadata, NOT culture artifacts.",
            "Under-annotation: absence of keywords ≠ absence of culture.",
            "No claim that entire GenBank/RefSeq viral corpus is non-viral.",
        ],
    }

    json_path = OUT / "mining_summary.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    L(f"Wrote {json_path}")

    # Results markdown
    md_path = OUT / "P3_genbank_mining_results_2026-09-19.md"
    lines = []
    lines.append("# P3 GenBank/RefSeq metadata mining — pilot results")
    lines.append("")
    lines.append("**Date:** 2026-09-19 (America/Toronto)")
    lines.append("**Scope:** RefSeq viral complete genomes — catalog-card metadata only (no sequence re-analysis).")
    lines.append(f"**Base query:** `{BASE_QUERY}`")
    lines.append(f"**M0 Count:** **{base_count}**")
    lines.append(f"**Sample n:** {len(rows_out)} ({sample_note})")
    lines.append("")
    lines.append("## Guardrails (read first)")
    lines.append("")
    lines.append("- Results estimate how often records **mention** culture/CPE language in metadata — **not** that they “are culture artifacts.”")
    lines.append("- **Under-annotation:** missing keywords do not prove a clinical-only path.")
    lines.append("- This pilot does **not** claim the entire GenBank/RefSeq viral corpus is non-viral.")
    lines.append("")
    lines.append("## Fast esearch prevalence (full base set)")
    lines.append("")
    lines.append("| Slice | Count | % of M0 |")
    lines.append("|-------|------:|--------:|")
    for k in ("culture_cell", "cpe", "passage", "clinical", "culture_and_clinical", "clinical_not_culture"):
        c = esearch_counts[k]
        pct = 100.0 * c / base_count if base_count else 0
        lines.append(f"| {k} | {c} | {pct:.2f}% |")
    lines.append("")
    lines.append("## Sampled deep parse")
    lines.append("")
    lines.append(f"Parsed metadata for **{len(rows_out)}** records → `refseq_viral_complete_metadata_sample.csv`.")
    lines.append("")
    lines.append("| Flag | n | % of sample |")
    lines.append("|------|--:|-----------:|")
    for k in ("culture_cell", "cpe", "passage", "clinical", "clinical_no_culture"):
        lines.append(
            f"| {k} | {sample_stats[k]} | {sample_stats[k + '_pct']:.2f}% |"
        )
    lines.append("")
    lines.append("### M1 — culture-cell keywords")
    lines.append("")
    lines.append(
        f"- **Esearch:** {summary['M1']['esearch_culture_pct']:.2f}% of base "
        f"({esearch_counts['culture_cell']}/{base_count})"
    )
    lines.append(
        f"- **Sample parse:** {summary['M1']['sample_culture_pct']:.2f}% "
        f"({sample_stats['culture_cell']}/{len(rows_out)})"
    )
    lines.append("")
    lines.append("### M2 — CPE / cytopathic language")
    lines.append("")
    lines.append(
        f"- **Esearch:** {summary['M2']['esearch_cpe_pct']:.2f}% of base "
        f"({esearch_counts['cpe']}/{base_count})"
    )
    lines.append(
        f"- **Sample parse:** {summary['M2']['sample_cpe_pct']:.2f}% "
        f"({sample_stats['cpe']}/{len(rows_out)})"
    )
    lines.append("")
    lines.append("### M3 — by year (sample)")
    lines.append("")
    lines.append("| Year | n | culture % | CPE % |")
    lines.append("|------|--:|----------:|------:|")
    for y, v in m3.items():
        if y == "unknown" or (y.isdigit() and 1980 <= int(y) <= 2026):
            lines.append(f"| {y} | {v['n']} | {v['culture_pct']} | {v['cpe_pct']} |")
    lines.append("")
    lines.append("### M4 — top organisms in sample (by count)")
    lines.append("")
    lines.append("| Organism | n | culture % | CPE % |")
    lines.append("|----------|--:|----------:|------:|")
    for org, v in list(m4.items())[:20]:
        lines.append(f"| {org} | {v['n']} | {v['culture_pct']} | {v['cpe_pct']} |")
    lines.append("")
    lines.append("### M5 — clinical-looking without culture keywords")
    lines.append("")
    lines.append(
        f"- **Esearch clinical NOT culture:** {summary['M5']['esearch_clinical_not_culture_pct']:.2f}% "
        f"({esearch_counts['clinical_not_culture']}/{base_count})"
    )
    lines.append(
        f"- **Esearch clinical ∩ culture:** {summary['M5']['esearch_culture_and_clinical_pct']:.2f}% "
        f"({esearch_counts['culture_and_clinical']}/{base_count})"
    )
    lines.append(
        f"- **Sample clinical ∧ ¬culture:** {summary['M5']['sample_clinical_no_culture_pct']:.2f}% "
        f"({sample_stats['clinical_no_culture']}/{len(rows_out)})"
    )
    lines.append("")
    lines.append("### M6 — type-strain audit high-risk vs keywords")
    lines.append("")
    lines.append(
        f"High-risk audit rows: {len(high_rows)}; successfully fetched: {m6_fetched}; "
        f"also in RefSeq complete-genome sample: {m6_in_sample}."
    )
    lines.append(
        f"Of fetched high-risk: **{m6_culture}** mention culture-cell keywords; "
        f"**{m6_cpe}** mention CPE language."
    )
    lines.append("")
    lines.append("| audit_id | virus | matched | culture | CPE | in_sample |")
    lines.append("|----------|-------|---------|--------:|----:|:---------:|")
    for d in m6_detail:
        lines.append(
            f"| {d['audit_id']} | {(d['virus'] or '')[:40]} | {d['matched_accession'] or '—'} | "
            f"{d['culture_cell'] if d['culture_cell'] is not None else '—'} | "
            f"{d['cpe'] if d['cpe'] is not None else '—'} | {'Y' if d['in_sample'] else 'N'} |"
        )
    lines.append("")
    lines.append("### M7 — low-risk audit vs culture keywords")
    lines.append("")
    lines.append(
        f"Low-risk rows: {len(low_rows)}; fetched: {m7_fetched}; "
        f"with culture keywords: **{m7_culture}** (annotation noise / dual-path flag)."
    )
    lines.append("")
    lines.append("| audit_id | virus | matched | culture | CPE |")
    lines.append("|----------|-------|---------|--------:|----:|")
    for d in m7_detail:
        lines.append(
            f"| {d['audit_id']} | {(d['virus'] or '')[:40]} | {d['matched_accession'] or '—'} | "
            f"{d['culture_cell'] if d['culture_cell'] is not None else '—'} | "
            f"{d['cpe'] if d['cpe'] is not None else '—'} |"
        )
    lines.append("")
    lines.append("## Files")
    lines.append("")
    lines.append("- `mining_summary.json` — machine-readable aggregates")
    lines.append("- `refseq_viral_complete_metadata_sample.csv` — one row per sampled accession")
    lines.append("- `run_pilot.py` — reproducible runner")
    lines.append("- `run_log.txt` — console log")
    lines.append("")
    lines.append("*Pilot only — metadata mentions, not particle identity.*")
    md_path.write_text("\n".join(lines), encoding="utf-8")
    L(f"Wrote {md_path}")

    (OUT / "run_log.txt").write_text("\n".join(log), encoding="utf-8")
    L("DONE")
    return summary


if __name__ == "__main__":
    main()
