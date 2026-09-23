# Control cultures scoring — justification notes

**Framework:** `control-cultures.md` v0.1  
**Results table:** `control-cultures-overview.csv`  
**Corpus:** 28 PDFs in `wrk/isolation_practice/`  
**Scorer:** grok-primary  
**Date:** 2026-07-20  

Quotes are taken from text extraction (`wrk/isolation_practice/_txt/`) or, for image-only **VI43**, from rendered PDF pages. Line breaks in PDFs may differ; search distinctive phrases.

**Decision tree recap:** D = no culture NC → C = NC wrong stage or explicit mismatch → A = Isolation-stage NC + M1–M6 matched → else B = Isolation-stage NC under-specified.

---

## Summary counts (primary tier) — post agent remediation

| Tier | n | IDs |
|------|---|-----|
| **A** | 4 | VI16, VI33, VI38, VI43 |
| **B** | 6 | VI8, VI13, VI14, VI36, VI40, VI42 |
| **C** | 1 | VI25 |
| **D** | 17 | VI2, VI4, VI15, VI18, VI23, VI24, VI28, VI29, VI30, VI32, VI34, VI39, VI41, VI45, VI46, VI47, SPT10 |

**Total: 28.**

**Remediation log (from agent1–3 reviews):**
1. **VI25** A→**C** (`C-stage`): TCID50/toxicity NCs are wrong-stage for primary Isolation plates (agent2).
2. **VI40** A→**B**: mock medium not stated; 2% FBS/MEM language applies to infected arm only (agent3).
3. **VI8** justification: corrected Isolation medium quotes (agent1 notes fix; tier remains B).
4. **VI29/VI47**: same article content; both retained as separate corpus IDs (both D).

---

## VI2 — Tier **D**

**Primary experiment:** Isolation of bat SL-CoV (WIV1) on Vero E6 from PCR-positive samples.  
**Endpoint:** CPE.

### NC search
No mock-infected, uninfected, or culture negative-control wells in Isolation methods.

### Quotes — Isolation medium (test only)
> "Virus isolation. Vero E6 cell monolayers were maintained in DMEM supplemented with 10% FCS. PCR-positive samples (in 200 ml buffer) were gradient centrifuged at 3,000–12,000g, and supernatant were diluted 1:10 in DMEM before being added to Vero E6 cells. After incubation at 37uC for 1 h, inocula were removed and replaced with fresh DMEM with 2% FCS. Cells were incubated at 37uC for 3 days and checked daily for cytopathic effect."

### Quotes — non-culture “negative controls” (do not count as culture NC)
> "Serum from a healthy blood donor was used as a negative control in each experiment."  
*(neutralization assay, not Isolation culture)*

> "HeLa cells without ACE2 expression and Vero E6 cells were used as negative and positive controls, respectively."  
*(receptor/entry assay)*

### Decision
`nc_any=no` for Isolation/infection culture morphology → **D**.

---

## VI4 — Tier **D**

**Primary experiment:** Isolation of HFRS agent from rat lung on Vero E6.  
**Endpoint:** IFA antigen (authors state no CPE).

### Quotes — no CPE; no culture NC
> "There was no visible cytopathic effect (CPE) in the antigen-positive cultures."

> "The infected cells in the subculture were suspended by trypsin treatment, washed, and mixed with an equal number of fresh normal cells in the fresh growth medium."

*"Fresh normal cells" = co-culture for passage, not a parallel negative control for morphology/antigen.*

### Quotes — media
> "cultured in a growth medium of minimum essential medium (MEM), Eagle, with 5-10% fetal calf serum (FCS) or a maintenance medium of MEM with 1-2% FCS."

### Decision
No mock/uninfected NC → **D**.

---

## VI8 — Tier **B** (ambiguous; not A)

**Primary experiment:** Isolation of 2019-nCoV from BALF on Vero E6/Huh7; CPE/IF characterization.  
**Endpoint:** Cytopathogenic effect / IF.

### Quotes — Isolation medium (primary Isolation; corrected after agent1)
> "The following cell lines were used for virus isolation in this study: Vero E6 and Huh7 cells, which were cultured in DMEM containing 10% FBS."

> "…filtered and diluted 1:2 with DMEM supplemented with 16 μg ml−1 trypsin before it was added to the cells. After incubation at 37 °C for 1 h, the inoculum was removed and replaced with fresh culture medium containing antibiotics (see below) and 16 μg ml−1 trypsin. The cells were incubated at 37 °C and observed daily for cytopathogenic effects."

> "Clear cytopathogenic effects were observed in cells after incubation for three days (Extended Data Fig. 6a, b)."

**Note:** A separate methods sentence (“Cells were incubated with DMEM supplemented with 2% FBS for 3 days…”) appears in the neutralization/infection context in the full text; it must **not** be attributed as the Isolation maintenance formula without that linkage. Isolation post-inoculum medium is “fresh culture medium … and trypsin” as quoted above.

### Quotes — mock (results/figures; methods under-specified)
> "a, b, Vero E6 cells are shown at 24 h after infection with mock virus (a) or 2019-nCoV (b). c, d, Mock-virus-infected (c) or 2019-nCoV-infected (d) samples were stained with rabbit serum raised against recombinant SARSr-CoV Rp3 N protein..."

> "mock-transfected cells were used as controls."  
*(ACE2 transfection experiment — wrong stage for Isolation CPE)*

### Decision
Isolation-stage **mock virus** appears in Extended Data for CPE/IF, so `nc_isolation_stage=yes`, but methods do **not** define mock preparation or matched post-inoculum medium for Isolation → M2/M3 **unknown** → **B**.  
`ambiguous=yes`.

---

## VI13 — Tier **B** (ambiguous; not A)

**Primary experiment:** Isolation of SARS-CoV-2 from NP/OP swabs, limiting dilution, Vero CCL-81.  
**Endpoint:** CPE.

### Quotes — methods (no explicit mock preparation)
> "For isolation, limiting dilution, and passage 1 of the virus, we pipetted 50 µL of serum-free DMEM into columns 2–12 of a 96-well tissue culture plate, then pipetted 100 µL of clinical specimens into column 1 and serially diluted 2-fold across the plate. We then trypsinized and resuspended Vero cells in DMEM containing 10% fetal bovine serum, 2 × penicillin/streptomycin, 2× antibiotics/antimycotics, and 2× amphotericin B at a concentration of 2.5 × 105 cells/mL. We added 100 µL of cell suspension directly to the clinical specimen dilutions and mixed gently by pipetting. We then grew the inoculated cultures ... and observed for cytopathic effects (CPEs) daily."

### Quotes — results/figure mock
> "CPE was not observed in mock infected cells (Figure 1, panel A)."

