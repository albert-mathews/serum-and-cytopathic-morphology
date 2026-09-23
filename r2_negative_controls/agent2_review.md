# Agent 2 review

**Framework:** `control-cultures.md` v0.1  
**Assigned papers:** VI25, VI28, VI29, VI30, VI32, VI33, VI34, VI36, VI38, VI39  
**Sources:** `control-cultures-overview.csv`, `control-cultures-justification-notes.md`, full text under `wrk/isolation_practice/_txt/`  
**Stance:** adversarial; when genuinely ambiguous, prefer the worse tier (toward D). Special scrutiny on VI25 (A), VI33 (A), VI36 (B), VI38 (A).

---

## Per-paper findings

### VI25 — assigned **A** → **DISAGREE** → agent tier **C** (`C-stage`)

**Primary experiment (Section 6):** In vitro Isolation sensitivity comparison of EBOV/Mak on Vero E6 / Huh-7 / MDM (methods §2.9), with matrix toxicity as a related methods module (§2.7). Endpoint for Isolation success is plaque titer of supernatant and/or immunostaining of passage material—not parallel CPE scoring of Isolation wells against a no-virus control.

**Decision tree**

| Step | Finding |
|------|---------|
| 1 `nc_any` | **yes** — culture NCs exist, but not on the Isolation plates |
| 2 Isolation-stage for primary | **no** — best NC language is TCID50 diluent rows and toxicity media flasks |
| 3 M1–M6 | N/A for Isolation-stage → do not assign A/B |

**Why not A (over-inference)**

Assigned A rests on TCID50 “matrix diluent… two control rows” and the toxicity “negative control monolayer.” That is not a matched Isolation-stage NC for §2.9.

Primary Isolation methods describe only virus-containing inputs:

> "Ten µL of each virus dilution (target dose 0.1 to 10,000 PFU/mL) in cell culture media was added to each well of a 6-well plate containing a 90% confluent monolayer of cells (Vero E6, Huh-7, or MDM) and 300 µL of the respective cell culture media. … Following incubation, cell culture supernatant was collected and titered by plaque assay…"

> "The process was repeated with virus diluted in single donor semen, breast milk, or cell culture media… virus isolation was confirmed by immunostaining p2 of each virus isolation attempt…"

No mock / uninfected / PBS-only well is stated on Isolation plates. Lowest PFU doses and CPE-negative outcomes remain **test** cultures (framework §4.2.5), not NCs.

**NC language that does exist (wrong stage relative to primary Isolation)**

TCID50 titration (stock assay, not Isolation plate):

> "Briefly, matrix diluent was added to two control rows of each plate, and all test samples were added in quadruplicate and serially diluted 1:10 in a 96-well plate containing a 90% confluent Vero E6 monolayer. … Following 14 days of incubation… cytopathic effect was visually observed…"

Matrix toxicity (§2.7 / results)—explicitly a toxicity comparator, which framework §2.5 lists as non-Isolation-stage when not the Isolation morphology comparator:

> "A control flask with only media was [included]…"  
> "…cell culture media (control)."  
> "Monolayers exposed to semen retained roughly 50% of the monolayer compared to that of the negative control monolayer."

Animal “negative control (media)” groups are **in vivo**, not culture NCs for Isolation CPE.

Even if TCID50 diluent rows were re-scored as their own experiment, serum/enrichment for the 14-day TCID50 incubation is not stated in-text (methods cite “as previously described [18]”), so M3 would be **unknown** → **B** at best for that module—and secondary modules do not upgrade primary Isolation tier (§5.1 / §6).

**Forced phrases for the tier change**

- Isolation §2.9 has virus dilutions only; no culture NC on Isolation plates.  
- Toxicity / TCID50 controls are present but **wrong stage** for primary Isolation → **C-stage**, not A.

**Missing / weak quotes in justification notes**

- Missing: “A control flask with only media was…” (toxicity).  
- Missing: explicit acknowledgment that §2.9 Isolation wells never receive a no-virus inoculum.  
- Over-called: treating TCID50 diluent rows as “best documented culture NC” sufficient for tier A on an Isolation paper.

**Flags:** `ambiguous=yes` (C vs a hard-line D if a scorer refuses to count toxicity/TCID50 as any culture NC for this paper). Worse adjacent choice under framework wording is still **C** once `nc_any=yes`. Prefer **C** over original **A**.

