# P3 stock-origin hops (2026-09-21 / 2026-09-22, pass **21R**)

**Purpose:** For priority O-events (esp. `culture_no_cpe` / thin stocks), hop from the sequenced stock name to the isolation/production paper and record the **origin warrant class**. Immediate `path_score` stays documentary for sequenced material (see `P3_warrant_and_process_codes_2026-09-21.md`).

**Status codes:** `hop_closed_cpe` | `hop_closed_animal` | `hop_closed_other` | `hop_open_need_pdf` | `hop_dead_end`

**Soft bar:** documentary method↔stock link within reasonable doubt — not forensic custody. OA/Unpaywall/EuropePMC/local only — no Sci-Hub.

---

## Summary (this pass)

| Status | n (priority + expanded table) |
|--------|-------------------------------|
| `hop_closed_cpe` | **14** (incl. HPIV3←Chanock 1958 **hemadsorption**; Type 1 first-passage no definite CPE) |
| `hop_closed_animal` | **1** (CHIK←Ross; Buckley also co-warrants animal at Lassa *species* level) |
| `hop_closed_other` | **4** (EBV transformation; POL←Enders 1949 no CPE; **HAV←Provost 1979 no CPE**; **RAB←Kissling 1958 HKTC no CPE**) |
| `hop_open_need_pdf` | **1** (VAC Copenhagen lymph history) |
| `hop_dead_end` | **0** |
| **Total priority+expanded rows** | **20** |

**Hypothesis signal:** Closed culture-stock hops still often land on **culture detection** warrants (CPE / hemadsorption / plaque). A growing minority are **culture without CPE** (`hop_closed_other`: Enders POL; Provost HAV; Kissling RAB) or animal (CHIK) / transformation (EBV). Open row = VAC lymph-history cite lock — not a counterexample.

**21R deltas vs 21Q:** Closed HPIV3←Chanock 1958 NEJM hemadsorption (Type 1 HA; JS lineage gap vs Wash/47885/57); HAV←Provost 1979 PSEBM CR326 TC **without CPE** (LA≠CR326; Najarian cites Provost procedures); RAB←Kissling 1958 PSEBM fixed+street hamster-kidney TC **without CPE** (mouse LD50; Pasteur PV≠CVS). Enders 1952 optional SKIP (Albert could not acquire). Immediate path_scores unchanged.

---

## Priority hop table

