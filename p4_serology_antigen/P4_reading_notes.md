# P4 reading notes — serology / antigen provenance references

**Purpose:** Track the sources read for P4 and how each bears on the prediction in
`P4_prediction.md`. Not a corpus table — that is `p4_antigen_provenance.csv`. Tagged claims
only; quotes stay short and attributable. Role codes only.

**Status:** Working notes, first pass 2026-11-06.

---

## 1. How the reference set maps to the P4 empirical tests

`P4_prediction.md` lists four empirical tests. The sources below were found against
tests 2 and 3 (matched-mock / uninoculated-culture reactivity, and cross-reactivity /
contaminant overlap). Test 1 (provenance census) is the CSV rows; test 4 (sequence-linked
serology) chains into P3 and is not yet populated here.

| P4 test | What this note adds |
|---------|---------------------|
| 1. Provenance census | (carried in `p4_antigen_provenance.csv`) |
| 2. Matched mock / uninoculated antigen | Documented examples where the diagnostic antigen *is* a culture lysate |
| 3. Cross-reactivity / contaminant overlap | Documented examples where culture-system contaminants (FBS-borne pestiviruses) produced false serology |
| 4. Sequence-linked serology | not yet populated (P3 linkage) |

---

## 2. Culture-derived antigen as the reference reagent (test 1 support, outside kit territory)

**Saliki et al. 1998** — *Use of tick cell culture-derived Anaplasma marginale antigen in a
competitive ELISA for serodiagnosis of anaplasmosis.* Ann N Y Acad Sci 849:273-81.
DOI: 10.1111/j.1749-6632.1998.tb11059.x. PMID 9668475.

> "Anaplasma marginale was propagated in a continuous tick cell line and
> detergent-solubilized infected cells were used as antigen in a competitive ELISA"

Reading for P4: the reference antigen is a **detergent-solubilized infected-cell lysate**
from a continuous culture line. Veterinary domain (bovine). Exactly the `culture_isolate_lysate`
reference-antigen pattern the census is designed to catch; the C-ELISA's specificity is argued
against a complement-fixation comparator, not against a matched uninfected tick-cell lysate
antigen. Mapped to `reference_antigen_source = culture_isolate_lysate`, `matched_mock_run`
unaddressed in the abstract. A candidate CSV row if the full text is added to `refs/`.

**Beier et al. 2004** — *Establishment of a new bovine leukosis virus producing cell line.*
J Virol Methods 121(2):239-46. DOI: 10.1016/j.jviromet.2004.06.017. PMID 15381362.

> "contamination of the BLV antigen-producing cell culture systems by bovine viral
> diarrhea virus (BVDV) may give rise to misinterpretation of serological test results"

Reading for P4: this is the P4 mechanism stated by practitioners in the veterinary
literature. The antigen-producing cell culture carried a contaminant (BVDV), and the
contaminant confused serological interpretation until a contamination-free line was
substituted. This is not a "wrong antigen" in the abstract sense; it is the culture system
supplying label-relevant material beyond the intended analyte. Strong direct support for the
inheritance reading, and it names the specific contaminant route (FBS/cell-line pestivirus)
developed in §3 below.

---

## 3. The contaminant route: FBS / cell-line pestiviruses entering antigen and serology

*Route note (2026-11-06):* the **culture-reagent** half of this strand (FBS lots and repository
cell lines carrying pestivirus material — Giammarioli 2015, Bolin 1994, Muhsen 2013) has been
filed to R1 as `../r1_isolation_standards_and_practice/P4_handoff_to_R1.md`. P4 keeps only the
**serology/antigen-assay design** angle: what culture-derived antigen / reagents do to a serology
readout.

**Xu et al. 2022** — *An Improved Immunochromatographic Strip Based on Plant-Derived E2 for
Detection of Antibodies against Classical Swine Fever Virus.* Microbiol Spectr 10(4):e0105022.
DOI: 10.1128/spectrum.01050-22. PMID 35862968.

> "plant-derived E2 avoids the limitations of low immunogenicity of eukaryotic expression
> systems and potential contamination of fetal bovine serum with bovine viral diarrhea
> virus in cell culture."

