# R3 rater-morphology figures - draft review

**Status:** DRAFT visualization figures for the R3 rater-morphology results, waiting for Albert to choose which ones to use. Nothing here is final.
**Last updated:** 2026-10-06 (CRO labels rebuilt from the CRO image descriptions under the single-frame rule)

## What the figures need to show

The figure set needs to convey four messages:

1. **Global trend** - Culture A (10% FBS) vs Culture B (2% FBS), across raters.
2. **Rater deltas** - where raters agree and differ, item by item.
3. **Pass 1 vs Pass 2 effect** - free-text description vs fixed checklist.
4. **Briefing-condition effect** - what each rater was told about the cultures (blind vs knows-protocol; further conditions fill in as raters deliver).

**Coverage now (tracked data):** CRO: CPE-type and healthy-type labels n = 9 A / 13 B (22 frames with their own CRO description; binary; group descriptions not used); IR1: Pass 1 and Pass 2 n = 50 A / 50 B; IR2: Pass 1 and Pass 2 n = 50 A / 50 B.

**Regeneration:** the PNGs are not tracked. They are rebuilt from the tracked data deposits by `viz/make_figures.py` (config `viz/raters.toml`); setup and the exact command are in `viz/README.md` (`python make_figures.py --no-overlay` from `r3_image_labeling/wrk/viz/`). New rater data is added to the config and the full set is regenerated, so new results fill in automatically (figure h has empty slots waiting for them). Public role codes only.

## Recommended headline set

**c0, c2, g2, h, j**:

- **c0** global direction per rater (message 1, 4)
- **c2** B - A per item (messages 1, 2)
- **g2** Pass 1 -> Pass 2 slopegraph (message 3)
- **h** briefing-condition contrast (message 4)
- **j** styled summary table, for readers who want exact numbers

The other figures are alternatives or supplementary options.

## How to review

Leave comments on the `**@Albert:**` line under each figure (e.g. "keep as headline", "supplementary", "drop", or requested changes). Replies from the assistant are added below yours, starting with `@CPE:`. Figures are listed roughly by priority.

---

## c0_global_direction_by_rater (headline candidate)

![c0_global_direction_by_rater](viz/figures/c0_global_direction_by_rater.png)

*Serves:* 1 Global trend · 4 Briefing condition

One row per rater × instrument: Culture A → B level with an arrow, plus explicit B − A differences with bootstrap CIs (CPE-type and healthy-type).

*CRO row:* one row, binary terms named in each frame's own CRO description (22 frames: 9 A / 13 B; source `cro-results/cro_cpe_detections.csv`). CPE-type share of six: A 0.02, B 0.36 (B − A +0.34). Healthy-type share of 7 descriptor keys: A 0.17, B 0.11 (B − A −0.06). The CRO's 10-frame group descriptions are lower-specificity and are not used (kept in `cro-results/cro_group_level_notes.csv`); its frame notes are short, so a term not named is not necessarily absent.

*Trade-off:* Best single 'headline' panel; levels are not comparable across instruments (normalized shares), only directions within a row.

**@Albert:** 

---

## c2_delta_dotplot_by_item (headline candidate)

![c2_delta_dotplot_by_item](viz/figures/c2_delta_dotplot_by_item.png)

*Serves:* 1 Global trend · 2 Rater deltas

Explicit-difference dot plot: B − A per item, colour = rater; open dots = saturated items. CRO dots on the three healthy rows (binary, single-frame descriptions): looks healthy 0.00 and nuclei 0.00 (never named for an individual frame), cytoplasmic extensions +0.46 (6/13 B frames, 0/9 A).

*Trade-off:* Drops the absolute level (pair with d or j); easiest read of 'same direction, different items'.

**@Albert:** 

---

## c1_dumbbell_A_to_B_by_item

![c1_dumbbell_A_to_B_by_item](viz/figures/c1_dumbbell_A_to_B_by_item.png)

*Serves:* 1 Global trend · 2 Rater deltas

Dumbbell per item: open = A, filled = B, colour = rater. Shows shared direction and which items carry each rater's B excess. CRO appears on the three healthy rows (binary, 22 frames).

*Trade-off:* Information-dense; with >4 raters switch to faceted version (i2).

**@Albert:** 

---

## j_styled_summary_table (headline candidate)

![j_styled_summary_table](viz/figures/j_styled_summary_table.png)

*Serves:* 1 Global trend · 2 Rater deltas

Colour-coded summary table (PNG + HTML): mean graded score A/B, B − A, incidence counts, aggregate sums. CRO columns: healthy rows and healthy sum (A 0.00, B 0.46) filled, binary, 22 frames; CPE-type rows "—".

*Trade-off:* For readers who want exact numbers; colour guides the eye to the B − A column.

*Also:* [j_styled_summary_table.html](viz/j_styled_summary_table.html)

**@Albert:** 

---

## d_heatmap_mean_score

![d_heatmap_mean_score](viz/figures/d_heatmap_mean_score.png)

*Serves:* 2 Rater deltas

Annotated heatmap of mean graded score (items × rater × arm) with a diverging B − A block. CRO columns (binary, 22 frames) fill the three healthy rows; CPE-type rows "—".

