# P1 synthesis (provisional)

**Date:** 2026-07-22 (Round 10 refresh)  
**Protocol:** `P1_research.md` v0.1  
**Artifacts:** `P1_search_log.md`, `P1_screened.csv` (~57 rows), `P1_useful.csv` (28 unique extracts), `P1_quotes.md`  
**Status:** Provisional through **Round 10** (Priority-A PDFs: Weller 1948, Youngner 1954, Scherer HeLa 1953, Baron 1958). **Not** bibliographic saturation. See **§7** for medium-vs-inoculation narrative.

### Round 6 update (user PDFs in `p1_history/refs/`)

Full-text re-extracts raised confidence for **P1-001, P1-002, P1-005, P1-015, P1-017**. New user IDs:

| ID | Paper | P1 relevance |
|----|--------|----------------|
| **P1-200** | Smith SE 1961 *A Maintenance Medium for Tissue Culture Virus Studies* | Explicit definition of **maintenance medium** as virus-study medium; **serum-free** liver-digest ultrafiltrate in Earle BSS; cells **grown** on lactalbumin + serum |
| **P1-201** | Hsiung GD 1961 primary cell cultures review | **2% horse serum** can **inhibit** polio plaques; protein-free overlays discussed — supports “serum can interfere” lineage |

**P1-017 confirmed counterexample:** growth **20%** sheep serum → maintenance **10%** sheep serum (still high; not modern 2%).

### Round 7 update (more user PDFs + re-search)

| User file | Canonical | Finding |
|-----------|-----------|---------|
| **P1-04** | **P1-004** Melnick & Riordan 1952 | **Protein-free** lactalbumin medium; Hanks–Simms + Simms ultrafiltrate + lactalbumin; serum/embryo extract **replaced**; CPE still used; uninoculated controls imaged |
| **P1-203** | **P1-018** Boyle 1964 RVF | Growth **199 + 10% calf serum** → **serum-free maintenance** for titration; **CPE appears when serum is omitted**; with serum, RVF can grow **without** obvious CPE; plaques still need serum in overlay |
| **P1-204** | **P1-035** Rosenbaum ~1963 | Growth **MEM + 10% FCS**; MACRO maintenance **MEM + 5% horse serum**; microtitration keeps growth medium |
| **P1-036** PDF | notice only | AJPH book notice of Lennette/Schmidt 4th ed — **not** full methods chapter |
| **P1-020** | Hematian 2016 | Re-confirmed **no** serum recipe |

**Strongest new interpretive point (Boyle):** medium enrichment can **toggle whether CPE is the readable endpoint** for the same virus — not only “help cells live longer.” That is directly relevant to non-specificity / confounded endpoints under Isolation conditions.

**Re-search leads still needing PDFs:** Li & Schaeffer 1953 (*Science*) **P1-042**; Melnick–Opton assay methods with **2% calf serum** snippet **P1-043**.

### Round 8 — Full Schmidt Chapter 3 (P1-008) — major end-marker locked

User supplied **entire** Ch. 3 (*Tissue Culture Technics for Diagnostic Virology*, 4th ed. 1969, book pp. ~79–178) as screenshots. Readable.

**Institutional dual-medium pattern is explicit and quantitative by 1969:**

| Role | Typical serum (Schmidt recipes) |
|------|----------------------------------|
| Growth | **10–20%** FBS (or 5% bovine for monkey kidney; 10% human serum for some continuous lines) |
| Maintenance / viral propagation | **Serum-free preferred**, else **~2% FBS** (or **5%** for some continuous-line maintenance mixes); L-15 + **2% FBS** for some respiratory viruses |
| Transition | Remove growth medium **before virus**; wash BSS if growth serum may contain inhibitors |

Also: CPE as main Isolation readout; **uninoculated control tubes** for spontaneous/nonspecific degeneration; toxic clinical inocula can cause non-viral degeneration.

This is the cleanest pre-CLSI **diagnostic** codification of the growth/maintenance split we have found. Combined with Melnick protein-free work and Boyle’s serum-dependent CPE, P1 historical layer is now strong enough for paper use with remaining gaps noted as optional.

