#!/usr/bin/env python3
"""P3 Step 1 — path_score count bar chart (+ optional family stack). Pass 21N."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
EVENTS = HERE / "P3_sequence_origin_events.csv"
OUT_COUNTS = HERE / "P3_step1_path_type_counts_2026-09-21.png"
OUT_FAMILY = HERE / "P3_step1_path_type_by_family_2026-09-21.png"

PATH_ORDER = ["culture_cpe", "culture_no_cpe", "clinical_direct", "other"]
COLORS = {
    "culture_cpe": "#c44e52",
    "culture_no_cpe": "#4c72b0",
    "clinical_direct": "#55a868",
    "other": "#8172b3",
}


def load_closed():
    with EVENTS.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if r.get("chain_status") == "chain_closed"]


def main():
    closed = load_closed()
    counts = Counter(r["path_score"] for r in closed)
    labels = PATH_ORDER
    values = [counts.get(p, 0) for p in labels]
    colors = [COLORS[p] for p in labels]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, values, color=colors, edgecolor="white", linewidth=0.8)
    ax.set_ylabel("Closed events (n)")
    ax.set_xlabel("path_score")
    ax.set_title(
        f"P3 Step 1 path types among chain_closed (n={len(closed)})\n"
        "Documentary coding — not endorsement of isolate=virus"
    )
    ax.set_ylim(0, max(values) * 1.15 if values else 1)
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.5, str(v), ha="center", va="bottom", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT_COUNTS, dpi=150)
    print("wrote", OUT_COUNTS)

    # Optional: stacked bars by family (top families by closed count)
    by_fam = defaultdict(Counter)
    for r in closed:
        by_fam[r["family"]][r["path_score"]] += 1
    fams_sorted = sorted(by_fam.keys(), key=lambda f: sum(by_fam[f].values()), reverse=True)
    # keep readable: top 20 families
    fams = fams_sorted[:20]
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    bottoms = [0] * len(fams)
    for ps in PATH_ORDER:
        vals = [by_fam[f].get(ps, 0) for f in fams]
        ax2.bar(fams, vals, bottom=bottoms, label=ps, color=COLORS[ps])
        bottoms = [b + v for b, v in zip(bottoms, vals)]
    ax2.set_ylabel("Closed events (n)")
    ax2.set_title("P3 Step 1 path types by family (top 20 by closed n)")
    ax2.legend(frameon=False, ncol=2)
    ax2.tick_params(axis="x", rotation=55, labelsize=8)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    fig2.tight_layout()
    fig2.savefig(OUT_FAMILY, dpi=150)
    print("wrote", OUT_FAMILY)


if __name__ == "__main__":
    main()
