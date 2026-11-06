# -*- coding: utf-8 -*-
"""
Consolidate R1 isolation-practice corpus into a single canonical CSV:
    r1_isolation_standards_and_practice/isolation-refs.csv

Reads the source-of-truth expanded CSV and normalizes columns, adds:
  - DOI  (blank where not yet verified; DOIs are NEVER guessed)
  - fbs_coded (yes/no: are BOTH pre- and post-inoculation FBS% populated
               with a usable value, incl. explicit "0").

Input:  expansion/isolation-refs-overview_expanded.csv
Output: isolation-refs.csv  (also emits a short report to stdout)
"""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # r1_isolation_standards_and_practice/
SRC = os.path.join(ROOT, "expansion", "isolation-refs-overview_expanded.csv")
DST = os.path.join(ROOT, "isolation-refs.csv")

# Canonical column order for agent-friendly output.
COLS = [
    "ID", "year", "virus", "cells", "base_medium",
    "FBS_pre_inoculation", "FBS_post_inoculation",
    "penicillin_IU_ml", "streptomycin_mg_ml", "amphotericin_mg_ml",
    "link", "DOI", "access", "fbs_coded", "source_batch",
    "notes", "quote_pre", "quote_post",
]

def is_fbs_value(v):
    """Return True if the cell holds a usable numeric FBS value (incl 0)."""
    if v is None:
        return False
    s = v.strip()
    if not s or s in ("-", "^^", "--"):
        return False
    # anything that starts with a digit or a bare 0 is treated as coded
    return bool(re.match(r"\d", s))

def main():
    with open(SRC, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        src_fields = reader.fieldnames
        rows = list(reader)

    def get(r, *names):
        for n in names:
            if n in r and r[n] is not None:
                return r[n]
        return ""

    out = []
    for r in rows:
        pre = get(r, "FBS% pre-inoculation", "FBS% pre-inculcation")
        post = get(r, "FBS% post-inculcation", "FBS% post-inoculation")
        coded = "yes" if (is_fbs_value(pre) and is_fbs_value(post)) else "no"
        row = {
            "ID": get(r, "ID"),
            "year": get(r, "year"),
            "virus": get(r, "virus"),
            "cells": get(r, "cells*", "cells"),
            "base_medium": get(r, "Base Medium", "base medium"),
            "FBS_pre_inoculation": pre,
            "FBS_post_inoculation": post,
            "penicillin_IU_ml": get(r, "penicillin (IU/ml)"),
            "streptomycin_mg_ml": get(r, "streptomycin (mg/ml)"),
            "amphotericin_mg_ml": get(r, "amphotericin (mg/ml)"),
            "link": get(r, "link"),
            "DOI": "",   # blank; DOI resolution is a separate, verified task
            "access": get(r, "access"),
            "fbs_coded": coded,
            "source_batch": get(r, "source_batch"),
            "notes": get(r, "notes"),
            "quote_pre": get(r, "quote_pre"),
            "quote_post": get(r, "quote_post"),
        }
        out.append(row)

    with open(DST, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, lineterminator="\n")
        w.writeheader()
        for row in out:
            w.writerow(row)

    coded = sum(1 for r in out if r["fbs_coded"] == "yes")
    print(f"wrote {DST}")
    print(f"rows: {len(out)} | fbs_coded=yes: {coded} | fbs_coded=no: {len(out)-coded}")
    print(f"source fields detected: {src_fields}")

if __name__ == "__main__":
    main()