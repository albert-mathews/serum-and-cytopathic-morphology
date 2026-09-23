# P4 prediction — Serology / antigen under Isolation-linked labels

**Status:** Formalized, **not started**.

## One-sentence prediction

If Isolation culture + CPE is a non-specific warrant for labeling culture products, then **serology and antigen assays whose reference materials, immunogens, or “viral antigen” standards were produced from those same culture products** will often **agree with Isolation labels** even when the physical analyte is under-determined (culture supernatant proteins, EV cargo, serum/contaminant proteins, or other co-purifying material)—so concordance with Isolation is weak evidence of an independent particle class.

## Motivation from CPE non-specificity

R1 documents dual-serum Isolation practice; R2 scores negative-control quality; R3/P1–P2 press morphology and particle class separation. Serology sits downstream: neutralizing titers, ELISA, Western, lateral-flow, and “antigen detection” frequently use **Isolates, infected-cell lysates, or culture-derived antigen preparations** as truth. If the Isolation endpoint is compositionally under-determined, antigen and antibody panels can **inherit** that under-determination—label agreement becomes circular rather than triangulating.

## Empirical tests

1. **Provenance census:** For major diagnostic/serology kits and classic papers, code whether the immunogen / antigen standard / positive control traces to culture+CPE Isolates vs clinical material vs recombinant expression from culture-derived sequences.
2. **Matched mock / uninoculated culture antigen:** Where papers run serology on culture products, ask whether uninfected low-serum or matched-maintenance cultures generate reactive bands/titers under the same assay.
3. **Cross-reactivity / EV overlap:** Literature where EV preparations or serum proteins react in “virus” antigen/antibody assays.
4. **Sequence-linked serology:** Assays that use peptides/proteins from genomes whose type path is culture-derived (link P3 inheritance)—score that path explicitly.

## What would strengthen / weaken

| Result pattern | Reading |
|----------------|---------|
| Antigen/serology standards overwhelmingly culture-Isolate-derived; mocks sometimes reactive | Strengthens inheritance / circular-concordance prediction |
| Clinical-only antigen standards with particle-separating biochem + non-culture infectivity | Weakens for those systems; keep as adversarial balance |
| Recombinants from culture-seeded reference ORFs “confirm” Isolation | Neutral-to-strengthening for inheritance unless independent particle proof exists |

## Non-goals

- Not a clinical-care recommendation or assay-bashing exercise.
- Not HIV ontology expansion; phage out of scope.
- Not a claim about all antibody biology; scoped to Isolation-linked reference materials.
- Nucleic acids assumed real; this stream is about **label inheritance** in antigen/serology practice.

## Links

- **R1–R3:** Isolation recipes, controls, morphology specificity.
- **P1–P3:** History of medium practice; EV/particle indistinguishability; sequence inheritance from culture type material.
- **P6:** Vaccine seed identity may share culture-product antigen ontology.

## Deliverables when started

p4.md working note; coding sheet for antigen/immunogen provenance; short corpus table; snippets for paper Discussion only if inheritance is in scope.

## Worked example sketch (how coding would look)

A minimal P4 row is not “assay brand bad/good.” It is a **provenance stack**:

1. **Analyte claimed:** antibody titer / antigen capture / neutralization / Western band.  
2. **Positive-control or immunogen source:** culture Isolate lysate; purified culture particles; recombinant ORF from a culture-derived reference; clinical specimen.  
3. **How the Isolate was justified historically:** CPE / plaque / TCID50 / PCR-only / unspecified.  
4. **Matched uninfected culture antigen run?** yes / no / unclear.  
5. **Serum/maintenance noted in antigen production?** link to R1 dual-FBS language if present.  
6. **Particle separation vs EV markers?** if antigen is “purified virus,” apply P2 overlap codes.  
7. **Sequence path (if any):** accession → P3 risk_path (culture_cpe / culture_no_cpe / clinical_direct / unclear).

**Expected pattern under the prediction:** many classic and kit-linked assays score culture_cpe for immunogen or reference antigen; matched mocks are rare; when mocks exist, reactive signal is sometimes reported and then explained away as “nonspecific” without revising the Isolation warrant.

## Detailed strengthen / weaken scenarios

**Strengthen.** (a) Parallel ELISA OD curves for infected and uninfected low-serum cultures using the same kit; (b) Western bands shared between EV-enriched uninfected pellets and “viral antigen” lanes; (c) neutralization assays that define titer solely by CPE reduction in the same dual-serum system R1 describes; (d) package inserts that name Isolate strains whose public genome path is culture_cpe.

**Weaken.** (a) Antigen standards produced from clinical material without culture, with orthogonal mass-spec identity not dependent on Isolation labels; (b) monoclonal panels raised against particles separated by class-defining biochemistry that uninfected matched preps lack; (c) functional assays that do not use culture CPE as the readout (rare in this corpus—document honestly when present).

**Ambiguous.** Recombinant antigens: they remove culture supernatant complexity but often **embed P3 inheritance** if the ORF comes from a culture-seeded reference. Code as 
ecombinant_from_culture_ref rather than as automatic independence.

## Sampling plan (when started)

- Start from R1 dual-FBS Isolation papers that also report serology/antigen on the Isolate.  
- Add landmark diagnostic kit inserts (public PDFs only; store under gitignored 
efs/).  
- Add 10–20 adversarial clinical-serology papers that claim to avoid culture antigen.  
- Freeze a coding sheet before expanding; no stealth enrichment against 10→2 recipes.

## Relation to paper drafting

P4 is **optional Discussion / future work** unless the main paper explicitly expands inheritance beyond particles and titers. If used, prefer one scoped sentence: serology concordance with Isolation often uses culture-derived antigen standards, so it does not by itself repair CPE specificity. Keep numbers in supplemental tables, not slogans.

## Open questions for Albert

- Prefer kit-insert census first, or Isolation-paper serology first?  
- Include animal serology (veterinary Isolation) as equal-weight rows?  
- Any hard-exclusion list beyond HIV/phage?
