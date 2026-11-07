# P4 product shortlist — popularity-ranked serology/antigen products (selection plan)

**Purpose:** select the 3–5 sold serology/antigen products whose design/validation-sample provenance
will be traced, so the census is *dispositive* rather than *convenience*. This note holds the
selection logic and the shortlist; provenance extraction goes into `../p4_antigen_provenance.csv`.

## The dispositive logic (Albert, 2026-11-06)

1. The prediction reduces to: **does any sold serology test *not* inherit the cell-culture / FBS / CPE
   under-determination in its design-and-validation material?**
2. If *no* test escapes (provenance census), *and* at least some tests are demonstrably
   non-viral-epitope (B-location: reference is culture material; or D-location: patient interference),
   then the case closes.
3. Therefore provenance is the most pertinent question, and only a **popularity-ranked** handful is
   needed — not all tests.

## Selection rules

- Identify **actual sold products** (manufacturer kits / licensed diagnostics), not papers.
- Rank by **citable** popularity anchors (guideline recommendations — WHO/CDC/CLSI/ASM/OIE — or
  seroprevalence studies naming the assay), not by assertion. If market-share data cannot be sourced,
  use guideline-citation frequency.
- Select the **top 3–5** spanning **all assay types**, so no format is cherry-picked, e.g.:
  1. an **ELISA** (high-volume human antibody serology);
  2. an **IFA / immunofluorescence**;
  3. a **licensed immunoblot / line assay**;
  4. a **lateral-flow / rapid antigen**;
  5. a **neutralization / functional** (if a productized form exists; otherwise the primary-paper form).
- For each selected product, extract provenance per `P4_coding_sheet.md`: `immunogen_source`,
  `reference_antigen_source`, `upstream_source_pointer`, `isolate_justification` — and answer
  **does its truth-trace route through culture CPE, or not?**

## Current census (from the pilot, n=8 — convenience, not yet popularity-ranked)

- P4-001 ZEUS CMV IFA (human, IFA — culture isolate substrate, strain AD169)
- P4-002 EUROIMMUN measles ELISA (human, ELISA — Vero/Edmonston lysate)
- P4-003 SERION measles ELISA (human, ELISA — provenance undisclosed)
- P4-004/005/006 ID Screen bluetongue / IBV (veterinary, ELISA — recombinant, provenance unclear)
- P4-007 VMRD bluetongue cELISA (veterinary, ELISA — catalogue only)
- P4-008 IBT anti-SUDV mAb (research reagent — mixed provenance)

## To fill

| Assay type | Candidate products (to verify/rank) | Provenance question |
|-----------|-------------------------------------|---------------------|
| ELISA (human, high-volume) | measles/rubella/mumps IgG; HCV; EBV; CMV; VZV | immunogen & coating antigen source → culture Isolate? |
| IFA | CMV, EBV, HSV, autoimmune-adjacent viral IFA | slide substrate = infected cell line (which, and how justified) |
| Immunoblot / line | EBV, Borrelia (Lyme), HSV | does an uninfected-lysate / reagent-control lane exist? (the `matched_mock` question) |
| Lateral-flow / rapid antigen | influenza, RSV, SARS-CoV-2, rotavirus | capture antibody raised against what; antigen standard from what |
| Neutralization | (productized or paper) | titer defined by CPE reduction in the same dual-serum system (R1 link) |

## Popularity anchors found (2026-11-06) — citable, not asserted

These name the category-leading commercial products per assay type, so the shortlist is popularity-
grounded. Full citations live in `../P4_bibliography.md` (add as located).

