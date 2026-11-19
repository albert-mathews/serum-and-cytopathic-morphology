# R6 — synthesis (freeze)

**Written:** 2026-11-19, after Round 2b extraction (23 sources read full-text `[VERIFIED src]`). This freezes the
mechanism framework and upgrades **CNJ059 → LM059** (Conjecture → Lemma; Status `predicted` → `established-scoped`).

**Scope and guardrail.** R6 develops the **no-virus explanation on its own terms** (AX011: non-specificity ≠
non-existence). It enumerates, from the cell-biology and negative-control literature, the generic non-viral pathways
by which an *uninoculated* monolayer can show the morphology the field reads as "CPE" and the countable clearing it
reads as "plaques" — each with a distinguishing prediction testable against the CRO/Zenodo record and the CLSI M41
Table 7 descriptor set. It does **not** state that no infectious agent exists, and it **never states or insinuates
that the CPE/plaque methods are validated.**

## 1. The anchor datum every mechanism must match

The serum-only CRO (Vero E6, **no inoculum**, Culture A 10% FBS vs Culture B 2% FBS, 5-day window) is the dataset:

- CPE-type terms named on **1/9** Culture A frames vs **10/13** Culture B frames; B's terms: rounded (8), dying
  cells (7), granularity (6), vacuolation (4), detached (2), refractile (1). `[SUPPLIER]/[IN-HOUSE]` (OB024)
- Two blinded raters score **more CPE in B than A** (IR1, IR2). `[IN-HOUSE]` (OB025)
- Neither culture exceeded **~80% confluence** → the CPE-classified morphology arose in a **sub-confluent** monolayer;
  post-confluent degeneration (R6-M3) is therefore **excluded as a CRO explanation** (OB082).

Consequent requirement: the leading mechanisms must predict *more rounded/dying/granular/vacuolated/detached
morphology in 2% than in 10% FBS within ~5 days, in a sub-confluent anchorage-dependent monkey epithelial line.*

## 2. What R6 did

A **mechanism survey** (not a particle census). Twelve candidates enumerated in `R6_mechanisms.md`
(R6-M1…M12), each with (a) a literature warrant and (b) a **distinguishing prediction**. 25 sources screened,
**23 read full-text `[VERIFIED src]`** (18 fetched PDFs + 5 open-access), 2 non-critical wishlist items remain
(R6-007 Nahapetian 1986; R6-014 Macpherson 1966 — M4/M8 already anchored elsewhere). Every mechanism row is recorded
in `R6_useful.csv` (extraction schema) and `R6_bibliography.md` (used) vs `R6_bibliography_unused.md`.

## 3. The twelve mechanisms, one line each

| Code | Mechanism | CRO/Zenodo distinguishing prediction |
|------|-----------|-------------------------------------|
| R6-M1 | Abrupt serum / growth-factor step-down → mitochondrial/Bax apoptosis | onset 1–3 d post-switch; dose-dependent on drop magnitude → B>A |
| R6-M2 | Nutrient / glucose / glutamine depletion → same apoptotic program | later onset; accelerates at density; acid medium colour |
| R6-M3 | Post-confluent degeneration | **excluded for CRO** by OB082 (retained as a generic mechanism) |
| R6-M4 | Metabolic waste / pH drift (lactate, NH₃) | correlates with medium colour; faster in lower-serum arm |
| R6-M5 | Paracrine/bystander **death wave** (ferroptosis + apoptosis propagation) | focal, radially expanding, adjacency gradient → "plaque" with no virus |
| R6-M6 | Anoikis / adhesion-loss → rounding + detachment | rounding precedes detachment; floating cells; re-adhesion rescue |
| R6-M7 | Freeze–thaw / desiccation / trauma at seeding | focal, **non-progressive**, not serum-dependent (nil control) |
| R6-M8 | Mycoplasma / contaminant | persistent across passage; PCR/Hoechst rule-out; no clean serum split |
| R6-M9 | Cell-line intrinsic instability (aneuploidy → foci) | baseline foci in healthy cultures; passage-dependent |
| R6-M10 | Starvation autophagy → vacuolation | vacuoles appear with starvation, reverse on re-feed → more in B |
| R6-M11 | Overlay diffusion limitation + overlay toxicity | size/border varies with overlay composition (agarose %, glucose) |
| R6-M12 | Osmotic / ionic stress | tied to a defined osmotic perturbation; absent in isosmolar control |

