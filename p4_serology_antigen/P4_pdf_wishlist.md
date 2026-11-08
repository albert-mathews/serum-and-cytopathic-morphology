# P4 wishlist — files to fetch / still needed

**Purpose:** track documents for P4 that were identified but not yet read in full, or that
could not be fetched in this session (bot-blocked / paywalled / JS-only product pages). Owner
fetches into `p4_serology_antigen/refs/` under the suggested filenames; on drop-off the assistant
extracts into `p4_antigen_provenance.csv` and re-scores.

**Columns:** ID · Title · Authors · Year · Venue · Locator · Save-as filename (`refs/`) · Why needed · Where cited · Priority.

*(Section A keeps its save-as filename inside the **Locator** cell, matching the existing received
files. Section B carries an explicit **Save-as filename** column.)*

---

## A. Manufacturer inserts / IFUs (fill the two missing census formats + upgrade veterinary rows)

| ID | Title / product | Authors (mfr) | Year | Locator | Why needed | Cited in | Priority |
|----|-----------------|---------------|------|---------|------------|----------|----------|
| P4W-01 | ~~Licensed **immunoblot** / line-immunoassay IFU~~ **RECEIVED** — MIKROGEN recomLine Borrelia insert + recomLine portfolio catalogue | n/a (manufacturer) | current | `refs/P4W-01 - PI_RLBB_E008.pdf`, `refs/P4W-01 - FO_Line_E009.pdf`, `refs/P4W-01 - mikrogen_line_assay_catalogue.pdf` | Only format that routinely runs an uninfected-lysate / reagent-control lane → best chance of a `matched_mock_run = yes` row. Avoid HIV + phage | coded as P4-009 (HSV lysate), P4-011 (Borrelia) | done |
| P4W-02 | ~~Licensed **lateral-flow / rapid antigen** IFU (non-HIV)~~ **RECEIVED** — 5 EUA/FDA rapid-antigen IFUs + lateral-flow doc | n/a (manufacturer) | current | `refs/P4W-02 - *` (GenBody, iHealth, Phase, Siemens, 510(k)) | Missing census format; P4-007 lesson = catalogue sources cannot fill the stack | coded as P4-010 (GenBody COVID Ag) | done |
| P4W-03 | VMRD Bluetongue cELISA v2 **manufacturer insert** (upgrade P4-007) | n/a | current | `refs/P4W-03 - VMRD_Bluetongue_cELISA_v2_IFU.pdf` | P4-007 currently a distributor catalogue; needs real insert | `p4_antigen_provenance.csv` P4-007 | medium |
| P4W-04 | ID Screen Bluetongue / Infectious Bronchitis **manufacturer inserts** (upgrade P4-004/-005/-006) | n/a (Innovative Diagnostics) | current | `refs/P4W-04 - ID_Screen_Bluetongue_IB_IFUs.pdf` | veterinary rows rest on product pages / a 2011 catalogue | CSV P4-004/005/006 | medium |

---

## B. Prior-art full texts — RECEIVED (full texts in `refs/`; read & re-tagged 2026-11-08)

