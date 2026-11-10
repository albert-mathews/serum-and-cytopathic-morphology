# R1 PDF wishlist

**How this file works (for Albert):**
1. Every *corpus row* in `isolation-refs_reparse.csv` should have a local PDF in `refs/isolation_practice/` so all agents can open it directly.
2. **When you fetch items, tell me.** I confirm the filename + first-page title, extract FBS pre/post + quotes, and remove the row(s) from this file.
3. Keep lean: only unfetched rows live here.

**Drop folder:** `r1_isolation_standards_and_practice/refs/isolation_practice/` (gitignored)
**Rule:** verified PMCID/DOI only; suggested filename provided.

**Status:** 128 of 189 rows still lack a local PDF (76 open-access PMC, 52 publisher/DOI).

**De-duplication (one PDF covers multiple rows):**
- **VI254–VI261** → all the *same* Mizuta JJID 2019 paper (DOI 10.7883/yoken.JJID.2018.500); one fetch covers 8 rows.
- **VI262–VI263** → same Mizuta JJID 2008 paper (DOI 10.7883/yoken.JJID.2008.196); one fetch covers 2 rows.
- **VI241 / VI242** → same McSwiggan 1981 paper (DOI 10.1136/bjo.65.8.546), also already have VI240 on disk; one fetch covers both.
So ~128 rows correspond to ~114 distinct PDFs.

---

## Open access (PMC) — one-click fetch

