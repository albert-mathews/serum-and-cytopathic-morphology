#!/usr/bin/env python3
"""
R1 FBS% pre/post inoculation — normalized distribution charts.

Ingests:
  - isolation-refs-dual-fbs_only.csv  (practice papers)
  - institution-guideline-protocol-refs.csv  (guidelines; APHIS VIRPRO excluded)

Outputs several styled PNGs for visual iteration.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import pandas as pd
from scipy import stats

# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

RANGE_RE = re.compile(
    r"(?P<a>\d+(?:\.\d+)?)\s*[-–—to]+\s*(?P<b>\d+(?:\.\d+)?)",
    re.I,
)
TYPICALLY_RE = re.compile(r"typically\s*(?P<t>\d+(?:\.\d+)?)", re.I)
NUM_RE = re.compile(r"(?<![A-Za-z])(\d+(?:\.\d+)?)\s*%?")


def parse_fbs(value) -> float | None:
    """Parse an FBS% cell to a single float for density estimation.

    Prefer 'typically X' when present; else midpoint of a–b range; else first plausible %.
    Reject year-like tokens (e.g. 'Cardoso 2000') and values outside 0–30%.
    """
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return None
    s = str(value).strip()
    if not s or s in {"-", "?", "n/a", "N/A", "."}:
        return None
    # strip footnote junk / citation years in parentheses
    s = s.replace("**", "").replace("~", "")
    s = re.sub(r"\(ref\.[^)]*\)", " ", s, flags=re.I)
    s = re.sub(r"\b(19|20)\d{2}\b", " ", s)  # drop years
    m = TYPICALLY_RE.search(s)
    if m:
        v = float(m.group("t"))
        return v if 0 <= v <= 30 else None
    m = RANGE_RE.search(s)
    if m:
        a, b = float(m.group("a")), float(m.group("b"))
        if 0 <= a <= 30 and 0 <= b <= 30:
            return (a + b) / 2.0
    nums = [float(x) for x in NUM_RE.findall(s)]
    nums = [x for x in nums if 0 <= x <= 30]
    if not nums:
        return None
    return nums[0]


def load_papers(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    # normalize columns
    cols = {c: c.strip() for c in df.columns}
    df = df.rename(columns=cols)
    pre_c = "FBS% pre-inoculation"
    post_c = "FBS% post-inculcation"  # historical typo in corpus
    if post_c not in df.columns:
        for c in df.columns:
            if "post" in c.lower() and "fbs" in c.lower():
                post_c = c
                break
    df["pre"] = df[pre_c].map(parse_fbs)
    df["post"] = df[post_c].map(parse_fbs)
    df["source"] = "papers"
    df = df.dropna(subset=["pre", "post"], how="any")
    # Hard fence for plot corpus: plausible culture serum percentages only
    return df[(df["pre"] <= 20) & (df["post"] <= 20)].copy()


def load_institutions(path: Path, exclude_aphis: bool = True) -> pd.DataFrame:
    df = pd.read_csv(path)
    cols = {c: c.strip() for c in df.columns}
    df = df.rename(columns=cols)
    name_c = [c for c in df.columns if c.lower().startswith("institution")][0]
    pre_c = [c for c in df.columns if "pre-inoculation" in c.lower()][0]
    post_c = [c for c in df.columns if "post-inoculation" in c.lower()][0]
    if exclude_aphis:
        mask = ~df[name_c].astype(str).str.contains("APHIS|VIRPRO", case=False, na=False)
        df = df.loc[mask].copy()
    df["pre"] = df[pre_c].map(parse_fbs)
    df["post"] = df[post_c].map(parse_fbs)
    df["institution"] = df[name_c]
    df["source"] = "institutions"
    return df.dropna(subset=["pre", "post"], how="any")


# ---------------------------------------------------------------------------
# Density helpers
# ---------------------------------------------------------------------------

def kde_on_grid(values: np.ndarray, grid: np.ndarray, bw_method=None) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if len(values) == 0:
        return np.zeros_like(grid)
    # Singular / near-constant samples (typical for guidelines at 10% and 2%)
    # -> mixture of narrow Gaussians so the chart reads as vertical spines.
    uniq = np.unique(np.round(values, 6))
    std = float(np.std(values, ddof=1)) if len(values) > 1 else 0.0
    if len(values) == 1 or len(uniq) == 1 or std < 1e-6:
        sigma = 0.22 if bw_method is None or isinstance(bw_method, str) else max(float(bw_method), 0.15)
        dens = np.zeros_like(grid, dtype=float)
        for v in values:
            dens += np.exp(-0.5 * ((grid - v) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))
        dens /= len(values)
        return dens
    try:
        kde = stats.gaussian_kde(values, bw_method=bw_method)
        dens = kde(grid)
    except np.linalg.LinAlgError:
        sigma = 0.25
        dens = np.zeros_like(grid, dtype=float)
        for v in values:
            dens += np.exp(-0.5 * ((grid - v) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))
        dens /= len(values)
        return dens
    return np.clip(dens, 0, None)


def annotate_leader(ax, x, y, text, color, xytext, ha="left", rad=0.12):
    ax.annotate(
        text,
        xy=(x, y),
        xytext=xytext,
        textcoords="data",
        ha=ha,
        va="center",
        fontsize=9,
        color=color,
        fontweight="bold",
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=1.35,
            shrinkA=4,
            shrinkB=2,
            mutation_scale=10,
            connectionstyle=f"arc3,rad={rad}",
            alpha=0.9,
        ),
        path_effects=[pe.withStroke(linewidth=3, foreground="white", alpha=0.9)],
        zorder=10,
        clip_on=False,
    )


# Color palette — papers warm, institutions cool
COLORS = {
    "papers_pre": "#C45C26",       # terracotta
    "papers_post": "#E8A838",      # amber
    "inst_pre": "#1F4E79",         # deep navy
    "inst_post": "#2A9D8F",        # teal
}


def style_axes(ax, title: str, xmax: float = 16):
    ax.set_xlim(-0.5, xmax)
    ax.set_xlabel("FBS concentration (%)", fontsize=11)
    ax.set_ylabel("Normalized density", fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.25, linestyle=":")
    ax.set_axisbelow(True)


# ---------------------------------------------------------------------------
# Plot styles
# ---------------------------------------------------------------------------

def plot_style_a_overlapping_kde(papers, inst, out: Path, grid):
    """Overlapping KDEs with fills + leader labels (story plot)."""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=160)
    series = [
        ("papers", "pre", "Isolation papers — growth (pre)", COLORS["papers_pre"], 0.28, "scott"),
        ("papers", "post", "Isolation papers — maintenance (post)", COLORS["papers_post"], 0.28, "scott"),
        ("inst", "pre", "Institutions — growth (pre)", COLORS["inst_pre"], 0.22, 0.35),
        ("inst", "post", "Institutions — maintenance (post)", COLORS["inst_post"], 0.22, 0.35),
    ]
    data = {
        ("papers", "pre"): papers["pre"].to_numpy(),
        ("papers", "post"): papers["post"].to_numpy(),
        ("inst", "pre"): inst["pre"].to_numpy(),
        ("inst", "post"): inst["post"].to_numpy(),
    }
    peaks = {}
    for key_src, key_phase, label, color, alpha, bw in series:
        vals = data[(key_src, key_phase)]
        dens = kde_on_grid(vals, grid, bw_method=bw)
        ax.fill_between(grid, dens, color=color, alpha=alpha, linewidth=0)
        ax.plot(grid, dens, color=color, lw=2.2, label=label)
        peaks[(key_src, key_phase)] = (grid[np.argmax(dens)], dens.max(), color, label)

    style_axes(
        ax,
        "Dual-media practice: FBS% before vs after inoculation\n"
        f"(papers n={len(papers)}; institutions n={len(inst)})",
    )
    # Leader lines to peaks
    annotate_leader(ax, *peaks[("papers", "pre")][:2], "Papers pre\n(growth)", peaks[("papers", "pre")][2],
                    xytext=(peaks[("papers", "pre")][0] + 2.2, peaks[("papers", "pre")][1] * 0.92))
    annotate_leader(ax, *peaks[("papers", "post")][:2], "Papers post\n(maintenance)", peaks[("papers", "post")][2],
                    xytext=(peaks[("papers", "post")][0] + 2.8, peaks[("papers", "post")][1] * 0.75))
    annotate_leader(ax, *peaks[("inst", "pre")][:2], "Institutions pre\n~10%", peaks[("inst", "pre")][2],
                    xytext=(peaks[("inst", "pre")][0] - 3.5, peaks[("inst", "pre")][1] * 0.55), ha="right")
    annotate_leader(ax, *peaks[("inst", "post")][:2], "Institutions post\n~2%", peaks[("inst", "post")][2],
                    xytext=(peaks[("inst", "post")][0] - 2.2, peaks[("inst", "post")][1] * 0.45), ha="right")

    ax.legend(frameon=False, loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_style_b_split_panels(papers, inst, out: Path, grid):
    """Two panels: pre vs post, papers vs guidelines."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 5), dpi=160, sharey=True)
    for ax, phase, title in zip(
        axes,
        ["pre", "post"],
        ["Growth medium (pre-inoculation)", "Maintenance medium (post-inoculation)"],
    ):
        for src, df, color, label, bw, alpha in [
            ("papers", papers, COLORS["papers_pre"] if phase == "pre" else COLORS["papers_post"],
             "Isolation papers", "scott", 0.32),
            ("inst", inst, COLORS["inst_pre"] if phase == "pre" else COLORS["inst_post"],
             "Institutions", 0.35, 0.25),
        ]:
            dens = kde_on_grid(df[phase].to_numpy(), grid, bw_method=bw)
            ax.fill_between(grid, dens, color=color, alpha=alpha)
            ax.plot(grid, dens, color=color, lw=2.3, label=label)
            # rug
            ax.plot(df[phase], np.full(len(df), -0.01 * dens.max()), "|", color=color, alpha=0.45, markersize=8)
        style_axes(ax, title, xmax=16)
        ax.legend(frameon=False, fontsize=9)
        # callout modal value
        vals = papers[phase].to_numpy()
        mode_x = grid[np.argmax(kde_on_grid(vals, grid))]
        ax.axvline(mode_x, color="0.4", ls="--", lw=0.9, alpha=0.5)
        ax.text(mode_x + 0.15, ax.get_ylim()[1] * 0.9 if ax.get_ylim()[1] else 0.1,
                f"paper mode ≈ {mode_x:.0f}%", fontsize=8, color="0.35")
    fig.suptitle("FBS% distributions by culture stage", fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_style_c_hist_kde(papers, inst, out: Path, grid):
    """Histogram (normalized) + KDE overlay — classic stats look."""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=160)
    bins = np.arange(-0.5, 16.5, 1.0)
    for vals, color, label, alpha in [
        (papers["pre"], COLORS["papers_pre"], "Papers pre", 0.35),
        (papers["post"], COLORS["papers_post"], "Papers post", 0.35),
        (inst["pre"], COLORS["inst_pre"], "Guidelines pre", 0.45),
        (inst["post"], COLORS["inst_post"], "Guidelines post", 0.45),
    ]:
        ax.hist(vals, bins=bins, density=True, color=color, alpha=alpha, edgecolor="white", linewidth=0.6, label=label)
        dens = kde_on_grid(vals.to_numpy(), grid, bw_method="scott" if "Papers" in label else 0.4)
        ax.plot(grid, dens, color=color, lw=2.0)
    style_axes(ax, "Normalized histogram + density curves (1% bins)")
    # text boxes with leaders near expected modes
    annotate_leader(ax, 10, ax.get_ylim()[1] * 0.55 if False else 0.25, "Institution/paper\ngrowth ≈ 10%", COLORS["inst_pre"],
                    xytext=(12.5, 0.35))
    annotate_leader(ax, 2, 0.25, "Maintenance\n≈ 2%", COLORS["inst_post"], xytext=(4.5, 0.42))
    ax.legend(frameon=False, loc="upper right", fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_style_d_ridge(papers, inst, out: Path, grid):
    """Ridge / stacked densities for clear separation."""
    fig, axes = plt.subplots(4, 1, figsize=(10, 8), dpi=160, sharex=True)
    rows = [
        (papers["pre"], COLORS["papers_pre"], "Isolation papers — pre (growth)"),
        (papers["post"], COLORS["papers_post"], "Isolation papers — post (maintenance)"),
        (inst["pre"], COLORS["inst_pre"], "Institutions — pre (growth)"),
        (inst["post"], COLORS["inst_post"], "Institutions — post (maintenance)"),
    ]
    for ax, (vals, color, title) in zip(axes, rows):
        dens = kde_on_grid(vals.to_numpy(), grid, bw_method="scott" if "papers" in title.lower() else 0.35)
        ax.fill_between(grid, dens, color=color, alpha=0.4)
        ax.plot(grid, dens, color=color, lw=2.0)
        ax.plot(vals, np.zeros(len(vals)), "o", color=color, ms=4, alpha=0.55)
        ax.set_ylabel("Density", fontsize=9)
        ax.set_title(title, loc="left", fontsize=10, fontweight="bold", color=color)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="y", alpha=0.2, linestyle=":")
        # annotate median
        med = np.median(vals)
        ax.axvline(med, color=color, ls="--", lw=1.0, alpha=0.7)
        ax.text(med + 0.2, dens.max() * 0.7, f"median {med:g}%", fontsize=8, color=color)
    axes[-1].set_xlabel("FBS concentration (%)", fontsize=11)
    axes[-1].set_xlim(-0.5, 16)
    fig.suptitle("Ridge view: each group on its own baseline", fontsize=13, fontweight="bold")
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_style_e_delta_focus(papers, inst, out: Path, grid):
    """Pre vs post on one axis for papers; guidelines as reference spikes + ΔFBS inset."""
    fig = plt.figure(figsize=(11, 6.2), dpi=160)
    ax = fig.add_axes([0.08, 0.12, 0.62, 0.78])
    ax_in = fig.add_axes([0.74, 0.35, 0.22, 0.4])

    for vals, color, label, bw, alpha in [
        (papers["pre"], COLORS["papers_pre"], "Papers pre", "scott", 0.3),
        (papers["post"], COLORS["papers_post"], "Papers post", "scott", 0.3),
    ]:
        dens = kde_on_grid(vals.to_numpy(), grid, bw_method=bw)
        ax.fill_between(grid, dens, color=color, alpha=alpha)
        ax.plot(grid, dens, color=color, lw=2.4, label=label)

    # Guideline reference as thin tall kernels
    for vals, color, label in [
        (inst["pre"], COLORS["inst_pre"], "Institution pre"),
        (inst["post"], COLORS["inst_post"], "Institution post"),
    ]:
        dens = kde_on_grid(vals.to_numpy(), grid, bw_method=0.28)
        ax.plot(grid, dens, color=color, lw=2.0, ls="--", label=label)
        ax.fill_between(grid, dens, color=color, alpha=0.12)

    style_axes(ax, "Practice papers vs institution reference spines")
    annotate_leader(ax, 10, kde_on_grid(papers["pre"].to_numpy(), grid).max() * 0.95,
                    "Growth peak\n~10% FBS", COLORS["papers_pre"], xytext=(12.2, 0.55))
    annotate_leader(ax, 2, kde_on_grid(papers["post"].to_numpy(), grid).max() * 0.9,
                    "Maintenance peak\n~2% FBS", COLORS["papers_post"], xytext=(5.0, 0.48))
    ax.legend(frameon=False, fontsize=8, loc="upper right")

    # Inset: delta = pre - post
    delta = (papers["pre"] - papers["post"]).to_numpy()
    dgrid = np.linspace(-2, 14, 400)
    dd = kde_on_grid(delta, dgrid, bw_method="scott")
    ax_in.fill_between(dgrid, dd, color="#6C63FF", alpha=0.35)
    ax_in.plot(dgrid, dd, color="#6C63FF", lw=1.8)
    ax_in.axvline(np.median(delta), color="#6C63FF", ls="--", lw=1)
    ax_in.set_title("ΔFBS (pre − post)", fontsize=9, fontweight="bold")
    ax_in.set_xlabel("percentage points", fontsize=8)
    ax_in.set_ylabel("density", fontsize=8)
    ax_in.spines["top"].set_visible(False)
    ax_in.spines["right"].set_visible(False)
    ax_in.text(0.05, 0.95, f"median Δ = {np.median(delta):.1f} pp",
               transform=ax_in.transAxes, fontsize=8, va="top")

    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_style_f_overlap_plus_delta(papers, inst, out: Path, grid):
    """Style A overlapping KDEs + leaders, with Style E ΔFBS inset. Uses 'institution' wording.

    Layout tuned to avoid legend/label collisions:
    - legend sits under the main axes
    - leader labels parked in clear regions (not on peaks)
    """
    fig = plt.figure(figsize=(11.4, 7.0), dpi=170)
    # Leave bottom room for legend; right room for inset
    ax = fig.add_axes([0.08, 0.22, 0.60, 0.68])
    ax_in = fig.add_axes([0.73, 0.40, 0.23, 0.38])

    series = [
        ("papers", "pre", "Isolation papers — growth (pre)", COLORS["papers_pre"], 0.28, "scott"),
        ("papers", "post", "Isolation papers — maintenance (post)", COLORS["papers_post"], 0.28, "scott"),
        ("inst", "pre", "Institutions — growth (pre)", COLORS["inst_pre"], 0.22, 0.35),
        ("inst", "post", "Institutions — maintenance (post)", COLORS["inst_post"], 0.22, 0.35),
    ]
    data = {
        ("papers", "pre"): papers["pre"].to_numpy(),
        ("papers", "post"): papers["post"].to_numpy(),
        ("inst", "pre"): inst["pre"].to_numpy(),
        ("inst", "post"): inst["post"].to_numpy(),
    }
    peaks = {}
    handles = []
    labels = []
    for key_src, key_phase, label, color, alpha, bw in series:
        vals = data[(key_src, key_phase)]
        dens = kde_on_grid(vals, grid, bw_method=bw)
        ax.fill_between(grid, dens, color=color, alpha=alpha, linewidth=0)
        (line,) = ax.plot(grid, dens, color=color, lw=2.2, label=label)
        handles.append(line)
        labels.append(label)
        peaks[(key_src, key_phase)] = (float(grid[np.argmax(dens)]), float(dens.max()), color)

    style_axes(
        ax,
        "Dual-media practice: FBS% before vs after inoculation\n"
        f"(papers n={len(papers)}; institutions n={len(inst)})",
    )
    # Raise ylim a bit so labels above peaks have air
    ymax = max(v[1] for v in peaks.values())
    ax.set_ylim(0, ymax * 1.18)

    # Leaders: place text in open space; arrows point to peaks
    # Institutions post (~2%): text higher / right of spine so leader curves downward like the others
    annotate_leader(
        ax, peaks[("inst", "post")][0], peaks[("inst", "post")][1] * 0.96,
        "Institutions post\n~2%", peaks[("inst", "post")][2],
        xytext=(3.2, ymax * 1.08), ha="left", rad=0.18,
    )
    # Institutions pre (~10%): text high, mid-right of peak but left of legend zone
    annotate_leader(
        ax, peaks[("inst", "pre")][0], peaks[("inst", "pre")][1],
        "Institutions pre\n~10%", peaks[("inst", "pre")][2],
        xytext=(12.2, ymax * 1.05), ha="left",
    )
    # Papers post: mid height, between 3–6%
    annotate_leader(
        ax, peaks[("papers", "post")][0], peaks[("papers", "post")][1],
        "Papers post\n(maintenance)", peaks[("papers", "post")][2],
        xytext=(4.6, ymax * 0.55), ha="left",
    )
    # Papers pre: lower-right of 10% peak
    annotate_leader(
        ax, peaks[("papers", "pre")][0], peaks[("papers", "pre")][1],
        "Papers pre\n(growth)", peaks[("papers", "pre")][2],
        xytext=(12.0, ymax * 0.42), ha="left",
    )

    # Legend below main axes — not over curves
    fig.legend(
        handles, labels,
        loc="upper center",
        bbox_to_anchor=(0.38, 0.14),
        ncol=2,
        frameon=False,
        fontsize=8.5,
    )

    delta = (papers["pre"] - papers["post"]).to_numpy()
    dgrid = np.linspace(-2, 14, 400)
    dd = kde_on_grid(delta, dgrid, bw_method="scott")
    ax_in.fill_between(dgrid, dd, color="#6C63FF", alpha=0.35)
    ax_in.plot(dgrid, dd, color="#6C63FF", lw=1.8)
    med = float(np.median(delta))
    ax_in.axvline(med, color="#6C63FF", ls="--", lw=1)
    ax_in.set_title("ΔFBS (pre − post)", fontsize=9, fontweight="bold")
    ax_in.set_xlabel("percentage points", fontsize=8)
    ax_in.set_ylabel("density", fontsize=8)
    ax_in.spines["top"].set_visible(False)
    ax_in.spines["right"].set_visible(False)
    # Put median note under inset title area without covering curve peak
    # Place median note on the right flank of the inset (away from the Δ peak ~8 pp)
    ax_in.text(
        0.98, 0.22, f"median Δ\n= {med:.1f} pp",
        transform=ax_in.transAxes, fontsize=8, va="bottom", ha="right",
        color="#4B45C0",
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9),
    )

    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", type=Path, required=True)
    ap.add_argument("--institutions", type=Path, required=True)
    ap.add_argument("--outdir", type=Path, required=True)
    args = ap.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    papers = load_papers(args.papers)
    inst = load_institutions(args.institutions, exclude_aphis=True)

    summary = args.outdir / "fbs_distribution_summary.txt"
    with summary.open("w", encoding="utf-8") as f:
        f.write(f"papers n={len(papers)}\n")
        f.write(f"  pre:  mean={papers['pre'].mean():.2f} median={papers['pre'].median():.2f}\n")
        f.write(f"  post: mean={papers['post'].mean():.2f} median={papers['post'].median():.2f}\n")
        f.write(f"institutions n={len(inst)} (APHIS VIRPRO excluded)\n")
        f.write(f"  pre:  {inst['pre'].tolist()}  names={inst['institution'].tolist()}\n")
        f.write(f"  post: {inst['post'].tolist()}\n")
        # value counts
        f.write("\nPaper pre value counts:\n")
        f.write(papers["pre"].value_counts().sort_index().to_string() + "\n")
        f.write("\nPaper post value counts:\n")
        f.write(papers["post"].value_counts().sort_index().to_string() + "\n")

    grid = np.linspace(-1, 16, 600)

    outs = [
        ("styleA_overlapping_kde_leaders.png", plot_style_a_overlapping_kde),
        ("styleB_split_pre_post_panels.png", plot_style_b_split_panels),
        ("styleC_histogram_plus_kde.png", plot_style_c_hist_kde),
        ("styleD_ridge_baselines.png", plot_style_d_ridge),
        ("styleE_papers_vs_guideline_spines_delta.png", plot_style_e_delta_focus),
        ("styleF_overlap_plus_delta_institution.png", plot_style_f_overlap_plus_delta),
    ]
    for name, fn in outs:
        path = args.outdir / name
        fn(papers, inst, path, grid)
        print(f"wrote {path}")

    print(f"wrote {summary}")
    print(f"papers={len(papers)} institutions={len(inst)}")


if __name__ == "__main__":
    main()
