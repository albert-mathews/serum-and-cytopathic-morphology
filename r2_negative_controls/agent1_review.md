# Agent 1 review

**Role:** Independent adversarial re-score of Isolation-stage negative culture controls (framework `control-cultures.md` v0.1).  
**Papers:** VI2, VI4, VI8, VI13, VI14, VI15, VI16, VI18, VI23, VI24.  
**Sources:** `wrk/isolation_practice/_txt/` full extracts; cross-checked against `control-cultures-overview.csv` and `control-cultures-justification-notes.md`.  
**Rule applied:** Decision tree Steps 0–3 in order; worse tier when genuinely ambiguous; no invented quotes; no “standard practice” inference for tier A.

---

## Per-paper findings

### VI2 — assigned **D** → agent **D** — **AGREE**

**Primary experiment:** Isolation of bat SL-CoV (WIV1) from PCR-positive faecal samples on Vero E6.  
**Endpoint:** CPE (daily observation; three blind passages).

**Decision tree**
- Step 1: No culture-level mock / uninfected / uninoculated / diluent-only Isolation wells. → **D**.

**Isolation medium (test only; not an NC quote)**
> "Virus isolation. Vero E6 cell monolayers were maintained in DMEM supplemented with 10% FCS. PCR-positive samples (in 200 ml buffer) were gradient centrifuged at 3,000–12,000g, and supernatant were diluted 1:10 in DMEM before being added to Vero E6 cells. After incubation at 37uC for 1 h, inocula were removed and replaced with fresh DMEM with 2% FCS. Cells were incubated at 37uC for 3 days and checked daily for cytopathic effect."

**Non-culture “negative controls” correctly excluded by prior scorer**
> "HeLa cells without ACE2 expression and Vero E6 cells were used as negative and positive controls, respectively."  
*(receptor/entry IF assay — different cell phenotype contrast, not Isolation NC)*

> "Serum from a healthy blood donor was used as a negative control in each experiment."  
*(serum neutralization, not culture NC)*

**Flags:** No missing Isolation NC language found. No over-inference risk (already D). PC present for ACE2 assays only (`positive_control_present=yes` appropriate).

---

### VI4 — assigned **D** → agent **D** — **AGREE**

**Primary experiment:** Isolation of HFRS agent from rat lung homogenates on Vero E6 with serial co-culture passage.  
**Endpoint:** IFA antigen (authors report no CPE).

**Decision tree**
- Step 1: No mock / uninfected parallel culture NC. → **D**.

**“Fresh normal cells” is co-culture passage material, not NC**
> "The infected cells in the subculture were suspended by trypsin treatment, washed, and mixed with an equal number of fresh normal cells in the fresh growth medium."

**No CPE; Isolation still in scope for culture NC scoring**
> "There was no visible cytopathic effect (CPE) in the antigen-positive cultures."

**Media (test system only)**
> "cultured in a growth medium of minimum essential medium (MEM), Eagle, with 5-10% fetal calf serum (FCS) or a maintenance medium of MEM with 1-2% FCS."

**Flags:** Prior notes correctly reject “normal cells” as NC. IFA serial-dilution assay uses inoculated wells only (“Two wells were inoculated with each dilution”) — no uninoculated culture control described. No under-calling of NC language.

---

### VI8 — assigned **B** (ambiguous) → agent **B** — **AGREE** (with justification correction)

**Primary experiment:** Isolation of 2019-nCoV from BALF on Vero E6/Huh7; CPE/IF characterization of the Isolate.  
**Endpoint:** Cytopathogenic effect / IF.

**Decision tree**
- Step 1: Culture NC language present (“mock virus” / “Mock-virus-infected”). → continue.
- Step 2: Extended Data Fig. 6 is used to document Isolation-associated CPE/IF of the recovered agent → treat as Isolation-stage morphology comparator. → continue.
- Step 3: Mock preparation and post-inoculation medium/serum for mock **not** stated; M2/M3 (and much of M4) **unknown** → **B** (not A). No explicit mismatch stated → not C-mismatch.

