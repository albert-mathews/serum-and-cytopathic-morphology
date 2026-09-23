# P1 historical research protocol

**Status:** Draft plan (v0.1) — execute after Isolation control-tier work is frozen  
**Related thesis:** Combined CPE non-specificity + particle ontology paper  
**Stance:** There is no required historical outcome. The goal is to learn what the published record says about serum / nutrient enrichment in virus–tissue / virus–cell culture, and to demonstrate that the search was thorough enough that absence of a pattern is informative, not just a failed hunt for a preferred story.

---

## 1. What P1 is (and is not)

### 1.1 Motivating interest (P1)

If standard Isolation practice couples **reduced serum / nutrient enrichment** at or after inoculation with **culture endpoints** (especially CPE) that are treated as evidence of virus, a natural historical question is:

> How did serum and related nutrient enrichment actually appear in published virus culture work **before** that recipe was locked into institutional laboratory protocols? Does the record show a recoverable pattern of use (including any shift toward lower enrichment at infection), or does the step mainly appear already as assumed practice?

This interest is **reader-facing and discovery-oriented**. It is **not** a pass/fail test of the paper’s main empirical claims (those rest on contemporary guidelines, Isolation corpus, control tiers, and the CRO experiment).

### 1.2 What would count as learning (any of these is success)

| Outcome class (descriptive, not scored as “win”) | What it would mean for readers |
|--------------------------------------------------|--------------------------------|
| Clear early statements of **reduced enrichment at infection / long observation** | Practice is old; modern 2% FBS is a late label for an older pattern |
| Comparative work (richer vs poorer medium) judged by culture readout | Published optimization (or attempted optimization) exists |
| Practice stated without comparison or origin | Early **lock-in / transmission** without a published genealogy |
| Heterogeneous rationales when reasons appear | No single evidence-based “why” in the record |
| Sparse specification of enrichment | Methods opacity; limits historical inference |
| No recoverable pre-institutional trail of the modern step | Institutional codification may have outrun published evolutionary narrative |

**Interpretation of consistency with “empirical lock-in / selection on culture endpoints” is deferred to Discussion after extraction.** Rounds of search are not stopped when a preferred narrative appears, and not extended only to avoid an unpreferred one.

### 1.3 Explicit non-goals

- Not organized as pre- vs post-Enders (or any celebrity breakpoint). Named workers and years **fall where sources place them**.
- Not limited to the string “FBS” or “2%.”
- Not required to find a high→low serum evolution graph.
- Not a full history of tissue culture or of filtration / “virus” ontology (those may appear only if sources force them).
- Not an etiology study; documents Isolation-medium practice only.

---

## 2. Scope boundaries

### 2.1 Time window

| Bound | Rule |
|-------|------|
| **Start** | Approximately **1900** (practical floor for published virus work involving tissue or cell culture; earlier only if a citation chain forces it) |
| **End** | Appearance of **institutional / standard laboratory protocols** that **prescribe** growth vs maintenance (or reduced enrichment at infection) as standard Isolation practice |

**Operational end criterion (not a fixed year in advance):**  
Stop *forward expansion* of the evolution search once multiple independent standard sources treat the medium step as **prescribed practice** (manuals, national lab procedures, widely adopted diagnostic guidance). Record the earliest clear institutional hits as **window-end markers**. Literature after that point is out of scope for P1 *evolution* search (it is transmission/codification). Contemporary guidelines (CLSI, ATCC, ASM, etc.) remain in the **main paper** as current practice, not as P1 discovery targets.

### 2.2 Inclusion (content)

Include a source if it is primarily about, or contains a substantial methods description of:

- Virus isolation, propagation, titration, or cytopathogenicity / degeneration in **tissue culture, explants, primary cells, or continuous cell lines**; and  
- Medium composition is stated or clearly implied for growth and/or infection / maintenance / observation phases.

Also include:

- Early media papers **only when** they are used in virus work or explicitly for viral maintenance (otherwise log as screened-not-useful).  
- Diagnostic manuals and institutional protocols **only** as needed to **date the end** of the window and characterize lock-in.

### 2.3 Exclusion (default)

- Pure animal passage / egg work with no tissue or cell culture arm (unless used only as contrast, logged separately).  
- Modern Isolation papers already in the Isolation corpus (post-institutional; wrong window for P1).  
- Pure EV / purification literature (other workstream).  
- News, blogs, social media.  
- Sources with zero usable medium information after full-text check → **screened not useful** (still logged).

### 2.4 Functional definition of the variable of interest

**“Serum / nutrient enrichment”** means humoral or nutritional richness of the medium relative to basal salt/medium alone, including:

- % or qualitative amount of serum (fetal bovine, calf, horse, human, ox, etc.)  
- Serum ultrafiltrate, plasma, plasma clot  
- Embryo extract, tissue extract, peptone, tryptose, BSA, protein hydrolysates  
- Explicit “growth medium” vs “maintenance medium” / “maintenance fluid” language  
- Serum-free + defined additives (trypsin, etc.) when used as the infection regime  

**Modern “10% → 2% FBS”** is one **codified instance** of a broader pattern (reduced enrichment at infection or long-term observation relative to propagation), not the only searchable form.

---

## 3. Epistemic rules (bias control)

These rules are mandatory for every round.

1. **Pre-register the query set for the round** before deep reading (Section 5). Do not add “just one more” confirmatory query mid-extraction without logging it as a new round.  
2. **Log every screened source** as Useful / Not useful / Borderline, with a one-line reason.  
3. **Extract the same fields** from useful sources (Section 6) whether or not they support lock-in, reduction, or high serum throughout.  
4. **Prefer primary methods language** over secondary historical narrative when they conflict; record both.  
5. **Do not upgrade silence** into “they must have used 2% FBS.” Unknown stays unknown.  
6. **Negative search is a result:** document strategies that returned no hits or only not-useful hits.  
7. **Devil’s advocate pass** each major round (Section 8): actively seek counterexamples to any emerging pattern.  
8. **Separation of roles when possible:** extractor ≠ sole interpreter of “what this means for P1.” Interpretation memo only after a round’s extraction table is frozen.  
9. **Stop rules are about thoroughness, not about liking the answer** (Section 9).

---

## 4. Deliverables (artifacts to maintain)

| Artifact | Purpose |
|----------|---------|
| `P1_research.md` | This protocol (versioned) |
| `P1_search_log.md` | Round-by-round queries, databases, dates, hit counts, decisions |
| `P1_screened.csv` | Every citation screened: id, year, cite, source_of_lead, useful (Y/N/B), reason, fulltext_obtained (Y/N) |
| `P1_useful.csv` | Useful sources only + extraction fields (Section 6) |
| `P1_quotes.md` or per-id notes | Verbatim medium / rationale / endpoint quotes (searchable) |
| `P1_not_useful_notes.md` | Optional longer notes for borderline exclusions |
| `P1_synthesis.md` | Written only after ≥2 completed rounds; patterns + limits + open questions |
| PDF/HTML store | e.g. `p1_history/refs/` (mirrors Isolation practice layout) |

IDs: `P1-001`, `P1-002`, … assigned at first screen, never reused.

---

## 5. Multi-round research design

The search is **iterative by design**. Each round has a fixed aim, a pre-registered query list, a stop for that round, and a double-check. Later rounds are not “fixing” earlier rounds to force a story; they are **expanding coverage** and **stress-testing** emerging patterns.

### Round 0 — Scaffold (no deep claims)

**Aim:** Freeze protocol version, create empty CSVs/logs, define inclusion rules.  
**Outputs:** This file v0.1; empty `P1_search_log.md`, `P1_screened.csv`, `P1_useful.csv`.  
**Check:** Independent read of protocol for ambiguous inclusion language; revise to v0.2 if needed **before** Round 1.

---

### Round 1 — Seed from known anchors (transparent, high bias risk → treat as seeds only)

**Aim:** Collect **starting citations**, not conclusions.

**Sources of seeds (all logged as `source_of_lead=seed_*`):**
- Enders / Weller / Robbins polio tissue-culture papers and methods notes (as **items in the record**, not timeline rulers)  
- Early continuous-line / plaque / media classics that Isolation literature already cites (Eagle, Dulbecco, etc.) **only when virus culture is involved**  
- Bibliographies of modern historical reviews of “virus isolation” / “cell culture diagnosis”  
- Institutional manuals already in this repo (`wrk/isolation_protocols/`) **only to mark window-end candidates**, not as pre-institutional evolution  

**Actions:**
1. List seeds with year and why seeded.  
2. Obtain full text where possible.  
3. Screen and extract if useful.  
4. Harvest **backward citations** (references those papers cite for methods/medium).  
5. Harvest **forward citations** only within the time window (or forward to first institutional codifications for end-marker only).

**Bias note:** Round 1 over-weights famous names. Round 2+ must deliberately leave that neighborhood.

**Round 1 complete when:** All seeds screened; one-hop citation neighborhood logged; search log updated.

---

### Round 2 — Systematic database queries (pre-registered)

**Aim:** Broaden beyond celebrity seeds.

#### 2.1 Databases / libraries (query each; log platform + date + query string + approx hit count)

