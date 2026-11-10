# P4 reading notes — serology / antigen provenance references

**Purpose:** Track the sources read for P4 and how each bears on the prediction in
`P4_prediction.md`. Not a corpus table — that is `p4_antigen_provenance.csv`. Tagged claims
only; quotes stay short and attributable. Role codes only.

**Status:** Working notes, first pass 2026-11-06.

---

> **Evidence-status note (updated 2026-11-08 — full texts received).** Section B full texts were
> fetched into `refs/`; every prior-art/interference source in §2, §3, §4b, and §4d has now been
> read in full and re-tagged `[VERIFIED src]`, quote-checked against the full text and extended
> below (P4W-05, -06, -08, -10, -11, -14, -15, -16, -17, -18, -19, -20, -21). P4W-09 (Liu 2016 VZV)
> and P4W-22 (Krishnan 2022 exosomes) were also read in full and are recorded in
> `P4_bibliography.md` (they are wishlist/bibliography rows, not cited in these notes). Two scanned
> (image-only) items were **OCR'd 2026-11-08** (RapidOCR) and are now readable: Saliki 1998 (`P4W-07`,
> `[VERIFIED src]`, coded as `P4-019`) and Bolin 1994 (`P4W-13`, handed to R1). The handoff-to-R1
> items (Giammarioli 2015 `P4W-12`, Bolin 1994 `P4W-13`) are noted here for completeness; their
> extraction is filed to R1. The kit-insert/catalogue CSV rows (P4-001…P4-011) were already
> full-text reads and are not affected.

---

## 1. How the reference set maps to the P4 empirical tests

`P4_prediction.md` lists four empirical tests. The sources below were found against
tests 2 and 3 (matched-mock / uninoculated-culture reactivity, and cross-reactivity /
contaminant overlap). Test 1 (provenance census) is the CSV rows; test 4 (sequence-linked
serology) chains into P3 and is not yet populated here.

| P4 test | What this note adds |
|---------|---------------------|
| 1. Provenance census | (carried in `p4_antigen_provenance.csv`) |
| 2. Matched mock / uninoculated antigen | Full-text examples where the diagnostic antigen *is* a culture lysate |
| 3. Cross-reactivity / contaminant overlap | Full-text examples where culture-system contaminants (FBS/cell-line pestiviruses) produced false serology |
| 4. Sequence-linked serology | not yet populated (P3 linkage) |

---

## 2. Culture-derived antigen as the reference reagent (test 1 support, outside kit territory)

**Saliki et al. 1998** — *Use of tick cell culture-derived Anaplasma marginale antigen in a
competitive ELISA for serodiagnosis of anaplasmosis.* Ann N Y Acad Sci 849:273-81.
DOI: 10.1111/j.1749-6632.1998.tb11059.x. PMID 9668475.

`[VERIFIED src]` — OCR'd full text (`P4W-07`), read 2026-11-08.

> "Anaplasma marginale was propagated in a continuous tick cell line and
> detergent-solubilized infected cells were used as antigen in a competitive ELISA"

Reading for P4: the reference antigen is a **crude detergent-solubilized lysate** of A. marginale
propagated in the IDE8 tick cell line and harvested at 80-100% CPE (a rickettsial agent, not a
virus — veterinary analogue). **Full-text addition (OCR):** a matched **uninfected tick-cell lysate
negative control was run**, and the MAb "did not react with uninfected cell lysates (OD ≤0.08)"
versus ≥1.5 for infected lysate — so the matched mock was **nonreactive**. Note (see §4f·ii): a
nonreactive mock only rules out *baseline uninfected* reactivity; it does **not** establish that the
reactive molecule is the A. marginale (MSP5) epitope, because the infected culture differs from the
mock by much more than the organism particles. Coded as `P4-019`
(`matched_mock_run = yes`, mock nonreactive).

**Beier et al. 2004** — *Establishment of a new bovine leukosis virus producing cell line.*
J Virol Methods 121(2):239-46. DOI: 10.1016/j.jviromet.2004.06.017. PMID 15381362.

`[VERIFIED src]` — full text read (`P4W-08`).

> "contamination of the BLV antigen-producing cell culture systems by bovine viral
> diarrhea virus (BVDV) may give rise to misinterpretation of serological test results"