**Isolation methods (test only; note true Isolation post-inoculum medium)**
> "The following cell lines were used for virus isolation in this study: Vero E6 and Huh7 cells, which were cultured in DMEM containing 10% FBS."

> "The PCR-positive BALF sample from ICU-06 patient was spun at 8,000g for 15 min, filtered and diluted 1:2 with DMEM supplemented with 16 μg ml−1 trypsin before it was added to the cells. After incubation at 37 °C for 1 h, the inoculum was removed and replaced with fresh culture medium containing antibiotics (see below) and 16 μg ml−1 trypsin. The cells were incubated at 37 °C and observed daily for cytopathogenic effects."

**Isolation-stage mock (figure; methods do not define mock wells)**
> "a, b, Vero E6 cells are shown at 24 h after infection with mock virus (a) or 2019-nCoV (b). c, d, Mock-virus-infected (c) or 2019-nCoV-infected (d) samples were stained with rabbit serum raised against recombinant SARSr-CoV Rp3 N protein..."

**Wrong-stage NC (do not upgrade)**
> "mock-transfected cells were used as controls."  
*(ACE2 transfection/receptor experiment)*

**Neutralization medium (not Isolation; prior justification mis-attributed this as Isolation follow-up)**
> "After removing the supernatant, the plate was washed twice with DMEM medium. Cells were incubated with DMEM supplemented with 2% FBS for 3 days. Subsequently, the cells were checked for cytopathogenic effects."

**Why not A:** Framework §4.2 forbids upgrading from bare “mock” without medium/serum or “identical conditions” language. The only 2% FBS CPE sentence in methods is the **neutralization** arm, not Isolation and not Ext. Data mock. Isolation post-inoculum medium is “fresh culture medium … and trypsin” (growth medium family stated as DMEM + 10% FBS), so even the test Isolation enrichment trajectory is not cleanly “2% FBS.” Guessing that Ext. Data mock used either regime is forbidden.

**Why not D/C:** “Mock virus” panels paired with CPE/IF of the Isolate are culture NC language used for morphology/antigen of the Isolation product. Stage is Isolation-adjacent enough for Step 2 = yes; conditions under-specified → **B**.  
`ambiguous=yes` remains appropriate (primary Isolation methods never name mock wells; Ext. Data timing is 24 h while Isolation narrative cites CPE at three days — re-infection characterization is the better reading). Preferring the worse of A/B still lands on **B**.

**Flags:** Justification notes incorrectly treat the neutralization 2% FBS sentence as Isolation medium. That does **not** change the tier, but it overstates the case for an A-upgrade path. Fix the quote provenance.

---

### VI13 — assigned **B** (ambiguous) → agent **B** — **AGREE**

**Primary experiment:** Limiting-dilution Isolation of SARS-CoV-2 from NP/OP swabs on Vero CCL-81.  
**Endpoint:** CPE.

**Decision tree**
- Step 1: “mock infected cells” / Figure 1 panel A “Mock” = culture NC. → continue.
- Step 2: Mock is the morphology comparator for Isolation CPE at day 3. → Isolation-stage yes.
- Step 3: Methods never define how mock was prepared (no mock column, no “medium only,” no “identical conditions except no specimen”). M2/M3 unknown → **B**.

**Methods (specimen dilutions only; no mock protocol)**
> "For isolation, limiting dilution, and passage 1 of the virus, we pipetted 50 µL of serum-free DMEM into columns 2–12 of a 96-well tissue culture plate, then pipetted 100 µL of clinical specimens into column 1 and serially diluted 2-fold across the plate. We then trypsinized and resuspended Vero cells in DMEM containing 10% fetal bovine serum, 2 × penicillin/streptomycin, 2× antibiotics/antimycotics, and 2× amphotericin B at a concentration of 2.5 × 105 cells/mL. We added 100 µL of cell suspension directly to the clinical specimen dilutions and mixed gently by pipetting. We then grew the inoculated cultures … and observed for cytopathic effects (CPEs) daily."

