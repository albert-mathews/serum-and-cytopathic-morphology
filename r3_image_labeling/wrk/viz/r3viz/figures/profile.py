"""(i1) radar per rater (A vs B) — included on request, with caveats; (i2) recommended small-multiples dot-plot alternative."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from .. import items as I
from ..style import ARM_COLOR, footer, pending_panel, save, title, partial_badge
from .common import ROW_ITEMS, arm_handles, item_axis, rater_title


def fig_i1(cfg, data):
    raters = data.raters_configured("pass2")
    n = len(I.ITEM_KEYS)
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False)
    fig = plt.figure(figsize=(4.6 * len(raters), 5.4))
    for j, r in enumerate(raters):
        if r.code not in data.pass2:
            ax = fig.add_subplot(1, len(raters), j + 1)
            pending_panel(ax, f"{r.tag}\nPass 2 pending"); continue
        ax = fig.add_subplot(1, len(raters), j + 1, polar=True)
        df = data.pass2[r.code]
        for arm in ("A", "B"):
            v = df[df.arm == arm][[f"score_{k}" for k in I.ITEM_KEYS]].mean().to_numpy()
            vv = np.r_[v, v[:1]]; aa = np.r_[ang, ang[:1]]
            ax.plot(aa, vv, color=ARM_COLOR[arm], lw=2)
            ax.fill(aa, vv, color=ARM_COLOR[arm], alpha=0.15)
        ax.set_xticks(ang); ax.set_xticklabels([I.LABEL[k].replace(" / ", "/\n").replace(" ", "\n", 1) for k in I.ITEM_KEYS], fontsize=7)
        ax.set_ylim(0, 1); ax.set_yticks([0.25, 0.5, 0.75, 1]); ax.set_yticklabels([".25", ".5", ".75", "1"], fontsize=6.5, color="#777777")
        ax.set_title(rater_title(r, data, df), fontsize=9.5, pad=22)
    fig.legend(handles=arm_handles(), loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.02))
    title(fig, "Radar (spider) profile of mean graded score per item, Culture A vs B",
          "USE WITH CARE: polygon area and shape depend on the arbitrary order of the spokes; compare with the small-multiples version (i2).")
    fig.tight_layout(rect=(0, 0.04, 1, 0.9))
    footer(fig, "Healthy-type items: first three spokes clockwise from 3 o'clock; the rest are CPE-type.")
    return [save(fig, cfg, "i1_radar_profile_use_with_care")]


def fig_i2(cfg, data):
    raters = data.raters_configured("pass2")
    fig, axes = plt.subplots(1, len(raters), figsize=(3.7 * len(raters) + 1.7, 6.4), sharey=True, squeeze=False)
    for j, r in enumerate(raters):
        ax = axes[0, j]
        if r.code not in data.pass2:
            pending_panel(ax, f"{r.tag}\nPass 2 pending"); continue
        df = data.pass2[r.code]
        ypos = item_axis(ax, labels=(j == 0))
        for k in ROW_ITEMS:
            a = df.loc[df.arm == "A", f"score_{k}"].mean(); b = df.loc[df.arm == "B", f"score_{k}"].mean()
            ax.plot([a, b], [ypos[k]] * 2, color="#9E9E9E", lw=2, zorder=1)
            ax.plot(a, ypos[k], "o", color=ARM_COLOR["A"], ms=8, zorder=2)
            ax.plot(b, ypos[k], "o", color=ARM_COLOR["B"], ms=8, zorder=3)
        ax.set_xlim(-0.04, 1.04); ax.set_xticks([0, 0.5, 1])
        ax.grid(axis="x", color="#EEEEEE"); ax.set_axisbelow(True)
        ax.set_xlabel("mean graded score (0–1)")
        ax.set_title(rater_title(r, data, df), fontsize=9.5)
        if data.is_partial(df, r.code):
            partial_badge(ax)
    fig.legend(handles=arm_handles(), loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.03))
    title(fig, "Per-rater item profile, Culture A vs B (small multiples — recommended alternative to radar)",
          "Same data as the radar: one row per item on a common linear scale, so lengths and gaps can be compared directly.")
    fig.tight_layout(rect=(0, 0.03, 1, 0.91))
    footer(fig)
    return [save(fig, cfg, "i2_profile_small_multiples")]
