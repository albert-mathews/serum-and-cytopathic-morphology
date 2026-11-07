# P4 wishlist — files to fetch / still needed

**Purpose:** track documents for P4 that were identified but not yet read in full, or that
could not be fetched in this session (bot-blocked / paywalled / JS-only product pages). Owner
fetches into `p4_serology_antigen/refs/` under the suggested filenames; on drop-off the assistant
extracts into `p4_antigen_provenance.csv` and re-scores.

**Columns:** ID · Title · Authors · Year · Venue · Locator · Why needed · Where cited · Priority.

---

## A. Manufacturer inserts / IFUs (fill the two missing census formats + upgrade veterinary rows)

| ID | Title / product | Authors (mfr) | Year | Locator | Why needed | Cited in | Priority |
|----|-----------------|---------------|------|---------|------------|----------|----------|
| P4W-01 | ~~Licensed **immunoblot** / line-immunoassay IFU~~ **RECEIVED** — MIKROGEN recomLine Borrelia insert + recomLine portfolio catalogue | n/a (manufacturer) | current | `refs/P4W-01 - PI_RLBB_E008.pdf`, `refs/P4W-01 - FO_Line_E009.pdf`, `refs/P4W-01 - mikrogen_line_assay_catalogue.pdf` | Only format that routinely runs an uninfected-lysate / reagent-control lane → best chance of a `matched_mock_run = yes` row. Avoid HIV + phage | coded as P4-009 (HSV lysate), P4-011 (Borrelia) | done |
| P4W-02 | ~~Licensed **lateral-flow / rapid antigen** IFU (non-HIV)~~ **RECEIVED** — 5 EUA/FDA rapid-antigen IFUs + lateral-flow doc | n/a (manufacturer) | current | `refs/P4W-02 - *` (GenBody, iHealth, Phase, Siemens, 510(k)) | Missing census format; P4-007 lesson = catalogue sources cannot fill the stack | coded as P4-010 (GenBody COVID Ag) | done |
| P4W-03 | VMRD Bluetongue cELISA v2 **manufacturer insert** (upgrade P4-007) | n/a | current | VMRD | P4-007 currently a distributor catalogue; needs real insert | `p4_antigen_provenance.csv` P4-007 | medium |
| P4W-04 | ID Screen Bluetongue / Infectious Bronchitis **manufacturer inserts** (upgrade P4-004/-005/-006) | n/a (Innovative Diagnostics) | current | ID.vet | veterinary rows rest on product pages / a 2011 catalogue | CSV P4-004/005/006 | medium |

---

## B. Prior-art full texts (found as abstracts / metadata; fetch for quote-level evidence)