| Event | Stock | Immediate path_score | Cited / target origin paper | DOI / PMID | Origin warrant | Status | PDF drop name | Notes |
|-------|-------|----------------------|-----------------------------|------------|----------------|--------|---------------|-------|
| CMV-O1 | Ad169 | culture_no_cpe (Fleckenstein) | Rowe et al. 1956 PSEBM — cytopathogenic agent from adenoid cultures (Ad.169) | **DOI `10.3181/00379727-92-22497`** · PMID 13350367 | **culture_cpe** (focal fibroblast CPE; CF antigen) | **hop_closed_cpe** | `CMV-O1_rowe_1956_psebm.pdf` **HAVE** | Quote in 21O section. Oram/Spector CPE harvest companions HAVE. |
| HSV-O1 | strain 17 | culture_no_cpe | Brown, Ritchie & Subak-Sharpe 1973 JGV — Glasgow ts genetics on strain 17 | DOI `10.1099/0022-1317-18-3-329` · PMID 4348796 | **culture_cpe** (patient isolate; plaque×3; BHK CPE harvest; plaque assay) | **hop_closed_cpe** | `HSV-P_brown_strain17_1973_jgv.pdf` **HAVE** | Quote in 21Q section. Direct Glasgow strain 17 documentary link. |
| CHIK-O1 | S27 African prototype | culture_no_cpe | Ross 1956 J Hyg — Newala epidemic; **S27** named in isolation table | DOI `10.1017/s0022172400044442` · PMC2218030 | **animal_disease** (baby-mouse lethal; Seitz-filterable brain passage; characteristic tremor/death) | **hop_closed_animal** | `CHIK-P_ross_1956_jhyg.pdf` **HAVE** (EPMC/Cambridge OA) | Khan 2002 cites Ross 1956 for S27. Immediate path still C6/36 RNA / no CPE. |
| POL-O1 / O3 / O4 | Mahoney | culture_no_cpe | Enders, Weller & Robbins 1949 Science — Lansing in human embryonic tissue culture | DOI `10.1126/science.109.2822.85` | tissue-culture multiplication + **mouse LD50/paralysis** assay; **no CPE** in 1949 Science; strain = **Lansing** (≠Mahoney) | **hop_closed_other** | `POL-P_enders_1949_science.pdf` **HAVE** | Soft bar closes Enders tissue-culture origin class; Mahoney≠Lansing lineage gap recorded. 1952 J Immunol optional for CPE morphology. |
| COV-O7 | 229E Inf-1 / VR-740 | culture_no_cpe | Hamre & Procknow 1966 PSEBM | DOI `10.3181/00379727-121-30734` | **culture_cpe** | **hop_closed_cpe** | `COV-229E_P_hamre_1966_psebm.pdf` **HAVE** | |
| VAC-O1 | Copenhagen | culture_no_cpe | Goebel 1990 plaque-cloned Copenhagen; deeper vaccine-lymph history unopened | Deposit DOI `10.1016/0042-6822(90)90294-2` | plaque-clone = culture_cpe-class at deposit purity; animal/lymph origin open | hop_open_need_pdf | `VAC-P_copenhagen_history_<author>_<year>.pdf` (lock cite first) | Borderline. |
| VZV-O1 | Dumas | culture_no_cpe | Weller 1953 PSEBM serial propagation of varicella-zoster agents | DOI `10.3181/00379727-83-20354` | **culture_cpe** (focal cytopathogenic lesions + intranuclear inclusions) | **hop_closed_cpe** | `VZV-P_weller_1953_psebm.pdf` **HAVE** | Quote in 21Q. **Dumas** not named in Weller 1953 (species/lineage soft-bar close). |
| EBV-O1 | B95-8 | culture_no_cpe | Miller & Lipman 1973 PNAS — infectious EBV from transformed marmoset leukocytes | DOI `10.1073/pnas.70.1.190` · PMC433213 | producer lymphoblastoid line / **transformation** (not classical monolayer CPE) | **hop_closed_other** | `EBV-P_miller_lipman_1973_pnas.pdf` **HAVE** (EPMC OA) | B95-8 established after exposure to extract of 883L; infectivity = transforming units. |
| SV40-O1 | strain 776 | culture_no_cpe | Sweet & Hilleman 1960 PSEBM — vacuolating virus SV40 | DOI `10.3181/00379727-105-26128` | **culture_cpe** (prominent cytoplasmic vacuolation / cytopathic change in grivet kidney; harvest ≥50% CPE) | **hop_closed_cpe** | `SV40-P_sweet_hilleman_1960_psebm.pdf` **HAVE** (SAGE OA) | Strain **776** explicit in Sweet & Hilleman. |
| ADE-O1 / O2 | Ad2 | culture_cpe (immediate) | Gingeras plaque-purified Ad2 (HAVE); Rowe 1953 adenoid cytopathogenic agent | Rowe DOI `10.3181/00379727-84-20714` · PMID 13134217 | **culture_cpe** | **hop_closed_cpe** | Gingeras HAVE; `ADE-P_rowe_1953_psebm.pdf` **HAVE** (SAGE OA) | Rowe: “adenoid degeneration agent” / cytopathogenic effects. |
| RSV-O1 | A2 | culture_no_cpe | Chanock et al. 1957 Am J Hyg — chimpanzee-coryza–related agent (Long/Snyder) | DOI `10.1093/oxfordjournals.aje.a119901` | **culture_cpe** (syncytial CPE in KB/liver/amnion) | **hop_closed_cpe** | `RSV-P_chanock_1957_ajhyg.pdf` **HAVE** | Quote in 21Q. Isolates = **Long/Snyder**; **A2** not named (species soft-bar; A2 lineage gap noted). |
| MEA-O1 | Edmonston | culture_cpe | Enders & Peebles 1954 PSEBM | local PDF HAVE | **culture_cpe** | **hop_closed_cpe** | `MEA_enders_peebles_1954.pdf` **HAVE** | |
| MUM-O1 | Jeryl Lynn | culture_cpe | Buynak/Hilleman JL vaccine / plaque tradition | related DOI `10.1001/jama.1968.03140010016003` | culture_cpe | **hop_closed_cpe** | Deposit HAVE | |
| RUB-O1 | Therien | culture_cpe | Hemphill 1988 plaque-purified Therien | PMID 3336944 | **culture_cpe** | **hop_closed_cpe** | `RUB-P_hemphill_1988.pdf` **HAVE** | |
| LASSA-O1 | Josiah | **culture_cpe** (21P; was unclear) | **Immediate Methods:** Auperin 1986 Josiah GPC; **species isolation:** Buckley & Casals 1970 | Auperin 1986 `10.1016/0042-6822(86)90438-1`; Buckley `10.4269/ajtmh.1970.19.680` | **Josiah stock:** culture_cpe (plaque×3 Vero E6). **Species:** culture_cpe + animal (Buckley Vero CPE + mouse illness). | **hop_closed_cpe** (Josiah via Auperin 1986; species via Buckley) | all three LASSA PDFs **HAVE** | **Josiah gap:** Buckley isolates = Nigeria 1969 (L.P. etc.); Josiah = Sierra Leone **1976** human serum (Auperin 1986). Soft bar closes Josiah on Auperin’s own isolation+plaque statement — does **not** require Buckley lineage. Clegg 1985 = **GA391 Nigerian**, not Josiah. |

