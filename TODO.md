# TODO - research roadmap

Shared checklist for this repository. **Last updated:** 2026-11-18

Each item names an assignee (**Albert** or **CPE**, the research assistant) and links the file where its discussion lives. Per-stream details live in that stream's `rN.md` / `pN.md`; this file is the cross-stream priority list.

---

## Mini-paper candidates (flagged 2026-11-18)

P2 and P3 are wrapped and carry a self-contained **"in one screen" mini-paper summary** at the top of their `p*.md` (consumable for `tex/` drafting). The streams below are at the same "wrapped / almost wrapped" stage and are **prime for the same treatment**. Albert to instruct the owning agent.

| Stream | State | Prime? | Action |
|---|---|---|---|
| **P4** serology / antigen | Almost wrapped — provenance arm supported; reactivity arm supported-but-narrower; conclusion + adversarial balance written | **Prime now** | Add one-screen summary to top of `p4_serology_antigen/p4.md` |
| **P7** cross-lab repeatability | Wrapped — 18 rows all `[VERIFIED src]`; CNJ057 verdict written; 13 snippets | **Prime now** | Add one-screen summary to top of `p7_cross_lab_repeatability/p7.md` |
| **P1** history | Closed for drafting (`P1_for_paper.md` is the closed package) | **Prime (light)** | Optionally standardize a one-screen summary in `p1_history/p1.md` to match P2/P3 |
| **R2** negative controls | Frozen — 173 rows (A/B/C/D 12/40/14/107); snippets ready | **Prime (light)** | Add one-screen summary to top of `r2_negative_controls/r2.md` |
| **R5** pre-cell purification census | Wrapped — `R5_synthesis.md` drafted from 29 sources; CNJ058 "supported"; paper-ready prose + adversarial balance | **Prime now** | Add one-screen summary to top of `r5_precell_virus_purification_census/r5.md` |
| **R6** non-viral mechanisms | Framework wrapped — 12 mechanisms, most `[VERIFIED src]`; corpus + bibliography finalized ("R6 wrap up") | **Prime (one step)** | Write `R6_synthesis.md` + upgrade CNJ059, then one-screen summary in `r6_nonviral_morphology_mechanisms/r6.md` |
| **R1** isolation corpus | Core done; paste-ready `R1_for_paper_2026-09-19.md` | **Blocked on data hygiene** | Freeze numbers first (Priority 3) |
| **R3** image labeling | IR1/IR2 done; IR3v Pass 2 pending | **Blocked on IR3v Pass 2** | Finalize after Pass 2, then summarize |

Not prime (do not instruct yet): **P5** (not started), **P6** (not started), **R4** (parked — FOIA).

---

## Priority 1 — blocking the paper

- [ ] **Albert — review the paper draft** [`tex/main.tex`](tex/main.tex): read the drafted sections, check the two assumption blocks (FOIA, IR3v), and answer the 7 open decisions in [`tex/wrk/paper_notes.md`](tex/wrk/paper_notes.md).
- [ ] **IR3v rater → CPE — R3 IR3v Pass 2.** Checklist sent 2026-10-14; rater has started. CPE processes Pass 2 (99 unique frames) and replaces the provisional IR3v numbers in the paper. [`r3_image_labeling/r3.md`](r3_image_labeling/r3.md).
- [ ] **Albert — R3 figure set (Fig 2).** Choose the rater-morphology figures (15 drafts; suggested c0, c2, g2, h, j). [`r3_image_labeling/wrk/viz_figures_review.md`](r3_image_labeling/wrk/viz_figures_review.md).
- [ ] **Albert — R3 CRO label coding questions** (rounded vs "round cells", vacuolation vs "bright vesicles", refractile vs "bright reflective points", hedged mentions, shared two-frame descriptions, path1 "101" typo, group-level notes, CSV rename, briefing-condition assignment). [`r3_image_labeling/cro-results/cro_labels_consolidation.md`](r3_image_labeling/cro-results/cro_labels_consolidation.md).
- [ ] **CPE — extend the paper draft** as Albert's review comments and pending data come in. [`tex/wrk/paper_notes.md`](tex/wrk/paper_notes.md).

## Priority 2 — prime streams → mini-papers

