#!/usr/bin/env python3
"""R2 <- R1 alignment: annotate every R2 overview row with its current-R1 disposition.

Rule: R2 follows R1. R1 `isolation-refs.csv` (category-1) is the single source of truth.
This script does NOT change tiers; it adds three audit columns so downstream statistics
(counts, figures) can be computed over the correct R1-category-1 universe only.

Output columns appended to r2_negative_controls/control-cultures-overview.csv:

    r1_status        cat1 | cat2 | cat3 | dropped
    r1_current_id    canonical current R1 ID (PR###/MR### for moved; same VI### otherwise)
    r2_universe      yes  (In Isolation-practice scoring universe) | no

Disposition sources (all quoted in wrk/r1_r2_reconciliation_2026-11-19.md):
  - R1 destination CSVs scan "ex-VI###" notes (cat2: isolation-protocol-refs.csv; cat3: methods-review-refs.csv)
  - URL identity for VI271 -> PR010
  - R1 `isolation-refs.csv` note markers "[ex-SPT10]" -> VI303
  - R1 duplicate-row consolidation (McSwiggan VI240; Mizuta JJID2008 VI262)
  - genuinely-absent legacy IDs (VI4 HFRS 1983; VI24 AmB influenza) -> dropped

Regenerate:  tools/venv/Scripts/python r2_negative_controls/wrk/r1_r2_align.py
"""
from __future__ import annotations
import re
import csv
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
R1 = REPO / "r1_isolation_standards_and_practice" / "isolation-refs.csv"
PROT = REPO / "r1_isolation_standards_and_practice" / "isolation-protocol-refs.csv"
MR = REPO / "r1_isolation_standards_and_practice" / "methods-review-refs.csv"
OV = REPO / "r2_negative_controls" / "control-cultures-overview.csv"


def read_rows(p: Path) -> list[dict]:
    with p.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def ex_map(path: Path) -> dict[str, str]:
    """Scan a destination CSV's notes for 'ex-VI###' -> current ID."""
    out: dict[str, str] = {}
    for r in read_rows(path):
        m = re.search(r"ex-(VI\d+)", r.get("notes", ""))
        if m:
            out[m.group(1)] = r["ID"]
    return out


def main() -> None:
    r1_rows = read_rows(R1)
    r1_ids = {r["ID"] for r in r1_rows}

    cat2 = ex_map(PROT)  # ex-VI -> PR###
    cat3 = ex_map(MR)    # ex-VI -> MR### / MZ###

    # URL identity fixes + known re-ids + genuine-drop set
    # (each documented in the reconciliation note)
    extra_cat2 = {"VI271": "PR010"}          # CDC vero-slam.html URL match
    rekey = {"SPT10": "VI303"}               # R1 note "[ex-SPT10]"
    merge = {"VI241": "VI240", "VI242": "VI240", "VI263": "VI262"}  # residual R1 consolidation
    dropped = {"VI4", "VI24"}                # absent from current R1

    # map all ex-VI rows that folded under one destination ID (Mizuta 2019 arms VI255..VI261 -> MR001)
    for i in ("VI255", "VI256", "VI257", "VI258", "VI259", "VI260", "VI261"):
        cat3.setdefault(i, "MR001")

    header = None
    rows: list[dict] = []
    with OV.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        header = rd.fieldnames
        rows = list(rd)

    new_rows = []
    seen_cat1 = set()
    for r in rows:
        i = r["id"].upper()

        # resolve current id + status
        if i in cat2 or i in extra_cat2:
            cur = cat2.get(i) or extra_cat2[i]
            status, current, uni = "cat2", cur, "no"
        elif i in cat3:
            current = cat3[i]
            status, uni = "cat3", "no"
        elif i in merge:
            current = merge[i]
            status, uni = "cat1", "no"  # merged duplicate of an in-universe paper
        elif i in rekey:
            current = rekey[i]
            status, uni = "cat1", "yes"
        elif i in dropped:
            status, current, uni = "dropped", "", "no"
        elif i in r1_ids:
            status, current, uni = "cat1", i, "yes"
        else:
            status, current, uni = "unknown", "", "no"

        r["r1_status"] = status
        r["r1_current_id"] = current
        r["r2_universe"] = uni
        new_rows.append(r)

    if header is not None:
        new_header = list(header) + ["r1_status", "r1_current_id", "r2_universe"]
    with OV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=new_header)
        w.writeheader()
        for r in new_rows:
            w.writerow({k: r.get(k, "") for k in new_header})

    uni = [r for r in new_rows if r["r2_universe"] == "yes"]
    from collections import Counter
    print("rows total:", len(new_rows))
    print("universe yes:", len(uni))
    print("status:", Counter(r["r1_status"] for r in new_rows))
    print("universe tier:", Counter(r["tier"] for r in uni))


if __name__ == "__main__":
    main()
