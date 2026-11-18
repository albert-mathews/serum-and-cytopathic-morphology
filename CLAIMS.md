# Claims register — argument spine

**Purpose.** One reference file for every load-bearing assertion in this project, tagged with a
math-proof-style *kind* (axiom, definition, observation, lemma, theorem, corollary, conjecture,
counterexample) so that (a) authors can keep track of what is established, assumed, or predicted, and
(b) readers can build the argument step by step: later claims cite the earlier claims they rest on.

This is **not** a second TODO or a new source catalogue. Source IDs stay where they are
(`VI##` for Isolation papers, `P1-###`/`P2-###`/`P3-###` for screened sources, tier A–D for R2
controls, `R*`/`P*` for streams). A claim ID points *at* sources; it does not replace them.

## Code scheme (kind-prefixed) + table of contents

Each claim carries a **kind-prefixed** code. The numeric portion is identical to the old `C###` numeric
portion (1:1 mapping `C020` → `OB020`), so stream references update by swapping only the prefix.

| Kind | Prefix | Count | Example |
|------|--------|-------|---------|
| Definition | `DEF` | `DEF001`–`DEF006` | DEF001 Isolation |
| Axiom | `AX` | `AX010`–`AX012` | AX010 Pipeline scope |
| Observation | `OB` | `OB020`–`OB028`, `OB080`–`OB082`, `OB150` | OB020 corpus modal 10%→2% |
| Lemma | `LM` | `LM030`–`LM035` | LM030 practice follows recipe |
| Theorem | `TH` | `TH040` | TH040 serum step-down drives CPE |
| Corollary | `CRL` | `CRL041`–`CRL043` | CRL041 CPE not inoculum-specific |
| Conjecture | `CNJ` | `CNJ050`–`CNJ059`, `CNJ151` | CNJ053 genome inherits endpoint |
| Counterexample (adversarial) | `ADVR` | `ADVR060`–`ADVR062` | ADVR060 not all practice steps down |

