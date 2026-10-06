"""(j) colour-coded table of mean graded score and strict incidence (PNG + standalone HTML)."""
from __future__ import annotations

import html

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm, to_hex
from matplotlib.patches import Rectangle

from .. import items as I
from ..metrics import item_deltas, lookup
from ..style import footer, save, title

CM = {"cpe": plt.get_cmap("Oranges"), "healthy": plt.get_cmap("Greens")}
CMD = plt.get_cmap("PuOr_r"); ND = TwoSlopeNorm(0, -1, 1)


def _lev_color(kind, v):
    return CM[kind](0.08 + 0.75 * v)


def _txt(c):
    r, g, b = c[:3]
    return "black" if (0.299 * r + 0.587 * g + 0.114 * b) > 0.55 else "white"


def _rows(data):
    frames = data.item_frames()
    d = item_deltas(frames)
    raters = data.item_raters()
    out = []
    for k in I.ITEM_KEYS:
        cells = []
        for r in raters:
            row = lookup(d, r.code, k)
            if row is None:
                cells.append(None); continue
            df = frames[r.code]
            na, nb = data.n_arm(df)
            ia = int(round(row.inc_A * na)); ib = int(round(row.inc_B * nb))
            cells.append(dict(A=row.score_A, B=row.score_B, D=row.score_delta, ia=f"{ia}/{na}", ib=f"{ib}/{nb}"))
        out.append((k, cells))
    agg = []
    for col, lab, mx in (("cpe_score_sum", "CPE-type score sum (max 7)", 7), ("healthy_score_sum", "Healthy-type score sum (max 3)", 3)):
        cells = []
        for r in raters:
            df = frames[r.code]
            if col not in df.columns:
                cells.append(None); continue
            a = df.loc[df.arm == "A", col].mean(); b = df.loc[df.arm == "B", col].mean()
            cells.append(dict(A=a, B=b, D=b - a, mx=mx))
        agg.append((lab, col, cells))
    return raters, out, agg


def _dash(ax, X, cw, j, y):
    for t in range(3):
        xx = X[1 + 3 * j + t]
        ax.text(xx + cw[1 + t] / 2, y + 0.5, "—", ha="center", va="center", fontsize=9, color="#AAAAAA")


def fig_j(cfg, data):
    raters, rows, agg = _rows(data)
    ncol = 1 + 3 * len(raters)
    nrow = len(rows) + len(agg)
    cw = [3.2] + [1.15, 1.15, 0.95] * len(raters)
    X = np.r_[0, np.cumsum(cw)]
    fig, ax = plt.subplots(figsize=(sum(cw) * 0.95 + 0.4, 0.5 * (nrow + 2) + 1.4))
    ax.set_xlim(0, X[-1]); ax.set_ylim(nrow + 2, 0); ax.axis("off")
    for j, r in enumerate(raters):
        x0 = X[1 + 3 * j]
        ax.text((x0 + X[4 + 3 * j]) / 2, 0.45, f"{r.tag} · {cfg.cond_label(r.condition).splitlines()[0].lower()}"
                + (" · binary" if data.is_binary(r.code) else "") + f"\n({data.ntag(data.item_frames()[r.code], r.code)})",
                ha="center", va="center", fontweight="bold", fontsize=9.5, color=r.color)
        for t, sub in enumerate(("Culture A", "Culture B", "B − A")):
            ax.text((X[1 + 3 * j + t] + X[2 + 3 * j + t]) / 2, 1.3, sub, ha="center", va="center", fontsize=8.5)
    ax.text(0.1, 1.3, "Item", fontweight="bold", va="center")
    y = 2
    for k, cells in rows:
        kind = I.KIND[k]
        ax.text(0.1, y + 0.5, I.LABEL[k], va="center", fontsize=9, color="#1B5E20" if kind == "healthy" else "#BF360C")
        for j, c in enumerate(cells):
            if c is None:
                _dash(ax, X, cw, j, y); continue
            for t, key in enumerate(("A", "B")):
                col = _lev_color(kind, c[key]); xx = X[1 + 3 * j + t]
                ax.add_patch(Rectangle((xx + 0.03, y + 0.04), cw[1] - 0.06, 0.92, fc=col, ec="none"))
                ax.text(xx + cw[1] / 2, y + 0.42, f"{c[key]:.2f}", ha="center", va="center", fontsize=9, color=_txt(col), fontweight="bold")
                ax.text(xx + cw[1] / 2, y + 0.78, c["ia" if key == "A" else "ib"], ha="center", va="center", fontsize=6.5, color=_txt(col))
            col = CMD(ND(c["D"])); xx = X[3 + 3 * j]
            ax.add_patch(Rectangle((xx + 0.03, y + 0.04), cw[3] - 0.06, 0.92, fc=col, ec="none"))
            ax.text(xx + cw[3] / 2, y + 0.5, f"{c['D']:+.2f}", ha="center", va="center", fontsize=9, color=_txt(col), fontweight="bold")
        y += 1
        if k == I.HEALTHY_KEYS[-1]:
            ax.plot([0, X[-1]], [y, y], color="black", lw=0.8)
    ax.plot([0, X[-1]], [y, y], color="black", lw=1.4)
    for lab, colname, cells in agg:
        ax.text(0.1, y + 0.5, lab, va="center", fontsize=9, fontweight="bold")
        for j, c in enumerate(cells):
            if c is None:
                _dash(ax, X, cw, j, y); continue
            kind = "cpe" if "cpe" in colname else "healthy"
            for t, key in enumerate(("A", "B")):
                col = _lev_color(kind, c[key] / c["mx"]); xx = X[1 + 3 * j + t]
                ax.add_patch(Rectangle((xx + 0.03, y + 0.04), cw[1] - 0.06, 0.92, fc=col, ec="none"))
                ax.text(xx + cw[1] / 2, y + 0.5, f"{c[key]:.2f}", ha="center", va="center", fontsize=9.5, color=_txt(col), fontweight="bold")
            col = CMD(ND(c["D"] / c["mx"] * 2)); xx = X[3 + 3 * j]
            ax.add_patch(Rectangle((xx + 0.03, y + 0.04), cw[3] - 0.06, 0.92, fc=col, ec="none"))
            ax.text(xx + cw[3] / 2, y + 0.5, f"{c['D']:+.2f}", ha="center", va="center", fontsize=9.5, color=_txt(col), fontweight="bold")
        y += 1
    title(fig, "Colour-coded summary table: mean graded score per frame (small print = frames marked present)",
          "Orange = CPE-type intensity, green = healthy-type intensity; B − A column: orange = more in B, purple = more in A.")
    fig.subplots_adjust(top=0.86)
    from .delta import _cro_note
    footer(fig, "Pending raters are omitted here; see the heatmap (d) for placeholders. '—' = item not part of that rater's coding. " + _cro_note(data))
    paths = [save(fig, cfg, "j_styled_summary_table")]
    paths.append(_html(cfg, data, raters, rows, agg))
    return paths