| ID | Year | Virus | PMCID | Drop as |
|----|------|-------|-------|---------|
| VI200 | 1999 | enteroviruses (groundwater concentrates) | PMC91045 | `VI200 - enteroviruses-groundwater-concentrates.pdf` |
| VI201 | 2003 | TGEV | PMC7117453 | `VI201 - TGEV.pdf` |
| VI202 | 1991 | TGEV | PMC7159502 | `VI202 - TGEV.pdf` |
| VI203 | 2002 | HSV (shell vial) | PMC113264 | `VI203 - HSV-shell-vial.pdf` |
| VI204 | 2002 | HSV; HCMV | PMC139995 | `VI204 - HSV-HCMV.pdf` |
| VI205 | 2004 | HSV-1 SC16; HSV-2 G | PMC535897 | `VI205 - HSV-1-SC16-HSV-2-G.pdf` |
| VI206 | 1978 | measles (SSPE vs wild-type) | PMC2185000 | `VI206 - measles-SSPE-vs-wild-type.pdf` |
| VI208 | 1988 | human rhinovirus | PMC7110071 | `VI208 - human-rhinovirus.pdf` |
| VI209 | 1975 | IBR/BHV-1 | PMC275200 | `VI209 - IBR-BHV-1.pdf` |
| VI210 | 1982 | rat coronavirus (sialodacryoadenitis-related) | PMC7086715 | `VI210 - rat-coronavirus-sialodacryoadenitis-related.pdf` |
| VI211 | 1969 | human coronavirus 229E / related coronaviruses | PMC7086760 | `VI211 - human-coronavirus-229E-related-coronaviruses.pdf` |
| VI212 | 1984 | enteroviruses (faecal isolation) | PMC7166571 | `VI212 - enteroviruses-faecal-isolation.pdf` |
| VI214 | 1984 | human respiratory coronavirus | PMC7166702 | `VI214 - human-respiratory-coronavirus.pdf` |
| VI215 | 2004 | ISAV | PMC7172414 | `VI215 - ISAV.pdf` |
| VI216 | 2004 | SARS-CoV 2003VA2774 | PMC3323075 | `VI216 - SARS-CoV-2003VA2774.pdf` |
| VI217 | 2003 | PIV-3; PRCV | PMC7125565 | `VI217 - PIV-3-PRCV.pdf` |
| VI218 | 1998 | enteroviruses; adenoviruses | PMC105078 | `VI218 - enteroviruses-adenoviruses.pdf` |
| VI219 | 2000 | PEDV | PMC7117361 | `VI219 - PEDV.pdf` |
| VI220 | 1989 | JEV; YFV (glycoprotein study) | PMC7125691 | `VI220 - JEV-YFV-glycoprotein-study.pdf` |
| VI221 | 1965 | myxovirus (infectious hepatitis study) | PMC2138105 | `VI221 - myxovirus-infectious-hepatitis-study.pdf` |
| VI222 | 1970 | Chikungunya virus | PMC376692 | `VI222 - Chikungunya-virus.pdf` |
| VI223 | 1983 | rabies (street strain) | PMC264649 | `VI223 - rabies-street-strain.pdf` |
| VI224 | 1989 | FIPV (DF2) | PMC7086852 | `VI224 - FIPV-DF2.pdf` |
| VI230 | 1982 | influenza A/B (clinical NPA isolation) | PMC2536362 | `VI230 - influenza-A-B-clinical-NPA-isolation.pdf` |
| VI231 | 1973 | California encephalitis virus | PMC7111277 | `VI231 - California-encephalitis-virus.pdf` |
| VI232 | 2005 | WNV (3356); flavivirus assays | PMC1069577 | `VI232 - WNV-3356-flavivirus-assays.pdf` |
| VI233 | 1998 | human rhinovirus (clinical) | PMC104983 | `VI233 - human-rhinovirus-clinical.pdf` |
| VI250 | 2020 | Influenza (clinical; vaccine seed isolation) | PMC7040968 | `VI250 - Influenza-clinical-vaccine-seed-isolation.pdf` |
| VI252 | 1991 | human paramyxoviruses (PIV/mumps) primary isolation | PMC7086893 | `VI252 - human-paramyxoviruses-PIV-mumps-primary-isolation.pdf` |
| VI264 | 2015 | SFTSV (tick homogenate isolation) | PMC4593780 | `VI264 - SFTSV-tick-homogenate-isolation.pdf` |
| VI291 | 2024 | Orthohantavirus (genetic variants isolation) | PMC11376573 | `VI291 - Orthohantavirus-genetic-variants-isolation.pdf` |
| VI50 | 2025 | HAdV (human adenovirus) | PMC12265240 | `VI50 - HAdV-human-adenovirus.pdf` |
| VI51 | 2026 | bovine enterovirus | PMC13214444 | `VI51 - bovine-enterovirus.pdf` |
| VI52 | 2026 | herpes B virus (Macacine alphaherpesvirus 1) | PMC13386595 | `VI52 - herpes-B-virus-Macacine-alphaherpesvirus-1.pdf` |
| VI53 | 2026 | BVDV | PMC12784899 | `VI53 - BVDV.pdf` |
| VI54 | 2024 | enteroviruses (wastewater) | PMC11221682 | `VI54 - enteroviruses-wastewater.pdf` |
| VI55 | 2026 | Orthobunyavirus (novel) | PMC12796576 | `VI55 - Orthobunyavirus-novel.pdf` |
| VI56 | 2025 | sarbecoviruses (bat) | PMC12239476 | `VI56 - sarbecoviruses-bat.pdf` |
| VI57 | 2025 | insect-specific flavivirus (lineage I) | PMC12163729 | `VI57 - insect-specific-flavivirus-lineage-I.pdf` |
| VI58 | 2024 | Japanese encephalitis virus (JEV) | PMC11125879 | `VI58 - Japanese-encephalitis-virus-JEV.pdf` |
| VI59 | 2026 | BVDV-1c | PMC13565316 | `VI59 - BVDV-1c.pdf` |
| VI60 | 2025 | PIV5 (parainfluenza virus 5) | PMC12434234 | `VI60 - PIV5-parainfluenza-virus-5.pdf` |
| VI61 | 2024 | bat Jeilongvirus | PMC12017206 | `VI61 - bat-Jeilongvirus.pdf` |
| VI62 | 2025 | human adenovirus | PMC12698310 | `VI62 - human-adenovirus.pdf` |
| VI63 | 2026 | PRRSV-1 and PRRSV-2 | PMC13502029 | `VI63 - PRRSV-1-and-PRRSV-2.pdf` |
| VI64 | 2025 | HAdV-55 | PMC11792584 | `VI64 - HAdV-55.pdf` |
| VI65 | 2026 | mumps virus | PMC12918529 | `VI65 - mumps-virus.pdf` |
| VI66 | 2026 | fowl adenovirus (FAdV) | PMC13517140 | `VI66 - fowl-adenovirus-FAdV.pdf` |
| VI67 | 2026 | bovine enterovirus genotype F | PMC12772302 | `VI67 - bovine-enterovirus-genotype-F.pdf` |
| VI68 | 2025 | camelpox virus | PMC12474500 | `VI68 - camelpox-virus.pdf` |
| VI69 | 2024 | African swine fever virus (ASFV) | PMC11021262 | `VI69 - African-swine-fever-virus-ASFV.pdf` |
| VI70 | 2025 | fowl adenovirus | PMC12195013 | `VI70 - fowl-adenovirus.pdf` |
| VI71 | 2024 | poliovirus (Sabin type 1 D-antigen assays) | PMC11348703 | `VI71 - poliovirus-Sabin-type-1-D-antigen-assays.pdf` |
| VI72 | 2026 | SARS-CoV-2 | PMC12911001 | `VI72 - SARS-CoV-2.pdf` |
| VI73 | 2025 | HSV-1 | PMC12218886 | `VI73 - HSV-1.pdf` |
| VI74 | 2025 | DENV (C6/36 standardization) | PMC13077881 | `VI74 - DENV-C6-36-standardization.pdf` |
| VI75 | 2025 | mosquito-borne alphaviruses (Zambia) | PMC12274731 | `VI75 - mosquito-borne-alphaviruses-Zambia.pdf` |
| VI76 | 2026 | covert mortality nodavirus (CMNV) | PMC13485972 | `VI76 - covert-mortality-nodavirus-CMNV.pdf` |
| VI77 | 2024 | PDCoV (porcine deltacoronavirus) | PMC11646886 | `VI77 - PDCoV-porcine-deltacoronavirus.pdf` |
| VI78 | 2026 | FAdV-4 | PMC13527229 | `VI78 - FAdV-4.pdf` |
| VI79 | 2025 | RSV | PMC13481564 | `VI79 - RSV.pdf` |
| VI80 | 2026 | H3NX avian influenza | PMC13087598 | `VI80 - H3NX-avian-influenza.pdf` |
| VI81 | 2026 | FAdV | PMC13521011 | `VI81 - FAdV.pdf` |
| VI82 | 2025 | nervous necrosis virus (NNV) | PMC12197554 | `VI82 - nervous-necrosis-virus-NNV.pdf` |
| VI83 | 2025 | CPV-2c (canine parvovirus) | PMC13163062 | `VI83 - CPV-2c-canine-parvovirus.pdf` |
| VI84 | 2025 | porcine teschovirus 2 (PTV-2) | PMC12474445 | `VI84 - porcine-teschovirus-2-PTV-2.pdf` |
| VI85 | 2025 | feline astrovirus | PMC12323737 | `VI85 - feline-astrovirus.pdf` |
| VI86 | 2026 | Duck Tembusu virus (DTMUV) | PMC13119985 | `VI86 - Duck-Tembusu-virus-DTMUV.pdf` |
| VI87 | 2025 | novel duck orbivirus | PMC12668858 | `VI87 - novel-duck-orbivirus.pdf` |
| VI88 | 2025 | vaccine-like recombinant virus (cellular tropism study) | PMC12688635 | `VI88 - vaccine-like-recombinant-virus-cellular-tropism-study.pdf` |
| VI89 | 2025 | FHV-1 (MLV strain F2 clinical re-isolation) | PMC11700429 | `VI89 - FHV-1-MLV-strain-F2-clinical-re-isolation.pdf` |
| VI90 | 2025 | HSV-2 (primary clinical isolate) | PMC12298504 | `VI90 - HSV-2-primary-clinical-isolate.pdf` |
| VI91 | 2021 | RSV / measles (secondary infection methods) | PMC8446675 | `VI91 - RSV-measles-secondary-infection-methods.pdf` |
| VI92 | 2026 | DENV (antiviral NDGA study) | PMC13147777 | `VI92 - DENV-antiviral-NDGA-study.pdf` |
| VI93 | 2026 | DENV-2 | PMC12977633 | `VI93 - DENV-2.pdf` |
| VI94 | 2025 | PDCoV-related viruses (house sparrows) | PMC12568082 | `VI94 - PDCoV-related-viruses-house-sparrows.pdf` |