---

### VI28 — assigned **D** → **AGREE** → agent tier **D**

**Primary experiment:** Primary Isolation of SARS-CoV-2 from upper respiratory specimens on VeroE6/TMPRSS2 and Vero E6-TMPRSS2-T2A-ACE2; CPE to 6 dpi.

**Isolation methods (full text):**

> "Briefly, 50 μL of respiratory sample was mixed with isolation medium [DMEM supplemented with 2% FBS, 1% Antibiotic–Antimycotic (Thermo Fisher Scientific)] and inoculated onto VeroE6/TMPRRSS2 or Vero E6-TMPRSS2-T2A-ACE2 cells seeded in 96-well culture plates. Cells were observed daily under a microscope. The virus isolation assay was considered positive when CPEs were observed. … Virus isolation was considered negative when no CPEs were observed by 6 days post-inoculation (dpi)."

**NC search:** No mock-infected, uninfected, uninoculated, PBS-only, or diluent-only culture wells for Isolation. Hits for “control” are β-actin loading control (WB) and procedural PBS washes for pseudovirus work—not culture NCs (§2.3 exclusions).

**Decision:** `nc_any=no` → **D**.  
**Notes:** CPE-negative clinical wells are test outcomes, not NCs (§4.2.5). Secondary neutralization plates use CPE as a readout but do not describe culture NCs either; even if present, they would not upgrade Isolation tier.

---

### VI29 — assigned **D** → **AGREE** → agent tier **D**

**Primary experiment:** Propagation of Pasteur vaccine (PV) rabies on BSR for nucleoprotein extraction/purification (not classical CPE Isolation).

**Methods:** All culture work is infected monolayers:

> "Then, 9 mL of PV suspension was inoculated on to each monolayer and incubated for 1 hour at 37°C with 5% CO2…"  
> "After virus adsorption, the cell monolayers were washed with 20 mL PBS by adding Dulbecco's modified Eagle's medium(DMEM) containing 10% FBS…"

**NC search:** PBS used only as wash reagent. No mock/uninfected culture NC for propagation, FAT titration, or SDS-PAGE.  
**Decision:** `nc_any=no` → **D**.  
**Note:** Same article family as VI47; consistent D is correct.

---

### VI30 — assigned **D** → **AGREE** → agent tier **D**

**Primary experiment:** Primary Isolation of influenza A from clinical samples on MDCK (and eggs); harvest guided by CPE.

**Isolation (no NC):**

> "The cells were passaged on Petri dishes, lower passages of MDCK cells were infected with IAV clinical samples and added with viral growth media, including EMEM and 1% PS, in the presence of TPCK-treated trypsin. After 5–7 days of incubation at 35 °C, the supernatant was harvested based on the monitoring of cytopathic effects (CPE)…"

**Secondary NCs (do not upgrade Isolation tier — §5.1 / §6):**

Plaque assay:

> "…cells were washed with PBS and infected with viral dilutions ranging from 10−1 to 10−5, along with a negative control. After 1 h of incubation, the inoculum was removed, an overlay of DMEM and 0.9% soft agarose solution supplemented with 1% PS and 2 µg/ml TPCK-treated trypsin was added…"

IFA assay control:

> "The negative control, treated with phosphate-buffered saline (PBS), showed no fluorescence…"

**Decision:** Isolation-stage `nc_any=no` for primary Isolation → **D**.  
**Flag:** Justification notes correctly record secondary plaque/IFA NCs; original tier correctly does **not** promote them. If someone re-scoped primary experiment to plaque titer only, plaque NC medium is reasonably specified (could be A for that arm)—but Isolation claim remains D.

---

### VI32 — assigned **D** → **AGREE** → agent tier **D**

**Primary experiment:** Primary Isolation of FHV-1 from cat tissue homogenates on CRFK; CPE over passages.

**Isolation medium (test only):**

> "Confluent CRFK cells in 24-well plates were washed twice with phosphate-buffered saline (PBS, pH 7.2), then incubated with 200 μL of each filtered sample at 37°C for 1 h. Subsequently, the liquid in the 24-well plates was removed and 1 mL of fresh DMEM containing 3% FBS was added to each well."  
> "If the CRFK cells in the second passage did not show any cytopathic effects (CPE) after 7 days, the samples were considered negative for virus isolation."