def _html(cfg, data, raters, rows, agg):
    def td(v, col, small=""):
        c = to_hex(col)
        fg = _txt(col)
        s = f"<br><small>{small}</small>" if small else ""
        return f'<td style="background:{c};color:{fg}"><b>{v}</b>{s}</td>'
    h = ['<!doctype html><meta charset="utf-8"><title>R3 Pass-2 summary table</title>',
         "<style>body{font-family:Helvetica,Arial,sans-serif;margin:24px;color:#222}"
         "table{border-collapse:separate;border-spacing:3px}td,th{padding:6px 10px;text-align:center;font-size:13px;border-radius:3px}"
         "th{background:#f3f3f3}td.l{text-align:left;background:#fff}small{font-size:10px;opacity:.85}"
         ".h{color:#1B5E20}.c{color:#BF360C}</style>",
         "<h2>Pass-2 checklist: mean graded score per frame, Culture A (10% FBS) vs Culture B (2% FBS)</h2>",
         "<p>Cell colour: orange = CPE-type intensity, green = healthy-type intensity (0–1). B − A: orange = more in B, purple = more in A. "
         "Small print = frames marked present (strict). No viral inoculum in either culture; 'CPE-type' is a descriptor grouping, not a causal label.</p>",
         "<table><tr><th rowspan=2>Item</th>"]
    for r in raters:
        h.append(f'<th colspan=3 style="color:{r.color}">{html.escape(r.tag)} · {html.escape(cfg.cond_label(r.condition).splitlines()[0].lower())}<br>'
                 f"<small>{html.escape(data.ntag(data.item_frames()[r.code], r.code))}"
                 + ("<br>binary healthy-type coding" if data.is_binary(r.code) else "") + "</small></th>")
    h.append("</tr><tr>" + "".join("<th>A</th><th>B</th><th>B − A</th>" for _ in raters) + "</tr>")
    for k, cells in rows:
        kind = I.KIND[k]
        h.append(f'<tr><td class="l {"h" if kind == "healthy" else "c"}">{html.escape(I.LABEL[k])}</td>')
        for c in cells:
            if c is None:
                h.append('<td>—</td><td>—</td><td>—</td>'); continue
            h.append(td(f"{c['A']:.2f}", _lev_color(kind, c["A"]), c["ia"]) + td(f"{c['B']:.2f}", _lev_color(kind, c["B"]), c["ib"])
                     + td(f"{c['D']:+.2f}", CMD(ND(c["D"]))))
        h.append("</tr>")
    for lab, colname, cells in agg:
        kind = "cpe" if "cpe" in colname else "healthy"
        h.append(f'<tr><td class="l"><b>{html.escape(lab)}</b></td>')
        for c in cells:
            if c is None:
                h.append('<td>—</td><td>—</td><td>—</td>'); continue
            h.append(td(f"{c['A']:.2f}", _lev_color(kind, c["A"] / c["mx"])) + td(f"{c['B']:.2f}", _lev_color(kind, c["B"] / c["mx"]))
                     + td(f"{c['D']:+.2f}", CMD(ND(c["D"] / c["mx"] * 2))))
        h.append("</tr>")
    h.append("</table>")
    from .delta import _cro_note
    if _cro_note(data):
        h.append(f"<p><small>{html.escape(_cro_note(data))} '—' = item not part of that rater's coding.</small></p>")
    out = cfg.root / cfg.settings.get("tables_dir", str(cfg.out_dir / "tables")); out.mkdir(parents=True, exist_ok=True)
    p = out / "j_styled_summary_table.html"
    p.write_text("\n".join(h), encoding="utf-8")
    return str(p)
