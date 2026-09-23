# P3 GenBank/RefSeq metadata mining — pilot results

**Date:** 2026-09-19 (America/Toronto)
**Scope:** RefSeq viral complete genomes — catalog-card metadata only (no sequence re-analysis).
**Base query:** `Viruses[Organism] AND srcdb_refseq[PROP] AND "complete genome"[Title]`
**M0 Count:** **11073**
**Sample n:** 2000 (first 2000 of 11073 (NCBI default order; not random). For large N, pilot uses first-N systematic slice.)

## Guardrails (read first)

- Results estimate how often records **mention** culture/CPE language in metadata — **not** that they “are culture artifacts.”
- **Under-annotation:** missing keywords do not prove a clinical-only path.
- This pilot reports metadata prevalence only; sequence ontology conclusions require type-material reading beyond this catalog slice.
## Fast esearch prevalence (full base set)

| Slice | Count | % of M0 |
|-------|------:|--------:|
| culture_cell | 2003 | 18.09% |
| cpe | 6 | 0.05% |
| passage | 148 | 1.34% |
| clinical | 609 | 5.50% |
| culture_and_clinical | 9 | 0.08% |
| clinical_not_culture | 600 | 5.42% |


## Sample composition caveats (important)

- NCBI first-2000 slice is **not random**: years heavily **2023–2026**; **694/2000 (34.7%)** have “phage” in ORGANISM.
- Phage records often annotate bacterial `/lab_host`, which matches the culture-cell keyword list → **sample M1 (11.25%) is inflated** relative to vertebrate cell-line advertising.
- **Non-phage subset (n=1306):** culture-cell 1.30%; CPE 0.00%; clinical∧¬culture 26.26%.
- Prefer **esearch percentages on full M0=11073** for prevalence (M1/M2/M5); use sample for exploratory M3/M4.

## Sampled deep parse

Parsed metadata for **2000** records → `refseq_viral_complete_metadata_sample.csv`.

| Flag | n | % of sample |
|------|--:|-----------:|
| culture_cell | 225 | 11.25% |
| cpe | 0 | 0.00% |
| passage | 16 | 0.80% |
| clinical | 355 | 17.75% |
| clinical_no_culture | 354 | 17.70% |

### M1 — culture-cell keywords

- **Esearch:** 18.09% of base (2003/11073)
- **Sample parse:** 11.25% (225/2000)

### M2 — CPE / cytopathic language

- **Esearch:** 0.05% of base (6/11073)
- **Sample parse:** 0.00% (0/2000)

### M3 — by year (sample)

| Year | n | culture % | CPE % |
|------|--:|----------:|------:|
| 2023 | 1260 | 13.57 | 0.0 |
| 2024 | 5 | 0.0 | 0.0 |
| 2025 | 261 | 11.88 | 0.0 |
| 2026 | 474 | 4.85 | 0.0 |

### M4 — top organisms in sample (by count)

| Organism | n | culture % | CPE % |
|----------|--:|----------:|------:|
| Genomoviridae sp. | 45 | 0.0 | 0.0 |
| Anelloviridae sp. | 22 | 0.0 | 0.0 |
| Adult diarrheal rotavirus strain J19 | 11 | 0.0 | 0.0 |
| Giant panda anellovirus | 11 | 0.0 | 0.0 |
| Enterobacteria phage f1 | 10 | 0.0 | 0.0 |
| Porcine associated porprismacovirus | 10 | 0.0 | 0.0 |
| Giant panda associated gemycircularvirus | 9 | 0.0 | 0.0 |
| TTV-like mini virus | 6 | 0.0 | 0.0 |
| Bacteriophage sp. | 5 | 0.0 | 0.0 |
| Bat associated densovirus | 5 | 0.0 | 0.0 |
| Paguma larvata torque teno virus | 5 | 0.0 | 0.0 |
| Yangshan Harbor Nitrososphaeria virus | 4 | 0.0 | 0.0 |
| Parvoviridae sp. | 4 | 0.0 | 0.0 |
| Bat paramyxovirus | 3 | 66.67 | 0.0 |
| Fushun phasmavirus 2 | 3 | 0.0 | 0.0 |
| Fushun phasmavirus 1 | 3 | 0.0 | 0.0 |
| Alphacoronavirus sp. | 3 | 0.0 | 0.0 |
| Gemycircularvirus sp. | 3 | 0.0 | 0.0 |
| Chlorocebus cynosuros associated smacovirus | 3 | 0.0 | 0.0 |
| Rodent stool-associated circular genome virus | 3 | 0.0 | 0.0 |

### M5 — clinical-looking without culture keywords

- **Esearch clinical NOT culture:** 5.42% (600/11073)
- **Esearch clinical ∩ culture:** 0.08% (9/11073)
- **Sample clinical ∧ ¬culture:** 17.70% (354/2000)