Reading for P4: this is the P4 mechanism stated by practitioners in the veterinary
literature. The antigen-producing cell culture carried a contaminant (BVDV), and the
contaminant confused serological interpretation until a contamination-free line was
substituted. This is not a "wrong antigen" in the abstract sense; it is the culture system
supplying label-relevant material beyond the intended analyte. **Full-text additions:** (i) the
contaminant is the **co-cultivated carrier cell line itself** — FLK/BLV (fetal lamb kidney + BLV
leukocytes) and FLS/BLV were "known to be contaminated with BVDV", not (demonstrably) the serum;
(ii) the fix was a new sheep-kidney line **PO714** "free of 11 bovine, 2 ovine and 7 porcine
viruses"; (iii) the antigen is **crude cell-culture supernatant** ("pelleted…, resuspended in
detergent"), not purified virus; (iv) the false positive was driven by **vaccine-induced
anti-BVDV antibody cross-reacting with BVDV protein co-present in the BLV antigen** — a second
virus's antigen/antibody, so it supports "antigen impurity distorts serology" but *not* the
stronger "host-protein/FBS mimicry" route.

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

`[VERIFIED src]` — full text read (`P4W-10`).

> "plant-derived E2 avoids the limitations of low immunogenicity of eukaryotic expression
> systems and potential contamination of fetal bovine serum with bovine viral diarrhea
> virus in cell culture."

Reading for P4: a contemporary note that eukaryotic/cell-culture antigen production carries a
known FBS-contamination risk, motivating a plant-expression alternative. Veterinary, lateral-flow
format (this is the missing rapid-antigen/lateral-flow format noted in the pilot). It documents,
from the assay-developer side, that culture-derived antigen is treated as carrying the culture
system's own contamination risk. **Full-text additions:** the E2 antigen is a **transgenic-rice
expressed recombinant ectodomain** (no mammalian culture, no FBS); the paper also states
cell-produced E2 carries "risk of infection by other pestiviruses, particularly BVDV and BDV"
and that plant expression "avoids the risk of contamination by animal products"; no
cross-reactivity with BVDV/BDV/PRRSV/PCV2/FMDV/ASFV; commercial comparator is the IDEXX CSFV kit.

---

## 4. What this strand does and does not show

**It shows (full-text read):**
- Culture-derived antigen is a real, described reagent category (Saliki; Beier).
- The antigen-producing culture system can carry material (host protein, serum component, or a
  co-carried agent label) that enters the antigen and distorts interpretation (Beier; Xu).

**It does not show, and P4 should not claim:**
- That every kit or classic serology uses a culture-derived antigen that cross-reacts.
- That the "contamination" route is the *only* mechanism for concordance with Isolation labels.
  The P4 prediction is broader: any culture-product (host protein, EV cargo, serum protein,
  co-carried material) can stand in for "the antigen" without requiring a contaminating virus.

The culture-reagent contamination strand itself (FBS lots and cell lines carrying pestivirus
material) is filed to R1, not argued here. These sources are **full-text case evidence that the
serology mechanism the prediction describes is real and already named in the field**, not a census
result. Beier and Xu are the strongest one-liners for the assay-design side.

---

## 4b. Prior art — who has already published toward this prediction (credit owed)

A 2026-11-06 sweep of PubMed / Europe PMC / Zenodo / arXiv located work that already presses the
P4 direction. These are not "confirmation we are first"; several are ahead of us on specific
mechanisms and should be cited, not re-derived.

**Kainulainen et al. 2026** — *Monoclonal IgM antibodies mediate potent complement neutralization
by targeting cell-derived epitopes on enveloped viruses.* mBio 17(3):e0170925.
DOI: 10.1128/mbio.01709-25. PMID 41685933.

`[VERIFIED src]` — full text read (`P4W-05`).

> "The antibodies were found to bind ganglioside GM2... Gangliosides and other host membrane
> moieties are known to be carried by viruses... the membranes are known to contain cell-derived
> markers in addition to virally encoded proteins."