TOC (links jump to the section): [Definitions](#definitions) · [Axioms](#axioms-premises--scope) ·
[Observations](#observations-empirical-facts) · [Lemmas](#lemmas-supporting-established-findings) ·
[Theorem](#theorem) · [Corollaries](#corollaries) · [Conjectures](#conjectures-predictions-p-arms) ·
[Counterexamples](#counterexamples-adversarial-balance) · [Dependency index](#dependency-index-build-order) ·
[Rules of use](#rules-of-use)

## Kind vocabulary

| Kind | Proof-library meaning | Meaning here | Sets the bar |
|------|----------------------|--------------|--------------|
| **Axiom** | assumed, not proved | Stated premise / scope assumption the argument takes as given | Must be explicit; not a result |
| **Definition** | stipulated term | Stipulated meaning of a term ("Isolation", "CPE", tier A–D) | Just a definition, nothing empirical |
| **Observation** | recorded datum | A descriptive empirical fact from a corpus/experiment | Evidence-tagged; survives or falls on the source |
| **Lemma** | supporting result | An established finding that is not the headline but feeds a theorem | Evidence-backed; conservative |
| **Theorem** | main proved result | The central claim the paper is built to establish | Evidence-backed across the cited streams |
| **Corollary** | near-direct consequence | An inference that follows cheaply from a theorem/lemma | Must name exactly which claims it follows from |
| **Conjecture** | proposed, unproven | A directional prediction (the P1–P7 arms) | Marked "predicted"; strengthen/weaken log lives in the stream |
| **Counterexample** | refuting instance | An adversarial case that resists a pattern | Kept visible so the paper is not one-sided |

## Field schema

Each entry: `ID · Kind` — **Slug.** Statement. *(Follows from …; Evidence …; Status …; Stream …)*

- **ID:** `DEF###` / `AX###` / `OB###` / `LM###` / `TH###` / `CRL###` / `CNJ###` / `ADVR###`. Cite the
  code in notes and in `tex/` (can become a `\label`). For backward search, `grep "C###"` still finds old refs.
- **Follows from:** the claim IDs this one rests on (the dependency arrows of the build).
- **Evidence:** one of the house tags `[VERIFIED src]` (read in the full document), `[FIGURE]`,
  `[SUPPLIER]`, `[IN-HOUSE]`, `[UNVERIFIED]`, `[DATA REQUIRED]`, plus a source pointer (corpus file /
  snippet / bibliography). **Abstract-only research is not allowed**: an abstract may identify a source but
  not ground a claim. A claim that rests only on an abstract is `[DATA REQUIRED]` until the full text is
  read. `[VERIFIED-ABSTRACT]` is retained only as a legacy provenance marker for pre-existing
  abstract-derived material, never as a tag for a new claim.
- **Status:** `stipulated` | `assumed` | `established` | `established-scoped` | `provisional` | `predicted` |
  `rejected`.
- **Stream(s):** which stream owns the evidence (R1–R4, P1–P7).

---

## Definitions

- **DEF001 · Definition** — **Isolation.** Capital-I Isolation is the operational product
  *culture → cytopathic readout → passage* (an **Isolate**); it does not mean chemical purity.
  *(Evidence: house convention; Status: stipulated; Streams: all — source r1.md snippet R1-S2.)*

- **DEF002 · Definition** — **CPE.** "Cytopathic / cytopathogenic effect" is the morphologic change read
  in an inoculated monolayer as the primary indicator of viral presence in institutional guidance.
  *(Evidence: [VERIFIED src] ATCC, CLSI M41-A §7.4.2, ASM CPE protocols; Status: stipulated; Streams: R1, R3.)*

- **DEF003 · Definition** — **Maintenance medium.** The post-growth / infection-stage medium, typically lower
  in serum/enrichment than growth medium (institutional recipes use 1–3%, commonly 2% FBS).
  *(Evidence: [VERIFIED src] CLSI M41-A §5.4.1; Status: stipulated; Streams: R1, R4.)*

- **DEF004 · Definition** — **Negative-control tiers A–D.** A = Isolation-stage mock in matched maintenance
  medium; B = named but match unverifiable; C = wrong stage and/or explicit mismatch; D = none described.
  *(Evidence: house framework `r2_negative_controls/control-cultures.md`; Status: stipulated; Stream: R2.)*

- **DEF005 · Definition** — **Assembly fragility.** *(Short)* The deposited "complete genome" was built wrong.
  *(Long)* The published full-genome assembly of a named, culture-derived type material is later shown incorrect
  or incomplete — a missing gene-containing segment (CMV AD169 absent 929 bp affecting UL42/UL43), accumulated
  sequencing errors (HPV16, human adenovirus 17, AAV2, the adenovirus "four errors" corrected by Jung 1991, the
  HVT frameshift), a mis-sized genome (FMDV O1K poly(C) length corrected 7802→~8450 nt), or a retracted
  infectious clone (measles Edmonston, Ballart 1990 retracted 1991) — and the correction is itself published, so
  the error is *detectable*, not hidden. *(Evidence: [VERIFIED src] A3 census
  `sequence_origins/P3_A3_census_2026-11-13.md`; Status: stipulated — taxonomy; Stream P3.)*

- **DEF006 · Definition** — **Stock drift.** *(Short)* The culture product itself is not a fixed object.
  *(Long)* When "the same" named stock / isolate is re-sequenced, or held and passaged in different laboratories,
  the biological material has itself diverged — through passage and adaptation (CMV AD169 high-passage vs
  low-passage Merlin), lab-to-lab drift (AD169 varUC vs ATCC holdings), culture adaptation (HAV HM-175 wild-type
  vs cell-adapted attenuated), or residual population heterogeneity (MDV CVI988 consensus differing at 236
  positions / 13 ORFs across three holdings; Ad2 "heterogeneity persists after plaque purification") — so
  independent sequences differ because the stock drifted, not because a data-handling step failed. The "reference
  genome" is therefore a passage-drifted, lab-specific snapshot, not a stable natural identifier — a process
  critique, not a "virus is broken" claim. *(Evidence: [VERIFIED src] A3 census
  `sequence_origins/P3_A3_census_2026-11-13.md`; Status: stipulated — taxonomy; Stream P3.)*

## Axioms (premises / scope)

- **AX010 · Axiom** — **Pipeline scope.** The argument is bounded to the classical
  *culture → CPE → purify → name particles → sequence* pipeline; it does not claim anything about
  other detection routes or about etiology as a whole.
  *(Evidence: —; Status: assumed; Streams: all.)*

- **AX011 · Axiom** — **Non-specificity is not non-existence.** Showing that CPE under Isolation conditions
  is not a virus-specific detector does not assert that "nothing infectious exists" in any system.
  *(Evidence: —; Status: assumed; Streams: all.)*

- **AX012 · Axiom** — **Scope exclusions.** HIV and phage are out of scope for the particle/sequence
  ontology arms; nucleic-acid existence is taken as given for the P3 arm.
  *(Evidence: `P4_P7_index.md` rules; Status: assumed; Streams: P2–P7.)*

## Observations (empirical facts)

- **OB020 · Observation** — **Dual-FBS corpus is modal 10% → 2%.** Across the 189-row Isolation corpus,
  169 papers state numeric pre- and post-inoculation serum and are plotted: pre-inoculation serum is
  modal 10% (139/169), post-inoculation modal 2% (113/169), with medians 10.0% and 2.0% and means
  9.30% and 2.24%. *(Evidence: [FIGURE] `r1_…/isolation-refs.csv`, `fbs_distribution_plots/fbs_distribution_summary.txt`;
  Status: established; Stream: R1.)*

- **OB021 · Observation** — **Guidelines overlay at ~10% → ~2%.** Eight institutional recipes with parseable
  dual percentages cluster at the same growth→maintenance split (about 10% to about 2%).
  *(Evidence: [VERIFIED src] quotes in `tex/DRAFT.md`; Status: established; Stream: R1.)*

- **OB022 · Observation** — **Same step, different stated reasons.** The guidelines that prescribe a serum
  step-down at inoculation agree on the target but not the rationale: ATCC cites interference with
  attachment; CLSI cites cell viability, slower overgrowth, and serum-borne inhibitors; WHO EPI and the
  CDC Vero/hSLAM protocol cite overgrowth control ("to prevent overgrowth"; WHO adds "if cells are
  overgrown, virus isolation will be unsuccessful"); ASM, NEADL, WOAH, Health Canada/CCDR, and APHIS SAM
  104.04 give none. Two on-disk protocols that do not step down serum (WNV protocols.io 5%→5% hold;
  ANSES FMDV 0% post-inoculation) and one non-Isolation master-seed protocol (VIRPRO1013, R4) are
  excluded from the step-down set.
  *(Evidence: [VERIFIED src] `r1_…/institution-guideline-protocol-refs.md` "Rationale / justification for the serum
  drop at inoculation — verbatim audit (2026-11-14)"; table `tex/tables/rationale.tex`; Status: established; Stream: R1.)*

- **OB023 · Observation** — **Matched-medium controls are rare.** Of the scored Isolation-paper rows
  (~173), 11 are Tier A (matched-maintenance mock), 38 Tier B (match unverifiable), 14 Tier C (wrong
  stage/mismatch), 110 Tier D (none described). No Tier A paper reports CPE in its negative control.
  *(Evidence: [VERIFIED corpus] `r2_…/control-cultures-overview.csv`; Status: established; Stream: R2.
  Canonical pass = 173 rows (A/B/C/D 11/38/14/110).)*

- **OB024 · Observation** — **CRO medium-only effect (A vs B).** On the 22 CRO-described frames, CPE-type
  terms were named on 1 of 9 Culture A (10% FBS) and 10 of 13 Culture B (2% FBS) frames; Culture B's
  terms include rounded (8), dying cells (7), granularity (6), vacuolation (4), detached (2), refractile (1).
  *(Evidence: [SUPPLIER]/[IN-HOUSE] CRO descriptions; Status: established; Stream: R3.)*

- **OB025 · Observation** — **Blinded raters score more CPE on B.** IR1 mean CPE-item sums 0.87 (A) vs
  1.65 (B); IR2 2.41 (A) vs 4.91 (B). Item-level feature agreement is low even where direction agrees.
  *(Evidence: [IN-HOUSE] `r3_…/ir-results/`; Status: established; Stream: R3.)*

- **OB026 · Observation** — **A non-Isolation protocol holds or raises serum.** USDA APHIS VIRPRO1013
  (master-seed extraneous-agent testing) prescribes growth 5–10% serum → later 5–20%, i.e. serum held or
  raised rather than stepped down; most other regulators leave serum % unspecified. The 5–20% number lives
  in the internal *protocol* only — the implementing regulation 9 CFR 113.55/113.46 is serum-silent — and
  APHIS supplies **no stated rationale** for the hold-or-increase pattern.
  *(Evidence: [VERIFIED src] VIRPRO1013/SAM312; 9 CFR 113.55 & 113.46 (eCFR, read 2026-11-14);
  `r4_…/wrk/VIRPRO1013_analogs.md`, `r4_…/refs/_notes/R4_VIRPRO1013_SAM312_extraction_notes.md`;
  Status: established; Stream: R4.)*

- **OB027 · Observation** — **Isolation EQA reports sensitivity spread and control heterogeneity.** In the
  first WHO National Influenza Centre cell-culture Isolation EQA (n=21) the lowest-titre samples were isolated
  by only 52–62% of laboratories while high-titre samples were isolated by ≥90%, and 2 of 21 laboratories
  reported a positive Isolation result on a virus-free negative sample; within the same panel a negative
  Isolation control was used by only 16 of 21 laboratories and a positive control by only 12 of 21 (P7-003).
  In a 51-laboratory BVDV antibody ring trial four antibody-positive pooled milk samples were called negative
  in 43.6%, 50.9%, 3.6% and 56.4% of investigations, tracking ELISA-kit choice and incubation protocol
  (P7-007).
  *(Evidence: [VERIFIED src] P7-003 Reading 2017, P7-007 Wernike & Beer 2022; Status: established-scoped —
  two panels; Stream: P7.)*

- **OB028 · Observation** — **Origin/type genome deposits are predominantly culture-derived.** The Step 1
  genome-origin census (102 origin/confirmation events, all `chain_closed`, 0 open) finds 82 of 102 (80%)
  deposit events document culture-propagated sample production — 37 (36%) with a culture+CPE/plaque/syncytia
  warrant, 45 (44%) culture without stated CPE — versus 11 (11%) clinical-direct and 9 (9%) other
  (eggs/animal/synthetic). Coding used a documentary soft bar (method↔deposit within reasonable doubt) and
  passed a quality audit (0 of 24 re-read borderlines re-scored). This is the census premise that justifies
  looking for downstream ambiguity in the viral-genetics literature (OB150). *(Evidence: [VERIFIED src]
  `p3_genetics/sequence_origins/P3_sequence_origin_events.csv`, `P3_step1_path_type_map_2026-09-21.md`;
  Status: established-scoped — documentary census of 102 events, not a random taxonomy sample; Stream P3.)*

- **OB080 · Observation** — **The Isolation/titration endpoint is the least reproducible of the methods
  compared.** Across the first-class Isolation/titration panels that reported both a cell-culture endpoint and
  a molecular (qPCR/RT-PCR) or antigen comparator on the same known-positive material, the cell-culture
  endpoint is the least sensitive and most variable. The decisive un-blinded case (P7-008, Olesen 2022): qPCR
  0.96–1.0 while cell-culture infectivity reached only 0.68–0.90 — an unblinded lab reproduces the genetic
  readout yet fails the cell-culture readout, so the asymmetry is not an artifact of blinding; the two
  explicitly blinded panels still show the same direction. *(Follows from OB027; Evidence: [VERIFIED src]
  P7-001, P7-003, P7-004, P7-008, P7-018 (`OB080.csv` / `OB080.md`); Status: established-scoped — first-class
  Isolation/titration panels; Stream: P7. Detection is one side of the genetics toolchain; the assembly half is
  CNJ151's separate seam.)*

- **OB081 · Observation** — **Concordance is endpoint-dependent: relative fold-drops are reproducible,
  absolute titre magnitude is not.** In a 15-laboratory SARS-CoV-2 antigenicity comparison (P7-010, Brangel
  2024) titre magnitude varied ~9-fold across labs while relative fold-drops were consistent. *(Follows from
  OB027; Evidence: [VERIFIED src] P7-010; Status: established-scoped — one multi-lab panel; Stream: P7.)*

- **OB082 · Observation** — **The CRO cultures never reached confluence.** In the serum-only CRO experiment
  (Vero E6, no inoculum; Culture A 10% FBS, Culture B 2% FBS; 5-day window), neither culture exceeded ~80%
  confluence, so the CPE-classified morphology reported (OB024/OB025) arose in **sub-confluent** monolayers and
  cannot be attributed to post-confluent degeneration / contact-inhibition death. This removes R6-M3 as an
  explanation of the CRO result and strengthens the serum/nutrient-withdrawal mechanisms (R6-M1/R6-M2).
  *(Evidence: [SUPPLIER]/[IN-HOUSE] project-owner correction to the CRO record, 2026-11-17; Status:
  established-scoped — one cell line, two cultures; Streams R3, R6.)*

## Lemmas (supporting established findings)

- **LM030 · Lemma** — **Practice follows the recipe.** Published Isolation methods largely reproduce the
  dual-serum step-down codified in institutional guidance. *(Follows from OB020, OB021; Streams R1.)*

- **LM031 · Lemma** — **Audit-able controls are the exception.** Isolation publications typically do not
  describe an Isolation-stage mock in matched maintenance medium. *(Follows from OB023; Stream R2.)*

- **LM032 · Lemma** — **The step is justified heterogeneously.** Because the stated rationales for the serum
  step are inconsistent and partly absent (OB022), the practice reads as empirically locked for readable
  CPE/Isolates rather than grounded in one shared, tested mechanism. *(Follows from OB022; Streams R1, P1.)*

- **LM033 · Lemma** — **No serum-alone founding experiment (history).** Dual growth/maintenance media were
  mid-century practice (1953–54 primaries) and were codified (~2% FBS) in manuals such as Schmidt 1969;
  the published record shows no foundational experiment that varied serum alone on matched uninoculated
  monolayers to establish CPE specificity under Isolation conditions.
  *(Follows from P1 sources; Evidence: [VERIFIED src] `p1_history/P1_synthesis.md`, `P1_for_paper.md`; Stream P1.)*

- **LM034 · Lemma** — **Detection is deterministic but non-specific.** The molecular *detection* layer of
  viral genetics (PCR/qPCR/RT-PCR) is reproducible across laboratories even when blinded (OB080: P7-008
  unblinded qPCR 0.96–1.0 vs infectivity 0.68–0.90; P7-014 blinded RT-qPCR near-perfect), but it is
  *primer-driven* — it amplifies whatever nucleic acid matches the primers (viral, host, bovine, or reagent).
  Reproducible detection does not itself earn the "viral" label of the detected sequence. *(Follows from OB080;
  Status: established-scoped; Streams P3, P7.)*

- **LM035 · Lemma** — **APHIS is consistent at adsorption, silent at observation.** In VIRPRO1013 the serum
  *reduction* at adsorption (§4.1.5, "Discard inoculum … to reduce serum toxicity") is the same move and the
  same rationale virology uses in Isolation — serum is held to inhibit viral uptake, so it is stripped at that
  step. The **divergence is at the CPE-observation stage**: Isolation steps maintenance serum *down* (~2%)
  while VIRPRO1013 *holds or raises* it (5–20%, OB026), and VIRPRO1013 gives a rationale for serum at
  adsorption but **none for serum during CPE observation**. Because TH040 shows serum level is the causal
  variable producing CPE-classified morphology, the two protocols hold the "CPE" readout constant while
  moving that variable in opposite directions. *(Follows from OB026, TH040, DEF003; Evidence: [VERIFIED src]
  VIRPRO1013 §4.1.5/§2.2.10/§4.1.7, `r4_…/refs/_notes/R4_VIRPRO1013_SAM312_extraction_notes.md`,
  `r4_…/r4.md` §§ Interpretation; Status: established; Stream: R4.)*

## Theorem

- **TH040 · Theorem** — **The serum step-down alone drives CPE-classified morphology.** Under standard
  dual-medium Isolation conditions, lowering FBS from 10% to 2% in uninoculated Vero E6 cultures produces
  morphology that the contract laboratory and two blinded independent raters describe as CPE-type.
  *(Follows from OB024, OB025; Evidence: [IN-HOUSE]/[SUPPLIER]; Status: established-scoped — one cell line,
  one laboratory, two cultures; Stream R3.)*

## Corollaries

- **CRL041 · Corollary** — **CPE is not inoculum-specific under dual-medium conditions.** Because the
  Isolation culture varies inoculum and serum at once (DEF001, DEF003) and the serum step alone yields
  CPE-classified morphology (TH040), CPE read under those conditions cannot by itself be attributed to the
  inoculum. *(Follows from TH040, DEF001, DEF003.)*

- **CRL042 · Corollary** — **CPE-based detection/titration is not standalone proof of a viral agent.**
  Non-specificity of the CPE endpoint (CRL041), combined with the rarity of the control that
  would separate serum from inoculum (LM031), means CPE-based Isolation/titer is not valid on its own as
  proof of a discrete viral agent in culture. *(Follows from CRL041, LM031.)*

- **CRL043 · Corollary** — **The required control is a matched-maintenance mock.** A proper negative control
  for Isolation is a culture taken through the same maintenance/serum step with no inoculum; reporting
  standards for Isolation should make that control explicit. *(Follows from CRL041, LM031, DEF004.)*

## Conjectures (predictions, P arms)

- **CNJ050 · Conjecture** — **Hinge.** If culture/CPE endpoints do not uniquely identify a particle class,
  then physical overlap between extracellular vesicles and purported virions is an expected literature
  pattern to examine. *(Working hypothesis for discussion, not a result; follows from CRL041.)*

- **CNJ051 · Conjecture (P1)** — **History tracks operability, not mechanism.** Dual-medium protocols
  developed quickly after cell culture became the Isolation tool in part so the procedure yields the
  positive CPE endpoint associated with viral presence; the published history should show serum-practice
  change tracking culture operability rather than a shared mechanistic justification.
  *(Predicted; supported by LM033 but not settled; Streams P1.)*

- **CNJ052 · Conjecture (P2)** — **Purification will not restore dualism.** Purification/EM of culture
  products will not provide a method that uniquely separates extracellular vesicles from "virions" by
  physical parameters alone; the EV literature's indistinguishability reports are the expected pattern.
  *(Predicted; follows from CNJ050; Evidence: [VERIFIED src] P2 corpus `p2_…/P2_screened.csv` n=97,
  `P2_useful.csv` n=57 — non-retrovirus primaries (KSHV P2-084; influenza A SXC P2-085; rotavirus P2-089
  / Santiana P2-094; dengue P2-096; SARS-CoV-2 P2-090), pre-1997 historical primaries (P2-081/082/083/086,
  1954–1972), and
  naked-virus EV enclosure + separation caveat (P2-093/095, 2018–2026); bounds: CD63 affinity (P2-084) and
  adapted Ficoll (P2-088) separate conditionally, cf. ADVR061. Streams P2.)*

- **CNJ053 · Conjecture (P3)** — **Genome claims inherit the endpoint.** Sequence/database claims that rest
  on CPE-defined Isolates inherit the under-determination of the endpoint that declared them positive.
  *(Predicted; supported by OB028; Streams P3.)*

- **CNJ054 · Conjecture (P4)** — **Serology/antigen provenance inherits.** Antigen/serology reference
  reagents and kit-insert provenance that trace to Isolation-linked culture inherit the same
  under-determination risk. *(Predicted; Streams P4.)*

- **CNJ055 · Conjecture (P5)** — **Structure pipelines inherit the label.** Cryo-EM/structure work built on
  Isolation-defined stocks inherits the under-determined particle label it purports to resolve.
  *(Predicted; Streams P5.)*

- **CNJ056 · Conjecture (P6)** — **Seed identity is process ontology.** Vaccine master-seed identity, as
  publicly specified, is a regulated culture-process bundle continuous with Isolation practice rather than
  a uniquely grounded natural particle independent of that process. *(Predicted; explicit non-goal: this is
  process description, not a safety/efficacy/uptake claim.)*

- **CNJ057 · Conjecture (P7)** — **Repeatability reproduces the process.** Cross-lab replication reproduces
  the shared culture process, not an observationally unique particle; inter-lab agreement is therefore
  weak evidence of particle identity on its own. *(Follows from OB027; Status: predicted — supported by the
  first-class P7 corpus (OB027/OB080), not established; the "weaken" condition — stability under deliberate
  serum/matrix variation with Tier-A controls — remains untested. Stream P7.)*

- **CNJ058 · Conjecture (R5)** — **Pre-cell-culture methods were failing their own era's tests, not quietly
  validated.** Across the 1920s–1940s literature, the means by which a virus was detected, bulk-grown, purified,
  and "imaged" before cell culture were repeatedly documented as corrigible, unreliable, or correlational rather
  than demonstrative: Stanley's 1935 "crystalline protein" was corrected within a year to a liquid-crystalline
  nucleoprotein (Bawden, Pirie, Bernal & Fankuchen 1936); "purified" influenza from eggs co-purified with a normal
  allantoic-fluid component sharing serological reactivity with the virus (Friedewald 1944); the settled negative
  that poliovirus would not grow outside nervous tissue (Sabin & Olitsky 1936) was overturned in 1949; and the
  egg/animal route lacked a live readout and could not grow viruses lacking that host. CNJ058 predicts the record
  will show **recognized defects and reversals** (not silence) motivating the cell-culture transition — that cell
  culture was adopted as a *supposedly better* method amid documented dissatisfaction with its predecessors,
  rather than as a merely cheaper replacement of validated techniques. *(Follows from none — a standalone
  empirical prediction; Status: predicted; tested by the R5-B evidence audit + a documentation survey of the
  1920–1950 methods literature. Reject if the record instead shows the prior methods were held adequate and
  adoption was driven purely by cost/convenience. Stream R5.)*

- **CNJ059 · Conjecture (R6)** — **A generic stress/death pathway suffices to produce CPE-classified morphology
  and plaque-like clearing.** Under the working assumption that the inoculation step adds no virus, the
  morphology the field reads as "CPE" and the countable zones it reads as "plaques" are produced by a small set
  of generic, non-viral cell-biological pathways — abrupt serum/growth-factor withdrawal (→ mitochondrial
  apoptosis), nutrient/glucose depletion (the same Bax/mitochondrial/cytochrome-*c* program), post-confluent
  degeneration, metabolic-waste/pH drift, anoikis, paracrine/bystander death waves, contaminant, and
  overlay-dependent diffusion limitation — each carrying a distinguishing prediction (time-course, serum-dose
  dependence, focal-vs-uniform, reversibility, overlay composition) testable against the CRO/Zenodo record and
  the CLSI M41 Table 7 descriptor set. The "one plaque = one infectious particle" step is thereby re-read as an
  *inference from dilution-linearity + co-variance*, not a pattern-uniqueness proof: Dulbecco (1952) secured it by
  plaque count linear in virus concentration ("a linear dependence … can be obtained only if each plaque is
  produced by one virus particle"), absence in an uninoculated control, antiserum suppression, and an ~1:1
  plaque:egg-infectivity correspondence — evidence that plaques are seeded by a discrete unit coupled to the
  presumed-infectious inoculum, not that a focal clearing in a stressed monolayer has no non-viral producer.
  Abedon & Yin (2009) add the decisive generic fact: "plaque formation failure is not necessarily equivalent to
  virion inviability." *(Follows from TH040, CRL041, OB082; Status: predicted — mechanism framework drafted
  `r6_nonviral_morphology_mechanisms/R6_mechanisms.md` (R6-M1…R6-M12) with `[VERIFIED src]` anchors: Vander
  Heiden 2001 + Quesney 2001 + Mendonça 2009 (M1/M2, serum/nutrient → apoptosis), Ammerman 2008 (M3, which OB082
  removes as a CRO explanation), and Fenner ch.3 + Dulbecco 1952 + Abedon & Yin 2009 (M11, the plaque step);
  OB082 records that neither CRO culture exceeded ~80% confluence; M5 (bystander wave) still `[DATA REQUIRED]`.
  Stream R6.)*

- **OB150 · Observation (P3)** — **Under-determination is detectable in the viral-genetics literature.**
  The published viral-genetics literature already contains — scattered and often framed as technical noise —
  exactly the ambiguity that CNJ053 + OB028 predict, and the field itself documented and corrected it. In
  multiple differently-caused forms, across many virus families, the deposited "reference genome" of a named,
  culture-derived stock is repeatedly shown to be non-unique, wrong, or a single haplotype of a mixed
  population: *assembly fragility* (DEF005 — e.g. CMV AD169 missing 929 bp; HPV16/HPV18 reference-clone
  sequencing errors corrected, HPV-16R a composite no isolate matches; the PRV reference genome assembled
  from six strains; HSV-1/KOS repeat tracts "artificially matched" to strain 17) and *stock drift* (DEF006 —
  HSV-1 McKrae ≥2 variant strains; HSV-1 KOS63/KOS79 "genetically unrelated"; CSFV "Alfort" 86.2% identity
  name-collision; passage accumulating gE deletion + frameshifts). The A3 same-stock census is **27 divergent /
  0 unclear / 1 clean across 28 named-stock pairs**, plus the database-wide contamination counts (Chen 2022,
  Astashyn 2024) and three canonical de-discovery retractions (XMRV, MLV-CFS, PHV — the un-retracted
  de-discovery papers carry the load). This is an *existence* claim ("detectable, multi-form, across many
  families"), **not a rate**: the census is a biased literature retrospective (clean confirmations are
  unpublished), so it cannot say "how often" re-sequencing diverges. Adversarial balance is held visible — the
  one clean re-sequencing (Seto 2010, HAdV-C5 stable across 45 years) and Pyöriä 2024 (single dominant strains
  in healthy individuals) bound the claim. *(Follows from CNJ053, OB028; Evidence: [VERIFIED src] A3 census
  `sequence_origins/P3_A3_census_2026-11-13.md`, `P3_CNJ150_strong_signal_expansion_2026-11-14.md`,
  `P3_CNJ150_ambiguity_search_2026-11-12.md`; Status: established-scoped — existence, not prevalence; Stream P3.)*

- **CNJ151 · Conjecture (P3)** — **Viral genetics is non-deterministic in ways that absorb the ambiguity.**
  If the literature does not cleanly show OB150, the fallback is that the subfield's machinery —
  reference-prior-driven assembly and classification, consensus-sequence construction from
  passage/quasispecies, and database labels stored as ontology — is non-deterministic enough to paper over
  the ambiguity that CNJ053 + OB028 would otherwise make visible. OB150 and CNJ151 are a disjunction of
  outcomes to seek, not two independent predictions. *(Follows from CNJ053, OB028; Status: rejected
  2026-11-12 — the *detection* layer of viral genetics is reproducible even blinded (OB080: P7-008 unblinded
  qPCR 0.96–1.0 vs infectivity 0.68–0.90; P7-014 blinded RT-qPCR near-perfect to 1:10⁴, ELISA 100%), so
  "viral genetics is non-deterministic" is falsified at the detection layer. The *assembly* layer is
  non-deterministic (A3: corrections, retractions, size-corrections of culture-derived reference genomes),
  but that non-determinism is *detectable* — published as corrections/retractions — so it is OB150
  evidence, not CNJ151 (which claimed non-determinism *papers over* the ambiguity). The thread therefore
  looks only for OB150. Stream P3.)*

## Counterexamples (adversarial balance)

- **ADVR060 · Counterexample** — **Not all practice steps serum down.** Non-Isolation protocols such as
  VIRPRO1013 hold or raise serum (OB026), so the low-serum confound measured in TH040 applies to the
  published-recipe setting, not uniformly to all cell-culture practice. *(Follows from OB026.)*

- **ADVR061 · Counterexample** — **Separation is forceable under specific methods.** Tang et al. 2017 report
  single-particle separation of retrovirus-like particles from small EVs by nanoscale flow cytometry with a
  fluorescent envelope marker, while acknowledging general biochemical indistinguishability; this bounds
  the P2 claim (CNJ052) to standard/untargeted methods. *(Evidence: [VERIFIED src] P2-071; Streams P2.)*

- **ADVR062 · Counterexample** — **No Tier A control falsified its test culture.** Even among the 11 Tier A
  papers, none reported CPE in the matched-milieu negative control (OB023); this is a nil counter to the
  concern and is reported as such. *(Follows from OB023.)*

---

## Dependency index (build order)

```mermaid
flowchart TD
    subgraph terms["Definitions"]
        DEF001["DEF001 Isolation"]
        DEF003["DEF003 maintenance medium"]
    end
    subgraph obs["Observations"]
        OB020["OB020 corpus modal 10 to 2"]
        OB022["OB022 same step different reasons"]
        OB023["OB023 matched controls rare"]
        OB024["OB024 CRO A vs B"]
        OB025["OB025 raters: B greater than A"]
        OB026["OB026 VIRPRO holds serum"]
        OB028["OB028 deposits culture-derived"]
        OB080["OB080 isolation/titration least reproducible"]
        OB150["OB150 underdetermination detectable in viral-genetics lit"]
    end
    subgraph lem["Lemmas"]
        LM030["LM030 practice follows recipe"]
        LM031["LM031 audit-able controls rare"]
        LM032["LM032 step justified heterogeneously"]
        LM033["LM033 no serum-alone founding experiment"]
        LM034["LM034 detection deterministic non-specific"]
        LM035["LM035 APHIS consistent at adsorption silent at observation"]
    end
    subgraph thm["Theorem"]
        TH040["TH040 serum step-down drives CPE morphology"]
    end
    subgraph cor["Corollaries"]
        CRL041["CRL041 CPE not inoculum-specific"]
        CRL042["CRL042 not standalone proof"]
        CRL043["CRL043 matched-maintenance mock required"]
    end
    subgraph con["Conjectures (P arms)"]
        CNJ050["CNJ050 hinge"]
        CNJ051["CNJ051 P1 history"]
        CNJ052["CNJ052 P2 purification"]
        CNJ053["CNJ053 P3 genome"]
        CNJ054["CNJ054 P4 serology"]
        CNJ055["CNJ055 P5 structure"]
        CNJ056["CNJ056 P6 seed"]
        CNJ057["CNJ057 P7 repeatability"]
        CNJ058["CNJ058 R5 pre-cell methods documented-error-prone"]
        CNJ059["CNJ059 R6 non-viral mechanisms suffice"]
        CNJ151["CNJ151 non-determinism absorbs REJECTED"]
    end
    subgraph cx["Counterexamples"]
        ADVR060["ADVR060 not all practice steps down"]
        ADVR061["ADVR061 separation forceable"]
        ADVR062["ADVR062 no Tier A falsified"]
    end

    DEF001 --> CRL041
    DEF003 --> CRL041
    OB020 --> LM030
    OB022 --> LM032
    OB023 --> LM031
    OB024 --> TH040
    OB025 --> TH040
    TH040 --> CRL041
    LM031 --> CRL042
    CRL041 --> CRL042
    LM031 --> CRL043
    CRL041 --> CRL043
    LM033 --> CNJ051
    CNJ050 --> CNJ052
    CNJ050 --> CNJ053
    CNJ050 --> CNJ054
    CNJ050 --> CNJ055
    CNJ050 --> CNJ056
    CNJ050 --> CNJ057
    OB080 --> LM034
    OB028 --> CNJ053
    CNJ053 --> OB150
    OB028 --> OB150
    CNJ053 --> CNJ151
    OB080 --> CNJ151
    OB026 --> LM035
    TH040 --> LM035
    DEF003 --> LM035
    OB026 --> ADVR060
    OB023 --> ADVR062
    CNJ052 -.-> ADVR061
    TH040 --> CNJ059
    CRL041 --> CNJ059
```

## Rules of use

1. One registry (this file). Do not start a parallel claim-numbering system in a stream.
2. Evidence tags follow the house set in the global research instructions; a claim without an evidence tag
   is either an Axiom (allowed) or a bug.
3. Scope every observational claim explicitly ("under standard dual-medium Isolation conditions"; "in the
   sampled corpus"; "Vero E6, uninoculated").
4. Role codes only (CRO, IR1, IR2, IR3v). Never real names of raters, freelancers, or CRO staff.
5. If a number changes (corpus n, tier counts, rater sums), update the claim **and** bump the note in
   `tex/wrk/paper_notes.md`; do not leave a stale count in a claim.
6. When a Conjecture is upgraded by evidence, recast it as an Observation/Lemma and move its ID into that
   kind (keep the numeric portion stable; change prefix and status). A rejected Conjecture keeps its
   `CNJ` code and `Status: rejected`.
7. Diagrams use Mermaid per `CONVENTIONS.md`. Evidence tags, role codes, and file placement also follow
   `CONVENTIONS.md` — this file only owns the claims themselves.
8. **Recoding `C###` → kind-prefix is 1:1 on the numeric portion** (`C020`→`OB020`, `C040`→`TH040`,
   `C150`→`OB150`). Old `C###` references still grep correctly; update them when a stream is next touched.