### Round 9–10 update — dual-medium primaries + Priority A PDFs

| ID | Paper | Finding for medium / inoculation |
|----|--------|----------------------------------|
| **P1-206** | Melnick 1953 dry-tube | Growth **10%** bovine + 199 → wash inhibitors → **serum-free** maintenance |
| **P1-042** | Li & Schaeffer 1953 | Horse serum **inhibitory**; Medium E hydrolysate path |
| **P1-043** | Melnick & Opton 1956 | Nutrient medium + **2.0% calf serum** |
| **P1-006** | Melnick 1955 | Lactalbumin + **2% calf**; fluid replaced after inoculum |
| **P1-051** | Weller & Enders 1948 | **HS** ultrafiltrate single fluid; pre-polio |
| **P1-046** | Youngner 1954 | Medium D **2% horse serum** growth; **serum-free 199** for virus assay |
| **P1-047** | Scherer et al. 1953 HeLa | Growth **~50% human serum**; double **MS-100** wash dilutes antibodies **1:400–800** before virus |
| **P1-048** | Baron & Low 1958 | Named maintenance medium; **4–100×** polio inhibition by calf-serum maintenance vs serum-free |
| **P1-013** | Leland 2007 | Secondary formats review; **no** dual-medium % recipes |

**Interpretive gain (Round 10):** The dual-medium / low-or-no-serum-at-infection pattern is **operational by ~1953–54** in multiple labs, **rationalized** by serum as antibody/inhibitor (Baron, Li, Melnick wash, HeLa MS-100), and **codified** by Schmidt 1969 with **~2% FBS** recipes. Full narrative: **§7**.

---

## 1. What was asked

How serum / nutrient enrichment was used in virus tissue and cell culture from ~1900 until institutional protocols prescribed a dual growth/maintenance (often low-serum) recipe — without requiring a preferred evolutionary story.

---

## 2. Search effort (counts)

| Item | n (approx., Round 10) |
|------|---|
| Screened IDs | ~57 |
| Useful (Y) unique extracts | ~28 |
| Explicit dual-medium primaries | P1-046, P1-047, P1-048, P1-206, P1-004, P1-018, P1-008, … |
| Explicit counterexample useful rows | ≥2 (P1-017 high-serum maintenance; P1-018 serum-free infection medium / CPE toggle) |
| End-marker institutional sources | CLSI M41, ATCC guide, ASM CPE protocol, UK SMI V_39, Lennette/Schmidt diagnostic manuals |

Databases/tools used: web search (PubMed-like indexes via Scholar/web), PMC snippets, ATCC web guide, Nobel PDF full text, project in-repo protocols, WHO IRIS / DTIC snippets.

**Limits (honest):** Many 1950s primary PDFs remain paywalled or incomplete OCR; several useful rows are medium-confidence. Non-English literature not systematically processed. Cumitech / full Lennette-Schmidt chapter text not fully extracted.

---

## 3. Descriptive patterns (with IDs)

### Pattern A — Early operable virus culture used **non-whole-serum / reduced-protein** fluids and long observation

- **P1-001/P1-003:** BSS + **ox serum ultrafiltrate**; frequent medium replenishment; multi-week viability; CPE and pH endpoints.  
- Not yet the modern “10% FBS → 2% FBS” label, but **enrichment is already constrained** relative to rich whole-serum growth systems.

### Pattern B — Mid-century methods actively **strip or simplify protein/serum** for polio TC

- **P1-004:** Melnick & Riordan **protein-free** nutrient media replacing serum–embryo-extract proteins (lactalbumin hydrolysate path).  
- Shows published **optimization of medium composition** for virus culture success, not only silent tradition.

### Pattern C — Dual **growth vs maintenance** language is present by the diagnostic era and later textbooks state it as settled