Mechanisms are **not competitors**: the serum step links M1/M2 → M10 (vacuolation) + M6 (detachment) → M5
(propagative death) into one chain (see §4).

## 4. The lead causal chain

> **serum step-down (M1) → ↓ cystine (system xc⁻) + ↓ lipophilic antioxidants → ↓ glutathione (GSH) →
> lipid peroxidation (ROS + iron) = ferroptosis-capable**; in parallel **↓ growth factors/nutrients (M2) →
> apoptosis / secondary necrosis (Vero)**, **starvation autophagy → vacuolation (M10)**, and **adhesion loss →
> detachment (M6)**, and detachment feeds the same ferroptotic pathway; the ferroptotic (and apoptotic) branch then
> **propagates as a self-sustaining wave (M5)** → focal / contiguous death = "CPE" / "plaque" **with no virus**.

Anchored `[VERIFIED src]`:
- Cystine/GSH/ferroptosis: Riegman 2019 (system xc⁻, GSH, ROS chain); R6-023 Linkermann 2014 (ferroptosis depends on
  system xc⁻/GSH/GPX4); R6-024 Kim 2016 (amino-acid deprivation + GSH depletion → ferroptosis, DFO/ferrostatins/GSH
  rescue); R6-026 Tang 2026 (starvation lowers the propagation threshold through declining GSH).
- Serum-free apoptosis/necrosis in Vero: R6-016 Quesney 2001; nutrient-depletion Vero morphology: R6-004 Mendonça 2009.
- Starvation autophagy (M10) and adhesion loss (M6) in Vero: R6-017 Peng 2026, R6-005 Genari 1998.

Under the no-virus premise this chain explains the CRO signature end-to-end: the 2% arm loses more
cystine/GSH/growth factors → more lipid-ROS/apoptosis/vacuolation/detachment → a focally seeded, propagating zone of
death — CPE-classified morphology with no viral particle required (OB024/OB025; OB082 sub-confluence).

## 5. The M5 wave step — now primary-backed at two spatial scales

- **Intracellular** (a discrete focus seeds a self-regenerating wave through one cell): R6-025 Pacher & Hajnóczky 2001
  (mitochondrial depolarisation/Ca²⁺ waves); R6-022 Garcia-Perez 2012 (Bid → cyto *c* release propagates as a
  ROS-relayed intermitochondrial wave); consolidated by R6-021 Cheng & Ferrell 2018 ("apoptosis typically initiates
  at a single discrete focus… and then spreads").
- **Intercellular** (a dying cell kills neighbours → tissue-scale front): R6-023 Linkermann 2014 ("direct cell-to-cell
  communication to deliver the deadly signal"; synchronized tubular necrosis); R6-024 Kim 2016 (ferroptosis
  "propagate[s] from cell to cell in a wave-like manner… unlike… apoptosis"); consolidated by R6-020 Riegman 2019 and
  R6-026 Tang 2026 (ROS trigger wave ~5.5 µm/min over >5 mm; membrane-contact and EV-paracrine relay modes).

All five primaries read in full; extracts in `_notes/R6-M5_ferroptosis_wave_primaries.md`.

## 6. The two framing points (load-bearing for the paper)

1. **"One plaque = one infectious particle" is an *inference from dilution-linearity + co-variance*, not a
   pattern-uniqueness proof.** Dulbecco (1952) secured it the only way the assay can — plaque count linear in virus
   concentration ("a linear dependence … can be obtained only if each plaque is produced by one virus particle"),
   absence in an uninoculated control, antiserum suppression, and an ~1:1 plaque:egg-infectivity correspondence
   `[VERIFIED src]`. The WNV protocol states the PFU count is what it is "theoretically" (R6-019). R6's point is
   precise: dilution-linearity proves *one discrete seeding unit per plaque*; the "viral" reading of that unit is
   supplied by the surrounding inoculum/infectivity warrant, not by the focal pattern, which has non-viral producers
   (R6-M5/M7/M9/M11). Dulbecco's "absent when the virus is absent" held under *his* conditions (chicken fibroblasts,
   adequate medium), not the low-serum maintenance step that is this paper's confound.
