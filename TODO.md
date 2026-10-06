# TODO - research roadmap

Shared, living checklist for this repository. Maintained jointly by the author and the research assistant.

**Last updated:** 2026-10-06

Every item links to the markdown file where its discussion or pending input lives. This file only tracks what is open, who it is waiting on, and where to go; the detail and the conversation stay in the linked file.

---

## 1. Active - on Albert

Items that need Albert to read, comment, or decide.

- [ ] **P3 - genetics / sequence origins: review and decide next step**
  - **Discussion:** [`p3_genetics/p3.md`](p3_genetics/p3.md). Albert has left seven `@Albert:` comments (as of 2026-10-06). **Next (assistant):** reply in-doc with `@CPE:` and revise `p3.md` so it reads as a self-contained summary of the P3 section (question, rationale, research angles, findings, adversarial checks, conclusions).
  - Then Albert decides which of the threads in *Genetics beyond current P3 (open extensions)* to open as active work:
    - A1. inoculum / mock sequencing (Step 4)
    - A2. FBS contig audits
    - A3. same stock, different assemblies
    - A4. adversarial clinical-direct + particle + infectivity cases
  - Supporting material: [`p3_genetics/sequence_origins/`](p3_genetics/sequence_origins/). Start with [`P3_step1_progress_summary.md`](p3_genetics/sequence_origins/P3_step1_progress_summary.md), [`P3_step1_protocol.md`](p3_genetics/sequence_origins/P3_step1_protocol.md), [`P3_stock_origin_hops_2026-09-21.md`](p3_genetics/sequence_origins/P3_stock_origin_hops_2026-09-21.md), [`P3_step1_results_draft_2026-09-21.md`](p3_genetics/sequence_origins/P3_step1_results_draft_2026-09-21.md).

- [ ] **P4-P7 - formalized extensions: start now / schedule later / reshape**
  - **Discussion:** [`P4_P7_index.md`](P4_P7_index.md) (record each decision in its *Status* column), plus each stream note. Leave `@Albert:` comments in the stream note:
    - [`p4_serology_antigen/p4.md`](p4_serology_antigen/p4.md) (short form: [`P4_prediction.md`](p4_serology_antigen/P4_prediction.md))
    - [`p5_cryoEM_structure/p5.md`](p5_cryoEM_structure/p5.md) (short form: [`P5_prediction.md`](p5_cryoEM_structure/P5_prediction.md))
    - [`p6_vaccine_seed_identity/p6.md`](p6_vaccine_seed_identity/p6.md) (short form: [`P6_prediction.md`](p6_vaccine_seed_identity/P6_prediction.md))
    - [`p7_cross_lab_repeatability/p7.md`](p7_cross_lab_repeatability/p7.md) (short form: [`P7_prediction.md`](p7_cross_lab_repeatability/P7_prediction.md))
  - Started streams move into their own item below.

- [ ] **R3 - choose the rater-morphology figure set**
  - **Discussion:** [`r3_image_labeling/wrk/viz_figures_review.md`](r3_image_labeling/wrk/viz_figures_review.md). 15 draft figures, each with a `**@Albert:**` line for comments. Recommended headline set: c0, c2, g2, h, j.
  - Waiting on Albert's comments and selection. Then (assistant) regenerate with the requested changes and move the finals into `r3_image_labeling/ir-results/`.

---

## 2. Waiting elsewhere

Not blocking the items in section 1.

- [ ] **R1 - records-request follow-up.** Waiting on an external response; nothing to do until it arrives.
  - **Discussion:** [`r1_isolation_standards_and_practice/wrk/foia_status.md`](r1_isolation_standards_and_practice/wrk/foia_status.md)
- [ ] **R3 - morphology labeling: remaining IR3v rounds.** Round 1 (Pass 1, 10 frames) was received and processed on 2026-10-06. Later rounds will go through the same pipeline and into the figure set when they arrive. IR1 and IR2 Pass-2 results are processed (anonymized tables in [`r3_image_labeling/ir-results/`](r3_image_labeling/ir-results/)).
  - **Discussion:** [`r3_image_labeling/r3.md`](r3_image_labeling/r3.md), section *Status - independent rater results (2026-10-06)*.

---

## 3. Paper wishlists

Drop PDFs into the named **gitignored** `refs/` folders (never commit PDFs). Each wishlist file is the authoritative buy list for its stream and is where to comment on it; this table is a summary.

| Stream | Wishlist (discussion) | Open items | Drop folder |
|--------|----------|------------|-------------|
| **P2** | [`p2_virus_EV_indistinguishable_refs/P2_pdf_wishlist.md`](p2_virus_EV_indistinguishable_refs/P2_pdf_wishlist.md) | Tier A-C closed **except**: re-fetch Chen et al. 2015 *Cell* (`10.1016/j.cell.2015.01.032`). The on-disk P2-044 file is a misfile. | `p2_virus_EV_indistinguishable_refs/refs/` |
| **P3** | [`p3_genetics/sequence_origins/P3_step1_pdf_wishlist.md`](p3_genetics/sequence_origins/P3_step1_pdf_wishlist.md) | None right now. (Duplicate copy at `p3_genetics/P3_step1_pdf_wishlist.md` carries the same list.) | `p3_genetics/refs/sequence_origins/` |
| **R2** | [`r2_negative_controls/R2_pdf_wishlist.md`](r2_negative_controls/R2_pdf_wishlist.md) | Tier-D upgrades: VI44, VI249, VI251, VI266, VI267, VI270, VI271 (VI270 may be a free direct download; VI271 is a web page and optional). | `r1_isolation_standards_and_practice/refs/` (shared with R1) |
| **R1** | [`r1_isolation_standards_and_practice/expansion/paywall_wishlist_combined.md`](r1_isolation_standards_and_practice/expansion/paywall_wishlist_combined.md) | Older paywall expansion list; only if still filling R1 gaps. | `r1_isolation_standards_and_practice/refs/` |
| **P4-P7** | none yet | No buy list until streams are picked (section 1). | `refs/` inside each stream folder |

Notes:

- Ignore `p2_virus_EV_indistinguishable_refs/P2_pdf_request.md` for buying; it is superseded by the lean `P2_pdf_wishlist.md`.
- **Priority if only one pull:** Chen 2015 for P2, then the R2 Tier-D set when convenient. P3 needs no fetch right now.

---

## 4. How we maintain this

- This file is the shared source of truth for open work. Linked files hold the detail and the discussion; this file holds the status.
- **Every item links to its discussion file.** Albert leaves input in that file as inline comments starting with `@Albert:`. Replies from the assistant go directly below, on their own line or blockquote, starting with `@CPE:`. Prefer an existing stream file over a new one; only add a new file when there is no natural home for the discussion.
- **Working notes go in `wrk/`.** Intermediate notes and draft figures live in `wrk/` subfolders inside each stream (e.g. `r3_image_labeling/wrk/`). These folders are tracked, not gitignored, but are kept out of the main reading path. Finished material moves out of `wrk/` into the stream's main files or results folder.
- Items move between sections as they progress (Active -> Waiting -> Done). Tick the box when finished, then move the item to *Done* with a date and a one-line outcome or pointer to where the result is recorded.
- Add new items with an owner (Albert / assistant / external) and a link to the discussion file.
- Keep it public-safe: neutral research-planning language, file paths and role codes only (CRO, IR1, IR2, IR2v, IR3v), no participant names, no private correspondence.
- Update the *Last updated* date on every edit.

---

## Done

- [x] 2026-10-06 - R3 Pass-2 checklist results processed into `r3_image_labeling/ir-results/`.
