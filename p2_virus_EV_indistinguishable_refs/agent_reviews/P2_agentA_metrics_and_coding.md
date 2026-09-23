# Agent A review — metrics and coding

**Role:** Independent verification (P2 EV vs virion indistinguishability)  
**Date:** 2026-07-22  
**Stance:** Process accuracy over thesis support. Full-text local PDFs for seed IDs; PubMed abstracts for abstract-only IDs. No CSV edits performed.

**Sampled IDs:** P2-001, P2-002, P2-003, P2-004, P2-006, P2-007 (full PDF); P2-010, P2-016, P2-018 (abstract / quote archive). P2-005 full PDF spot-checked for M-EM / partial coding.

---

## Sample re-screen table

Legend for agreement: **A** = agree with provisional coding; **D** = disagree (recommend change); **P** = partial agree (nuance / under- or over-code).

| ID | Source | useful Y | metrics_coded | states_incomplete_physical_separation | supports_dilemma | confidence | Agent notes |
|----|--------|----------|---------------|----------------------------------------|------------------|------------|--------------|
| **P2-001** | Nolte-’t Hoen et al. 2016 PNAS (full PDF) | **A** | **A** (minor gap) | **A** `yes` | **A** `Y` | **A** `high` | Section “Mission (Almost) Impossible” is explicit: almost impossible to distinguish/separate EVs from (noninfectious) viruses; size 50–100 nm vs ~100 nm; density EV 1.13–1.18 vs retrovirus 1.16–1.18; “border between them seems not to exist”; density gradients “not always reliable”; historical UC co-pelleting of ~100 nm membrane particles. Metrics M-SIZE; M-DENS; M-CONT; M-RNA; M-MARK; M-UC all supported. Optional add **M-EM** (historical EM co-pellet language) — currently *not* coded, yet synthesis §2 cites P2-001 under M-EM (**synthesis/CSV mismatch**). |
| **P2-002** | McNamara & Dittmer 2020 (full PDF) | **A** | **A** | **A** `yes` | **A** `Y` | **A** `high` | Strong methods survey. Overlapping densities; “even carefully prepared … gradients cannot be used to conclusively separate”; co-contamination expected for lower-density families (e.g. flaviviruses); UC not ideally suited for EV–virus separation from infected cultures; PEG concentrates rather than separates; TFF/affinity/nano-flow discussed. Codes match. `claims_successful_separation=partial` appropriate (affinity, nano-flow as emerging). |
| **P2-003** | Zhou, McNamara & Dittmer 2020 (full PDF) | **A** | **A** (minor undercode) | **A** `yes` | **A** `Y` | **A** `high` | Core hinge paper for M-RNA: densities/buoyancies “so closely overlap … density gradients is impractical”; PEG “cannot separate viruses from EV”; SEC/IEC “virus-EV cross-contamination is difficult to avoid”; affinity can enrich marker+ EV. Could add **M-TFF** (filtration/TFF discussed) — optional. |
| **P2-004** | Raab-Traub & Dittmer 2017 (full PDF) | **A** | **A** | **A** `yes` | **A** `Y` | **A** `high` | Box 1 table: differential UC, ExoQuick, PEG, SEC, density flotation → virion co-purification **Yes**; CD63/composite magnetic beads → **No**. Biophysical similarity language verified. M-EM justified only weakly (purity assessment by EM mentioned; not a morphology-non-discriminating primary). `counterexample_value=partial` correct. |
| **P2-006** | Giannessi et al. 2020 (full PDF) | **A** | **P** undercoded | **A** `yes` | **A** `Y` | **A** `high` | Non-UNC authors — good diversification. Explicit separation failure language on p.3–4: “almost impossible mission to separate EVs and viruses by … differential ultracentrifugation”; “a reliable method that can actually guarantee a complete separation does not exist.” Current metrics `M-SIZE;M-LIPID;M-CONT;M-PROT` miss **M-UC** (and arguably **M-DENS** / marker discrimination language). Amend metrics upward. |
| **P2-007** | Moulin et al. 2023 (full PDF) | **P** soft Y | **P** | **A** `partial` | **D** → prefer `mixed` | **D** → `medium` | Biogenesis/hijacking/therapy review; “intertwined entities” and shared ESCRT/egress machinery are clear (**M-CONT; M-PROT** OK). **Little primary purification/separation methods content** relative to P2-001–004. **M-HIST** is weak (“past five years” of engineering/virotherapy, not historical co-contamination). Supports *ongoing biological intertwining*, not strong multi-metric physical-separation failure. Keep as Y for inclusion (scope: shared biogenesis used to argue relatedness), but do **not** treat as methods evidence equal to P2-001–003. Confidence high is inflated. |
| **P2-010** | Bess et al. 1997 (abstract) | **A** | **A** (pending fulltext) | **A** `yes` | **A** `Y` | **D** → `medium` until PDF | PubMed abstract (PMID 9126269) fully supports: microvesicles co-purify; band in sucrose at densities including retrovirus density; HLA DR / β2-M / RNA / DNA; EM various sizes/morphologies. Critical historical primary. **M-HIST; M-DENS; M-UC; M-PROT; M-EM; M-RNA** all abstract-justified. Confidence should not be `high` while fulltext=abstract_only (protocol: stop/ask PDF rather than over-claim). |
| **P2-016** | Feng et al. 2013 Nature (abstract) | **A** | **A** | **A** `yes` (nuanced) | **A** `Y` | **D** → `medium` until PDF | PMID 23542590: eHAV “resemble exosomes”; fully infectious; ESCRT (VPS4B, ALIX); blurs enveloped/non-enveloped. Gradient density *does* separate eHAV (low density) from naked HAV (high density) — so bulk methods partially work between eHAV and naked virions; the identity problem is **eHAV vs host exosomes**. `claims_successful_separation=partial` correct. Abstract does not by itself give the “79%” figure used in quotes (publisher/fulltext figure legend territory) — treat 79% as fulltext-dependent. |
| **P2-018** | Bukong et al. 2014 PLoS Pathog (abstract) | **A** | **A** | **A** `partial` | **A** `Y` | **D** → `medium` (or keep high with caveat) | PMID 25275643: patient/culture exosomes contain HCV RNA; receptor-independent transmission; Ago2–miR-122–HSP90; negative-strand RNA. Strong **M-RNA; M-INF; M-CONT**. Uses ExoQuick/UC + **CD63 immuno-selection** — so they operationally enrich a marker-positive infectious fraction (`claims_successful_separation` could be `partial` rather than `no`; minor). Supports infectious-unit identity continuum more than UC-alone inseparability. |

