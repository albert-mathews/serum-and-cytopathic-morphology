# Control cultures research framework

**Status:** Draft for iteration (v0.1)  
**Purpose:** Codify an unambiguous tier system (A–D) for classifying **negative / mock / uninfected culture controls** in virus Isolation and related infection–culture papers.  
**Scope of application:** Papers in the Isolation corpus (e.g. `isolation-refs-overview.csv` / PDFs under `wrk/isolation_practice/`), and any later additions scored the same way.  
**Related files:**
- `control-cultures-overview.csv` — machine-readable scores (to be aligned with this framework)
- `isolation-refs-endpoint-analysis-filtering.md` — prior free-text control notes
- `isolation-refs-overview.csv` — FBS / medium extraction (independent dimension)

---

## 1. Why this framework exists

Institutional Isolation practice typically couples:

1. reduced serum / nutrient enrichment at or after inoculation, and  
2. cytopathic effect (CPE) or related culture morphology as a primary viral readout, and  
3. (in principle) parallel negative controls.

This project treats (1)+(2) as a potential confound. Whether publications actually run **proper** negative controls is an empirical question. “Mock mentioned” is not enough: the control must be evaluable as a test of the Isolation culture system.

The A–D tier condenses that evaluation for readers. Tiers must be **mutually exclusive**, **jointly exhaustive** for the corpus, and assignable from the **paper text/figures alone** without guessing what the lab “must have done.”

---

## 2. Core definitions

### 2.1 Isolation (capitalized)

**Isolation** = the operational virology process of detecting, recovering, and/or propagating an agent in culture, where culture outcome (especially CPE) is used as evidence of viral presence or successful recovery.  
An **Isolate** is the culture-derived product of that process. Isolation does **not** imply chemical purity.

### 2.2 Test culture

A culture that receives the **virus source** under study: clinical specimen, animal sample, prior-passage Isolate, recombinant inoculum, or equivalent material the authors treat as the infectious input.

### 2.3 Negative culture control (NC)

A culture intended to show the **baseline culture system without the virus source**, used (or usable) as a comparator for culture morphology / CPE / “infection” claims.

**Counts as NC language** (non-exhaustive): mock-infected, mock-inoculated, uninfected, uninoculated, virus-negative control, sham, vehicle control, diluent-only, PBS/medium-only wells, “control wells without virus,” negative control monolayers.

**Does not by itself count as NC:**
- untreated cells described only as a reagent stock (no parallel experimental role)
- “normal cells” in a cartoon with no methods
- sequence-negative clinical cases used only as PCR controls with no culture arm
- isotype antibody controls, secondary-only IF controls, no-template PCR controls (assay controls, not culture NCs)

### 2.4 Positive culture control (PC)

A culture inoculated with a **known** virus or agent expected to produce the endpoint.  
**PC is recorded separately.** It does **not** raise the negative-control tier. Absence of PC does not lower the NC tier.

### 2.5 Isolation-stage vs non-Isolation-stage

**Isolation-stage** = the culture phase in which the authors:

- perform primary Isolation from specimens, and/or  
- propagate / infect cultures for the purpose of reading **CPE or equivalent culture morphology** as evidence of virus, and/or  
- decide “CPE-positive vs CPE-negative” / harvest based on culture appearance.

**Non-Isolation-stage (downstream or other module)** = controls used only for:

- Western blot / immunoblot loading comparisons  
- immunofluorescence or microscopy of a **separately described** expression experiment  
- PCR/qPCR assay validation  
- neutralization assay plates when Isolation itself had no NC  
- toxicity matrix rows that are not the Isolation morphology comparator  
- animal or clinical arms with no matched culture NC  

A paper may have excellent downstream NCs and still score poorly for Isolation-stage NC.

### 2.6 Matched conditions (for tier A)

Test cultures and NC cultures are **matched** if and only if **all** of the following are satisfied by **explicit statement** or by **allowed inference** (Section 4):