> "Phase-contrast microscopy of Vero cell monolayers at 3 days postinoculation: A) Mock, B) nasopharyngeal specimen, C) oropharyngeal specimen."

### Decision
Mock is **named** and used for CPE comparison → Isolation-stage NC present. Methods never define how mock was prepared or that it shared the 10% FBS cell-resuspension / incubation regime → M2/M3 **unknown** → **B**.  
Not A: forbidden to invent mock wells from serial-dilution description alone.

---

## VI14 — Tier **B**

**Primary experiment:** Isolation of HRSV from nasopharyngeal aspirates on Hep-2.  
**Endpoint:** CPE (then IFA).

### Quotes — Isolation medium (inoculated cultures)
> "The nasopharyngeal aspirates were treated with penicillin (100 units/mL) and streptomycin (100 µg/mL) before being inoculated to Hep-2 cells (ATCC) cultured in Dulbecco’s modified Eagle’s medium (DMEM; GIBCO, CA) supplemented with 2 % fetal bovine serum (FBS; GIBCO). The cytopathic effect (CPE) of inoculated Hep-2 cells was observed everyday for seven days."

### Quotes — mock
> "CPE positive and uninfected (mock) Hep-2 cells were digested by 0.02 % EDTA, spotted to eight well glass slide..."

> "Fig. 1 – Cytopathic effect and indirect immunofluoresence test of HRSV isolates on Hep-2 cells. A, Mock Hep-2 cell; B, Isolate GZA17-01 infected Hep-2 cells; C, Indirect immunofluoresence test of mock Hep-2 cell; D, ..."

### Decision
Mock is Isolation-related (CPE figure + IFA). Serum/medium for **mock** cultures is not stated separately (only inoculated cultures’ 2% FBS) → M3 **unknown** → **B**.

---

## VI15 — Tier **D**

**Primary experiment:** DENV Isolation from whole blood on C6/36, three blind passages.  
**Endpoint:** Plaque titer (CPE not used as Isolation endpoint).

### Quotes — Isolation
> "Blood samples were diluted 1:10 in minimal essential media (MEM) containing 2% fetal bovine serum (FBS) (Gibco) and added onto cultured monolayer of C6/36 cells for 1 hour... After 1 hour, the inoculum was removed and cells were cultured for 7 days in MEM with 2% FBS and antibiotics."

### Decision
No mock/uninfected/control cultures in Isolation or growth kinetics → **D**.

---

## VI16 — Tier **A**

**Primary experiment:** Shell-vial Isolation of HSV-1 from corneal scrapings on HCE and Vero; non-viral keratitis scrapings as controls.  
**Endpoint:** CPE / IF confirmation.

### Quotes — controls (Isolation-stage)
> "Scrapings obtained from 10 patients with infectious keratitis of non-viral origin were included as controls. All the scrapings were simultaneously inoculated into shell vials of HCE and Vero cells."

> "None of the controls yielded HSV-1."

### Quotes — matched maintenance medium (applies to inoculated vials including controls)
> "The supernatant was discarded and 1 ml of maintenance medium (SHEM Supplemented with 1% FBS for HCE and MEM with 1% FBS for Vero cells) was added. The vials were incubated for 24 hours at 36°C."

### Quotes — CPE endpoint
> "routine examination of the cell cultures were done the next day (12–16 h) following the day of specimen inoculation, for any evidence of CPE"

### Match (M1–M6)
Same cell systems, same adsorption, same 1% FBS maintenance, parallel timeline; difference is clinical material type (HSK vs non-viral keratitis) → treated as no-virus-source clinical matrix control under framework edge case → **A**, `match_basis=explicit`.

### Note
Figure legends also show “Uninfected cells” as IF counterstain — those are **assay** uninfected cells, not the Isolation controls; Isolation tier rests on non-viral scrapings.

---

## VI18 — Tier **D**

**Primary experiment:** Serial passage adaptation of influenza on Vero.  
**Endpoint:** Plaque / growth (not CPE Isolation).

### Quotes — infection medium
> "The Vero cell culture medium was changed to DMEM containing 0.2% bovine serum albumin (BSA) with 1 µg/ml TPCK-trypsin, and the Vero cells were inoculated with the PR8 virus..."

### Decision
No mock/uninfected culture NC → **D**.

---

## VI23 — Tier **D**

**Primary experiment:** SARS-CoV-2 Isolation from hospitalized patients on Vero lines.  
**Endpoint:** CPE.

### Quotes — Isolation / CPE
> "We observed the cells daily and harvested when 40%–50% demonstrated cytopathic effect"

> "After 1 hour incubation at 37°C, we added 1 mL of 2% FBS DMEM."

### Decision
No mock/uninfected culture NC in methods → **D**.

---

## VI24 — Tier **D**

**Primary experiment:** Influenza Isolation from clinical specimens on Vero ± AmB.  
**Endpoint:** CPE / HA.

### Quotes — CPE as presence
> "fected or noninfected by determining the presence or absence of a cytopathic effect"

### Quotes — “control” language that is **not** culture NC
> "matched negative controls (FITC-labeled mouse IgG1 and IgG2a; Sigma..."  
*(antibody isotype controls)*

> "At 20 min, control cells demonstrate..." / "the endosomes in the control culture without AmB."  
*(AmB experimental contrast, not no-virus Isolation NC)*

### Decision
No Isolation-stage mock/uninfected culture NC → **D**.

---

## VI25 — Tier **C** (`C-stage`) — remediated after agent2

**Primary experiment:** Isolation sensitivity comparison of EBOV/Mak on Vero E6 / Huh-7 / MDM (isolation incubations).  
**Endpoint:** Plaque titer / immunostaining of isolation material (not matched CPE vs culture NC).

### Quotes — primary Isolation (virus inputs only; no culture NC)
> "Ten µL of each virus dilution (target dose 0.1 to 10,000 PFU/mL) in cell culture media was added to each well of a 6-well plate containing a 90% confluent monolayer of cells (Vero E6, Huh-7, or MDM) and 300 µL of the respective cell culture media. … Following incubation, cell culture supernatant was collected and titered by plaque assay…"

### Quotes — culture NCs that exist but are **wrong stage**
TCID50 (stock assay, not Isolation plate):
> "Briefly, matrix diluent was added to two control rows of each plate, and all test samples were added in quadruplicate and serially diluted 1:10 in a 96-well plate containing a 90% confluent Vero E6 monolayer."

Matrix toxicity module:
> "Monolayers exposed to semen retained roughly 50% of the monolayer compared to that of the negative control monolayer. However, the remaining cells appear healthy."

Animal media control (not culture Isolation NC):
> "The one death in the EBOV/Mak negative control (media) group (n = 2) was not associated with viral disease."

