# IR results (independent researchers — IR1, IR2)

Analogous to ../cro-results/, built from independent-researcher Pass 1 free-text and Pass 2 checklist deliverables (source documents kept in gitignored local project folders). IR1 and IR2 were both blind to culture conditions and used the same two-pass instrument.

## Files

| File | Analog of | Contents |
|------|-----------|----------|
| ir_cpe_detections.csv | cro_cpe_detections.csv | IR1, all 100 images; IR_Dy/Ro/V/D/G/Re plus Pass-2 extras IR_BE/Sy/CS/ND |
| ir_cpe_detections_cro_overlap.csv | (subset) | IR1, same six columns for the 22 CRO-labeled frames only |
| cpe_detection_results_ir.json | cpe_detection_results_cro.json | IR1 per-image cpe_detected + cpe_types (CRO six) and cpe_types_extended |
| cpe_detection_results_ir_cro_overlap.json | (subset) | IR1 overlap-only compact JSON |
| cpe_detection_results_ir_gk.json | cpe_detection_results_cro_gk.json | IR1 full text (Pass 1), checklist (Pass 2); confluency is null |
| ir2_cpe_detections.csv | cro_cpe_detections.csv | IR2, all 100 images; IR2_Dy/Ro/V/D/G/Re plus IR2_BE/Sy/CS/ND |
| ir2_cpe_detections_cro_overlap.csv | (subset) | IR2, six columns for the 22 CRO-labeled frames |
| cpe_detection_results_ir2.json | cpe_detection_results_cro.json | IR2 per-image compact JSON |
| cpe_detection_results_ir2_cro_overlap.json | (subset) | IR2 overlap-only compact JSON |
| cpe_detection_results_ir2_gk.json | cpe_detection_results_cro_gk.json | IR2 full text (Pass 1), checklist (Pass 2); confluency is null |
| IR1_IR2_pass1_descriptor_comparison.csv / IR1_IR2_pass1_side_by_side.md | — | Pass 1 lexical descriptor incidence, IR1 vs IR2 |
| IR1_IR2_pass2_checklist_comparison.csv | — | Pass 2 strict incidence + mean graded score per item, rater, arm |
| IR1_IR2_pass2_item_agreement.csv | — | Pass 2 per-item IR1–IR2 agreement (% and κ; all / per arm) |
| IR1_IR2_CRO_overlap_agreement.csv | — | 22 CRO frames: CRO vs IR1 vs IR2 on the six CRO-comparable columns |
| IR1_IR2_pass2_side_by_side.md | — | Pass 2 narrative comparison, caveats, bottom line |

## Coding (identical for IR1 and IR2)

- **Dy, V, G, BE, Sy, CS, ND:** Pass 2 checklist; hit = Yes / Partial / Mild / Mild-partial (strict).
- **Ro, D, Re:** Pass 1 lexical hits (these were not on the Pass 2 checklist).
- **cpe_detected:** true if any of the six CRO-comparable types is present.
- **CultureA = path1 (10% FBS), CultureB = path2 (2% FBS).**
- Pass 2 graded scores (comparison files): Yes 1.0; Mild 0.66; Partial 0.5; Minimal 0.25; No/minimal 0.15; No / Not apparent 0 (healthy items: Yes 1.0, Partial/Mild 0.5, else 0).
- κ is reported only when both raters vary on an item; otherwise "n/a (constant)".

ir = independent researcher (not CRO).

## Important caveat on cpe_detected

cpe_detected is **true for all 100 images for both IR1 and IR2**. For IR1 this comes from near-saturated **Ro** and **Re** (Pass 1 lexical) and **G** (Pass 2 Partial on all); for IR2 from **V** and **G** (Pass 2 present on all). That mirrors the raw coding, not a claim that every frame shows classic CPE. For arm contrast prefer non-saturated columns (IR1: D, BE, CS; IR2: BE, Sy, ND, Dy, Re) or cpe_types_extended. Do **not** use confluence as a health or stress marker.

Overlap files *_cro_overlap* restrict to the 22 frames CRO labeled, for side-by-side comparison.

## Confluence policy

Confluence / surface coverage is **not** an indicator of culture health or stress (confounded by growth stage). IR metrics and summaries must not use confluence—including day-matched A vs B coverage gaps—to judge healthy vs stressed. Morphology descriptors only. The confluency field in the *_gk.json files is intentionally null.
