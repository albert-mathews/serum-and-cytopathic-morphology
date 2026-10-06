"""(c0) global direction per rater/instrument; (c1) dumbbell A->B per item; (c2) B-A delta dot plot."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from .. import items as I
from ..metrics import boot_ci, item_deltas, lookup
from ..style import ARM_COLOR, footer, save, title
from .common import ROW_ITEMS, item_axis


def _global_rows(cfg, data):
    """One row per rater x instrument with normalized CPE-type and healthy-type metrics."""
    rows = []
    it, sd = cfg.settings.get("bootstrap_iters", 2000), cfg.settings.get("seed", 7)
    for r in cfg.raters:
        specs = []
        if r.code not in data.pass2 and r.code not in data.pass1 and (r.code in data.cro or r.code in data.cro_healthy):
            cro = data.cro.get(r.code)
            hl = data.cro_healthy.get(r.code)
            if cro is not None and hl is not None:
                df = cro.merge(hl[["image_name", "healthy_share7"]], on="image_name", how="outer")
            else:
                df = cro if cro is not None else hl
            df = df.assign(cpe=df["n6"] / 6.0 if "n6" in df else np.nan,
                           hl=df["healthy_share7"] if "healthy_share7" in df else np.nan)
            specs.append(("labels from single-frame notes", df, "cpe" if cro is not None else None,
                          "hl" if hl is not None else None))
        if r.code in data.pass1:
            df = data.pass1[r.code].assign(cpe=lambda d: d["p1_cpe_count"] / len(I.P1_CPE_KEYS),
                                            hl=lambda d: d["p1_healthy_count"] / len(I.P1_HEALTHY_KEYS))
            specs.append(("Pass 1 · free text", df, "cpe", "hl"))
        if r.code in data.pass2:
            df = data.pass2[r.code].assign(cpe=lambda d: d["cpe_score_sum"] / 7.0, hl=lambda d: d["healthy_score_sum"] / 3.0)
            specs.append(("Pass 2 · checklist", df, "cpe", "hl"))
        elif r.pass1 is not None:
            specs.append(("Pass 2 · checklist", None, None, None))
        for inst, df, c, h in specs:
            row = dict(rater=r, inst=inst, df=df)
            if df is not None:
                row["A"] = boot_ci(df, c, it, sd, "A") if c else None
                row["B"] = boot_ci(df, c, it, sd, "B") if c else None
                row["d"] = boot_ci(df, c, it, sd, "delta") if c else None
                row["hd"] = boot_ci(df, h, it, sd, "delta") if h else None
                row["partial"] = data.is_partial(df, r.code)
                row["ntag"] = data.ntag(df, r.code)
            rows.append(row)
    return rows


def fig_c0(cfg, data):
    rows = _global_rows(cfg, data)
    n = len(rows)
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 0.62 * n + 2.6), sharey=True,
                             gridspec_kw=dict(width_ratios=[1.25, 1, 1]))
    ys = np.arange(n)[::-1]
    labels = []
    for y, row in zip(ys, rows):
        r = row["rater"]
        labels.append(f"{r.tag} · {row['inst']}" + (f"\n{row['ntag']}" if row.get("ntag") else "\n(not yet delivered)"))
        if row["df"] is None:
            for ax in axes:
                ax.text(0.5, y, "pending", transform=ax.get_yaxis_transform(), ha="center", va="center",
                        color="#9E9E9E", style="italic", fontsize=8.5)
            continue
        ax = axes[0]
        if row["A"] is None:
            ax.text(0.5, y, "healthy-type only → see right panel", transform=ax.get_yaxis_transform(), ha="center",
                    va="center", color="#9E9E9E", style="italic", fontsize=8)
        else:
            _level(ax, row, y, r)
        for ax, key in ((axes[1], "d"), (axes[2], "hd")):
            if row.get(key) is None:
                ax.text(0.5, y, "n/a", transform=ax.get_yaxis_transform(), ha="center", va="center", color="#9E9E9E", fontsize=8)
                continue
            d, lo, hi = row[key]
            ax.errorbar(d, y, xerr=[[d - lo], [hi - d]], fmt="D", color=r.color, ms=7,
                        mfc="white" if row["partial"] else r.color, mew=1.8, capsize=3)
    _c0_axes(fig, axes, ys, labels, rows, cfg)
    return [save(fig, cfg, "c0_global_direction_by_rater")]


def _level(ax, row, y, r):
    (a, alo, ahi), (b, blo, bhi) = row["A"], row["B"]
    ax.plot([a, b], [y, y], color=r.color, lw=2.4, alpha=0.8, zorder=1)
    ax.annotate("", xy=(b, y), xytext=(a, y), arrowprops=dict(arrowstyle="-|>", color=r.color, lw=0, mutation_scale=12))
    ax.errorbar(a, y, xerr=[[a - alo], [ahi - a]], fmt="o", mfc="white", mec=ARM_COLOR["A"], ecolor=ARM_COLOR["A"], ms=7, mew=1.8, zorder=3)
    ax.errorbar(b, y, xerr=[[b - blo], [bhi - b]], fmt="o", color=ARM_COLOR["B"], ms=7, zorder=3)


def _c0_axes(fig, axes, ys, labels, rows, cfg):
    axes[0].set_yticks(ys); axes[0].set_yticklabels(labels, fontsize=8.5)
    for tl, row in zip(axes[0].get_yticklabels(), rows):
        if row.get("partial") or row["df"] is None:
            tl.set_color("#B71C1C")
    axes[0].set_xlim(-0.02, 1.0)
    axes[0].set_xlabel("CPE-type marks per frame (share of the instrument's CPE-type items)")
    axes[0].set_title("Level: Culture A (open) → Culture B (filled)")
    for ax, t in ((axes[1], "CPE-type: B − A"), (axes[2], "Healthy-type: B − A")):
        ax.axvline(0, color="black", lw=0.9)
        ext = [abs(v) for row in rows for key in ("d", "hd") if row.get(key) for v in row[key]]
        lim = max(0.7, max(ext) + 0.08) if ext else 0.7
        ax.set_xlim(-lim, lim)
        ax.axvspan(0, lim, color=ARM_COLOR["B"], alpha=0.05); ax.axvspan(-lim, 0, color=ARM_COLOR["A"], alpha=0.05)
        ax.text(0.98, 1.0, "more in B →", transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color=ARM_COLOR["B"])
        ax.text(0.02, 1.0, "← more in A", transform=ax.transAxes, ha="left", va="bottom", fontsize=8, color=ARM_COLOR["A"])
        ax.set_title(t, pad=14)
        ax.set_xlabel("difference in normalized share (95% bootstrap CI)")
    for ax in axes:
        ax.grid(axis="x", color="#EEEEEE"); ax.set_axisbelow(True)
    handles = [Line2D([], [], marker="o", ls="", mfc="white", mec=ARM_COLOR["A"], mew=1.8, label="Culture A (10% FBS)"),
               Line2D([], [], marker="o", ls="", color=ARM_COLOR["B"], label="Culture B (2% FBS)"),
               Line2D([], [], marker="D", ls="", mfc="white", mec="#555555", mew=1.8, label="hollow diamond = partial coverage")]
    fig.legend(handles=handles, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.04))
    title(fig, "Global direction: does each rater mark more CPE-type (and less healthy-type) morphology in Culture B than in Culture A?",
          "One row per rater × instrument. Compare direction within a row; levels are not comparable across instruments.")
    fig.tight_layout(rect=(0, 0.03, 1, 0.92))
    note = ("Pass 1 = share of the 10 CPE-type / 7 healthy-type lexicon terms found in the free text; Pass 2 = graded score / 7 (CPE) or / 3 (healthy); "
            "CRO = binary terms named in each frame's own single-image description (22 frames): CPE-type = share of its six descriptors; "
            "healthy-type = share of the same 7 healthy-type keys (Look healthy, Mitotic/Bright, Adherent, Elongated, Polygonal, "
            "Cytoplasmic extensions, Well-defined nuclei). The CRO's 10-frame group descriptions are not used (lower specificity), and its short "
            "frame notes are not exhaustive checklists, so 'not named' is not 'absent'.")
    if any(r.note for r in cfg.raters):
        note += " * " + "; ".join(f"{r.code}: {r.note}" for r in cfg.raters if r.note) + "."
    footer(fig, note)


def _rater_offsets(raters, span=0.62):
    n = len(raters)
    return {r.code: (span / 2 - i * span / max(n - 1, 1)) if n > 1 else 0 for i, r in enumerate(raters)}


def _legend_tag(cfg, data, r, with_n=False):
    cond = cfg.cond_label(r.condition).splitlines()[0].lower()
    fr = data.item_frames()[r.code]
    extra = ", binary healthy-type only" if data.is_binary(r.code) else ""
    return f"{r.tag} ({cond}{extra}" + (f", {data.ntag(fr, r.code)})" if with_n else ")")


def fig_c1(cfg, data):
    raters = data.item_raters()
    d = item_deltas(data.item_frames())
    off = _rater_offsets(raters)
    fig, ax = plt.subplots(figsize=(8.6, 8.0))
    ypos = item_axis(ax)
    for r in raters:
        for k in ROW_ITEMS:
            row = lookup(d, r.code, k)
            if row is None:
                continue
            y = ypos[k] + off[r.code]
            a, b = row.score_A, row.score_B
            ax.plot([a, b], [y, y], color=r.color, lw=2.2, alpha=0.85, zorder=1)
            if abs(b - a) > 0.03:
                ax.annotate("", xy=(b, y), xytext=(a + (b - a) * 0.6, y),
                            arrowprops=dict(arrowstyle="-|>", color=r.color, lw=0, mutation_scale=11))
            ax.plot(b, y, "o", color=r.color, ms=6.5, zorder=3)
            ax.plot(a, y, "o", mfc="none", mec=r.color, mew=1.8, ms=9.5 if abs(b - a) < 0.02 else 6.5, zorder=4)
            if abs(b - a) >= 0.02:
                ax.plot(a, y, "o", mfc="white", mec=r.color, mew=1.8, ms=6.5, zorder=4)
    ax.set_xlim(-0.03, 1.03)
    ax.set_xlabel("mean graded score per frame (0 = never marked, 1 = 'Yes' on every frame)")
    ax.grid(axis="x", color="#EEEEEE"); ax.set_axisbelow(True)
    handles = [Line2D([], [], color=r.color, lw=2.5, marker="o", label=_legend_tag(cfg, data, r, True)) for r in raters]
    handles += [Line2D([], [], marker="o", ls="", mfc="white", mec="#444444", mew=1.8, label="open = Culture A (10% FBS)"),
                Line2D([], [], marker="o", ls="", color="#444444", label="filled = Culture B (2% FBS)")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.42, -0.08), ncol=2, fontsize=8)
    title(fig, "Item by item: where each rater's marks move from Culture A to Culture B",
          "Each line runs from A (open) to B (filled); arrow = direction. Long rightward lines on CPE-type rows = B excess.")
    fig.tight_layout(rect=(0, 0.02, 1, 0.92))
    footer(fig, _cro_note(data))
    return [save(fig, cfg, "c1_dumbbell_A_to_B_by_item")]


def _cro_note(data):
    codes = [c for c in data.item_frames() if data.is_binary(c)]
    if not codes:
        return ""
    return (f"{', '.join(codes)}: healthy-type rows only, binary (share of frames whose own single-image CRO description names the term; "
            "22 frames; group descriptions not used); no graded marks.")


def fig_c2(cfg, data):
    raters = data.item_raters()
    d = item_deltas(data.item_frames())
    off = _rater_offsets(raters, 0.5)
    fig, ax = plt.subplots(figsize=(8.4, 7.4))
    ypos = item_axis(ax)
    lim = max(0.85, float(d["score_delta"].abs().max()) + 0.1) if len(d) else 0.85
    ax.axvspan(0, lim, color=ARM_COLOR["B"], alpha=0.05); ax.axvspan(-lim, 0, color=ARM_COLOR["A"], alpha=0.05)
    for r in raters:
        for k in ROW_ITEMS:
            row = lookup(d, r.code, k)
            if row is None:
                continue
            y = ypos[k] + off[r.code]
            ax.plot([0, row.score_delta], [y, y], color=r.color, lw=1.2, alpha=0.6)
            ax.plot(row.score_delta, y, "o", ms=8, color=r.color, mfc="white" if row.saturated else r.color, mew=1.8)
    ax.axvline(0, color="black", lw=1)
    ax.set_xlim(-lim, lim)
    ax.set_xlabel("B − A difference in mean graded score")
    ax.text(0.99, 1.0, "marked more in Culture B →", transform=ax.transAxes, ha="right", va="bottom", color=ARM_COLOR["B"], fontsize=8.5)
    ax.text(0.01, 1.0, "← marked more in Culture A", transform=ax.transAxes, ha="left", va="bottom", color=ARM_COLOR["A"], fontsize=8.5)
    ax.grid(axis="x", color="#EEEEEE"); ax.set_axisbelow(True)
    handles = [Line2D([], [], color=r.color, marker="o", lw=0, ms=8, label=_legend_tag(cfg, data, r)) for r in raters]
    handles.append(Line2D([], [], marker="o", lw=0, ms=8, mfc="white", mec="#444444", mew=1.8,
                          label="open = strict incidence 0% or 100% in both arms (saturated)"))
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.4, -0.08), ncol=2, fontsize=8)
    title(fig, "Size and direction of the Culture B − A difference, per item and rater",
          "Dots right of zero = more marked in B. Shared direction on CPE-type rows; which rows carry it differs by rater.")
    fig.tight_layout(rect=(0, 0.02, 1, 0.92))
    footer(fig, _cro_note(data))
    return [save(fig, cfg, "c2_delta_dotplot_by_item")]