| Resource | Role |
|----------|------|
| **PubMed / MEDLINE** | Primary biomedical indexing |
| **PMC** (full text) | Full-text strings: maintenance medium, serum percent, cytopathogenic |
| **Google Scholar** | Books, older scans, citation chasing (higher noise; stricter screen) |
| **Web of Science / Scopus** (if available) | Citation networks, older journal coverage |
| **Internet Archive / HathiTrust / Google Books** | Pre-1960 manuals, monographs, society proceedings |
| **WHO IRIS / national lab archives** | Early lab manuals, polio/enterovirus guidance |
| **ASM / journal backfiles** (J Bacteriol, J Exp Med, Proc Soc Exp Biol Med, etc.) | Primary methods era |
| **Library catalogs** | Printed Cumitech / diagnostic manuals for **end-window** dating |

If a resource is unavailable, log **attempted / blocked** — unavailability is part of thoroughness documentation.

#### 2.2 Pre-registered query families (adapt syntax per database; do not drop families without logging)

Run in **both** title/abstract and, where available, full text. Combine with date filters matching the window; re-run without date filter only to catch mis-dated records, then exclude out-of-window.

**Family A — virus + culture system**
- virus isolation tissue culture  
- virus isolation cell culture  
- cytopathogenic OR cytopathic virus culture  
- viral degeneration tissue culture  
- “tissue culture” poliomyelitis / influenza / herpes / adenovirus (representative agents, not only one virus)

**Family B — medium language**
- “maintenance medium” virus  
- “maintenance medium” serum  
- “growth medium” “maintenance medium” virus  
- serum free virus isolation (historical + mid-century)  
- “percent serum” OR “% serum” OR “2% serum” OR “10% serum” virus culture  
- “fetal calf” OR “calf serum” OR “horse serum” OR “human serum” virus isolation  
- ultrafiltrate tissue culture virus  
- embryo extract virus culture  

**Family C — process language**
- inoculat* serum medium virus culture  
- “after adsorption” medium serum  
- “reduced serum” virus  
- “low serum” virus culture  

**Family D — counterexample hunters (mandatory)**
- virus isolation “10% serum” OR “20% serum” infection  
- virus culture “same medium” serum inoculat*  
- “high serum” virus isolation cell  
- deliberately seek papers that **do not** reduce enrichment at infection  

**Family E — institutional end markers**
- viral culture approved guideline  
- Cumitech virus  
- “maintenance medium” diagnostic virology manual  
- CLSI OR NCCLS viral culture (for dating codification only)

#### 2.3 Screening workflow (every hit list)

1. **Title/abstract screen** → include / exclude / unclear.  
2. **Full text** for include + unclear.  
3. Append row to `P1_screened.csv`.  
4. If useful → extract to `P1_useful.csv` + quotes.  
5. Cap per query if hits > N (e.g. 100): sort by relevance/date; screen top N and log that a cap was applied; later round may raise cap.

**Round 2 complete when:** All query families run on at least PubMed + one full-text source + one book/manual source; screened table has every decided hit; counterexample family D has been run.

---

### Round 3 — Citation snowball (structured)

**Aim:** Find what databases miss (vocabulary drift, unindexed methods).

1. From each **useful** source, list references that look methods-related.  
2. Screen those references (new IDs).  
3. For each useful source, sample forward citations **within window** (or to end-markers).  
4. Stop snowball at **depth 2** unless a new cluster of useful methods papers appears (then log depth-3 exception).

**Round 3 complete when:** Depth-2 complete for all Round 1–2 useful items; new useful items either extracted or queued for Round 4.

---

### Round 4 — Adversarial / gap-fill round

**Aim:** Attack whatever pattern is emerging.

| If emerging pattern is… | Adversarial tasks |
|-------------------------|-------------------|
| “Everyone reduced serum early” | Actively collect high-serum-throughout infection methods; different viruses/cell systems |
| “No one discussed serum” | Target full-text “% serum” in methods sections of known Isolation classics |
| “Only after year Y” | Search restricted to earlier decades with broader vocabulary (ultrafiltrate, plasma clot, etc.) |
| “Only polio/enterovirus” | Force sample of myxo, herpes, pox, plant viruses in culture if in window |
| “Only English” | If feasible, sample major non-English journals/manuals (log language limits) |

Also:
- Re-run Family D with new synonyms found in useful papers.  
- Expert secondary sources: does any historian already claim an origin for maintenance medium? Extract claim + their citations; verify primary.

**Round 4 complete when:** Adversarial tasks logged; at least one documented attempt to falsify each major emerging descriptive pattern.

---