Reading for P4: a contemporary note that eukaryotic/cell-culture antigen production carries a
known FBS-contamination risk, motivating a plant-expression alternative. Veterinary, lateral-flow
format (this is the missing rapid-antigen/lateral-flow format noted in the pilot). It documents,
from the assay-developer side, that culture-derived antigen is treated as carrying the culture
system's own contamination risk.

---

## 4. What this strand does and does not show

**It shows (documented):**
- Culture-derived antigen is a real, described reagent category (Saliki; Beier).
- The antigen-producing culture system can carry material (host protein, serum component, or a
  co-carried agent label) that enters the antigen and distorts interpretation (Beier; Xu).

**It does not show, and P4 should not claim:**
- That every kit or classic serology uses a culture-derived antigen that cross-reacts.
- That the "contamination" route is the *only* mechanism for concordance with Isolation labels.
  The P4 prediction is broader: any culture-product (host protein, EV cargo, serum protein,
  co-carried material) can stand in for "the antigen" without requiring a contaminating virus.

The culture-reagent contamination strand itself (FBS lots and cell lines carrying pestivirus
material) is filed to R1, not argued here. These sources are **case evidence that the serology
mechanism the prediction describes is real and already named in the field**, not a census result.
Beier and Xu are the strongest one-liners for the assay-design side.

---

## 4b. Prior art — who has already published toward this prediction (credit owed)

A 2026-11-06 sweep of PubMed / Europe PMC / Zenodo / arXiv located work that already presses the
P4 direction. These are not "confirmation we are first"; several are ahead of us on specific
mechanisms and should be cited, not re-derived.

**Kainulainen et al. 2026** — *Monoclonal IgM antibodies mediate potent complement neutralization
by targeting cell-derived epitopes on enveloped viruses.* mBio 17(3):e0170925.
DOI: 10.1128/mbio.01709-25. PMID 41685933.

> "The antibodies were found to bind ganglioside GM2... Gangliosides and other host membrane
> moieties are known to be carried by viruses... the membranes are known to contain cell-derived
> markers in addition to virally encoded proteins."

Reading for P4: this is the strongest prior-art anchor. A **neutralizing antibody** — the
gold-standard serological readout for "this is the virus" — here binds a **host membrane
component (GM2 ganglioside)** carried on the envelope, not a virus-encoded epitope. The authors
frame the effect as "non-specific" neutralization by naïve donors, but the structural point for P4
is independent of that framing: the neutralization readout can be driven by host/cell-derived
material co-carried on the "virus." It shows, in peer-reviewed form, that serology can read
host material rather than a virus-specific antigen.

**Ellis et al. 2023** — *SARS coronavirus 2-reactive antibodies in bovine colostrum.*
Can Vet J 64(4):337-43. PMID 37008643.

Reading for P4: bovine serum/colostrum — the same ingredient base as the FBS in Isolation medium —
carries material reactive against a "SARS-CoV-2" antigen. This is the serum-ingredient
cross-reactivity the P4 prediction describes, published in a veterinary journal. It supports the
reading in §4c below that the serum/medium component itself, not a virus, can be what a "viral
antigen" assay detects.

**Chodavarapu et al. 2026** — *Scalable downstream process for purification/inactivation of
microcarrier-propagated Japanese encephalitis virus antigen.* Zenodo. DOI 10.5281/zenodo.23842428.

Reading for P4: a non-peer-reviewed (Zenodo) publication whose entire downstream process is
organized around clearing **host-cell protein and host-cell DNA impurities** from culture-derived
"viral antigen." It documents, from the developer side, that culture-derived antigen is understood
to contain substantial host material — the co-purifying fraction P4 is about.

**Sherlock et al. 1986** — HSV-2 AG-4 complement-fixation type specificity. J Clin Microbiol
24(6):1093-7. PMID 3023439. A classic, older demonstration that a commercial CF "viral antigen"
was not type-specific (HSV-1 vs HSV-2 cross-reading), i.e. that antigen-driven serology can read
material other than the intended agent.

