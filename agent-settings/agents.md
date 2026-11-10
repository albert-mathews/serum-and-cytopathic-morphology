# Agent manifest and shared behavior contract

## Stream → agent map

| Agent | Folder | Topic |
|-------|--------|-------|
| `general` | (repo-wide) | Coordinator: cross-stream questions, routing, repo structure, drafting |
| `r1` | `r1_isolation_standards_and_practice/` | Isolation standards and practice (dual-serum corpus + guidelines) |
| `r2` | `r2_negative_controls/` | Isolation-stage negative controls (tiers A–D) |
| `r3` | `r3_image_labeling/` | Image labeling / CPE morphology (CRO + raters) |
| `r4` | `r4_non-isolation_standards_and_practice/` | Non-Isolation standards and practice (FBS × CPE landscape) |
| `p1` | `p1_history/` | History of serum / medium practice |
| `p2` | `p2_virus_EV_indistinguishable_refs/` | EV–virion particle indistinguishability |
| `p3` | `p3_genetics/` | Genetics / sequence-origin inheritance |
| `p4` | `p4_serology_antigen/` | Serology / antigen provenance |
| `p5` | `p5_cryoEM_structure/` | Cryo-EM / structure |
| `p6` | `p6_vaccine_seed_identity/` | Vaccine master-seed identity (process ontology) |
| `p7` | `p7_cross_lab_repeatability/` | Cross-lab repeatability |

Each stream's entry point is its main markdown (`rN.md` / `pN.md`), which owns that stream's single TODO list.

## Shared behavior contract (every agent)

1. **Claims.** Cite `C###` from `CLAIMS.md` instead of restating an established point; add/update claims
   there when a finding lands or a number changes.
2. **Conventions.** Follow `CONVENTIONS.md` (evidence tags, Mermaid diagrams, role codes, single-TODO-per-stream).
3. **Research.** Follow `research-strategy.md`; a paywalled/blocked full text goes on the stream's
   `<STREAM>_pdf_wishlist.md`.
4. **Environment.** Run Python through the shared `tools/venv`; see `environment.md`.
5. **Anonymity.** Role codes only (CRO, IR1, IR2, IR2v, IR3v) in tracked files.
6. **Git.** No commit/push unless Albert asks; leave changes unstaged for GitHub Desktop.
7. **Scanned PDFs.** Image-only PDFs are OCR'd with `tools/ocr_pdf.py` before extraction; improvements go
   back into that tool (see `tools/README.md`), so future agents inherit them.