### Additional high-visibility `culture_no_cpe` O rows

| Event | Stock | Target origin | DOI | Origin warrant | Status | PDF drop name | Notes |
|-------|-------|---------------|-----|----------------|--------|---------------|-------|
| SFV-O1 | SFV | Clegg & Kennedy 1974 — 3× plaque-purified wild-type SFV (Waiters/Burke/Skehel stock) | local PDF (JGV 1974) | **culture_cpe** (plaque×3) | **hop_closed_cpe** | local Clegg PDF **HAVE** | Takkinen 1986 uses purified 42S virion RNA; Clegg Methods: “Three times plaque-purified wild-type ts+ Semliki Forest virus”. Deeper Smithburn/Findlay animal isolation optional. |
| HPIV3-O1 | JS | Chanock et al. 1958 NEJM — Type 1 hemadsorption virus (MK TC) | **DOI `10.1056/nejm195801302580502`** | **hemadsorption** (MK; Type 1 first-passage no definite CPE; later separation/elongation) | **hop_closed_cpe** | `HPIV3-P_chanock_1958_nejm.pdf` **HAVE** | Quote in 21R. **JS** not named; Stokes JS vs Wash/47885/57 prototype — lineage gap. |
| RAB-O1 | Pasteur PV | Kissling 1958 PSEBM — fixed CVS + street in hamster kidney TC | **DOI `10.3181/00379727-98-23997`** | tissue-culture serial passage **without CPE**; infectivity = **mouse LD50** (+ Negri street) | **hop_closed_other** | `RAB-P_kissling_1958_psebm.pdf` **HAVE** | Quote in 21R. Pasteur **PV≠** Kissling CVS/Alabama street — fixed-virus TC class close. |
| HAV-O1 | LA | Provost & Hilleman 1979 PSEBM — CR326 in marmoset liver + FRhK6 | **DOI `10.3181/00379727-160-40422`** | culture **without CPE** (IF/IA/RIA + marmoset); Najarian LA cites Provost procedures | **hop_closed_other** | `HAV-P_provost_1979_psebm.pdf` **HAVE** | Quote in 21R. **LA≠CR326** (≠HM-175) lineage gap; method paper for LA culture path. |
| BK-O1 | MM | Gardner 1971 Lancet BK isolation | **DOI `10.1016/s0140-6736(71)91776-4`** · PMID **4104714** | **culture_cpe** (MK CPE day 18; Vero CPE; urine intranuclear inclusions + EM) | **hop_closed_cpe** | `BK-P_gardner_1971_lancet.pdf` **HAVE** | Quote in 21Q. **B.K.** patient isolate; **MM** = Takemoto tumor/urine strain (Yang) — lineage gap noted under soft bar. |

---

## 21Q origin warrants (quotes)

### Brown 1973 — HSV-1 Glasgow strain 17 (plaque / CPE)

From `HSV-P_brown_strain17_1973_jgv.pdf` METHODS:

> “Herpes simplex virus type I (**GLASGOW strain 17**) isolated from a patient and having a non-syncytial (syn+) plaque morphology, was purified by **three successive single plaque passages** and the stock then prepared constitutes the wild-type parent strain 17 syn+.”

> Growth: BHK21(C13) monolayers infected “…incubated at 31 °C for 3 days or until a **confluent cytopathic effect** was observed.” Assay: “**plaques** were counted after fixing with formol saline and staining with Giemsa.”

**Warrant class:** `culture_cpe`. Immediate HSV-O1 path_score stays `culture_no_cpe` (McGeoch plasmid/virion DNA Methods).