**NC search:** PBS only as wash; no mock/uninfected/control wells. IFA performed on infected cells only; no uninfected IFA counter-monolayer described as culture NC.  
**Decision:** `nc_any=no` → **D**.  
**Note:** Reduced serum (3% FBS) on inoculated wells makes absence of a matched NC especially material to the project confound—but absence → D, not C.

---

### VI33 — assigned **A** → **AGREE** → agent tier **A**

**Primary experiment:** Primary Isolation of MERS-CoV from dromedary camel nasal swabs on Vero E6; CPE for 7 days with blind passages.

**Isolation-stage PBS control (same plate):**

> "We inoculated Vero E6 cells seeded at 80–90% confluence in 6-well cell culture plates … with 100 μL of the samples and incubated the cells at 37°C in a 5% carbon dioxide atmosphere. A control well inoculated with sterile phosphate-buffered saline (PBS) was included on each plate. Plates were centrifuged at 1000 rpm (18 × g for 60 min)…"

> "The inoculum was removed, cells were gently washed three times with DMEM, and a fresh medium was added. The infected cells were monitored daily for 7 days to check for cytopathic effects (CPE) using an inverted microscope, and the medium was changed on alternate days."

**Growth medium (defines “medium” for the system):**

> "Cells were maintained in Dulbecco’s modified Eagle’s medium … supplemented with 10% heat-inactivated fetal bovine serum … and 5 mL of Gibco Antibiotic-Antimycotic solution…"

**Figure comparator:**

> "(A) Normal uninfected cells. (B) Early CPE of focal cell rounding at day three post-inoculation (PI) …"

**M1–M6 (allowed inference §4.1.3 same-plate / diluent substitution)**

| M | Status | Basis |
|---|--------|--------|
| M1 cells | yes | Same Vero E6 plate |
| M2 base medium | yes | Shared wash DMEM + “fresh medium” for plate protocol |
| M3 serum | yes | No reduced-serum infection medium stated; maintenance is 10% FBS; single post-inoculum medium statement applies to plate |
| M4 additives | yes | Same antibiotics in maintenance; PBS only implements no specimen |
| M5 timeline | yes | Same plate, centrifugation, wash, daily CPE, medium change schedule |
| M6 inoculum-only | yes | Sterile PBS vs swab supernatant |

**Adversarial checks that failed to demote**

- “Fresh medium” is not re-specified as “DMEM + 10% FBS” after the wash. Under §4.1.3 this is the canonical allowed-inference A pattern; inventing a different control medium would be forbidden guesswork the other way.  
- “The infected cells were monitored…” is infected-centric wording, but control well is defined on each plate before the shared post-inoculum paragraph, and Fig. 1A shows normal uninfected cells as the CPE comparator.  
- No reduced-serum Isolation medium → §4.3 special rule does not force M3 unknown.

**Decision:** Isolation-stage NC + M1–M6 by allowed inference → **A**. `match_basis=allowed_inference`.  
**Quote quality:** Justification notes are adequate; Fig. 1A quote is present.

---

### VI34 — assigned **D** → **AGREE** → agent tier **D**

**Primary experiment:** Primary Isolation of CAV-2 variant from raccoon dog fecal filtrates on MDCK; CPE.

**Isolation:**

> "The MDCK cells were plated into 24-well plates, the fecal samples (100 μL) were added, and the mixture was incubated … for 1 hour. After removing the fecal samples, 1 mL DMEM containing 5% FBS was added to each well. … When cytopathic effects (CPEs) were observed in the MDCK cells, the cell supernatants were collected… If CPEs were not observed after the second passage, the samples were excluded from virus isolation."

**NC search:** No mock/uninfected/control-well culture NC. PBS appears in other assay contexts (HA/embedding), not as Isolation NC. Reference CAV-1/CAV-2 strains are **positive** comparators for PCR/HA/VN, not culture NCs.  
**Decision:** `nc_any=no` → **D**.

---

### VI36 — assigned **B** → **AGREE** → agent tier **B** (keep worse-leaning ambiguity flag)

**Primary experiment selection:** Mixed paper. Culture Isolation claims that matter for this corpus:

1. Recovery of infectious CHIKV from fetal/placental tissue into Vero (successful).  
2. Attempted Isolation from human colostrum into Vero CCL-81 / Vero E6 (failed after three blind passages).  
3. Extensive animal “mock” arms (not culture NCs).  
4. “Mock-infected Vero” for serology IF (assay control).

Per §5.1, use the **best documented Isolation-stage culture NC**, not the worst arm alone.

**Isolation-stage NC present (under-specified):** parallel Vero cultures inoculated with mock-dam fetal material:

> "Infectious CHIKV was recovered in Vero cell cultures from fetal tissues exhibiting severe teratogenic effects, and isolates were confirmed by immunofluorescence (G2 and G4). Uterus and fetuses in figures B1 and B3 are representative of those obtained from mock females, as well figures G1 and G3 represent cultures of Vero cells inoculated with their samples."

This is Isolation-stage NC language (no-virus-source tissue inoculated in parallel into the same cell system). Methods never state the Isolation culture medium/serum trajectory for those tissue inoculations (only general Vero growth 10% FBS and plaque/PRNT overlays with 0%→2% FBS). → M2/M3/M4/M5 **unknown** → **B**.

**Colostrum Isolation (no culture NC):**

> "CHIKV was not recovered by inoculating colostrum samples into Vero CCL-81 and Vero E6 cell cultures, even after three blind passages."

If primary were forced exclusively to colostrum Isolation → **D**. Framework prefers best Isolation-stage NC when multiple exist → still **B** from fetal mock-tissue arm.

**Not Isolation-stage / not culture NC for Isolation**

Animal mock:

> "…infectious CHIKV, UV-inactivated CHIKV or the corresponding volume of mock via subcutaneous route"

Serology IF substrate (assay control, §2.3 / wrong-stage for Isolation morphology):

> "Mock-infected Vero cells remained negative, as expected (Figures 3A–D)."

PRNT uses 2% FBS overlay after infection but does not describe uninfected plaque-control wells as Isolation NCs.

**Adversarial pressure on assigned B**

- Under-calling risk: notes lean on “Mock-infected Vero for IF” as the culture NC; the stronger Isolation-stage quote is **G1/G3 mock-female tissue cultures**, which notes under-emphasize.  
- Over-calling risk: IF mock is not Isolation-stage; if that were the only culture “mock,” tier would be **C-stage** or **D**, not B.  
- Ambiguity: `ambiguous=yes` remains correct (B vs D if colostrum-only primary). Preferring worse adjacent tier would flip to **D**; the decision tree’s multi-NC rule keeps **B**. I **agree B** under §5.1, with the colostrum arm recorded as D in notes.

**Missing quote in justification notes:** the G1/G3 mock-female Vero inoculation sentence (should be primary `quotes_nc` for Isolation-stage).

---

### VI38 — assigned **A** → **AGREE** → agent tier **A**

**Primary experiment:** Main in vitro SARS-CoV-2 infection on Vero E6 ± exogenous trypsin; endpoints IF, titer, CPE/syncytia morphology (not clinical specimen Isolation). Allowed under §6 priority #3.

**Parallel mock language (explicit):**

> "Vero E6 cells were preincubated with trypsin for 1 h before infection and then mock infected or infected with SARS-CoV-2 (P3) at an MOI of 1 for 1 h without trypsin addition."

> "Vero E6 cells were mock infected or infected with SARS-CoV-2 (P3) at an MOI of 1 for 1 h in the presence of trypsin."

> "Vero E6 cells grown in 96-well tissue culture plates were mock infected or infected with SARS-CoV-2 (P3) at a multiplicity of infection (MOI) of 1 for 1 h and cultured under the indicated conditions."

**Medium / enrichment (including FBS-free + trypsin regime):**

> "Vero E6 cells (ATCC CRL-1586) were cultured in high-glucose Dulbecco’s modified Eagle’s medium (DMEM; Invitrogen…) supplemented with 10% fetal bovine serum (FBS…)"

> "…propagated in FBS-free medium with trypsin at different concentrations…"

> "The virus growth medium (high-glucose DMEM supplemented with penicillin-streptomycin and 5 µg of trypsin per ml) was then used in all subsequent experiments unless otherwise indicated."