### Decision
`nc_any=yes` but `nc_isolation_stage=no` for primary Isolation plates → **C** (`C-stage`).  
Secondary TCID50/toxicity NCs must not upgrade Isolation tier (framework §5.1 / §6).  
`ambiguous=yes` only for C vs hard-line D if toxicity/TCID50 are refused as any culture NC; framework with `nc_any=yes` lands **C**.

---

## VI28 — Tier **D**

**Primary experiment:** SARS-CoV-2 Isolation on VeroE6 / TMPRSS2 / ACE2 lines.  
**Endpoint:** CPE.

### Quotes
> "Cells were observed daily under a microscope. The virus isolation assay was considered positive when CPEs were observed"  
> "Virus isolation was considered negative when no CPEs were observed by 6 days post-inoculation"

### Decision
No mock/uninfected culture NC → **D**.

---

## VI29 — Tier **D**

**Primary experiment:** PV rabies propagation on BSR; NP extraction.  
**Endpoint:** NP purification (not CPE).

### Quotes
> "Then, 9 mL of PV suspension was inoculated on to each monolayer and incubated for 1 hour at 37°C with 5% CO2..."

> "After virus adsorption, the cell monolayers were washed with 20 mL PBS by adding Dulbecco's modified Eagle's medium(DMEM) containing 10% FBS"

### Decision
No mock/uninfected culture NC → **D**.  
**Note:** Same article content as **VI47**.

---

## VI30 — Tier **D**

**Primary experiment:** Isolation of influenza A clinical isolates (MDCK / eggs).  
**Endpoint:** CPE for harvest.

### Quotes — Isolation / CPE
> "After 5–7 days of incubation at 35 °C, the supernatant was harvested based on the monitoring of cytopathic effects (CPE)"

### Quotes — secondary NCs (do not upgrade Isolation tier)
> "cells were washed with PBS and infected with viral dilutions ranging from 10−1 to 10−5, along with a negative control. After 1 h of incubation, the inoculum was removed, an overlay of DMEM and 0.9% soft agarose..."

> "The negative control, treated with phosphate-buffered saline (PBS), showed no fluorescence..."

### Decision
Primary Isolation lacks culture NC → **D**. Plaque/IFA NCs recorded in notes only.

---

## VI32 — Tier **D**

**Primary experiment:** FHV-1 Isolation on CRFK.  
**Endpoint:** CPE.

### Quotes
> "If the CRFK cells in the second passage did not show any cytopathic effects (CPE) after 7 days, the samples were considered negative for virus isolation"

### Decision
No mock/uninfected culture NC → **D**.

---

## VI33 — Tier **A**

**Primary experiment:** MERS-CoV Isolation from dromedary camel nasal swabs on Vero E6.  
**Endpoint:** CPE.

### Quotes — Isolation-stage PBS control well
> "A control well inoculated with sterile phosphate-buffered saline (PBS) was included on each plate. Plates were centrifuged at 1000 rpm (18 × g for 60 min)..."

> "The inoculum was removed, cells were gently washed three times with DMEM, and a fresh medium was added. The infected cells were monitored daily for 7 days to check for cytopathic effects (CPE) using an inverted microscope, and the medium was changed on alternate days."

### Quotes — figure
> "(A) Normal uninfected cells. (B) Early CPE of focal cell rounding at day three..."

### Match
Same plate, PBS instead of sample, then shared wash + fresh medium + daily CPE monitoring → M1–M6 by **allowed_inference** (Section 4.1 same-plate / diluent substitution) → **A**.

---

## VI34 — Tier **D**

**Primary experiment:** CAV-2 variant Isolation on MDCK.  
**Endpoint:** CPE / characterization.

### Decision
Text search: no mock/uninfected/control-well culture NC for Isolation → **D**.

---

## VI36 — Tier **B**

**Primary experiment:** CHIKV animal vertical transmission / breastfeeding study; Vero in vitro work; failed culture recovery from human colostrum.  
**Endpoint:** Mixed (animal; IF; plaque; culture Isolation attempt).

### Quotes — animal mock (not culture NC)
> "infected ... with ... infectious CHIKV, UV-inactivated CHIKV or the corresponding volume of mock via subcutaneous route"

### Quotes — Vero mock (culture-related but under-specified medium for mock)
> "Mock-infected Vero cells remained negative, as expected (Figures 3A–D)."

### Quotes — Vero medium (propagation / PRNT overlay)
> "Vero cells (ATCC CCL-81) were cultivated in DMEM with 10 % fetal bovine serum (FBS) and 1 % antibiotics/antimycotics..."

> "monolayers were overlayed with 500 µL of DMEM with 2% FBS and 1.5 % carboxymethylcellulose."

### Quotes — culture Isolation from colostrum (no NC stated)
> "CHIKV was not recovered by inoculating colostrum samples into Vero CCL-81 and Vero E6 cell cultures, even after three blind passages."

### Decision
Culture-level mock-infected Vero appears for IF → `nc_isolation_stage` borderline **yes** for in vitro IF; M3 for mock not explicit → **B**.  
`ambiguous=yes`: if primary forced to colostrum Isolation only → would be **D**.

---

## VI38 — Tier **A**

**Primary experiment:** Trypsin enhancement of SARS-CoV-2 infection on Vero E6; parallel mock infections.  
**Endpoint:** IF / titer / CPE-related morphology.

### Quotes — parallel mock
> "Vero E6 cells were preincubated with trypsin for 1 h before infection and then mock infected or infected with SARS-CoV-2 (P3) at an MOI of 1 for 1 h without trypsin addition."

> "Vero E6 cells were mock infected or infected with SARS-CoV-2 (P3) at an MOI of 1 for 1 h in the presence of trypsin."

> "Vero E6 cells grown in 96-well tissue culture plates were mock infected or infected with SARS-CoV-2 (P3) at a multiplicity of infection (MOI) of 1 for 1 h and cultured under the indicated conditions."

### Quotes — medium regime
> "Vero E6 cells (ATCC CRL-1586) were cultured in high-glucose Dulbecco’s modified Eagle’s medium (DMEM; Invitrogen...) supplemented with 10% fetal bovine serum (FBS...)"

> "When exogenous trypsin was added after inoculation, virus titers were considerably higher... The virus growth medium (high-glucose DMEM supplemented with penicillin-streptomycin and 5 µg of trypsin per ml) was then used in all subsequent experiments unless otherwise indicated."

> "...propagated in FBS-free medium with trypsin..."

### Decision
Mock and infected share stated experimental arms (trypsin/medium conditions) → M1–M6 **yes**, `match_basis=explicit` → **A**.

---

## VI39 — Tier **D**

**Primary experiment:** Isolation of Oita virus from bats.  
**Endpoint:** Culture growth / CPE-type observation.

