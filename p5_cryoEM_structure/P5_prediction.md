# P5 prediction — Cryo-EM / structure under culture-derived particle sets

**Status:** Formalized, **not started**.

## One-sentence prediction

If the particles entered into cryo-EM / tomography / “virus structure” pipelines are purified from **culture + CPE Isolates** (or from supernatants under Isolation maintenance), then high-resolution maps and symmetry models can **beautifully describe a culture-product particle class** without independently proving that Isolation CPE was a virus-specific detector—or that the imaged class is cleanly separated from EVs and other co-purifying particles (P2).

## Motivation from CPE non-specificity

Structural biology often begins after Isolation has already defined the object: grow, wait for CPE, purify, image. Resolution and model quality answer “what does this preparation look like?” They do not automatically answer “was the Isolation warrant specific?” P2’s co-purification problem remains unless class-separating biochemistry is shown on the **same** prep.

## Empirical tests

1. **Upstream warrant coding:** For landmark virus cryo-EM papers, score: culture vs clinical source; CPE/plaque used; serum/maintenance; particle-separation method vs EV markers; whether uninfected matched purifications were imaged.
2. **EV / mixed-particle controls:** Cases where EV-enriched fractions produce ordered or virus-like projections under similar pipelines.
3. **Heterogeneity reports:** Papers that acknowledge pleomorphic / damaged / “contaminant” particles in the same grids used for reconstruction—map how often those are dismissed vs modeled.
4. **Clinical-direct particle imaging:** Adversarial set where structure claims avoid culture; still score classification references (P3) and infectivity method if claimed.

## What would strengthen / weaken

| Result pattern | Reading |
|----------------|---------|
| Landmark structures almost all culture-Isolate upstream; rare matched uninfected imaging | Strengthens “structure inherits Isolation object” |
| Same morphology in matched uninfected purifications | Strengthens non-specificity / co-purification |
| Clinical particles with class-separating markers + non-culture functional assay | Weakens for those entries; keep hard cases |

## Non-goals

- Not anti-cryo-EM or anti-structural biology.
- Not a claim that maps are fabricated; scoped to **object selection and Isolation upstream**.
- Phage / HIV ontology expansion out of scope unless a row is needed for adversarial balance (default: skip).

## Links

- **P2:** Particle class overlap / purification.
- **R1–R2:** How Isolates are made and controlled.
- **P3:** Genomes often from same culture products that feed structure pipelines.
- **P7:** Cross-lab repeatability of particle prep + imaging claims.

## Deliverables when started

p5.md; worksheet of landmark structures with upstream warrant codes; Discussion snippet only if particle ontology is in paper scope.

## Worked example sketch (upstream warrant for a structure paper)

For each landmark cryo-EM / helical / icosahedral “virus structure” paper:

1. **Particle source:** named Isolate / supernatant / clinical fluid.  
2. **Isolation endpoint used upstream:** CPE, plaque, focus assay, PCR-only, unspecified.  
3. **Culture conditions:** cell line; growth vs maintenance serum if stated (R1 link).  
4. **Purification:** ultracentrifugation, gradient, chromatography, affinity; any EV-marker discussion (P2).  
5. **Uninfected matched purification imaged?** yes / no / unclear.  
6. **Selection for reconstruction:** how particles were picked; what was discarded as damaged/contaminant.  
7. **Functional claim attached to the map:** infectivity of the same prep? If infectivity = culture titer, note culture foundation.

**Prediction detail:** Maps can be correct descriptions of the imaged ensemble and still leave the Isolation warrant untouched. The interesting empirical object is the **rate** at which structure pipelines disclose matched uninfected controls and EV-overlap tests—not whether Fourier shell correlation is high.

## Detailed strengthen / weaken scenarios

**Strengthen.** Frequent absence of uninfected grids; purification recipes that match EV enrichment; authors noting “virus-like” particles in controls or mock gradients; structures of particles from Isolates whose genomes are culture_cpe type paths (P3).

**Weaken.** Clinical fluid particles with independent biochemistry (unique proteome not explained by host/EV databases) plus a non-culture functional assay; deliberate imaging of matched uninfected preps showing absence of the reconstructed class.

**Ambiguous.** In vitro assembly from recombinants: powerful chemistry, still often seeded by culture-derived sequence ontology. Code separately from Isolation-supernatant imaging.

## Sampling plan

- ICTV exemplar / textbook structures (finite list).  
- Recent high-impact cryo-ET of “infected” cells—score whether CPE/serum conditions are described.  
- EV cryo-EM papers as contrast class (not to merge labels, but to compare purification language).

## Relation to paper drafting

Default: **park**. One Discussion sentence only if particle ontology is already in scope via P2. Do not imply that unresolved Isolation specificity falsifies a density map.

## Open questions

- Include tomograms of infected cells without purified particles?  
- How hard to push on “contaminant” particle mentions in supplements?

## Why structure papers feel decisive (and what they decide)

High-resolution maps persuade because they look like ground truth. Under this prediction they are ground truth about **the prepared ensemble**, not automatic ground truth about Isolation specificity. A correct asymmetric unit can still sit atop a culture+CPE object selection step that R1–R2 show is recipe-heavy and often weakly controlled. P5’s job is to keep those layers separate in coding: reconstruction quality ≠ warrant quality.

Operationally, when a paper says “virions were purified from infected cells showing CPE,” P5 records that sentence as an **upstream Isolation claim**, then asks what else was imaged. If the answer is “nothing matched uninfected,” the structure result remains compatible with both a specific virion story and a culture-product particle story; inheritance from Isolation is not dissolved by angstroms.

Cross-checks with P2 (EV co-purification), P3 (genome from same Isolate), and P7 (other labs reproducing the prep) should be filled when those streams have rows, not hand-waved in prose.