**Browne et al. 2025** — *Multilayer Fluorescent Immunoassay for Dengue Using Host and Viral
Biomarkers.* Bioconjug Chem 36(7):1474-82. PMID 40503688. Reads **host** biomarkers *alongside* viral
markers — an adjacent acknowledgement that host material is diagnostically informative in "viral"
assays.

arXiv returned no direct hits on these phrasings (arXiv is physics/CS-heavy); the relevant
preprint corpus is bioRxiv/medRxiv, which remain to be swept in a later pass.

---

## 4c. An interpretive split: the "no virus enters" reading vs the "contamination" reading

The sources in §3 are usually reported as **contamination** — e.g. "FBS was contaminated with
BVDV." That framing *presupposes* a virus (BVDV) is the thing detected. P4 should record a second,
more parsimonious reading that the same data also accommodates, without asserting it as fact:

- The only evidence that "FBS contains BVDV" is itself a serology / antigen-capture / PCR readout
  whose reference material traces, by the coding-sheet logic, to culture-derived material.
- Under the P4 prediction, that reference material can consist of host proteins, EV cargo, serum
  proteins, or other culture products rather than a virus particle. If an isolate used to *define*
  the "BVDV" label carried a set of serum/culture compounds (and nothing that was demonstrated to be
  a distinct particle class), then the antigen/antibody reagents were tuned to those compounds.
- A later "positive in FBS" then reports the presence of those *compounds in serum* — which is
  trivially expected — and the "contamination" label is a re-description of reagent cross-reactivity,
  not an independent observation of a contaminating virus.

Formal statement of the two readings, held open rather than decided:

| Reading | What it assumes | What the same data shows |
|---------|-----------------|--------------------------|
| Contamination | A virus (BVDV) exists and is present in FBS | Serology/PCR detects contaminating virus in a "virus-free" reagent |
| No-virus / shared-substance | No virus need ever be involved | Reagents raised/tuned on isolate material react with compounds that were *in* the isolate and are *also* in serum, so "pure product" positives are the compounds, not a virus |

The no-virus reading is **more conservative in what it claims**: it does not require a virus to
explain the observed reactivity, and it predicts reactivity where "virus-free" serum is guaranteed
to be reactive (because the compounds are serum components). The contamination reading must posit a
virus, then posit that it leaked through a "virus-free" process. P4's job is to record which reading
the documents *force* versus *permit*, not to settle it by assertion. The Ellis 2023 colostrum result
and the Kainulainen 2026 GM2 result are each cleaner instances of the no-virus-permitted reading,
because neither requires a contaminating virus: they report cross-reactivity by serum/host material
directly.

*Guardrail note:* none of the above states "viruses were never present" as a prior or as fact. It
states that specific, citable observations can be explained without positing a virus, and that P4
tracks that as an interpretation the evidence permits. The repo does not assert the no-virus
conclusion; if the evidence favors it, that is what gets written, as a finding about what the
documents show, not as a stored belief.

---

## 4d. The interference literature — location-D evidence of the single non-viral-epitope arm

A second search pass (2026-11-06) found a large, well-established literature on **why viral serology
reads positive without the virus present.** It is almost entirely explained, by practitioners, via
endogenous anti-reagent antibodies (heterophile/HAMA) and shared/cross-reacting epitopes. Under the
collapsed framing in `P4_prediction.md` (§"Two fundamental cases"), these are **location-D and
location-C evidence of the single non-viral-epitope arm**: the bound epitope is not viral, and no
virus is needed to explain the positive. They differ from the reference-side (location-B) evidence
only in *where* the non-viral substance is said to originate — which is irrelevant to the no-virus
conclusion. Recorded here as the field's own demonstration that a non-viral epitope is, in fact,
what routine viral serology binds in a large fraction of cases.

**Kricka 1999** — *Human anti-animal antibody interferences in immunological assays.* Clin Chem
45(7):942-56. PMID 10388468 (cited >300×).

> "The most common human anti-animal antibody interferent is HAMA, which causes both positive and
> negative interferences in two-site mouse monoclonal antibody-based assays."

Reading: the canonical statement of the patient-side (location-D) mechanism. Endogenous human
anti-mouse (or anti-rabbit/cow/sheep/etc.) antibodies bridge or block the assay's own capture/detection
reagents, producing positives that have nothing to do with any virus antigen. Prevalences run
"<1% to 80%."