**Results / figure mock**
> "CPE was not observed in mock infected cells (Figure 1, panel A)."

> "Phase-contrast microscopy of Vero cell monolayers at 3 days postinoculation: A) Mock, B) nasopharyngeal specimen, C) oropharyngeal specimen."

**Why not A:** Serial dilution description does **not** create a mock well; inventing a medium-only well is forbidden guesswork (§4.2.1, §4.2.5). Same-day imaging of Mock with specimens supports M5 only weakly and does not establish M3.

**Why not D:** Mock is named and used for Isolation CPE comparison — `nc_any=yes`, `nc_isolation_stage=yes`.

**Flags:** Prior scorer’s refusal to invent mock from the dilution plate is correct. `ambiguous=yes` appropriate. No missing NC quote.

---

### VI14 — assigned **B** → agent **B** — **AGREE** (stage borderline; stay B)

**Primary experiment:** Isolation of HRSV from nasopharyngeal aspirates on Hep-2.  
**Endpoint:** CPE (then IFA confirmation).

**Decision tree**
- Step 1: “uninfected (mock) Hep-2” / “Mock Hep-2 cell” = culture NC language. → continue.
- Step 2: Fig. 1A is a CPE morphology panel paired with Isolate-infected cells; Results cite Fig. 1A–B for CPE of isolates → Isolation-stage morphology comparator **accepted** (not pure IF-only assay control). → continue.
- Step 3: Medium/serum stated only for inoculated Isolation cultures; mock medium never restated → M3 (and M2/M4) **unknown** → **B**.

**Isolation medium (inoculated cultures only)**
> "The nasopharyngeal aspirates were treated with penicillin (100 units/mL) and streptomycin (100 µg/mL) before being inoculated to Hep-2 cells (ATCC) cultured in Dulbecco’s modified Eagle’s medium (DMEM; GIBCO, CA) supplemented with 2 % fetal bovine serum (FBS; GIBCO). The cytopathic effect (CPE) of inoculated Hep-2 cells was observed everyday for seven days."

**Mock first appears in IFA methods + figure**
> "CPE positive and uninfected (mock) Hep-2 cells were digested by 0.02 % EDTA, spotted to eight well glass slide..."

> "Fig. 1 – Cytopathic effect and indirect immunofluoresence test of HRSV isolates on Hep-2 cells. A, Mock Hep-2 cell; B, Isolate GZA17-01 infected Hep-2 cells; C, Indirect immunofluoresence test of mock Hep-2 cell; D, ..."

**Stage borderline (not enough to force change)**
- Isolation **methods** never place a mock well on the Isolation plate during the 7-day CPE watch.
- Mock is introduced when CPE-positive isolates are harvested for IFA.
- Adversarial C-stage reading: mock is IF/antigen-specificity material plus a morphology snapshot of stock uninfected cells, not a parallel Isolation NC under reduced serum.
- Adversarial D reading: if mock is only assay uninfected cells, §2.3 can exclude secondary IF controls.

**Why still B (not C/D):** Fig. 1A is explicitly a **CPE** panel (not IF-only), and Results treat panels A–B as the morphological definition of HRSV CPE. Under §2.5 that is usable as Isolation-stage morphology NC language. Conditions remain unverifiable → **B**.  
If corpus policy later forces **primary Isolation methods only** (no figure-level morphology NC), this paper would fall to **D**; that is a policy choice, not required by the current tree once Fig. 1A is accepted.

**Flags:** Not A. Do not allow universal “Hep-2 cultured in DMEM + 2% FBS” to cover mock without saying mock was run under that Isolation regime (§4.2.3).

---

### VI15 — assigned **D** → agent **D** — **AGREE**

**Primary experiment:** DENV Isolation from whole blood on C6/36, three blind passages.  
**Endpoint:** Plaque titer on BHK-21 (not CPE Isolation).

**Decision tree**
- Step 1: Full-text search finds **no** mock / uninfected / control culture language for Isolation or growth kinetics. → **D**.