- **P1-035 (1963):** tube cultures “changed to maintenance.”  
- **P1-015:** after ~3 days → maintenance with **1% serum or serum-free**.  
- **P1-009 (Fenner textbook):** FCS **5–10%** for growth; after monolayer + inoculation → maintenance with **little or no serum**.  
- **P1-010/011/012/016:** modern institutional codification **10% → ~2%** (or 1–3%), with **heterogeneous rationales** (overgrowth, inhibitors, attachment, or none).

### Pattern D — **Heterogeneous practice** in-window (counterexamples)

- **P1-017 (1961):** “maintenance medium” still **10% sheep serum** (vaccinia / sheep kidney).  
- **P1-018 (1964):** **serum-free** maintenance for RVF inoculation.  
- Together: “maintenance” does **not** always mean modern 2% FBS; the word is older and broader.

### Pattern E — We did **not** find a single continuous, famous experimental series that *only* titrates serum % on matched uninoculated monolayers to invent Isolation CPE specificity

- No screened source in this pass is a clean “serum-as-sole-IV on uninfected cells” foundation for the Isolation recipe.  
- Absence is **informative for methods genealogy**, not proof of absence of all lab notebooks.

### Pattern F — Institutional **end markers** (window upper bound)

By the time of widely used diagnostic manuals and later CLSI/ATCC/ASM-type documents, the dual-medium / low-serum maintenance pattern is **prescribed**, not argued as a new discovery:

| Marker | Role |
|--------|------|
| Lennette & Schmidt diagnostic procedures (1960s–69 chapter lineage) | Diagnostic TC technics codification |
| CLSI M41-A (2006) | Explicit 10% vs 1–3% + CPE |
| ATCC Virology Guide | Lower viral serum; NOTE 5 → 2% attachment |
| ASM CPE protocol | Maintenance 2% serum + uninoculated well |
| UK SMI V_39 | Growth 10% / maintenance 2% tables |

For the paper: **evolution search ends at first clear prescription wave**; later sources mainly **transmit**.

---

## 4. Consistency with the P1 “interest” (light interpretation)

| Interest element | Provisional fit |
|------------------|-----------------|
| Reduced enrichment at infection appears before today’s brand-name 2% FBS | **Supported** (ultrafiltrate, protein-free media, maintenance little/no serum language) |
| A neat published high→low FBS titration inventing the recipe | **Not found** in this pass |
| Practice becomes **institutional prescription** | **Supported** (end markers) |
| Single evidence-based rationale across history | **Not supported** (attachment vs overgrowth vs inhibitors vs none; high-serum “maintenance” still appears) |
| Empirical lock-in selected on culture endpoints | **Plausible / consistent** with early CPE operability + medium simplification, but **not proven** as a documented selection experiment |

**Bottom line for the paper:**  
The published record is **compatible with early embedding of reduced/simpler enrichment for long culture observation**, later **codified** as growth vs maintenance (often ~2% serum), with **heterogeneous practice and rationales**. It does **not** supply a clean, deconfounded experimental origin story for low-FBS CPE Isolation. That is a legitimate historical finding, not a failed search.

---

## 5. What remains open (next rounds if reopened)

1. ~~Full Schmidt 1969 chapter~~ — done (**P1-008**). ~~Youngner / Baron / Weller 1948 / HeLa~~ — done Round 10.  
2. Still missing Priority A: **P1-045 / 045b** *J Immunol* 1952 Weller/Robbins methods series (I/II).  
3. Optional: Melnick chapter *Diagnostic Procedures* 2nd ed (**P1-044**); Cumitech / edition-specific ASM manuals.  
4. Non-English (French/German/Japanese diagnostic manuals).  
5. Pre-1940 vaccinia/yellow fever TC medium recipes (borderline).  
6. Independent replication pass on Family B/D queries.

---

## 6. Relationship to main empirical paper

P1 is **contextual**. It does not replace:

- CRO serum-only control  
- Isolation corpus FBS reduction prevalence  
- Control-tier A–D results  
- EV particle-layer synthesis  

Use this synthesis in Discussion as: *historical embedding and institutionalization of medium practice*, with limits stated. Prefer **§7** for the dual-medium / inoculation-step timeline.