Reading for P4: the strongest prior-art anchor. A **neutralizing antibody** — the
gold-standard serological readout for "this is the virus" — here binds a **host membrane
component (GM2 ganglioside)** carried on the envelope, not a virus-encoded epitope. The authors
frame the effect as "non-specific" neutralization by naïve donors, but the structural point for P4
is independent of that framing: the neutralization readout can be driven by host/cell-derived
material co-carried on the "virus." **Full-text additions — this is decisive:** (i) three monoclonal
IgMs were isolated and their neutralization was "**absolutely dependent on the cell line that
produced the virus**" (same virus, different producer cell → different neutralization), so the
target is host-cell material, not a viral protein; (ii) the epitope is GM2 ganglioside, a
host-membrane glycolipid, confirmed by glycan array and ELISA vs purified GM1/GM2; (iii) present
in **immunologically naïve, virus-unexposed donors** (up to 1/85 titer); (iv) extends to EBOV/SUDV/LUJV
but not a non-enveloped control; (v) the authors explicitly note "**serologic relatedness of
viruses could be misidentified due to apparent cross-reactivity against cell-derived antigenic
determinants**" — the P4 inheritance point stated in the field's own words.

**Ellis et al. 2023** — *SARS coronavirus 2-reactive antibodies in bovine colostrum.*
Can Vet J 64(4):337-43. PMID 37008643.

`[VERIFIED src]` — full text read (`P4W-06`).

Reading for P4 (corrected on full text): the cross-reactivity is **not** primarily a serum/FBS
ingredient effect. The antibodies are "likely the result of responses to epitopes on the spike and
nucleocapsid proteins that are **shared between the 2 betacoronaviruses**" (bovine CoV ↔ SARS-CoV-2)
— i.e. **homotypic shared-epitope cross-reactivity**, and the "reactive" ELISA signal is **not**
neutralizing (cPass and N-capture were negative). Two P4-relevant controls are present: a matched
**uninfected-cell control antigen** (Vero for SARS-CoV-2; rectal-carcinoma cells for BCoV) was
subtracted, and **FBS was used as the negative control** — so this source cuts *against* a naive
"serology can't tell culture material from antigen" reading and belongs on the adversarial side of
the ledger, not the reference-side side.

**Chodavarapu et al. 2026** — *Scalable downstream process for purification/inactivation of
microcarrier-propagated Japanese encephalitis virus antigen.* Zenodo. DOI 10.5281/zenodo.23842428.

`[VERIFIED src]` — full text read (`P4W-11`).

Reading for P4: a non-peer-reviewed (Zenodo, IJCPI) publication whose downstream process is
organized around clearing **host-cell protein (via Cygnus Vero 2G HCP ELISA) and host-cell DNA
(via resDNASEQ qPCR)** from whole-inactivated JEV vaccine antigen grown in (nominally) serum-free
Vero microcarrier culture. It documents, from the developer side, that culture-derived antigen is
understood to contain substantial host material. **Caveats on full text:** it reports host-material
clearance *qualitatively* (no residual HCP/HCD quantities are stated), it is a vaccine-antigen (not
diagnostic-antigen) paper, and it describes an **uninoculated-Vero monolayer negative control** to
"rule out background cellular artifacts" — so both a supporting and a control-side point in one
source. Its methods list "serum-free VP-SFM… and 10% FBS" together, an internal inconsistency worth
noting.

**Sherlock et al. 1986** — HSV-2 AG-4 complement-fixation type specificity. J Clin Microbiol
24(6):1093-7. PMID 3023439. A classic, older demonstration that a commercial CF "viral antigen"
was not type-specific (HSV-1 vs HSV-2 cross-reading), i.e. that antigen-driven serology can read
material other than the intended agent. `[VERIFIED src]` — full text read (`P4W-19`). **Full-text
addition:** the kit antigen is "a **crude lysate of HEp-2 cells infected with HSV-2** … lysed at 4 h",
and the control antigen is a **lysate of uninfected HEp-2 cells** — so the kit *does* ship an
uninfected-lysate control, yet 44% (19/43) of **HSV-1**-positive sera still read positive in the CF
test (vs 81% (34/42) of HSV-2-positive sera); the cross-read is the crude-lysate "viral antigen"
binding shared HSV-1/HSV-2 protein, the strongest direct P4 analogue of a culture-lysate antigen
reading beyond its label.

