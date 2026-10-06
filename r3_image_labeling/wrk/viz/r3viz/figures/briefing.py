"""(h) Briefing-condition contrast: B-A gap and A/B level grouped by what each rater was told."""
from __future__ import annotations

import textwrap

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from ..metrics import boot_ci
from ..style import ARM_COLOR, footer, save, title


def _panels(cfg, data):
    p1 = data.pass1
    matched = None
    if len(p1) >= 2:
        sets = [set(df.image_name) for df in p1.values()]
        matched = set.intersection(*sets)
    cro = data.cro
    keep = set(cro["CRO"].image_name) if "CRO" in cro else None
    panels = [
        dict(key="p1_all", title="Pass 1 · free text\nall frames each rater described", store=p1, col="p1_cpe_count",
             ylab="CPE-type lexicon terms per frame", ymax=None, flag=True),
        dict(key="p1_matched", title=f"Pass 1 · free text\nmatched frames only (n = {len(matched) if matched else 0})",
             store={c: df[df.image_name.isin(matched)] for c, df in p1.items()} if matched else {}, col="p1_cpe_count",
             ylab="CPE-type lexicon terms per frame", ymax=None, flag=False),
        dict(key="p2", title="Pass 2 · fixed checklist\nall frames", store=data.pass2, col="cpe_score_sum",
             ylab="CPE-type score sum per frame (max 7)", ymax=7, flag=True),
        dict(key="cro", title="CRO-comparable six descriptors\nCRO-labelled frames only",
             store={c: df[df.image_name.isin(keep)] for c, df in cro.items()} if keep else {}, col="n6",
             ylab="CRO descriptors marked per frame (max 6)", ymax=6, flag=False),
    ]
    return panels


def fig_h(cfg, data):
    conds = cfg.conditions
    panels = _panels(cfg, data)
    it, sd = cfg.settings.get("bootstrap_iters", 2000), cfg.settings.get("seed", 7)
    fig, axes = plt.subplots(2, len(panels), figsize=(4.6 * len(panels), 9.2), squeeze=False)
    for j, pn in enumerate(panels):
        axg, axl = axes[0, j], axes[1, j]
        for ci, c in enumerate(conds):
            rs = [r for r in cfg.raters if r.condition == c["key"] and r.code in pn["store"] and len(pn["store"][r.code])]
            if not rs:
                for ax in (axg, axl):
                    ax.text(ci, 0.5, "awaiting\ndata", transform=ax.get_xaxis_transform(), ha="center", va="center",
                            color="#B0B0B0", fontsize=8, style="italic")
                continue
            offs = np.linspace(-0.18, 0.18, len(rs)) if len(rs) > 1 else [0.0]
            for r, o in zip(rs, offs):
                df = pn["store"][r.code]
                x = ci + o
                partial = data.is_partial(df, r.code) if pn["flag"] else False
                d, lo, hi = boot_ci(df, pn["col"], it, sd, "delta")
                axg.errorbar(x, d, yerr=[[d - lo], [hi - d]], fmt="D", ms=8, color=r.color, capsize=3,
                             mfc="white" if partial else r.color, mew=2)
                axg.text(x, hi, f" {r.tag}", rotation=90, ha="center", va="bottom", fontsize=7.5, color=r.color, fontweight="bold")
                a, b = df.loc[df.arm == "A", pn["col"]].mean(), df.loc[df.arm == "B", pn["col"]].mean()
                axl.plot([x, x], [a, b], color=r.color, lw=2.2)
                axl.plot(x, a, "o", mfc="white", mec=ARM_COLOR["A"], mew=1.8, ms=7)
                axl.plot(x, b, "o", color=ARM_COLOR["B"], ms=7)
                na, nb = data.n_arm(df)
                axl.text(x, -0.13, f"{r.tag}\n{na}/{nb}" + ("\nPARTIAL" if partial else ""), transform=axl.get_xaxis_transform(),
                         ha="center", va="top", fontsize=7, color="#B71C1C" if partial else "#555555",
                         fontweight="bold" if partial else "normal")
        for ax in (axg, axl):
            ax.set_xlim(-0.6, len(conds) - 0.4)
            for ci in range(len(conds)):
                ax.axvspan(ci - 0.45, ci + 0.45, color="#FAFAFA", zorder=0)
            ax.grid(axis="y", color="#EEEEEE"); ax.set_axisbelow(True)
        axg.set_xticks(range(len(conds))); axg.set_xticklabels([c["label"].replace("-", "-\n", 1) if len(c["label"]) > 8 else c["label"] for c in conds], fontsize=8)
        lo_, hi_ = axg.get_ylim(); axg.set_ylim(lo_, hi_ + 0.22 * (hi_ - lo_))
        axl.set_xticks([])
        axg.axhline(0, color="black", lw=0.9)
        axg.set_title(pn["title"], fontsize=9.5)
        if j == 0:
            axg.set_ylabel("Culture B − A gap\n(95% bootstrap CI)")
        axl.set_ylabel(pn["ylab"], fontsize=8.5)
        if pn["ymax"]:
            axl.set_ylim(0, pn["ymax"])
        else:
            axl.set_ylim(bottom=0)
    handles = [Line2D([], [], marker="D", ls="", color="#444444", ms=8, label="B − A gap (filled = full set)"),
               Line2D([], [], marker="D", ls="", mfc="white", mec="#444444", mew=2, ms=8, label="hollow = partial coverage"),
               Line2D([], [], marker="o", ls="", mfc="white", mec=ARM_COLOR["A"], mew=1.8, label="Culture A level"),
               Line2D([], [], marker="o", ls="", color=ARM_COLOR["B"], label="Culture B level")]
    fig.legend(handles=handles, loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.035))
    title(fig, "Briefing-condition contrast: does what a rater was told change the Culture B − A gap?",
          "Columns = instrument; x-groups = briefing condition. Top: B − A gap. Bottom: the A and B levels behind it. "
          "Empty slots fill in as briefed raters deliver.")
    fig.tight_layout(rect=(0, 0.04, 1, 0.92), h_pad=3.5)
    notes = ["Conditions: " + "; ".join(f"{c['label']} = {c.get('description', '')}" for c in conds) + "."]
    notes += ["Matched-frame and CRO-frame columns are subsets by design (not flagged partial)."]
    notes += [f"{r.code}: {r.figure_note}." for r in cfg.raters if r.figure_note]
    notes += [f"* {r.code}: {r.note}." for r in cfg.raters if r.note]
    lead = cfg.settings.get("h_note", "")
    footer(fig, (lead + " " if lead else "") + " ".join(notes))
    return [save(fig, cfg, "h_briefing_condition_contrast")]
