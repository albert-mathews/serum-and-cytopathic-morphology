# P4 bibliography — running reference trail

**Purpose:** maintain the trail from finding → source → peer-reviewed equivalent so nothing is
lost. One row per distinct source. Items already on the fetch wishlist are cross-referenced by
`P4W-###` (see `P4_pdf_wishlist.md`). Peer-reviewed column records whether the source is citable
for the paper, and if a non-peer-reviewed item "says the same thing," the peer-reviewed equivalent
is listed so the paper cites the latter.

> **Basis note (updated 2026-11-08 — full texts received).** Section B full texts were fetched into
> `refs/` and read. Every peer-reviewed source in §A, §A2, and §A3 is now `[VERIFIED src]`
> (quotes verified against the full text; findings extended in `P4_reading_notes.md`). The two
> scanned (image-only) PDFs — Saliki 1998 (`P4W-07`) and Bolin 1994 (`P4W-13`, §C, handed to R1) —
> were OCR'd 2026-11-08 (RapidOCR) and are now readable; Saliki is `[VERIFIED src]` and coded as
> `P4-019`. The kit inserts/catalogues backing the CSV rows were already full-text reads.

## A. Peer-reviewed sources (citable)

| ID | Citation | Provenance of note | P4 use |
|----|----------|--------------------|--------|
| P4B-01 | Kainulainen MH et al. 2026. Complement neutralization via cell-derived epitopes on enveloped viruses. mBio 17(3):e0170925. DOI 10.1128/mbio.01709-25. PMID 41685933 | full text — refs/P4W-05 | Anchor prior art: neutralizing antibody binds host GM2 ganglioside (cell-derived epitope) |
| P4B-02 | Ellis J et al. 2023. SARS coronavirus 2-reactive antibodies in bovine colostrum. Can Vet J 64(4):337-43. PMID 37008643 | found Europe PMC | Serum ingredient cross-reacts with "viral" antigen |
| P4B-03 | Saliki JT et al. 1998. Tick cell culture-derived Anaplasma antigen C-ELISA. Ann N Y Acad Sci 849:273-81. DOI 10.1111/j.1749-6632.1998.tb11059.x. PMID 9668475 | OCR full text — refs/P4W-07 (coded P4-019) | Reference antigen = infected cell lysate; matched uninfected lysate run and nonreactive (adversarial) |
| P4B-04 | Beier D et al. 2004. New BLV-producing cell line. J Virol Methods 121(2):239-46. DOI 10.1016/j.jviromet.2004.06.017. PMID 15381362 | PubMed E-utilities | Antigen-producing culture contaminant → false serology |
| P4B-05 | Xu Q et al. 2022. Plant-derived E2 immunochromatographic strip for CSFV. Microbiol Spectr 10(4):e0105022. DOI 10.1128/spectrum.01050-22. PMID 35862968 | PubMed E-utilities | Lateral-flow format; culture antigen FBS risk noted |
| P4B-06 | Sherlock CH et al. 1986. HSV-2 AG-4 CF type specificity. J Clin Microbiol 24(6):1093-7. PMID 3023439 | Europe PMC | Commercial CF antigen not type-specific |
| P4B-07 | Browne AS et al. 2025. Dengue immunoassay using host + viral biomarkers. Bioconjug Chem 36(7):1474-82. PMID 40503688 | Europe PMC | Host material diagnostically informative in "viral" assay |
| P4B-08 | Krishnan A et al. 2022. Convalescent serum exosomes as COVID-19 diagnostic. Exp Biol Med 247(14):1244-52. DOI 10.1177/15353702221092984. PMID 35549570 | full text — refs/P4W-22 | Minireview (not experimental): asserts false positives come from "cross-reactivity of the viral antigens or… patient-related autoimmune factors", and that EVs share endosomal sorting with viruses — background/argument only |

## A2. Non-viral-epitope evidence — interference, cross-reactivity, and disconfirmation (added 2026-11-06)