**Browne et al. 2025** — *Multilayer Fluorescent Immunoassay for Dengue Using Host and Viral
Biomarkers.* Bioconjug Chem 36(7):1474-82. PMID 40503688. Reads **host** biomarkers (MCP-1, IP-10)
*alongside* the viral biomarker NS1. `[VERIFIED src]` — full text read (`P4W-20`). **Full-text
caveat (adversarial):** the host chemokines are measured **deliberately as host-response markers**,
not as a "viral" assay falsely reading host protein; the paper uses recombinant antigens (rMCP-1,
rNS1, rIP-10) and a saline-mock with NS1=0, so it should **not** be read as evidence of a viral
antigen cross-reacting with host material. Held as an adjacent recognition that host material is
diagnostically informative in a "viral" panel, not as a false-read instance.

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
the documents *force* versus *permit*, not to settle it by assertion. The cleanest no-virus-permitted
instances are **Kainulainen 2026** (host GM2 ganglioside neutralizing material in virus-unexposed
donors — no virus needed for the target), and the patient-side anti-reagent results (Song/Kricka/
Costa). **Ellis 2023** is *not* a clean no-virus instance on full text: its cross-reactivity is
homotypic shared beta-coronavirus (BCoV↔SARS-CoV-2) epitopes, so it still presupposes a real BCoV —
recorded here as cross-*virus* shared-epitope, not as serum-ingredient mimicry.

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

`[VERIFIED src]` — full text read (`P4W-15`).

> "The most common human anti-animal antibody interferent is HAMA, which causes both positive and
> negative interferences in two-site mouse monoclonal antibody-based assays."

Reading: the canonical statement of the patient-side (location-D) mechanism. Endogenous human
anti-mouse (or anti-rabbit/cow/sheep/etc.) antibodies bridge or block the assay's own capture/detection
reagents, producing positives that have nothing to do with any virus antigen. Prevalences run
"<1% to 80%." **Full-text addition — the serum/animal route is quantified:** Table 3 lists
**human anti-bovine albumin 43%** (28 healthy subjects) and **human anti-bovine IgG 7%** (blood
donors), alongside anti-mouse IgG up to 80% — the concrete animal-serum/FBS-facing antibodies that
would bind bovine-derived assay reagents, which is the serum-ingredient half of the P4 route.

**Song et al. 2025** — *Resolving heterophile antibody interference in viral serology using blocking
tubes.* Microbiologyopen 14(6):e70098. PMID 41144880.

`[VERIFIED src]` — full text read (`P4W-14`).

> "HBT pretreatment significantly reduced both reactivity levels... and positivity rates (EBV VCA:
> 38/185 [20.5%] to 5/185 [2.7%]; HSV: 92/185 [49.7%] to 5/185 [2.7%])."

Reading: the single most direct measurement. In routine viral IgM serology for common
agents (EBV, HSV, VZV, CMV, rubella, Toxoplasma), up to **49.7%** of HSV IgM "positives" were
heterophile interference — i.e. endogenous antibody binding the assay's *reagents*, resolved by
heterophile-blocking tubes. This is "positive without the named virus," with the bound epitope being
**non-viral** (patient anti-reagent antibody). Same arm as the reference-side evidence; only the
supposed *location* of the non-viral epitope differs. **Full-text additions:** IgG was essentially
unchanged by blocking (interference is IgM-specific); **46 patients** initially read as primary EBV
infection were reclassified; mechanism is patient-derived **anti-animal antibody** (not a property
of culture-derived antigen) — a patient-side route, adjacent to but distinct from the reference-side
culture-reagent mechanism.

**Ye et al. 2021** — false-positive SARS-CoV-2 antibody reasons (PMID 33710634): "the most common
endogenous interferences include rheumatoid factor, heterophile antibodies, human anti-animal
antibodies, lysozyme, complement, and cross-antigens." `[VERIFIED src]` — full text read (`P4W-16`).
**Full-text additions:** lysozyme (a normal host enzyme, pI ≈ 11) physically **bridges** the labelled
and coated IgG to give a false positive — a concrete *host protein* generating signal; the named
"cross-antigens" are **shared coronavirus N/S epitopes** (homotypic, not host mimicry); and the paper
also lists exogenous interferences (specimen contamination, kit-conditioning).

**Kharlamova et al. 2021** (PMID 34012450; `[VERIFIED src]`, `P4W-17`) and
**Costa et al. 2021** (PMID 34336313, isolated false-reactive HBsAg; `[VERIFIED src]`, `P4W-18`) —
further non-viral-epitope instances. **Full-text additions:** Kharlamova = RF/autoantibody interference
(mostly RF, bridging assay reagent IgG), overall false-positive rate **2–45%** across the 13
non-specific commercial assays, RF-positive RA dominant, MS samples clean in all 20 assays. Costa =
heterophile antibody bridging the two reagent antibodies, resolved by blocking tube + an alternate
platform (Abbott Architect) + confirmatory tests; the same heterophile also gave a **false-positive
HIV 1/2/p24 screen** (confirmatory Geenius and HIV-1 RNA both negative).