**Isolation (test only)**
> "Blood samples were diluted 1:10 in minimal essential media (MEM) containing 2% fetal bovine serum (FBS) (Gibco) and added onto cultured monolayer of C6/36 cells for 1 hour... After 1 hour, the inoculum was removed and cells were cultured for 7 days in MEM with 2% FBS and antibiotics. Culture supernatant was collected on day 7 and used to infect new batch of C6/36 cells as above. This was repeated three times to achieve passage 3 (P3) isolates."

**Flags:** No under-calling. Plaque assay “as described earlier” external citations cannot create NC for this paper.

---

### VI16 — assigned **A** → agent **A** — **AGREE**

**Primary experiment:** Shell-vial Isolation of HSV-1 from corneal scrapings on HCE and Vero; non-viral keratitis scrapings as parallel controls.  
**Endpoint:** CPE examination + IF confirmation of HSV-1.

**Decision tree**
- Step 1: Isolation-stage culture controls present (non-viral scrapings inoculated in parallel). → continue.
- Step 2: Same shell-vial Isolation pipeline; outcome “None of the controls yielded HSV-1.” → Isolation-stage yes.
- Step 3: M1–M6 established by **explicit parallel protocol + universal post-inoculation maintenance medium** (allowed inference §4.1.1 / edge-case matrix NC §9). → **A**.

**Controls (Isolation-stage)**
> "Scrapings obtained from 10 patients with infectious keratitis of non-viral origin (Bacterial keratitis: n = 4, Mycotic keratitis: n = 3, Acanthamoeba keratitis: n = 1, Keratitis due to Nocardia spp: n = 1, and Mycobacterium spp: n = 1), were included as controls."

> "All the scrapings were simultaneously inoculated into shell vials of HCE and Vero cells."

> "None of the controls yielded HSV-1."

**Matched maintenance medium after adsorption (cases and controls share this protocol)**
> "For the shell vial cultures, specimens collected in VTM were thawed, vortexed vigorously for 30 seconds and an equal volume (0.5 ml/ vial) of the sample was inoculated into a vial of HCE and Vero cells. The vials were then centrifuged at 700 × g for 1 hour at room temperature and were incubated at 36°C for 1 hour for adsorption. The supernatant was discarded and 1 ml of maintenance medium (SHEM Supplemented with 1% FBS for HCE and MEM with 1% FBS for Vero cells) was added. The vials were incubated for 24 hours at 36°C."

> "routine examination of the cell cultures were done the next day (12–16 h) following the day of specimen inoculation, for any evidence of CPE. Cultures were terminated at 24 h post-infection."

**Match checklist**
| M | Call | Basis |
|---|------|--------|
| M1 | yes | Same HCE/Vero shell vials |
| M2 | yes | SHEM vs MEM as defined per line for all vials of that line |
| M3 | yes | Maintenance 1% FBS after adsorption for the Isolation phase |
| M4 | yes | Same adsorption/centrifugation protocol; difference is specimen etiology |
| M5 | yes | Simultaneous inoculation; same 24 h termination |
| M6 | yes | Intended contrast = non-HSV clinical matrix (framework matrix edge case) |

**Non-Isolation “Uninfected cells” (IF counterstain) correctly not used as the Isolation NC**
> "Uninfected cells are stained blue due to the counterstain..."  
*(assay counterstain; Isolation tier rests on non-viral scrapings)*

**Adversarial pressure that fails:** Demoting to B because control scrapings contain bacteria/fungi/etc. Framework §9 allows matrix/no-virus-source clinical controls when that is the stated contrast; endpoint is HSV-1 Isolation/IF, and Table 1 treats controls as true negatives. No evidence controls stayed in 5% growth serum while cases switched to 1% (would be C-mismatch if stated).

**Flags:** Prior A call is justified; not over-inference.

---

### VI18 — assigned **D** → agent **D** — **AGREE**