| ID | Title | Authors | Year | Venue | Locator | Why needed | Cited in | Priority |
|----|-------|---------|------|-------|---------|------------|----------|----------|
| P4W-05 | Monoclonal IgM antibodies mediate potent complement neutralization by targeting cell-derived epitopes on enveloped viruses | Kainulainen MH, Harmon JR, Bergeron É, et al. | 2026 | mBio 17(3):e0170925 | DOI 10.1128/mbio.01709-25; PMID 41685933; PMC12977607 | Anchor prior art: "neutralizing" antibody binds host GM2 ganglioside (cell-derived epitope) carried on the envelope — serology neutralization reads host material, not only virus-encoded antigen | `P4_reading_notes.md` §prior-art | high |
| P4W-06 | SARS coronavirus 2-reactive antibodies in bovine colostrum | Ellis J, et al. | 2023 | Can Vet J 64(4):337-43 | PMID 37008643; PMC10031788 | Bovine serum/colostrum carries "SARS-CoV-2-reactive antibodies" — serum ingredient itself cross-reacts with a "viral" antigen | `P4_reading_notes.md` §prior-art | high |
| P4W-07 | Use of tick cell culture-derived Anaplasma marginale antigen in a competitive ELISA... | Saliki JT, Blouin EF, Rodgers SJ, Kocan KM | 1998 | Ann N Y Acad Sci 849:273-81 | DOI 10.1111/j.1749-6632.1998.tb11059.x; PMID 9668475 | Reference antigen = detergent-solubilized infected tick-cell lysate; candidate census row | `P4_reading_notes.md` §2 | medium |
| P4W-08 | Establishment of a new bovine leukosis virus producing cell line | Beier D, et al. | 2004 | J Virol Methods 121(2):239-46 | DOI 10.1016/j.jviromet.2004.06.017; PMID 15381362 | "contamination of the BLV antigen-producing cell culture systems by BVDV may give rise to misinterpretation of serological test results" | `P4_reading_notes.md` §2 | high |
| P4W-09 | Serological Evaluation of Immunity to the Varicella-Zoster Virus Based on a Novel Competitive ELISA | Liu J, et al. | 2016 | Sci Rep 6:20577 | DOI 10.1038/srep20577; PMID 26853741 | VZV competitive ELISA; monoclonals raised on "membrane proteins or cell-free virus" | `P4_reading_notes.md` | medium |
| P4W-10 | An Improved Immunochromatographic Strip Based on Plant-Derived E2 for Detection of Antibodies against Classical Swine Fever Virus | Xu Q, et al. | 2022 | Microbiol Spectr 10(4):e0105022 | DOI 10.1128/spectrum.01050-22; PMID 35862968 | Lateral-flow format; developers avoid culture because of "contamination of fetal bovine serum with BVDV in cell culture" | reading §3 | medium |
| P4W-11 | SCALABLE DOWNSTREAM PROCESS FOR PURIFICATION AND INACTIVATION OF MICROCARRIER-PROPAGATED JAPANESE ENCEPHALITIS VIRUS ANTIGEN | Chodavarapu, Mallepaddi, Podha | 2026 | Zenodo | DOI 10.5281/zenodo.23842428 | Antigen purification explicitly tracks host-cell protein/DNA impurity clearance — culture-derived "viral antigen" residual host material | reading §prior-art | medium |
| P4W-12 | Genetic detection and characterization of emerging HoBi-like viruses in archival foetal bovine serum batches | Giammarioli M, et al. | 2015 | Biologicals 43(4):220-4 | DOI 10.1016/j.biologicals.2015.05.009; PMID 26071653 | All 26 FBS batches pestivirus-positive by RT-PCR | reading §3 | medium |
| P4W-13 | Detection of a cell line contaminated with hog cholera virus | Bolin SR, et al. | 1994 | J Am Vet Med Assoc 205(5):742-5 | PMID 7989247 | ATCC-repository cell line carried undeclared pestivirus; upstream-source-pointer concern | reading §3 | medium |
| P4W-14 | Resolving heterophile antibody interference in viral serology using blocking tubes | Song J, Jeong I, Kim S, Park Y | 2025 | Microbiologyopen 14(6):e70098 | DOI 10.1002/mbo3.70098; PMID 41144880; PMC12558593 | Measured non-viral-epitope (patient-side): HBT dropped HSV IgM positivity 49.7%→2.7%, EBV VCA 20.5%→2.7% — bulk viral-IgM "positives" were heterophile (anti-reagent), not virus | `P4_reading_notes.md` §4d | high |
| P4W-15 | Human anti-animal antibody interferences in immunological assays | Kricka LJ | 1999 | Clin Chem 45(7):942-56 | PMID 10388468 | Canonical non-viral-epitope prior art (HAMA); cited >300× | `P4_reading_notes.md` §4d | high |
| P4W-16 | Potential false-positive reasons for SARS-CoV-2 antibody testing and its solution | Ye Q, Zhang T, Lu D | 2021 | J Med Virol 93(7):4242-46 | DOI 10.1002/jmv.26937; PMID 33710634 | Names endogenous interferents: RF, heterophile, HAMA, lysozyme, complement, cross-antigens | `P4_reading_notes.md` §4d | medium |
| P4W-17 | False positive results in SARS-CoV-2 serological tests for samples with chronic inflammatory disease | Kharlamova N, et al. | 2021 | Front Immunol 12:666114 | DOI 10.3389/fimmu.2021.666114; PMID 34012450; PMC8126683 | Peer-reviewed stand-in for medRxiv PPR237451 | `P4_bibliography.md` §B | medium |
| P4W-18 | An interesting case of isolated false-reactive hepatitis B surface antigen | Costa V, et al. | 2021 | Case Reports Hepatol 2021:9928098 | DOI 10.1155/2021/9928098; PMID 34336313 | Heterophile → isolated HBsAg false positive | `P4_reading_notes.md` §4d | low |

---

## Status note

- Items P4W-05 through P4W-13 were located as abstracts/open metadata in the 2026-11-06
  session via PubMed E-utilities, Europe PMC, and Zenodo. Full texts go to `refs/` when fetched.
- Search engines (Bing/DDG) were bot-blocked in that session; manufacturer eIFU pages (MIKROGEN,
  EUROIMMUN) returned JS-nav HTML rather than PDF text, so P4W-01/-02/-03/-04 need direct PDF
  URLs or owner fetch.
- Nothing here is paywalled-blocking in the abstract sense; the block is retrieval/parsing.

*End of P4 wishlist.*