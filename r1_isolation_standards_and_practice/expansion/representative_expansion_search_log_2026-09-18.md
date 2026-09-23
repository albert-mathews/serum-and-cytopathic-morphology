# Representative expansion search log — 2026-09-18

**Timezone:** written ~2026-09-18 evening America/Toronto (UTC-4).
**Sampling frame (user correction):** equal-weight any dual numeric pre/post FBS (including 0). Do **not** privilege or deprioritize 10→2; pattern counts are for reporting only.

## Baseline
- Expanded n before: **167**
- Dual n before: **148**
- Max VI before: **VI271**
- Dedup keys built from expansion + root CSVs: **346** keys (`_dedup_keys_repr.json`)

## Search strategies (pattern-agnostic)
1. **EuropePMC OA full-text** queries for maintenance/growth/infection/isolation medium + FBS across virus families (enterovirus, adenovirus, measles/rubella, HSV/RSV, PRRSV/PPRV/IBDV, arboviruses, influenza, aquatic, shell-vial, Numazaki/microplate).
2. **Decade-light stratification:** OA scans spanning 1990s–2020s; within each stratum accepted whatever dual numeric practice the paper reported.
3. **Author/lab threads continued:** PPRV veterinary isolation; aquatic (ranavirus, nodavirus, CyHV-2); SARS clinical isolation systems; filovirus culture; hantavirus patient isolation; rabies Vero adaptation.
4. **Non-English / regional:** FCS-coded Ethiopian IBDV Vero adaptation (EN); aquatic JP/EN OA; feline/porcine veterinary EN OA.
5. **Institution:** added **Health Canada / CCDR Measles Surveillance Lab Support (B95-a)** — growth 5–10% FBS, maintenance 2% FBS. Did **not** re-add CLSI/ASM/ATCC/NEADL/ANSES/CDC measles/VIRPRO1013.

## QC rules
- Dual only when **both** stages numeric (0 allowed).
- Prefer primary/field/clinical specimen isolation or explicit diagnostic/adaptation culture with growth + post-inoculation %.
- Excluded antiviral IC50-only papers, off-topic cell biology, and soft cases where post-% was not restated after inoculation (e.g. prior soft SARS 10→5 NIID inoculum-only).
- Never invent %.

## Outcomes
- Candidates written: **22** → `expansion/representative_expansion_candidates_2026-09-18.csv`
- Upserted dual practice rows: **22** (VI272–VI293)
- Dual n: **148 → 170** (Δ = **+22**)
- Expanded n: **167 → 189**
- Institution adds: Health Canada B95-a measles (5–10% → 2%)
- Plots regenerated into `expansion/fbs_distribution_plots/` via `plot_fbs_distributions.py`

## New dual pairs by pattern (reporting only; inclusion not ranked by pattern)
| Pattern | n new |
|---------|------:|
| 10→2 | 13 |
| 10→0 | 2 |
| 10→1 | 1 |
| 10→5 | 1 |
| 10→2.5 | 1 |
| 10→10 | 1 |
| 5→5 | 1 |
| 5→2 | 1 |
| 5→0 | 1 |
| **Total** | **22** |
| **10→2 share of new** | **13/22 (59%)** |
| **Other patterns** | **9/22 (41%)** |

## New dual IDs (short)
- VI272 10→2 Ranavirus McRV / BF-2 / L-15
- VI273 10→2 Betanodavirus gonad / RTG-2 / L-15
- VI274 10→2 IBDV Vero adaptation / DMEM (FCS)
- VI275 10→2 PPRV in vitro isolation / Vero; SEK
- VI276 10→0 Bat MRV / Vero (trypsin MM, no FBS)
- VI277 10→2 DEV field outbreak / CEF
- VI278 10→1 FAdV-8a / LMH
- VI279 10→2 GETV piglet brain / Vero; N2a
- VI280 10→0 PEDV intestinal / Vero (serum-free + trypsin)
- VI281 5→5 HEV retail pork pâté / A549-D3
- VI282 10→2 Ebola outbreak-variant culture / VeroE6
- VI283 10→2 PRRSV Marc-145 post-inoculation practice
- VI284 10→2 Negevirus mosquito / C6/36
- VI285 10→5 SARS-CoV-2 feline primary isolation / Vero E6
- VI286 10→2 FPV anal swab / CRFK
- VI287 10→2.5 SARS-CoV-2 clinical Alpha swab / Vero-E6-TMPRSS2
- VI288 10→2 CyHV-2 / FtGF / L-15
- VI289 10→2 JEV culture / Vero
- VI290 5→0 Influenza A tissue homogenate / MDCK (trypsin MM)
- VI291 10→2 Orthohantavirus patient isolates / Vero-E6
- VI292 10→10 SARS-CoV-2 clinical isolation systems / Caco-2; HuH-6
- VI293 5→2 Rabies Vero-adapted Flury HEP

## Virus / decade mix (new batch)
- **Families:** ranavirus, nodavirus, birnavirus (IBDV), morbillivirus (PPRV), reovirus (bat MRV), avian herpes (DEV), adenovirus (FAdV), alphavirus (GETV), coronavirus (PEDV, SARS-CoV-2×3), hepevirus (HEV), filovirus (Ebola), arterivirus (PRRSV), negevirus, parvovirus (FPV), cyprinid herpesvirus, flavivirus (JEV), orthomyxovirus (IAV), hantavirus, rhabdovirus (rabies).
- **Decades:** 2016 (1), 2020 (1), 2021 (1), 2022 (1), 2023 (1), 2024 (7), 2025 (5), 2026 (5) — OA full-text availability skews recent; older classic 10→2 still present in prior corpus (Yamagata/Mizuta, Hierholzer, etc.).

## Notes on target (≥25–40)
- Literature-supported **verified dual** yield this pass = **22** after strict isolation/practice QC (many EPMC hits were antiviral/lab-stock only).
- 10→2 remains the modal practice pattern among new rows (**59%**), consistent with a representative (not adversarial) sample; non-10→2 patterns were coded with equal priority when found (equal-holds, serum-free MM, 10→1, 10→5, 5→2, etc.).

## Paths
- `expansion/representative_expansion_candidates_2026-09-18.csv`
- `expansion/isolation-refs-overview_expanded.csv` (n=189)
- `expansion/isolation-refs-dual-fbs_only.csv` (n=170)
- `expansion/representative_expansion_search_log_2026-09-18.md`
- `expansion/fbs_distribution_plots/`
- `institution-guideline-protocol-refs.csv` (Health Canada B95-a added)

## Plot regeneration
- Command: `python plot_fbs_distributions.py --papers isolation-refs-dual-fbs_only.csv --institutions ..\institution-guideline-protocol-refs.csv --outdir fbs_distribution_plots`
- Plotter parsed **n=169** papers (dual CSV n=170; 1 soft non-numeric cell as in prior passes)
- Institutions n=8 (APHIS VIRPRO excluded); includes new Health Canada B95-a (pre coded 7.5 midpoint of 5–10%)
- Paper post median remains **2.0**; pre median **10.0**
