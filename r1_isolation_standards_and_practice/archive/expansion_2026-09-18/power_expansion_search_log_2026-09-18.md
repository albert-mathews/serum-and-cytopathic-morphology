# Power expansion search log — 2026-09-18

**Timezone note:** file written ~2026-09-18 20:01 UTC (~20:01 UTC; user zone America/Toronto UTC-4).

## Baseline
- Expanded n before: 142; Dual n before: **123**
- Max VI before: VI246
- Dedup keys built from 9 CSVs: **646**

## Strategies run
### A — Author / collaborator threads
- Mined surnames from dual/expanded notes (Abbaszadegan, Athmanathan, Hirano, Numazaki, Hsiung, Mizuta/Abiko/Yamagata, Hierholzer, Chen, Fukai, …).
- Highest yield: **Mizuta Yamagata PIPH** microplate SOP tables (2008 + 2019) + Abiko hMPV 2007.
- Hierholzer NCI-H292 paramyxovirus isolation (1991).
- NIID/Matsuyama SARS-CoV-2 isolation lineage (SciRep 2024).
- Hsiung thread led mainly to serum-contaminant detection (excluded as not clinical isolation).

### B — Citation / methods chaining
- CLSI M41 sample (already in institution; no new % beyond known 10→1–3%).
- CDC measles Vero/hSLAM lab tool (new institution + practice).
- CIRAD/NEADL PPR already present — Gujarat PPRV practice paper added separately.
- Shell-vial PMC105078 already in corpus (2→3 increase) — skipped.
- WOAH/ANSES FMDV serum-free already present; FLI 1→1 and Japan LFPK 10→10 added as practice equal-holds.

### C — Non-English / regional
- French: IFREMER Lymphocystivirus 10%→2% SVF (hit).
- Portuguese/English Brazil SciELO RSV 10→2 (hit).
- Japanese: Yamagata JJID tables + MNT-1 HPIV + SFTSV Nagasaki (hits).
- Chinese (EN OA): BVDV Hebei PMC; BPIV3 yak (single-stage only).
- Russian: HRSV JIDC 10→2 (hit); patents often lacked clean dual FBS for clinical isolation.
- German keyword search: mostly general FKS encyclopedic; FLI English paper used instead.
- Spanish: fewer explicit dual-% isolation hits in this pass (oocyte/serum QC noise).

### D — Virus-family gaps
- Paramyxovirus/hMPV/HPIV/PIV: Hierholzer, Abiko, MNT-1, Yamagata LLC-MK2.
- Pestivirus BVDV: Hebei clinical.
- FMDV equal-holds: Japan 10→10, FLI 1→1.
- Orthomyxo non-classic: exhibition swine + OptiPRO SF 10→0.
- Iridovirus aquatic: IFREMER.
- SFTSV bunyavirus: Nagasaki ticks.
- ASFV field MA104 / soil Ba71V: propagation/adaptation borderline — not upserted as dual practice.

## Outcomes
- Candidates written: **29** → `power_expansion_candidates_2026-09-18.csv`
- Upserted dual practice rows: **25** (VI247–VI271)
- Dual n before: **123** → after: **148** (Δ = **+25**)
- Expanded n before: **142** → after: **167**
- Skipped (dedup): BVDV Hebei PMC12784899 (already VI53)
- Institution adds: CDC Measles Lab Tools — Vero/hSLAM (10%→2%)
- Plots regenerated into `fbs_distribution_plots/` (plotter parsed n=147 papers; 1 soft cell failed numeric parse)

## New dual pairs
- VI247: 10->2.5 | SARS-CoV-2 | Vero E6
- VI248: 10->2 | SARS-CoV-2 | VeroE6/TMPRSS2; Vero E6-TMPRSS2-T2A-ACE2
- VI249: 10->0 | Influenza A (exhibition swine) | MDCK (SFM-adapted)
- VI250: 10->0 | Influenza (clinical; vaccine seed isolation) | MDCK-A; LLC-MK2D; MDCK-S
- VI251: 10->2 | RSV (nasopharyngeal aspirates) | HEp-2
- VI252: 10->2 | human paramyxoviruses (PIV/mumps) primary isolation | NCI-H292
- VI253: 10->0 | hMPV (clinical isolation) | Vero E6
- VI254: 15->2 | respiratory viruses (HEF microplate) | HEF
- VI255: 2->2 | respiratory viruses (HEp-2 microplate) | HEp-2
- VI256: 8->0 | influenza / respiratory (MDCK microplate) | MDCK
- VI257: 10->2 | enteroviruses (GMK microplate) | GMK
- VI258: 10->2 | parechovirus / PeV isolation (no trypsin MM) | LLC-MK2-N
- VI259: 10->0 | parainfluenza isolation (trypsin MM) | LLC-MK2-N
- VI260: 10->5 | EV-D68 / CV-A6 isolation | RD-A
- VI261: 10->2 | Saffold virus isolation | RD-18S-N
- VI262: 10->2 | respiratory viruses (HEF microplate 2004-2005) | HEF
- VI263: 8->2 | respiratory viruses (RD-18S microplate) | RD-18S
- VI264: 10->2 | SFTSV (tick homogenate isolation) | Vero E6
- VI265: 10->2 | PPRV (clinical tissues/swabs) | Vero
- VI266: 10->2 | HRSV (clinical PCR-positive) | HeLa; HEp-2; Vero
- VI267: 10->0 | HPIV-1 and HPIV-3 (clinical) | MNT-1
- VI268: 10->10 | FMDV (clinical outbreak isolation) | LFPK-alphav-beta6
- VI269: 1->1 | FMDV (experimental/clinical sample isolation) | BHK-21 (FLI CCLV-RIE 164)
- VI270: 10->2 | Lymphocystivirus (Iridoviridae) | BF2
- VI271: 10->2 | measles (clinical isolation) | Vero/hSLAM

## Author threads followed
- CDC / WHO measles isolation
- China veterinary paramyxovirus
- China veterinary pestivirus
- FLI / FMDV national labs
- FMDV national labs
- French / IFREMER aquatic
- Hierholzer / CDC paramyxovirus
- Japan NIID/university arbovirus
- Japan paramyxovirus
- Latin America / Fiocruz
- Mizuta Yamagata
- NIID / Matsuyama lineage
- PPRV veterinary isolation
- Russian clinical RSV
- SARS clinical protocols
- SARS reviews
- adenovirus clinical
- influenza serum-free

## Languages yielding hits
- en
- en/de
- en/ja
- en/ru
- en/zh
- fr
- pt/en

## Saturation assessment
Classic **10→2** remains abundant; this pass deliberately prioritized equal-holds (HEp-2 2→2, FMDV 10→10, FLI 1→1), increases/non-classic decreases (RD-A 10→5, HEF 15→2, SARS 10→2.5), and serum-free post (0) influenza/paramyxovirus protocols. Further English PubMed 10→2 mining would add volume but little distributional diversity; highest remaining yield is likely more national SOP PDFs (Pirbright, NIID Japanese SOPs, SENASA, China CDC) when serum % is explicit, plus citation-chaining from Yamagata/Numazaki microplate descendants. Honest estimate: literature is **partially saturated** for classic pairs; non-classic/equal-hold/serum-free still expandable. Dual gain this pass: **+25** (target >=20 MET).