### Spot-check (not full sample mandate)

| ID | Note |
|----|------|
| **P2-005** Meckes & Raab-Traub 2011 | useful Y OK; `states_incomplete=partial` correctly conservative (shared biophysical properties/table of sizes/densities; not “cannot separate” prose). M-EM = cup-shaped EM morphology of exosomes, not strong virus/EV non-discrimination claim. |
| **P2-008** van Niel 2018 | **B correctly held** — EV cell biology background; not dilemma primary. |

---

## Overclaims / underclaims

### Overclaims in `P2_synthesis.md` (relative to evidence quality)

1. **M-EM strength / ID list (synthesis §2)**  
   - Rated **Moderate** with example IDs **P2-001, P2-005, P2-010**.  
   - **P2-001 is not coded M-EM** in `P2_useful.csv` (and fulltext M-EM is only historical one-liner, not a morphology non-discrimination study).  
   - P2-005 EM is largely standard exosome morphology, not a controlled virion-vs-EV TEM discrimination paper.  
   - P2-010 EM claim is abstract-only (“various sizes and morphologies”).  
   - **Recommendation:** Downgrade M-EM to **Weak–moderate** until Bess/Gluschankof fulltexts and primary TEM/cryo-EM comparative studies are extracted. Do not list P2-001 under M-EM unless metrics_coded is amended after re-read.

2. **“Strong” multi-metric bulk-method claim is review-concentrated**  
   - M-SIZE / M-DENS / M-UC / M-PEG “Strong” rests heavily on **the same review cluster** (Nolte-’t Hoen; McNamara/Dittmer; Zhou; Raab-Traub/Dittmer) plus abstract-only 1997 primaries.  
   - Provisional multi-metric claim is appropriately hedged (“still under-determined pending PDFs”) — **keep that hedge**; do not freeze “Strong” labels for argument tables until Tier A primaries are fulltext-extracted.

3. **Using P2-007 (Moulin 2023) as methods-persistence evidence**  
   - Synthesis timeline (“2023–2025 … Dilemma continues”) is fair for *field activity*, but Moulin is **not** a purification-methods codification paper like P2-002/003/004.  
   - Avoid equating “EV–virus intertwining still reviewed in 2023” with “physical separation still demonstrated impossible by methods data.”

