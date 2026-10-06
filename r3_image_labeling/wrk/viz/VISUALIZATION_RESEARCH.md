# Showing the R3 rater results so readers get it without reading numbers

**Scope:** which chart types work best for this dataset: 3+ raters × 2 cultures × 10 ordinal items × 2 instruments (Pass 1 free text, Pass 2 checklist) × day 1–5 × briefing condition. The goal is that readers see the main points with little effort. The recommendations come from graphical-perception research and from published guidance on scientific figures. The figure files they point to are written to `figures/` by `make_figures.py` (not tracked; regenerate them), and `GALLERY.md` shows them all.

---

## 1. Principles from the evidence

1. **Show the values you want compared as positions on a shared axis.** In Cleveland & McGill's ranking of how accurately people read values, the order is: position on a common scale > position on non-aligned scales > length > angle/slope > area > volume/colour saturation. Heer & Bostock's large crowdsourced replication got the same ordering. Practical consequence: B − A comparisons should be points or bars along one axis, not angles, areas or 3-D depth.
   - Cleveland & McGill (1984), *JASA* 79:531–554. https://doi.org/10.1080/01621459.1984.10478080
   - Heer & Bostock (2010), *CHI '10*. https://idl.cs.washington.edu/files/2010-MTurk-CHI.pdf
2. **Plot the difference itself.** When the message is a comparison, drawing the computed difference is the most direct of the three comparison strategies. The other two are side-by-side panels and overlays. That is why the delta dot plot and dumbbell charts are the headline figures.
   - Gleicher et al. (2011), *Information Visualization* 10:289–309. https://graphics.cs.wisc.edu/Papers/2011/GAWJHR11/paper.pdf
3. **Use small multiples with shared axes for each rater or condition.** Shared scales make panels comparable at a glance. Javed et al. found that separate panels beat one cluttered shared plot for comparing time series that cover a wide range.
   - Javed, McDonnel & Elmqvist (2010), *IEEE TVCG* 16:927–934. https://www.cs.au.dk/~elm/pdf/multilinevis.pdf
4. **Show n and the uncertainty, and don't hide small samples.** This matters most for small or partial deliveries (e.g. n = 5 per arm).
   - Weissgerber et al. (2015), *PLOS Biol* 13:e1002128. https://doi.org/10.1371/journal.pbio.1002128
   - Rougier, Droettboom & Bourne (2014), "Ten simple rules for better figures", *PLOS Comput Biol* 10:e1003833. https://doi.org/10.1371/journal.pcbi.1003833
