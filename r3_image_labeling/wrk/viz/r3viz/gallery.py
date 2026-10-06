"""Gallery registry (captions, key message served, trade-offs) and GALLERY.md / index.html writers."""
from __future__ import annotations

import html
import os
from pathlib import Path

MSG = {1: "Global trend", 2: "Rater deltas", 3: "Pass 1 vs Pass 2", 4: "Briefing condition"}

REGISTRY = {
    "c0_global_direction_by_rater": ([1, 4], "One row per rater × instrument: Culture A → B level with an arrow, plus explicit B − A differences with bootstrap CIs (CPE-type and healthy-type). CRO has one row: binary CPE-type and healthy-type terms from its 22 single-frame descriptions (group descriptions not used).",
                                     "Best single 'headline' panel; levels are not comparable across instruments (normalized shares), only directions within a row."),
    "c1_dumbbell_A_to_B_by_item": ([1, 2], "Dumbbell per item: open = A, filled = B, colour = rater. Shows shared direction and which items carry each rater's B excess.",
                                   "Information-dense; with >4 raters switch to faceted version (i2)."),
    "c2_delta_dotplot_by_item": ([1, 2], "Explicit-difference dot plot: B − A per item, colour = rater; open dots = saturated items.",
                                 "Drops the absolute level (pair with d or j); easiest read of 'same direction, different items'."),
    "a_diverging_likert_marks": ([2], "Diverging stacked bars (Likert-style): full mark distribution per item, A vs B, small multiples by rater.",
                                 "Shows graded marks honestly (incl. 'Minimal', 'Mild'); dense — better as supplementary or for expert readers."),
    "b1_incidence_grouped_bars": ([1, 2], "Grouped horizontal bars of strict incidence by arm, faceted by rater, values printed.",
                                  "Most familiar format; binary incidence hides grading and saturates (many 0%/100% bars)."),
    "b2_cpe_composition_stacked": ([1, 2], "Stacked bars: which CPE-type items make up each rater's total, A vs B.",
                                   "Totals are easy to compare (common baseline); inner segments are harder to compare (no common baseline)."),
    "d_heatmap_mean_score": ([2], "Annotated heatmap of mean graded score (items × rater × arm) with a diverging B − A block.",
                             "Compact and scales to many raters; colour is a less precise channel than position — values are printed."),
    "e_agreement_heatmap_kappa": ([2], "Inter-rater agreement per item and rater pair: κ colour, % agreement printed, grey hatch where κ is undefined (constant rater).",
                                  "Makes the low frame-level agreement visible; κ is unstable with skewed marginals — always read with % agreement."),
    "f_daily_time_course": ([1, 2], "Line small multiples by rater: CPE-type and healthy-type score sums by day, A vs B, ±1.96 SE bands.",
                            "Clear monotonic-rise vs flat-offset contrast between raters; per-day n is small (~10 per arm)."),
    "g1_pass1_vs_pass2_by_item": ([3], "Within-rater arrows from Pass-1 free-text mention to Pass-2 checklist mark, per item and arm.",
                                  "Directly shows the instrument effect; Pass 1 counts lexicon matches only, so wording outside the lexicon is missed."),
    "g2_pass1_vs_pass2_summary_slope": ([3], "Slopegraph: CPE-type items reported per frame (level and B − A gap), Pass 1 → Pass 2, per rater.",
                                        "Simplest instrument-effect figure; collapses items into a count."),
    "h_briefing_condition_contrast": ([4], "B − A gap (top) and A/B levels (bottom) grouped by briefing condition, per instrument; empty slots = awaiting data; hollow = partial n.",
                                      "Populates as raters in further briefing conditions deliver; with n = 1 rater per condition it is descriptive, not inferential."),
    "i1_radar_profile_use_with_care": ([2], "Radar/spider profile per rater, A vs B (included on request).",
                                       "USE WITH CARE: shape/area depend on spoke order; angles and radial lengths are read less accurately than a common linear scale."),
    "i2_profile_small_multiples": ([2], "Recommended alternative to the radar: same data as dot plots on a common linear scale, small multiples by rater.",
                                   "Less 'iconic' than a radar but every comparison is position-on-common-scale."),
    "j_styled_summary_table": ([1, 2], "Colour-coded summary table (PNG + HTML): mean graded score A/B, B − A, incidence counts, aggregate sums.",
                               "For readers who want exact numbers; colour guides the eye to the B − A column."),
}
ORDER = ["c0_global_direction_by_rater", "c2_delta_dotplot_by_item", "c1_dumbbell_A_to_B_by_item", "j_styled_summary_table",
         "d_heatmap_mean_score", "b1_incidence_grouped_bars", "b2_cpe_composition_stacked", "a_diverging_likert_marks",
         "e_agreement_heatmap_kappa", "f_daily_time_course", "g1_pass1_vs_pass2_by_item", "g2_pass1_vs_pass2_summary_slope",
         "h_briefing_condition_contrast", "i2_profile_small_multiples", "i1_radar_profile_use_with_care"]