### Round 5+ — Saturation and replication

**Aim:** Demonstrate diminishing returns and repeatability.

**Saturation signals (need more than one):**
- New queries only recover already-screened items  
- Snowball yields no new useful methods descriptions  
- Counterexample search stabilizes (same small set of high-serum-throughout papers)  
- Two independent passes (Section 8) agree on pattern summary

**Replication pass (mandatory before synthesis freeze):**
- Second person or fresh agent session receives **only** this protocol + empty templates (not the synthesis conclusions).  
- Re-runs a **subset** of Round 2 queries (pre-specified sample).  
- Compares: overlap of useful IDs, disagreements on useful Y/N, extraction field mismatches.  
- Log agreement rates in `P1_search_log.md`.

**Optional Round 6:** Targeted archives (university special collections, national library scans) if Round 5 shows manuals are the gap.

---

## 6. Extraction schema (useful sources)

One row per useful source in `P1_useful.csv`. Unknown = `unknown` / empty with `notes`, never guessed.

| Field | Description |
|-------|-------------|
| `id` | P1-### |
| `year` | Publication year |
| `authors` | Short |
| `title` | Full |
| `citation` | Journal/book, volume, pages, DOI/URL if any |
| `document_type` | primary_methods / review / manual / monograph / other |
| `virus_or_agent` | As stated |
| `culture_system` | explant / primary / continuous line / mixed / unclear |
| `cell_or_tissue` | Free text |
| `enrichment_propagation` | Serum type + amount or other enrichment for growth |
| `enrichment_infection_or_observation` | Same for infection / maintenance / long observation |
| `enrichment_change` | yes / no / unclear — was a change described? |
| `change_timing` | e.g. at inoculation, at confluence, after adsorption |
| `rationale_quoted` | Verbatim reason if any, else `none_stated` |
| `endpoint` | CPE / degeneration / titer / antigen / other |
| `comparison_of_media` | yes / no — did they compare enrichment levels? |
| `uninoculated_under_same_medium` | yes / no / unclear |
| `quotes_medium` | Key verbatim passages |
| `quotes_endpoint` | Key verbatim passages |
| `window_status` | in_window / end_marker / out_of_window_excluded |
| `extractor` | Who filled the row |
| `extract_date` | ISO date |
| `confidence` | high / medium / low (OCR, translation, incomplete PDF) |
| `notes` | Free text |

**Borderline useful:** Extract if any medium+virus culture link exists; set `confidence=low` and explain.

---

## 7. Screening codes (`P1_screened.csv`)

| Field | Values |
|-------|--------|
| `id` | P1-### |
| `year` | |
| `short_cite` | |
| `lead_source` | seed / pubmed_q# / scholar_q# / snowball_from_P1-### / manual / other |
| `useful` | **Y** / **N** / **B** (borderline) |
| `reason` | One line (required for N and B) |
| `fulltext` | Y / N / paywall / not_found |
| `round` | 0,1,2,… |
| `notes` | |

**Example not-useful reasons (use consistently):**  
`no_culture` · `no_medium_info` · `out_of_window` · `not_virus` · `secondary_no_primary_methods` · `duplicate` · `unobtainable_fulltext` · `language_not_processed`

**Unobtainable fulltext:** Keep as screened N or B with `fulltext=not_found`; do not silently drop. Later rounds may recover.

---

## 8. Double-check and quality control

### 8.1 Within-round QC

| Check | Procedure |
|-------|-----------|
| Extraction accuracy | Second reader verifies quotes against PDF for every **Y** row (or ≥20% random sample + all low-confidence) |
| Useful Y/N | Second reader re-screens a random 20% of N and all B |
| Query fidelity | Search log must show exact query strings; re-run one query per family to confirm hit stability |
| ID integrity | No duplicate primary citations under two IDs; merge with note if found |

### 8.2 Cross-round QC

- After Round 2 and after Round 4: reconcile `P1_useful.csv` with quotes file.  
- Any change to a previously frozen row requires `amendment_note` + date (no silent edits).

### 8.3 Adversarial QC (pattern-level)

Before writing `P1_synthesis.md`:

1. List 3 descriptive claims you are tempted to make.  
2. For each, point to **supporting** row IDs and **contradicting or limiting** row IDs.  
3. If a claim has no contradicting search attempt in the log, run that search (mini-round) first.

### 8.4 Optional external check

- Hand protocol + 5 PDFs to a second agent/session with **blank** extraction sheet; compare field agreement (Cohen-style or simple % match on enrichment_change, rationale_quoted presence, endpoint).

---

## 9. Stop rules and “we did our best” criteria

Declare P1 search **provisionally complete** only when **all** hold:

1. Rounds **0–4** finished and logged.  
2. Round **5 replication subset** finished and agreement logged.  
3. Counterexample Family D run at least twice (Round 2 and Round 4).  
4. Institutional **end markers** identified and dated with citations.  
5. Diminishing returns: last snowball/query batch added **zero** new useful in-window methods papers **or** only duplicates.  
6. Screened table contains **not-useful** entries in substantial number (proves breadth, not cherry-picking).  
7. Synthesis lists **limits** (language, paywall, lost manuals, vocabulary) as prominently as patterns.

**Incomplete but publishable honesty:** If paywalls or language block a known cluster, state that explicitly; do not pretend saturation in that cluster.

---

## 10. How the process is repeated to find more references

After provisional completion, further rounds are **optional reopenings** with a written trigger:

| Trigger | Action |
|---------|--------|
| New database access | Re-run Family A–D on new platform; log as Round 6+ |
| Peer reviewer cites a missing classic | Screen as new seed; snowball depth 1–2 |
| New digitization of a manual | Screen as end-marker or in-window methods |
| Vocabulary discovered late (e.g. period synonym) | New query family; do not retrofit old rounds without re-screen |
| Disagreement between extractors | Freeze contested rows; third pass |

Each reopening appends to `P1_search_log.md` and never deletes prior screened N rows (audit trail).

---

## 11. From data to prose (only after extraction freezes)

`P1_synthesis.md` structure (suggested):

1. **Methods of the historical search** (rounds, databases, counts screened / useful).  
2. **Descriptive patterns** (with ID citations only).  
3. **Counterexamples and heterogeneity**.  
4. **Institutional end markers** (when prescription appears).  
5. **What remains unknown**.  
6. **Optional light discussion:** ways these patterns may be consistent, inconsistent, or inconclusive relative to the lock-in interest in Section 1 — without rewriting the extraction.

Main paper text should cite synthesis + key primary IDs, not re-run ad hoc Scholar searches in the Discussion draft.

---

## 12. Resource query checklist (copy into each round of `P1_search_log.md`)

```text
Round #:
Date:
Operator:

[ ] Query list frozen before execution (paste list)
[ ] PubMed
[ ] PMC full text
[ ] Google Scholar
[ ] WoS/Scopus (or logged unavailable)
[ ] Books/Archive/Hathi (or logged unavailable)
[ ] WHO/national manuals (end markers)
[ ] Family D counterexamples run
[ ] Hit lists saved or counts logged
[ ] All decisions → P1_screened.csv
[ ] All Y → P1_useful.csv + quotes
[ ] Second-reader sample QC
[ ] Round complete criteria met (see Section 5)
```

---

## 13. Roles and tools (practical)

| Role | Responsibility |
|------|----------------|
| **Planner** | Freezes round query list; enforces stop rules |
| **Searcher** | Runs queries; fills screened CSV |
| **Extractor** | Full-text quotes + useful CSV |
| **Checker** | Re-screens sample; verifies quotes |
| **Synthesizer** | Writes P1_synthesis only after freeze (can be same person on a later day, not same sitting as extraction) |

Grok/agent sessions: use **separate sessions** for (a) search listing, (b) extraction, (c) adversarial counterexample hunt, (d) synthesis — to reduce same-context confirmation drift. Hand each session this protocol and the relevant CSV only.

---

## 14. Relationship to the rest of the paper

| Workstream | Depends on P1? |
|------------|----------------|
| CRO / FBS control experiment | No |
| Institutional protocol tables (current) | No (but supplies end-marker candidates) |
| Isolation-ref control tiers (A–D) | No |
| EV / particle layer | No |
| Discussion: historical lock-in interest | **Yes — uses P1 synthesis** |

P1 can be incomplete without blocking the empirical Isolation/CPE core. It should not delay those results.

---

## 15. Immediate next steps (when you say go)

1. Create empty `P1_search_log.md`, `P1_screened.csv`, `P1_useful.csv` headers.  
2. Create `p1_history/refs/` for PDFs.  
3. Round 0 protocol freeze (edit this file if you want stricter language limits, hit caps, or mandatory non-English).  
4. Round 1 seed list from papers already known + repo manuals as end-marker candidates only.  
5. Do not write historical conclusions in `DRAFT.md` until Round 2+ extraction exists.

---

## 16. Revision log

| Version | Date | Change |
|---------|------|--------|
| v0.1 | 2026-07-20 | Initial protocol: prediction-as-interest, window, multi-round design, bias rules, schemas, QC, stop rules |

---

*End of P1 research protocol. Iterate before Round 1 execution.*