---

## 7. Medium history vs inoculation-step history (integrated narrative)

**Question for paper Discussion:** What does the published record say about **when and why** culture fluid changed between **growing cells** and **observing virus effects after inoculation**?

This is not the same question as “did FBS % decline continuously from 1900.” It is about the **operational split**: enrichment for **monolayer production** vs enrichment (or lack of it) for the **Isolation/CPE observation step**.

### Stage 1 — Constrained single fluid (~1948–1950): no formal inoculation switch

| Source | Fluid | At inoculation |
|--------|--------|----------------|
| **P1-051** Weller & Enders 1948 | Hanks BSS + **ox serum ultrafiltrate** (“HS”) | Same HS; fluid **replaced**, not switched to low-serum |
| **P1-001** Enders et al. 1949 | BSS 3 + ox ultrafiltrate 1 | Same system; serial subculture |
| **P1-002** Robbins et al. 1950 | Hanks–Simms ± beef embryo extract; plasma clots | Medium **replenished**; CPE endpoint emerges |

**Reading:** Early operable virus TC already used **non-whole-serum** or reduced-protein fluids. Enrichment is **constrained**, but authors do **not** yet describe a **growth medium → maintenance medium** percent drop as a named inoculation step.

### Stage 2 — Medium simplification for outgrowth and virus (~1952–1953)

| Source | What changes |
|--------|----------------|
| **P1-004** Melnick & Riordan 1952 | Serum/embryo extract **replaced** by **lactalbumin hydrolysate**; lower protein after virus |
| **P1-042** Li & Schaeffer 1953 | **Horse serum frequently inhibitory**; Medium E hydrolysate path |
| **P1-034** Morgan et al. 1950 | Medium **199** as synthetic base (later used **with** serum for growth) |

**Reading:** Published **optimization** of medium composition for polio TC success and readability (less nonspecific degeneration). Still not fully the modern “10% FBS growth / 2% maintenance” label.

### Stage 3 — Explicit dual media at the inoculation / assay step (~1953–1956)

Three independent operational patterns appear almost simultaneously:

| Pattern | Source | Growth / prep | After inoculum / for assay |
|---------|--------|---------------|----------------------------|
| **A. Serum outgrowth → serum-free maintenance + wash** | **P1-206** Melnick 1953 | **10%** bovine serum + 199 | Wash Earle to remove **inhibitors** in bovine serum; maintenance **serum-free** 199 + Earle |
| **B. Low horse serum outgrowth → serum-free assay fluid** | **P1-046** Youngner 1954 | Medium D: 199 + **2% horse serum** | Virus/Ab titration: **serum-free** 199 + bicarbonate only |
| **C. High human serum continuous line → synthetic MS after antibody dilution** | **P1-047** Scherer et al. 1953 | **~50%** human serum/ascites + EE | Double replace **MS-100**; residual serum diluted **1:400–800** because growth fluid **assumed to contain polio antibodies** |

Supporting mid-decade practice:

| Source | Detail |
|--------|--------|
| **P1-005** Dulbecco 1954 | Rich horse serum + embryo extract for monolayers; plaque overlay **without** listed horse serum |
| **P1-006** Melnick 1955 | Lactalbumin + **2% calf serum** outgrowth; fluid **replaced after inoculum** |
| **P1-043** Melnick & Opton 1956 | Nutrient medium = lactalbumin base + **2.0% calf serum** for assay panels |

**Reading:** By the mid-1950s the **inoculation step** is already the moment when authors **remove** growth-associated serum (or switch off horse-serum Medium D) for virus readout. Motives stated in-period: **inhibitors**, **antibodies**, assay clarity—not a single published “serum % as sole IV on uninfected cells” experiment.

### Stage 4 — “Maintenance medium” named and serum inhibition quantified (~1958–1964)

