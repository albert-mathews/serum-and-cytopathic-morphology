# P4 bibliography — running reference trail

**Purpose:** maintain the trail from finding → source → peer-reviewed equivalent so nothing is
lost. One row per distinct source. Items already on the fetch wishlist are cross-referenced by
`P4W-###` (see `P4_pdf_wishlist.md`). Peer-reviewed column records whether the source is citable
for the paper, and if a non-peer-reviewed item "says the same thing," the peer-reviewed equivalent
is listed so the paper cites the latter.

## A. Peer-reviewed sources (citable)

| ID | Citation | Provenance of note | P4 use |
|----|----------|--------------------|--------|
| P4B-01 | Kainulainen MH et al. 2026. Complement neutralization via cell-derived epitopes on enveloped viruses. mBio 17(3):e0170925. DOI 10.1128/mbio.01709-25. PMID 41685933 | found Europe PMC full-text search | Anchor prior art: neutralizing antibody binds host GM2 ganglioside (cell-derived epitope) |
| P4B-02 | Ellis J et al. 2023. SARS coronavirus 2-reactive antibodies in bovine colostrum. Can Vet J 64(4):337-43. PMID 37008643 | found Europe PMC | Serum ingredient cross-reacts with "viral" antigen |
| P4B-03 | Saliki JT et al. 1998. Tick cell culture-derived Anaplasma antigen C-ELISA. Ann N Y Acad Sci 849:273-81. DOI 10.1111/j.1749-6632.1998.tb11059.x. PMID 9668475 | PubMed E-utilities | Reference antigen = infected cell lysate (census candidate) |
| P4B-04 | Beier D et al. 2004. New BLV-producing cell line. J Virol Methods 121(2):239-46. DOI 10.1016/j.jviromet.2004.06.017. PMID 15381362 | PubMed E-utilities | Antigen-producing culture contaminant → false serology |
| P4B-05 | Xu Q et al. 2022. Plant-derived E2 immunochromatographic strip for CSFV. Microbiol Spectr 10(4):e0105022. DOI 10.1128/spectrum.01050-22. PMID 35862968 | PubMed E-utilities | Lateral-flow format; culture antigen FBS risk noted |
| P4B-06 | Sherlock CH et al. 1986. HSV-2 AG-4 CF type specificity. J Clin Microbiol 24(6):1093-7. PMID 3023439 | Europe PMC | Commercial CF antigen not type-specific |
| P4B-07 | Browne AS et al. 2025. Dengue immunoassay using host + viral biomarkers. Bioconjug Chem 36(7):1474-82. PMID 40503688 | Europe PMC | Host material diagnostically informative in "viral" assay |
| P4B-08 | Krishnan A et al. 2022. Convalescent serum exosomes as COVID-19 diagnostic. Exp Biol Med 247(14):1244-52. DOI 10.1177/15353702221092984. PMID 35549570 | PubMed E-utilities | False-positive serology from cross-reactivity (general) |

## A2. Assay-artifact and cross-reactivity arm (arm C / D, added 2026-11-06)

| ID | Citation | Note |
|----|----------|------|
| P4B-11 | Kricka LJ. 1999. Human anti-animal antibody interferences in immunological assays. Clin Chem 45(7):942-56. PMID 10388468 (cited 318×) | Canonical arm-D prior art: HAMA/anti-species antibodies cause both + and − interference in two-site mAb assays |
| P4B-12 | Song J et al. 2025. Resolving heterophile antibody interference in viral serology using blocking tubes. Microbiologyopen 14(6):e70098. DOI 10.1002/mbo3.70098. PMID 41144880 | Viral IgM survery: HBT dropped HSV positivity 49.7%→2.7%, EBV VCA 20.5%→2.7% — bulk "positives" were heterophile, not virus |
| P4B-13 | Ye Q et al. 2021. Potential false-positive reasons for SARS-CoV-2 antibody testing. J Med Virol 93(7):4242-46. PMID 33710634 | Lists endogenous interferents (RF, heterophile, HAMA, lysozyme, complement, cross-antigens) |
| P4B-14 | Kharlamova N et al. 2021. False positive SARS-CoV-2 serology in chronic inflammatory disease. Front Immunol 12:666114. DOI 10.3389/fimmu.2021.666114. PMID 34012450 | Peer-reviewed; predicts false positives from non-viral immune state |
| P4B-15 | Costa V et al. 2021. Isolated false-reactive HBsAg. Case Reports Hepatol 2021:9928098. PMID 34336313 | Heterophile antibody → isolated HBsAg false positive |

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