# R2 rescore status — 2026-09-19

**Scorer:** cpe-assistant  
**Date:** 2026-09-19 (America/Toronto)  
**Scope:** dual-FBS Isolation-practice IDs in `isolation-refs-dual-fbs_only.csv` not already in `control-cultures-overview.csv`.

## Counts

| Metric | Value |
|--------|-------|
| n before | 28 |
| n scored this run | 78 |
| n after | 106 |
| Backlog / inaccessible (methods) | 1 (VI44) — abstract-only; wishlist PDF |
| PDFs newly pulled for scoring | VI225–VI229 |

## Tier histogram — this batch (n=78)

| Tier | n | % |
|------|---|---|
| A | 3 | 3.8% |
| B | 25 | 32.1% |
| C | 5 | 6.4% |
| D | 45 | 57.7% |

## Tier histogram — full overview (n=106)

| Tier | n |
|------|---|
| A | 7 |
| B | 31 |
| C | 6 |
| D | 62 |

## Isolation-stage NC

- This batch: `nc_isolation_stage=yes` = **29/78 (37.2%)**
- Full overview: **39/106 (36.8%)**

## Notable Tier A hits (this batch)

| ID | Why |
|----|-----|
| **VI53** | Uninfected MDBK control under similar conditions; plaque/NC wells share post-inoculum DMEM+2% FBS |
| **VI57** | Explicit mock infection with 2% FBS media (matched to infection regime) |
| **VI93** | Uninfected blank control under identical culture conditions; DMEM+2% FBS for blank and virus controls |

## Tier C highlights

- **VI85** `C-mismatch`: Isolation-stage NC present, but NC “maintained using sterile PBS” while test wells use DMEM+2% FBS (M3 fail; conservative).
- **VI55, VI56, VI228, VI232** `C-stage`: NC language is animal mock / assay / scramble-PMO / serology antigen — not Isolation-stage culture NC.

## Method notes

1. Followed `control-cultures.md` decision tree; ambiguity → worse tier; no invented mocks.
2. Sources: Europe PMC fullTextXML for OA PMC IDs; local `r1/expansion/` HTML/pdftxt where present; JSTAGE/Arch Razi/Redalyc PDFs for VI225–229.
3. **Machine path** `C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology` was **not writable from this box** (no ListMachines/CopyFromBox in harness). Outputs written under `/workspace/r2/` (and mirrored notes under `/workspace/review_r1r2/`). Parent should CopyFromBox → MSI `r2_negative_controls/`.
4. Backup: `control-cultures-overview.csv.bak_20260919`.
5. No git commit.

## Backlog

| ID | Reason |
|----|--------|
| VI44 | IJID paywall; abstract only — add PDF then rescore |
| Expanded dual-coded non-`dual-fbs_only` rows with OA | Not in this batch primary list; optional follow-on |

## Files touched

- `control-cultures-overview.csv` (+78 rows)
- `control-cultures-justification-notes.md` (dated section)
- `r2_rescore_status_2026-09-19.md` (this file)
- `r2.md` (light TODO/status)
