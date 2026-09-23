# P2 research protocol — EV / virion particle indistinguishability

**Status:** v0.1 — Round 0 scaffold + Round 1 seed/search active  
**Related thesis:** Combined CPE non-specificity + particle-layer prediction (see `grok.md`, `p2.md`, `p2_HANDOFF.md`)  
**Stance:** There is no required outcome that “EVs and virions are the same.” The goal is to learn what the **published record** says about whether physical purification, morphology, density, size, markers, and related metrics can **uniquely define** culture-derived “virions” versus host extracellular vesicles (EVs)—and when that problem entered and remained in the literature.

---

## 1. What P2 is (and is not)

### 1.1 Motivating interest (P2)

If Isolation under dual-media + CPE never uniquely grounded a second particle class, a natural particle-layer prediction is:

> Purification / EM / biophysical fractionation of culture products will not cleanly separate “virions” from host EVs under the conditions that produced the Isolate.

P2 tests whether **field literature** supports that prediction as a recognized, multi-metric, historically persistent problem—not a slogan invented for this paper.

### 1.2 What would count as learning (any is success)

| Outcome class (descriptive) | Meaning for readers |
|-----------------------------|---------------------|
| Multiple independent metrics of overlap / co-purification | Dilemma is multi-dimensional, not one technique’s failure |
| Explicit field statements that complete physical separation is not guaranteed | Consensus language exists (quote-backed) |
| Methods that *do* separate (affinity, infectivity, capsids, multi-marker) | Counterexamples / partial solutions; bounds the claim |
| Continuum / hybrid / defective-particle models | Dual classification not forced by observation alone |
| Historical trail of co-pelleting / “contaminants” / defective particles → modern EV–virus reviews | Problem is not “late technical annoyance” only |
| Sparse or contradictory record | Limits what Discussion may claim |

**Interpretation of “expected if second class never grounded” is Discussion-only after extraction freezes.**

### 1.3 Explicit non-goals

- Claims limited to what the cited corpus documents about particle co-purification / class-label under-determination.
- Not a full EV biogenesis treatise (van Niel–type reviews are **background**, useful only if they speak to isolation/purity/overlap).  
- Not limited to authors affiliated with known collaborators (anti-cherry-pick rule).  
- Not limited to reviews; prefer primary methods/separation papers when available.  
- Not re-proving CPE non-specificity (R streams).

---

## 2. Scope boundaries

### 2.1 Time window

| Bound | Rule |
|-------|------|
| **Start** | ~**1950s–1960s** for EM/density/ultracentrifuge co-contamination language; earlier only if citation chain forces (defective interfering particles, “cellular debris” in virus preps) |
| **End** | **Present** — does the dilemma continue in current methods literature? |

Historical aim: date **when** co-isolation / indistinguishability language appears and whether it **persists**.

### 2.2 Inclusion

Include if substantial content on **any**:

- Physical or biochemical **co-purification / co-isolation** of EVs (exosomes, microvesicles, ectosomes, membrane vesicles) with virus particles  
- **Failed or incomplete separation** by size, density, charge, precipitation, filtration, SEC, TFF, UC  
- Morphological / EM **overlap** of culture-derived nanoparticles  
- Shared **biogenesis pathways** used to argue structural/functional relatedness **and** purification difficulty  
- **RNA/protein cargo attribution** problems when EV and virion fractions co-migrate  
- Defective / noninfectious particles as intermediate entities in the continuum  
- Primary separation protocols that claim EV–virus discrimination (useful as methods + potential counterexamples)

### 2.3 Exclusion (default)

- Pure therapy/delivery engineering with no purification or identity claims  
- Cancer EV biomarkers with no viral particle comparison  
- News, blogs, social media  
- Papers with zero methods or zero identity/separation language after full-text → **N** (still logged)

### 2.4 Metrics taxonomy (extract against these)

| Code | Metric / axis |
|------|----------------|
| M-SIZE | Diameter / NTA / DLS overlap |
| M-DENS | Buoyant density / gradient band overlap |
| M-UC | Differential / ultra-centrifugation co-pelleting |
| M-PEG | Crowding-agent / commercial kit co-precipitation |
| M-SEC | Size-exclusion chromatography co-elution |
| M-TFF | Tangential / cross-flow filtration co-retention |
| M-EM | TEM / cryo-EM morphology non-discriminating |
| M-LIPID | Shared lipid composition (cholesterol, raft lipids) |
| M-PROT | Shared host proteins (tetraspanins, ESCRT, etc.) |
| M-RNA | Co-purifying / mis-attributed RNA (miRNA, viral RNA) |
| M-INF | Infectivity vs particle count / noninfectious majority |
| M-MARK | Marker-based affinity (CD63 etc.) separation claims |
| M-CONT | Continuum / hybrid / Trojan / defective-particle framing |
| M-HIST | Explicit historical statement of co-contamination |

---

## 3. Epistemic rules (bias control)

