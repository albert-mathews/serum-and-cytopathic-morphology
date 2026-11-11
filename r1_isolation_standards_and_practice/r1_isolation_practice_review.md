# R1 isolation-practice review — reproduction spec (for a second, independent reader)

**Purpose:** a second bot, given this file and the PDFs only, should able to page-by-page read
every PDF in `refs/isolation_practice/` and reproduce `isolation-refs.csv` from scratch, so the
two independent extractions can be diffed for discrepancies.

**Do NOT** copy the existing `isolation-refs.csv`. Read each PDF yourself and code from the text.
You may look at the CSV only to learn the *schema/column order* and the *ID↔PDF assignment* (below).

---

## 1. Input

PDFs live in:
`r1_isolation_standards_and_practice\refs\isolation_practice\`

Each PDF is named `VI### - <title>.pdf`, so **the `ID` is the leading `VI###` token** of the
filename. One PDF = one paper; if a paper reports multiple distinct cell/serum recipes, it becomes
multiple rows (recipe letters A, B, C…).

**Note:** the corpus intentionally includes some **non-Isolation-endpoint** references — the
`VI295`–`VI303` block are single-virus/particle-tracking (live-cell imaging) papers (class 4).
They are part of the curated "isolation practice" set (Arg 2: the 2I1D serum pattern persists
across the field regardless of endpoint). Code them by the same rules; their class will come out
4 because their endpoint is imaging, not CPE-as-detection.

Image-only (no text layer) PDFs must be OCR'd before reading (see `tools/ocr_pdf.py`); tag any
quote taken from OCR as OCR-derived, not clean text.

## 2. Output

Write one CSV, `isolation-refs.csv`, with EXACTLY these columns (in this order):

```
ID, recipe, year, virus, cells, base_medium, FBS_pre_inoculation, FBS_post_inoculation,
TPB_pre_inoculation, TPB_post_inoculation,
lactalbumin_pre_inoculation, lactalbumin_post_inoculation,
yeast_extract_pre_inoculation, yeast_extract_post_inoculation,
peptone_pre_inoculation, peptone_post_inoculation,
penicillin_IU_ml, streptomycin_mg_ml, amphotericin_mg_ml, link, DOI, access, fbs_coded,
source_batch, notes, quote_pre, quote_post,
endpoint_CPE_detection_isolate, endpoint_titration_TCID50, endpoint_antigen_detection,
endpoint_neutralization, endpoint_plaque, endpoint_hemagglutination_hemadsorption,
endpoint_molecular, primary_endpoint, class, endpoint_purification, endpoint_characterization
```

## 3. The atomic unit: one row = one (paper, recipe) "instance"

- One paper reporting **M distinct recipes** (different cell line and/or different FBS pre/post)
  → **M rows**, same `ID`, `recipe` = A, B, C, … per recipe.
- One paper with **many replicate cultures of the same recipe** → **1 row** (`recipe` = A).
- Two different papers with the identical recipe → **2 rows** (never merged).
- Recipe-*independent* columns (year, virus, link, DOI, access, source_batch) are identical across
  a paper's rows; recipe-*dependent* columns (cells, base_medium, FBS pre/post, antibiotics,
  quotes, endpoints, class) differ per row.

## 4. FBS fields (the core extraction)

Read the **Methods** (and Results if needed). For the *isolation/culture* step:

- **`FBS_pre_inoculation`** = serum % in the **growth medium** the cells were amplified in before
  inoculation. Record as the PDF states it: `10`, `5`, `8`, `15`, `0`, or a range `5-10`, or an
  either/or `5 or 10`. Leave **blank** if the paper states no numeric %.
- **`FBS_post_inoculation`** = serum % in the **maintenance / virus / overlay medium** at or after
  inoculation. Blank if not stated.
- **Serum type:** `FBS`/`FCS`/`fetal calf`/`newborn calf`/`calf`/`bovine` all count as "serum".
  If it is NOT fetal (e.g. calf/newborn/adult bovine), note the type in `notes` but still put the
  number in the FBS column. `BSA` (bovine serum albumin) is **NOT** serum — do not record a BSA %
  as an FBS value.
- `base_medium` = the cell-culture base (DMEM, MEM, RPMI-1640, L-15, M199, …).
- `penicillin_IU_ml`, `streptomycin_mg_ml`, `amphotericin_mg_ml` = antibiotic amounts if stated
  (else blank/`-`).

### Enrichment columns (the non-serum half of the "medium rich → poor" switch)

The growth→maintenance switch often changes **more than serum** at once. Record each non-serum
enrichment in its own pre/post column — **NOT** in the FBS columns.

| columns | substance | note |
|---|---|---|
| `TPB_` | tryptose phosphate broth | common growth additive |
| `lactalbumin_` | lactalbumin hydrolysate (LAH) | |
| `yeast_extract_` | yeast extract | |
| `peptone_` | peptone / proteose peptone | |

- Put the **%** in the matching pre/post cell (e.g. `TPB_pre=10`, `TPB_post=0`). Blank if not
  stated. These are enrichment, so record them even though they are not serum.