**Primary experiment:** Serial Vero passage adaptation of PR8 influenza (± reverse genetics / plaque / growth).  
**Endpoint:** Plaque size / growth kinetics (not classical CPE Isolation from specimens).

**Decision tree**
- Step 1: No mock / uninfected culture NC anywhere in methods. → **D**.

**Infection / passage medium (test only)**
> "The Vero cell culture medium was changed to DMEM containing 0.2% bovine serum albumin (BSA) with 1 µg/ml TPCK-trypsin, and the Vero cells were inoculated with the PR8 virus at an MOI of 0.001."

**Flags:** Clean D. No NC language under-called.

---

### VI23 — assigned **D** → agent **D** — **AGREE**

**Primary experiment:** SARS-CoV-2 Isolation from clinical respiratory specimens on Vero E6 / Vero E6 T2 / Vero E6 A2T2.  
**Endpoint:** CPE (harvest at 40–50% CPE).

**Decision tree**
- Step 1: No mock / uninfected / diluent-control culture NC in Isolation methods. → **D**.

**Isolation protocol (test only)**
> "We removed the medium and inoculated 50 µL of PCR-positive clinical specimen diluted 1:1 in DMEM with 2% fetal calf serum … in triplicate. After 1 hour incubation at 37°C, we added 1 mL of 2% FBS DMEM. We incubated the plates at 37°C in a CO2 incubator. We observed the cells daily and harvested when 40%–50% demonstrated cytopathic effect."

**“PBS” is specimen collection vehicle, not culture NC**
Text compares isolation rates from specimens collected in PBS vs VTM — not parallel uninoculated culture wells.

**Flags:** Clean D. No under-calling.

---

### VI24 — assigned **D** → agent **D** — **AGREE**

**Primary experiment:** Influenza Isolation from clinical swabs on Vero (± AmB) in serum-free medium + trypsin.  
**Endpoint:** CPE then HA confirmation.

**Decision tree**
- Step 1: No Isolation-stage mock / uninfected culture NC. → **D**.

**Isolation (test only)**
> "The thawed original material was isolated on Vero or MDCK cells in SFM supplemented with 5 µg of trypsin … and 25 µg of gentamicin …/ml. AmB (250 ng/ml) was added as indicated. After incubation for 5 to 7 days at 34°C and 5% CO2, the virus supernatants were passaged by transferring 50 µl to fresh subconfluent cell monolayers."

**“Control” language that is not culture NC**
> "matched negative controls (FITC-labeled mouse IgG1 and IgG2a; Sigma..."  
*(isotype antibody controls for flow)*

> "At 20 min, control cells demonstrate viral uptake by endosomes..." / "the endosomes in the control culture without AmB."  
*(AmB-absent experimental arm — still virus-infected)*

**TCID50 scoring language (not NC setup)**
> "...infected or noninfected by determining the presence or absence of a cytopathic effect"  
*(readout definition for wells already on the titration plate, not a described parallel Isolation mock)*

**Flags:** Prior scorer correctly refused to promote AmB-absent or isotype “controls.” Clean D.

---

## Systematic issues

1. **VI8 justification medium mis-attribution (does not change tier).**  
   The sentence “Cells were incubated with DMEM supplemented with 2% FBS for 3 days…” is the **neutralization assay**, not Isolation. Isolation post-inoculum medium is “fresh culture medium … and 16 μg ml−1 trypsin” after growth in DMEM + 10% FBS. Justification notes currently imply a plausible A path via that 2% sentence; framework forbids that path. Keep **B**, fix notes.

2. **Mock-in-figure without methods definition is a recurring B pattern (VI8, VI13, VI14).**  
   Corpus is consistently (and correctly) refusing A without methods-level mock medium/identity. Do not silently upgrade any of these three.

3. **Stage tension for post-Isolation IF/morphology mock (VI14).**  
   Isolation methods silent; mock appears in IFA methods + CPE figure. Current B is defensible via Fig. 1A. A future dual field (`primary_isolation_nc_tier` vs `best_culture_nc_tier`) would reduce ambiguity. Under single-tier rules, do **not** invent Isolation mock wells that methods omit.