| Assay type | Anchor (who establishes popularity) | Named/implied products | Anchor locator |
|-----------|--------------------------------------|------------------------|----------------|
| ELISA (measles/rubella, human) | Systematic review of measles IgG EIA vs PRNT head-to-head (names the dominant commercial EIAs) | Enzygnost (Siemens/Dade-Behring), EUROIMMUN, Captia (Trinity), SERION | Lutz et al. 2023, BMC Infect Dis 23:367, PMID 37259032 |
| ELISA (serosurveillance standard) | WHO-aligned serosurveillance review | (commercial measles/rubella IgG EIAs) | Brady et al. 2024, Vaccines 12(7):816, PMID 39066453 |
| Immunoblot / LIA (chemiluminescence) | Evaluation of Chagas TESA `VirClia` assay | Vircell VirClia | Silgado et al. 2026, J Clin Microbiol 64(7):e0173925, PMID 42284051 |
| Immunoblot (Lyme) | New single-tier Lyme serology (replaces 2-tier WB) | (C6-based single-tier; leading Lyme immunoassay) | Levin et al. 2025, J Clin Microbiol 63(9):e0048325, PMID 40833084 |
| Lateral-flow / rapid antigen | Multicenter evaluation of a rapid IgG/IgM test | COVID19SEROSpeed (and class-leading rapid Ag/IgG-IgM) | Plebani et al. 2021, J Clin Microbiol 59(2):e02240-20, PMID 33218990 |

## Next concrete step

For each shortlisted product above (+ any IFA/neutralization product to fill type coverage), obtain the
**manufacturer insert / IFU** and extract the `immunogen_source` / `reference_antigen_source` /
`upstream_source_pointer` / `isolate_justification` columns → `../p4_antigen_provenance.csv`. Insert
PDFs go under `refresh/refs/` (gitignored); many already listed in `../P4_pdf_wishlist.md` (P4W-01…).

## Insert-level extraction results (2026-11-06, from fetched `refs/`)

Two of the three wishlist fetches (P4W-01 immunoblot/line, P4W-02 lateral-flow) were dropped into
`../refs/` and read (via `pdftotext`). Findings coded into `../p4_antigen_provenance.csv` as new
rows:

- **P4-009 — MIKROGEN recomLine HSV-1/HSV-2 IgG (line immunoassay).** The manufacturer's own
  portfolio catalogue labels the HSV strips as using **"HSV lysates"** (a culture-lysate antigen band)
  alongside recombinant gG-1/gG-2. Lysate substrate line and validation are not disclosed; no matched
  uninfected-lysate lane; the anti-HSV reagent's immunogen is undisclosed. `inheritance_score =
  inherits` (reference antigen is a culture lysate; provenance one hop upstream unresolved).
- **P4-010 — GenBody COVID-19 Ag rapid test (lateral flow).** Capture/detection = mouse **anti-NP
  monoclonals**; positive control = "recombinant SARS-CoV-2 protein antigen" with no expression host
  and no ORF origin stated; the mAb immunogen is undisclosed. `inheritance_score = partial`.
- **P4-011 — MIKROGEN recomLine Borrelia IgG/IgM.** Recombinant antigens, each keyed to a Borrelia
  *strain designation*, but the ORF/sequence origin (culture isolate vs clinical vs reference genome)
  and expression host are not stated — `upstream_source_pointer = strain_designation_only`. Strip
  controls are conjugate/cutoff procedural controls, not a matched non-viral antigen. `partial`.

**Cross-cutting finding:** within one manufacturer's line-assay portfolio, antigen provenance spans
the whole spectrum — culture **lysate** (HSV), **recombinant-with-undisclosed-ORF** (Borrelia, and
most others), and a genuine **Western blot** (recomBlot Rubella, E1/E2). The catalogue's own
flow chart ("from pathogen to antigen: cloning → fermentation → chromatography") confirms the
antigens are cloned from "the pathogen's gene," yet no product in the line discloses whether that
gene's source isolate was culture+CPE derived. This is the P3-inheritance link made visible at the
kit level.

## Remaining for type coverage

- IFA and neutralization still need a popularity-grounded product/paper pick (the existing ZEUS CMV
  IFA row is a convenience start). Open.

*Status: two formats (immunoblot/line + lateral-flow) now have insert-level provenance coded.
Remaining: IFA + neutralization anchors; then the pattern statement (do any sold tests escape the
under-determination?).*