| # | Dimension | Requirement |
|---|-----------|-------------|
| M1 | **Cell system** | Same cell type/line (or same co-culture system) as the test cultures being controlled |
| M2 | **Base medium** | Same basal medium family as stated for test cultures (e.g. DMEM, MEM) |
| M3 | **Serum / nutrient enrichment** | Same serum type and concentration **trajectory** as test cultures for the comparable phase (including reduced maintenance / viral medium if test cultures use it) |
| M4 | **Other medium additives** | Same antibiotics, antimycotics, trypsin/TPCK, etc., except differences that **only** implement “no virus source” (e.g. diluent instead of specimen) |
| M5 | **Handling timeline** | Same adsorption / incubation / observation schedule in kind (parallel experiment), not a materially different duration regime unless the paper states the NC followed the same schedule |
| M6 | **Inoculum difference** | The intended experimental difference is absence of virus source: no inoculum, vehicle/diluent only, sterile PBS/medium, or inactivated/non-infectious input **only if** the paper’s claim is specifically about that contrast (see edge cases) |

**Not required for “matched” (but recorded as quality flags):**
- equal number of replicate wells  
- blinding of CPE scoring  
- public raw images  
- same plate vs parallel plates  

**Fails match** if any of M1–M6 is **contradicted** by the text, or if M3 cannot be established when test cultures use a reduced-enrichment infection medium (serum match unknown ⇒ not tier A).

### 2.7 Explicit vs inferred

- **Explicit:** the paper states control medium, serum %, cells, and parallel handling in methods, figure legend, or results with clear protocol force.  
- **Inferred (allowed only per Section 4):** e.g. “all wells received maintenance medium (DMEM + 2% FBS)” and “control wells received PBS instead of sample.”  
- **Guesswork (forbidden):** “they would have used the same medium,” “standard practice implies mock controls,” “uninfected cells must mean matched.”

---

## 3. Tier system (A–D)

Tiers are ordered by **adequacy of Isolation-stage negative culture control** for interpreting CPE / culture morphology under the paper’s own Isolation or infection conditions.

| Tier | One-line meaning | Reader takeaway |
|------|------------------|-----------------|
| **A** | Isolation-stage NC with **verified matched** conditions (incl. serum/enrichment) | Proper parallel NC for the culture system as run |
| **B** | Isolation-stage NC **mentioned**, but match **not verifiable** (under-specified) | NC claimed; cannot audit identity of conditions |
| **C** | Culture NC present, but **wrong stage** and/or **explicitly unmatched** conditions | Control exists; does not adequately control Isolation CPE under test conditions |
| **D** | **No** culture-level NC described for Isolation/infection culture work | No culture NC to evaluate |

**Ordering for conservatism:** A > B > C > D (A best).  
When assignment is genuinely ambiguous between two adjacent tiers after applying the decision tree, assign the **worse** tier (lower letter quality: toward D) and flag `ambiguous=yes` with a note.

---

## 4. Allowed inference rules

Use these so “matched” is strict but not absurdly pedantic.

### 4.1 Allowed (can support tier A)

1. **Universal medium statement:** A methods sentence applies to all experimental wells/plates (e.g. “cells were maintained in DMEM + 2% FBS after inoculation”) **and** NC wells are on that experiment (same plate or same protocol paragraph).  
2. **Diluent substitution:** Test wells get specimen/virus in diluent D; control wells get diluent D only; medium thereafter described once for the plate.  
3. **Same-plate controls:** “One well per plate received PBS instead of sample” + single post-inoculation medium for the plate.  
4. **Shared protocol pointer:** “Mock infections were performed identically except that medium alone was added” **and** the infection medium is defined in that section.  
5. **Figure + methods consistency:** Figure shows “mock” and methods define mock as uninoculated under the stated infection medium.

### 4.2 Not allowed (blocks tier A; usually tier B or C)