**M1–M6**

| M | Status | Basis |
|---|--------|--------|
| M1 | yes | Vero E6 throughout |
| M2 | yes | High-glucose DMEM |
| M3 | yes | Parallel mock/infected under indicated conditions; virus growth medium (FBS-free + trypsin) applied to subsequent experiments that include mock arms; early arms use growth medium without trypsin for both |
| M4 | yes | Trypsin is the experimental additive shared across mock vs virus contrast when “indicated”; difference is virus presence |
| M5 | yes | Same infection timing / imaging at 24 hpi etc. |
| M6 | yes | Mock vs SARS-CoV-2 inoculum |

**Adversarial checks**

- Some legends say “The virus-infected cells were then maintained in the presence of trypsin,” which is infected-centric. Counterweight: IFA methods explicitly “mock infected or infected … and cultured under the indicated conditions,” and Fig. 2 shows mock vs infected under presence/absence of trypsin. That is enough for §4.1 allowed inference; demotion to B would require treating parallel mock design as non-evidence—too pedantic relative to §4.1.  
- MTT “Control” rows are reagent cytotoxicity controls, not Isolation NCs; they neither help nor hurt the A assignment.  
- Paper is not primary clinical Isolation; tier still applies to the infection–culture morphology arm as scored.

**Decision:** Isolation-stage (infection-stage) NC with matched conditions → **A**, `match_basis=explicit` / mixed explicit+allowed.  
**Quote quality:** Adequate; consider adding the IFA “cultured under the indicated conditions” sentence as the strongest M3/M5 quote.

---

### VI39 — assigned **D** → **AGREE** → agent tier **D**

**Primary experiment:** Primary Isolation of Oita virus from bat swab samples on Vero-RcACE2 (blind passages); CPE/cell detachment.

**Isolation methods:**

> "Suspended swab samples were used for virus isolation… the supernatant was filtered… and inoculated into Vero-RcACE2 cells. After an hour of incubation at 37°C, the inoculum was replaced with fresh medium. The samples were subjected to blind passage thrice at 1-week intervals."

**NC search:** Only animal pathogenicity NCs:

> "Negative controls were mice administered PBS intracerebrally (n = 3) or intranasally (n = 3)."

No culture-level mock/uninfected/PBS well for Isolation or growth-kinetics monolayers.  
**Decision:** `nc_any=no` for culture Isolation → **D**. Animal PBS controls do not count (§2.5).

---

## Systematic issues

1. **Primary-experiment drift → false A (VI25)**  
   Assigned A used the *best-looking* culture control language in the paper (TCID50 diluent rows; toxicity “negative control monolayer”) rather than NC quality for the **primary Isolation** protocol (§2.9). Framework §5.1 / §6 forbids upgrading Isolation tier from wrong-stage or secondary modules. This is the clearest over-inference for tier A in this batch.

2. **Toxicity / matrix media controls misread as Isolation CPE NCs**  
   Framework §2.5 explicitly treats toxicity matrix rows that are not the Isolation morphology comparator as non-Isolation-stage. VI25’s media-only flasks compare matrix toxicity, not inoculum-specific CPE on Isolation plates. Edge-case “matrix toxicity controls may be Isolation-stage” was stretched into A without parallel no-virus wells on Isolation assays.

3. **Secondary assay NCs correctly not upgraded (VI30) — keep this discipline**  
   Plaque “negative control” and IFA PBS negative control were rightly left out of the Isolation tier. Same rule must apply to VI25 TCID50 rows.

4. **Mock-infected IF substrates vs Isolation-stage NC (VI36)**  
   Justification notes lean on “Mock-infected Vero cells remained negative” (serology IF). That is weak/wrong-stage. The paper actually has a better Isolation-stage quote (mock-female tissues → Vero G1/G3) that is under-quoted. Risk: either under-calling Isolation NC language or over-calling assay mocks as Isolation-stage.

5. **Same-plate PBS + shared post-inoculum medium (VI33) is the gold A pattern**  
   This is the cleanest A in the batch and matches §4.1.3. Do not let pedantic “fresh medium” re-composition worries demote it without textual contradiction.

6. **Parallel “mock infected or infected … under the indicated conditions” (VI38)**  
   When infection medium (including FBS-free + trypsin) is defined for the experimental series, this supports A. Infected-only legend wording is noise if methods bind mock and infected to the same conditions.

