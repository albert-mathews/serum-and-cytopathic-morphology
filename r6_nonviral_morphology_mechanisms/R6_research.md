# R6 research protocol — non-viral mechanisms of CPE/plaque morphology

**Status:** v0.1 scaffold (2026-11-17). Mirrors `r5_precell_virus_purification_census/R5_research.md` where the
machinery applies, adapted from a *census* (R5) to a *mechanism survey* (R6).
**Stance:** There is no preferred outcome. The goal is to enumerate, from the cell-biology and negative-control
literature, the **generic, non-viral** pathways by which an uninoculated monolayer can round, vacuolate, become
granular, detach, or form a focal zone of death — and to attach to each candidate a **distinguishing prediction**
testable against the CRO/Zenodo record and the CLSI M41 Table 7 descriptor set.

## 1. What R6 is (and is not)

**Is:** a mechanism survey. Under the explicit working assumption that the inoculum held no virus / no
disease-causing agent (AX011: this is the development of the no-virus explanation on its own terms, **not** a
claim that no infectious agent exists), R6 asks: by what cell-biological processes do "CPE" and "plaques" —
foci of rounding, detachment, granularity, vacuolation, and countable zones of death under a solid overlay —
actually form?

**Is not:** a particle-purification history (R5); an EV–virion indistinguishability review (P2); a history of
serum/nutrient practice (P1); an Isolation-practice corpus census (R1/R2); an image-labeling study (R3); a
non-isolation-protocol survey (R4); or any claim that the CPE/plaque methods are *validated* (guardrail — R6 may
draw temporal/process connections to R5 and the CRO result but must never state or insinuate the methods are
validated).

## 2. Working assumptions (explicit, not results)

| Assumption | Meaning |
|-----------|---------|
| **No-virus premise** | The inoculum is assumed to contain no virus / no disease-causing agent. R6 develops this explanation on its own terms. |
| **Plaque = countable zone of death** | Under the premise, a "plaque" is a locally countable region of cell death / clearing; R6 asks what produces that region and what predicts its size, shape, timing, and serum dependence. |
| **Non-specificity ≠ non-existence** | R6 does not assert that "nothing infectious exists" in any system (AX011). |
| **Scope = standard culture/maintenance conditions** | All claims are scoped to classical dual-medium Isolation conditions (growth ~10% FBS → maintenance ~1–3% FBS) and standard plaque-overlay practice. |

## 3. Inclusion / exclusion

**Include** a source if it documents, in a mammalian cell-culture system (ideally Vero / continuous epithelial
lines), one or more of:

1. a *mechanism* by which uninoculated / uninfected monolayers round, vacuolate, granulate, detach, or die
   (serum/growth-factor withdrawal, nutrient depletion, metabolic waste, pH drift, anoikis, senescence,
   confluent degeneration, paracrine/bystander death, autophagy, contaminant, intrinsic instability, overlay
   effects, osmotic stress);
2. a *negative-control or stability report* describing what uninoculated monolayers do under maintenance media
   and/or solid overlays (including what "negatives that formed foci" were attributed to);
3. a *plaque-assay mechanism* source that states what a plaque is and what determines its size/shape (so the
   "one plaque = one particle" step can be read as assumption vs demonstration).

**Exclude:** pure particle-purification/EM (P2/R5); serum-practice history (P1); Isolation-practice corpus
coding (R1/R2); image-labeling method work (R3); non-isolation-protocol prescription (R4); retracted articles
(they are note-only, never load-bearing).

## 4. Epistemic rules (bias control)

1. Log every candidate in `R6_screened.csv` (Y/N/B + reason), never silently drop.
2. Extract the same mechanism fields from every useful item (Section 5) using the fixed mechanism code in
   `R6_mechanisms.md` (R6-M1 … R6-M12). Do not invent ad hoc categories per paper.
3. **Secondary citations of a primary mechanism are corroboration, not the primary.** Wishlist the primary; tag
   `[DATA REQUIRED]` until its full text is read.
4. **Abstract-only research is not allowed.** An abstract may identify a source; a load-bearing claim needs the
   full text (`[VERIFIED src]`). An abstract-only source goes on `R6_pdf_wishlist.md` and its claim is
   `[DATA REQUIRED]`.
5. **Distinguish paper-body from reference-list text.** A grep hit inside a cited reference's title is not the
   paper making the statement. Quote/tag accordingly.
6. **Distinguishing predictions are the deliverable.** Every mechanism must carry at least one prediction that
   would *distinguish it* from the others against the CRO/Zenodo data (time-course, serum-dependence, focal vs
   uniform, reversibility, overlay-dependence, contaminant-detectability).