**Song et al. 2025** — *Resolving heterophile antibody interference in viral serology using blocking
tubes.* Microbiologyopen 14(6):e70098. PMID 41144880.

> "HBT pretreatment significantly reduced both reactivity levels... and positivity rates (EBV VCA:
> 38/185 [20.5%] to 5/185 [2.7%]; HSV: 92/185 [49.7%] to 5/185 [2.7%])."

Reading: the single most direct measurement found so far. In routine viral IgM serology for common
agents (EBV, HSV, VZV, CMV, rubella, Toxoplasma), up to **49.7%** of HSV IgM "positives" were
heterophile interference — i.e. endogenous antibody binding the assay's *reagents*, resolved by
heterophile-blocking tubes. This is "positive without the named virus," with the bound epitope being
**non-viral** (patient anti-reagent antibody). Same arm as the reference-side evidence; only the
supposed *location* of the non-viral epitope differs.

**Ye et al. 2021** — false-positive SARS-CoV-2 antibody reasons (PMID 33710634): "the most common
endogenous interferences include rheumatoid factor, heterophile antibodies, human anti-animal
antibodies, lysozyme, complement, and cross-antigens."

**Kharlamova et al. 2021** (PMID 34012450) and **Costa et al. 2021** (PMID 34336313, isolated
false-reactive HBsAg) — further non-viral-epitope instances.

### What this strand establishes

- The field already *has* a mature account of "serology positive with no virus," and in every version
  of it the bound epitope is **non-viral** (heterophile/HAMA/cross-antigen, all non-viral molecules).
  None of these accounts requires a virus; they require a non-viral substance and an assay fitted to
  bind it — which is exactly the non-viral-epitope arm.
- Song 2025 quantifies this at ~50% of positives in one viral-IgM panel. That is the field's own
  demonstration that routine viral serology binds a non-viral epitope in a large fraction of cases.
- The location distinction (reference-side vs patient-side vs shared-hit) remains **unresolved**, but
  P4 records it as a *location* question, not a *does-a-virus-exist* question. Either way, no virus is
  needed. The coding sheet can still record, per document, whether the evidence points to a
  reference-standard origin or a patient-side interference origin, because that is a real (if
  secondary) empirical question — but it does not alter the no-virus conclusion.

**Hornig et al. 2012** — *Absence of evidence for bornavirus infection in schizophrenia, bipolar
disorder and major depressive disorder.* Mol Psychiatry 17(5):486-93. PMID 22290118.

Reading for P4: a well-controlled disconfirmation. Earlier reports of bornavirus "infection" in
psychiatric patients (largely serological) did not hold up when re-tested with serology plus
independent nucleic-acid and blinded replication assays. A caution against reading any serology
positive (including ours) as evidence for a discrete particle, and an instance where the cognate
agent was *not* found on better-controlled measurement — i.e. consistent with the non-viral-epitope
reading. Not a P4 "win"; a P4 check.

---

## 5. Open collection items for the census (not yet read in full)

- A licensed **immunoblot** IFU (best chance of `matched_mock_run = yes`: immunoblots
  routinely run an uninfected-lysate lane). Candidate manufacturers with public eIFU
  libraries: MIKROGEN `recomLine` Line Immunoassays, EUROIMMUN line blots. Non-HIV targets
  only (e.g. Borrelia/Lyme, EBV, measles). Inserts to store under `refs/`.
- A **lateral-flow / rapid antigen** IFU (non-HIV). A manufacturer-insert-level document,
  not a distributor catalogue — see P4-007's lesson that catalogue sources cannot fill the stack.
- Upgrade P4-004/-005/-006 and P4-007 (veterinary rows) from catalogue/datasheet to
  manufacturer inserts.

---

## 6. Exclusions applied

- HIV material (e.g. 1987 immunofluorescence confirmatory work) is out of P4 scope per the
  repo-wide ontology exclusion; noted here only to record that it was screened and set aside.
- Bacteriophage systems out of scope.
- Patents not read or listed.

---

*End of first-pass reading notes. Extend with full-text reads under `refs/` as they arrive.*