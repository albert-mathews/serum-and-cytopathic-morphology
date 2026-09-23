# P3 Step 1 — Path-type map (documentary coding)

**Date:** 2026-09-21 (pass **21N**)  
**Scope:** Closed O/C events only for counts and the virus×path table; open events listed separately.  
**Tone:** Exploration / census documentation — **not** scientific endorsement that “isolate = virus.” Path labels are documentary coding of how papers describe sample production linked to deposited sequences.

---

## 1. Path-type definitions (plain prose)

| Code | Plain definition |
|------|------------------|
| `culture_cpe` | Sequenced material comes from cell-culture production, and at least one paper in the resolved record uses CPE, plaques, syncytia, foci, or clear cytopathic selection as part of isolate assertion or stock production for that material. |
| `culture_no_cpe` | Sequenced material comes from a culture-propagated stock or culture-derived nucleic acid, but CPE/plaques/syncytia are **not** used as the warrant in the resolved record. Do not inflate from silence or from tangential CPE mentions. |
| `clinical_direct` | Clinical (or tumor) specimen sequenced without an intervening culture-isolate path for the sequenced material (e.g. BALF → NGS; stool extract → cloning). |
| `other` | Eggs, animals-only, recombinant/synthetic clone or reverse-genetics confirmation without a fresh culture-production claim for the sequenced molecule, or other non-culture / non-clinical-direct paths — reason noted in event notes. |
| `unclear` | Reserved; open chains stay `chain_open` rather than forced into a path. |

Soft evidentiary bar: documentary **method ↔ deposit** link within reasonable scientific doubt — **not** forensic custody of aliquots.

---

## 2. Overall counts among `chain_closed`

| Metric | n |
|--------|---|
| Events (O+C) | **102** |
| `chain_closed` | **101** (99%) |
| `chain_open` | **1** (1%) |

### path_score among closed

| path_score | n closed | % of closed |
|------------|----------|-------------|
| `culture_cpe` | **36** | 36% |
| `culture_no_cpe` | **45** | 45% |
| `clinical_direct` | **11** | 11% |
| `other` | **9** | 9% |

| Culture-propagated (`culture_cpe` + `culture_no_cpe`) | **81** / 101 closed (**80%**) |
| `culture_cpe` alone | **36** / 101 closed (**36%**) |

---

## 3. Virus / family × path_score table (every closed event_id)

Grouped by **family**, then **virus**. Each cell lists closed `event_id`s under that path.

