"""Shared styling: colorblind-safe palettes (Okabe-Ito), fonts, footers, coverage flags."""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ARM_COLOR = {"A": "#0072B2", "B": "#D55E00"}      # Okabe-Ito blue / vermillion
ARM_LABEL = {"A": "Culture A (10% FBS)", "B": "Culture B (2% FBS)"}
ARM_SHORT = {"A": "A · 10% FBS", "B": "B · 2% FBS"}
OKABE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]
GREY = "#BDBDBD"
PENDING = "#9E9E9E"
FOOT = ("Culture A = 10% FBS, Culture B = 2% FBS; no viral inoculum in either culture. "
        "'CPE-type' = descriptor grouping only, not a causal label.")


def setup():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9.5, "axes.titlesize": 10.5,
        "axes.titleweight": "bold", "axes.labelsize": 9.5, "axes.spines.top": False,
        "axes.spines.right": False, "legend.frameon": False, "figure.dpi": 100,
        "savefig.bbox": "tight", "savefig.pad_inches": 0.15,
    })


def title(fig, main: str, sub: str = ""):
    fig.suptitle(main, x=0.01, ha="left", fontsize=13, fontweight="bold", y=0.995)
    if sub:
        fig.text(0.01, 0.955, sub, ha="left", va="top", fontsize=9.5, color="#444444")


def footer(fig, extra: str = "", y: float | None = None):
    """Footnote below everything. If the figure has a bottom legend, place the note under it."""
    txt = FOOT + (" " + extra if extra else "")
    if y is None:
        y = -0.005
        fig.canvas.draw()
        lgs = list(fig.legends) + [a.get_legend() for a in fig.axes if a.get_legend() is not None]
        for lg in lgs:
            bb = lg.get_window_extent().transformed(fig.transFigure.inverted())
            y = min(y, bb.y0 - 0.01)
        for a in fig.axes:  # also clear x tick labels / axis labels hanging below
            bb = a.get_tightbbox(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())
            y = min(y, bb.y0 - 0.01)
    import textwrap
    width = int(fig.get_figwidth() * 17)
    fig.text(0.01, y, "\n".join(textwrap.wrap(txt, width)), ha="left", va="top", fontsize=7.5, color="#555555")


def pending_panel(ax, text: str):
    ax.set_facecolor("#F5F5F5")
    ax.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(True); s.set_color("#DDDDDD"); s.set_linestyle("--")
    ax.text(0.5, 0.5, text, ha="center", va="center", transform=ax.transAxes, color=PENDING,
            fontsize=10, style="italic", wrap=True)


def partial_badge(ax, text="PARTIAL n", loc=(0.98, 0.98)):
    ax.text(*loc, text, transform=ax.transAxes, ha="right", va="top", fontsize=8, fontweight="bold",
            color="white", bbox=dict(boxstyle="round,pad=0.25", fc="#B71C1C", ec="none"))


def save(fig, cfg, name: str) -> str:
    out = cfg.out_dir / "figures"
    out.mkdir(parents=True, exist_ok=True)
    p = out / f"{name}.png"
    fig.savefig(p, dpi=cfg.settings.get("dpi", 220))
    plt.close(fig)
    return str(p)