4. **Abstract-only high confidence**  
   - P2-010, P2-016 (and to a degree P2-018) coded `confidence=high` + `fulltext=abstract_only` conflicts with protocol §9 (prefer PDF; do not over-claim from abstracts).  
   - Synthesis §3 treats **1997 Bess/Gluschankof as “hard historical evidence”** — justified at *title/abstract strength* for co-banding contamination, but full quotes, methods details, and particle counts remain PDF-dependent.

5. **M-SIZE “High” (synthesis §7)**  
   - Size ranges are repeatedly stated in reviews; independent primary NTA/DLS co-distribution studies are thin in the useful set. Prefer “High in review consensus; primary quantitative size-overlap corpus incomplete.”

### Underclaims / undercoding

1. **P2-006 metrics** under-code explicit UC inseparability language (add M-UC ± M-DENS).  
2. **Counterexamples (synthesis §4)** are appropriately kept; CD45/subtilisin (P2-013–015) and bead isolation (P2-004) correctly bound absolute-inseparability claims — **do not weaken this section**.  
3. Synthesis §5 scope guardrail (“co-purification ≠ no infectious agent”) is correct and should remain frozen language.

---

## Bias notes

### Colleague / seed-network skew (remaining)

| Issue | Evidence |
|-------|----------|
| Full-text core is lab-network heavy | Of 8 local PDFs: P2-002, P2-003, P2-004 Dittmer (UNC); P2-005 Raab-Traub; P2-001 Margolis/Gallo (+ Nolte-’t Hoen); only **P2-006 Giannessi (Roma Tre)** and **P2-007 Moulin (Ottawa)** clearly outside that seed neighborhood among fulltexts. P2-008 van Niel is EV-biology, not virus separation. |
| Circular citation risk | Method tables and density claims recycle across Dittmer-linked reviews (P2-002, P2-003, P2-004) and are re-cited by seeds. Independent primary methods replications still sparse at fulltext. |
| Round 2 partially mitigates | Bess/Gluschankof 1997, Feng 2013, Bukong 2014, Chen 2015, Cantin/Coren/Ott, Dias 2018 — good anti-cherry-pick intent, but **still abstract-only**. |

### Review-heavy bias (remaining)

| Useful Y shape | Problem |
|----------------|---------|
| Seed fulltexts | Mostly **review/perspective**, not primary separation experiments. |
| Many Y rows | Continuum / Trojan / cargo papers (Pegtel, Lenassi, Narayanan, Izquierdo-Useros, Wiley, etc.) support **shared biogenesis or infectious EV fractions**, which is related but **not identical** to “physical purification fails to uniquely define virions.” |
| Risk | Over-weighting M-CONT framing papers can inflate “dilemma strength” without multi-metric primary purification data. Protocol prefers primary methods language when it conflicts with review narrative — **not yet stress-tested** because primaries lack fulltext. |

### Other process notes

- **P2-022 B / P2-023 Y** (Martin et al. 2023): imprint still fuzzy; risk of double-counting one paper.  
- **Class leads** (P2-029, P2-043 imprint, P2-046 DI class, P2-048 monographs): correctly B, but synthesis timeline implies more historical depth than currently quote-backed.

---

## Recommended CSV amendments

*Do not apply here — recommendations only.*

### Field-level changes on sampled / related rows

| ID | Field | Current | Recommend | Rationale |
|----|-------|---------|-----------|-----------|
| P2-001 | metrics_coded | no M-EM | Optional `+M-EM` **or** remove P2-001 from synthesis M-EM list | Align CSV and synthesis. |
| P2-006 | metrics_coded | SIZE;LIPID;CONT;PROT | Add `M-UC` (consider `M-DENS`) | Fulltext explicit UC co-pelleting / no complete separation. |
| P2-007 | supports_dilemma | Y | `mixed` | Biogenesis intertwining >> purification failure. |
| P2-007 | confidence | high | `medium` | Soft separation evidence. |
| P2-007 | metrics_coded | CONT;PROT;HIST | Drop or soften **M-HIST** unless a true historical co-contamination statement is quoted | “Past five years” is not M-HIST as defined. |
| P2-010 | confidence | high | `medium` | abstract_only until PDF. |
| P2-011 | confidence | high | `medium` | Same; title is strong but fulltext pending. |
| P2-016 | confidence | high | `medium` | abstract_only; 79% claim needs fulltext. |
| P2-018 | claims_successful_separation | no | `partial` | CD63 immuno-selection used as operational enrichment. |
| P2-018 | confidence | high | `medium` (conservative) | abstract-level verification only in this pass. |
| P2-003 | metrics_coded | … | Optional `+M-TFF` | Filtration/TFF discussed. |

