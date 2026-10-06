"""(a) Diverging stacked (Likert-style) bars of graded marks per item, A vs B, per rater."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

from .. import items as I
from ..style import ARM_COLOR, footer, pending_panel, save, title, partial_badge
from .common import ROW_ITEMS, item_axis, rater_title

RIGHT = {"cpe": {"partial": "#FDD0A2", "mild": "#FD8D3C", "yes": "#C2410C"},
         "healthy": {"partial": "#C7E9C0", "mild": "#74C476", "yes": "#1B7837"}}
LEFT = {"trace": "#D9D9D9", "absent": "#8C8C8C"}


def _binary_note(ax, ypos):
    """Text in the CPE-type block of a CRO healthy-type panel (binary coding, no graded CPE-type marks)."""
    cpe = [ypos[k] for k in ROW_ITEMS if I.KIND[k] == "cpe"]
    ax.text(0.5, (min(cpe) + max(cpe)) / 2, "binary healthy-type coding\n(CRO single-frame notes, 22 frames)\n\nCPE-type: CRO six descriptors,\nsame 22 frames - see c0, e, h",
            transform=ax.get_yaxis_transform(), ha="center", va="center", fontsize=8, color="#8A8A8A", style="italic")


def fig_a(cfg, data):
    raters = data.item_raters(pending=True)
    frames = data.item_frames()
    fig, axes = plt.subplots(1, len(raters), figsize=(4.3 * len(raters) + 1.4, 7.4), sharey=True, squeeze=False)
    for j, r in enumerate(raters):
        ax = axes[0, j]
        if r.code not in frames:
            pending_panel(ax, f"{r.tag} · {cfg.cond_label(r.condition).splitlines()[0].lower()}\nPass-2 checklist\nnot yet delivered")
            continue
        df = frames[r.code]
        ypos = item_axis(ax, labels=(j == 0))
        if data.is_binary(r.code):
            _binary_note(ax, ypos)
        for k in ROW_ITEMS:
            if f"level_{k}" not in df.columns:
                continue
            for arm, off in (("A", 0.19), ("B", -0.19)):
                sub = df[df["arm"] == arm]
                if not len(sub):
                    continue
                share = sub[f"level_{k}"].value_counts(normalize=True)
                y = ypos[k] + off
                x0 = 0.0
                for lv in I.PRESENT_LEVELS:
                    w = share.get(lv, 0.0)
                    ax.barh(y, w, left=x0, height=0.34, color=RIGHT[I.KIND[k]][lv], edgecolor="white", lw=0.4)
                    x0 += w
                x0 = 0.0
                for lv in I.ABSENT_LEVELS:
                    w = share.get(lv, 0.0)
                    ax.barh(y, -w, left=x0, height=0.34, color=LEFT[lv], edgecolor="white", lw=0.4)
                    x0 -= w
                ax.text(-1.04, y, arm, color=ARM_COLOR[arm], fontsize=7.5, fontweight="bold", ha="right", va="center")
        ax.axvline(0, color="black", lw=0.9)
        ax.set_xlim(-1.08, 1.0)
        ax.set_xticks([-1, -0.5, 0, 0.5, 1])
        ax.set_xticklabels(["100%", "50%", "0", "50%", "100%"])
        ax.set_xlabel("← marked absent / trace        marked present →", fontsize=8.5)
        ax.set_title(rater_title(r, data, df), fontsize=9.5)
        ax.grid(axis="x", color="#EEEEEE", lw=0.6); ax.set_axisbelow(True)
        if data.is_partial(df, r.code):
            partial_badge(ax)
    handles = ([Patch(color=LEFT["absent"], label="No / not apparent"), Patch(color=LEFT["trace"], label="Minimal / no-minimal")]
               + [Patch(color=RIGHT["cpe"][lv], label=f"CPE-type: {I.LEVEL_LABEL[lv]}") for lv in I.PRESENT_LEVELS]
               + [Patch(color=RIGHT["healthy"][lv], label=f"Healthy-type: {I.LEVEL_LABEL[lv]}") for lv in I.PRESENT_LEVELS])
    fig.legend(handles=handles, loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.06), fontsize=8)
    title(fig, "Pass-2 checklist marks, item by item: Culture A (upper bar) vs Culture B (lower bar)",
          "Bars right of the line = feature marked present (darker = stronger mark); left = marked absent or trace. "
          "Read the orange (CPE-type) bars: they grow in B for every rater, but on different items.")
    fig.tight_layout(rect=(0, 0.02, 1, 0.93))
    from .delta import _cro_note
    footer(fig, "Strict presence = Yes / Partial / Mild (/partial). Rater vocabularies differ (IR2 has no 'Minimal'). "
           "Binary coding: named = 'Yes', not named = 'No / not apparent'. " + _cro_note(data))
    return [save(fig, cfg, "a_diverging_likert_marks")]
