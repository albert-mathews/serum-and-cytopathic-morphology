# TODO - research roadmap

Shared checklist for this repository. **Last updated:** 2026-10-15

Each item has an assignee (**Albert** or **CPE**, the research assistant) and links to the file where its input is waiting. Discussion happens in that file, not here.

---

## Not started

- [ ] **Albert - P4-P7: start now / schedule later / reshape each stream.** Record the decision in the *Status* column of [`P4_P7_index.md`](P4_P7_index.md); comments go in the stream notes ([`p4.md`](p4_serology_antigen/p4.md), [`p5.md`](p5_cryoEM_structure/p5.md), [`p6.md`](p6_vaccine_seed_identity/p6.md), [`p7.md`](p7_cross_lab_repeatability/p7.md)).
- [ ] **Albert - fetch R2 full texts to bring papers back into the analysis.** 10 papers are excluded because only abstracts were available: VI44, VI239, VI240 (= VI241, VI242, same paper), VI243, VI249, VI251, VI266, VI267, VI270, VI271. List and links: [`r2_negative_controls/R2_pdf_wishlist.md`](r2_negative_controls/R2_pdf_wishlist.md).
- [ ] **CPE - R4: expand the non-isolation protocol search** (protocols outside virus isolation, then reports of practice under them). Plan: [`r4_non-isolation_standards_and_practice/r4.md`](r4_non-isolation_standards_and_practice/r4.md).

## In progress

- [ ] **CPE - P3: reply in-doc to Albert's `@Albert:` comments and revise `p3.md`** into a self-contained P3 summary; then Albert chooses which extension threads (A1-A4) to open. Discussion: [`p3_genetics/p3.md`](p3_genetics/p3.md).
- [ ] **IR3v (rater) then CPE - R3: IR3v Pass 2 in progress.** Checklist sent by Albert 2026-10-14; the rater has started. Waiting on the rater; then CPE processes Pass 2 (99 unique frames, duplicate excluded) and replaces the provisional IR3v numbers in the paper. Discussion: [`r3_image_labeling/r3.md`](r3_image_labeling/r3.md).
- [ ] **CPE - R4: code the public-records response when it arrives** and replace the `[ASSUMED -- pending FOIA]` text in the paper. Status: [`r4_non-isolation_standards_and_practice/wrk/foia_status.md`](r4_non-isolation_standards_and_practice/wrk/foia_status.md).
- [ ] **CPE - paper: extend the draft** as Albert's review comments and pending data come in. Notes: [`tex/wrk/paper_notes.md`](tex/wrk/paper_notes.md).

## In review (waiting on Albert)

- [ ] **Albert - review the paper draft** [`tex/main.tex`](tex/main.tex): read the drafted sections, check the two assumption blocks (FOIA, IR3v coding) and answer the 7 open decisions. Leave `@Albert:` lines in [`tex/wrk/paper_notes.md`](tex/wrk/paper_notes.md).
- [ ] **Albert - R3: choose the rater-morphology figure set** (15 drafts; suggested c0, c2, g2, h, j). Comment on each `@Albert:` line in [`r3_image_labeling/wrk/viz_figures_review.md`](r3_image_labeling/wrk/viz_figures_review.md). CPE then regenerates finals into `ir-results/`.
- [ ] **Albert - R3: resolve CRO label coding questions** (rounded vs "round cells", vacuolation vs "bright vesicles", refractile vs "bright reflective points", hedged mentions, shared two-frame descriptions, path1 202 "101" typo, group-level notes, CSV rename, CRO briefing-condition assignment). Answer inline in [`r3_image_labeling/cro-results/cro_labels_consolidation.md`](r3_image_labeling/cro-results/cro_labels_consolidation.md). CPE then applies them in `build_cro_labels.py`.

## Done

- [x] 2026-10-14 - Albert/CPE - R3 duplicate frame decision: `CultureB_day4_08` (= `CultureB_day4_07`) excluded for all raters via [`frames_excluded_from_analysis.csv`](r3_image_labeling/frames_excluded_from_analysis.csv); results, figures and paper recomputed on 99 unique frames (50 A / 49 B). Note: [`tex/wrk/paper_notes.md`](tex/wrk/paper_notes.md).
- [x] 2026-10-14 - CPE - R1/R2: VI47 merged into VI29 (same article; row and duplicate PDF removed); R2 now 173 rows (A/B/C/D 11/38/14/110). Mislabelled VI44 dengue PDF deleted. See [`r2.md`](r2_negative_controls/r2.md).
- [x] 2026-10-14 - CPE - IR3v Pass 1 recorded in `r3_image_labeling/ir-results/` (`ir3v_*`, `IR3v_pass1_side_by_side.md`) with the rater's clarifications applied; figures regenerated; paper numbers updated.
- [x] 2026-10-14 - CPE - `tex/` split into `sections/` and `tables/` (driver `main.tex`; compiles).
- [x] 2026-10-14 - CPE - P3 superseded attempts moved to [`p3_genetics/archive/`](p3_genetics/archive/README.md) with an index.
- [x] 2026-10-14 - CPE - R2 174 vs 170 rows explained in [`r2.md`](r2_negative_controls/r2.md); VI44 PDF identified as an old ID collision (not renamed).
- [x] 2026-10-14 - CPE - Paper skeleton started in `tex/main.tex` (PLOS Biology structure); notes in `tex/wrk/paper_notes.md`.
- [x] 2026-10-14 - CPE - One literature catalogue per stream; redundant wishlists removed (see table below).
- [x] 2026-10-14 - CPE - `cro_labels_consolidation.md` re-encoded as clean UTF-8 (one Windows-1252 byte fixed).
- [x] 2026-10-06 - CPE - R3 Pass-2 checklist results processed into `r3_image_labeling/ir-results/`.

---

## Literature catalogues (one per stream)

PDFs go in the gitignored `refs/` folder named below; never commit PDFs.

| Stream | Catalogue / wishlist | Have / used / still needed | Drop folder |
|---|---|---|---|
| P2 | [`P2_pdf_catalogue.md`](p2_virus_EV_indistinguishable_refs/P2_pdf_catalogue.md) | 32 IDs on disk / 23 used (quoted) / 0 needed | `p2_virus_EV_indistinguishable_refs/refs/` |
| P3 | [`P3_pdf_catalogue.md`](p3_genetics/sequence_origins/P3_pdf_catalogue.md) | 171 files / 181 bibliography entries / 0 required (2 optional) | `p3_genetics/refs/sequence_origins/` |
| R2 | [`R2_pdf_wishlist.md`](r2_negative_controls/R2_pdf_wishlist.md) | 173 scored rows / 7 Tier-D upgrades wanted (optional) | `r1_isolation_standards_and_practice/refs/` |
| R1 | [`paywall_wishlist_combined.md`](r1_isolation_standards_and_practice/expansion/paywall_wishlist_combined.md) | 18 of 25 on disk / 7 missing (optional) | `r1_isolation_standards_and_practice/refs/` |
| P1 | [`P1_BIBLIOGRAPHY.md`](p1_history/P1_BIBLIOGRAPHY.md) | closed for drafting | `p1_history/refs/` |

---

## Conventions

- Every item names an assignee and links to its discussion file. Albert comments there as `@Albert:`; CPE replies below as `@CPE:`.
- Items move Not started -> In progress -> In review -> Done; Done entries get a date and a one-line outcome.
- Working notes go in tracked `wrk/` folders. Public-safe language and role codes only (CRO, IR1, IR2, IR2v, IR3v).