1. Word **mock** / **uninfected** with **no** medium, serum, or “identical conditions” language.  
2. Assuming ATCC/CLSI practice was followed though uncited in the paper.  
3. Assuming pre-inoculation growth medium (e.g. 10% FBS) continued post-inoculation for controls when test cultures switched to 2%.  
4. Treating downstream “uninfected lysates” as proof of Isolation-stage matched NC.  
5. Equating “CPE-negative specimen” (test well that did not show CPE) with a negative **control** culture.  
6. Equating patient-negative PCR with culture NC.

### 4.3 Serum / enrichment special rule (central to this project)

If test cultures for Isolation/infection use **reduced** serum or altered nutrient enrichment relative to growth medium, then for **tier A**:

- the NC must be shown to use that **same reduced / altered** regime, **or**  
- a single protocol must clearly apply that regime to test and NC alike.

If the paper is silent on NC serum while test cultures clearly use reduced serum → **not A** (typically **B** if Isolation-stage NC is named; **D** if no NC).

If the paper states NC remained in high serum while test cultures were reduced → **C** (explicit mismatch on M3).

---

## 5. Decision tree (mandatory assignment order)

Score **one primary experiment** per paper (Section 6), then apply steps **in order**. Stop at the first tier that fits.

```
Step 0  Select primary experiment (Section 6).
        Extract quotes for any NC language.

Step 1  Is there ANY culture-level NC (Section 2.3) for virus
        Isolation or infection culture work in this paper?
        │
        NO ──► Tier D
        │
        YES
        ▼
Step 2  Is at least one NC Isolation-stage (Section 2.5)
        for the primary experiment?
        │
        NO ──► Tier C   (NC only wrong-stage / other module)
        │
        YES
        ▼
Step 3  Are matched conditions (M1–M6) established by explicit
        statement or allowed inference (Section 4)?
        │
        YES, all M1–M6 hold ──► Tier A
        │
        NO — conditions are stated and at least one of M1–M6
        is contradicted (unmatched) ──► Tier C
        │
        NO — Isolation-stage NC exists but one or more of M1–M6
        cannot be verified (under-specified / silent) ──► Tier B
```

### 5.1 Tie-break and multi-NC papers

- If multiple NCs exist, classify using the **best** Isolation-stage NC that the paper actually documents (do not invent a better control than written).  
- If the best Isolation-stage NC is B and a downstream NC is well specified, tier remains **B** or **A** from Isolation-stage only; record downstream NC in flags, do not upgrade tier from downstream alone.  
- If Isolation-stage NC is unmatched (**C**) and a better matched NC exists only downstream, tier remains **C** for Isolation-stage adequacy; note downstream separately.  
- **PC only, no NC** → **D** (optional flag `positive_control_present=yes`).

### 5.2 What tier C covers (two sub-reasons; same tier)

Both map to **C** (same letter; distinguish in `c_reason`):

| Code | Meaning |
|------|---------|
| `C-stage` | NC only non-Isolation-stage |
| `C-mismatch` | Isolation-stage NC with explicit condition mismatch |
| `C-both` | Both |

Do **not** split C into separate top-level tiers unless a later revision demands it; one letter keeps the reader model simple.

### 5.3 What tier B is (and is not)

**B** = authors assert an Isolation-stage NC, but the reader **cannot verify** match—especially serum/enrichment identity.

**B is not** “bad science” by definition; it is **under-reported relative to the confound we care about**.

---

## 6. Selecting the primary experiment

Many papers mix clinical Isolation, lab propagation, plaque assays, and molecular follow-ups.

**Priority order** for which experiment’s NC is scored for the tier:

1. **Primary Isolation from clinical/field specimens** (first recovery claims).  
2. Else **propagation / infection** used to claim CPE as virus evidence for an Isolate.  
3. Else **main in vitro infection** where CPE or culture morphology is a stated infection endpoint.  
4. Else, if no CPE morphology endpoint, score NC for the culture infection arm that defines “infected vs not” (and note `endpoint_not_cpe=yes`).

