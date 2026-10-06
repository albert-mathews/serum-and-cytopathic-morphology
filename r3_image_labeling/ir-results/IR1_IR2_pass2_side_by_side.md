# IR1 vs IR2 — Pass 2 structured checklist (10 criteria)

**Scope:** Pass-2 checklist marks on the same 100 blinded CultureA/CultureB phase-contrast images.
**Labels:** IR1 and IR2 only (independent researchers; both blind to culture conditions).
**Instrument:** identical 10 criteria (IR1 Pass-2 wording). IR1 used Yes / Partial / Mild-partial / Minimal / No-minimal / No / Not apparent; IR2 used Yes / Partial / Mild / No (IR2 definitions: Partial = subset of field/cells; Mild = present but subtle).
**Scorer:** the IR1 Pass-2 scorer, unchanged (graded score: Yes 1.0; Mild 0.66; Partial 0.5; Minimal 0.25; No/minimal 0.15; No/Not apparent 0; healthy items Yes 1.0 / Partial-Mild 0.5 / else 0).
**Strict incidence:** Yes / Partial / Mild / Mild-partial = present (same rule as `ir_cpe_detections.csv`).
**Arms (analysis only):** CultureA = path1 (10% FBS), CultureB = path2 (2% FBS). n = 50 per arm.
**Rule:** Confluence/coverage is not used as healthy vs stressed.

**Companion CSVs:** `IR1_IR2_pass2_checklist_comparison.csv` (incidence + mean score per rater/arm), `IR1_IR2_pass2_item_agreement.csv` (per-item agreement, all / per arm), `IR1_IR2_CRO_overlap_agreement.csv` (22 CRO-labeled frames).

---

## Coverage

| | IR1 | IR2 |
|--|--:|--:|
| Images with all 10 criteria marked | 100 | 100 |
| CultureA / CultureB | 50 / 50 | 50 / 50 |
| Blank cells | 0 | 0 |
| Distinct 10-item mark patterns (of 100 images) | 14 | 40 |

Image IDs match 1:1 (`CultureX_dayY_ZZ`).

---

## Strict incidence by arm

| # | Item | IR1 A | IR1 B | IR1 B−A | IR2 A | IR2 B | IR2 B−A |
|---|------|------:|------:|-------:|------:|------:|-------:|
| 1 | H_Look_Healthy | 1.00 | 1.00 | +0.00 | 1.00 | 0.58 | −0.42 |
| 2 | H_well_defined_nuclei | 1.00 | 1.00 | +0.00 | 1.00 | 1.00 | +0.00 |
| 3 | H_Cytoplasmic_extensions | 1.00 | 1.00 | +0.00 | 1.00 | 0.98 | −0.02 |
| 4 | CPE_Vacuolation_V | 0.00 | 0.00 | +0.00 | 1.00 | 1.00 | +0.00 |
| 5 | CPE_Granularity_G | 1.00 | 1.00 | +0.00 | 1.00 | 1.00 | +0.00 |
| 6 | CPE_Ballooned_Enlarged_BE | 0.38 | 1.00 | +0.62 | 0.00 | 0.78 | +0.78 |
| 7 | CPE_Syncytia_Sy | 0.00 | 0.00 | +0.00 | 0.00 | 0.56 | +0.56 |
| 8 | CPE_Cytoplasmic_strands_CS | 0.14 | 0.96 | +0.82 | 1.00 | 1.00 | +0.00 |
| 9 | CPE_Cell_death_Dy | 0.06 | 0.00 | −0.06 | 0.78 | 1.00 | +0.22 |
| 10 | CPE_Nonspecific_degeneration_ND | 0.00 | 0.00 | +0.00 | 0.00 | 1.00 | +1.00 |

(IR1 Dy under the looser score>0 rule, which also counts Minimal / No-minimal, is A 0.20 / B 0.00 — see IR1 Pass-2 review.)

## Mean graded score by arm

