# Rater image package notes

**Folder:** `images_rater_blinded/` (flat; no subfolders)  
**Mapping:** `images_rater_blinded_mapping.csv`  
**Excluded originals:** `images_rater_blinded_excluded.csv`

## Culture codes

| Code | Original experiment path |
|------|--------------------------|
| CultureA | path1 |
| CultureB | path2 |

## Path 2 day 3 — retry vs parent (binary check)

All parent `EXP_path2_passage4_30x.tif` vs retry `…30xa.tif` pairs were compared by **SHA-256**.

| Pair | Identical binary? |
|------|-------------------|
| 301 vs 301a | No |
| 302 vs 302a | No |
| 303 vs 303a | No |
| 304 vs 304a | No |
| 306 vs 306a | No |
| 307 vs 307a | No |
| 308 vs 308a | No |
| 309 vs 309a | No |
| 310 vs 310a | No |
| 305 | Parent **missing**; only `305a` exists |

**Conclusion:** Retry files are **not copy-duplicates** of the parent set. They are separate files (new captures or re-saves).

## CRO explanation (Excel)

From `refs/20250620 Vero Cells Reporting_v1.xlsx` (Sheet1 (2), path2 day corresponding to 2025-06-18 / EXP day 3):

> EXP_path2_passage 4_301a-310a — *I get an error that some of the files might have been corrupted therefore a new set "a" was taken.*

The light-microscope description PDF lists both `301-310` and `301a-310a` for Path 2 Day 3.

## Clean-package decision

| Item | Decision |
|------|----------|
| Culture B day 3 (default) | Prefer the `a` recapture set for non-CRO fields. Rename to `CultureB_day3_01.tif` … `_10.tif` (**no `a` in rater names**). |
| Culture B day 3 IDs in `cro_cpe_detections.csv` (303, 307, 308) | Use **exact non-`a` originals** so the rater package matches CRO-scored files (SHA-256 verified). |
| Other parent day-3 non-`a` files | Excluded where superseded by `a` (possible corruption; incomplete set). |
| Culture B day 2 `212`, `213` | **Excluded** — outside CRO listed sequence `201-210`; `211` absent. |
| Other EXP frames | Included as `Culture{A\|B}_day{D}_{01-10}.tif` |

## CRO detection coverage (`cro-results/cro_cpe_detections.csv`)

All **22** path+id rows are in the rater package as **exact** original files (`missing_count=0`). Path2 day3 CRO ids use non-`a` originals after explicit swap for correlation with CRO labels.

## Package size

- **Included for raters:** 100 images  
- **Excluded from rater package:** see `images_rater_blinded_excluded.csv` (still present under `images/EXP stage/`)

## Magnification

CRO notes 10x and 20x objectives are used (scale bar on images). Per-file mag is not always explicit in every EXP filename; brief states 10x or 20x.