### What this strand establishes (full-text read)

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

`[VERIFIED src]` — full text read (`P4W-21`).

Reading for P4: a well-controlled disconfirmation. Earlier reports of bornavirus "infection" in
psychiatric patients (largely serological) did not hold up when re-tested with serology plus
independent nucleic-acid and blinded replication assays. A caution against reading any serology
positive (including ours) as evidence for a discrete particle, and an instance where the cognate
agent was *not* found on better-controlled measurement — i.e. consistent with the non-viral-epitope
reading. Not a P4 "win"; a P4 check. **Full-text additions:** 396 subjects (198 matched pairs);
**no sample was positive by ELISA**; 8/396 (2%) were IFA-immunoreactive but **none confirmed by
Western immunoblot** (labeled nonspecific); RT-PCR negative throughout. The assay used recombinant
BDV N/P antigens with a carbonic-anhydrase negative control — so this also shows that *with* adequate
controls the earlier serology-positive claim collapses to negative.

---

## 4e. Net effect of the full-text reads on the prediction (2026-11-08)

Reading the Section-B full texts did **not** uniformly strengthen the earlier abstract-only notes;
it **disciplined** them. Direction is unchanged — the prediction remains open, and its provenance
half is now better documented — but three of the collected cases were re-classified rather than
simply confirmed:

- **Strengthened / decisive (reference-side, non-viral host material):** Kainulainen 2026 (neutralizing
  IgM targets host GM2 ganglioside, virus-unexposed donors) and Sherlock 1986 (a crude infected-cell
  lysate shipped as the "viral antigen" cross-reads).
- **Re-classified as cross-virus, not non-viral:** Ellis 2023 (BCoV↔SARS shared epitopes) and Beier
  2004 (a second contaminant virus's antigen inside the preparation). Both show antigen *impurity*
  distorts serology, but neither shows a *non-viral* host/FBS molecule driving the read.
- **Re-classified as not-false-read:** Browne 2025 (host markers deliberate), Chodavarapu 2026 and
  Hornig 2012 (matched/uninoculated controls present, false positives vanish under controls).

**Net relative to the prediction:** the **provenance** half (reference antigens are culture-lysate /
native / culture-isolate material) is robustly documented across kits *and* papers (inserts P4-001/-002/
-009/-011, Sherlock, Saliki, Diesse Vero-E6, Vircell TESA). The **positive-on-a-non-viral-reagent**
half currently rests on one decisive reference-side anchor (Kainulainen) plus the patient-side
interference literature (Song/Kricka/Costa/Kharlamova), which is the *same non-viral-epitope arm*
at a different location. The still-open empirical question is the **matched-mock score**: whether
the culture-derived reference antigens read positive on their own matched uninfected-culture
material. Kit inserts will *not* answer that (P4-001 shows they treat uninfected cells only as a
counterstain, not a matched antigen; the immunoblot rows P4-009/-011 likewise carry no matched
mock); it is answered by **primary papers**, i.e. the R1 dual-serum Isolation papers that report
serology (TODO 5). The two outstanding vendor inserts (P4W-03/-04) are a *provenance-completeness*
item for the veterinary rows only — not a blocker for the main argument.

---

## 4f. Two sufficiency gaps (recorded 2026-11-08, with Albert)

Two inference gaps qualify how far the census can be read as "the signal is the viral epitope."
Both were pointed out during review; they stand as qualifications over the whole stream.

**(i) The recombinant "escape hatch" does not close the P3 inheritance link.** A recombinant antigen
looks independent because it is a defined protein, not a crude lysate. But recombinance only fixes
*which molecule is produced*, not *whether that molecule is the viral epitope*. The recombinant ORF is
cloned from a "reference strain" whose genome was itself obtained from a culture+CPE-defined Isolate.
Cloning a gene faithfully reproduces the culture-anchored sequence; it does not re-verify that the
sequence came from a distinct particle class. So "recombinant VP7" is recombinant *of whatever the
culture-anchored reference genome calls VP7* — a label reproduced, not an identity re-measured. Truly
independent would require the sequence/analyte to never route through culture+CPE (e.g. mass-spec of a
particle separated by non-culture class-defining biochemistry, or a clinical-direct specimen with an
orthogonal non-culture identity).

**(ii) A nonreactive matched mock does not establish viral-epitope specificity.** The mock subtraction
(test − mock = "the virus") is only sound if test and mock differ *solely* by the viral particles. They
cannot: there is no process that produces a pure viral-particle preparation, so no mock can ever be
"the test minus pure virus." Infection transforms the entire culture — cytopathic degeneration, cell
death and debris, host-protein up/down-regulation, virus–host interaction products (syncytia, membrane
blebs, EVs, stress granules), and altered (depleted/acidified) medium. The infected culture therefore
contains a large class of *non-viral* material that is absent (or differently constituted) in the
healthy mock. A positive-on-infected / negative-on-mock result shows only that the signal requires the
*infected (sickened) state* — not that the reacting molecule is the viral epitope. The mock rules out
*baseline uninfected* reactivity; the viral attribution is then read back through the warrant, not
measured. This qualifies every matched-mock row: Saliki (`P4-019`) and VI14 (`P4-014`) showing a
nonreactive mock do **not** demonstrate an antigen validated against a viral epitope — only that
uninfected cells did not react.

---

## 4g. Recombinant vs culture-direct, and the P3 link (2026-11-08, with Albert)

The census reduces to a two-way antigen-provenance split, plus the P3 upstream trace:

1. **Culture-direct** — the reference antigen or confirmation *is* the culture product (infected
   monolayer / culture lysate / culture supernatant) or a functional read on it (CPE-suppression
   neutralization, FAT/IFA, HA, Western). All nine P4-coded primary-paper serology rows are
   culture-direct (`P4-012`…`P4-021`), as are the culture-lysate kit rows (`P4-001`, `-002`, `-005`, `-009`).
2. **Recombinant** — a defined protein (or an antibody raised against one) stands in for the antigen.
   In the census these are all `recombinant_source_unclear`: the insert names a "recombinant
   VP7 / GP / NP / Borrelia protein" but does **not** state the ORF's source isolate (`P4-004`, `-006`,
   `-008`, `-010`, `-011`).
