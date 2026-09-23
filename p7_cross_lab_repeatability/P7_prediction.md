# P7 prediction — Cross-lab repeatability of Isolation-linked claims

**Status:** Formalized, **not started**.

## One-sentence prediction

Claims that depend on **Isolation culture + CPE** (and on culture-derived particles, antigens, or sequences) will show **material cross-lab discordance**—in CPE calls, control behavior, particle yields, serology titers, or assemblies—when labs differ in serum lots, medium, cell passage, imaging thresholds, or bioinformatics priors; concordance, when it occurs, often reflects **shared process templates** rather than independent discovery of a uniquely grounded object.

## Motivation from CPE non-specificity

If the Isolation warrant is non-specific or under-determined, independent labs following similar dual-serum recipes (R1) and weak matched controls (R2) can reproduce **the same labeled outcome** without that reproduction proving specificity. Conversely, serum lot / FBS / matrix differences can change CPE and downstream assays. Repeatability is therefore a **process probe**, not automatic validation.

## Empirical tests

1. **Multi-lab Isolation panels:** Ring trials / EQAS / proficiency tests for virus Isolation or CPE reading—score serum conditions, control design, and discordance rates.
2. **Same inoculum, different labs:** Published inter-lab comparisons of titer, CPE, antigen, or sequence from aliquots of one stock.
3. **Blinded morphology (R3-style) across sites:** Whether low-serum uninfected cultures draw CPE-like calls across raters/labs.
4. **Assembly / serology discordance:** Same stock sequenced or titered in multiple centers (link P3 A3, P4).

## What would strengthen / weaken

| Result pattern | Reading |
|----------------|---------|
| High concordance only under shared recipes; mocks or serum shifts move calls | Strengthens process-template reading |
| Stable results under deliberately varied serum/matrix with strong matched NCs | Weakens non-specificity for those systems |
| Blinded raters disagree on CPE for identical images | Strengthens endpoint subjectivity (R3) |

## Non-goals

- Not a claim that all labs are unreliable.
- Not advocacy; scoped empirical repeatability under Isolation-linked methods.
- Nucleic acids assumed real; phage/HIV ontology out of scope.

## Links

- **R1–R3:** Practice, controls, morphology.
- **P2–P6:** Particle, genetics, serology, structure, seeds—all can be scored for cross-lab stability.
- **P3 A1/A3:** Mock sequencing and same-stock assemblies as genetics repeatability probes.

## Deliverables when started

p7.md; table of ring-trial / inter-lab papers; coding fields for serum, controls, discordance metric.

## Repeatability as a process probe

Reproduction can mean (i) same labeled CPE under same recipe, (ii) same titer within a factor, (iii) same antigen OD, (iv) same assembly, or (v) same blinded morphology calls. P7 distinguishes **template-following concordance** from **robustness under deliberate serum/matrix/control variation**. The prediction says Isolation-linked claims are often strong at (i) under shared templates and weak at robustness tests.

## Worked example sketch

1. **Study type:** EQAS / ring trial / two-lab aliquot split / multi-rater image set.  
2. **Endpoint:** CPE call, titer, PCR Ct, antigen, assembly hash/diff, rater marks.  
3. **Serum/medium disclosed?**  
4. **Matched NC design?** (R2 tiers).  
5. **Discordance metric:** % labs outside reference; kappa for raters; assembly edit distance.  
6. **After protocol harmonization:** did concordance rise only when serum and CPE thresholds were forced identical?

## Detailed strengthen / weaken scenarios

**Strengthen.** Ring trials show CPE discordance that shrinks only after enforcing maintenance serum and reading SOPs; blinded raters mark CPE-like features on low-FBS uninfected images across labs (R3 extension); same stock assemblies diverge across centers (P3 A3).

**Weaken.** Endpoints stable across intentional serum lot changes with Tier-A matched NCs and particle-level assays that uninfected preps fail.

## Sampling plan

- Public EQAS reports for virus Isolation / molecular detection (molecular may still classify via culture refs—code P3 inheritance).  
- Inter-lab titer papers on named stocks.  
- Any multi-center cryo or serology ring trials (link P4/P5).

## Relation to paper drafting

Natural Methods/limitations bridge: even descriptive Isolation corpora (R1) are practice samples, not proof that every lab’s CPE means the same particle event. Keep tone empirical.

## Open questions

- Include molecular-only EQAS as first-class or secondary?  
- Minimum n for a “panel” before claiming a rate?

## Failure modes to code explicitly

1. **Hidden template sharing:** labs trained on the same SOP produce matching CPE calls; treat as low information for specificity.  
2. **Serum lot shocks:** switching FBS lot changes CPE or titer without inoculum change; high information for process sensitivity.  
3. **Rater threshold drift:** same image set, different CPE prevalence after threshold discussion.  
4. **Bioinformatics prior drift:** same reads, different “viral” contigs after DB or filter update (genetics arm of P7 / P3 A3).  
5. **False comfort from PCR EQAS:** molecular concordance can be concordance to culture-derived references; code P3 inheritance rather than counting as particle proof.

A short methods note for any future paper: inter-lab agreement under Isolation-linked endpoints should be interpreted in light of shared recipes and control quality (R1–R2), not as standalone confirmation of CPE virus-specificity.

## Minimum reporting fields (CSV when started)

study_id, year, endpoint_class (cpe|titer|antigen|assembly|morphology_rater|molecular), 
_labs_or_raters, serum_disclosed (yes|no|partial), 
c_tier_link_r2 (A|B|C|D|na), discordance_metric, discordance_value, harmonization_changed_serum_or_threshold (yes|no|unclear), p3_inheritance_flag (for molecular endpoints), 
otes.

Freeze these columns before collecting rows. Prefer public ring-trial reports and papers with explicit aliquot splits. This stream stays formalized-not-started until that sheet exists and a first dozen rows are coded without slogan language.

