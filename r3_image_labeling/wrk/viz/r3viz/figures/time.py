"""(f) per-day line small multiples: CPE-type and healthy-type score sums, A vs B, per rater."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from ..metrics import daily
from ..style import ARM_COLOR, footer, pending_panel, save, title, partial_badge
from .common import arm_handles, rater_title


def fig_f(cfg, data):
    raters = data.raters_configured("pass2")
    rows = [("cpe_score_sum", "CPE-type score sum\n(max 7)", 7), ("healthy_score_sum", "Healthy-type score sum\n(max 3)", 3)]
    fig, axes = plt.subplots(2, len(raters), figsize=(3.9 * len(raters) + 1, 6.6), squeeze=False, sharex=True)
    for j, r in enumerate(raters):
        for i, (col, lab, mx) in enumerate(rows):
            ax = axes[i, j]
            if r.code not in data.pass2:
                pending_panel(ax, f"{r.tag}\nPass 2 pending" if i == 0 else ""); continue
            df = data.pass2[r.code]
            dd = daily(df, col)
            for arm in ("A", "B"):
                s = dd[dd.arm == arm]
                ax.fill_between(s.day, s["mean"] - 1.96 * s.se.fillna(0), s["mean"] + 1.96 * s.se.fillna(0),
                                color=ARM_COLOR[arm], alpha=0.15, lw=0)
                ax.plot(s.day, s["mean"], "-o", color=ARM_COLOR[arm], lw=2.2, ms=5)
                last = s.iloc[-1]
                ax.text(last.day + 0.12, last["mean"], arm, color=ARM_COLOR[arm], fontweight="bold", va="center")
            ax.set_ylim(0, mx); ax.set_xlim(0.7, 5.5); ax.set_xticks([1, 2, 3, 4, 5])
            ax.grid(axis="y", color="#EEEEEE"); ax.set_axisbelow(True)
            if j == 0:
                ax.set_ylabel(lab)
            if i == 0:
                per_day = int(dd["count"].median())
                ax.set_title(rater_title(r, data, df, f" · ~{per_day}/day/arm"), fontsize=9.5)
                if data.is_partial(df, r.code):
                    partial_badge(ax)
            if i == 1:
                ax.set_xlabel("day")
    fig.legend(handles=arm_handles(), loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.03))
    title(fig, "Time course: mean score per frame by day, Culture A vs B (Pass-2 checklist)",
          "Shared y-axes across raters. Band = ±1.96 SE across frames of that day.")
    fig.tight_layout(rect=(0, 0.03, 1, 0.91))
    footer(fig)
    return [save(fig, cfg, "f_daily_time_course")]