### Chanock 1957 — RSV / CCA-related Long & Snyder (syncytial CPE)

From `RSV-P_chanock_1957_ajhyg.pdf`:

> “The most striking effect of Long virus in tissue culture was the formation of **syncytial areas**…. Cytopathogenic changes were first seen as small circumscribed syncytial areas… Usually, within 1 to 4 days the entire cell sheet was involved.”

> Summary: agents “characterized by the occurrence of a **syncytial cytopathogenic effect** in KB or human liver tissue culture.”

**Warrant class:** `culture_cpe` at RSV isolation/species level. Isolates named **Long** and **Snyder** (related to CCA). Sequenced stock **A2** is not named in Chanock 1957 — soft-bar species close with A2 lineage gap (parallel to LASSA Josiah≠Buckley). Immediate RSV-O1 stays `culture_no_cpe` (Stec HEp-2).

### Weller 1953 — VZV vesicle-fluid agents (focal CPE + inclusions)

From `VZV-P_weller_1953_psebm.pdf` Summary:

> “The inoculation of roller tube tissue cultures of human tissues with vesicle fluid derived from patients with varicella has resulted in the isolation of **six cytopathogenic agents**…. Histologically the lesions… consist of **focal** accumulations of cells which become swollen, and then degenerate: characteristically, such cells contain **intranuclear inclusion bodies**.”

**Warrant class:** `culture_cpe` (+ inclusion morphology). **Dumas** not in Weller 1953 — soft-bar species/lineage close for VZV culture tradition. Immediate VZV-O1 stays `culture_no_cpe` (Davison clones).

### Enders 1949 — Lansing poliovirus tissue culture (no CPE; mouse assay)

From `POL-P_enders_1949_science.pdf`:

> Primary inoculum: “0.1 cc of a suspension of **mouse brain infected with the Lansing strain** of poliomyelitis virus.” Identity verified by disease in white mice + neutralization; fluids produce paralysis/death in mice and characteristic cord lesions in monkeys. Multiplication calculated via **mouse LD50** across subcultures in human embryonic tissues.

**Warrant class:** `hop_closed_other` — tissue-culture multiplication **without** monolayer CPE in this 1949 paper; infectivity/identity = **animal** (mouse/monkey paralysis). Strain = **Lansing**, not Mahoney — lineage gap noted. Immediate POL-O* path_scores stay `culture_no_cpe`.

### Gardner 1971 — B.K. papovavirus from urine (CPE)

From `BK-P_gardner_1971_lancet.pdf`:

> “A **cytopathic effect** was first observed in **M.K.** cells 18 days after the cultures were inoculated with urine…. Following urine inoculation, cytopathic changes were slow in developing in **Vero** cell cultures… scattered granular round cells on the surface of the monolayer (fig. 2).”

> Urine cytology: membranes “packed with **inclusion-bearing** epithelial cells” (basophilic intranuclear inclusions); EM papova particles ~43.6 nm.

**Warrant class:** `culture_cpe` (MK/Vero) + inclusions/EM companions. Soft bar closes BK species origin on Gardner **B.K.** isolate. Sequenced **MM** (Yang/Takemoto tumor+urine) ≠ Gardner patient B.K. — lineage gap noted. Immediate BK-O1 stays `culture_no_cpe` (Yang).

---


## 21R origin warrants (quotes)

### Chanock 1958 — HPIV3 / Type 1 hemadsorption virus (hemadsorption; late mild CPE)

From `HPIV3-P_chanock_1958_nejm.pdf` (OCR; NEJM image PDF):

> Isolation: monkey-kidney cultures inoculated with throat-swab fluid; after incubation, guinea-pig erythrocytes added and cultures “examined microscopically for adsorption of red cells to the monkey-kidney monolayer. If adsorption (hereafter called **hemadsorption**) occurred, the tissue-culture fluid was passed…”

> Effects in tissue culture: “**Type 1 virus did not produce definite cytopathogenic changes during the first passage** in monkey-kidney tissue culture and thus could only be recognized by the **hemadsorption** technic. After passage… it produced an effect on cells that was characterized by their **separation from the cell sheet, followed by an elongation** of such cells.”

> Summary: “Two new myxoviruses were isolated from children with respiratory illness by means of the **hemadsorption technic** and monkey-kidney tissue culture. **Type 1 hemadsorption virus** was recovered from 35 children…”

