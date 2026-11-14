# P2 PDF catalogue and wishlist

**Single source of truth** for P2 literature holdings: what is on disk, what was used (bibliography), and what is still needed. Replaces `P2_pdf_request.md` (Tier A-C request list) and `P2_pdf_wishlist.md` (lean buy list), both folded in here on 2026-10-14.

**Drop folder:** `p2_virus_EV_indistinguishable_refs/refs/` (gitignored; never commit PDFs). Naming: `P2-0xx_firstauthor_year_slug.pdf`. Verified DOI only; no Sci-Hub.  
**Screen table:** `P2_screened.csv` (all screened IDs, useful Y/B/N, fulltext status). **Quotes:** `P2_quotes.md`.  
**Last checked against disk:** 2026-10-14 (Round 5 additions logged 2026-11-14).

## Counts

| Measure | n |
|---|--:|
| Screened IDs (`P2_screened.csv`) | 94 |
| Distinct P2 IDs with a PDF on disk | 32 (P2-0xx: 24; seed reviews P2-200-207: 8) |
| Used (quoted in `P2_quotes.md`) = bibliography below | 31 |
| On disk, P2-0xx, not yet quoted | 3 (P2-017, P2-020, P2-021) |
| Round 5 sources read OA online, PDF not yet dropped to `refs/` | 8 (P2-082, 083, 084, 086, 088, 089, 090, 091) |
| Previously requested PDFs still missing | 0 (resolved) |

## Please fetch

Every former Tier A–C item is on disk, including the corrected Chen et al. 2015 *Cell* (P2-044, `10.1016/j.cell.2015.01.032`; title verified on disk, prior misfile resolved). Round 5 (2026-11-14) opened a new fetch queue below — OA items are listed so the research rests on the fetched PDF (per `agent-settings/research-strategy.md`), and the paywalled primaries need the owner. Drop into `p2_virus_EV_indistinguishable_refs/refs/`.

| ID | Title · year | Author | Identifier | Drop as | Priority |
|----|--------------|--------|------------|---------|----------|
| P2-083 | Structure and development of viruses … VII. Incomplete influenza virus · 1962 | Morgan C, Hsu KC, Rose HM | `10.1084/jem.116.4.553` (PMC2137626) | `P2-083_morgan_1962_incomplete_influenza.pdf` | high (OA) |
| P2-086 | Proteins specified by herpes simplex virus. V … herpesvirion · 1972 | Spear PG, Roizman B | `10.1128/jvi.9.1.143-159.1972` (PMC356272) | `P2-086_spear_1972_hsv_purification.pdf` | high (OA) |
| P2-084 | Systemically circulating viral and tumor-derived microRNAs in KSHV-associated malignancies · 2013 | Chugh PE et al. | `10.1371/journal.ppat.1003484` | `P2-084_chugh_2013_kshv_exosomes.pdf` | high (OA) |
| P2-089 | Rotaviruses associate with distinct types of extracellular vesicles · 2020 | Iša P et al. | `10.3390/v12070763` (PMC7411906) | `P2-089_isa_2020_rotavirus_ev.pdf` | high (OA) |
| P2-090 | Investigation of extracellular vesicles from SARS-CoV-2 infected specimens: a safety perspective · 2021 | Nunez Lopez YO et al. | `10.3389/fimmu.2021.617042` | `P2-090_nunezlopez_2021_sarscov2_safety.pdf` | high (OA) |
| P2-088 | Comprehensive characterization of extracellular HSV-1 virions · 2008 | Loret S, Guay G, Lippé R | `10.1128/JVI.00904-08` (PMC2519676) | `P2-088_loret_2008_hsv1_virions.pdf` | high (OA) |
| P2-091 | Extracellular vesicles in viral infections: two sides of the same coin? · 2020 | Martins ST, Alves LR | `10.3389/fcimb.2020.593170` (PMC7736630) | `P2-091_martins_2020_two_sides.pdf` | medium (OA) |
| P2-082 | Influenza virus nucleic acid … · 1956 | Ada GL, Perry BT | `10.1099/00221287-14-3-623` (PMID 13346022) | `P2-082_adaperry_1956_influenza_nucleic_acid.pdf` | medium |
| P2-081 | Incomplete forms of influenza virus · 1954 | von Magnus P | `10.1016/S0065-3527(08)60529-1` | `P2-081_vonmagnus_1954_incomplete_influenza.pdf` | medium (paywalled) |
| P2-085 | Steric exclusion chromatography … influenza A virus … · 2017 | Marichal-Gallardo P et al. | pii `S0021967316317423` (DOI not seen) | `P2-085_marichalgallardo_2017_sxc_influenza.pdf` | medium (paywalled) |
| P2-087 | Purification of herpes simplex virus · 1973 | Gentry GA, Randall CC (verify) | `10.1099/0022-1317-22-2-297` (PMID 4362407) | `P2-087_gentryrandall_1973_hsv_purification.pdf` | medium (paywalled) |
| P2-092 | Nonlytic egress and transmission in the virus world · 2025 | Altan-Bonnet N | `10.1146/annurev-biochem-052521-120140` | `P2-092_altanbonnet_2025_nonlytic_egress.pdf` | low (paywalled) |
| P2-093 | Interactions between extracellular vesicles and viruses · 2026 | Defourny K et al. | `10.1093/femsre/fuag028` | `P2-093_defourny_2026_ev_virus.pdf` | low (paywalled) |