| Source | Contribution |
|--------|----------------|
| **P1-048** Baron & Low 1958 | Explicit **maintenance medium** problem; sera contain **inhibitors**; skim milk replaces serum protein; **4–100-fold** polio inhibition by calf-serum maintenance vs serum-free on MK; proposes isolation of agents **missed** under serum maintenance |
| **P1-200** Smith 1961 | Defines maintenance medium for **virus studies**; **serum-free** liver-digest ultrafiltrate; cells **grown** on lactalbumin + serum |
| **P1-201** Hsiung 1961 | **2% horse serum** can **inhibit 90%** of polio plaques in overlay |
| **P1-018** Boyle 1964 | Growth 199 + **10% calf**; infection in **serum-free** maintenance; **CPE appears when serum is omitted** (RVF can multiply **without** clear CPE **with** serum) |

**Reading:** “Maintenance” is now a **named medium class** for virus observation. Serum is treated as something that can **block sensitivity**, **block plaques**, or even **toggle CPE visibility** (Boyle). Heterogeneous substitutes (skim milk, liver digest, pure synthetic, low % serum) compete; the **shared structure** is: grow cells rich → observe virus leaner.

### Stage 5 — Heterogeneous still in-window (counterexamples)

| Source | Counter-pattern |
|--------|-----------------|
| **P1-017** 1961 vaccinia / sheep kidney | “Maintenance” still **10% sheep serum** (growth was 20%) |
| **P1-035** Rosenbaum ~1963 | MACRO maintenance **5% horse serum**; microtitration keeps **growth** medium |
| **P1-047** note | **10% chicken serum + MS** better morphology than MS-100 alone; titers identical |

**Reading:** Dual media is **not** universally “→2% FBS.” The word maintenance is older and broader. Modern institutional 2% is a **later attractor**, not the only 1950s–60s solution.

### Stage 6 — Diagnostic codification (~1969 → manuals → CLSI)

| Source | Prescription |
|--------|--------------|
| **P1-008** Schmidt 1969 ch.3 | Growth vs maintenance **defined**; remove growth medium **prior to virus**; wash if inhibitors; recipes often **~2% FBS** maintenance (sometimes serum-free; continuous lines sometimes 5%) |
| **P1-015** Moffat ~1969 | Growth 10% calf → after ~3 days maintenance **1% or serum-free** |
| **P1-009–012, 016** Fenner / CLSI / ATCC / ASM / UK SMI | Transmit **10% → ~2%** (or 1–3%); rationales **heterogeneous** (overgrowth, inhibitors, attachment, or none) |

**P1-013** (Leland 2007) reviews Isolation **formats** after lock-in; does not re-derive medium %.

### What changed at the inoculation step? (one-line genealogy)

1. **Early:** one constrained fluid (ultrafiltrate / hydrolysate path) through culture life.  
2. **~1953–54:** **operational split** at assay/infection — strip or drop serum (Melnick wash; Youngner serum-free 199; HeLa MS-100 after antibody dilution).  
3. **~1958–64:** **named** maintenance media + **quantified** serum inhibition / CPE toggles.  
4. **~1969+:** diagnostic manuals **fix** dual media and **~2% FBS** as default Isolation practice.  
5. **Modern institutional:** same structure with FBS branding and mixed rationales; no found foundational “serum-only IV on uninfected monolayers” paper inventing CPE specificity.

### Paper-facing claim (conservative)

The published mid-century record supports:

- A **structural** growth/prep vs post-inoculation medium difference emerging **before** institutional 2% FBS language.  
- Stated motives that treat serum as **inhibitor / antibody / sensitivity problem** for virus observation.  
- **Not** a single clean experimental origin story that deconfounds serum reduction from inoculum for CPE as a virus-specific detector.

That is enough for Discussion **context**; it does not replace R1/R2/CRO empirical results.

---

---

## 8. Close for paper (2026-07-22)

Research archive above remains provisional in the sense of **not bibliographic saturation**.  
**Paper-facing P1 is closed:** see **`P1_for_paper.md`** (narrative + minimal bibliography + reopen criteria).  
Further PDFs only if they meet reopen criteria in that file.

---

*Provisional synthesis end (Round 10); paper close in P1_for_paper.md.*
