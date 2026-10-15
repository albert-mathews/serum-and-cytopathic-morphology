# IR3v - Pass 1 open-ended morphology (lexical + clarified coding)

**Scope:** Pass-1 free-text descriptions by a third independent rater (IR3v) of the same blinded CultureA/CultureB phase-contrast images rated by IR1 and IR2 (100 rated; 99 unique frames analysed, see Data notes).
**Rater:** IR3v, briefing-condition pilot arm. The briefing condition is described in the paper only after the rater has finished Pass 2 and been debriefed.
**Status (2026-10-14):** Pass 1 complete (100/100 frames rated; 99 unique frames analysed). Coding clarifications answered by the rater 2026-10-14 and applied below. **Pass 2 (checklist) in progress.**
**Arms (analysis only):** CultureA = path1 (10% FBS), CultureB = path2 (2% FBS). n = 50 (A) / 49 (B) after excluding the duplicate frame `CultureB_day4_08`.
**Rule:** Confluence/coverage is not healthy vs stressed.

**Companion files:** `ir3v_pass1_text.csv` (verbatim Pass-1 text, 99 rows; duplicate frame excluded), `ir3v_cpe_detections.csv` (clarified CRO-comparable coding, `IR3v_` prefix), `IR3v_pass1_descriptor_comparison.csv` (per-arm incidence, shared lexicon vs clarified).

---

## Coding

1. **Shared lexicon** (identical regex sets used for IR1/IR2 Pass 1; `wrk/viz/r3viz/items.py`). Used unchanged for the Pass-1 figures so all raters are scored the same way.
2. **Clarified coding** (`ir3v_cpe_detections.csv`), applying the rater's answers to five clarification questions:
   - *Shrinking* (shrink / shrunk / shrinkage) = CPE class rounded/shrinking -> **Ro** (with the shared "rounded").
   - *"Vaculation"* = vacuolation -> **V**. The rater distinguished vacuolation from a **single large bright vacuole in about 1% of cells**; sentences describing that single vacuole are coded separately (**Vsingle**) and not as V.
   - *Refraction / refractive* = cells bright or highlighted under phase contrast = refractile -> **Re** (not counted when the word describes the single vacuole).
   - *Projections / migration*: the rater's rule is stressed when projections are thin and late in the time course, healthy-type when thick and early. No IR3v sentence states projection thickness, so **no frame meets either rule; all mentions are left uncoded** (`IR3v_Proj_mentioned` records the mention, `IR3v_Proj_coded` is blank).
   - Dy, D, G, BE, Sy, CS, ND: shared lexicon. For IR3v these are Pass-1 lexical columns (for IR1/IR2 the BE/Sy/CS/ND columns come from Pass 2).

## Incidence by arm (frames with the descriptor; A n=50, B n=49)

| Descriptor | Shared lexicon A | B | Clarified A | B | Clarified B-A |
|---|--:|--:|--:|--:|--:|
| Vacuolation (V) | 38 | 41 | 31 | 30 | -1 |
| Single large vacuole (Vsingle) | - | - | 14 | 24 | +10 |
| Rounded / shrinking (Ro) | 1 | 1 | 8 | 12 | +4 |
| Refractile (Re) | 0 | 0 | 17 | 21 | +4 |
| Detached (D) | 0 | 2 | 0 | 2 | +2 |
| Dying (Dy), Granularity (G) | 0 | 0 | 0 | 0 | 0 |
| Any of the CRO six (Dy, Ro, V, D, G, Re) | 38* | 42* | 36 | 40 | +4 |
| Projections / migration mentioned (uncoded) | - | - | 10 | 32 | +22 |
| Elongated (healthy-type, shared lexicon) | 35 | 33 | - | - | - |

\* shared lexicon "any CPE term" (all ten CPE regexes).

**By day** (clarified, any CRO-six term): A 2, 4, 10, 10, 10; B 7, 8, 9, 8 (of 9), 8 (days 1-5). Culture B leads on days 1-2; both cultures reach 8-10 of 10 frames from day 3.

**On the 22 CRO-described frames:** IR3v names a CRO-six term on 5/9 Culture A and 8/13 Culture B frames (CRO: 1/9 and 10/13).

## Comparison with IR1, IR2 and CRO (Pass 1, any CPE-type term)

| Source | A | B |
|---|--:|--:|
| IR3v, clarified CRO-six | 36/50 | 40/49 |
| IR1, shared lexicon | 50/50 (saturated by rounded/refractile) | 49/49 |
| IR2, shared lexicon | 19/50 | 25/49 |
| CRO, own single-frame descriptions | 1/9 | 10/13 |

Direction is B >= A for every source. IR3v's B-A gap is +10 percentage points, similar to IR2 Pass 1 (+13 pp) and much smaller than the CRO (11% vs 77%). IR3v's most B-skewed descriptions fall outside the CRO six: single large vacuoles (14 vs 24) and projections (10 vs 32, uncoded).

## Data notes

- The text follows a fixed per-image template (scale bar, confluence, clustering, aggresome-like structures, vacuolation, halo/refraction, single-cell shape), so term presence partly reflects the template. Percentages inside sentences are not scored.
- **CultureB_day4_08:** the rater reported a 400 µm scale bar where even-numbered frames otherwise show 200 µm, and confirmed it on re-download. Checked 2026-10-14: the image shows a 400 µm bar, and `CultureB_day4_08.tif` is byte-identical to `CultureB_day4_07.tif` (same MD5). The duplicate is already present in the CRO originals (path2 frames 407 and 408 are the same file). All raters therefore described one field twice in Culture B day 4. Decision (2026-10-14): the duplicate is excluded for every rater (IR1, IR2, IR3v, CRO) through `../frames_excluded_from_analysis.csv`; all counts above use the 99 unique frames (50 A / 49 B). Raw rater files are unchanged.
- No image-analysis software disclosed.