- **Do NOT** put any of these in `FBS_*`.

### Systematic exclusions (never in any enrichment column, never serum)

1. **Single purified stabilizers:** albumin (BSA/Fraction V), gelatin, detergents (Tween/PEG/
   Pluronic). Trypsin is an enzyme (µg/ml), not a % supplement. → `base_medium`/`notes` only.
2. **Assay reagent sera:** goat/horse/donkey serum named with "block"/"wash"/"antibody" (immuno-
   staining), not the culture serum.
3. **Serum albumin ≠ serum:** a "0.2% BSA + trypsin" medium is **serum-free** — code `FBS_post = 0`,
   not 0.2.

### `fbs_coded` (data-availability flag, 3 values)

| value | condition |
|---|---|
| `yes` | both pre AND post stated as a numeric value |
| `post_only` | post is numeric but pre is **not stated** → record post value; put the pre cell as the number `10` and add `[post_only: pre assumed 10% ATCC]` to notes |
| `no` | neither numeric, or pre-only |

**Rule:** a paper that states post but not pre gets `fbs_coded = post_only`, `FBS_pre_inoculation = 10` (assumed ATCC default), and a `[post_only: pre assumed 10% ATCC]` note tag. Do NOT lift a serum % from a *different cell line* in the same paper (a companion line's 10% is not the test line's pre).

### `quote_pre` / `quote_post`

Verbatim (quote-sized) sentences from the PDF backing the pre and post values. If not stated, put
`(none)` or `(assumed ATCC 10% — growth FBS not stated in paper)` for post_only pre.

## 5. Endpoint + class (the two-axis classification)

### `class` — endpoint-based (category-1 rows only; values `1` or `4`)

- **`class = 1`** — the PRIMARY endpoint is **CPE read as virus detection and/or Isolate**
  ("CPE = we found / Isolated the virus"), typically from a clinical/field/environmental specimen.
- **`class = 4`** — the culture uses the growth→maintenance serum change, but its PRIMARY endpoint
  is **something else**: titration/TCID50, antigen detection (ELISA/NS1/IFA), neutralization,
  plaque/focus assay, hemagglutination/hemadsorption, molecular (sequencing/PCR/phylogeny),
  purification (viral protein/particle), or characterization (morphology, tropism, immunogenicity,
  antiviral screening, vaccine-donor passage, live-cell imaging / single-particle tracking).

**The critical judgment:** is CPE being used as "we found / Isolated the virus"?
- Yes → class 1. No (culture is for quantitation/antigen/neutralization/imaging/protein prep/
  screening) → class 4.

### `endpoint_*` columns — yes/no

There are 9 fixed endpoint columns:
`endpoint_CPE_detection_isolate`, `endpoint_titration_TCID50`, `endpoint_antigen_detection`,
`endpoint_neutralization`, `endpoint_plaque`, `endpoint_hemagglutination_hemadsorption`,
`endpoint_molecular`, `endpoint_purification`, `endpoint_characterization`.

- For a **class 1** paper, mark `endpoint_CPE_detection_isolate = yes`, and ALSO mark yes any
  *other* endpoint the paper actually uses (e.g. most Isolation papers also do `molecular`
  confirmation → `endpoint_molecular = yes`). **A multi-endpoint paper records ALL its endpoints,**
  not only the primary one.
- For a **class 4** paper, `endpoint_CPE_detection_isolate = no`, and mark yes the endpoint(s) that
  ARE its primary(s).

### `primary_endpoint` — free text

The dominant endpoint that fixes the class, e.g. `CPE (virus detection / Isolate)`, or
`titration TCID50`, `antigen detection (NS1)`, `neutralization`, `live-cell imaging / single-particle tracking`, `characterization (…specifics…)`.

## 6. Other columns

- `year` — publication year (from the PDF/DOI).
- `virus` — the virus(es) being cultured/studied (short).
- `cells` — cell line(s) (short).
- `link` / `DOI` — PMID/DOI/stable URL if visible in the PDF; leave blank and don't guess.
- `access` — `fulltext_verified` if you read the full PDF.
- `source_batch` — `reproduction <your-run-tag>`.
- `notes` — any ambiguity, serum-type caveats, or OCR caveats. Tag genuine judgment calls with
  `[OWNER_REVIEW]` rather than silently deciding.

## 7. Self-check before you finish

- Every PDF in the folder produced ≥1 row; every row maps to a real PDF.
- Every numeric FBS value has a supporting `quote_*` sentence (post_only pre is the exception).
- `fbs_coded` is one of `yes`/`post_only`/`no` and matches the pre/post cells.
- `class` is `1` or `4`; a class-1 row has `endpoint_CPE_detection_isolate=yes`; a class-4 row has it `no`.
- Multi-endpoint papers have ALL their `endpoint_*` columns filled, not just the primary.

Output the CSV and a short memo listing any PDFs that were image-only (OCR'd), inaccessible, or
for which you needed to flag `[OWNER_REVIEW]`.