| # | Item | IR1 A | IR1 B | IR1 B−A | IR2 A | IR2 B | IR2 B−A |
|---|------|------:|------:|-------:|------:|------:|-------:|
| 1 | H_Look_Healthy | 1.00 | 1.00 | +0.00 | 1.00 | 0.29 | −0.71 |
| 2 | H_well_defined_nuclei | 1.00 | 1.00 | +0.00 | 1.00 | 0.72 | −0.28 |
| 3 | H_Cytoplasmic_extensions | 1.00 | 1.00 | +0.00 | 0.82 | 0.78 | −0.04 |
| 4 | CPE_Vacuolation_V | 0.00 | 0.00 | +0.00 | 0.63 | 0.63 | −0.01 |
| 5 | CPE_Granularity_G | 0.52 | 0.50 | −0.02 | 0.63 | 0.92 | +0.29 |
| 6 | CPE_Ballooned_Enlarged_BE | 0.19 | 0.50 | +0.31 | 0.00 | 0.57 | +0.57 |
| 7 | CPE_Syncytia_Sy | 0.00 | 0.00 | +0.00 | 0.00 | 0.44 | +0.44 |
| 8 | CPE_Cytoplasmic_strands_CS | 0.07 | 0.66 | +0.59 | 0.64 | 0.64 | +0.00 |
| 9 | CPE_Cell_death_Dy | 0.06 | 0.00 | −0.06 | 0.51 | 0.99 | +0.49 |
| 10 | CPE_Nonspecific_degeneration_ND | 0.03 | 0.00 | −0.03 | 0.00 | 0.73 | +0.73 |

### Aggregates

| Metric | IR1 A | IR1 B | IR2 A | IR2 B |
|--------|------:|------:|------:|------:|
| Mean CPE-item score sum (max 7) | 0.87 | 1.66 | 2.41 | 4.91 |
| Mean CPE items present (score > 0, max 7) | 1.92 | 2.96 | 3.78 | 6.34 |
| Mean healthy score sum (max 3) | 3.00 | 3.00 | 2.82 | 1.79 |

### By day — mean CPE-item score sum

| Day | IR1 A | IR1 B | IR2 A | IR2 B |
|----:|------:|------:|------:|------:|
| 1 | 1.60 | 1.75 | 2.56 | 3.48 |
| 2 | 0.65 | 1.70 | 2.36 | 4.22 |
| 3 | 0.55 | 1.55 | 2.36 | 4.81 |
| 4 | 0.70 | 1.75 | 2.15 | 5.71 |
| 5 | 0.85 | 1.55 | 2.60 | 6.34 |

IR2 marks a monotonic day-1→day-5 rise in Culture B (healthy-score sum B: 2.25 → 0.95) with Culture A flat; IR1 is flat in both arms with a constant B>A offset.

---

## Per-item inter-rater agreement (IR1 vs IR2, n = 100)

Binary = strict present/absent. 3-level = Yes / Partial-or-Mild / absent. κ is reported only when both raters vary on the item; otherwise "n/a (constant)" because one rater gave the same mark to every image and κ is uninformative.

| # | Item | IR1 present | IR2 present | Binary % agree | Binary κ | 3-level % exact | 3-level linear-weighted κ |
|---|------|-----:|-----:|-----:|-----:|-----:|-----:|
| 1 | H_Look_Healthy | 100 | 79 | 79 | n/a (constant) | 50 | n/a (constant) |
| 2 | H_well_defined_nuclei | 100 | 100 | 100 | n/a (constant) | 72 | n/a (constant) |
| 3 | H_Cytoplasmic_extensions | 100 | 99 | 99 | n/a (constant) | 61 | n/a (constant) |
| 4 | CPE_Vacuolation_V | 0 | 100 | 0 | n/a (constant) | 0 | n/a (constant) |
| 5 | CPE_Granularity_G | 100 | 100 | 100 | n/a (constant) | 52 | n/a (constant) |
| 6 | CPE_Ballooned_Enlarged_BE | 69 | 39 | 70 | 0.45 | 55 | 0.35 |
| 7 | CPE_Syncytia_Sy | 0 | 28 | 72 | n/a (constant) | 72 | n/a (constant) |
| 8 | CPE_Cytoplasmic_strands_CS | 55 | 100 | 55 | n/a (constant) | 37 | n/a (constant) |
| 9 | CPE_Cell_death_Dy | 3 | 89 | 14 | 0.01 | 14 | 0.01 |
| 10 | CPE_Nonspecific_degeneration_ND | 0 | 50 | 50 | n/a (constant) | 50 | n/a (constant) |

