#!/usr/bin/env python3
"""Extract candidate control-outcome passages for re-passing nc_cpe_code.

For each paper with an Isolation-stage NC (nc_isolation_stage=yes), pull the
paper's own description of its no-virus control (control / mock / uninoculated /
uninfected / negative control) so a human can classify the control's morphology
against the protocol descriptor set (CLSI M41 Table 7 + ASM CPE theory).

Writes wrk/nc_cpe_evidence_review.txt (one block per paper) for hand review.
This script only extracts candidate text; it does not assign codes.
"""
from __future__ import annotations
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OV = REPO / "r2_negative_controls" / "control-cultures-overview.csv"
REFDIR = REPO / "r1_isolation_standards_and_practice" / "refs" / "isolation_practice"
OUT = Path(__file__).resolve().parent / "nc_cpe_evidence_review.txt"

import csv

# control-marker terms
CTRL_RE = re.compile(
    r"(?i)\b(controls?|mock|uninoculat\w*|uninfect\w*|negative control|"
    r"non[- ]?inoculat\w*|cell control|normal control|blank)\b"
)
# descriptor / CPE-outcome terms
DESC_RE = re.compile(
    r"(?i)\b(cytopathic|CPE|round(ed|ing)?|refractil\w*|syncyti\w*|vacuol\w*|"
    r"detach\w*|granular\w*|strand\w*|degenerat\w*|balloon\w*|enlarg\w*|pykno\w*|"
    r"normal|healthy|intact|confluen\w*|unremarkable)\b"
)


def find_pdf(pid: str):
    """Locate the PDF for a paper id, tolerant of filename variants."""
    for cand in REFDIR.glob(f"{pid}*"):
        if cand.suffix.lower() == ".pdf":
            return cand
    # fall back to any file whose name starts with the id (e.g. "VI13 - ...pdf")
    for cand in REFDIR.glob(f"{pid}*"):
        if cand.suffix.lower() in (".pdf", ".txt", ".md"):
            return cand
    return None


def text_of(pid: str, pdf: Path):
    """Prefer an existing _txt extract; else extract from the PDF with pymupdf."""
    # existing extract files
    for cand in [
        REFDIR / "_txt" / f"{pid}_extract.md",
        REFDIR / "_txt" / f"{pid} - " + pdf.stem if False else None,
    ]:
        if cand is None:
            continue
    # try _txt folder for any file starting with pid
    txt_dir = REFDIR / "_txt"
    if txt_dir.exists():
        for cand in txt_dir.glob(f"{pid}*"):
            if cand.suffix.lower() in (".md", ".txt"):
                t = cand.read_text(encoding="utf-8", errors="replace")
                if len(t.strip()) > 200:
                    return t, cand.name
    # fall back to extracting the PDF
    try:
        import pymupdf  # noqa: F401
        doc = pymupdf.open(str(pdf))
        return "".join(p.get_text() for p in doc), pdf.name
    except Exception as e:
        return "", f"<extract failed: {e}>"


def sentences(txt: str):
    # crude sentence split
    t = re.sub(r"\s+", " ", txt)
    return re.split(r"(?<=[.;:!?])\s+", t)


def main():
    with OV.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    ids = sorted(
        {r["id"].upper() for r in rows
         if r.get("r2_universe", "") == "yes" and r.get("nc_isolation_stage", "") == "yes"},
        key=lambda s: (int(re.sub(r"\D", "", s) or 0), s),
    )

    blocks = []
    for pid in ids:
        pdf = find_pdf(pid)
        if pdf is None:
            blocks.append(f"===== {pid} =====\n<no PDF found>\n")
            continue
        txt, src = text_of(pid, pdf)
        if not txt:
            blocks.append(f"===== {pid} =====  (src {src})\n<empty text>\n")
            continue
        # rank sentences: prefer those mentioning a control marker AND a descriptor/CRE outcome
        sents = sentences(txt)
        hits = []
        for s in sents:
            cm = CTRL_RE.search(s)
            dm = DESC_RE.search(s)
            if cm and dm:
                hits.append((2, s))
            elif cm:
                hits.append((1, s))
        hits.sort(key=lambda x: -x[0])
        seen = set()
        kept = []
        for prio, s in hits:
            if s in seen or len(s) < 12:
                continue
            seen.add(s)
            kept.append(f"[{prio}] {s[:500]}")
            if len(kept) >= 14:
                break
        blocks.append(
            f"===== {pid} =====  (src {src})\n" + "\n".join(kept) + "\n"
        )

    OUT.write_text("\n".join(blocks), encoding="utf-8")
    print(f"wrote {OUT} with {len(ids)} paper blocks")


if __name__ == "__main__":
    main()
