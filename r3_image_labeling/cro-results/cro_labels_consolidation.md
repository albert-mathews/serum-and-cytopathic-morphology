# CRO labels: source, coding rules and consolidation record

**Status:** processed CRO labels rebuilt from the CRO image-description report under the conservative single-frame rule (2026-10-06). Working-tree change, not yet committed.

## Source and extraction

- **Source of truth:** the CRO light-microscopy image-description report (docx, dated 2025-06-23). The docx itself is not tracked (its file metadata carries personal information); its paragraph text is exported verbatim, without metadata, to `cro_image_descriptions.txt` (127 lines; regenerate with `python build_cro_labels.py --export-docx "<report.docx>"`, which needs python-docx).
- **Structure:** title and microscope note; PREP sections (passages 1–3, culture expansion; not part of the 100-frame rating set); then `EXPERIMENT P4 Day N:` sections. Each day has, per culture, one **group/range** description (`EXP_pathX_passage4_N01-N10:`; path2 day 3 is `301-310, 301a-310a`) followed by **single-image** descriptions (`EXP_pathX_passage4_NNN: …`). Some single-image descriptions name two frames together (`307 and 308`, `405, 406`, `503 & 504`, `507, 508`); these name each frame individually and are applied to each named frame.
- **Builder:** `build_cro_labels.py` (Python standard library only) parses the EXPERIMENT section of the text export, splits it at each `EXP_pathX_passage4_…:` heading, and codes each description with fixed regular expressions (rules in the script header). Hedged mentions (e.g. "might be vacuoles", "most likely dying cells") count as named and are listed in `hedged_terms`.

## Outputs

| File | Unit | Used in per-frame analysis / figures |
|---|---|---|
| `cro_cpe_detections.csv` | **Canonical.** One row per frame with its own single-image description: 22 frames (path1 101, 103, 104, 201, 202, 305, 401, 406, 501; path2 101, 201, 202, 303, 307, 308, 402, 405, 406, 503, 504, 507, 508). CPE-type CRO_Dy, CRO_Ro, CRO_V, CRO_D, CRO_G, CRO_Re and healthy-type CRO_H_* (8 terms), binary; plus blinded_id, culture, day, described_as, hedged_terms and the verbatim description. | Yes |
| `cro_group_level_notes.csv` | One row per group/range description (10 groups), same coding, `used_in_per_frame_analysis = 0`. Lower specificity. | **No** |
| `cpe_detection_results_cro.json` | Derived JSON view of the canonical CPE-type columns (same values). | (same data as canonical) |

**Single-frame rule:** a frame's labels come only from a description that names that frame. Group descriptions are not applied to member frames and do not enter any per-frame incidence, agreement statistic or figure.

## The 8 frame-level disagreements (spreadsheet export vs previous deposit), resolved from the report text