Record in the datasheet:

- `primary_experiment` — short label  
- `endpoint_for_control_comparison` — e.g. CPE, plaque, IF foci, mixed  

If primary Isolation has **D** but a later lab infection has **A**, still score tier on **primary Isolation** when the paper’s Isolation claim is what we are evaluating; record `secondary_experiment_tier` optionally.  
**Default rule for this project:** tier = NC quality for the experiment that supports the paper’s **Isolation / virus-detection-in-culture** claim most directly (usually #1 or #2 above).

---

## 7. Extraction fields (codified)

Each scored paper gets one row (or one row per scored experiment if multi-row mode is enabled later).

### 7.1 Identity

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Corpus ID (e.g. VI14) |
| `citation` | string | Short cite |
| `scorer` | string | Who applied the tree |
| `score_date` | date | ISO date |
| `primary_experiment` | string | What was scored |
| `endpoint_for_control_comparison` | string | CPE / other |

### 7.2 Decision outputs

| Field | Type | Allowed values |
|-------|------|----------------|
| `tier` | enum | `A`, `B`, `C`, `D` |
| `c_reason` | enum | `NA`, `C-stage`, `C-mismatch`, `C-both` |
| `ambiguous` | bool | `yes` / `no` |
| `ambiguity_note` | text | Required if ambiguous |

### 7.3 NC presence and stage

| Field | Type | Allowed values |
|-------|------|----------------|
| `nc_any` | bool | Culture-level NC anywhere for infection/Isolation work |
| `nc_isolation_stage` | bool | Isolation-stage NC for primary experiment |
| `nc_downstream_only` | bool | NC only non-Isolation-stage |
| `nc_labels` | text | Words used: mock, uninfected, PBS well, … |

### 7.4 Match checklist (Isolation-stage NC only; else `NA`)

| Field | Type | Allowed values |
|-------|------|----------------|
| `m1_cells` | enum | `yes`, `no`, `unknown`, `NA` |
| `m2_base_medium` | enum | `yes`, `no`, `unknown`, `NA` |
| `m3_serum_enrichment` | enum | `yes`, `no`, `unknown`, `NA` |
| `m4_additives` | enum | `yes`, `no`, `unknown`, `NA` |
| `m5_timeline` | enum | `yes`, `no`, `unknown`, `NA` |
| `m6_inoculum_only_diff` | enum | `yes`, `no`, `unknown`, `NA` |
| `match_basis` | enum | `explicit`, `allowed_inference`, `mixed`, `NA` |

**Tier A requires:** `nc_isolation_stage=yes` and all of `m1`–`m6` = `yes`.  
**Tier B:** `nc_isolation_stage=yes` and no `m*` = `no`, but at least one `m*` = `unknown`.  
**Tier C-mismatch:** `nc_isolation_stage=yes` and at least one `m*` = `no`.  
**Tier C-stage:** `nc_isolation_stage=no` and `nc_any=yes`.  
**Tier D:** `nc_any=no`.

If both some `m*=no` and some `m*=unknown`, prefer **C-mismatch** (contradiction beats mere silence).

### 7.5 Outcome and evidence quality (flags — do not change tier alone)

| Field | Type | Description |
|-------|------|-------------|
| `control_cpe_reported` | enum | `yes`, `no`, `NA` — morphology/CPE of NC discussed |
| `control_cpe_claimed_negative` | enum | `yes`, `no`, `partial`, `NA` |
| `control_images` | enum | `yes`, `no`, `unclear` |
| `blinded_scoring` | enum | `yes`, `no`, `unclear` |
| `positive_control_present` | enum | `yes`, `no`, `unclear` |
| `quotes_nc` | text | Verbatim quotes (methods + results) |
| `quotes_medium_test` | text | Test culture medium at infection |
| `quotes_medium_nc` | text | NC medium if any |
| `notes` | text | Free text |
| `exclude_from_corpus` | bool | If paper excluded from Isolation set for other reasons |
| `exclude_reason` | text | e.g. CPE not an endpoint |

### 7.6 Minimal CSV profile (if full sheet is too wide)

For a compact `control-cultures-overview.csv`:

```text
id,tier,c_reason,nc_any,nc_isolation_stage,m3_serum_enrichment,match_basis,control_cpe_reported,control_cpe_claimed_negative,ambiguous,quotes_nc,notes
```

Full checklist can live in a wider table or in per-paper notes under `isolation-refs-endpoint-analysis-filtering.md`.

---

## 8. Worked sketches (illustrative; re-score from PDFs when applying)

These are **training examples** from prior notes. Final corpus scores must re-apply this tree to the PDF.

| ID | Likely tier | Why (sketch) |
|----|-------------|--------------|
| VI paper with no mock/uninfected/control wells | **D** | `nc_any=no` |
| “Mock-infected cells” only in WB/IF methods; Isolation methods silent | **C** | `C-stage` |
| “Mock-infected cells (Fig. 1A); CPE not observed in mock” but infection medium for mock never stated | **B** | Isolation-stage NC language; M3/M2 unknown |
| Same plate: sample vs PBS; all wells then DMEM+2% FBS; CPE compared | **A** | Allowed inference; M1–M6 hold |
| Test cultures in 2% FBS; controls “maintained in 10% FBS” | **C** | `C-mismatch` on M3 |
| Uninfected cells digested for RNA alongside CPE-positive cells; no statement they were cultured under infection medium | **B** or **C** | If presented as parallel Infection NC → B if silent on medium; re-read context |
| Only CPE-positive known-virus control, no negative | **D** | PC ≠ NC |

**VI14 (from prior extract):** uninfected (mock) Hep-2 mentioned; limited medium detail for mock → lean **B** unless PDF establishes same maintenance medium for mock and inoculated wells by allowed inference.  
**VI13 (from prior extract):** mock-infected cells; CPE not observed in mock; if methods apply one medium to inoculated and mock → may be **A**; if mock only named in results/figure → **B**.  
*These two must be formally re-scored; do not treat this table as final data.*

---

## 9. Edge cases

| Case | Ruling |
|------|--------|
| Blind passage of CPE-negative **specimens** | Those are test cultures, not NCs |
| UV-inactivated virus as “control” | Not NC for “no inoculum” morphology unless the claim is specifically inactivated vs live; usually **not** tier A NC; record as special contrast; if only control present, tier **C** or **D** depending on whether live-uninoculated NC also exists |
| Matrix toxicity controls (semen, milk) without virus | May be Isolation-stage NC if parallel and matched medium except matrix; score M1–M6 carefully; matrix ≠ pure medium NC but can still be A for “no virus” if that is the intended contrast |
| Different cell line as “control” | **C-mismatch** (M1 fails) if offered as NC for morphology on the test line |
| Serum-free + trypsin infection; mock also serum-free + trypsin | Can be **A** (enrichment matched at 0% serum) |
| Paper uses IFA not CPE as Isolation endpoint | Still score NC tier for the culture infection arm; set `endpoint_for_control_comparison` accordingly; may `exclude_from_corpus` for CPE-specific analyses |
| Review article / no methods | **D** or exclude from corpus |
| “Control” means positive control only | **D** for NC tier; `positive_control_present=yes` |

---

## 10. Relationship to institutional “parallel negative controls”

Guidelines may require or recommend uninoculated / mock controls. This framework does **not** score guidelines (unless we later apply the same tree to protocol documents).  

It scores **whether a given publication’s methods, as written, implement an audit-able Isolation-stage NC**.

Mapping (informal):

| Institutional ideal | Framework |
|---------------------|-----------|
| Parallel uninoculated cultures, same maintenance medium, same observation | **A** |
| “Include controls” without specifying identity | Publication often lands **B** or **D** |
| Controls only for reagents/assays | **C** or **D** |

---

## 11. Relationship to the FBS / enrichment confound

This tier system is **necessary but not sufficient** for the serum-matched control interpretation.

- **Tier A** means: a proper no-virus culture existed under the same medium regime. If authors report NC without CPE while test wells show CPE, that is **their** claimed specificity under matched conditions—still subject to imaging quality, blinding, and whether serum reduction itself was ever tested as an IV (it usually was not).  
- **Tier A does not mean** the authors ran a serum-only factorial (10% vs 2% without virus). That experiment is the CRO / dedicated control study, outside this tier.  
- **Tiers B–D** mean the publication does not document a verifiable matched NC for Isolation-stage morphology, which limits how strongly one can claim that CPE was shown to be inoculum-specific in that paper.

Optional future flag (not part of A–D):

| Field | Meaning |
|-------|---------|
| `serum_factorial_on_uninoculated` | Did they vary serum on uninoculated cells? (almost always `no`) |

---

## 12. Scoring procedure (workflow)

1. Confirm paper is in scope (Isolation / infection culture methods present).  
2. Read methods + figure legends + results sentences that mention mock/uninfected/control wells.  
3. Select `primary_experiment`.  
4. Fill quotes (`quotes_nc`, medium quotes).  
5. Apply decision tree (Section 5); fill `m1`–`m6`.  
6. Assign `tier` and `c_reason`.  
7. Fill outcome flags (CPE reported on NC, etc.).  
8. If unsure, set `ambiguous=yes`, choose worse tier, write `ambiguity_note`.  
9. Second scorer (if used): independent tier; resolve disagreements by re-reading PDF against Section 5; record final tier.

**Disagreement rule:** final tier = worse of the two if unresolved; or consensus after quote-level review.

---

## 13. Reporting in the paper

Recommended reader-facing summary:

- Count and percent in each tier A–D for the CPE-endpoint Isolation corpus.  
- Separate: fraction with `control_cpe_claimed_negative=yes`.  
- Highlight: fraction with `m3_serum_enrichment=yes` (serum-matched NC).  
- Do not equate “mock mentioned” with tier A.

Example sentence shapes:

- “Of N Isolation papers, X% were tier D (no culture NC described); Y% tier B (NC named, conditions not verifiable); Z% tier A (matched Isolation-stage NC).”  
- “Serum-matched Isolation-stage NCs (`m3=yes`) were limited to …”

---

## 14. Out of scope (for this document)

- Historical serum-use survey (~1900 → institutional lock-in) — separate workstream.  
- EV / purification controls.  
- Whether institutional protocols themselves are tier A (can be scored later with the same tree).  
- CRO experiment — reference standard for serum-only design; not a corpus paper tier.

---

## 15. Revision log

| Version | Date | Change |
|---------|------|--------|
| v0.1 | 2026-07-20 | Initial codification: definitions, M1–M6, decision tree, A–D, fields, edge cases |

---

## 16. Open items for iteration

- [ ] Confirm default when primary Isolation is D but lab propagation is A (keep primary-only vs dual reporting).  
- [ ] Whether UV-inactivated / heat-inactivated arms need a named sub-flag beyond edge table.  
- [ ] Whether plaque-assay “cell control” wells without virus automatically inherit infection overlay medium (usually yes → often A if stated).  
- [ ] Align/replace columns in `control-cultures-overview.csv` with Section 7.6.  
- [ ] Dual-scorer pilot on 5 PDFs to test ambiguity rate.  
- [ ] Add 2–3 fully quoted gold-standard examples (one A, one B, one D) after PDF re-read.

---

*End of framework. Iterate in place; bump version in Section 15.*