**Warrant class:** culture **hemadsorption** (bucketed `hop_closed_cpe` as monolayer culture detection). First-passage Type 1 = **no definite CPE**; later mild CPE morphology. Sequenced stock **JS** (Stokes infant; vs Wash/47885/57 prototype) **not named** in Chanock 1958 — soft-bar species/Type 1 HA close with JS lineage gap. Immediate HPIV3-O1 stays `culture_no_cpe` (Stokes LLC-MK2).

### Provost & Hilleman 1979 — HAV CR326 cell culture (no CPE)

From `HAV-P_provost_1979_psebm.pdf`:

> “We have now been able to propagate the **CR326** strain in liver explant cell cultures of *S. labiatus* marmoset and in a fetal rhesus kidney normal cell line.”

> Liver explants: “**No cytopathic changes** were seen…” FRhK6: “…but **there was no evident cytopathic effect**.” Discussion: “Hepatitis A virus has, unfortunately, proved **noncytopathic** in these cell cultures to date.”

> Summary: “Human hepatitis A virus was **reliably and repeatedly propagated** in primary explant cell cultures of marmoset livers and in the normal fetal rhesus kidney cell line (FRhK6)…. The virus propagated to greatest extent in FRhK6 cells. **No cytopathology was observed.**” Identity by IF / blockade / neutralization / IA / RIA / IEM / marmoset inoculation.

**Warrant class:** `hop_closed_other` — serial cell-culture propagation **without CPE**; antigen/IF + animal identity. Najarian 1985 LA Methods cite Provost procedures (ref 12) for establishing LA stool isolate in TC — soft-bar **method** close. Sequenced **LA ≠ CR326** (and ≠ HM-175) — lineage gap noted. Immediate HAV-O1 stays `culture_no_cpe`.

### Kissling 1958 — rabies fixed + street in hamster kidney TC (no CPE; mouse assay)

From `RAB-P_kissling_1958_psebm.pdf`:

> Fixed (CVS) virus in hamster kidney: nutrient fluid harvested over 91 days — “**No cytopathic changes** occurred during this period.” Serial HK passage through ≥15 passages (Table I) “without any diminution in titer”; “**No cytopathic changes** could be observed in cell cultures infected with fixed rabies virus at any passage level.” Identity by mouse neutralization.

> Street virus (dog salivary gland): serial HK passage ≥4× (Table IV); “**Negri bodies** could be demonstrated in impression smears from the brains of mice inoculated with tissue culture fluids at each passage level. **No cytopathic changes** were observed in the tissue cultures.”

> Summary: “Both **fixed and street** rabies virus strains were propagated serially in hamster kidney tissue cultures but **no cytopathic changes** were evident in these cultures.”

**Warrant class:** `hop_closed_other` — non-nervous tissue-culture hop **without CPE**; infectivity/identity = **animal** (mouse LD50 / Negri). Soft bar closes fixed-virus **TC class** for Pasteur PV genealogy; **PV ≠** Kissling CVS / Alabama street — lineage gap. Immediate RAB-O1 stays `culture_no_cpe` (Tordo virion RNA).

---
## LASSA warrants (21P quotes)

### Auperin 1986 — Josiah sequenced-material + stock-origin (plaque)

From `LASSA-O1_auperin_1986_virology.pdf` Materials and Methods:

> “The **Josiah strain** of Lassa virus (reference no. **800593**) was isolated from human serum taken in **Sierra Leone in 1976**. The virus was **plaque purified three times** on monolayers of **Vero E6** cells … and a high titer stock prepared by passage in **BHK-21** cells.”

> Grown on BHK-21 (m.o.i. = 0.1); virus harvested from culture media, ultracentrifuged/purified; **RNA from purified virus** used for cDNA.

**Auperin 1989** (deposit): cDNA from “viral RNA templates”; cites Auperin 1986 as ref 7. Soft bar: same lab/strain + prior Methods paper → **immediate path closed** `culture_cpe` / `chain_closed`.

**Clegg & Oram 1985:** strain **GA391** (Nigerian), plaque-purified ×5 in Vero, grown CV-1/L929 — **not Josiah**. Useful parallel Nigerian path only.

### Buckley & Casals 1970 — species isolation (not Josiah)

From `LASSA-P_buckley_casals_1970_ajtmh.pdf`:

> Fourteen isolates recovered in **Vero** cell cultures from Nigerian patients (1969). **Cytopathic effects (CPE)** / plaques in Vero; cytopathology section documents CPE appearance and destruction of monolayers.

> Animal: mouse inoculations; virus isolated from urine of infected mice as late as day 83; newborn-mouse passage with illness/death.