7. Devil's-advocate pass: actively record the conditions under which the *no-virus* explanation would look
   wrong (e.g., plaques that expand at virus-like kinetics with no metabolic handle; contaminant ruled out; a
   serum-independent focal death that passes to fresh cells). Keep these in the "weaken" column of the
   mechanism table rather than burying them.
8. Separation of roles: enumerate mechanisms and their predictions first; interpret ("what this means for the
   paper's CPE/plaque claims") only in the synthesis, after the table is backed.

## 5. Extraction schema (`R6_useful.csv`)

`id · year · author_short · model_cell_line · mechanism_class · mechanism_detail · observable_morphology ·
clsi_descriptor_map · serum_or_nutrient_dependency · focal_vs_uniform · distinguishing_prediction · evidence_tag ·
citation · identifier · source_type · extract_date · notes`

| Field | Meaning |
|-------|---------|
| `mechanism_class` | One of `R6-M1 … R6-M12` from `R6_mechanisms.md` |
| `observable_morphology` | rounded / ballooned / vacuolation / granularity / detachment / refractile / syncytia / strands / degeneration / none (the CLSI-Table-7 vocabulary plus the CRO sixth term "dying cells") |
| `clsi_descriptor_map` | which CLSI M41 Table 7 descriptor(s) the mechanism reproduces (e.g. "rounded + detached"; "vacuolation") |
| `serum_or_nutrient_dependency` | serum-step-dependent / nutrient-dependent / confluence-dependent / overlay-dependent / contaminant / none |
| `focal_vs_uniform` | focal (plaque-like) / uniform (whole-monolayer) / mixed |
| `distinguishing_prediction` | the test that separates this mechanism from the others vs the CRO/Zenodo data |
| `evidence_tag` | `[VERIFIED src]` / `[VERIFIED-ABSTRACT]` / `[FIGURE]` / `[IN-HOUSE]` / `[UNVERIFIED]` / `[DATA REQUIRED]` per CONVENTIONS §3 |
| `source_type` | primary / secondary / textbook / protocol / review |

## 6. Rounds

- **Round 1 (done 2026-11-17):** seed the mechanism framework from (a) the CRO/CLSI anchor already in the repo
  (OB024/OB025, CLSI Table 7), (b) full-text reads already in hand (Ammerman 2008 PMC2657228; Vander Heiden 2001
  PMC87309; Fenner chapter PMC7173454), and (c) a first web sweep for Vero/monolayer degeneration + plaque
  mechanism + mycoplasma mimicry. See `R6_search_log.md`.
- **Round 2:** systematic queries per mechanism class — serum starvation / growth-factor withdrawal apoptosis in
  adherent epithelial lines; nutrient (glucose/glutamine) depletion morphology; post-confluent / contact-inhibition
  death; lactate/ammonia/pH toxicity; anoikis; bystander / "community effect" / secondary-necrosis wave;
  autophagy-vacuolation; mycoplasma CPE mimicry; aneuploidy / spontaneous transformation foci; overlay (agarose/CMC/
  Avicel) diffusion + toxicity. Databases: PubMed/PMC, Europe PMC, Crossref, Google Scholar, vs. journals.
- **Round 3:** snowball from the bibliographies of each useful primary (esp. the plaque-theory literature:
  Abedon & Yin; Cooper's plaque-assay review; Dulbecco 1952).
- **Round 4:** adversarial — for each mechanism, document both its best supporting primary and the observation
  that would *falsify* it (the "weaken" column); bound each with the cell-line caveat (e.g. Vander Heiden is an
  IL-3-dependent hematopoietic line, not Vero).
- **Round 5+:** saturation; reconcile against the CRO/Zenodo time-course and the CLSI descriptor set; freeze;
  synthesize into `R6_synthesis.md`.

## 7. Stop / "we know" criteria

Declare the mechanism survey **provisionally complete** only when:

1. Rounds 1–4 logged.
2. Every candidate mechanism in `R6_mechanisms.md` carries (a) at least one primary/secondary citation with an
   evidence tag, and (b) at least one distinguishing prediction vs the CRO/Zenodo data.
3. The leading serum/nutrient/confluence mechanisms (R6-M1–M4) are backed by Vero-or-comparable full-text reads,
   not only by analogy from non-epithelial lines.
4. The "one plaque = one particle" step is characterized as assumption-vs-demonstration with primary quotes
   (Dulbecco 1952; Fenner chapter; Abedon & Yin), not asserted.
5. Each mechanism carries a confidence and an explicit "still open" list (paywalled primaries → wishlist).

## 8. Revision log

| Version | Date | Change |
|---------|------|--------|
| v0.1 | 2026-11-17 | Scaffold: scope, assumptions, inclusion, schema, rounds, stop criteria. |