Image-level Spearman correlation of CPE-item score sum (IR1 vs IR2): 0.62 across all 100 images, driven by the arm split; within arm it is 0.18 (Culture A) and −0.23 (Culture B), i.e. no frame-level agreement inside an arm.

High raw % agreement on items 2, 3, 5 reflects both raters marking the feature present on (nearly) every image, not discriminating agreement.

---

## Merged CRO-comparable coding (Pass-1 lexical Ro/D/Re + Pass-2 Dy/V/G; extras from Pass 2)

Strict incidence, n = 50 per path. Source files: `ir_cpe_detections.csv` (IR1), `ir2_cpe_detections.csv` (IR2).

| Column | Source | IR1 path1 | IR1 path2 | IR2 path1 | IR2 path2 |
|--------|--------|------:|------:|------:|------:|
| Dy | P2 | 0.06 | 0.00 | 0.78 | 1.00 |
| Ro | P1 | 1.00 | 1.00 | 0.10 | 0.02 |
| V | P2 | 0.00 | 0.00 | 1.00 | 1.00 |
| D | P1 | 0.58 | 1.00 | 0.04 | 0.02 |
| G | P2 | 1.00 | 1.00 | 1.00 | 1.00 |
| Re | P1 | 1.00 | 1.00 | 0.26 | 0.50 |
| BE | P2 | 0.38 | 1.00 | 0.00 | 0.78 |
| Sy | P2 | 0.00 | 0.00 | 0.00 | 0.56 |
| CS | P2 | 0.14 | 0.96 | 1.00 | 1.00 |
| ND | P2 | 0.00 | 0.00 | 0.00 | 1.00 |
| cpe_detected (any of CRO six) | — | 1.00 | 1.00 | 1.00 | 1.00 |

`cpe_detected` is saturated for both raters (IR1 via Ro/Re/G; IR2 via V/G), so it carries no arm information.

## CRO overlap (22 CRO-labeled frames: 9 path1, 13 path2)

Positives per path (CRO / IR1 / IR2) and pairwise binary agreement across the 22 frames.

| Column | CRO p1 | IR1 p1 | IR2 p1 | CRO p2 | IR1 p2 | IR2 p2 | CRO–IR1 % (κ) | CRO–IR2 % (κ) | IR1–IR2 % (κ) |
|--------|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Dy | 0/9 | 0/9 | 5/9 | 7/13 | 0/13 | 13/13 | 68 (n/a) | 50 (0.19) | 18 (n/a) |
| Ro | 0/9 | 9/9 | 1/9 | 8/13 | 13/13 | 0/13 | 36 (n/a) | 59 (−0.09) | 5 (n/a) |
| V | 1/9 | 0/9 | 9/9 | 4/13 | 0/13 | 13/13 | 77 (n/a) | 23 (n/a) | 0 (n/a) |
| D | 0/9 | 5/9 | 0/9 | 2/13 | 13/13 | 0/13 | 27 (0.04) | 91 (n/a) | 18 (n/a) |
| G | 0/9 | 9/9 | 9/9 | 6/13 | 13/13 | 13/13 | 27 (n/a) | 27 (n/a) | 100 (n/a) |
| Re | 0/9 | 9/9 | 3/9 | 4/13 | 13/13 | 7/13 | 18 (n/a) | 64 (0.23) | 45 (n/a) |
| any | 1/9 | 9/9 | 9/9 | 10/13 | 13/13 | 13/13 | 50 (n/a) | 50 (n/a) | 100 (n/a) |

On the overlap, CRO marks almost nothing on path1 (1/9 frames) and some CPE-type feature on 10/13 path2 frames. Both IRs mark something on every overlap frame. IR2's Pass-2 Dy pattern (path2 13/13, path1 5/9) is directionally closest to CRO's Dy (path2 7/13, path1 0/9); IR1 marks no Dy on these frames. Vacuolation diverges: CRO 1/9 and 4/13, IR1 0 everywhere, IR2 every frame (mostly "Mild").

---

## Compare / contrast