Optional (only if P2 is reopened further): abstract-only useful rows in `P2_screened.csv` (P2-024, 028, 031, 043, 051, 052) and the Santiana et al. 2018 lead logged in `P2_search_log.md`.

## Bibliography: used in P2 (quoted)

| ID | Citation | DOI | On disk |
|---|---|---|---|
| P2-001 | Nolte-'t Hoen E et al. 2016. Extracellular vesicles and viruses: Are they close relatives?. *PNAS. 2016;113(33):9155-9161* | `10.1073/pnas.1605146113` | yes, as seed review P2-203 |
| P2-009 | Gould SJ et al. 2003. The Trojan exosome hypothesis. *PNAS. 2003;100(19):10592-10597* | `10.1073/pnas.1831413100` | yes |
| P2-010 | Bess JW Jr et al. 1997. Microvesicles are a source of contaminating cellular proteins found in purified HIV-1 preparations. *Virology. 1997;230(1):134-144* | `10.1006/viro.1997.8499` | yes |
| P2-011 | Gluschankof P et al. 1997. Cell membrane vesicles are a major contaminant of gradient-enriched human immunodeficiency virus type-1 preparations. *Virology. 1997;230(1):125-133* | `10.1006/viro.1997.8453` | yes |
| P2-013 | Cantin R et al. 2008. Discrimination between exosomes and HIV-1: Purification of both vesicles from cell-free supernatants. *J Immunol Methods. 2008;338:21-30* | `10.1016/j.jim.2008.07.007` | yes |
| P2-014 | Coren LV et al. 2008. CD45 immunoaffinity depletion of vesicles from Jurkat T cells demonstrates that exosomes contain CD45: no evidence for a distinct exosome/HIV-1 budding pathway. *Retrovirology. 2008;5:64* | `10.1186/1742-4690-5-64` | yes |
| P2-015 | Ott DE et al. 2009. Purification of HIV-1 virions by subtilisin digestion or CD45 immunoaffinity depletion for biochemical studies. *Methods Mol Biol. 2009;485:15-25* | `10.1007/978-1-59745-170-3_2` | yes |
| P2-016 | Feng Z et al. 2013. A pathogenic picornavirus acquires an envelope by hijacking cellular membranes. *Nature. 2013;496:367-371* | `10.1038/nature12029` | yes |
| P2-018 | Bukong TN et al. 2014. Exosomes from hepatitis C infected patients transmit HCV infection and contain replication competent viral RNA in complex with Ago2-miR122-HSP90. *PLoS Pathog. 2014* | `10.1371/journal.ppat.1004424` | yes |
| P2-019 | Théry C et al. 2018. Minimal information for studies of extracellular vesicles 2018 (MISEV2018). *J Extracell Vesicles. 2018;7(1):1535750* | `10.1080/20013078.2018.1535750` | yes |
| P2-019b | Welsh JA et al. (ISEV consortium) et al. 2024. Minimal information for studies of extracellular vesicles (MISEV2023): From basic to advanced approaches. *J Extracell Vesicles. 2024;13:e12404* | `10.1002/jev2.12404` | yes |
| P2-044 | Chen YH et al. 2015. Phosphatidylserine vesicles enable efficient en bloc transmission of enteroviruses. *Cell. 2015* | `10.1016/j.cell.2015.01.032` | yes |
| P2-061 | Trubey CM et al. 2001. Quantitation of HLA class II protein incorporated into HIV-1 virions purified by anti-CD45 immunoaffinity depletion of microvesicles. *J Virol. 2003* | `10.1128/jvi.77.23.12699-12709.2003` | yes |
| P2-071 | Tang VA et al. 2017. Single-particle discrimination of retroviruses from extracellular vesicles by nanoscale flow cytometry. *Sci Rep. 2017;7:17769* | `10.1038/s41598-017-18227-8` | yes |
| P2-072 | Vaillancourt M et al. 2021. Velocity gradient separation reveals a new extracellular vesicle population enriched in miR-155 and mitochondrial DNA. *Pathogens. 2021;10(5):526* | `10.3390/pathogens10050526` | yes |
| P2-073 | Perez PS et al. 2019. Extracellular vesicles and chronic inflammation during HIV infection. *J Extracell Vesicles. 2019;8(1):1687275* | `10.1080/20013078.2019.1687275` | yes |
| P2-074 | Park IW et al. 2010. HIV-1 is budded from CD4+ T lymphocytes independently of exosomes. *Virol J. 2010;7:234* | `10.1186/1743-422X-7-234` | yes |
| P2-075 | Heilingloh CS et al. 2017. Role of L-particles during herpes simplex virus infection. *Front Microbiol. 2017;8:2565* | `10.3389/fmicb.2017.02565` | yes |
| P2-076 | Esser MT et al. 2001. Differential incorporation of CD45 CD80 CD86 and MHC into HIV-1 virions and microvesicles. *J Virol. 2001;75(13):6173-6182* | `10.1128/jvi.75.13.6173-6182.2001` | yes |
| P2-077 | Konadu KA et al. 2016. Isolation of exosomes from the plasma of HIV-1 positive individuals. *J Vis Exp. 2016;(107):e53495* | `10.3791/53495` | yes |
| P2-078 | Szilagyi JF et al. 1991. Identification and characterization of a novel non-infectious herpes simplex virus-related particle. *J Gen Virol. 1991;72:661-668* | `10.1099/0022-1317-72-3-661` | yes |
| P2-079 | Welsh JA et al. (ISEV) et al. 2024. MISEV2023: An updated guide to EV research and applications (editorial companion). *J Extracell Vesicles. 2024;13:e12416* | `10.1002/jev2.12416` | no (quoted from OA full text) |
| P2-080 | Reiter K et al. et al. 2018. Separation of virus-like particles and extracellular vesicles by flow-through and heparin affinity chromatography. *J Chromatogr A. 2019;1588:77-* | `10.1016/j.chroma.2018.12.035` | yes |
| P2-082 | Ada GL, Perry BT. 1956. Influenza virus nucleic acid: relationship between biological characteristics of the virus particle and properties of the nucleic acid. *J Gen Microbiol. 1956;14(3):623-633* | `10.1099/00221287-14-3-623` | not yet (OA online) |
| P2-083 | Morgan C, Hsu KC, Rose HM. 1962. Structure and development of viruses … VII. Incomplete influenza virus. *J Exp Med. 1962;116(4):553-564* | `10.1084/jem.116.4.553` | not yet (OA PMC) |
| P2-084 | Chugh PE et al. 2013. Systemically circulating viral and tumor-derived microRNAs in KSHV-associated malignancies. *PLoS Pathog. 2013;9(7):e1003484* | `10.1371/journal.ppat.1003484` | not yet (OA) |
| P2-086 | Spear PG, Roizman B. 1972. Proteins specified by herpes simplex virus. V … herpesvirion. *J Virol. 1972;9(1):143-159* | `10.1128/jvi.9.1.143-159.1972` | not yet (OA PMC) |
| P2-088 | Loret S, Guay G, Lippé R. 2008. Comprehensive characterization of extracellular herpes simplex virus type 1 virions. *J Virol. 2008;82(17):8605-8618* | `10.1128/JVI.00904-08` | not yet (OA PMC) |
| P2-089 | Iša P et al. 2020. Rotaviruses associate with distinct types of extracellular vesicles. *Viruses. 2020;12(7):763* | `10.3390/v12070763` | not yet (OA PMC) |
| P2-090 | Nunez Lopez YO, Casu A, Pratley RE. 2021. Investigation of extracellular vesicles from SARS-CoV-2 infected specimens: a safety perspective. *Front Immunol. 2021;12:617042* | `10.3389/fimmu.2021.617042` | not yet (OA) |
| P2-091 | Martins ST, Alves LR. 2020. Extracellular vesicles in viral infections: two sides of the same coin? *Front Cell Infect Microbiol. 2020;10:593170* | `10.3389/fcimb.2020.593170` | not yet (OA PMC) |