1. **Pre-register query families** for each round; log mid-round extras as new sub-round.  
2. **Log every screened source** Y / N / B with one-line reason.  
3. **Extract same fields** from useful sources whether or not they support indistinguishability.  
4. **Prefer primary methods language** over review narrative when they conflict; record both.  
5. **Do not upgrade silence** into “everyone knows EVs and virions cannot be separated.”  
6. **Negative search is a result.**  
7. **Devil’s advocate:** actively seek papers claiming **successful** EV–virus separation.  
8. **Anti-colleague bias:** Round 1 may include known seeds; Round 2+ must expand beyond Dittmer / Raab-Traub / Nolte-’t Hoen / Margolis / Gould seed neighborhood.  
9. **Stop on thoroughness**, not preferred narrative.

---

## 4. Deliverables

| Artifact | Purpose |
|----------|---------|
| `P2_research.md` | This protocol |
| `P2_search_log.md` | Round queries, dates, hit notes, decisions |
| `P2_screened.csv` | Every citation screened |
| `P2_useful.csv` | Useful sources + metric extraction |
| `P2_quotes.md` | Verbatim separation / overlap quotes |
| `P2_synthesis.md` | After ≥2 rounds; patterns + limits |
| `agent_reviews/` | Independent agent re-reads / feedback |
| `refs/` | Local PDFs only (**gitignored**) |

IDs: **`P2-001`**, `P2-002`, … assigned at first screen, never reused.

Existing folder PDFs (8) are **Round 1 seeds** with IDs assigned at first formal screen.

---

## 5. Multi-round design

### Round 0 — Scaffold
Freeze protocol; empty CSVs; define metrics.

### Round 1 — Seeds + transparent high-bias start
- Screen 8 local `refs/` PDFs.  
- Harvest their cited foundational papers (Gould 2003, Théry/ISEV, early EM co-pellet language).  
- Log as `seed_*` / `snowball_*`.

### Round 2 — Systematic web / PubMed-style queries (pre-registered)

**Family A — separation failure language**  
`extracellular vesicles` OR exosomes AND (virus OR virion) AND (co-purif* OR co-isolat* OR “cannot separate” OR indistinguishable OR “similar size” OR “overlapping density”)

**Family B — method-specific**  
UC / density gradient / PEG / SEC / TFF / “size exclusion” + virus + exosome/EV

**Family C — cargo attribution**  
RNA packaged virion vs EV; miRNA virus particles contamination

**Family D — counterexample hunters**  
separate OR purify OR discriminate EVs from virus / virions (successful methods)

**Family E — historical**  
defective interfering particles membrane; virus purification cellular debris ultracentrifuge; “exosome” virus 1990s–2005

**Family F — standards**  
ISEV MISEV virus; purity EV preparation viral

### Round 3 — Citation snowball depth ≤2  
From useful Y rows.

### Round 4 — Adversarial  
Falsify “always inseparable”; collect successful affinity/infectivity separations; non-enveloped virus cases; plant/bacteriophage if relevant contrast.

### Round 5 — Saturation + agent replication  
Independent agents re-screen sample; log agreement.

---

## 6. Extraction schema (`P2_useful.csv`)

| Field | Description |
|-------|-------------|
| `id` | P2-### |
| `year` | |
| `authors` | |
| `title` | |
| `citation` | |
| `document_type` | primary_methods / primary_experimental / review / perspective / standard / other |
| `virus_or_system` | |
| `metrics_coded` | Semicolon-separated M-* codes |
| `states_incomplete_physical_separation` | yes / no / partial / unclear |
| `claims_successful_separation` | yes / no / partial / unclear |
| `separation_methods_discussed` | free text |
| `historical_claim` | free text or none |
| `quotes_key` | short verbatim |
| `supports_dilemma` | Y / N / mixed |
| `counterexample_value` | Y / N |
| `fulltext` | Y / N / abstract_only |
| `extractor` | |
| `extract_date` | |
| `confidence` | high / medium / low |
| `notes` | |

---

## 7. Screening codes (`P2_screened.csv`)

| Field | Values |
|-------|--------|
| `id` | P2-### |
| `year` | |
| `authors` | |
| `title` | |
| `journal_or_source` | |
| `citation` | |
| `doi` | |
| `pmid` | |
| `useful` | Y / N / B |
| `reason` | one line |
| `fulltext` | Y / N / paywall / abstract_only / not_found |
| `lead_source` | seed / web_q# / snowball_from_P2-### / agent / other |
| `round` | |
| `metrics_hint` | optional M-* from abstract |
| `notes` | |

**Not-useful reasons:** `no_separation_or_identity` · `therapy_only` · `no_virus` · `no_EV` · `duplicate` · `unobtainable` · `secondary_thin` · `language_not_processed`

---

## 8. Double-check

- Agents re-read assigned PDFs/abstracts; write `agent_reviews/P2_agentN_*.md`.  
- Primary synthesizer consumes agent feedback before freezing `P2_synthesis.md`.  
- Quotes for **Y** rows verified against full text when PDF available.

---

## 9. PDF request rule

If a source is **high priority** (explicit separation claims, primary methods, historical firsts) and full text is not in `refs/`, **stop and ask the user to fetch the PDF** rather than over-claiming from abstracts.

---

*End of protocol v0.1*