| ID | Citation | Note |
|----|----------|------|
| P4B-11 | Kricka LJ. 1999. Human anti-animal antibody interferences in immunological assays. Clin Chem 45(7):942-56. PMID 10388468 (cited 318×) | Canonical non-viral-epitope (patient-side) prior art: HAMA/anti-species antibodies cause both + and − interference in two-site mAb assays |
| P4B-12 | Song J et al. 2025. Resolving heterophile antibody interference in viral serology using blocking tubes. Microbiologyopen 14(6):e70098. DOI 10.1002/mbo3.70098. PMID 41144880 | Viral IgM survery: HBT dropped HSV positivity 49.7%→2.7%, EBV VCA 20.5%→2.7% — bulk "positives" were heterophile, not virus |
| P4B-13 | Ye Q et al. 2021. Potential false-positive reasons for SARS-CoV-2 antibody testing. J Med Virol 93(7):4242-46. PMID 33710634 | Lists endogenous interferents (RF, heterophile, HAMA, lysozyme, complement, cross-antigens) |
| P4B-14 | Kharlamova N et al. 2021. False positive SARS-CoV-2 serology in chronic inflammatory disease. Front Immunol 12:666114. DOI 10.3389/fimmu.2021.666114. PMID 34012450 | Peer-reviewed; predicts false positives from non-viral immune state |
| P4B-15 | Costa V et al. 2021. Isolated false-reactive HBsAg. Case Reports Hepatol 2021:9928098. PMID 34336313 | Heterophile antibody → isolated HBsAg false positive |
| P4B-19 | Hornig M et al. 2012. Absence of evidence for bornavirus infection in schizophrenia, bipolar disorder and major depressive disorder. Mol Psychiatry 17(5):486-93. PMID 22290118 | Cautionary: serology "infection" claims disconfirmed by better controls — falsifier-side anchor |
| P4B-25 | Grimm K et al. 2024. Serologic testing of US blood donations to identify SARS-CoV-2 and other coronaviruses, Dec 2019–Jul 2020. Open Forum Infect Dis 11(7):ofae351. DOI 10.1093/ofid/ofae351. PMID 39026530 | Healthy/pre-pandemic blood donors cross-react on SARS-CoV-2 serology — clean "positive, no virus expected" patient-side case |
| P4B-26 | Luo M et al. 2025. False-positive treponemal syphilis serology linked to EBV-related heterophile antibodies. IDCases 42:e02403. DOI 10.1016/j.idcr.2025.e02403. PMID 41209423 | Heterophile (non-viral) antibody drives false positive in a different pathogen's serology |
| P4B-27 | Nowak K et al. 2025. When serology misleads: cross-reactivity in acute hepatitis. Arch Virol 171(1):12. DOI 10.1007/s00705-025-06470-8. PMID 41348228 | Review — serology cross-reactivity as a general failure mode |
| P4B-28 | Chen D et al. 2026. Impact of cross-reactive antibodies induced by SARS-CoV-2 infection on the false-positive rate of HIV serological testing. Indian J Hematol Blood Transfus 42(4):1448-54. DOI 10.1007/s12288-025-02081-0. PMID 42333151 | Cross-reactivity inflates a serology false-positive rate (HIV assay — out of P4 scope; kept for the cross-reactivity mechanism only) |

## A3. Product popularity / market anchors (for the shortlist, added 2026-11-06)

| ID | Citation | Anchors the popularity of |
|----|----------|----------------------------|
| P4B-20 | Lutz CS et al. 2023. Comparison of measles IgG EIA vs PRNT (systematic review). BMC Infect Dis 23:367. PMID 37259032 | dominant commercial measles IgG EIAs (Enzygnost, EUROIMMUN, Captia, SERION) |
| P4B-21 | Brady AM et al. 2024. Serosurveillance for measles and rubella. Vaccines 12(7):816. PMID 39066453 | WHO-aligned standard commercial measles/rubella serology |
| P4B-22 | Silgado A et al. 2026. Evaluation of Chagas TESA VirClia. J Clin Microbiol 64(7):e0173925. PMID 42284051 | Vircell VirClia chemiluminescence LIA |
| P4B-23 | Levin AE et al. 2025. A novel single-tier serologic test for all stages of Lyme disease. J Clin Microbiol 63(9):e0048325. PMID 40833084 | Lyme single-tier immunoblot (modern C6-based, replaces 2-tier WB) |
| P4B-24 | Plebani M et al. 2021. Performance of COVID19SEROSpeed rapid IgG/IgM test (multicenter). J Clin Microbiol 59(2):e02240-20. PMID 33218990 | rapid/lateral-flow IgG-IgM class |

## B. Non-peer-reviewed sources and their peer-reviewed stand-ins

| ID | Non-PR item | Says | Peer-reviewed equivalent (on wishlist) | Locator |
|----|-------------|------|----------------------------------------|---------|
| P4B-16 | Kharlamova N et al. medRxiv 2020.11.13.20231076. SARS-CoV-2 serology false positives in chronic inflammatory disease | preprint of P4B-14 | **P4B-14** (Front Immunol 2021, PMID 34012450) — already located, cites it directly | — |
| P4B-09 | Chodavarapu, Mallepaddi, Podha 2026. JEV antigen downstream purification. Zenodo. DOI 10.5281/zenodo.23842428 | culture-derived "viral antigen" contains host-cell protein/DNA impurities | seek a peer-reviewed JEV/vaccine antigen impurity-clearance paper | P4W-11 |

## C. Handed to R1 (not P4 bibliography)

Giammarioli 2015 (PMID 26071653), Bolin 1994 (PMID 7989247), Muhsen 2013 (PMID 23178968) —
filed to `../r1_isolation_standards_and_practice/P4_handoff_to_R1.md`.

## Fill rule

- Add a row the moment a source is *located* (abstract or full text), with its peer-reviewed
  stand-in if it is a preprint/Zenodo/report.
- Do not drop a reference from this table; mark it `handed_to_R1` or `excluded` instead of deleting.
- Every row feeding the paper must have a peer-reviewed locator (DOI or PMID); preprints are
  admissible only as leads, never as the paper's citation.

*End of P4 bibliography.*