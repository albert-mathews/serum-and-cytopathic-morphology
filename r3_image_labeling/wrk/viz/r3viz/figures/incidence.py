"""(b1) grouped incidence bars per item by arm, faceted by rater; (b2) stacked CPE-score composition."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch, Rectangle

from .. import items as I
from ..style import ARM_COLOR, ARM_LABEL, OKABE, footer, pending_panel, save, title, partial_badge
from .common import ROW_ITEMS, arm_handles, item_axis, rater_title


SHORT = {"CPE_Vacuolation_V": "Vacuolation", "CPE_Granularity_G": "Granularity", "CPE_Ballooned_Enlarged_BE": "Ballooned",
         "CPE_Syncytia_Sy": "Syncytia", "CPE_Cytoplasmic_strands_CS": "Strands", "CPE_Cell_death_Dy": "Cell death",
         "CPE_Nonspecific_degeneration_ND": "Degeneration"}


def fig_b1(cfg, data):
    raters = data.item_raters(pending=True)
    frames = data.item_frames()
    fig, axes = plt.subplots(1, len(raters), figsize=(3.8 * len(raters) + 1.6, 6.4), sharey=True, squeeze=False)
    for j, r in enumerate(raters):
        ax = axes[0, j]
        if r.code not in frames:
            pending_panel(ax, f"{r.tag}\nPass-2 checklist\nnot yet delivered"); continue
        df = frames[r.code]
        ypos = item_axis(ax, labels=(j == 0))
        if data.is_binary(r.code):
            from .likert import _binary_note
            _binary_note(ax, ypos)
        for k in ROW_ITEMS:
            if f"hit_{k}" not in df.columns:
                continue
            for arm, off in (("A", 0.19), ("B", -0.19)):
                v = df.loc[df["arm"] == arm, f"hit_{k}"].mean()
                ax.barh(ypos[k] + off, v, height=0.36, color=ARM_COLOR[arm], alpha=0.9)
                ax.text(v + 0.02, ypos[k] + off, f"{v:.0%}", va="center", fontsize=6.5, color="#333333")
        ax.set_xlim(0, 1.18); ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "50%", "100%"])
        ax.set_xlabel("frames with feature marked present")
        ax.set_title(rater_title(r, data, df), fontsize=9.5)
        if data.is_partial(df, r.code):
            partial_badge(ax)
    fig.legend(handles=arm_handles(), loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.03))
    title(fig, "How often each feature was marked present (Pass-2 checklist, strict incidence; CRO healthy-type: named in CRO table)",
          "Grouped bars: blue = Culture A (10% FBS), vermillion = Culture B (2% FBS).")
    fig.tight_layout(rect=(0, 0.03, 1, 0.92))
    from .delta import _cro_note
    footer(fig, _cro_note(data))
    return [save(fig, cfg, "b1_incidence_grouped_bars")]


def fig_b2(cfg, data):
    raters = data.raters_configured("pass2")
    colors = dict(zip(I.CPE_KEYS, [OKABE[i] for i in (0, 3, 5, 6, 1, 7, 2)]))
    fig, ax = plt.subplots(figsize=(2.3 * len(raters) + 3.5, 5.6))
    xt, xl = [], []
    for j, r in enumerate(raters):
        base = j * 3.0
        if r.code not in data.pass2:
            ax.add_patch(Rectangle((base - 0.4, 0), 1.8, 7, fill=False, ls="--", ec="#BBBBBB"))
            ax.text(base + 0.5, 3.5, f"{r.tag}\nPass 2\npending", ha="center", va="center", color="#9E9E9E", style="italic")
            xt.append(base + 0.5); xl.append(f"{r.tag}\n({cfg.cond_label(r.condition).splitlines()[0].lower()})")
            continue
        df = data.pass2[r.code]
        for i, arm in enumerate(("A", "B")):
            sub = df[df["arm"] == arm]
            bottom = 0.0
            for k in I.CPE_KEYS:
                v = sub[f"score_{k}"].mean()
                ax.bar(base + i, v, bottom=bottom, width=0.8, color=colors[k], edgecolor="white", lw=0.6)
                if v >= 0.35:
                    ax.text(base + i, bottom + v / 2, SHORT[k], ha="center", va="center", fontsize=6.3,
                            color="white" if k in ("CPE_Cell_death_Dy", "CPE_Syncytia_Sy", "CPE_Cytoplasmic_strands_CS", "CPE_Nonspecific_degeneration_ND") else "black")
                bottom += v
            ax.text(base + i, bottom + 0.1, f"{bottom:.2f}", ha="center", va="bottom", fontsize=8, fontweight="bold")
            ax.text(base + i, -0.25, arm, ha="center", va="top", color=ARM_COLOR[arm], fontweight="bold")
        xt.append(base + 0.5)
        xl.append(f"\n{r.tag} ({cfg.cond_label(r.condition).splitlines()[0].lower()})\n{data.ntag(df, r.code)}")
    ax.set_xticks(xt); ax.set_xticklabels(xl, fontsize=8.5)
    ax.tick_params(axis="x", length=0, pad=14)
    ax.set_ylim(0, 7.3); ax.set_ylabel("mean CPE-type score sum per frame (max 7)")
    ax.legend(handles=[Patch(color=colors[k], label=I.LABEL[k]) for k in I.CPE_KEYS][::-1],
              loc="upper left", bbox_to_anchor=(1.0, 1.0), title="CPE-type item", fontsize=8)
    title(fig, "Which features make up each rater's CPE-type total, Culture A vs B",
          "Stack height = mean graded CPE-type score per frame; segment = one item's contribution.")
    fig.tight_layout(rect=(0, 0.02, 1, 0.9))
    footer(fig, "Graded score: Yes 1, Mild 0.66, Partial 0.5, Minimal 0.25, No/minimal 0.15, No 0.")
    return [save(fig, cfg, "b2_cpe_composition_stacked")]