| ID | Title | Authors | Year | Venue | Locator | Save-as filename (`refs/`) | Why needed | Cited in | Priority |
|----|-------|---------|------|-------|---------|----------------------------|------------|----------|----------|
| P4W-05 | Monoclonal IgM antibodies mediate potent complement neutralization by targeting cell-derived epitopes on enveloped viruses | Kainulainen MH, Harmon JR, Bergeron É, et al. | 2026 | mBio 17(3):e0170925 | DOI 10.1128/mbio.01709-25; PMID 41685933; PMC12977607 | P4W-05 - Kainulainen_2026_mBio_GM2_ganglioside.pdf | Anchor prior art: "neutralizing" antibody binds host GM2 ganglioside (cell-derived epitope) carried on the envelope — serology neutralization reads host material, not only virus-encoded antigen | `P4_reading_notes.md` §prior-art | high |
| P4W-06 | SARS coronavirus 2-reactive antibodies in bovine colostrum | Ellis J, et al. | 2023 | Can Vet J 64(4):337-43 | PMID 37008643; PMC10031788 | P4W-06 - Ellis_2023_colostrum_SARS_antibodies.pdf | Bovine serum/colostrum carries "SARS-CoV-2-reactive antibodies" — serum ingredient itself cross-reacts with a "viral" antigen | `P4_reading_notes.md` §prior-art | high |
| P4W-07 | Use of tick cell culture-derived Anaplasma marginale antigen in a competitive ELISA... | Saliki JT, Blouin EF, Rodgers SJ, Kocan KM | 1998 | Ann N Y Acad Sci 849:273-81 | DOI 10.1111/j.1749-6632.1998.tb11059.x; PMID 9668475 | P4W-07 - Saliki_1998_Anaplasma_CELISA.pdf | Reference antigen = detergent-solubilized infected tick-cell lysate; candidate census row | `P4_reading_notes.md` §2 | medium |
| P4W-08 | Establishment of a new bovine leukosis virus producing cell line | Beier D, et al. | 2004 | J Virol Methods 121(2):239-46 | DOI 10.1016/j.jviromet.2004.06.017; PMID 15381362 | P4W-08 - Beier_2004_BLV_BVDV_contamination.pdf | "contamination of the BLV antigen-producing cell culture systems by BVDV may give rise to misinterpretation of serological test results" | `P4_reading_notes.md` §2 | high |
| P4W-09 | Serological Evaluation of Immunity to the Varicella-Zoster Virus Based on a Novel Competitive ELISA | Liu J, et al. | 2016 | Sci Rep 6:20577 | DOI 10.1038/srep20577; PMID 26853741 | P4W-09 - Liu_2016_VZV_competitive_ELISA.pdf | VZV competitive ELISA; monoclonals raised on "membrane proteins or cell-free virus" | `P4_reading_notes.md` | medium |
| P4W-10 | An Improved Immunochromatographic Strip Based on Plant-Derived E2 for Detection of Antibodies against Classical Swine Fever Virus | Xu Q, et al. | 2022 | Microbiol Spectr 10(4):e0105022 | DOI 10.1128/spectrum.01050-22; PMID 35862968 | P4W-10 - Xu_2022_plant_E2_CSFV_strip.pdf | Lateral-flow format; developers avoid culture because of "contamination of fetal bovine serum with BVDV in cell culture" | reading §3 | medium |
| P4W-11 | SCALABLE DOWNSTREAM PROCESS FOR PURIFICATION AND INACTIVATION OF MICROCARRIER-PROPAGATED JAPANESE ENCEPHALITIS VIRUS ANTIGEN | Chodavarapu, Mallepaddi, Podha | 2026 | Zenodo | DOI 10.5281/zenodo.23842428 | P4W-11 - Chodavarapu_2026_JEV_purification.pdf | Antigen purification explicitly tracks host-cell protein/DNA impurity clearance — culture-derived "viral antigen" residual host material | reading §prior-art | medium |
| P4W-12 | Genetic detection and characterization of emerging HoBi-like viruses in archival foetal bovine serum batches | Giammarioli M, et al. | 2015 | Biologicals 43(4):220-4 | DOI 10.1016/j.biologicals.2015.05.009; PMID 26071653 | P4W-12 - Giammarioli_2015_FBS_HoBi_pestivirus.pdf | All 26 FBS batches pestivirus-positive by RT-PCR | reading §3 | medium |
| P4W-13 | Detection of a cell line contaminated with hog cholera virus | Bolin SR, et al. | 1994 | J Am Vet Med Assoc 205(5):742-5 | PMID 7989247 | P4W-13 - Bolin_1994_contaminated_cell_line.pdf | ATCC-repository cell line carried undeclared pestivirus; upstream-source-pointer concern | reading §3 | medium |
| P4W-14 | Resolving heterophile antibody interference in viral serology using blocking tubes | Song J, Jeong I, Kim S, Park Y | 2025 | Microbiologyopen 14(6):e70098 | DOI 10.1002/mbo3.70098; PMID 41144880; PMC12558593 | P4W-14 - Song_2025_heterophile_blocking.pdf | Measured non-viral-epitope (patient-side): HBT dropped HSV IgM positivity 49.7%→2.7%, EBV VCA 20.5%→2.7% — bulk viral-IgM "positives" were heterophile (anti-reagent), not virus | `P4_reading_notes.md` §4d | high |
| P4W-15 | Human anti-animal antibody interferences in immunological assays | Kricka LJ | 1999 | Clin Chem 45(7):942-56 | PMID 10388468 | P4W-15 - Kricka_1999_HAMA_interference.pdf | Canonical non-viral-epitope prior art (HAMA); cited >300× | `P4_reading_notes.md` §4d | high |
| P4W-16 | Potential false-positive reasons for SARS-CoV-2 antibody testing and its solution | Ye Q, Zhang T, Lu D | 2021 | J Med Virol 93(7):4242-46 | DOI 10.1002/jmv.26937; PMID 33710634 | P4W-16 - Ye_2021_false_positive_reasons.pdf | Names endogenous interferents: RF, heterophile, HAMA, lysozyme, complement, cross-antigens | `P4_reading_notes.md` §4d | medium |
| P4W-17 | False positive results in SARS-CoV-2 serological tests for samples with chronic inflammatory disease | Kharlamova N, et al. | 2021 | Front Immunol 12:666114 | DOI 10.3389/fimmu.2021.666114; PMID 34012450; PMC8126683 | P4W-17 - Kharlamova_2021_false_positive.pdf | Peer-reviewed stand-in for medRxiv PPR237451 | `P4_bibliography.md` §B | medium |
| P4W-18 | An interesting case of isolated false-reactive hepatitis B surface antigen | Costa V, et al. | 2021 | Case Reports Hepatol 2021:9928098 | DOI 10.1155/2021/9928098; PMID 34336313 | P4W-18 - Costa_2021_false_HBsAg.pdf | Heterophile → isolated HBsAg false positive | `P4_reading_notes.md` §4d | low |
| P4W-19 | HSV-2 AG-4 complement-fixation type specificity | Sherlock CH, et al. | 1986 | J Clin Microbiol 24(6):1093-7 | PMID 3023439; DOI not seen | P4W-19 - Sherlock_1986_HSV2_AG4_CF.pdf | Commercial CF "viral antigen" not type-specific (HSV-1 vs HSV-2 cross-read) — pre-recombinant example of antigen-driven serology reading beyond the intended agent | `P4_reading_notes.md` §4b | medium |
| P4W-20 | Multilayer Fluorescent Immunoassay for Dengue Using Host and Viral Biomarkers | Browne AS, et al. | 2025 | Bioconjug Chem 36(7):1474-82 | PMID 40503688; DOI not seen | P4W-20 - Browne_2025_dengue_host_viral.pdf | Reads host biomarkers alongside viral markers — host material diagnostically informative in a "viral" assay | `P4_reading_notes.md` §4b | medium |
| P4W-21 | Absence of evidence for bornavirus infection in schizophrenia, bipolar disorder and major depressive disorder | Hornig M, et al. | 2012 | Mol Psychiatry 17(5):486-93 | PMID 22290118; DOI not seen | P4W-21 - Hornig_2012_bornavirus.pdf | Falsifier-side anchor: serology "infection" claims disconfirmed by better-controlled measurement | `P4_reading_notes.md` §4d | high |
| P4W-22 | Convalescent serum exosomes as COVID-19 diagnostic | Krishnan A, et al. | 2022 | Exp Biol Med 247(14):1244-52 | DOI 10.1177/15353702221092984; PMID 35549570 | P4W-22 - Krishnan_2022_exosomes_COVID.pdf | False-positive serology from cross-reactivity (general) | `P4_bibliography.md` §A P4B-08 | low |
| P4W-23 | Comparison of measles IgG enzyme immunoassays to plaque reduction neutralization test (systematic review) | Lutz CS, et al. | 2023 | BMC Infect Dis 23:367 | PMID 37259032; DOI not seen | P4W-23 - Lutz_2023_measles_EIA_PRNT.pdf | Popularity anchor: names the dominant commercial measles IgG EIAs (Enzygnost, EUROIMMUN, Captia, SERION) | `P4_bibliography.md` §A3 P4B-20 | medium |
| P4W-24 | Serosurveillance for measles and rubella | Brady AM, et al. | 2024 | Vaccines (Basel) 12(7):816 | PMID 39066453; DOI not seen | P4W-24 - Brady_2024_serosurveillance.pdf | WHO-aligned standard commercial measles/rubella serology anchor | `P4_bibliography.md` §A3 P4B-21 | medium |
| P4W-25 | Evaluation of Chagas TESA VirClia | Silgado A, et al. | 2026 | J Clin Microbiol 64(7):e0173925 | PMID 42284051; DOI not seen | P4W-25 - Silgado_2026_Chagas_VirClia.pdf | Vircell VirClia chemiluminescence LIA anchor | `P4_bibliography.md` §A3 P4B-22 | medium |
| P4W-26 | A novel single-tier serologic test for all stages of Lyme disease | Levin AE, et al. | 2025 | J Clin Microbiol 63(9):e0048325 | PMID 40833084; DOI not seen | P4W-26 - Levin_2025_Lyme_single_tier.pdf | Modern C6-based single-tier Lyme immunoblot anchor (replaces 2-tier WB) | `P4_bibliography.md` §A3 P4B-23 | medium |
| P4W-27 | Performance of COVID19SEROSpeed rapid IgG/IgM test (multicenter) | Plebani M, et al. | 2021 | J Clin Microbiol 59(2):e02240-20 | PMID 33218990; DOI not seen | P4W-27 - Plebani_2021_Serospeed.pdf | Rapid/lateral-flow IgG-IgM class anchor | `P4_bibliography.md` §A3 P4B-24 | medium |

---

## Status note

- **Received 2026-11-08:** P4W-05 through P4W-27 are now in `refs/` and were read in full; the
  reading notes / bibliography have been re-tagged `[VERIFIED src]` (quote-checks + extended
  findings). Details per source in `P4_reading_notes.md`.
- **Two scanned-image exceptions (no text layer — OCR still needed):** P4W-07 Saliki 1998 and
  P4W-13 Bolin 1994. They remain `[DATA REQUIRED]`; the extracted text was empty/watermark-only.
- **Still needed (manufacturer inserts only):** P4W-03 and P4W-04 — see the email request drafts
  in `wrk/P4_insert_request_emails.md`.
- Items P4W-19 through P4W-27 were added 2026-11-07 in the abstract-only rectification pass; all
  are now received and read.

*End of P4 wishlist.*