# P7 PDF wishlist — full texts needed to clear deferred (abstract-identified) rows

**Purpose.** One registry of full texts needed to clear the `DATA_REQUIRED` rows (abstract-identified only)
to `VERIFIED`, recover serum/medium disclosure and matched-control design, and (where free text resolves
ambiguity) resolve `serum_disclosed`, `c_tier_link_r2`, and `discordance_value`. Until a row's full text is
read, that row is a deferred lead, not a claim.

**Every row carries full title + PMID + full DOI** so a fetch can be pinned to the exact document. Pass the
DOI (or the PMC URL, when `open_access` = yes) to the fetcher, not the PMID alone. PDFs go in the gitignored
`p7_cross_lab_repeatability/refs/` folder, saved under the `file_name` column. Never commit PDFs.

## Still needed (subscription; fetch by DOI)

| file_name | full title | PMID | full DOI | year | needed for |
|-----------|-----------|------|----------|------|-----------|
| leung2021_second_eqa_influenza.pdf | A second external quality assessment of isolation and identification of influenza viruses in cell culture in the Asia Pacific region highlights improved performance by participating laboratories | 34274614 | 10.1016/j.jcv.2021.104907 | 2021 | P7-002 |
| wernike2024_bvdv_proficiency.pdf | Comparison of bovine viral diarrhea virus detection methods: Results of an international proficiency trial | 38219410 | 10.1016/j.vetmic.2024.109985 | 2024 | P7-001 |

## Already fetched / open access (verify, then read)

| file_name | full title | PMID | full DOI | PMCID / open | needed for | status |
|-----------|-----------|------|----------|--------------|-----------|--------|
| reading2017_first_eqa_influenza.pdf | The first external quality assessment of isolation and identification of influenza viruses in cell culture in the Asia Pacific region, 2016 | 29127947 | 10.1016/j.jcv.2017.10.018 | (subscription) | P7-003 | ✅ read; cleared |
| goodell2016_swine_iav_ringtrial.pdf | Ring test evaluation of the detection of influenza A virus in swine oral fluids by real-time reverse-transcription polymerase chain reaction and virus isolation | 26733728 | (no DOI — Can J Vet Res) | PMC4686030 (free) | P7-004 | open, not yet read |
| perezramirez2020_rvf_eqa.pdf | External quality assessment of Rift Valley fever diagnosis in 17 veterinary laboratories of the Mediterranean and Black Sea regions | 32986725 | 10.1371/journal.pone.0239478 | PMC7521712 (free) | P7-005 | open, not yet read |
| yu2024_aav9_mn_interlab.pdf | Methodological Validation and Inter-Laboratory Comparison of Microneutralization Assay for Detecting Anti-AAV9 Neutralizing Antibody in Human | 39459848 | 10.3390/v16101512 | PMC11512302 (free) | P7-006 | open, not yet read |
| wernike2022_bvdv_serology.pdf | International proficiency trial for bovine viral diarrhea virus (BVDV) antibody detection: limitations of milk serology | 35524302 | 10.1186/s12917-022-03265-w | open access (BMC); PMC9074317 | P7-007 | ✅ read; cleared |

## Fetch audit (2026-11-07)

The first fetch round produced two wrong files because the wishlist at that time carried **only a short
title + PMID and no DOI**. This was corrected: every row now carries full title + PMID + full DOI. The
mislabelled files and their actual contents:

- `refs/reading2017_first_eqa_influenza.pdf` → ✅ correct (Reading 2017 accepted manuscript).
- `refs/wernike2024_bvdv_proficiency.pdf` → ❌ actually Wernike & Beer **2022** serology trial (BMC Vet Res
  18:168), i.e. the P7-007 paper, not the 2024 isolation paper. Recoded as P7-007; the 2024 paper is still
  outstanding under P7-001.
- `refs/leung2021_second_eqa_influenza.pdf` → ❌ actually an unrelated JSTOR article (Cacciari, "Nomes de
  Lugar: Confim", Revista de Letras 45(1)). The Leung 2021 paper is still outstanding under P7-002.

To avoid a repeat: when fetching, **use the full DOI**. For Can J Vet Res (Goodell 2016) there is no DOI —
use the PMCID URL `https://pmc.ncbi.nlm.nih.gov/articles/PMC4686030/`.