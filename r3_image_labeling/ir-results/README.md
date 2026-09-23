# IR results (independent researcher — IR1)

Analogous to ../cro-results/, built from independent-researcher (IR1) Pass 1 free-text and Pass 2 checklist deliverables (source documents kept in gitignored local project folders).

## Files

| File | Analog of | Contents |
|------|-----------|----------|
| ir_cpe_detections.csv | cro_cpe_detections.csv | All 100 images; IR_Dy/Ro/V/D/G/Re plus Pass-2 extras IR_BE/Sy/CS/ND |
| ir_cpe_detections_cro_overlap.csv | (subset) | Same six columns for the 22 CRO-labeled frames only |
| cpe_detection_results_ir.json | cpe_detection_results_cro.json | Per-image cpe_detected + cpe_types (CRO six) and cpe_types_extended |
| cpe_detection_results_ir_cro_overlap.json | (subset) | Overlap-only compact JSON |
| cpe_detection_results_ir_gk.json | cpe_detection_results_cro_gk.json | Full text (Pass 1), checklist (Pass 2); confluency is null |

## Coding

- **IR_Dy, IR_V, IR_G, IR_BE, IR_Sy, IR_CS, IR_ND:** Pass 2 checklist; hit = Yes / Partial / Mild / Mild-partial (strict).
- **IR_Ro, IR_D, IR_Re:** Pass 1 lexical hits (these were not on the Pass 2 checklist).
- **cpe_detected:** true if any of the six CRO-comparable types is present.
- **CultureA = path1 (10% FBS), CultureB = path2 (2% FBS).**

ir = independent researcher (not CRO).

## Important caveat on cpe_detected

Under the six CRO-comparable columns, **IR_Ro** and **IR_Re** (Pass 1 lexical) and **IR_G** (Pass 2 Partial-on-all) are near-saturated, so cpe_detected is **true for essentially all 100 images**. That mirrors the raw coding, not a claim that every frame shows classic CPE. For arm contrast on morphology features, prefer **IR_D, IR_BE, IR_CS**, or use cpe_types_extended. Do **not** use confluence as a health or stress marker.

Overlap file *_cro_overlap* restricts to the 22 frames CRO labeled, for side-by-side comparison.

## Confluence policy

Confluence / surface coverage is **not** an indicator of culture health or stress (confounded by growth stage). IR metrics and summaries must not use confluence—including day-matched A vs B coverage gaps—to judge healthy vs stressed. Morphology descriptors only. The confluency field in cpe_detection_results_ir_gk.json is intentionally null.