3. **Synthetic / clinical-direct** — zero rows. The escape route the prediction says would weaken it is
   simply absent so far.

**The logical equivalence (Albert):** a recombinant antigen whose ORF was cloned from a culture+CPE-defined
reference strain is *not* more independent than a culture-direct antigen — it is the same
culture-anchored definition with translation interposed. "Nothing lost in translation" is already
generous: P3 documents that assembling a genotype out of a *mixed culture product* (host RNA, co-carried
agents, EV cargo, medium components) and then assigning which contigs belong to "the virus" is far from
error-free (`p3_genetics/sequence_origins/`). So each recombinant-with-unnamed-ORF row rests on the
chain `cell culture → sequence assembly → recombinant → assay`, every hop assumed error-free, and no
insert discloses the first hop.

**Where P3 has already traced the reference to `culture_cpe`:** measles **Edmonston** (MEA-O1 Crowley
`culture_cpe`, Edmonston/HeLa — the strain behind P4-002's EUROIMMUN lysate and any recombinant measles
antigen), **bluetongue** (BTV-C1/-C2/-O1 `culture_cpe` — behind P4-004's recombinant VP7), and **BVDV**
(NADL plaque-purified on MDBK, `culture_cpe`). A recombinant antigen only escapes if its ORF source
strain — which the inserts do not name — traces `clinical_direct`; P3 finds `clinical_direct` is the
minority, and for SARS-CoV-2 the same label spans both `clinical_direct` (MN908947) and `culture_cpe`
(WIV04), so "recombinant NP" is under-specified.

**Coverage.** All 189 R1 refs classified 2026-11-08 in `p4_r1_roster.csv`: **151 classified / 38
wishlist** (fetch blockers appended to R1's `paywall_wishlist_combined.md`). Of the 151, **96 report a
serology/antigen confirmation, and all but a handful are culture-native** (IFA/FAT/HA/HI/neutralization/
western/IPMA on infected cells or supernatant). Recombinant antigens appear in only a few R1 refs
(VI55 E. coli NP MAb, VI205 scFv-vs-gD, VI38 anti-N MAb against recombinant N) — consistent with §4g's
point that "recombinant" lives mainly in the commercial kit inserts, whose ORFs trace culture-anchored
references.

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