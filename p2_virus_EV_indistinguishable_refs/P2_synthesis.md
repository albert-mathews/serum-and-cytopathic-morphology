# P2 synthesis (provisional — Round 1–2; not frozen)

**Date:** 2026-07-22  
**Status:** Working synthesis after seed full-texts + web abstract screen. **Do not treat as final** until Tier A PDFs extracted and agent reviews consumed.  
**Stance:** Descriptive patterns from logged literature; Discussion ontology hinge deferred until extraction freezes.

---

## 1. Corpus shape so far

| Class | n (approx) | Notes |
|-------|------------|-------|
| Screened IDs | ~70 | `P2_screened.csv` |
| Useful Y | ~30 | Many abstract-only pending PDF |
| Borderline B | ~25 | Class leads, imprint TBD, background |
| Not useful N | ~10+ | Pure EV biology / therapy / noise |
| Full text held | 8 seeds | Still colleague-skewed for full text |

**Bias control progress:** Round 2 added Bess/Gluschankof 1997, Feng 2013, Bukong 2014, Chen 2015, Cantin/Coren/Ott methods, Dias 2018, Giannessi/Moulin already non-UNC, MISEV2018. Round 3 must deepen pre-1997 virus-purification monographs and non-retrovirus systems.

---

## 2. Metrics: where the dilemma appears

Coded from useful rows (M-* taxonomy in `P2_research.md`):

| Metric | Supported by literature so far? | Example IDs |
|--------|----------------------------------|-------------|
| **M-DENS** density band overlap | **Strong** | P2-001,002,003,010,011 |
| **M-UC** UC co-pelleting | **Strong** | P2-002,003,004,010 |
| **M-SIZE** diameter overlap | **Strong** | P2-001,005,006 |
| **M-PEG** precipitation co-enrich | **Strong** | P2-002,003,004 |
| **M-SEC** co-elution | **Moderate–strong** | P2-003,004 |
| **M-EM** morphology non-discriminating | **Weak–moderate** (Agent A: thinner than first pass) | P2-010 abstract; P2-005 morphology tables; need primary TEM comparisons |
| **M-PROT / M-LIPID** shared host components | **Strong** | P2-001,005,006,009,021 |
| **M-RNA** cargo mis-attribution risk | **Strong** | P2-003,018,020,052 |
| **M-MARK** affinity partial separation | **Mixed** | P2-004 beads “no co-purify”; P2-013–015 CD45 methods **work partially** |
| **M-INF** infectivity vs particle identity | **Strong in HCV/HAV/enterovirus** | P2-016,017,018,044 |
| **M-CONT** continuum / Trojan / hybrid | **Strong as framing** | P2-001,009,016,043 |
| **M-HIST** historical recognition | **1997 clear; earlier incomplete** | P2-010,011; DI/L-particles queued |

**Provisional multi-metric claim (still under-determined pending PDFs):**  
Physical bulk methods (UC, density, PEG, often SEC) **do not uniquely define** virions vs EVs for many enveloped and some non-enveloped culture systems. Marker/infectivity/affinity methods can **partially** resolve subpopulations but (a) assume the dual classification, (b) exclude marker-negative particles, (c) were developed **because** co-purification is real.

---

## 3. Historical perspective (provisional timeline)

| Era | What the record shows (so far) |
|-----|--------------------------------|
| **Pre-1990s** | Classic **defective interfering (DI)** particles and herpes **L-particles** = noninfectious co-produced particles (queued full-text). Virus purification monographs likely discuss “cellular debris/membrane contamination” under non-EV names — **not yet systematically extracted**. |
| **1997** | **Bess** and **Gluschankof**: microvesicles / cell membrane vesicles are major contaminants of **gradient-purified HIV-1**; same density range; EM heterogeneous. This is hard historical evidence that co-isolation predates the modern EV boom. |
| **2003–2006** | **Gould Trojan exosome** hypothesis; **Booth** shared budding domains; macrophage exosome-pathway budding papers. Dilemma reframed from “contamination” toward **shared biogenesis / continuum**. |
| **2008–2009** | **CD45 / subtilisin** methods (Cantin, Coren, Ott) = field admits problem by inventing remediation for proteomics of “pure” virions. |
| **2010–2016** | Explosive EV–virus literature: EBV miRNA exosomes; HCV infectious exosomes; HAV eHAV; Nolte-’t Hoen **“almost impossible to distinguish/separate”**. |
| **2017–2020** | Method reviews (Raab-Traub/Dittmer; McNamara/Dittmer; Zhou RNA; Giannessi) codify multi-method co-purification tables. |
| **2018** | **MISEV2018** institutionalizes EV purity/characterization standards (virus wording to verify on PDF). |
| **2023–2025** | EV–virus **biology** still actively reviewed (Moulin 2023; thin recent reviews). **Methods-impossibility continuity is weaker** (Agent B): live topic, not a proven permanent crisis. |

**Does it continue today?** As a **live research topic** (biology + co-handling), yes—not a closed 1990s artifact. As “bulk physical separation remains non-unique,” support is strong through ~2016–2020 method reviews; post-2020 is thinner in this corpus.

---

## 4. Counterexamples (must keep)

Do **not** claim absolute inseparability:

1. **Affinity / CD45 depletion / subtilisin** can reduce microvesicle contamination in HIV proteomics (P2-013–015).  
2. **Marker-positive bead isolation** of EVs can reduce free virion co-isolation for some systems (P2-004 table).  
3. **Infectivity / neutralization / capsid markers** can functionally distinguish some fractions (e.g. naked vs eHAV; p24 vs AChE).  
4. **Velocity gradients** sometimes separate HIV from some EV markers (cited in P2-001).  

These show **partial operational discriminants**, not a general physical uniqueness proof of two particle classes under Isolation→purify→EM.

---

## 5. Alignment with paper hinge (careful)

Literature **supports**: multi-metric co-purification and field language that complete physical separation is often impossible; problem historically visible by 1997 and ongoing.

Literature **does not by itself prove**: “virions were never observationally grounded.” That remains a **Discussion prediction** linking P2 to Isolation under-determination (detection layer), not a result of EV reviews alone.

**Scope guardrail remains:** co-purification ≠ no infectious agent.

---

## 6. Gaps / next rounds

1. Full-text extract Tier A–C PDFs (`P2_pdf_request.md`).  
2. Pre-1997 purification manuals / DI / HSV L-particles with quotes.  
3. Non-retrovirus density tables (flavivirus, herpes, influenza) primary papers.  
4. Named critiques of Trojan hypothesis (adversarial).  
5. Agent re-screen agreement rates.  
6. Rebalance away from review-heavy corpus toward primaries.

---

## 7. Provisional counts for argument building

| Statement type | Working support level |
|----------------|----------------------|
| Size overlap | High (multiple independent reviews + HIV preps) |
| Density overlap | High (1997 primaries + modern reviews) |
| UC/PEG co-enrichment | High |
| RNA attribution ambiguity | High (Zhou + HCV EV papers) |
| Continuum framing in field | High (Nolte-’t Hoen; Gould; HAV/enterovirus vesicles) |
| “Solved by modern methods” | **Low** — methods mitigate, do not erase multi-metric problem |
| Pre-1997 systematic EV-named literature | Low (vocabulary); high for microvesicle contamination once 1997 read |

---

*Update after agent reviews and user PDF drop; freeze only after Round 4 adversarial pass.*