7. **Solid D cluster (VI28, VI29, VI32, VI34, VI39)**  
   No evidence of under-calling NC language after full-text search. Reduced-serum Isolation media appear (VI28 2% FBS; VI32 3% FBS; VI34 5% FBS) with zero culture NC—important for the serum-match scoring criterion, correctly scored D.

8. **Zero tier C in the whole corpus overview is a red flag**  
   This batch alone yields at least one clear **C-stage** (VI25) if scored by the decision tree. Corpus-wide C = 0 suggests systematic preference for A/B/D over C when wrong-stage NCs exist.

9. **Ambiguity handling inconsistent**  
   VI25 was marked A with `ambiguous=yes` but ambiguity was about Isolation vs TCID50 scope—framework says choose worse tier when unresolved. That would have been C or D, not A.

---

## Required remedies (numbered, actionable)

1. **Rescore VI25 from A → C (`c_reason=C-stage`)** in `control-cultures-overview.csv`. Set `nc_isolation_stage=no`, `nc_any=yes`, all `m*=NA`, `match_basis=NA`, `ambiguous=yes` with note: “TCID50 diluent rows + toxicity media flasks exist; primary Isolation §2.9 has no culture NC.”

2. **Rewrite VI25 justification notes:** quote §2.9 Isolation protocol in full; state explicitly that Isolation wells only receive virus dilutions; move TCID50/toxicity quotes to “wrong-stage / secondary”; remove A claim based on diluent rows.

3. **Do not use TCID50/plaque/IFA NCs to assign Isolation tier A** unless that assay *is* the primary experiment under §6 (document `primary_experiment` label when that rare choice is made).

4. **VI36 notes fix:** replace primary `quotes_nc` emphasis with the G1/G3 mock-female Vero inoculation sentence; relegate “Mock-infected Vero cells remained negative” to assay-control / non-Isolation-stage. Keep tier **B**; retain `ambiguous=yes` (B vs colostrum-only D).

5. **VI33:** keep **A**; optionally add note that M3 is allowed inference from single plate medium + 10% maintenance (no reduced-serum Isolation medium stated). No CSV change.

6. **VI38:** keep **A**; add IFA methods quote “mock infected or infected … and cultured under the indicated conditions” and virus growth medium (FBS-free + 5 µg/ml trypsin) to `quotes_medium_test` / `quotes_medium_nc`.

7. **VI28, VI29, VI30, VI32, VI34, VI39:** no tier change. For VI30, keep secondary plaque/IFA NCs in notes only.

8. **Re-audit all original tier A papers** for the same VI25 failure mode: secondary titration/toxicity/assay controls promoted to Isolation A. At minimum re-check VI16, VI40, VI43 with primary-experiment discipline.

9. **Recount corpus A/B/C/D** after VI25 change (A: 6→5; C: 0→1). Update summary table in justification notes.

10. **When `ambiguous=yes`, enforce worse-tier rule** in scoring SOP (framework §3 / §12): document both candidate tiers and assign the worse letter unless quote-level review resolves upward.

---

## Verdict summary table

| id | assigned | agent_tier | status |
|----|----------|------------|--------|
| VI25 | A | C | **DISAGREE** — C-stage (toxicity/TCID50 NC only; Isolation §2.9 has no culture NC) |
| VI28 | D | D | AGREE |
| VI29 | D | D | AGREE |
| VI30 | D | D | AGREE (secondary plaque/IFA NC noted, not upgraded) |
| VI32 | D | D | AGREE |
| VI33 | A | A | AGREE (same-plate PBS + shared wash/medium; allowed inference) |
| VI34 | D | D | AGREE |
| VI36 | B | B | AGREE (best Isolation NC = mock-female tissue→Vero under-specified; colostrum arm D; IF mock is assay-stage) |
| VI38 | A | A | AGREE (parallel mock under indicated trypsin/medium conditions) |
| VI39 | D | D | AGREE (PBS NC is animal-only) |

**Batch tally:** 9/10 agree; **1 disagree (VI25 A→C)**.  
**Special-scrutiny outcomes:** VI25 demoted; VI33 A held; VI36 B held with quote remediation; VI38 A held.