### M6 — type-strain audit high-risk vs keywords

High-risk audit rows: 26; successfully fetched: 22; also in RefSeq complete-genome sample: 0.
Of fetched high-risk: **4** mention culture-cell keywords; **0** mention CPE language.

| audit_id | virus | matched | culture | CPE | in_sample |
|----------|-------|---------|--------:|----:|:---------:|
| P3T001 | Poliovirus 1 Mahoney (Enterovirus C) | V01149 | 0 | 0 | N |
| P3T002 | Measles morbillivirus Edmonston | NC_001498 | 1 | 0 | N |
| P3T003 | Human alphaherpesvirus 1 strain 17 (HSV- | NC_001806 | 0 | 0 | N |
| P3T004 | Human mastadenovirus C / Human adenoviru | AC_000008 | 0 | 0 | N |
| P3T005 | Influenza A virus A/Puerto Rico/8/1934 ( | NC_002016 | 0 | 0 | N |
| P3T006 | Vaccinia virus Western Reserve (WR) | NC_006998 | 1 | 0 | N |
| P3T007 | Vesicular stomatitis Indiana virus | NC_001560 | 0 | 0 | N |
| P3T008 | Human orthopneumovirus (RSV) A Long | AY911262 | 0 | 0 | N |
| P3T009 | Human cytomegalovirus AD169 | NC_006273 | 0 | 0 | N |
| P3T010 | Epstein-Barr virus B95-8 | NC_007605 | 0 | 0 | N |
| P3T011 | Varicella-zoster virus Oka (parental/vac | — | — | — | N |
| P3T012 | MERS-CoV EMC/2012 | JX869059 | 0 | 0 | N |
| P3T013 | Ebola virus Mayinga | NC_002549 | 0 | 0 | N |
| P3T014 | Nipah virus (Malaysia) | NC_002728 | 0 | 0 | N |
| P3T015 | Lassa virus Josiah | NC_004296 | 0 | 0 | N |
| P3T016 | Rubella virus (e.g. Therien / vaccine RA | NC_001545 | 0 | 0 | N |
| P3T017 | Yellow fever virus 17D | NC_002031 | 0 | 0 | N |
| P3T018 | Rabies virus PV / SAD laboratory lineage | NC_001542 | 0 | 0 | N |
| P3T019 | Foot-and-mouth disease virus (prototype  | — | — | — | N |
| P3T020 | Simian virus 40 (SV40) reference strains | NC_001669 | 0 | 0 | N |
| P3T021 | Human immunodeficiency virus 1 (HXB2 / L | K03455 | 0 | 0 | N |
| P3T022 | SARS-CoV Urbani / Tor2 laboratory Isolat | AY278741 | 1 | 0 | N |
| P3T041 | Dengue virus type 2 NGC / 16681 laborato | NC_001474 | 0 | 0 | N |
| P3T042 | Chikungunya virus S27 / La Reunion labor | NC_004162 | 1 | 0 | N |
| P3T043 | Human adenovirus 7 (prototype vaccine/la | — | — | — | N |
| P3T045 | Rotavirus A (Wa / SA11 reference strains | — | — | — | N |

### M7 — low-risk audit vs culture keywords

Low-risk rows: 10; fetched: 6; with culture keywords: **0** (annotation noise / dual-path flag).

| audit_id | virus | matched | culture | CPE |
|----------|-------|---------|--------:|----:|
| P3T031 | SARS-CoV-2 Wuhan-Hu-1 (clinical BALF gen | NC_045512 | 0 | 0 |
| P3T032 | 2019-nCoV clinical BALF genomes MN988668 | MN988668 | 0 | 0 |
| P3T033 | Human bocavirus (discovery sequences) | DQ000495 | 0 | 0 |
| P3T034 | Norwalk virus (norovirus GI.1 prototype  | M87661 | 0 | 0 |
| P3T035 | Human sapovirus (clinical genomes; ICTV  | — | — | — |
| P3T036 | Rift Valley fever virus clinical metagen | OR972326 | 0 | 0 |
| P3T037 | Hepatitis E virus clinical/molecular ref | — | — | — |
| P3T038 | Torque teno virus / Anelloviridae clinic | — | — | — |
| P3T039 | BK polyomavirus clinical molecular refer | NC_001538 | 0 | 0 |
| P3T040 | Human astrovirus clinical stool genomes  | — | — | — |

## Files

- `mining_summary.json` — machine-readable aggregates
- `refseq_viral_complete_metadata_sample.csv` — one row per sampled accession
- `run_pilot.py` — reproducible runner
- `run_log.txt` / `run_console.txt` — console logs

*Pilot only — metadata mentions, not particle identity.*