**Agree:**
- **Ballooned/enlarged** is higher in Culture B for both raters (IR1 +0.62, IR2 +0.78 strict incidence). It is the only item with a computable, moderate κ (0.45 binary).
- **Granularity** is marked present on all 100 images by both raters (saturated); IR2 grades it stronger in B (mean 0.63 → 0.92), IR1 does not.
- **Nuclei** and **cytoplasmic extensions** are marked present on (nearly) all images by both.

**Disagree:**
- **Overall level of CPE-type marks:** IR2 marks far more CPE-type features in both arms (mean CPE score sum A 2.41 / B 4.91 vs IR1 0.87 / 1.66).
- **Healthy overall:** IR1 Yes on all 100; IR2 Yes on all A, but Partial 29 / No 21 in B.
- **Cell death, nonspecific degeneration, syncytia:** essentially absent in IR1; in IR2 cell death is marked on 39/50 A and 50/50 B frames, degeneration on 0/50 A vs 50/50 B, syncytia 0/50 A vs 28/50 B.
- **Cytoplasmic strands:** IR1's largest B−A item (+0.82); IR2 marks it Mild/Partial on every image (no arm difference).
- **Vacuolation:** IR1 absent on all 100; IR2 present (mostly Mild) on all 100.

**Direction:** Both raters mark more CPE-type features in Culture B (2% FBS) than Culture A (10% FBS). The size of the difference and the items carrying it differ: IR1 = ballooned + strands; IR2 = degeneration, ballooned, syncytia, cell death, granularity grade, and lower healthy-overall.

---

## Within-rater Pass 1 → Pass 2 shift (IR2)

IR2's Pass-1 free text had zero lexical hits for cell death, ballooning, syncytia, strands, and nonspecific degeneration in either arm, and a small Pass-1 CPE-term difference (mean hits A 0.50 / B 0.60). On the Pass-2 checklist the same rater marks these features frequently, with a large B>A gap. IR1 showed the same type of shift on a smaller scale (Pass 1 had no ballooning/strands; Pass 2 marked both, B>A). The checklist elicits features that open text did not mention; this is a property of the instrument as much as of the images and should be reported alongside any Pass-2 contrast.

---

## Quality caveats

1. **Saturation:** IR2 items 4 (V), 5 (G), 8 (CS) are present on 100/100; IR2 item 2 (nuclei) 100/100. IR1 items 1–3 and 5 are present on 100/100 and item 4/7/10 absent on 100/100. κ is uninformative on all of these.
2. **Templating:** IR1 used 14 distinct 10-item patterns across 100 images (2–3 per culture-day block after day 1). IR2 used 40 (3–7 per culture-day block) — less templated, but day blocks still share patterns.
3. **Magnification:** IR2 recorded a scale bar per frame (400 µm on odd-numbered fields, 200 µm on even). IR2 granularity is graded higher on the 200 µm frames (Yes 28 vs 20; Mild 2 vs 19); other items are similar across the two scales.
4. **Scale vocabularies differ** (IR1 used Minimal / No-minimal / Not apparent; IR2 did not). Strict coding treats Minimal as absent; IR2 has no Minimal marks, so strict and score>0 incidence are identical for IR2.
5. Culture A/B and day are visible in the image IDs for both raters, so within-culture time trends and A↔B contrasts are possible even though conditions were not disclosed.
6. Pass-2 checklist items describe morphology only; "CPE" labels in column names follow this project's CRO descriptor grouping and do not imply a cause.
7. Confluence/coverage was not used.

---

## Bottom line for paper drafting

On the identical 10-item checklist, two blind independent researchers both mark more CPE-type morphology in Culture B (2% FBS) than Culture A (10% FBS), and both mark ballooned/enlarged cells predominantly in B (the one item with moderate agreement, κ = 0.45). Beyond that, item-level agreement is low: IR2 marks cell death, degeneration and syncytia heavily in B and reduces "healthy overall" in B, whereas IR1 marks the same images as healthy throughout and places its B excess on cytoplasmic strands. Several items are saturated for one or both raters. Report the shared direction, the disagreement on which features carry it, and the Pass-1→Pass-2 elicitation shift together.
