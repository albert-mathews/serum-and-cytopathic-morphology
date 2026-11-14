# P7 PDF wishlist — provenance record + deepening leads

**Purpose.** Registry of full texts for the P7 corpus. All 11 coded rows are `VERIFIED` (full text read)
and every source PDF is saved locally in `refs/`. This file is retained as (a) the provenance record
(full title + PMID + full DOI per source), and (b) the list of *deepening leads* for the next expansion.

**Every row carries full title + PMID + full DOI** so a fetch can be pinned to the exact document. Pass the
DOI (or the PMC URL, when `open_access` = yes) to the fetcher, not the PMID alone. PDFs go in the gitignored
`p7_cross_lab_repeatability/refs/` folder, saved under the `file_name` column. Never commit PDFs.

## Corpus provenance (11 rows, all fetched + read + VERIFIED)

| file_name | full title | PMID | full DOI | row |
|-----------|-----------|------|----------|-----|
| wernike2024_bvdv_proficiency.pdf | Comparison of bovine viral diarrhea virus detection methods: Results of an international proficiency trial | 38219410 | 10.1016/j.vetmic.2024.109985 | P7-001 |
| leung2021_second_eqa_influenza.pdf | A second external quality assessment of isolation and identification of influenza viruses in cell culture in the Asia Pacific region… | 34274614 | 10.1016/j.jcv.2021.104907 | P7-002 |
| reading2017_first_eqa_influenza.pdf | The first external quality assessment of isolation and identification of influenza viruses in cell culture in the Asia Pacific region, 2016 | 29127947 | 10.1016/j.jcv.2017.10.018 | P7-003 |
| goodell2016_swine_iav_ringtrial.pdf | Ring test evaluation of the detection of influenza A virus in swine oral fluids by real-time reverse-transcription polymerase chain reaction and virus isolation | 26733728 | (no DOI — Can J Vet Res) | P7-004 |
| perezramirez2020_rvf_eqa.pdf | External quality assessment of Rift Valley fever diagnosis in 17 veterinary laboratories of the Mediterranean and Black Sea regions | 32986725 | 10.1371/journal.pone.0239478 | P7-005 |
| yu2024_aav9_mn_interlab.pdf | Methodological Validation and Inter-Laboratory Comparison of Microneutralization Assay for Detecting Anti-AAV9 Neutralizing Antibody in Human | 39459848 | 10.3390/v16101512 | P7-006 |
| wernike2022_bvdv_serology.pdf | International proficiency trial for bovine viral diarrhea virus (BVDV) antibody detection: limitations of milk serology | 35524302 | 10.1186/s12917-022-03265-w | P7-007 |
| olesen2022_asfv_multilab.pdf | A Multi-Laboratory Comparison of Methods for Detection and Quantification of African Swine Fever Virus | 35335649 | 10.3390/pathogens11030325 | P7-008 |
| wernike2019_german_bvdv.pdf | Diagnostics in the context of an eradication program: Results of the German bovine viral diarrhea proficiency trial | 31767099 | 10.1016/j.vetmic.2019.108452 | P7-009 |
| brangel2024_sarscov2_antigenicity.pdf | A Global Collaborative Comparison of SARS-CoV-2 Antigenicity Across 15 Laboratories | 39772242 | 10.3390/v16121936 | P7-010 |
| onyilagha2026_csf_asf_americas.pdf | Multi-laboratory proficiency assessment for molecular and serological diagnosis of classical and African swine fever in the Americas | (PMC only) | 10.3389/fvets.2026.1874382 | P7-011 |

Supporting (fetched, not a corpus row — no discordance metric): `squires2018_who_influenza_eqa.pdf`
(PMID 31832255, DOI 10.5365/wpsar.2018.9.5.006) — WHO influenza EQA program overview.

## Deepening leads — identified sources (fetch next)

These are *confirmed* ring-trial / inter-lab sources found in the 2026-11-12 search. Each targets a gap in the
current 11-row corpus; add to `p7_repeatability_corpus.csv` only after the full text is read and the
blinding/serum columns resolved. Most are open access — see the open-access policy above (all go on the
wishlist regardless).

