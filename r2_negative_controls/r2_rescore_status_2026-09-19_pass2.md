# R2 rescore status — 2026-09-19 pass2

**Scorer:** cpe-assistant  
**Date:** 2026-09-19 (America/Toronto)  
**Scope:** dual-FBS IDs in best available `isolation-refs-dual-fbs_only.csv` not already in `control-cultures-overview.csv`.

## Dual source caveat

| Source | n | Notes |
|--------|---|-------|
| MSI path (user claim) | ~170 | **Not accessible** this run (executor lacks ListMachines / CopyToBox / Shell machineId). |
| Local best: `r1/plots/isolation-refs-dual-fbs_only.csv` | **123** | Used for exact miss list (includes VI99–VI121 paywall-batch + ADV/HOLD VI234–VI246). |
| Stale `/workspace/isolation-refs-dual-fbs_only.csv` | 103 | Fully covered by pass1; miss vs overview = 0. |

Exact miss this pass = dual∖overview = **21** IDs: VI99, VI105, VI109, VI110, VI111, VI112, VI115, VI118, VI121, VI234, VI235, VI236, VI237, VI239, VI240, VI241, VI242, VI243, VI244, VI245, VI246.

If MSI dual truly has n=170 (VI247–VI293 etc.), those IDs remain an **external backlog** until dual CSV is CopyToBox’d.

## Counts

| Metric | Value |
|--------|-------|
| n before | 106 |
| n scored this pass | 21 |
| n after | 127 |
| Remaining vs local dual | **0** |
| Possible MSI-only dual backlog | unknown (need fresh dual from MSI) |

## Tier histogram — this batch (n=21)

| Tier | n | % |
|------|---|---|
| A | 1 | 4.8% |
| B | 1 | 4.8% |
| C | 1 | 4.8% |
| D | 18 | 85.7% |

## Tier histogram — full overview (n=127)

| Tier | n |
|------|---|
| A | 8 |
| B | 32 |
| C | 7 |
| D | 80 |

## Isolation-stage NC

- This batch: `nc_isolation_stage=yes` = **2/21 (9.5%)**
- Full overview: **41/127 (32.3%)**

## Notable Tier A

| ID | Why |
|----|-----|
| **VI121** | Same-slide central uninoculated control; L-15M (2% FCS) shared maintenance; allowed inference M1–M6 |

## Tier C

| ID | Code | Why |
|----|------|-----|
| **VI244** | C-stage | Uninfected cells = flow-cytometry assay baseline, not Isolation culture NC |

## Tier B highlight

| ID | Why |
|----|-----|
| **VI111** | Control cells / control tissue cultures for CPE; M3 for NC not explicit → B |

## Method notes

1. Followed `control-cultures.md` decision tree; ambiguity → worse tier; no invented mocks.
2. Sources: local PDFs under `r1/pdfs/` (VI99–VI121); PLOS ONE / CDC EID / PMC / protocols.io / IntechOpen / PubMed abstracts for ADV/HOLD IDs.
3. Machine path not writable from this box. Outputs under `/workspace/r2_negative_controls/` (and `/workspace/r2/`). Parent: CopyFromBox → MSI `r2_negative_controls/`.
4. Backup: `control-cultures-overview.csv.bak_20260919_pass2`.
5. No git commit.

## Backlog

| Item | Reason |
|------|--------|
| Fresh MSI `isolation-refs-dual-fbs_only.csv` (n≈170) | Pull via CopyToBox; score any new IDs (VI247+) |
| VI239, VI240–242, VI243, VI246 | Full PDF preferred (abstract/landing scored conservatively D) |
| VI44 (from pass1) | IJID paywall still wishlist |

## Files touched

- `control-cultures-overview.csv` (+21 rows → n=127)
- `control-cultures-justification-notes.md` (pass2 section)
- `r2_rescore_status_2026-09-19_pass2.md` (this file)
- backups: `control-cultures-overview.csv.bak_20260919_pass2`
