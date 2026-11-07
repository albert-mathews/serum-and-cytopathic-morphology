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

*Status: selection logic + popularity anchors recorded. Insert-level provenance extraction next.*