*Trade-off:* Compact and scales to many raters; colour is a less precise channel than position — values are printed.

**@Albert:** 

---

## h_briefing_condition_contrast (headline candidate)

![h_briefing_condition_contrast](viz/figures/h_briefing_condition_contrast.png)

*Serves:* 4 Briefing condition

B − A gap (top) and A/B levels (bottom) grouped by briefing condition, per instrument; empty slots = awaiting data; hollow = partial n.

*Trade-off:* Populates as raters in further briefing conditions deliver; with n = 1 rater per condition it is descriptive, not inferential. (CPE-type only; CRO healthy-type descriptors are in c0.)

**@Albert:** 

---

## g2_pass1_vs_pass2_summary_slope (headline candidate)

![g2_pass1_vs_pass2_summary_slope](viz/figures/g2_pass1_vs_pass2_summary_slope.png)

*Serves:* 3 Pass 1 vs Pass 2

Slopegraph: CPE-type items reported per frame (level and B − A gap), Pass 1 → Pass 2, per rater.

*Trade-off:* Simplest instrument-effect figure; collapses items into a count.

**@Albert:** 

---

## g1_pass1_vs_pass2_by_item

![g1_pass1_vs_pass2_by_item](viz/figures/g1_pass1_vs_pass2_by_item.png)

*Serves:* 3 Pass 1 vs Pass 2

Within-rater arrows from Pass-1 free-text mention to Pass-2 checklist mark, per item and arm.

*Trade-off:* Directly shows the instrument effect; Pass 1 counts lexicon matches only, so wording outside the lexicon is missed.

**@Albert:** 

---

## b1_incidence_grouped_bars

![b1_incidence_grouped_bars](viz/figures/b1_incidence_grouped_bars.png)

*Serves:* 1 Global trend · 2 Rater deltas

Grouped horizontal bars of strict incidence by arm, faceted by rater, values printed. CRO panel: healthy rows only (named in the frame's own CRO description, A/B: looks healthy 0%/0%, nuclei 0%/0%, cytoplasmic extensions 0%/46%).

*Trade-off:* Most familiar format; binary incidence hides grading and saturates (many 0%/100% bars).

**@Albert:** 

---

## b2_cpe_composition_stacked

![b2_cpe_composition_stacked](viz/figures/b2_cpe_composition_stacked.png)

*Serves:* 1 Global trend · 2 Rater deltas

Stacked bars: which CPE-type items make up each rater's total, A vs B.

*Trade-off:* Totals are easy to compare (common baseline); inner segments are harder to compare (no common baseline).

**@Albert:** 

---

## a_diverging_likert_marks

![a_diverging_likert_marks](viz/figures/a_diverging_likert_marks.png)

*Serves:* 2 Rater deltas

Diverging stacked bars (Likert-style): full mark distribution per item, A vs B, small multiples by rater. CRO panel: healthy rows only, binary, 22 frames (named = 'Yes', not named = 'No / not apparent').

*Trade-off:* Shows graded marks honestly (incl. 'Minimal', 'Mild'); dense — better as supplementary or for expert readers.

**@Albert:** 

---

## f_daily_time_course

![f_daily_time_course](viz/figures/f_daily_time_course.png)

*Serves:* 1 Global trend · 2 Rater deltas

Line small multiples by rater: CPE-type and healthy-type score sums by day, A vs B, ±1.96 SE bands.

*Trade-off:* Clear monotonic-rise vs flat-offset contrast between raters; per-day n is small (~10 per arm).

**@Albert:** 

---

## e_agreement_heatmap_kappa

![e_agreement_heatmap_kappa](viz/figures/e_agreement_heatmap_kappa.png)

*Serves:* 2 Rater deltas

Inter-rater agreement per item and rater pair: κ colour, % agreement printed, grey hatch where κ is undefined (constant rater).

*Trade-off:* Makes the low frame-level agreement visible; κ is unstable with skewed marginals — always read with % agreement.

**@Albert:** 

---

## i2_profile_small_multiples

![i2_profile_small_multiples](viz/figures/i2_profile_small_multiples.png)

*Serves:* 2 Rater deltas

Recommended alternative to the radar: same data as dot plots on a common linear scale, small multiples by rater.

*Trade-off:* Less 'iconic' than a radar but every comparison is position-on-common-scale.

**@Albert:** 

---

## i1_radar_profile_use_with_care

![i1_radar_profile_use_with_care](viz/figures/i1_radar_profile_use_with_care.png)

*Serves:* 2 Rater deltas

Radar/spider profile per rater, A vs B (included on request).

*Trade-off:* USE WITH CARE: shape/area depend on spoke order; angles and radial lengths are read less accurately than a common linear scale.

**@Albert:** 

---

## After selection

- Once Albert picks the set, the chosen figures are marked as the headline set in `viz/GALLERY.md` and regenerated for the paper. PNGs stay untracked; the code, config and data deposits are what is versioned.
- To select figures or change one (labels, ordering, colours, which raters/conditions appear), edit `viz/raters.toml` / the `viz/r3viz/` code and regenerate. The PNGs are never edited by hand, so every figure can be reproduced from the data and config.