### Quotes — animal NC only
> "Negative controls were mice administered PBS intracerebrally (n = 3)..."

### Decision
No culture-level Isolation NC in extracted text → **D**.

---

## VI40 — Tier **B** — remediated after agent3

**Primary experiment:** RSV multi-strain infection of HEp-2 and A549 vs mock.  
**Endpoint:** IF morphology, RNA-seq vs mock, cytokines.

### Quotes — mock (results/figures)
> "Mock-infected HEp-2 and A549 cells also differed in the morphology of their actin cytoskeleton..."

> "Cells were either mock-treated or infected with RSV/..."

> "we subjected RSV-infected and mock-infected A549 and HEp2 cells to high-throughput, short-read RNA sequencing"

### Quotes — medium (methods language targets infected arm)
> "...infected with RSV ... at an MOI of 0.01 for 1.5 h then the inoculum was removed, washed with PBS, and 2% FBS/MEM was added and incubated for a period of 24, 48, 72, or 96 hpi."

### Decision
Mock is clearly used as culture comparator (`nc_isolation_stage=yes` for infection morphology/omics), but methods do **not** state that mock wells received the same 2% FBS/MEM post-inoculum regime (sentence is framed for infected cells). Consistent with VI8/VI13/VI14 scoring → M3 **unknown** → **B**, not A.  
`ambiguous=yes`; `match_basis` is not explicit.

---

## VI41 — Tier **D**

**Primary experiment:** WNV small-plaque variant characterization.  
**Endpoint:** Plaque / growth.

### Decision
No mock/uninfected culture NC in text search → **D**.

---

## VI42 — Tier **B**

**Primary experiment:** VZV ORF29p localization; AdORF29 expression experiments.  
**Endpoint:** IF / WB (not classical clinical Isolation CPE).

### Quotes — mock infected
> "MeWo and U373MG cells were infected with AdORF29 at an MOI of 50 (lanes 2 to 7) or mock infected (lane 1)."

> "MeWo (A) and U373MG (B) cells were infected with AdORF29 at an MOI of 50 (lanes 1 to 6) or mock infected (lane 7)."

### Quotes — mock treated (drug vehicle — not culture NC)
> "infected cultures were either mock treated, treated with MG132, or treated with cycloheximide"

### Quotes — maintenance medium (context)
> "Infected cells were scraped in the maintenance medium..."

> "These cell lines were infected with AdORF29 and incubated for 3 days in maintenance medium..."

### Decision
Mock-infected exists for Ad experiments → culture NC present. Full M1–M6 for mock medium/serum not always restated at mock mention → **B**.  
`ambiguous=yes`; not classical Isolation paper.

---

## VI43 — Tier **A**

**Primary experiment:** Persistent SARS-CoV infection of Vero E6; mock-infected / control flasks.  
**Endpoint:** Morphology / viability / WB.  
**Source note:** PDF is image-only; quotes from rendered pages 262–263 (Materials and methods / Fig. 1 legend).

### Quotes — serum switch and controls in 2% FBS
> "The medium was changed to 2% FBS DMEM before virus infection."

> "On the other hand, Vero E6 cells were prepared in T-25 flasks at several concentrations with 2% FBS containing DMEM as controls because surviving cell number is different (less than 5% of total cells) in each experiment."

> "At 50 h.p.i., surviving cells and controls were washed with 2% FBS containing DMEM 5 times..."

> "We obtained a protein sample from mock-infected cells, with a similar cell number to persistently infected cells."

> "Mock-infected subconfluent cells, similar in number to surviving cells that had escaped from apoptosis by SARS-CoV infection, were also washed in the same manner."

### Decision
Mock-infected / control cultures explicitly in **2% FBS DMEM** parallel to infection → M1–M6 **yes** → **A**.

---

## VI45 — Tier **D**

**Primary experiment:** Rabies Isolation comparison HEK-293 / Neuro-2a / BHK-21.  
**Endpoint:** FAT foci.

### Quotes — “Virus control” = positive control strain
> "2.2. Virus control  
> The challenge virus standard CVS-11 strain of rabies virus was used."

### Quotes — maintenance medium
> "...replenished with maintenance medium (IMDM with 2% FBS) and the incubation continued..."

### Decision
CVS-11 is a **positive** control virus, not a negative culture control → `nc_any=no` → **D**.  
`positive_control_present=yes`.

---

## VI46 — Tier **D**

**Primary experiment:** RTCIT for street rabies Isolation.  
**Endpoint:** FAT.

### Quotes — media
> "Eagle basal medium with 3% fetal bovine serum was used as the cell maintenance medium, and a combination of 10% fetal bovine serum and 10% tryptose phosphate broth was used as the cell growth medium."

### Decision
No mock/uninfected culture NC in extracted text → **D**.

---

## VI47 — Tier **D**

**Primary experiment:** Same as VI29 (rabies NP from BSR).  
**Decision:** Duplicate methods; no culture NC → **D**.

---

## SPT10 — Tier **D**

**Primary experiment:** TC-tagged ZIKV propagation and imaging.  
**Endpoint:** CPE for harvest; biarsenical labeling / IFA.

### Quotes — propagation / CPE
> "Vero cells were cultured in DMEM (10% FBS) for 2 to 3 days. When the cell confluence reached 90 to 95%, the viral inoculum was added. After incubation for 2 h... the cells were washed once in PBS buffer and then cultured in fresh DMEM (2% FBS) medium for another 5 to 6 days. When the cytopathic effect (CPE) was progressed through 70 to 80%, the culture supernatants..."

### Quotes — “uninfected” (assay dye specificity, not Isolation NC)
> "strong biarsenical fluorescent signals were detected in the infected cells, while no biarsenical fluorescent signal was detected in the uninfected cells. This result clearly showed that the biarsenical reagent FlAsH only labeled the viral components..."

### Decision
Uninfected cells used to validate labeling reagent → not Isolation-stage morphology NC for CPE claims → `nc_any=no` under Section 2.3 → **D**.

---

## Double-check log

| Check | Result |
|-------|--------|
| All 28 PDF filenames have a row | Yes (agent3 corpus audit) |
| VI29/VI47 both scored (duplicate content) | Both D; same article |
| VI43 image-PDF scored via page render | A; agent3 verified quotes on rendered PDF |
| C tiers | VI25 only (`C-stage`) after remediation |
| Ambiguous cases flagged | VI8, VI13, VI25, VI36, VI40, VI42 |
| Secondary NCs not used to upgrade D Isolation papers | VI30 plaque/IFA NC kept secondary; VI25 TCID50/toxicity no longer upgrade Isolation |
| Positive-only control not scored as NC | VI45 D |
| Agent1 (VI2–VI24) | All tiers agree; VI8 notes medium fix |
| Agent2 (VI25–VI39) | VI25 A→C applied; others agree |
| Agent3 (VI40–SPT10 + corpus) | VI40 A→B applied; others agree; 28/28 rows |