| file_name | full title | PMID | full DOI | endpoint | why |
|-----------|-----------|------|----------|----------|-----|
| ferris2006_fmd_isolation.pdf | Foot-and-mouth disease virus: A first inter-laboratory comparison trial to evaluate virus isolation and RT-PCR detection methods | 16846700 | 10.1016/j.vetmic.2006.06.001 | FMD virus isolation + RT-PCR | **first-class Isolation**; subscription — STILL TO FETCH |
| keck2022_fmd_germany.pdf | Proof of Proficiency of Decentralized Foot-and-Mouth Disease Virus Diagnostics in Germany | 35632839 | 10.3390/v14051098 | FMD RT-qPCR + NSP ELISA (blinded) | ✅ fetched, read → P7-014 |
| dill2017_fmd_germany.pdf | Inter-laboratory validation of foot-and-mouth disease diagnostic capability in Germany | 28619169 | 10.1016/j.vetmic.2017.03.001 | FMD molecular/serology | ✅ fetched, read → P7-015 |
| gourlaouen2020_rabies_africa.pdf | An inter-laboratory trial as a tool to increase rabies diagnostic capabilities of Sub-Saharan African Veterinary laboratories | 32040472 | 10.1371/journal.pntd.0008010 | rabies DFA + RT-PCR | ✅ fetched, read → P7-012 |
| clavijo2017_rabies_lac.pdf | An inter-laboratory proficiency testing exercise for rabies diagnosis in Latin America and the Caribbean | 28369139 | 10.1371/journal.pntd.0005427 | rabies DFA | ✅ fetched, read → P7-013 |
| gigante2018_lyssavirus_ln34.pdf | Multi-site evaluation of the LN34 pan-lyssavirus real-time RT-PCR assay for post-mortem rabies diagnostics | 29768505 | 10.1371/journal.pone.0197074 | rabies LN34 RT-PCR | ✅ fetched, read → P7-017 |
| fischer2013_lyssavirus_ringtrial.pdf | A step forward in molecular diagnostics of lyssaviruses—results of a ring trial among European laboratories | 23520505 | 10.1371/journal.pone.0058372 | lyssavirus molecular | ✅ fetched, read → P7-016 |

## Note on the identified leads (classified + fetched 2026-11-12)

All six deepening leads below are now fetched and read (rows P7-012..P7-017 coded `VERIFIED`). Classification
correction: **none of the six is virus isolation/CPE** — they are antigen/molecular/serology, so they extend
the stream corpus but do **not** enter `C080.csv` (which stays Isolation-only, 4 rows):

- Gourlaouen 2020 (rabies, n=13) → **DFA 87.69% vs RT-PCR 98.2% concordance** — the key new data: the
  human-microscopy readout (fluorescent antibody) underperforms molecular (P7-012).
- Clavijo 2017 (rabies, n=23) → DFA practice heterogeneity (no standardized protocol) (P7-013).
- Keck 2022 (FMD, n=23) → explicitly **blinded** molecular/serology, near-perfect (P7-014).
- Dill 2017 (FMD, n=20) → molecular/LFD/serology robust (P7-015).
- Fischer 2013 (lyssavirus, n=16) → molecular robust; multi-assay labs always correct (P7-016).
- Gigante 2018 (lyssavirus, n=14) → LN34 RT-PCR vs DFA (P7-017).

The true first-class **FMD virus-isolation** inter-lab trial remains **Ferris NP et al. 2006**, *Vet Microbiol*
117:130–140 (PMID 16846700, DOI 10.1016/j.vetmic.2006.06.001, subscription) — still to fetch for a first-class
Isolation row.

## Still-untargeted prediction tests (no confirmed source yet)

These remain *search targets*, not confirmed sources; a row is added only once a full text is read.

1. **Blinded morphology across sites (R3-style).** Multi-rater / multi-site scoring of the same CPE images —
   prediction test #3 / failure mode 3 (rater threshold drift). Search: "cytopathic effect" + "inter-rater" /
   "observer agreement" / "kappa" / "blinded".
2. **Same-stock assembly discordance (P3 A3).** One named stock sequenced/assembled in multiple centers with
   divergent contigs — the genetics arm of P7 / C151. Search: "inter-laboratory" + "assembly" + "viral genome"
   + "discordance" / "discrepancy".
3. **Serum-lot shock (failure mode 2).** A study where switching FBS lot changes CPE/titer without inoculum
   change. Search: "fetal bovine serum" + "lot" + "cytopathic" / "titer" + "variability".

## Fetch audit

- **2026-11-07 (first round):** two wrong files because the wishlist carried only a short title + PMID and no
  DOI. Corrected: every row now carries full title + PMID + full DOI.
- **2026-11-12 (second round):** the two subscription papers were re-fetched correctly (Leung 2021, Wernike &
  Beer 2024) and read; the three open-access papers were read from PMC.
- **2026-11-12 (third round):** all remaining items fetched (Wernike 2019 subscription; Goodell, Pérez-Ramírez,
  Yu, Olesen open-access; Brangel, Onyilagha, Squires expansion leads). All 11 rows coded `VERIFIED`.

To avoid a repeat: when fetching, **use the full DOI**. For Can J Vet Res (Goodell 2016) there is no DOI —
use the PMCID URL `https://pmc.ncbi.nlm.nih.gov/articles/PMC4686030/`.