4. **Non-culture “control” vocabulary is well handled (VI2, VI4, VI24).**  
   Neutralization sera, ACE2-null cells, “fresh normal cells” co-culture, AmB-minus arms, and isotype antibodies are correctly excluded. No systematic over-counting found in this set.

5. **No tier C in this 10-paper set.**  
   That is consistent with the sources: either no culture NC (D) or named Isolation-stage NC without match proof (B) or fully parallel clinical-matrix Isolation controls (A). No explicit M3 contradiction (e.g., NC held at 10% while tests at 2%) was found here.

6. **Over-inference risk is low on the lone A (VI16).**  
   Non-viral scrapings + simultaneous shell-vial protocol + explicit 1% FBS maintenance is within allowed inference. Not guesswork.

7. **Missing quotes in prior notes for this set:**  
   - VI8: Isolation trypsin / “fresh culture medium” quote should be primary Isolation medium evidence (add).  
   - VI8: Neutralization 2% FBS quote should be labeled neutralization, not Isolation.  
   - VI13/VI14/VI2/VI4/VI15/VI16/VI18/VI23/VI24: core NC/medium quotes in justification notes are essentially accurate relative to full text.

---

## Required remedies (numbered, actionable)

1. **Edit `control-cultures-justification-notes.md` for VI8:** Move the 2% FBS / 3-day CPE sentence under neutralization; add the Isolation quotes for BALF + trypsin + “fresh culture medium.” Keep tier **B**, `ambiguous=yes`, with note that A is blocked because mock medium is undefined and Isolation enrichment is not the neutralization 2% regime.

2. **Keep VI13 at B; do not promote to A** on re-score boards. Record explicit note: serial-dilution columns are all specimen dilutions; mock is results/figure-only.

3. **Keep VI14 at B; add stage flag** in notes: `stage_borderline=yes` — mock introduced in IFA methods; Isolation section silent; Fig. 1A supports Isolation-stage morphology NC for B. Optional future dual-tier field.

4. **Keep VI16 at A.** No demotion. Optionally add quote listing non-viral etiologies and the simultaneous-inoculation sentence for auditability.

5. **Keep all D papers (VI2, VI4, VI15, VI18, VI23, VI24) at D.** No NC language was missed on re-read of full text.

6. **Do not invent a C for this set** unless a later policy forces primary-methods-only scoring of VI14 (then D or C-stage — decide policy first; current framework text supports B via Fig. 1A).

7. **CSV flags to retain as-is for these IDs:**  
   VI8 `ambiguous=yes`; VI13 `ambiguous=yes`; VI16 `match_basis=explicit` (or `allowed_inference`/`mixed` if you want stricter labeling — either is defensible); all listed M\* = `unknown` for B papers remain correct.

8. **If a second scorer disputes VI14 stage:** Resolve by quote-level rule — if Fig. 1A is accepted as Isolation morphology NC → B; if rejected as assay/stock uninfected cells only → **C-stage** (or D if IF-only exclusion). Prefer **worse** → C-stage only if Fig. 1A is rejected. Agent 1 does **not** reject Fig. 1A.

---

## Verdict summary table (id | assigned | agent_tier | status)

| id   | assigned | agent_tier | status |
|------|----------|------------|--------|
| VI2  | D        | D          | AGREE  |
| VI4  | D        | D          | AGREE  |
| VI8  | B        | B          | AGREE (fix notes medium attribution; still B) |
| VI13 | B        | B          | AGREE  |
| VI14 | B        | B          | AGREE (stage borderline flagged; stay B) |
| VI15 | D        | D          | AGREE  |
| VI16 | A        | A          | AGREE  |
| VI18 | D        | D          | AGREE  |
| VI23 | D        | D          | AGREE  |
| VI24 | D        | D          | AGREE  |

**Hard tier changes proposed: 0 / 10.**  
**Soft documentation fixes: VI8 medium quote provenance; VI14 stage borderline note.**
