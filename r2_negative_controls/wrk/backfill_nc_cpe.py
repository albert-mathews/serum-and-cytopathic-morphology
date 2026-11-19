#!/usr/bin/env python3
"""Backfill negative-control CPE outcome coding (`nc_cpe_code` + free text + quote).

Source of truth for Isolation-stage NC papers = wrk/nc_cpe_assignments.py (ASSIGN),
coded against the protocol descriptor set (control-cultures.md §7.5b).
Papers without an Isolation-stage NC get a blank code (default).

Regenerate after tier re-scoring:  tools/venv/Scripts/python r2_negative_controls/wrk/backfill_nc_cpe.py
"""
from __future__ import annotations
import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nc_cpe_assignments import ASSIGN, OTHER  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
OV = REPO / "r2_negative_controls" / "control-cultures-overview.csv"


def default_code(r: dict) -> str:
    if r.get("nc_isolation_stage", "") != "yes":
        return ""  # no Isolation-stage culture NC (Tier D / C-stage)
    # fallback only if a nc_isolation_stage=yes paper is missing from ASSIGN
    if r.get("control_cpe_claimed_negative", "") == "yes":
        return "2"
    if r.get("control_cpe_claimed_negative", "") == "partial":
        return "3"
    if r.get("control_cpe_reported", "") in ("no", "unknown"):
        return "4"
    return "3"


def main():
    with OV.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        header = list(rd.fieldnames)
        rows = list(rd)

    for c in ("nc_cpe_code", "nc_cpe_free", "nc_cpe_quote", "nc_other_endpoint"):
        if c not in header:
            header.append(c)

    for r in rows:
        i = r["id"].upper()
        if i in ASSIGN:
            code, free, quote = ASSIGN[i]
            r["nc_cpe_code"] = code
            r["nc_cpe_free"] = free
            r["nc_cpe_quote"] = quote
            r["nc_other_endpoint"] = OTHER.get(i, "")
        else:
            r["nc_cpe_code"] = default_code(r)
            r.setdefault("nc_cpe_free", "")
            r.setdefault("nc_cpe_quote", "")
            r.setdefault("nc_other_endpoint", "")

    with OV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=header)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in header})

    by_tier = {}
    for r in rows:
        if r.get("r2_universe", "yes") != "yes":
            continue
        by_tier.setdefault(r["tier"], Counter())[r["nc_cpe_code"]] += 1
    print("nc_cpe_code x tier (universe=yes):")
    for t in ("A", "B", "C", "D"):
        print(f"  {t}: {dict(by_tier.get(t, Counter()))}")
    code1 = [r["id"] for r in rows if r.get("nc_cpe_code") == "1" and r.get("r2_universe", "yes") == "yes"]
    print("code-1 (virus-independent CPE in the control) instances:", code1)


if __name__ == "__main__":
    main()