KIND_LABEL = {"pass1": "Pass 1", "pass2": "Pass 2", "cro": "CPE-type six", "cro_healthy": "healthy-type (binary)"}


def coverage_line(cfg, data) -> str:
    return "; ".join(
        f"{r.code}: " + ", ".join(f"{KIND_LABEL[k]} {data.ntag(getattr(data, k)[r.code], r.code)}"
                                  for k in ("pass1", "pass2", "cro", "cro_healthy") if r.code in getattr(data, k))
        for r in cfg.raters)


def write(cfg, data, outputs: dict[str, list[str]]):
    """GALLERY.md next to the tracked config (public set). With a local overlay active, the gallery goes
    next to the overlay as GALLERY_local.md so the tracked GALLERY.md never lists local-only raters."""
    root = cfg.overlays[0].parent if cfg.overlays else cfg.root
    gname = "GALLERY_local.md" if cfg.overlays else "GALLERY.md"
    fig_dir = cfg.out_dir / "figures"
    lines = ["# R3 rater-morphology figures — gallery", "",
             "Regenerate with `python make_figures.py --no-overlay` from `r3_image_labeling/wrk/viz/` (reads `raters.toml`; "
             "see README.md for setup). Figures are written to `figures/` (gitignored). Public role codes only. "
             "Key messages: **1** global trend · **2** rater deltas · **3** Pass 1 vs Pass 2 · **4** briefing condition.", "",
             "**Coverage now:** " + coverage_line(cfg, data), ""]
    if data.warnings:
        lines += ["**Warnings:** " + "; ".join(data.warnings), ""]
    for name in ORDER:
        if name not in outputs:
            continue
        msgs, cap, trade = REGISTRY[name]
        png = fig_dir / f"{name}.png"
        rel = Path(os.path.relpath(png, root)).as_posix()
        lines += [f"## {name}", f"*Serves:* {' · '.join(f'{m} {MSG[m]}' for m in msgs)}", "",
                  f"![{name}]({rel})", "", f"{cap}  ", f"*Trade-off:* {trade}"]
        extra = [p for p in outputs[name] if not p.endswith(".png")]
        for p in extra:
            lines.append(f"  \n*Also:* [{os.path.basename(p)}]({Path(os.path.relpath(p, root)).as_posix()})")
        lines.append("")
    (root / gname).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return root / gname
    # index.html
    h = ['<!doctype html><meta charset="utf-8"><title>R3 figure gallery</title>',
         "<style>body{font-family:Helvetica,Arial,sans-serif;max-width:1200px;margin:24px auto;color:#222}"
         "img{max-width:100%;border:1px solid #ddd}figure{margin:0 0 40px}.tag{display:inline-block;background:#eee;"
         "border-radius:3px;padding:1px 6px;margin-right:4px;font-size:12px}</style>",
         "<h1>R3 rater-morphology figures — gallery</h1>"]
    for name in ORDER:
        if name not in outputs:
            continue
        msgs, cap, trade = REGISTRY[name]
        tags = "".join(f'<span class="tag">{m} {MSG[m]}</span>' for m in msgs)
        h.append(f'<figure><h2>{name}</h2>{tags}<img src="figures/{name}.png"><figcaption><p>{html.escape(cap)}</p>'
                 f"<p><i>Trade-off:</i> {html.escape(trade)}</p></figcaption></figure>")
    (cfg.out_dir / "index.html").write_text("\n".join(h), encoding="utf-8")
