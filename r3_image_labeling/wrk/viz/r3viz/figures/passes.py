"""(g1) Pass 1 (free-text mention) -> Pass 2 (checklist mark) per item, per rater and arm;
(g2) summary slopegraph of CPE-type level and B-A gap, Pass 1 vs Pass 2."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from .. import items as I
from ..metrics import boot_ci
from ..style import ARM_COLOR, ARM_SHORT, footer, pending_panel, save, title
from .common import ROW_ITEMS, item_axis


def _p1_raters(cfg, data):
    return [r for r in cfg.raters if r.code in data.pass1 or r.code in data.pass2]


def fig_g1(cfg, data):
    raters = _p1_raters(cfg, data)
    fig, axes = plt.subplots(len(raters), 2, figsize=(10.5, 3.9 * len(raters) + 0.8), squeeze=False, sharex=True)
    for i, r in enumerate(raters):
        p1, p2 = data.pass1.get(r.code), data.pass2.get(r.code)
        for j, arm in enumerate(("A", "B")):
            ax = axes[i, j]
            ypos = item_axis(ax, labels=(j == 0))
            c = ARM_COLOR[arm]
            for k in ROW_ITEMS:
                y = ypos[k]
                v1 = p1.loc[p1.arm == arm, f"p1_{k}"].mean() if p1 is not None else None
                v2 = p2.loc[p2.arm == arm, f"hit_{k}"].mean() if p2 is not None else None
                if v1 is not None and v2 is not None:
                    ax.annotate("", xy=(v2, y), xytext=(v1, y),
                                arrowprops=dict(arrowstyle="-|>", color=c, lw=1.6, alpha=0.75, shrinkA=4, shrinkB=4))
                if v1 is not None:
                    ax.plot(v1, y, "o", mfc="white", mec=c, mew=1.8, ms=7, zorder=3)
                if v2 is not None:
                    ax.plot(v2, y, "s", color=c, ms=7, zorder=3)
            ax.set_xlim(-0.04, 1.04); ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "50%", "100%"])
            ax.grid(axis="x", color="#EEEEEE"); ax.set_axisbelow(True)
            n1 = data.ntag(p1, r.code) if p1 is not None else "Pass 1: none"
            n2 = data.ntag(p2, r.code) if p2 is not None else "PENDING"
            ax.set_title(f"{r.tag} · {cfg.cond_label(r.condition).splitlines()[0].lower()} · {ARM_SHORT[arm]}\nP1 {n1} | P2 {n2}",
                         fontsize=9, color="#B71C1C" if (p1 is not None and data.is_partial(p1, r.code)) or p2 is None else "black")
            if i == len(raters) - 1:
                ax.set_xlabel("frames where the feature appears")
    handles = [Line2D([], [], marker="o", ls="", mfc="white", mec="#444444", mew=1.8, ms=7, label="Pass 1: mentioned in open free text (shared lexicon)"),
               Line2D([], [], marker="s", ls="", color="#444444", ms=7, label="Pass 2: marked present on the fixed checklist"),
               Line2D([], [], color="#444444", lw=1.6, label="arrow = within-rater shift, same frames")]
    fig.legend(handles=handles, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.02), fontsize=8.5)
    title(fig, "Instrument effect: the same rater, the same frames — open description vs fixed checklist",
          "Long arrows = features rarely or never written in free text but marked once the checklist names them.")
    fig.tight_layout(rect=(0, 0.03, 1, 0.94))
    footer(fig, "Pass 1 counts a lexicon match in the text (any wording outside the lexicon is missed); Pass 2 counts strict presence (Yes/Partial/Mild).")
    return [save(fig, cfg, "g1_pass1_vs_pass2_by_item")]


def fig_g2(cfg, data):
    raters = _p1_raters(cfg, data)
    it, sd = cfg.settings.get("bootstrap_iters", 2000), cfg.settings.get("seed", 7)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.4))
    xs = [0, 1]
    end_labels = []
    for r in raters:
        p1, p2 = data.pass1.get(r.code), data.pass2.get(r.code)
        lv = {"A": [None, None], "B": [None, None]}
        gap = [None, None]
        for x, (df, col) in enumerate(((p1, "p1_cpe7_count"), (p2, "cpe_hits_strict"))):
            if df is None:
                continue
            for arm in ("A", "B"):
                lv[arm][x] = df.loc[df.arm == arm, col].mean()
            gap[x] = boot_ci(df, col, it, sd, "delta")
        partial = p1 is not None and data.is_partial(p1, r.code)
        for arm, ls, mfc in (("A", "--", "white"), ("B", "-", r.color)):
            pts = [(x, v) for x, v in zip(xs, lv[arm]) if v is not None]
            if len(pts) == 2:
                ax1.plot([p[0] for p in pts], [p[1] for p in pts], ls=ls, color=r.color, lw=2)
            for x, v in pts:
                ax1.plot(x, v, "o", color=r.color, mfc=mfc, mew=1.8, ms=8)
        lbl = r.tag + (" (partial)" if partial else "") + (" — P2 pending" if p2 is None else "")
        if lv["B"][1] is not None:
            ax1.text(1.06, lv["B"][1], f"{r.tag} B", color=r.color, va="center", fontsize=8.5, fontweight="bold")
            ax1.text(1.06, lv["A"][1], f"{r.tag} A", color=r.color, va="center", fontsize=8.5)
        pts = [(x, g) for x, g in zip(xs, gap) if g is not None]
        if len(pts) == 2:
            ax2.plot([p[0] for p in pts], [p[1][0] for p in pts], color=r.color, lw=2.2)
        for x, g in pts:
            ax2.errorbar(x, g[0], yerr=[[g[0] - g[1]], [g[2] - g[0]]], fmt="o", color=r.color,
                         mfc="white" if partial else r.color, mew=1.8, ms=8, capsize=3)
        last = pts[-1]
        end_labels.append([last[0] + 0.06, last[1][0], lbl, r.color])
    lo, hi = ax2.get_ylim(); gap = 0.07 * (hi - lo)
    if any(l[0] < 0.5 for l in end_labels):
        ax2.set_ylim(lo - 2.2 * gap, hi)
    for x0 in sorted({round(l[0], 3) for l in end_labels}):
        grp = sorted([l for l in end_labels if round(l[0], 3) == x0], key=lambda l: l[1])
        for a_, b_ in zip(grp, grp[1:]):
            if b_[1] - a_[1] < gap:
                b_[1] = a_[1] + gap
        for x, y, t, c in grp:
            if x < 0.5:  # ends at Pass 1 (Pass 2 pending): put the label below the crowded Pass-1 points
                ax2.annotate(t, xy=(x - 0.06, y), xytext=(x + 0.04, y - 1.3 * gap), color=c, fontsize=8.5, fontweight="bold",
                             va="top", arrowprops=dict(arrowstyle="-", color=c, lw=0.8))
            else:
                ax2.text(x, y, t, color=c, va="center", fontsize=8.5, fontweight="bold")
    for ax in (ax1, ax2):
        ax.set_xticks(xs); ax.set_xticklabels(["Pass 1\nopen free text", "Pass 2\nfixed checklist"])
        ax.set_xlim(-0.25, 1.6); ax.grid(axis="y", color="#EEEEEE"); ax.set_axisbelow(True)
    ax1.set_ylim(-0.1, 7); ax1.set_ylabel("mean number of the 7 CPE-type checklist items\nreported per frame")
    ax1.set_title("Level (dashed/open = Culture A, solid/filled = Culture B)")
    ax2.axhline(0, color="black", lw=0.9)
    ax2.set_ylabel("B − A in items reported per frame (95% bootstrap CI)")
    ax2.set_title("Culture B − A gap")
    title(fig, "Instrument effect summary: CPE-type reports jump when the checklist names the features",
          "Same 7 CPE-type items in both passes (Pass 1 via the shared lexicon, Pass 2 via strict checklist presence).")
    fig.tight_layout(rect=(0, 0.02, 1, 0.9))
    footer(fig, "Pass 1 and Pass 2 measure different acts (spontaneous mention vs prompted mark); the shift is a property of the instrument, not only of the images.")
    return [save(fig, cfg, "g2_pass1_vs_pass2_summary_slope")]