2. **Focal clearing is a generic diffusion-/contact-limited spatial pattern.** Abedon & Yin (2009): plaque size is set
   by a "hindered diffusion constant," agar density, and nutrient/waste diffusion; "plaque formation failure is not
   necessarily equivalent to virion inviability." Oaks et al. (1985): a bacterial plaque's diameter is set by overlay
   glucose (MEM vs DMEM) — plaque size is medium-controlled even for a bona fide replicator.

## 7. What R6 establishes — and what it does not

**Establishes (LM059, scoped).** Under the no-virus premise, a generic non-viral stress/death pathway *suffices* to
reproduce CPE-classified morphology and plaque-like clearing, each mechanism testable by a distinguishing prediction;
the death-wave step is primary-backed; the "one particle = one plaque" step is re-read as an inference, not a
pattern-uniqueness proof.

**Does not establish.** (i) That no infectious agent exists (AX011) — R6 assumes its negation and develops the
consequence. (ii) That these mechanisms *in fact* produced the CRO's exact frames — R6 supplies the mechanisms and
their predictions, not a re-run of the CRO. (iii) That any CPE/plaque method is validated. (iv) A Vero-specific
wet demonstration of the wave step in the CRO's own sub-confluent serum-drop geometry (the wave literature is
confluence-rich; see §8).

## 8. Adversarial balance (conditions under which R6 looks wrong)

- The wave-front geometry is **best-documented in confluent monolayers** (Tang 2026), whereas the CRO was ~80%
  sub-confluent; R6-M5's CRO relevance therefore leans on the **serum-dose (2% vs 10%) differential** + the
  M1/M2 metabolic trigger, not on confluency per se.
- Tang 2026: **spatial clustering ≠ causal transmission** — "cells occupying the same microenvironment may simply be
  exposed to a shared upstream insult"; true propagation needs a spatially-defined initiation site, mechanistic
  continuity, and ferroptosis specificity. This is the discipline R6 applies, not a fatal objection.
- R6-M3 is excluded *for the CRO* (OB082); R6-M8 (contaminant) cannot by itself produce a clean serum-dose A/B split
  from one stock split into two arms.
- The no-virus reading **fails** if the CRO/Zenodo record showed foci that (a) expand at virus-like replication
  kinetics with no metabolic handle, (b) appear serum-independently, and (c) pass to fresh cells while contaminant is
  ruled out — none of which is currently in the record.

## 9. Paper integration

- Backs **TH040 / CRL041 / CRL042** at the mechanism level (the *why* behind "CPE is not inoculum-specific").
- Supplies the Discussion's mechanism table and the two framing points (plaque step; generic focal pattern).
- Registers **LM059** (was CNJ059) in `CLAIMS.md`; the paper cites the claim code, not this file.

## 10. Open items (not blocking the freeze)

1. Confirm peer-review status of R6-004 (ResearchGate DOI copy) before any load-bearing use.
2. Optional non-critical fetch: R6-007 (Nahapetian 1986, M4), R6-014 (Macpherson 1966, M8).
3. Optional depth: a Vero sub-confluent serum-step time-course to test R6-M5 in the CRO's exact geometry (a wet
   follow-on, not needed for the mechanism claim).

## Revision log

| Version | Date | Change |
|---------|------|--------|
| v0.1 | 2026-11-19 | Freeze after Round 2b; 23 sources read; M5 primary-backed; CNJ059 → LM059. |