*End of justification notes.*


---

# Expansion rescore — 2026-09-19 (cpe-assistant)
**Corpus:** dual-FBS Isolation-practice IDs not previously in `control-cultures-overview.csv` (n=78).
**Rule reminder:** ambiguity → worse tier; no inventing mocks; Isolation-stage vs downstream; PC does not raise NC tier.

## New tier counts (this batch only)

| Tier | n | IDs |
|------|---|-----|
| **A** | 3 | VI53, VI57, VI93 |
| **B** | 25 | VI203, VI208, VI211, VI215, VI217, VI219, VI220, VI221, VI227, VI51, VI52, VI58, VI59, VI60, VI63, VI67, VI74, VI76, VI77, VI79, VI82, VI83, VI87, VI91, VI92 |
| **C** | 5 | VI228, VI232, VI55, VI56, VI85 |
| **D** | 45 | VI200, VI201, VI202, VI204, VI205, VI206, VI209, VI210, VI212, VI214, VI216, VI218, VI222, VI223, VI224, VI225, VI226, VI229, VI230, VI231, VI233, VI44, VI50, VI54, VI61, VI62, VI64, VI65, VI66, VI68, VI69, VI70, VI71, VI72, VI73, VI75, VI78, VI80, VI81, VI84, VI86, VI88, VI89, VI90, VI94 |

**Batch total: 78.** Isolation-stage NC (`nc_isolation_stage=yes`): 29 (37.2%).

**Notable Tier A:** VI53, VI57, VI93.

**Access wishlist (methods not accessible this run):** VI44 (IJID subscription; abstract-only).

**PDF recovered this run (not previously in expansion cache):** VI225–VI229 (JSTAGE / Arch Razi / Redalyc).

## VI53 — Tier **A**

**Primary experiment:** BVDV titration/infection on MDBK with negative control groups  
**Endpoint:** CPE / titer

### Quotes
> MDBK cells infected with the HB2411 strain (experimental group) and uninfected cells (control group) were cultured under similar conditions for 72 h

> The collected virus supernatant was inoculated at 200 µL per well, with three replicates and three negative control groups. … inoculum was discarded, and 2 mL of DMEM containing 2% FBS was added to each well.

### Decision
Three negative control groups on same 6-well plate; after adsorption all wells get DMEM+2% FBS. Allowed inference M3 from shared post-inoculum medium. ambiguous=yes.

## VI57 — Tier **A**

**Primary experiment:** QBV infection assays on Vero/C6/36 with mock-infected wells  
**Endpoint:** CPE / growth (mock vs infected)

### Quotes
> Cell monolayers were either infected with QBV at an m.o.i. of 0.1 or mock infected with 2% FBS media.

> For mock-infected wells, this was done with 2% FBS L-15 Leibovitz media instead. … The inoculum was replaced with 2 ml/well of media.

### Decision
Methods: monolayers infected with QBV or mock infected with 2% FBS media; mock wells use 2% FBS L-15 instead of virus; inoculum replaced with maintenance medium. Isolation-stage matched NC including M3.

## VI93 — Tier **A**

**Primary experiment:** DENV-2 infection of cells with blank uninfected control under identical conditions  
**Endpoint:** CPE / morphology

### Quotes
> Both uninfected (blank control) and virus-infected (positive control) groups were maintained under identical culture conditions at 37 °C with 5% CO₂.

> All groups were cultured with DMEM containing 2% FBS and 1% antibiotics post-infection … including blank and virus controls.

### Decision
Methods: Both uninfected (blank control) and virus-infected groups maintained under identical culture conditions at 37C/5% CO2; morphology observed daily. Explicit identical-conditions NC → A.

## VI52 — Tier **B**

**Primary experiment:** B virus Isolation from oral swab on Vero/LLC-MK2; DMEM-only control well  
**Endpoint:** CPE

### Decision
Control well inoculated with sterile DMEM only; all wells washed then fresh maintenance medium. Maintenance medium composition (serum %) not explicit in Isolation paragraph → M3 unknown → B (not A).

## VI77 — Tier **B**

**Primary experiment:** PDCoV isolation/passage on LLC-PK with NC wells without virus  
**Endpoint:** CPE

### Decision
During passage positive and negative control wells without virus inoculation included; mock-infected also for IF. Medium for NC wells not restated → B.

## VI215 — Tier **B**

**Primary experiment:** ISAV replication in CHSE-214; uninfected flask control  
**Endpoint:** CPE / titer

### Decision
Five flasks infected and one uninfected flask as control for U5575-1 replication time course. Medium match for uninfected flask not restated → B.

## VI221 — Tier **B**

**Primary experiment:** Myxovirus/hepatitis culture; uninoculated control cultures  
**Endpoint:** CPE / morphology

### Decision
Uninoculated control cultures and controls inoculated with non-hepatitis sera; also control cultures on regular MEM-2CS in IUdR experiment. Isolation-stage NC present; serum match incompletely specified → B.

## VI55 — Tier **C** (C-stage)

**Primary experiment:** Isolation/infection (Orthobunyavirus (novel))  
**Endpoint:** CPE / morphology

### Decision
Re-audit: uninfected/mock only as IF/serology assay control, not Isolation-stage culture NC. Snip: munological staining, Vero-81 cells (including infected and mock-infected controls) were fixed and permeabilized to allow antibody access. Briefly, cells were fixed with 4

## VI56 — Tier **C** (C-stage)

**Primary experiment:** Primary Isolation/infection (sarbecoviruses (bat))  
**Endpoint:** CPE / other

### Decision
Culture NC language appears only in wrong-stage context (assay/IF/serology/animal). Quotes: amsters were intranasally inoculated with either CoV/Bat54, SARS-CoV-2, or PBS (Mock), and monitored daily for clinical signs and body weight changes up to 14 dpi ( A ). On 14 dpi,

## VI85 — Tier **C** (C-mismatch)

**Primary experiment:** FeAstV isolation on F81; parallel PBS negative controls for CPE  
**Endpoint:** CPE

### Quotes
> …discarded and maintained in DMEM supplemented with 2% FBS. Parallel negative controls were maintained using sterile phosphate-buffered saline. Cellular morphology was monitored … for cytopathic effect (CPE) assessment.

### Decision
Infected wells: adsorb then DMEM+2% FBS. Quote: "Parallel negative controls were maintained using sterile phosphate-buffered saline." Conservative reading = M3 mismatch (PBS maintenance vs 2% FBS), not matched inoculum-only contrast. ambiguous A vs C → C.

## VI228 — Tier **C** (C-stage)