## Publisher / DOI (fetch direct) — 52

| ID | Year | Virus | DOI / link | Drop as |
|----|------|-------|------------|---------|
| VI225 | 1968 | parainfluenza 1-3; SV5 | https://www.jstage.jst.go.jp/article/mandi1957/12/3/12_3_275/_pdf | `VI225 - parainfluenza-1-3-SV5.pdf` |
| VI226 | 1972 | measles SSPE (brain biopsy) | https://archrazi.areeo.ac.ir/article_108816_72ba44a25505a5edcb8bb10bc733b746.pdf | `VI226 - measles-SSPE-brain-biopsy.pdf` |
| VI227 | 2004 | IBDV | https://www.redalyc.org/pdf/1797/179713982009.pdf | `VI227 - IBDV.pdf` |
| VI228 | 1997 | PRRSV (EDRD-1) | https://www.jstage.jst.go.jp/article/jvms/59/1/59_1_31/_pdf | `VI228 - PRRSV-EDRD-1.pdf` |
| VI229 | 1997 | PRRSV (EDRD-1) | https://www.jstage.jst.go.jp/article/jvms/59/4/59_4_281/_pdf | `VI229 - PRRSV-EDRD-1.pdf` |
| VI235 | 2021 | Zika virus (mosquito suspension isolation) | 10.1371/journal.pone.0255314 | `VI235 - Zika-virus-mosquito-suspension-isolation.pdf` |
| VI236 | 2024 | Yellow fever virus (mosquito pool isolation) | https://wwwnc.cdc.gov/eid/article/31/4/24-0108-app1.pdf | `VI236 - Yellow-fever-virus-mosquito-pool-isolation.pdf` |
| VI237 | 2023 | West Nile virus | 10.17504/protocols.io.14egn2e7pg5d/v1 | `VI237 - West-Nile-virus.pdf` |
| VI238 | 2022 | FMDV (clinical suspicion isolation) | https://sitesv2.anses.fr/sites/default/files/221216%20-%20Virus%20Isolation.pdf | `VI238 - FMDV-clinical-suspicion-isolation.pdf` |
| VI241 | 1981 | ophthalmic viruses primary isolation | 10.1136/bjo.65.8.546 | `VI241 - ophthalmic-viruses-primary-isolation.pdf` |
| VI242 | 1981 | ophthalmic viruses primary isolation | 10.1136/bjo.65.8.546 | `VI242 - ophthalmic-viruses-primary-isolation.pdf` |
| VI245 | 2012 | Influenza; hMPV; PIV-4 | https://www.intechopen.com/chapters/40221 | `VI245 - Influenza-hMPV-PIV-4.pdf` |
| VI247 | 2021 | SARS-CoV-2 | 10.1177/20402066211061063 | `VI247 - SARS-CoV-2.pdf` |
| VI248 | 2024 | SARS-CoV-2 | 10.1038/s41598-024-75038-4 | `VI248 - SARS-CoV-2.pdf` |
| VI251 | 2004 | RSV (nasopharyngeal aspirates) | https://www.scielo.br/j/mioc/a/zJh549P7hQB4R98sdj7PqcR/?lang=en | `VI251 - RSV-nasopharyngeal-aspirates.pdf` |
| VI253 | 2007 | hMPV (clinical isolation) | 10.1128/jcm.01251-06 | `VI253 - hMPV-clinical-isolation.pdf` |
| VI254 | 2019 | respiratory viruses (HEF microplate) | 10.7883/yoken.JJID.2018.500 | `VI254 - respiratory-viruses-HEF-microplate.pdf` |
| VI255 | 2019 | respiratory viruses (HEp-2 microplate) | 10.7883/yoken.JJID.2018.500 | `VI255 - respiratory-viruses-HEp-2-microplate.pdf` |
| VI256 | 2019 | influenza / respiratory (MDCK microplate) | 10.7883/yoken.JJID.2018.500 | `VI256 - influenza-respiratory-MDCK-microplate.pdf` |
| VI257 | 2019 | enteroviruses (GMK microplate) | 10.7883/yoken.JJID.2018.500 | `VI257 - enteroviruses-GMK-microplate.pdf` |
| VI258 | 2019 | parechovirus / PeV isolation (no trypsin MM) | 10.7883/yoken.JJID.2018.500 | `VI258 - parechovirus-PeV-isolation-no-trypsin-MM.pdf` |
| VI259 | 2019 | parainfluenza isolation (trypsin MM) | 10.7883/yoken.JJID.2018.500 | `VI259 - parainfluenza-isolation-trypsin-MM.pdf` |
| VI260 | 2019 | EV-D68 / CV-A6 isolation | 10.7883/yoken.JJID.2018.500 | `VI260 - EV-D68-CV-A6-isolation.pdf` |
| VI261 | 2019 | Saffold virus isolation | 10.7883/yoken.JJID.2018.500 | `VI261 - Saffold-virus-isolation.pdf` |
| VI262 | 2008 | respiratory viruses (HEF microplate 2004-2005) | 10.7883/yoken.JJID.2008.196 | `VI262 - respiratory-viruses-HEF-microplate-2004-2005.pdf` |
| VI263 | 2008 | respiratory viruses (RD-18S microplate) | 10.7883/yoken.JJID.2008.196 | `VI263 - respiratory-viruses-RD-18S-microplate.pdf` |
| VI265 | 2022 | PPRV (clinical tissues/swabs) | https://www.thepharmajournal.com/archives/2022/vol11issue12/PartAE/11-12-166-726.pdf | `VI265 - PPRV-clinical-tissues-swabs.pdf` |
| VI268 | 2019 | FMDV (clinical outbreak isolation) | 10.1128/mSphere.00294-19 | `VI268 - FMDV-clinical-outbreak-isolation.pdf` |
| VI269 | 2020 | FMDV (experimental/clinical sample isolation) | 10.3390/pathogens9020129 | `VI269 - FMDV-experimental-clinical-sample-isolation.pdf` |
| VI270 | 1995 | Lymphocystivirus (Iridoviridae) | https://archimer.ifremer.fr/doc/00406/51774/52372.pdf | `VI270 - Lymphocystivirus-Iridoviridae.pdf` |
| VI271 | n.d. | measles (clinical isolation) | https://www.cdc.gov/measles/lab-tools/vero-slam.html | `VI271 - measles-clinical-isolation.pdf` |
| VI272 | 2026 | Ranavirus micropterus1 (McRV) | 10.3389/fvets.2026.1829414 | `VI272 - Ranavirus-micropterus1-McRV.pdf` |
| VI273 | 2026 | Betanodavirus / NNV (gonad diagnostics) | 10.1007/s00248-026-02733-2 | `VI273 - Betanodavirus-NNV-gonad-diagnostics.pdf` |
| VI274 | 2021 | IBDV (LC-75 Vero adaptation) | 10.2147/VMRR.S326479 | `VI274 - IBDV-LC-75-Vero-adaptation.pdf` |
| VI275 | 2025 | PPRV (in vitro isolation from domestic/wild ruminants) | 10.3390/v17091231 | `VI275 - PPRV-in-vitro-isolation-from-domestic-wild-ruminants.pdf` |
| VI276 | 2024 | Mammalian orthoreovirus (bat MRV2) | 10.1128/spectrum.01762-23 | `VI276 - Mammalian-orthoreovirus-bat-MRV2.pdf` |
| VI277 | 2024 | Duck enteritis virus (DEV field outbreak) | 10.1080/01652176.2024.2350668 | `VI277 - Duck-enteritis-virus-DEV-field-outbreak.pdf` |
| VI278 | 2024 | Fowl adenovirus 8a (FAdV-8a) | 10.1016/j.heliyon.2024.e26578 | `VI278 - Fowl-adenovirus-8a-FAdV-8a.pdf` |
| VI279 | 2026 | Getah virus (GETV) from diseased piglets | 10.1080/21505594.2026.2714605 | `VI279 - Getah-virus-GETV-from-diseased-piglets.pdf` |
| VI280 | 2026 | PEDV (intestinal tissue isolation) | 10.1155/tbed/1340053 | `VI280 - PEDV-intestinal-tissue-isolation.pdf` |
| VI281 | 2026 | Hepatitis E virus (retail pork pate) | 10.3390/v18070760 | `VI281 - Hepatitis-E-virus-retail-pork-pate.pdf` |
| VI282 | 2016 | Ebola virus outbreak variants (Mayinga/Kikwit/Makona) | 10.1038/srep38293 | `VI282 - Ebola-virus-outbreak-variants-Mayinga-Kikwit-Makona.pdf` |
| VI283 | 2024 | PRRSV-2 (Marc-145 culture after inoculation) | 10.3389/fvets.2024.1439015 | `VI283 - PRRSV-2-Marc-145-culture-after-inoculation.pdf` |
| VI284 | 2025 | Negevirus (mosquito isolation) | 10.1186/s12985-025-02961-x | `VI284 - Negevirus-mosquito-isolation.pdf` |
| VI285 | 2026 | SARS-CoV-2 (feline primary isolation) | 10.3390/vetsci13040374 | `VI285 - SARS-CoV-2-feline-primary-isolation.pdf` |
| VI286 | 2025 | Feline parvovirus (FPV) from anal swab | 10.3389/fmicb.2025.1658838 | `VI286 - Feline-parvovirus-FPV-from-anal-swab.pdf` |
| VI287 | 2022 | SARS-CoV-2 (clinical swab isolation Alpha) | 10.1172/jci.insight.155944 | `VI287 - SARS-CoV-2-clinical-swab-isolation-Alpha.pdf` |
| VI288 | 2020 | Cyprinid herpesvirus-2 (CyHV-2) | 10.7717/peerj.9373 | `VI288 - Cyprinid-herpesvirus-2-CyHV-2.pdf` |
| VI289 | 2026 | Japanese encephalitis virus (JEV) culture | 10.3390/v18080850 | `VI289 - Japanese-encephalitis-virus-JEV-culture.pdf` |
| VI290 | 2024 | Influenza A (tissue homogenate MDCK isolation) | 10.1080/22221751.2024.2387449 | `VI290 - Influenza-A-tissue-homogenate-MDCK-isolation.pdf` |
| VI292 | 2023 | SARS-CoV-2 (clinical isolates; Caco-2/HuH-6 systems) | 10.1016/j.isci.2023.106634 | `VI292 - SARS-CoV-2-clinical-isolates-Caco-2-HuH-6-systems.pdf` |
| VI293 | 2024 | Rabies virus (Vero-adapted Flury HEP) | 10.1038/s41598-024-63337-9 | `VI293 - Rabies-virus-Vero-adapted-Flury-HEP.pdf` |