### Screened-row upgrade / downgrade candidates

| ID | Current | Recommend | Why |
|----|---------|-----------|-----|
| **P2-055** HSV L-particles | B | **Prioritize → Y** when imprint/PDF fixed | Historical noninfectious co-produced particles with density/EM/identity language; high M-HIST value. |
| **P2-046 / P2-047** DI particle classics | B | Keep B until named monographs extracted; then **Y** if co-production/separation language present | Pre-EV vocabulary continuum; synthesis already queues them. |
| **P2-008** van Niel | B | **Keep B** | Correct; background only. |
| **P2-035 / P2-036** pure EV reviews | N | **Keep N** | Correct exclusions. |
| **P2-012 vs P2-013** Cantin cluster | B / Y | Resolve imprint; avoid double use | Discrimination paper should stay Y once DOI/pages locked. |
| **P2-022 / P2-023** Martin 2023 | B / Y | Merge/verify single imprint; do not count twice for “2023 persistence.” | |
| **P2-065** Trojan critiques | B | **Actively upgrade** named adversarial papers in Round 4 | Bias control requires named counter-Trojan literature, not class lead only. |
| Soft Y cargo papers (e.g. P2-051, P2-052, P2-056, P2-062) | Y | Keep Y but flag **low separation-metric density** in synthesis weight | Inclusion OK; do not treat as M-DENS/M-UC support. |

### Missing metric evidence (priority gaps)

| Metric | Status after this audit | Gap action |
|--------|-------------------------|------------|
| **M-EM** | **Thin** | Fulltext Bess/Gluschankof; primary TEM/cryo side-by-side virion vs microvesicle; herpes L-particles. Do not lean on review size tables. |
| **M-TFF** | Coded mainly via P2-002 | Need non-Dittmer primary TFF EV–virus papers if claim “strong.” |
| **M-SEC** | Review-strong (P2-003,004) | Primary SEC co-elution traces still abstract/review-level. |
| **M-HIST pre-1997** | Incomplete | DI / L-particles / purification monographs still B/class. |
| **M-DENS non-HIV** | Partial (HAV eHAV densities in Feng abstract; flavivirus notes) | Primary density tables beyond HIV and HAV needed. |
| **M-MARK counterexamples** | Present but abstract-only (P2-013–015) | Fulltext extract before freezing “partial resolution” bounds. |

---

## Overall agreement (high/medium/low) with provisional synthesis section 2

### Verdict: **MEDIUM** agreement with synthesis §2

**What holds (agree):**

- Multi-metric **overlap / co-purification** as a *recognized field problem* is real in fulltext seeds, especially **M-DENS, M-UC, M-PEG, M-RNA**, with explicit incomplete-separation language (P2-001, P2-002, P2-003, P2-004, and fulltext-confirmed in P2-006).  
- **M-MARK** as **mixed** (partial operational separation) is correctly stated.  
- Provisional multi-metric claim is **appropriately under-determined** pending PDFs; counterexample section (§4) and Discussion-only ontology hinge (§5) are process-correct.  
- Sampled useful=Y decisions for core method papers (P2-001–004, P2-006) are sound.

**What does not yet hold at “Strong” freeze quality:**

- **M-EM** is over-listed / under-evidenced.  
- **M-SIZE** “Strong/High” is review-consensus more than independent primary measurement density.  
- **M-HIST** “1997 clear; earlier incomplete” is fair — but 1997 still abstract-only for quotes at freeze-ready depth.  
- Review- and colleague-skew still inflate the apparent independence of metric supports (same lab cluster restating the same tables).  
- Some Y rows (notably **P2-007**) and abstract_only `confidence=high` rows slightly oversell separation-dilemma strength.

**Process recommendation before freezing synthesis §2 strength labels:**

1. Extract Tier A PDFs (Bess, Gluschankof, Feng, Bukong, Cantin/Coren/Ott, Gould).  
2. Re-weight metrics by **primary vs review** and **fulltext vs abstract**.  
3. Align M-EM example IDs with `metrics_coded`.  
4. Keep absolute-inseparability **out**; keep multi-metric bulk-method limitation **in**, with confidence stratified.

---

*End Agent A review. No CSVs modified.*