5. **Choose colour by data type and make it colour-blind safe.**
   - Sequential maps for levels and diverging maps centred at zero for B − A. Avoid rainbow and red–green maps (Crameri et al. 2020, https://www.nature.com/articles/s41467-020-19160-7).
   - Categorical colours from the Okabe–Ito palette (Wong 2011, https://www.nature.com/articles/nmeth.1618).
   - The toolkit uses Okabe–Ito for raters and the two cultures, *cividis* for levels, and *PuOr* / *BrBG* for differences.

---

## 2. Chart types for this data

| Data shape | Recommended | Why | Use with care / avoid |
|---|---|---|---|
| Incidence across items (share of frames marked) | **Horizontal grouped bars** (A vs B), small multiples per rater (`b1`); **dot plot** | Lengths start from a common baseline, and horizontal bars keep the item names readable. | **Stacked bars** (`b2`) only for "what makes up the total": only the bottom segment and the total sit on a common baseline. **Pie charts:** angle and area judgments rank low (Cleveland & McGill). Few (2007) shows that labelled pies become a badly arranged table. |
| Ordinal / graded marks (Yes, Mild, Partial, Minimal, No) | **Diverging stacked bars (Likert plot)** centred on the present/absent boundary (`a`) | Heiberger & Robbins recommend these as the main display for rating scales. The key comparison (total present vs absent) sits on the zero baseline, and the full grading stays visible. | Bar charts of means hide how marks are distributed. |
| A → B difference per item | **Dumbbell / arrow plot** (`c1`); **delta dot plot** around zero (`c2`) | The difference is drawn as a position on a common axis. | Two separate bar panels make readers compute the difference in their heads. |
| Within-rater change (Pass 1 → Pass 2) | **Slopegraph** (`g2`) and **paired arrows per item** (`g1`) | The slope encodes the change, and each line is one rater, so pairing is visible. | Unpaired grouped bars lose the within-rater link. |
| Item × rater matrices | **Annotated heatmap** (`d`), **colour-coded table** (`j`) | Compact, and grows to more raters. Colour shows the pattern while the printed values give precision. Gehlenborg & Wong stress choosing the colour scale carefully. | Unannotated heatmaps, because colour is a weak channel for quantities. Rainbow colour maps. |
| Inter-rater agreement | **κ heatmap (items × rater pair) with % agreement printed; grey where κ is undefined** (`e`) | Shows at a glance where raters agree frame by frame and where they don't. | **κ on its own**: with lopsided marks, κ can be low even when raw agreement is high (the "high agreement, low κ" paradox), and κ is undefined when one rater gives the same mark to every frame. Always print % agreement and the positive counts with it. |
| Profile across 10 items | **Small-multiple dot plots** (`i2`) | Every comparison is a position on one linear scale. | **Radar / spider chart** (`i1`, included because you asked for it): see section 4. |
| Time course (day 1–5) | **Line small multiples, shared y-axis, uncertainty bands** (`f`) | Lines are the standard way to show change over time, and shared axes let readers compare raters. | Using 3-D or a second y-axis to cram raters into one panel. |
| Briefing-condition contrast | **Dot + CI of B − A, grouped by briefing condition, with the A/B levels underneath** (`h`) | Explicit difference plus the levels it comes from. Empty conditions stay visible as "awaiting data". | Bars of means for n = 1 rater per arm, because they imply a precision that isn't there. |

Sources for this section:
- Heiberger & Robbins (2014), "Design of diverging stacked bar charts for Likert scales and other applications", *J Stat Softw* 57(5). https://www.jstatsoft.org/article/view/v057i05
- Robbins & Heiberger (2011), "Plotting Likert and other rating scales" (critiques tables, grouped and divided bars, multiple pies, radar plots). http://www.asasrms.org/Proceedings/y2011/Files/300784_64164.pdf
- Gehlenborg & Wong (2012), "Points of view: Heat maps", *Nat Methods* 9:213. https://www.nature.com/articles/nmeth.1902
- Feinstein & Cicchetti (1990), "High agreement but low kappa: I", *J Clin Epidemiol* 43:543–549. https://doi.org/10.1016/0895-4356(90)90158-L
- Cicchetti & Feinstein (1990), "… II. Resolving the paradoxes" (recommends reporting positive and negative agreement alongside κ). https://doi.org/10.1016/0895-4356(90)90159-M

---

## 3. Shortlist for each key message

| Key message | Primary (pick 1) | Supporting | Trade-off |
|---|---|---|---|
| **1. Global trend**: every rater marks more CPE-type morphology in B (2% FBS) than in A (10% FBS) | `c0_global_direction_by_rater`: one row per rater × instrument, A → B arrow plus B − A with a 95% bootstrap CI | `j_styled_summary_table` (aggregate rows); `f_daily_time_course` | Instrument levels are normalized shares and can't be compared across rows. Only direction within a row is meaningful. |
| **2. Rater deltas**: big differences in overall level and in which items carry the B excess; low agreement except ballooned/enlarged | `c2_delta_dotplot_by_item` (same direction, different items) | `c1_dumbbell_A_to_B_by_item` (adds levels); `b2_cpe_composition_stacked` (which items make up each total); `e_agreement_heatmap_kappa`; `d_heatmap_mean_score` | `c2` drops absolute levels, so pair it with `c1`, `d` or `j`. `e` has to show κ as undefined on saturated items. |
| **3. Pass 1 vs Pass 2**: the checklist draws out features the free text never mentioned | `g2_pass1_vs_pass2_summary_slope` | `g1_pass1_vs_pass2_by_item` (per item and arm) | The two passes measure different acts (spontaneous mention vs prompted mark). Pass 1 relies on lexicon matches, so wording outside the lexicon is missed. |
| **4. Briefing condition**: raters who were blind to the culture conditions vs raters who knew the protocol, on the same frames | `h_briefing_condition_contrast` | `c0` | Partial deliveries show as hollow markers with a PARTIAL flag. With one rater per condition it describes what happened; it can't support inference. CRO's briefing status still needs confirming. |

Recommended main-text set: **c0 + c2 (or c1) + g2 + h**, with **j** as the table. Everything else is supplementary.

---

## 4. Avoid / use-with-care list

| Chart | Status | Reason (evidence) |
|---|---|---|
| **Pie / donut** | Avoid | Readers judge slices by angle, arc and area, all of which rank below position and length (Cleveland & McGill 1984; Heer & Bostock 2010). Multiple pies make comparing across cultures or raters especially hard (Few 2007, quoting Tufte: "the only worse design than a pie chart is several of them", https://www.perceptualedge.com/articles/visual_business_intelligence/save_the_pies_for_dessert.pdf). The evidence has nuance: Spence & Lewandowsky (1991) found pies roughly equal to bars for some part-to-whole judgments (https://doi.org/10.1002/acp.2350050106), and Skau & Kosara (2016) show readers rely more on area and arc than angle (https://onlinelibrary.wiley.com/doi/10.1111/cgf.12888). But our messages are A-vs-B and rater-vs-rater comparisons, which pies handle worst. |
| **3-D bars / 3-D pies** | Avoid | Decorative depth adds no information. In Siegrist's experiment, 3-D pies gave less accurate estimates, and 3-D bars took longer to read, with accuracy depending on bar position and height (Siegrist 1996, *Behav Inf Technol* 15:96–100, https://www.tandfonline.com/doi/abs/10.1080/014492996120300). Perspective also distorts lengths, which damages exactly the comparisons we need. |
| **Radar / spider** | Use with care (`i1` shown next to `i2`) | (a) The polygon's shape and area depend on the arbitrary order of the spokes. (b) Values are read as radial lengths with no common baseline, and differences between neighbouring spokes are hard to see. (c) Overlapping A and B polygons hide each other: IR1's A and B nearly coincide. In a controlled study, radar was the least effective and least liked of the radial designs tested (Albo et al. 2016, *IEEE TVCG* 22:569–578, https://doi.org/10.1109/TVCG.2015.2467322). Few (2005) recommends bars or lines unless the data are cyclic (https://www.perceptualedge.com/articles/dmreview/radar_graphs.pdf), and Robbins & Heiberger (2011) list radar plots among the weaker displays for rating scales. If one is used, fix the spoke order (healthy items, then CPE-type), keep the radial axis linear from 0, and always pair it with `i2`. |
| **Stacked bars for comparing inner segments** | Use with care (`b2`) | Only the bottom segment and the total share a baseline, so use it for "composition of the total", not for comparing a middle item. |
| **κ without % agreement / positive counts** | Avoid | κ is unstable with lopsided marks and undefined when a rater gives the same mark to every frame (Feinstein & Cicchetti 1990). `e` greys these cells out and prints % agreement. |
| **Bars of means without n or uncertainty** | Avoid | These hide small or partial samples (Weissgerber et al. 2015). Every figure here prints n per arm and flags partial deliveries. |

---

## 5. How these choices show up in the toolkit

- Every figure carries coverage (n A / n B), a red PARTIAL flag or hollow marker for incomplete deliveries, and a footnote: no viral inoculum in either culture; "CPE-type" is a descriptor grouping, not a causal label.
- Raters appear by public role code only (CRO, IR1, IR2, ...). Condition labels come from `raters.toml`.
- CRO healthy-type terms (binary, from each frame's own CRO description; 22 frames; group descriptions not used) fill the healthy-type rows of a, b1, c1, c2, d and j and the healthy-type panel of the CRO row in c0; their footnotes say they are binary, not graded.
- The B − A difference is drawn directly in c0, c2, d, g2, h and j.
- The briefing-condition figure keeps empty condition slots visible, so the design reads correctly before every condition has data.
