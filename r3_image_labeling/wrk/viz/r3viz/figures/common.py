from __future__ import annotations

import numpy as np

from .. import items as I
from ..style import ARM_COLOR

ROW_ITEMS = I.ITEM_KEYS  # display order top -> bottom


def item_axis(ax, keys=ROW_ITEMS, labels=True, sep=True):
    ys = np.arange(len(keys))[::-1]
    ax.set_yticks(ys)
    if labels:
        ax.set_yticklabels([I.LABEL[k] for k in keys])
    else:
        ax.tick_params(labelleft=False)
    ax.set_ylim(-0.6, len(keys) - 0.4)
    if sep and any(I.KIND[k] == "healthy" for k in keys) and any(I.KIND[k] == "cpe" for k in keys):
        nh = sum(I.KIND[k] == "healthy" for k in keys)
        ax.axhline(len(keys) - nh - 0.5, color="#888888", lw=0.8, ls=":")
    return dict(zip(keys, ys))


def group_labels(ax, keys=ROW_ITEMS, x=-0.02):
    nh = sum(I.KIND[k] == "healthy" for k in keys)
    n = len(keys)
    ax.annotate("HEALTHY-type", xy=(x, (n - nh / 2 - 0.5) / n), xycoords=("axes fraction", "axes fraction"),
                rotation=90, ha="right", va="center", fontsize=7.5, color="#2E7D32", fontweight="bold",
                xytext=(-95, 0), textcoords="offset points")
    ax.annotate("CPE-type", xy=(x, ((n - nh) / 2 - 0.5 + 0.5) / n), xycoords=("axes fraction", "axes fraction"),
                rotation=90, ha="right", va="center", fontsize=7.5, color="#BF360C", fontweight="bold",
                xytext=(-95, 0), textcoords="offset points")


def rater_title(r, data, df, extra=""):
    cond = data.cfg.cond_label(r.condition).split("\n")[0].lower()
    return f"{r.tag} · {cond}\n{data.ntag(df, r.code)}{extra}"


def arm_handles():
    from matplotlib.lines import Line2D
    return [Line2D([], [], marker="o", ls="", color=ARM_COLOR[a], label=l)
            for a, l in (("A", "Culture A (10% FBS)"), ("B", "Culture B (2% FBS)"))]