- [ ] **CPE — P4 mini-paper.** Write a self-contained "in one screen" summary at the top of [`p4_serology_antigen/p4.md`](p4_serology_antigen/p4.md) (prediction → methods → results → adversarial balance → conclusion → paper integration).
- [ ] **CPE — P7 mini-paper.** Same treatment for [`p7_cross_lab_repeatability/p7.md`](p7_cross_lab_repeatability/p7.md).
- [ ] **CPE — P1 summary.** Standardize a one-screen summary at the top of [`p1_history/p1.md`](p1_history/p1.md) (source: `P1_for_paper.md`).
- [ ] **CPE — R2 mini-paper.** One-screen summary at the top of [`r2_negative_controls/r2.md`](r2_negative_controls/r2.md).
- [ ] **CPE — R5 mini-paper.** One-screen summary at the top of [`r5_precell_virus_purification_census/r5.md`](r5_precell_virus_purification_census/r5.md) (source: `R5_synthesis.md`).
- [ ] **CPE — R6 freeze + mini-paper.** Write `R6_synthesis.md`, upgrade CNJ059 in `CLAIMS.md`, then one-screen summary at the top of [`r6_nonviral_morphology_mechanisms/r6.md`](r6_nonviral_morphology_mechanisms/r6.md).

## Priority 3 — unblock the near-prime streams

- [ ] **CPE — R1 data hygiene (before Results freeze).** DOI backfill in `isolation-refs.csv`; reconcile the FBS parse drift (`fbs_coded=yes` 166 vs plotter 169 vs archived dual 170); resolve the 11 abstract-only rows (fetch list in `R1_pdf_wishlist.md` §B); run the full enrichment sweep (TPB/LAH/yeast/peptone). [`r1_isolation_standards_and_practice/r1.md`](r1_isolation_standards_and_practice/r1.md).
- [ ] **CPE — R2 VI117 control-tier scoring.** Score Deig/Rie/Watkins 1970 (uninfected monolayers degenerate under 1–2% FCS maintenance) A–D. [`r2_negative_controls/r2.md`](r2_negative_controls/r2.md). *(Not a blocker; VI271 is the only outstanding wishlist row — a CDC web page, optional, stays D.)*

## Priority 4 — low-priority depth (optional)

- [ ] **CPE — R5 optional depth.** Fetch the 4 book-length sources + the optional Schlesinger secondary still on [`R5_pdf_wishlist.md`](r5_precell_virus_purification_census/R5_pdf_wishlist.md) if ever wanted; not needed for CNJ058.
- [ ] **CPE — R6 optional fetch.** Remaining `R6-0xx` wishlist PDFs (depth only); confirm R6-004 peer-review status before any load-bearing use. [`r6_nonviral_morphology_mechanisms/r6.md`](r6_nonviral_morphology_mechanisms/r6.md).

## Parked / waiting

- [ ] **R4 — PARKED until the FOIA meeting (Monday).** Hold the non-isolation protocol/practice search and the landscape survey until the FOIA-team meeting outcome. Then code the public-records response and replace the `[ASSUMED -- pending FOIA]` text. [`r4_non-isolation_standards_and_practice/r4.md`](r4_non-isolation_standards_and_practice/r4.md) · [`wrk/foia_status.md`](r4_non-isolation_standards_and_practice/wrk/foia_status.md).
- [ ] **P5 / P6 — not started.** Formalized predictions exist (`P5_prediction.md`, `P6_prediction.md`). Decide start vs schedule vs reshape after the paper core lands. [`P4_P7_index.md`](P4_P7_index.md).

---

## Stale / completed items — removed this pass (annotated)

Removed because completed or superseded; outcomes live in the stream files they linked and in git history.

- **R2 full-text fetch** (VI44/VI239/VI240/VI243/VI249/VI251/VI266/VI267/VI270/VI271) — **completed 2026-11-18** (Pass4 re-score: VI249→A, VI266→B, VI267→B; only VI271 remains — a CDC web page, optional, stays D).
- **P3 in-doc reply + revise `p3.md`** — **completed** (`p3.md` now opens with the mini-paper; all `@Albert:` notes resolved).
- **P4–P7 "start now / schedule later / reshape"** — **superseded**: P4 and P7 have started (and are now prime for mini-papers); P5/P6 remain not started. `P4_P7_index.md`'s Status column **was updated 2026-11-18** to reflect this.
- **`r5.md` / `r6.md` status headers + TODO lists are stale** — `r5.md`'s TODO (8 unchecked items) and `r6.md`'s "Scaffold + Round 1 seeds" header predate the actual work (`R5_synthesis.md` with 29 sources; `R6_mechanisms.md` with 12 `[VERIFIED src]` mechanisms; the "R6 wrap up" commit). Clean them as part of the R5/R6 mini-paper pass (Priority 2).
- Older "Done" entries (2026-10-06 … 2026-10-14) — removed; outcomes recorded in the stream files.

---

## Conventions

- Every item names an assignee and links its discussion file. Albert comments there as `@Albert:`; CPE replies as `@CPE:`.
- Items move Not started → In progress → In review → Done; Done entries are pruned from this file (outcomes recorded in the stream).
- Working notes go in tracked `wrk/` folders. Public-safe language and role codes only (CRO, IR1, IR2, IR2v, IR3v).