## Held but not yet quoted

| ID | Citation | DOI | Note |
|---|---|---|---|
| P2-017 | Ramakrishnaiah V et al. 2013. Exosome-mediated transmission of hepatitis C virus between human hepatoma Huh7.5 cells. *PNAS. 2013 (approx)* | `` | Tier C cargo/biogenesis background; quote pass pending if cited |
| P2-020 | Pegtel DM et al. 2010. Functional delivery of viral miRNAs via exosomes. *PNAS. 2010* | `10.1073/pnas.0914843107` | Tier C cargo/biogenesis background; quote pass pending if cited |
| P2-021 | Booth AM et al. 2006. Exosomes and HIV Gag bud from endosome-like domains of the T cell plasma membrane. *J Cell Biol. 2006;172(6):923-935* | `10.1083/jcb.200508014` | Tier C cargo/biogenesis background; quote pass pending if cited |

## Seed reviews on disk (P2-200-207)

The seed set originally logged as P2-001-P2-008 is held under P2-200-P2-207 (file names carry the review titles). P2-001 (Nolte-’t Hoen et al. 2016) is quoted.

- `P2-200 - Extracellular Vesicles and Viruses- Two Intertwined Entities.pdf`
- `P2-201 - Microvesicles and Viral Infection - meckes-raab-traub-2011.pdf`
- `P2-202 - Modern Techniques for the Isolation of Extracellular Vesicles and Viruses - nihms-1539689.pdf`
- `P2-203 - nolte-t-hoen-et-al-2016-extracellular-vesicles-and-viruses-are-they-close-relatives.pdf`
- `P2-204 - Purification Methods and the Presence of RNA in Virus Particles and Extracellular Vesicles.pdf`
- `P2-205 - Shedding light on the cell biology of extracellular vesicles - vanniel2018.pdf`
- `P2-206 - The Role of Extracellular Vesicles as Allies of HIV, HCV and SARS Viruses.pdf`
- `P2-207 - Viral effects on the content and function of extracellular vesicles - raab-traub2017.pdf`

## DOI corrections (kept from the former wishlist)

- P2-010 Bess et al. 1997 = `10.1006/viro.1997.8499`
- P2-011 Gluschankof et al. 1997 = `10.1006/viro.1997.8453`
- P2-013 Cantin et al. 2008 = `10.1016/j.jim.2008.07.007`
- P2-044 Chen et al. 2015 = `10.1016/j.cell.2015.01.032` (not `.09.032`)

## Disk housekeeping

- 2026-10-14: the second P2-010 copy (long title file name; same paper, same 11 pages, extracted text identical apart from one character, likely a download stamp) was deleted locally; `P2-010_bess_1997_microvesicles_HIV.pdf` is kept. Distinct P2 IDs on disk unchanged (32).
