#!/usr/bin/env python3
"""Focused outcome-phrase sweep for re-passing nc_cpe_code.

For each Isolation-stage NC paper, search the full text for contiguous control-outcome
phrases and print which are present, so codes 1/2/3/4 can be assigned on explicit wording.
Does not assign codes; reports evidence.
"""
from __future__ import annotations
import csv
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OV = REPO / "r2_negative_controls" / "control-cultures-overview.csv"
REFDIR = REPO / "r1_isolation_standards_and_practice" / "refs" / "isolation_practice"
TXT = REFDIR / "_txt"

# outcome phrases (lowercased); each maps to evidence of control outcome
PHRASES = [
    "no cpe", "no cytopathic", "without cpe", "without cytopathic", "free of cpe",
    "remained normal", "normal morphology", "remained healthy", "remained flat",
    "remained intact", "intact cells", "remained unchanged", "did not show", "did not exhibit",
    "no morphological", "normal cells", "normal control", "normal uninfected",
    "stayed normal", "appeared normal", "cytotoxic", "degenerat", "spontaneous",
    "uninoculated monolayer", "uninfected control", "mock-infected", "mock infected",
    "negative control", "blank control", "control cells remained", "control cells exhibited",
    "exhibited minimal", "age-related", "control group remained",
]


def get_text(pid: str):
    if TXT.exists():
        for cand in TXT.glob(f"{pid}*"):
            if cand.suffix.lower() in (".md", ".txt"):
                t = cand.read_text(encoding="utf-8", errors="replace")
                if len(t.strip()) > 200:
                    return t
    pdf = next(iter(REFDIR.glob(f"{pid}*.pdf")), None)
    if pdf is None:
        return ""
    try:
        import pymupdf
        doc = pymupdf.open(str(pdf))
        return "".join(p.get_text() for p in doc)
    except Exception:
        return ""


def main():
    with OV.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    ids = sorted(
        {r["id"].upper() for r in rows
         if r.get("r2_universe", "") == "yes" and r.get("nc_isolation_stage", "") == "yes"},
        key=lambda s: (int(re.sub(r"\D", "", s) or 0), s),
    )
    lines = []
    for pid in ids:
        t = get_text(pid).lower()
        found = [p for p in PHRASES if p in t]
        lines.append(f"{pid}: " + "; ".join(found) if found else f"{pid}: <none>")
    out = Path(__file__).resolve().parent / "nc_cpe_phrase_sweep.txt"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out} ({len(ids)} papers)")


if __name__ == "__main__":
    main()