| Frame | Feature | Report text (frame's own description) | Spreadsheet | Previous deposit | Resolved |
|---|---|---|---|---|---|
| path1 406 | Vacuolation | "Some cells have clear bright vesicles." | 0 | 1 | **1** (vesicle coded as vacuolation; the report uses "bright spots (vacuoles)" for the same appearance at path2 303/402) |
| path2 202 | Refractile | "Some cells have bright reflective points." | 0 | 1 | **0** ("refractile" not stated; the report uses "refractile" for whole cells at path2 402) |
| path2 303 | Rounded | "Multiple cells appear rounded." | 0 | 1 | **1** |
| path2 405, 406 | Rounded | "Some round cells have granular and irregular shape, most likely dying cells or debris." | 0 | 1 | **1** ("round cells" coded as rounded) |
| path2 507, 508 | Rounded | same text as 405/406 | 0 | 1 | **1** |
| path2 503, 504 | Refractile | "Some bright reflective points that might be vacuoles are present. … floating bright cells that might be dying/cell debris …" | 0 | 1 | **0** |

Effect on the Culture A vs B comparison: none on direction. CRO CPE-type terms are named on 1/9 Culture A frames and 10/13 Culture B frames before and after; refractile on Culture B frames goes from 4/13 to 1/13 (path2 402 only); the mean share of the six CPE-type terms is A 0.02, B 0.36 (previously B 0.40).

The spreadsheet also marked "Bright" (healthy-type) for path1 406 ("bright vesicles"), path2 202 ("bright reflective points") and path2 503/504 ("floating bright cells that might be dying"); the canonical file codes "Bright" only for bright cells not described as dying or debris, so these four are 0 (see the ambiguities below).

## Verification diff before removing the spreadsheet export

Both previous files cover the same 22 frames as the canonical file; every value differing from the canonical file is listed (all other cells are identical). Section C checks the spreadsheet's group rows against `cro_group_level_notes.csv`, which carries the group-level information forward.

```
## A. cro_cpe_detections.csv (previous tracked deposit) vs canonical, CPE-type columns
frames: previous 22 canonical 22 same frame set: True
  path2 202 Re: previous 1 -> canonical 0
  path2 503 Re: previous 1 -> canonical 0
  path2 504 Re: previous 1 -> canonical 0
  cells compared 132 changed 3

## B. tables - CRO morph table.csv (spreadsheet export) frame rows vs canonical, all 14 terms
frames: table 22 canonical 22 same frame set: True
  path1 406 H_Bright: table 1 -> canonical 0
  path1 406 V: table 0 -> canonical 1
  path2 202 H_Bright: table 1 -> canonical 0
  path2 303 Ro: table 0 -> canonical 1
  path2 405 Ro: table 0 -> canonical 1
  path2 406 Ro: table 0 -> canonical 1
  path2 503 H_Bright: table 1 -> canonical 0
  path2 504 H_Bright: table 1 -> canonical 0
  path2 507 Ro: table 0 -> canonical 1
  path2 508 Ro: table 0 -> canonical 1
  cells compared 308 differ 10

## C. morph table group rows vs cro_group_level_notes.csv (group level; not used per frame)
  path1 101-110 H_Mitotic: table 0 -> group notes 1
  path1 201-210 H_Polygonal: table 0 -> group notes 1
  path1 301-310 H_Polygonal: table 0 -> group notes 1
  path2 101-110 H_Mitotic: table 0 -> group notes 1
  path2 201-210 H_Look_Healthy: table 0 -> group notes 1
  path2 201-210 H_Mitotic: table 0 -> group notes 1
  path2 301-310 H_Bright: table 1 -> group notes 0
  path2 301-310 H_Cytoplasmic_extensions: table 0 -> group notes 1
  path2 401-410 H_Bright: table 1 -> group notes 0
  path2 401-410 H_Cytoplasmic_extensions: table 0 -> group notes 1
  path2 401-410 Ro: table 0 -> group notes 1
  path2 501-510 H_Bright: table 1 -> group notes 0
  path2 501-510 H_Cytoplasmic_extensions: table 0 -> group notes 1
  path2 501-510 Ro: table 0 -> group notes 1
  group rows 10 cells compared 140 differ 14
```

The spreadsheet's footer counts (filled cells per path, "ok"/"bad" blocks) summarize its own group and frame rows; they are superseded by the two CSVs above and can be recomputed from them.

**Removed (2026-10-06, authorized):** `tables - CRO morph table.csv` (untracked spreadsheet export; every row is represented in `cro_cpe_detections.csv` or `cro_group_level_notes.csv`, differences as listed). Also removed: the superseded, untracked `cro_healthy_detections.csv` and `build_cro_healthy_detections.py` from the earlier group-plus-frame coding. **Kept:** `cro_cpe_detections.csv`, rewritten as the canonical file (same name, so the IR-parallel naming and all existing paths still work).

`cpe_detection_results_cro.json` changes accordingly: "refractile" removed from path2 202, 503 and 504.

## Not changed, flagged

- `cpe_detection_results_cro_gk.json` (narrative-text deposit, 100 frames) propagates group text to member frames, and its path2 303 entry carries the path2 402 text (including "refractile" and "dying"). It is not used by the figures or the comparison tables; left unedited pending a decision.

## Ambiguities for review

- "round cells" (path2 405/406/507/508) coded as Rounded.
- "bright vesicles" (path1 406) coded as Vacuolation.
- "bright reflective points" (path2 202, 503, 504) not coded as Refractile.
- "floating bright cells that might be dying/cell debris" (path2 503/504) not coded as healthy-type Bright; coded as Detached (floating) and Dying (hedged).
- Hedged terms count as named: Dying at path2 402/405/406/503/504/507/508; Vacuolation at 503/504.
- Shared single descriptions (307 and 308; 405, 406; 503 & 504; 507, 508) applied to each named frame.
- The report's path1 202 text reads "Magnification of the center of 101 image" (probably 201); coded as written (Mitotic).
- No single-frame description says "healthy", so Look healthy is 0 on all 22 frames; healthy-type terms are mostly stated in the group descriptions, which the single-frame rule does not use.

## Note on healthy-type direction (added 2026-10-06)

Earlier wrap-ups wrongly said the single-frame coding "no longer claims an A-healthier direction" because they fixated on the empty **Look healthy** column (0/22). The other healthy-type terms are not empty:

| Term | Culture A (9) | Culture B (13) |
|---|---|---|
| Look healthy | 0/9 | 0/13 |
| Mitotic | 5/9 | 3/13 |
| Bright | 3/9 (Albert table 4/9) | 0/13 (Albert table 3/13) |
| Adherent | 5/9 | 0/13 |
| Cytoplasmic extensions | 0/9 | 6/13 |
| Any healthy term | 8/9 | 9/13 |

Albert's original spreadsheet (single-frame rows only) and the canonical file agree on every healthy cell except four **Bright** marks (path1 406; path2 202, 503, 504) � the same ambiguity already listed above. Mitotic / Bright / Adherent favor Culture A in both files; Cytoplasmic extensions favor Culture B. The side-by-side and figure c0 captions should be revised to report that pattern instead of "too sparse to call a direction."

