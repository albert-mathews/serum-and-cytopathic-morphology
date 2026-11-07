#!/usr/bin/env python3
"""Regenerate R2 (Isolation-stage negative-control tier) summary figures.

Reads the scored R2 corpus:
    r2_negative_controls/control-cultures-overview.csv

Writes print-safe grayscale figures + a machine-readable summary into the
target directory (default: this `wrk/viz/`; PNGs are gitignored, this script
is the tracked source):

    r2_fig1_tier_distribution_bar.png    horizontal tier ladder (A..D)
    r2_fig2_tier_distribution_donut.png  donut of the same
    r2_fig3_nc_presence.png              any-NC vs Isolation-stage-NC presence
    r2_fig4_serum_match_ladder.png       serum-match (M3) audit ladder
    r2_summary.txt                       every number used in the figures

Regenerate with:
    python make_figures.py                      # outputs to this directory
    python make_figures.py --outdir ../../tex/figures   # or wherever
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]  # r2_negative_controls/wrk/viz -> repo root
OVERVIEW = REPO / "r2_negative_controls" / "control-cultures-overview.csv"

ORDER = ["A", "B", "C", "D"]
TIER_LABEL = {
    "A": "A  matched Isolation-stage NC (serum included)",
    "B": "B  NC named, conditions not verifiable",
    "C": "C  NC wrong stage and/or explicit mismatch",
    "D": "D  no culture-level NC described",
}


def load() -> list[dict]:
    rows = []
    with OVERVIEW.open(encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            rows.append(r)
    return rows


def counts(rows: list[dict]) -> dict:
    tier = Counter(r["tier"] for r in rows)
    return {
        "n": len(rows),
        "tier": {t: tier.get(t, 0) for t in ORDER},
        "nc_isolation_stage_yes": sum(1 for r in rows if r["nc_isolation_stage"] == "yes"),
        "nc_any_yes": sum(1 for r in rows if r["nc_any"] == "yes"),
        "m3": Counter(r["m3_serum_enrichment"] for r in rows),
        "tier_a_cpe_claimed_negative": Counter(
            r["control_cpe_claimed_negative"] for r in rows if r["tier"] == "A"
        ),
    }


def pct(part: int, total: int) -> str:
    return f"{100 * part / total:.1f}%"


def style_ax(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0)


def _hbar(ax, labels, vals, grays, hatches, value_fmt):
    """Draw top-to-bottom horizontal bars; returns list of (bar, label, value)."""
    y = list(range(len(vals)))[::-1]
    bars = ax.barh(y, vals, color=grays, edgecolor="black",
                   linewidth=0.6, height=0.62)
    for b, h in zip(bars, hatches):
        b.set_hatch(h)
    return bars, labels, vals


def fig1_tier_bar(c: dict, out: Path):
    n = c["n"]
    grays = ["#d8d8d8", "#b0b0b0", "#6f6f6f", "#2b2b2b"]
    hatches = ["", "///", "...", "xxx"]
    labels = [TIER_LABEL[t] for t in ORDER]
    vals = [c["tier"][t] for t in ORDER]

    fig, ax = plt.subplots(figsize=(8.6, 4.4))
    y = list(range(len(vals)))[::-1]
    bars = ax.barh(y, vals, color=grays, edgecolor="black", linewidth=0.6, height=0.66)
    for b, h in zip(bars, hatches):
        b.set_hatch(h)
    for i, b in enumerate(bars):
        ax.text(b.get_width() + 1.0, b.get_y() + b.get_height() / 2,
                f"{vals[i]}  ({pct(vals[i], n)})", va="center", ha="left", fontsize=10)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(0, max(vals) * 1.30)
    ax.set_xlabel("Number of Isolation papers")
    ax.set_title(f"Isolation-stage negative cultures in the scored corpus (n = {n})",
                 fontsize=11, loc="left")
    style_ax(ax)
    fig.tight_layout()
    fig.savefig(out / "r2_fig1_tier_distribution_bar.png", dpi=220)
    plt.close(fig)


def fig2_tier_donut(c: dict, out: Path):
    n = c["n"]
    vals = [c["tier"][t] for t in ORDER]
    grays = ["#d8d8d8", "#b0b0b0", "#6f6f6f", "#2b2b2b"]
    hatches = ["", "///", "...", "xxx"]

    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    wedges, _ = ax.pie(
        vals, startangle=90, counterclock=False, colors=grays,
        wedgeprops=dict(edgecolor="black", linewidth=0.6, width=0.42),
    )
    for w, h in zip(wedges, hatches):
        w.set_hatch(h)

    for i, w in enumerate(wedges):
        ang_deg = (w.theta1 + w.theta2) / 2.0
        ang = np.deg2rad(ang_deg)
        lab = f"{ORDER[i]}: {vals[i]} ({pct(vals[i], n)})"
        ax.annotate(
            lab,
            xy=(np.cos(ang), np.sin(ang)),
            xytext=(1.36 * np.cos(ang), 1.36 * np.sin(ang)),
            ha="center", va="center", fontsize=10,
            arrowprops=dict(arrowstyle="-", lw=0.5, color="0.35"),
        )
    ax.text(0, 0, f"n = {n}", ha="center", va="center", fontsize=13, weight="bold")
    ax.set_title("Negative-control tier distribution", fontsize=11, loc="center")
    fig.tight_layout()
    fig.savefig(out / "r2_fig2_tier_distribution_donut.png", dpi=220)
    plt.close(fig)


def fig3_nc_presence(c: dict, out: Path):
    n = c["n"]
    panels = [
        ("Any culture-level NC", c["nc_any_yes"]),
        ("Isolation-stage NC", c["nc_isolation_stage_yes"]),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.4))
    for ax, (title, p) in zip(axes, panels):
        a = n - p
        vals = [p, a]
        lab = [f"{p}  reported ({pct(p, n)})", f"{a}  not reported ({pct(a, n)})"]
        y = [1, 0]
        bars = ax.barh(y, vals, color=["#6a6a6a", "#cfcfcf"],
                       edgecolor="black", linewidth=0.6, height=0.6)
        bars[0].set_hatch("")
        bars[1].set_hatch("///")
        for i, b in enumerate(bars):
            ax.text(b.get_width() / 2, b.get_y() + b.get_height() / 2,
                    lab[i], va="center", ha="center", fontsize=10)
        ax.set_yticks([])
        ax.set_xlim(0, n * 1.08)
        ax.set_xlabel("Number of papers")
        ax.set_title(title, fontsize=10, loc="left")
        style_ax(ax)
    fig.suptitle(f"Negative-control presence in the R2 corpus (n = {n})",
                 fontsize=11, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(out / "r2_fig3_nc_presence.png", dpi=220)
    plt.close(fig)


def fig4_serum_match(c: dict, out: Path):
    n = c["n"]
    m3 = c["m3"]
    # best (top) -> worst (bottom)
    cats = [
        ("NC serum matched", "yes", m3.get("yes", 0), "#d8d8d8", ""),
        ("NC serum explicitly mismatched", "no", m3.get("no", 0), "#b0b0b0", "..."),
        ("NC serum not verifiable", "unknown", m3.get("unknown", 0), "#6f6f6f", "///"),
        ("No culture-level NC", "NA", m3.get("NA", 0), "#2b2b2b", "xxx"),
    ]
    labels = [f"{name}: {v}  ({pct(v, n)})" for name, _, v, _, _ in cats]
    vals = [v for _, _, v, _, _ in cats]
    grays = [g for _, _, _, g, _ in cats]
    hatches = [h for _, _, _, _, h in cats]

    fig, ax = plt.subplots(figsize=(8.6, 3.2))
    y = list(range(len(vals)))[::-1]
    bars = ax.barh(y, vals, color=grays, edgecolor="black", linewidth=0.6, height=0.62)
    for b, h in zip(bars, hatches):
        b.set_hatch(h)
    for i, b in enumerate(bars):
        ax.text(b.get_width() + 1.0, b.get_y() + b.get_height() / 2,
                labels[i], va="center", ha="left", fontsize=9)
    ax.set_yticks([])
    ax.set_xlim(0, n * 1.22)
    ax.set_xlabel("Number of papers (n = 173)")
    ax.set_title("Serum/enrichment match (M3) of negative cultures — the R2 crux",
                 fontsize=11, loc="left")
    style_ax(ax)
    fig.tight_layout()
    fig.savefig(out / "r2_fig4_serum_match_ladder.png", dpi=220)
    plt.close(fig)


def write_summary(c: dict, out: Path):
    n = c["n"]
    t = c["tier"]
    lines = [
        "R2 negative-control tier summary (scored corpus)",
        f"scored rows (overview): {n}",
    ]
    for k in ORDER:
        lines.append(f"tier {k}: {t[k]} ({pct(t[k], n)})")
    lines.append(f"any culture-level NC: {c['nc_any_yes']} ({pct(c['nc_any_yes'], n)})")
    lines.append(f"Isolation-stage NC: {c['nc_isolation_stage_yes']} "
                 f"({pct(c['nc_isolation_stage_yes'], n)})")
    for k in ("NA", "yes", "unknown", "no"):
        lines.append(f"M3 serum/enrichment = {k}: {c['m3'].get(k, 0)}")
    lines.append("Tier A controls reported CPE in the NC (would falsify specificity): "
                 f"{c['tier_a_cpe_claimed_negative'].get('no', 0)}")
    lines.append("Tier A controls claimed CPE-negative: "
                 f"{c['tier_a_cpe_claimed_negative'].get('yes', 0)}")
    (out / "r2_summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=str(HERE), help="output directory for PNGs + summary")
    args = ap.parse_args()
    out = Path(args.outdir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    c = counts(load())
    fig1_tier_bar(c, out)
    fig2_tier_donut(c, out)
    fig3_nc_presence(c, out)
    fig4_serum_match(c, out)
    write_summary(c, out)
    print("summary:", c)
    print("wrote:", ", ".join(sorted(p.name for p in out.glob("r2_*"))))
    print("outdir:", out)


if __name__ == "__main__":
    main()