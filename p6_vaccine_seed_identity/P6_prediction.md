# P6 prediction — Vaccine master-seed identity as process ontology

**Status:** Formalized, **not started**.

## One-sentence prediction

**Vaccine master seeds and working seeds** are best read as **regulated culture-process products** (passage history, cell substrate, medium/serum regime, release assays including CPE/infectivity-in-culture, and sequence identity to a reference)—so “seed identity” tracks a **manufacturing ontology** continuous with Isolation practice; this stream documents that process ontology, **not** vaccine efficacy, safety, or uptake.

## Motivation from CPE non-specificity

If Isolation culture + CPE under-determines the particle/sequence label (R1–R3, P2–P3), then seeds whose identity and potency assays still route through **culture endpoints** (CPE, plaque, TCID50, culture MOI) and through **references born as Isolates** inherit the same process questions. The public object “the seed virus” may be a **stabilized culture consensus** (passage + assays + release specs) rather than a uniquely grounded natural particle independent of that process.

## Empirical tests

1. **Seed dossier coding (public docs only):** WHO/pharmacopeia/manufacturer public descriptions—cell substrate, passage, medium/serum mentions, identity assays, adventitious-agent tests, sequence identity criteria.
2. **Link to Isolation recipes:** Where seed production uses growth/maintenance serum step-downs akin to R1 dual-FBS practice, record the parallel.
3. **Sequence identity to culture-derived references:** When release genetics matches a type/prototype with culture_cpe origin (P3 Step 1), flag inheritance.
4. **Same seed, divergent genetics/assays over time:** Public reports of seed re-derivation, sequence drift, or assay method changes (tie A3 in p3.md).

## What would strengthen / weaken

| Result pattern | Reading |
|----------------|---------|
| Seed identity/potency still culture-endpoint + Isolate-reference dependent | Strengthens process-ontology reading |
| Seed release uses clinical-direct genetics + particle assays that separate from EVs + non-culture function | Weakens for those products |
| Adventitious-agent / bovine/reagent NA findings in seed systems | Supports culture-system ingredient scrutiny (link P3 A2) |

## Non-goals (mandatory)

- **Not anti-vaccine advocacy.** No efficacy/safety/uptake claims; no campaign language.
- Not a recommendation to use or avoid any product.
- Not HIV ontology expansion; phage out of scope.
- Exploration of **process identity**, scoped to public manufacturing/Isolation-linked documents.

## Links

- **R1–R2 / P3:** Culture recipes, controls, sequence inheritance.
- **P4:** Antigen/serology standards often share culture ontology with seeds.
- **P7:** Cross-lab / cross-manufacturer repeatability of seed identity assays.

## Deliverables when started

p6.md; public-doc coding sheet; explicit non-goals block repeated in any paper snippet.

## Process ontology (what “seed identity” means here)

In public manufacturing language, a master seed is identified by a **bundle**: lineage name, passage level, substrate cells, production medium, in-process controls, identity tests (often phenotypic in culture), potency (often culture titer), purity/adventitious-agent panels, and increasingly sequence identity to a reference file. P6 treats that bundle as an empirical object continuous with Isolation practice.

This is **descriptive process ontology**. It does not argue for or against vaccination programs, mandates, or individual risk–benefit. Those topics are out of scope for this repo stream.

## Worked example sketch (public-doc coding)

1. **Document class:** WHO TRS excerpt; pharmacopeia monograph; EMA/FDA public assessment; manufacturer methods paper.  
2. **Substrate:** cell line / eggs / other.  
3. **Medium/serum:** any dual growth–maintenance language (R1 parallel).  
4. **Identity assay:** CPE morphology, neutralization in culture, PCR to culture-derived reference, antigen ELISA, sequencing.  
5. **Potency:** PFU, TCID50, focus-forming units, animal assay, HPLC antigen—**flag if culture-endpoint**.  
6. **Reference genome path:** if named strain has P3 Step 1 code, inherit it.  
7. **Adventitious / bovine / reagent NA notes:** link P3 A2 without turning P6 into a contamination exposé.

## Detailed strengthen / weaken scenarios

**Strengthen process-ontology reading.** Seed release still depends on CPE/TCID50; genetics match culture_cpe type strains; public docs describe serum step-down Isolation-like production; re-derivation changes consensus sequence while the trade name stays fixed.

**Weaken.** Potency/identity rest on clinical-direct genetics and particle assays that separate from EVs, with functional readouts that are not culture CPE. Document such cases carefully as adversarial balance.

## Non-goals repeated (do not drift)

- No efficacy, safety, uptake, or hesitancy content.  
- No campaign or advocacy framing in filenames, headings, or snippets.  
- No implication that process ontology equals “products do nothing.” Mechanism of clinical protection is simply **not the question** this stream asks.

## Sampling plan

Public WHO/pharmacopeia texts first (no paywalled regulatory dumps). Optional manufacturer methods papers already in 
efs/ when legally held offline. Prefer equal-weight across several families already in P3 Step 1 rather than a single famous product.

## Relation to paper drafting

Likely **out of main paper** unless a short “manufacturing continuity with Isolation” clause is requested. If drafted, lead with process description and non-goals.

## Open questions

- Eggs-based production in or out?  
- Sequence-only identity seeds: still code culture reference inheritance?

## Tone and filename discipline

Use neutral process words: seed, passage, substrate, release assay, identity, potency, reference sequence path. Avoid persuasion vocabulary in headings and CSV fields. If a public document discusses efficacy, P6 extracts only the **identity/process** clauses and leaves efficacy sentences unscored.

When sequence identity is required to a named strain, always attempt a P3-style origin code for that strain. A seed can be fully “in spec” as manufacturing and still inherit culture_cpe genetics; that conjunction is exactly the process-ontology point, not a safety claim.

If Albert later wants a paper sentence, the safe form is: vaccine master-seed identity, as publicly specified, is continuous with Isolation culture process and culture-linked references; evaluating clinical programs is outside this paper’s scope.