**Primary experiment:** PRRSV isolation/serology on MARC-145  
**Endpoint:** CPE / NT

### Decision
Uninfected MARC-145 used as negative control antigen for serology; uninoculated in-contact pig is animal arm — not Isolation-stage culture NC.

## VI232 — Tier **C** (C-stage)

**Primary experiment:** WNV antiviral PMO assays on Vero  
**Endpoint:** titer / Rluc

### Decision
Negative controls are scramble PMO / DMSO vehicle — assay controls, not Isolation-stage uninfected culture NC.

## Compact notes — remaining batch IDs

| ID | Tier | Notes (abbrev) |
|----|------|----------------|
| VI44 | D | methods not accessible (subscription IJID; abstract-only). Abstract describes cell panel Isolation without mentioning culture NC. Wishlist PDF. Conservative D. |
| VI50 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI51 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: rstained with DAPI (Beyotime-C1006, CHN), and images were acquired using a fluore |
| VI54 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI58 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: oup) were inoculated with 10 4 PFU virus via the intracerebral route and observed |
| VI59 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip:  detection of BVDV RNA in the cell culture supernatants, whereas no amplification |
| VI60 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: g was clearly observed in PIV5-infected Vero cells ( Figure 1 D), whereas no sign |
| VI61 | D | Re-audit: prior B lacked Isolation-stage culture NC; animal/assay control language only or none. → D. |
| VI62 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI63 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip:  Ltd. Five pigs were assigned to the AHB1- and Chah2022-inoculated groups, and th |
| VI64 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI65 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI66 | D | Re-audit: prior B lacked Isolation-stage culture NC; animal/assay control language only or none. → D. |
| VI67 | B | Mock/uninfected present; serum trajectory for NC not verified → B. |
| VI68 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI69 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI70 | D | Negative control language is ELISA serum NC, not culture Isolation NC. |
| VI71 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI72 | D | Re-audit: prior B lacked Isolation-stage culture NC; animal/assay control language only or none. → D. |
| VI73 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI74 | B | Results: untreated C6/36 (negative control) maintained normal morphology vs serum/DENV. Matched infection medium for untreated arm not methods-defined → B. |
| VI75 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI76 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: t an MOI of 0.001, the mock group received an equal volume of CMNV-negative shrim |
| VI78 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI79 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: 6 h post-infection (hpi). RSV infection induced a time-dependent increase in EMV  |
| VI80 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI81 | D | Re-audit: prior B lacked Isolation-stage culture NC; animal/assay control language only or none. → D. |
| VI82 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: cted at 15°C showed VER signs. In addition, neither mortalities nor the NNV genom |
| VI83 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: rate was added, and the reaction was stopped with the stop solution. Absorbance w |
| VI84 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI86 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI87 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: n, ultimately affecting about 80% of the monolayer by the fifth passage ( Figure  |
| VI88 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI89 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI90 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI91 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: 3 (12 h MeV), 4–6 (12 h RSV), 7–9 (24 h MeV), and 10–12 (24 h RSV) clustered toge |
| VI92 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: a non-cytotoxic concentration: 90 µM), all prepared in a semisolid medium and inc |
| VI94 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI200 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI201 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI202 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI203 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: tab HSV-1 (McIntyre) infected HCE . Note the virus-infected cells showing apple g |
| VI204 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI205 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI206 | D | Re-audit: mock/uninfected language is animal-arm or non-culture; no Isolation-stage culture NC → D. |
| VI208 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: ent aliquot collected until ::: : : ~il !ii~ the cpe was complete. oQ. ... ~ ~ 25 |
| VI209 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI210 | D | Re-audit: mock/uninfected language is animal-arm or non-culture; no Isolation-stage culture NC → D. |
| VI211 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip:  interference was detected in cultures of L 132 and S-3 HeLa cells. SFV was titra |
| VI212 | D | Re-audit: prior B lacked Isolation-stage culture NC; animal/assay control language only or none. → D. |
| VI214 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI216 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI217 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: as washed with PBS and further incubated in MEM until a cytophatic effect was vis |
| VI218 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI219 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip:  times with 2 ml of MEM. The cell cultures were fed with 2 ml per well of MM. Con |
| VI220 | B | Isolation-stage NC mentioned; M2/M3 (serum) not verifiable from methods. Snip: ld not be immunoprecipitated from radiolabeled ished release of NSl and NSl’ (Fig |
| VI222 | D | "Uninfected cell monolayers" are assay substrates receiving infected cells, not parallel negative culture controls for Isolation CPE. |
| VI223 | D | Re-audit: prior B lacked Isolation-stage culture NC; animal/assay control language only or none. → D. |
| VI224 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI225 | D | Full PDF reviewed; no culture-level mock/uninfected NC for Isolation. |
| VI226 | D | Full PDF reviewed; no culture-level mock/uninfected NC for Isolation. |
| VI227 | B | Figure legends: CER/Vero uninfected cells vs CPE after IBDV propagation. Methods do not define matched maintenance medium for uninfected arm → B. |
| VI229 | D | Full PDF reviewed; no culture-level mock/uninfected NC for Isolation. |
| VI230 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |
| VI231 | D | Uninfected cultures shown for EM comparison of normal ultrastructure; not described as parallel Isolation-stage CPE NC under infection medium. Conservative D/am |
| VI233 | D | No culture-level mock/uninfected/negative-control wells described for Isolation/infection culture work. |


---

# Pass2 — 2026-09-19 (cpe-assistant)
Scored **21** remaining dual-FBS IDs from local `r1/plots/isolation-refs-dual-fbs_only.csv` (n=123). MSI dual claimed n=170 was not readable from this executor (no ListMachines/CopyToBox); miss list below is exact for available dual.

## VI121 — Tier **A**

**Primary experiment:** Adenovirus/coxsackie Isolation in WI-38 microcultures (IFAT)
**Endpoint:** IFAT / CPE morphology

### Decision
Same-slide central microculture “served as an uninoculated control.” Microcultures maintained in Leibovitz L-15 + 2% FCS (L-15M); inoculated wells receive specimen then L-15M. Allowed inference that uninoculated central well shares L-15M (M1–M6, including M3). Positive stock-virus controls present. Fig. 2 shows uninfected WI-38 microculture.

## VI111 — Tier **B** (detail)

Isolation-stage control cells / control tissue cultures for CPE comparison in figure and results. Maintenance medium 2% FCS stated for HeLa/MRC5 generally; not explicitly restated for control wells → M3 unknown → B (conservative).

## VI244 — Tier **C** (C-stage)

**Primary experiment:** CMV early antigen by two-color flow cytometry
Uninfected cells provide assay fluorescence baseline — not Isolation-stage culture NC for CPE under infection medium.

## Compact notes — pass2 batch

| ID | Tier | Notes (abbrev) |
|----|------|----------------|
| VI99 | D | Full PDF: Vero grown 8% FBS / maintained 2% FBS; CPE described. Sham/mock language is animal piglet arm only — no culture-level mock/uninfected NC for Isolat… |
| VI105 | D | Full PDF screened; no culture-level mock/uninfected/negative-control wells for Isolation. → D. |
| VI109 | D | PDF: “uninfected goat brain used as a control” is IF inoculum/antigen control, not parallel culture NC. No Isolation-stage culture NC. → D. |
| VI110 | D | PDF: “uninoculated and inoculated cultures” refers to transport-vest temperature maintenance, not NC wells. Specimens inoculated into duplicate cultures; no … |
| VI111 | B | Figure: HeLa “(a) control cells (b) CPE…”; text: control tissue cultures remained healthy longer. Isolation-stage uninoculated NC present. Universal 2% FCS m… |
| VI112 | D | Full PDF: “negative control [N]” is radioimmunoassay P/N ratio, not culture Isolation NC. No mock/uninfected culture NC. → D. |
| VI115 | D | Full PDF: MEM 5%→2% FCS; no culture-level mock/uninfected NC for Isolation. → D. |
| VI118 | D | Full PDF: DMEM 10%→2% FBS; no culture-level mock/uninfected NC for Isolation. → D. |
| VI121 | A | Methods: “The central culture served as an uninoculated control” on same slide as inoculated microcultures; cells maintained in L-15M (2% FCS); specimen well… |
| VI234 | D | PMC full text: compares Omni vs FBS for HSV Isolation sensitivity. “Positive and negative” tubes = CPE+/CPE− specimen outcomes, not parallel NC wells. No cul… |
| VI235 | D | PLOS ONE PDF: un-inoculated mosquitoes as NC for mosquito inoculation; PCR NTC. C6/36 culture Isolation/passage has no culture-level mock/uninfected NC. → D. |
| VI236 | D | EID appendix PDF: after adsorption MEM+1% FBS (Vero) / L-15+2% FBS (C6/36); observe CPE 7d. No culture-level mock/uninfected NC described. → D. |
| VI237 | D | Protocol text (protocols.io/DOI): inoculate PCR+ clinical sample on Vero; add DMEM+5% FBS; no mock/uninfected culture NC stated. → D. |
| VI239 | D | Landing-page abstract only accessible (full PDF blocked). Abstract describes MDCK Isolation; no culture NC mentioned. Conservative D (methods incomplete). |
| VI240 | D | Abstract-only (BJO full PDF paywalled). No culture NC mentioned. Same McSwiggan 1981 paper as VI241/VI242 (serum-type dual arms). → D. |
| VI241 | D | Same paper as VI240; abstract-only; no culture NC. → D. |
| VI242 | D | Same paper as VI240; abstract-only; no culture NC. → D. |
| VI243 | D | Full text not retrieved (JDS paywall). Abstract/notes in dual CSV have no culture NC language. Conservative D pending PDF. |
| VI244 | C | Abstract: viral antigen measured in infected or uninfected cells — assay baseline for flow cytometry, not Isolation-stage parallel culture NC for CPE. → C-st… |
| VI245 | D | IntechOpen chapter: prescribes “non-infected cultures (negative controls) should be maintained…” — recommendation language, not documentation that a scored I… |
| VI246 | D | PubMed abstract: cell-line sensitivity comparison for FMDV Isolation; no culture-level mock/uninfected NC mentioned. → D. |


---

# Pass3 — 2026-09-19 (cpe-assistant)

Scored **47** remaining dual-FBS IDs (VI247–VI293) from fresh MSI-copied `r1/plots/isolation-refs-dual-fbs_only.csv` (n=170). dual∖overview after this pass = **0**.

Sources: Europe PMC fullTextXML / PMC HTML; JSTAGE JJID PDFs (VI254–VI263); Pharma Journal PDF (VI265); abstracts where OA blocked. MSI local PDF path not reachable from this executor (no ListMachines/CopyToBox). SciELO (VI251), IFREMER PDF (VI270), CDC page (VI271) inaccessible this pass → conservative D with backlog note.

## VI272 — Tier **A**

**Primary experiment:** Ranavirus (McRV) Isolation from wrasse spleen homogenate on BF-2  
**Endpoint:** CPE / morphology

### Decision
Before inoculation, growth medium replaced with maintenance medium (L15 + 2% FBS + Anti-anti) for the plate. Same-plate control wells inoculated with equivalent volumes of sterile culture medium (negative control). Fig.1B uninfected control BF-2 monolayer at 6 dpi; no CPE in controls. Allowed inference M1–M6 including M3 (universal maintenance medium on plate + inoculum = sterile medium).

## VI281 — Tier **A**

**Primary experiment:** HEV infectivity/Isolation assay from pork pâté extracts on A549-D3  
**Endpoint:** IF ORF2 / culture infectivity

### Decision
Explicit: cells inoculated with virus extract **or medium (negative control)**; after 1 h washed and maintained in infection medium (maintenance medium + 2% DMSO + 5% FBS). Equal-hold 5% FBS trajectory. M1–M6 matched by explicit protocol (`match_basis=explicit`).

## VI288 — Tier **A**

**Primary experiment:** CyHV-2 Isolation from goldfish tissue homogenate on FtGF  
**Endpoint:** CPE / morphology

### Decision
“In control flasks, maintenance medium was used in place of tissue homogenate. After 1 h adsorption, 6.5 mL of the maintenance medium (L-15 medium with 2% FBS) was added to the FtGF flasks.” Fig.4 uninfected FtGF. Allowed inference M1–M6 including M3. (Titration arm also uses DPBS control wells + maintenance medium.)

## Tier C (pass3)

| ID | Code | Why |
|----|------|-----|
| **VI247** | C-stage | Non-infected control is plaque titration under 2.5% FBS DMEM; Isolation uses uninfected cells only for co-culture passage |
| **VI274** | C-stage | Cells-only column = TCID50 plate NC; chick/ELISA/PCR NCs wrong stage |
| **VI275** | C-stage | Hanks’ devoid-of-virus NC is in Virus Titration section, not primary Isolation |
| **VI277** | C-stage | CEF without virus = IIFT / neutralization assay NC |
| **VI279** | C-stage | Mock-treated N2a for IF; mouse mock inoculum — not Isolation-stage culture NC |
| **VI289** | C-stage | Maintenance-medium NC wells are for TCID50 validity, not propagation Isolation NC |
| **VI293** | C-stage | Medium-only / mock for plaque & IF of adapted stocks; mouse mock animal |

## Compact notes — pass3 batch (all 47)

| ID | Tier | Notes (abbrev) |
|----|------|----------------|
| VI247 | C | EPMC full text: Isolation mixes uninfected cells only for co-culture passage. Non-infected control is for plaque titration (2.5% FBS DMEM… |
| VI248 | D | OA full text screened; no culture-level mock/uninfected/negative-control wells for Isolation. → D. |
| VI249 | D | Abstract/EPMC metadata only (Sage paywall). No culture NC language in available text. Conservative D. |
| VI250 | D | PMC full text screened; no culture-level mock/uninfected NC for Isolation. → D. |
| VI251 | D | SciELO full text blocked (403/timeout) this pass; dual quotes have no NC language. Conservative D; backlog for PDF. |
| VI252 | D | EuropePMC text screened; no culture-level mock/uninfected NC for Isolation. → D. |
| VI253 | B | Fig.1 uninfected Vero E6 panel vs hMPV CPE. Isolation-stage uninfected comparator present; methods define trypsin MM for plate wells but … |
| VI254 | D | Mizuta JJID 2019 full PDF: microplate Isolation SOP Table 1; no culture-level mock/uninfected/negative-control wells described. → D. |
| VI255 | D | Mizuta JJID 2019 full PDF: microplate Isolation SOP Table 1; no culture-level mock/uninfected/negative-control wells described. → D. |
| VI256 | D | Mizuta JJID 2019 full PDF: microplate Isolation SOP Table 1; no culture-level mock/uninfected/negative-control wells described. → D. |
| VI257 | D | Mizuta JJID 2019 full PDF: microplate Isolation SOP Table 1; no culture-level mock/uninfected/negative-control wells described. → D. |
| VI258 | D | Mizuta JJID 2019 full PDF: microplate Isolation SOP Table 1; no culture-level mock/uninfected/negative-control wells described. → D. |
| VI259 | D | Mizuta JJID 2019 full PDF: microplate Isolation SOP Table 1; no culture-level mock/uninfected/negative-control wells described. → D. |
| VI260 | D | Mizuta JJID 2019 full PDF: microplate Isolation SOP Table 1; no culture-level mock/uninfected/negative-control wells described. → D. |
| VI261 | D | Mizuta JJID 2019 full PDF: microplate Isolation SOP Table 1; no culture-level mock/uninfected/negative-control wells described. → D. |
| VI262 | D | Mizuta JJID 2008 full PDF: HHVe6MRG microplate Isolation; GM/MM Table 1; no culture-level mock/uninfected NC. → D. |
| VI263 | D | Mizuta JJID 2008 full PDF: HHVe6MRG microplate Isolation; GM/MM Table 1; no culture-level mock/uninfected NC. → D. |
| VI264 | D | PMC full text screened; no culture-level mock/uninfected NC for Isolation. → D. |
| VI265 | B | Results: monolayer infected with sterile PBS (negative control) / Plate 1 uninfected Vero vs CPE. Isolation-stage PBS NC present. Methods… |
| VI266 | D | Abstract/EPMC only (JIDC). No culture NC mentioned. Conservative D. |
| VI267 | D | Abstract/EPMC only (Microbiol Immunol). No culture NC mentioned. Conservative D. |
| VI268 | D | OA full text screened; no culture-level mock/uninfected NC for Isolation (Belsham hits are citations only). → D. |
| VI269 | D | OA full text screened; no culture-level mock/uninfected NC for Isolation. → D. |
| VI270 | D | IFREMER PDF timed out / archive TLS fail this pass; dual FR quotes have no NC language. Conservative D; backlog for PDF. |
| VI271 | D | CDC URL 404/403 this pass; dual quotes (seed 10% FBS; inoculations DMEM+2% FBS) have no culture NC language. Guideline page scored D pend… |
| VI272 | A | Before inoculation all wells switched to maintenance L15+2% FBS+Anti-anti. Same-plate control wells inoculated with sterile culture mediu… |
| VI273 | D | OA full text: “uninfected” refers to NNV-free fish specimens (animal/tissue arm), not culture Isolation NC. No culture-level mock wells. … |
| VI274 | C | Column 12 “inoculated only with cells” = TCID50 plate NC; chick group NC and PCR/ELISA NCs are wrong stage. Isolation/adaptation inoculat… |
| VI275 | C | Hanks’ solution devoid of virus as negative control is in Virus Titration section; primary Isolation methods (adsorb → DMEM+2% FBS MM) do… |
| VI276 | B | Results/Fig.1: mock-infected cells normal morphology vs Isolation CPE. Isolation-stage mock present; methods do not define matched mainte… |
| VI277 | C | CEF without virus = IIFT negative control; cell control without virus in neutralization — assay-stage, not Isolation-stage culture NC for… |
| VI278 | D | OA full text: negative controls are PCR water and animal vaccine group D — not Isolation culture NC. → D. |
| VI279 | C | Mock-treated cells used for IF infection-efficiency on N2a; mock inoculum in neonatal mouse arm. Not Isolation-stage parallel culture NC … |
| VI280 | B | Fig.3/results: mock-infected controls without CPE vs PEDV Isolation. Isolation-stage mock present; methods (adsorb → serum-free wash → tr… |
| VI281 | A | Cells inoculated with virus extract or medium (negative control); after 1 h all washed and maintained in infection medium (maintenance +2… |
| VI282 | D | OA full text screened; no culture-level mock/uninfected NC for virus culture. → D. |
| VI283 | D | OA full text screened; no culture-level mock/uninfected NC. → D. |
| VI284 | D | OA full text screened; no culture-level mock/uninfected NC for Isolation. → D. |
| VI285 | D | OA full text: negative controls are PCR water / gel lanes — not Isolation culture NC. → D. |
| VI286 | B | Fig.1 mock-infected control group vs FPV013 CPE; TCID50 diluent NC wells then DMEM+2% FBS to each well. Isolation-stage mock for morpholo… |
| VI287 | D | OA full text: “uninfected” = human HC cohort; ELISA plate NCs — not Isolation culture NC. → D. |
| VI288 | A | Isolation: control flasks received maintenance medium in place of tissue homogenate; after 1 h adsorption, L-15 + 2% FBS added to FtGF fl… |
| VI289 | C | Wells inoculated with maintenance medium as NC are for TCID50 titration validity — not Isolation-stage NC for primary propagation/CPE und… |
| VI290 | D | OA full text screened; no culture-level mock/uninfected NC for Isolation. → D. |
| VI291 | B | Methods: “In parallel, a flask of uninfected Vero-E6 cells was passaged as a control” during 28-day Isolation passages (infected flasks g… |
| VI292 | D | OA full text: “remained uninfected” = specimen outcome, not parallel culture NC. → D. |
| VI293 | C | Mock-infected / medium-only negative controls are for plaque observation and IF/immunoblot of adapted stocks; mouse mock is animal arm. N… |
