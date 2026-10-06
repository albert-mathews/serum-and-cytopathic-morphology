# R3 rater-morphology figures — gallery

Regenerate with `python make_figures.py --no-overlay` from `r3_image_labeling/wrk/viz/` (reads `raters.toml`; see README.md for setup). Figures are written to `figures/` (gitignored). Public role codes only. Key messages: **1** global trend · **2** rater deltas · **3** Pass 1 vs Pass 2 · **4** briefing condition.

**Coverage now:** CRO: CPE-type six n = 9 A / 13 B, healthy-type (binary) n = 9 A / 13 B; IR1: Pass 1 n = 50 A / 50 B, Pass 2 n = 50 A / 50 B, CPE-type six n = 50 A / 50 B; IR2: Pass 1 n = 50 A / 50 B, Pass 2 n = 50 A / 50 B, CPE-type six n = 50 A / 50 B

## c0_global_direction_by_rater
*Serves:* 1 Global trend · 4 Briefing condition

![c0_global_direction_by_rater](figures/c0_global_direction_by_rater.png)

One row per rater × instrument: Culture A → B level with an arrow, plus explicit B − A differences with bootstrap CIs (CPE-type and healthy-type). CRO has one row: binary CPE-type and healthy-type terms from its 22 single-frame descriptions (group descriptions not used).  
*Trade-off:* Best single 'headline' panel; levels are not comparable across instruments (normalized shares), only directions within a row.

## c2_delta_dotplot_by_item
*Serves:* 1 Global trend · 2 Rater deltas

![c2_delta_dotplot_by_item](figures/c2_delta_dotplot_by_item.png)

Explicit-difference dot plot: B − A per item, colour = rater; open dots = saturated items.  
*Trade-off:* Drops the absolute level (pair with d or j); easiest read of 'same direction, different items'.

## c1_dumbbell_A_to_B_by_item
*Serves:* 1 Global trend · 2 Rater deltas

![c1_dumbbell_A_to_B_by_item](figures/c1_dumbbell_A_to_B_by_item.png)

Dumbbell per item: open = A, filled = B, colour = rater. Shows shared direction and which items carry each rater's B excess.  
*Trade-off:* Information-dense; with >4 raters switch to faceted version (i2).

## j_styled_summary_table
*Serves:* 1 Global trend · 2 Rater deltas

![j_styled_summary_table](figures/j_styled_summary_table.png)

Colour-coded summary table (PNG + HTML): mean graded score A/B, B − A, incidence counts, aggregate sums.  
*Trade-off:* For readers who want exact numbers; colour guides the eye to the B − A column.
  
*Also:* [j_styled_summary_table.html](j_styled_summary_table.html)

## d_heatmap_mean_score
*Serves:* 2 Rater deltas

![d_heatmap_mean_score](figures/d_heatmap_mean_score.png)

Annotated heatmap of mean graded score (items × rater × arm) with a diverging B − A block.  
*Trade-off:* Compact and scales to many raters; colour is a less precise channel than position — values are printed.

## b1_incidence_grouped_bars
*Serves:* 1 Global trend · 2 Rater deltas

![b1_incidence_grouped_bars](figures/b1_incidence_grouped_bars.png)

Grouped horizontal bars of strict incidence by arm, faceted by rater, values printed.  
*Trade-off:* Most familiar format; binary incidence hides grading and saturates (many 0%/100% bars).

## b2_cpe_composition_stacked
*Serves:* 1 Global trend · 2 Rater deltas

![b2_cpe_composition_stacked](figures/b2_cpe_composition_stacked.png)

Stacked bars: which CPE-type items make up each rater's total, A vs B.  
*Trade-off:* Totals are easy to compare (common baseline); inner segments are harder to compare (no common baseline).

## a_diverging_likert_marks
*Serves:* 2 Rater deltas

![a_diverging_likert_marks](figures/a_diverging_likert_marks.png)

Diverging stacked bars (Likert-style): full mark distribution per item, A vs B, small multiples by rater.  
*Trade-off:* Shows graded marks honestly (incl. 'Minimal', 'Mild'); dense — better as supplementary or for expert readers.

## e_agreement_heatmap_kappa
*Serves:* 2 Rater deltas

![e_agreement_heatmap_kappa](figures/e_agreement_heatmap_kappa.png)

Inter-rater agreement per item and rater pair: κ colour, % agreement printed, grey hatch where κ is undefined (constant rater).  
*Trade-off:* Makes the low frame-level agreement visible; κ is unstable with skewed marginals — always read with % agreement.

## f_daily_time_course
*Serves:* 1 Global trend · 2 Rater deltas

![f_daily_time_course](figures/f_daily_time_course.png)

Line small multiples by rater: CPE-type and healthy-type score sums by day, A vs B, ±1.96 SE bands.  
*Trade-off:* Clear monotonic-rise vs flat-offset contrast between raters; per-day n is small (~10 per arm).

## g1_pass1_vs_pass2_by_item
*Serves:* 3 Pass 1 vs Pass 2

![g1_pass1_vs_pass2_by_item](figures/g1_pass1_vs_pass2_by_item.png)

Within-rater arrows from Pass-1 free-text mention to Pass-2 checklist mark, per item and arm.  
*Trade-off:* Directly shows the instrument effect; Pass 1 counts lexicon matches only, so wording outside the lexicon is missed.

## g2_pass1_vs_pass2_summary_slope
*Serves:* 3 Pass 1 vs Pass 2

![g2_pass1_vs_pass2_summary_slope](figures/g2_pass1_vs_pass2_summary_slope.png)

Slopegraph: CPE-type items reported per frame (level and B − A gap), Pass 1 → Pass 2, per rater.  
*Trade-off:* Simplest instrument-effect figure; collapses items into a count.

## h_briefing_condition_contrast
*Serves:* 4 Briefing condition

![h_briefing_condition_contrast](figures/h_briefing_condition_contrast.png)

B − A gap (top) and A/B levels (bottom) grouped by briefing condition, per instrument; empty slots = awaiting data; hollow = partial n.  
*Trade-off:* Populates as raters in further briefing conditions deliver; with n = 1 rater per condition it is descriptive, not inferential.

## i2_profile_small_multiples
*Serves:* 2 Rater deltas

![i2_profile_small_multiples](figures/i2_profile_small_multiples.png)

Recommended alternative to the radar: same data as dot plots on a common linear scale, small multiples by rater.  
*Trade-off:* Less 'iconic' than a radar but every comparison is position-on-common-scale.

## i1_radar_profile_use_with_care
*Serves:* 2 Rater deltas

![i1_radar_profile_use_with_care](figures/i1_radar_profile_use_with_care.png)

Radar/spider profile per rater, A vs B (included on request).  
*Trade-off:* USE WITH CARE: shape/area depend on spoke order; angles and radial lengths are read less accurately than a common linear scale.

