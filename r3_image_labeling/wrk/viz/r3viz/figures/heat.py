"""(d) heatmap of mean graded score (+ B-A block); (e) inter-rater agreement heatmap (kappa, greyed when constant)."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import Rectangle

from .. import items as I
from ..metrics import item_deltas, lookup, pair_agreement
from ..style import footer, save, title


def _txtcolor(rgba):
    r, g, b = rgba[:3]
    return "black" if (0.299 * r + 0.587 * g + 0.114 * b) > 0.55 else "white"


def fig_d(cfg, data):
    raters = data.item_raters(pending=True)
    frames = data.item_frames()
    d = item_deltas(frames)
    lv_cols, dl_cols = [], []
    for r in raters:
        lv_cols += [(r, "A"), (r, "B")]
        dl_cols.append(r)
    nrow = len(I.ITEM_KEYS)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(1.0 * len(lv_cols) + 0.9 * len(dl_cols) + 4.8, 6.6),
                                   gridspec_kw=dict(width_ratios=[len(lv_cols), len(dl_cols) + 0.3]))
    cm_l = plt.get_cmap("cividis"); cm_d = plt.get_cmap("PuOr_r"); nd = TwoSlopeNorm(0, -1, 1)
    for i, k in enumerate(I.ITEM_KEYS):
        for j, (r, arm) in enumerate(lv_cols):
            if r.code not in frames:
                ax1.add_patch(Rectangle((j, i), 1, 1, fc="#F2F2F2", ec="white", hatch="///", lw=0))
                continue
            row = lookup(d, r.code, k)
            if row is None:  # item not part of this rater's coding (CRO healthy-type coding: 3 healthy items)
                ax1.add_patch(Rectangle((j, i), 1, 1, fc="#FAFAFA", ec="white", lw=1.5))
                ax1.text(j + 0.5, i + 0.5, "—", ha="center", va="center", fontsize=8, color="#AAAAAA")
                continue
            v = row[f"score_{arm}"]
            c = cm_l(v)
            ax1.add_patch(Rectangle((j, i), 1, 1, fc=c, ec="white", lw=1.5))
            ax1.text(j + 0.5, i + 0.5, f"{v:.2f}", ha="center", va="center", fontsize=8, color=_txtcolor(c))
        for j, r in enumerate(dl_cols):
            if r.code not in frames:
                ax2.add_patch(Rectangle((j, i), 1, 1, fc="#F2F2F2", ec="white", hatch="///", lw=0)); continue
            row = lookup(d, r.code, k)
            if row is None:
                ax2.add_patch(Rectangle((j, i), 1, 1, fc="#FAFAFA", ec="white", lw=1.5))
                ax2.text(j + 0.5, i + 0.5, "—", ha="center", va="center", fontsize=8, color="#AAAAAA")
                continue
            v = row["score_delta"]
            c = cm_d(nd(v))
            ax2.add_patch(Rectangle((j, i), 1, 1, fc=c, ec="white", lw=1.5))
            ax2.text(j + 0.5, i + 0.5, f"{v:+.2f}", ha="center", va="center", fontsize=8.5, color=_txtcolor(c), fontweight="bold")
    for ax, ncol in ((ax1, len(lv_cols)), (ax2, len(dl_cols))):
        ax.set_xlim(0, ncol); ax.set_ylim(nrow, 0)
        ax.set_yticks(np.arange(nrow) + 0.5)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.tick_params(length=0)
        ax.axhline(3, color="black", lw=1.2)
    ax1.set_yticklabels([I.LABEL[k] for k in I.ITEM_KEYS])
    ax2.set_yticklabels([])
    ax1.set_xticks(np.arange(len(lv_cols)) + 0.5)
    ax1.set_xticklabels([f"{r.tag}\n{arm}" + ("\n(pending)" if r.code not in frames else "\n(binary)" if data.is_binary(r.code) else "")
                         for r, arm in lv_cols], fontsize=8.5)
    ax1.xaxis.tick_top()
    ax2.set_xticks(np.arange(len(dl_cols)) + 0.5)
    ax2.set_xticklabels([f"{r.tag}\nB − A" for r in dl_cols], fontsize=8.5); ax2.xaxis.tick_top()
    ax1.set_title("Mean graded score per frame (0–1; binary coding = share of frames)", pad=34)
    ax2.set_title("Difference B − A", pad=34)
    sm = plt.cm.ScalarMappable(cmap=cm_l, norm=plt.Normalize(0, 1))
    fig.colorbar(sm, ax=ax1, orientation="horizontal", fraction=0.04, pad=0.03, label="score (cividis, colour-blind safe)")
    sm2 = plt.cm.ScalarMappable(cmap=cm_d, norm=nd)
    fig.colorbar(sm2, ax=ax2, orientation="horizontal", fraction=0.04, pad=0.03, label="purple = more in A · orange = more in B")
    title(fig, "Heatmap of graded marks: items × rater × culture", "Left: level in each culture. Right: the B − A difference on a diverging scale centred at zero.")
    fig.tight_layout(rect=(0, 0.02, 1, 0.92))
    from .delta import _cro_note
    footer(fig, "Healthy-type items above the black line, CPE-type below. A = Culture A (10% FBS), B = Culture B (2% FBS). "
           "'—' = item not part of that rater's coding. " + _cro_note(data))
    return [save(fig, cfg, "d_heatmap_mean_score")]


def _agree_panel(ax, ag, items, labels, cm, norm):
    pairs = list(dict.fromkeys(ag["pair"]))
    for i, k in enumerate(items):
        for j, p in enumerate(pairs):
            row = ag[(ag.item == k) & (ag.pair == p)]
            if row.empty:
                continue
            row = row.iloc[0]
            if row.kappa is None or (isinstance(row.kappa, float) and np.isnan(row.kappa)):
                ax.add_patch(Rectangle((j, i), 1, 1, fc="#E6E6E6", ec="white", lw=1.5, hatch="//", ))
                ax.text(j + 0.5, i + 0.5, f"κ n/a\n(constant)\n{row.pct:.0f}% agree", ha="center", va="center", fontsize=7, color="#666666")
            else:
                c = cm(norm(row.kappa))
                ax.add_patch(Rectangle((j, i), 1, 1, fc=c, ec="white", lw=1.5))
                ax.text(j + 0.5, i + 0.5, f"κ {row.kappa:.2f}\n{row.pct:.0f}% agree", ha="center", va="center", fontsize=8,
                        color=_txtcolor(c), fontweight="bold")
    ax.set_xlim(0, len(pairs)); ax.set_ylim(len(items), 0)
    ax.set_yticks(np.arange(len(items)) + 0.5); ax.set_yticklabels(labels)
    ns = ag.groupby("pair")["n"].first()
    ax.set_xticks(np.arange(len(pairs)) + 0.5); ax.set_xticklabels([f"{p}\n(n = {ns[p]})" for p in pairs], fontsize=8.5)
    ax.xaxis.tick_top(); ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)


def fig_e(cfg, data):
    p2 = {c: df[["image_name"] + [f"hit_{k}" for k in I.ITEM_KEYS]].rename(columns={f"hit_{k}": k for k in I.ITEM_KEYS})
          for c, df in data.pass2.items()}
    ag2 = pair_agreement(p2, I.ITEM_KEYS)
    cro = dict(data.cro)
    if "CRO" in cro:  # restrict CRO-comparable comparison to the CRO-labelled frames
        keep = set(cro["CRO"]["image_name"])
        cro = {c: df[df.image_name.isin(keep)] for c, df in cro.items()}
    agc = pair_agreement(cro, I.CRO_SIX)
    cm = plt.get_cmap("BrBG"); norm = TwoSlopeNorm(0, -1, 1)
    npair2 = max(ag2["pair"].nunique(), 1) if len(ag2) else 1
    npc = max(agc["pair"].nunique(), 1) if len(agc) else 1
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(2.0 * (npair2 + npc) + 6.5, 7.2),
                                   gridspec_kw=dict(width_ratios=[npair2 + 0.6, npc]))
    if len(ag2):
        _agree_panel(ax1, ag2, I.ITEM_KEYS, [I.LABEL[k] for k in I.ITEM_KEYS], cm, norm)
        ax1.axhline(3, color="black", lw=1.2)
    ax1.set_title("Pass-2 checklist items (strict present / absent)", pad=36)
    if len(agc):
        _agree_panel(ax2, agc, I.CRO_SIX, [I.CRO_LABEL[c] for c in I.CRO_SIX], cm, norm)
    ax2.set_title("CRO-comparable coding (CRO-labelled frames)", pad=36)
    sm = plt.cm.ScalarMappable(cmap=cm, norm=norm)
    cax = fig.add_axes([0.3, 0.08, 0.4, 0.025])
    fig.colorbar(sm, cax=cax, orientation="horizontal",
                 label="Cohen's κ (−1 … 0 = chance … 1 = perfect); grey hatch = κ undefined because a rater gave one mark to every frame")
    title(fig, "Do raters agree frame by frame? Inter-rater agreement per item",
          "Colour = chance-corrected agreement (κ). Raw % agreement is printed but can be high just because both raters always say 'present'.")
    fig.subplots_adjust(top=0.80, bottom=0.2, wspace=0.35)
    footer(fig, "Pairs appear automatically for every rater pair with overlapping frames. κ computed only when both raters vary on the item.")
    return [save(fig, cfg, "e_agreement_heatmap_kappa")]