| Family | Virus | culture_cpe | culture_no_cpe | clinical_direct | other |
|--------|-------|-------------|----------------|-----------------|-------|
| AAV | adeno-associated virus 2 | — | AAV-O1 | — | — |
| adenovirus | human adenovirus 2 | ADE-O1, ADE-O2 | — | — | — |
| adenovirus | human adenovirus 5 | — | ADE-C1 | — | — |
| astrovirus | human astrovirus | ASTRO-O1 | — | — | — |
| BK_polyomavirus | BK polyomavirus | — | BK-O1, BK-O2 | — | — |
| bluetongue | bluetongue virus | BTV-C1, BTV-C2, BTV-O1 | — | — | — |
| bocavirus | human bocavirus | — | — | BOCA-O1 | — |
| BVDV | bovine viral diarrhea virus | BVDV-C1, BVDV-C2, BVDV-O1 | — | — | — |
| canine_distemper | canine distemper virus | CDV-C1, CDV-C3 | CDV-C2, CDV-O1 | — | — |
| chikungunya | chikungunya virus | — | CHIK-O1 | — | — |
| classical_swine_fever | classical swine fever virus | — | CSFV-C1 | — | — |
| classical_swine_fever | classical swine fever virus (hog cholera) | — | CSFV-O1 | — | — |
| CMV | human cytomegalovirus | — | CMV-C1, CMV-C2, CMV-C3, CMV-O1 | — | — |
| coronavirus | HCoV-OC43 | — | COV-C2, COV-O3 | — | — |
| coronavirus | human coronavirus 229E | — | COV-C4, COV-O7 | — | — |
| coronavirus | human coronavirus HKU1 | — | — | COV-O4 | — |
| coronavirus | human coronavirus NL63 | COV-O5 | — | — | — |
| coronavirus | MERS-CoV (HCoV-EMC/2012) | COV-O6 | — | — | — |
| coronavirus | SARS-CoV | COV-O2 | COV-C1, COV-O1 | — | — |
| coronavirus | SARS-CoV-2 | COV-C5 | — | COV-O8 | — |
| coxsackievirus_B3 | coxsackievirus B3 | — | COX-O1 | — | — |
| dengue | dengue virus type 2 | DEN-O1 | — | — | — |
| Ebola | Zaire ebolavirus | EBO-O1 | — | — | — |
| EBV | Epstein-Barr virus | — | EBV-O1 | — | — |
| enterovirus_71 | enterovirus 71 | EV71-C1, EV71-O1 | — | — | — |
| enterovirus_71 | enterovirus A71 | EV71-C2 | — | — | — |
| feline_calicivirus | feline calicivirus | — | FCV-O1 | — | — |
| FMDV | foot-and-mouth disease virus | FMDV-C1, FMDV-O1 | — | — | — |
| hantavirus | Hantaan virus | — | HANTA-O1 | — | — |
| HBV | hepatitis B virus | — | — | HBV-O1 | — |
| Hendra | Hendra virus (equine morbillivirus) | HEND-O1 | — | — | — |
| hepatitis_A | hepatitis A virus | — | HAV-C1, HAV-O1 | — | HAV-O2 |
| hepatitis_C | hepatitis C virus | — | — | — | HCV-O1 |
| hepatitis_E | hepatitis E virus | — | — | — | HEV-O1 |
| HHV-6 | human herpesvirus 6 | — | HHV6-O1 | — | — |
| HPIV-1 | human parainfluenza virus type 1 | — | HPIV1-O1 | — | — |
| HPIV-3 | human parainfluenza virus type 3 | — | HPIV3-O1 | — | — |
| HPV | human papillomavirus type 16 | — | — | HPV-O1 | — |
| HSV | herpes simplex virus type 1 | — | HSV-O1 | — | — |
| influenza_A | influenza A virus | — | — | — | FLU-O1 |
| influenza_B | influenza B virus | — | — | — | FLU-B-O1 |
| JC_virus | JC polyomavirus | JC-O1 | — | — | — |
| LCMV | lymphocytic choriomeningitis virus | — | LCMV-O1 | — | — |
| Marburg | Marburg virus | — | — | — | MARB-O1 |
| MCPyV | Merkel cell polyomavirus | — | — | MCPYV-O1 | — |
| measles | measles virus | MEA-C1, MEA-O1 | — | — | MEA-C2 |
| mumps | mumps virus | MUM-O1 | — | — | — |
| NDV | Newcastle disease virus | NDV-O1 | — | — | — |
| Nipah | Nipah virus | NIPAH-C1, NIPAH-O1 | — | — | — |
| norovirus | Norwalk virus | — | — | NOR-O1 | — |
| parvovirus_B19 | human parvovirus B19 | — | — | B19-O1 | — |
| poliovirus | poliovirus type 1 | — | POL-C1, POL-O1, POL-O3, POL-O4 | — | — |
| rabies | rabies virus | — | RAB-O1 | — | — |
| reovirus | reovirus type 3 | — | REO-O1 | — | — |
| rhinovirus | human rhinovirus 14 | — | RHV-O1 | — | — |
| rotavirus | simian rotavirus SA11 | — | ROTA-O1 | — | — |
| RSV | human respiratory syncytial virus | RSV-C1 | RSV-O1 | — | — |
| rubella | rubella virus | RUB-O1 | — | — | — |
| sapovirus | sapovirus (Sapporo virus) | — | — | SAPO-C1, SAPO-O1 | — |
| Semliki_Forest | Semliki Forest virus | — | SFV-O1 | — | — |
| Sindbis | Sindbis virus | SIN-O1 | — | — | — |
| sv40 | simian virus 40 | — | SV40-O1 | — | — |
| vaccinia | vaccinia virus | — | VAC-O1 | — | — |
| VSV | vesicular stomatitis Indiana virus | VSV-C1 | VSV-O1 | — | — |
| VZV | varicella-zoster virus | — | VZV-O1 | — | — |
| West_Nile | West Nile virus | WNV-C1, WNV-O1 | — | — | — |
| yellow_fever | yellow fever virus | — | — | — | YFV-O1 |
| Zika | Zika virus | — | ZIKV-C2 | ZIKV-C1 | ZIKV-O1 |

---

## 4. Still open

| event_id | virus / strain | Why still open |
|----------|----------------|----------------|
| LASSA-O1 | Lassa virus / Josiah S segment | 21M: PDF have/title-verified; Methods give only "viral RNA templates" without production path — remain chain_open (do not invent culture). |

---

## 5. Pass 21N closes (summary warrants)

| event_id | path_score | 1–2 sentence Methods warrant |
|----------|------------|------------------------------|
| COV-O7 | culture_no_cpe | Thiel 2001 JGV: parental HCoV 229E propagated in MRC-5; poly(A)+ RNA → cDNA library/RT-PCR → full-length insert cloned in vaccinia (vHCoV-inf-1); AF304460 is the sequenced cDNA insert. Inf-1 rescue CPE/plaques and Hamre 1966 isolation CPE kept as P/validation context — not inflated. |
| HSV-O1 | culture_no_cpe | McGeoch 1988 JGV: UL (completing strain 17 genome) sequenced from plasmid-cloned restriction fragments of HSV-1 strain 17 DNA; limited virion DNA for oriL. No CPE warrant in Methods (parallel to VZV-O1). |
| CHIK-O1 | culture_no_cpe | Khan 2002 JGV: S27 African prototype inoculated into C6/36 mosquito cells; infected culture fluid harvested/concentrated; RNA from stored virus → complete genome. No CPE/plaque language in Methods. |
| CMV-O1 | culture_no_cpe | Fleckenstein 1982 Gene: Ad169 propagated in HEL or foreskin fibroblasts; virion DNA from culture fluids → cosmid pHC79 library. Chee 1990 cites those overlapping cosmids (with Oram/Bankier) for the AD169 sequence era. No CPE warrant in Fleckenstein Methods. |

---

## 6. Note on labels

These path_score labels are **documentary codes** for how the census papers describe production of material that was sequenced and deposited. They are **not** endorsements that culture isolates equal viruses, nor forensic proofs of aliquot custody. Soft bar only.

