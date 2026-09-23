# R2 rescore status — 2026-09-19 pass3

**Scorer:** cpe-assistant  
**Date:** 2026-09-19 (America/Toronto)  
**Scope:** ALL dual-FBS IDs in fresh `r1/plots/isolation-refs-dual-fbs_only.csv` (n=170) still missing from `control-cultures-overview.csv`.

## Dual source

| Source | n | Notes |
|--------|---|-------|
| Fresh on box: `r1/plots/isolation-refs-dual-fbs_only.csv` | **170** | Copied from MSI; authoritative this pass |
| Overview before pass3 | 127 | After pass2 |
| Exact miss = dual∖overview | **47** | VI247–VI293 (matches `pass3_miss_ids.txt`) |

## Counts

| Metric | Value |
|--------|-------|
| n before | 127 |
| n scored this pass | **47** |
| n after | **174** |
| Remaining dual∖overview | **0** |

## Tier histogram — this batch (n=47)

| Tier | n | % |
|------|---|---|
| A | 3 | 6.4% |
| B | 6 | 12.8% |
| C | 7 | 14.9% |
| D | 31 | 66.0% |

## Tier histogram — full overview (n=174)

| Tier | n |
|------|---|
| A | 11 |
| B | 38 |
| C | 14 |
| D | 111 |

## Isolation-stage NC

- This batch: `nc_isolation_stage=yes` = **9/47 (19.1%)** (3A+6B)
- Full overview: **50/174 (28.7%)**

## Notable Tier A

| ID | Why |
|----|-----|
| **VI272** | Same-plate sterile culture-medium NC under universal L15+2% FBS maintenance |
| **VI281** | Explicit medium (NC) then shared infection medium (5% FBS+DMSO) |
| **VI288** | Control flasks: MM in place of homogenate; then L-15+2% FBS to all FtGF flasks |

## Tier C

| ID | Code | Why |
|----|------|-----|
| VI247 | C-stage | Plaque titration non-infected control |
| VI274 | C-stage | TCID50 cells-only column |
| VI275 | C-stage | Titration Hanks’ NC |
| VI277 | C-stage | IIFT / neutralization cell NC |
| VI279 | C-stage | IF mock / animal mock |
| VI289 | C-stage | TCID50 maintenance-medium NC |
| VI293 | C-stage | Plaque/IF medium-only mock (adaptation) |

## Tier B highlight

| ID | Why |
|----|-----|
| VI253 | Uninfected Vero E6 figure panel; M3 for NC not explicit |
| VI265 | Sterile PBS monolayer NC; MM serum % under-specified |
| VI276 | Mock-infected morphology vs Isolation CPE; mock medium unknown |
| VI280 | Mock-infected controls vs PEDV CPE; mock medium unknown |
| VI286 | Mock-infected CPE figure; mock medium unknown |
| VI291 | Parallel uninfected Vero-E6 flask during Isolation passages; M3 under-specified |

## Soft / inaccessible (scored D conservatively)

| ID | Reason |
|----|--------|
| VI251 | SciELO 403/timeout; dual quotes lack NC language |
| VI249, VI266, VI267 | Abstract-only (publisher paywall) |
| VI270 | IFREMER PDF timeout / archive TLS fail |
| VI271 | CDC lab-tool URL 404/403 |

Re-open these if MSI local PDFs under `isolation_practice/` become CopyToBox-accessible (`machineId 04858ede-3dda-4a66-bccd-83193e310018`).

## Method notes

1. Followed `control-cultures.md` decision tree; ambiguity → worse tier; no invented mocks.
2. MSI desktop PDF path not usable from this executor (no machine file tools in MCP catalog).
3. Backup: `control-cultures-overview.csv.bak_20260919_pass3` (+ justification notes bak).
4. No git commit.
5. Outputs under `/workspace/r2_negative_controls/` for parent CopyFromBox.

## Backlog (optional PDF upgrade — not dual∖overview)

| Item | Reason |
|------|--------|
| VI251, VI270, VI271 | Full text blocked; currently D |
| VI249, VI266, VI267 | Abstract-only D |
| VI44 (pass1) | IJID paywall wishlist |

## Files touched

- `control-cultures-overview.csv` (+47 → n=174)
- `control-cultures-justification-notes.md` (pass3 section)
- `r2_rescore_status_2026-09-19_pass3.md` (this file)
- `scores_pass3.json`, `miss_pass3.json`, `texts_pass3/`, `extracts_pass3/`
- backups: `*.bak_20260919_pass3`
