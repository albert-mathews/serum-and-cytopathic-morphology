# Paywall extraction status — 2026-09-18

## Summary counts
- Present PDFs screened: **18**
- Newly dual-FBS coded: **9** → VI99, VI105, VI109, VI110, VI111, VI112, VI115, VI118, VI121
- Single-stage only (post or pre only; dual blank): **5** → VI98, VI100, VI106, VI113, VI116
- Ambiguous / multi-system (dual blank): **4** → VI101, VI102, VI107, VI117
- No FBS found: **0**
- Still missing PDFs: **7** → VI97, VI103, VI104, VI108, VI114, VI119, VI120
- Dual-subset CSV rebuilt: **112** data rows (filter = both FBS fields non-empty; was 103 before this batch → +9)

## Per-ID outcome table

| ID | Outcome | Pre→Post | Notes brief |
|----|---------|----------|-------------|
| VI98 | single | — | ATCC growth medium FBS% not stated; maintenance MEM + 2% FBS |
| VI99 | dual | 8→2 | Vero DMEM 8% FBS growth → 2% FBS maintenance |
| VI100 | single | — | Only maintenance MEM + 2% FCS; growth FBS not stated |
| VI101 | ambiguous | — | Aspirated maint 2% FCS; post-inoc 3% FCS; growth FBS not stated |
| VI102 | ambiguous | — | Homogenate diluent 10% FBS; L-15+2% for inoculum; C6/36 growth FBS not stated |
| VI105 | dual | 10→2 | HeLa growth 10% bovine (5% fetal+5% calf) → McCoy + 2% FBS (HELF maint 5% noted) |
| VI106 | single | — | Only maintenance MEM + 2% FCS; growth FBS not stated |
| VI107 | ambiguous | — | Tube maint 2% FBS; growth via std procedures w/o %; overlays 1.8–5% |
| VI109 | dual | 10→2 | G-MEM + 10% FBS growth → 2% FBS maintenance (primary cells also 15% growth) |
| VI110 | dual | 10→2 | Medium 199/Eagle MEM + 10% FBS → maintenance 2% FBS |
| VI111 | dual | 10→2 | HeLa/MRC5 grown 10% FCS → maintained 2% FCS |
| VI112 | dual | 10→2 | Eagle MEM + 10% heat-inact. FBS → after adsorption 2% FBS (serum-free also tested) |
| VI113 | single | — | Maintenance 2% FCS in Eagle basal; growth FBS not stated |
| VI115 | dual | 5→2 | HEF MEM + 5% FCS → maintenance 2% FCS |
| VI116 | single | — | Only 2% FBS maintenance/diluent; growth FBS not stated |
| VI117 | ambiguous | — | Multiple cell-specific growth (5/10%) and storage/maint (1/2%); no single dual |
| VI118 | dual | 10→2 | DMEM + 10% FBS → maintenance 2% FBS before inoculation |
| VI121 | dual | 10→2 | Eagle MEM/Hanks + 10% FCS → L-15M + 2% FCS |
| VI97 | missing PDF | — | PDF still missing; not invented |
| VI103 | missing PDF | — | PDF still missing; not invented |
| VI104 | missing PDF | — | PDF still missing; not invented |
| VI108 | missing PDF | — | PDF still missing; not invented |
| VI114 | missing PDF | — | PDF still missing; not invented |
| VI119 | missing PDF | — | PDF still missing; not invented |
| VI120 | missing PDF | — | PDF still missing; not invented |

## New dual-FBS pairs
- **VI99**: 8 → 2 (Vero; DMEM)
- **VI105**: 10 → 2 (HeLa arm; MEM growth / McCoy maint)
- **VI109**: 10 → 2 (G-MEM; skunk/raccoon primary + cell lines)
- **VI110**: 10 → 2 (medium 199 or Eagle MEM)
- **VI111**: 10 → 2 (Ohio HeLa / MRC5)
- **VI112**: 10 → 2 (AGMK/BS-C-1 etc.; Eagle MEM)
- **VI115**: 5 → 2 (HEF; Eagle MEM)
- **VI118**: 10 → 2 (DMEM; HSV isolation)
- **VI121**: 10 → 2 (WI-38 microcultures; Eagle MEM → L-15M)

## Artifacts
- Expanded CSV: `expansion/isolation-refs-overview_expanded.csv`
- Dual CSV: `expansion/isolation-refs-dual-fbs_only.csv`
- Quotes: `expansion/quotes_paywall_extracted_2026-09-18.md`
- Temp extracts: `expansion/_pdf_extract_tmp/` (VI*.txt from pdftotext -layout)