**Warrant class:** `culture_cpe` **and** `animal_disease` at **species** level. **Not** a Josiah-specific documentary link (Josiah = 1976 Sierra Leone per Auperin 1986).

---

## CHIK Ross 1956 origin warrant (quote)

From `CHIK-P_ross_1956_jhyg.pdf` (S27 in Table; “Evidence that the agents were viruses”):

> Each strain “was an agent **lethal for baby mice**, could pass through a Seitz filter, and could be passaged apparently indefinitely in dilute **brain suspensions** with the regular production of characteristic symptoms… often on the second day… animals died in a typical attitude.”

> Antiserum against the **S27** strain neutralized ~10,000 LD50 of related Chikungunya strains. Strain table lists **S27** from serum of Athumani, Liteho.

**Warrant class at origin:** `animal_disease` (mouse-lethal brain-passage isolation). No monolayer CPE in Ross 1956.

**Immediate CHIK-O1 path_score:** remains `culture_no_cpe` (Khan C6/36 RNA Methods).

---

## SV40 Sweet & Hilleman 1960 (quote)

From `SV40-P_sweet_hilleman_1960_psebm.pdf`:

> Called the “**vacuolating virus**” because of prominent cytoplasmic vacuolation accompanying cytopathic change in **grivet / Cercopithecus** kidney cultures. Propagation: harvest “when at least **50% of the cell sheet showed cytopathic change** typical of that of the vacuolating agent.” Strain **776** used in cytopathic-effect titration tables/figures.

**Warrant class:** `culture_cpe`. Immediate SV40-O1 path_score stays `culture_no_cpe` (Fiers Methods thin).

---

## Rowe Ad169 origin warrant (quote) — retained from 21O

From Rowe et al. 1956 (`CMV-O1_rowe_1956_psebm.pdf`): cytopathogenic agent; Ad.169 from 7-year-old girl; focal fibroblast CPE. Immediate CMV-O1 remains `culture_no_cpe` (Fleckenstein).

---

## Suggested PDF drops still needed (stock-origin layer)

| Priority | Drop as | DOI |
|----------|---------|-----|
| 1 | `VAC-P_copenhagen_history_<lock>.pdf` | lock cite first (only remaining open hop) |
| optional | `SFV-P_smithburn_findlay_<year>.pdf` | deeper than plaque stock |
| skip | `POL-P_enders_weller_robbins_1952_jimmunol.pdf` | optional CPE companion — **SKIP** (Albert could not acquire) |
| skip | Classical Pasteur 1885 rabies animal history | superseded for soft bar by Kissling 1958 HKTC **HAVE** |
| skip | HPIV3/HAV/RAB origin PDFs above | **HAVE** after 21R |

---

## Pass log

- **21O:** Created hop ledger; closed CMV←Rowe, COV-229E←Hamre, MEA←Enders, ADE←Gingeras/Rowe-class, RUB←Hemphill, MUM←plaque JL; EBV←Miller as other; left HSV/CHIK/POL/VAC/VZV/SV40/RSV/LASSA open.
- **21P:** Read Auperin 1986 + Clegg 1985 + Buckley 1970; closed LASSA-O1 immediate path (`culture_cpe`/`chain_closed`) + Josiah stock-origin CPE; Buckley species CPE+animal with Josiah lineage gap noted. Downloaded/closed CHIK←Ross (animal), SV40←Sweet (CPE), SFV←Clegg plaque; ADE Rowe + EBV Miller PDFs HAVE. Wishlist lean = remaining open hops only.
- **21Q:** MSI PDFs CopyToBox'd. Closed HSV←Brown CPE; RSV←Chanock syncytial CPE (A2 lineage note); VZV←Weller CPE+inclusions (Dumas lineage note); POL←Enders 1949 `hop_closed_other` (Lansing; no CPE; mouse assay; Mahoney gap); BK←Gardner CPE (MM lineage note). BK DOI fixed to `10.1016/s0140-6736(71)91776-4`. Immediate path_scores not thrashed.
- **21R:** MSI PDFs on box. Closed HPIV3←Chanock 1958 hemadsorption (JS lineage gap); HAV←Provost 1979 CR326 TC no CPE (LA≠CR326; Najarian cites procedures); RAB←Kissling 1958 fixed+street HKTC no CPE (PV≠CVS). Enders 1952 SKIP. Wishlist Please fetch = None; three → HAVE. Immediate path_scores not thrashed.
