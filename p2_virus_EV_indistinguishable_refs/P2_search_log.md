# P2 search log

**Protocol:** `P2_research.md` v0.1  
**Synthesizer:** grok-primary  
**Main repo path:** `p2_virus_EV_indistinguishable_refs/`  
**Date opened:** 2026-07-22  

---

## Round 0 — Scaffold (2026-07-22)

| Action | Result |
|--------|--------|
| Protocol | `P2_research.md` v0.1 written (P1-style: inclusion, metrics taxonomy, anti-colleague bias, counterexample family) |
| Artifacts created | `P2_search_log.md`, `P2_screened.csv`, `P2_useful.csv`, `P2_quotes.md` (provisional), `agent_reviews/` |
| Pre-existing local PDFs | 8 files under `refs/` treated as **seeds only**, not as complete corpus |

---

## Round 1 — Seeds + transparent bias (2026-07-22)

### 1.1 Seed list (local `refs/`)

| ID | File / paper |
|----|----------------|
| P2-001 | Nolte-’t Hoen et al. 2016 PNAS perspective |
| P2-002 | McNamara & Dittmer 2020 J Neuroimmune Pharmacol (modern techniques) |
| P2-003 | Zhou, McNamara & Dittmer 2020 Viruses (purification + RNA) |
| P2-004 | Raab-Traub & Dittmer 2017 Nat Rev Microbiol |
| P2-005 | Meckes & Raab-Traub 2011 J Virol minireview |
| P2-006 | Giannessi et al. 2020 Viruses (HIV/HCV/SARS) |
| P2-007 | Moulin et al. 2023 IJMS (two intertwined entities) |
| P2-008 | van Niel, D’Angelo & Raposo 2018 Nat Rev Mol Cell Biol (EV cell biology) |

**Bias note:** Seeds over-weight UNC/Dittmer/Raab-Traub/Nolte-’t Hoen network and general EV biology. Round 2 deliberately leaves this neighborhood.

### 1.2 Seed outcomes

- All 8 screened; **P2-001–007 = Y** (identity/separation language).  
- **P2-008 = B** (foundational EV biology; limited virus-separation claims — keep for biogenesis background, not as dilemma primary).  

### 1.3 One-hop snowball from seeds (abstract/title screen)

Leads harvested from seed bibliographies and abstract cross-refs (not full-text snowball yet):

| Lead | Rationale |
|------|-----------|
| Gould et al. 2003 PNAS Trojan exosome | Foundational continuum hypothesis |
| Bess et al. 1997 Virology microvesicles in HIV preps | Pre-exosome era co-purification primary |
| Gluschankof et al. 1997 Virology cell membrane vesicles HIV | Parallel 1997 primary |
| Cantin et al. 2008 J Virol CD45 discrimination | Marker-based separation attempt |
| Ott 2008 Methods Mol Biol / related CD45 subtilisin | Purification protocol for clean HIV proteomics |
| Feng et al. 2013 Nature eHAV / membrane hijacking | Enveloped HAV resembles exosomes |
| Bukong et al. 2014 / Ramakrishnaiah et al. 2013 HCV + exosomes | Infectious RNA in EV-like fractions |
| Théry et al. 2018 MISEV | Standards; purity / contamination context |
| Pegtel et al. 2010 EBV miRNA via exosomes | Viral cargo in EVs (identity of particle type) |

Logged as P2-009 onward in `P2_screened.csv`.

---

## Round 2 — Systematic web queries (2026-07-22)

**Platforms:** Web search (PubMed/PMC/publisher landing pages via web tools). Full PubMed API not used this session.  
**Cap:** Screen top ~15–25 relevance hits per family; log that deeper recall remains for later rounds.

### Family A — separation / indistinguishability language

| Query (approx) | Notes |
|----------------|-------|
| extracellular vesicles viruses co-purification separation density gradient ultracentrifugation review | High review density; confirms multi-method co-enrichment narrative |
| "cannot distinguish" OR indistinguishable OR co-isolate OR co-purif exosomes OR EV virus OR virions | Hits Nolte-’t Hoen 2016; many secondary reviews |

### Family B — method-specific

| Query | Notes |
|-------|-------|
| modern techniques isolation EV viruses McNamara | Seed confirmation + method tables |
| purification methods RNA virus particles extracellular vesicles Zhou | Cargo attribution |
| density gradient separate HIV exosomes CD45 | Cantin 2008; Coren 2008; Ott methods |

### Family C — cargo

| Query | Notes |
|-------|-------|
| RNA packaged virion EV contamination | Zhou 2020; debate on miRNA copy number in EV vs virion |

### Family D — counterexamples (successful separation claims)

| Query | Notes |
|-------|-------|
| separate purify discriminate EVs from virus / virions | Affinity (CD45, CD63 beads), velocity gradients, subtilisin shaving, infectivity assays claimed as partial solutions — **not** “impossible always” |

### Family E — historical

| Query | Notes |
|-------|-------|
| Bess 1997 microvesicles HIV | **Key historical primary** — sucrose density co-banding |
| Gluschankof 1997 vesicles HIV preparations | Parallel primary |
| defective interfering particles membrane virus EM | Continuum language pre-EV field; needs deeper full-text round |
| early exosome virus purification contamination 1980s–2000s | Sparse pre-1997 with modern “EV” vocabulary; 1997 cluster is strong |

### Family F — standards / recent persistence

| Query | Notes |
|-------|-------|
| MISEV 2018 virus contamination | Purity recommendations; viral particle co-isolation awareness |
| EV virus separation 2021–2025 | Martin et al. 2023 Viruses; Dias 2018 Frontiers; field still framing as hard problem |

### Negative / thin results

| Strategy | Result |
|----------|--------|
| Pre-1990 English “exosome virus co-purify” | Vocabulary anachronism; need “cellular debris / microvesicles / membrane fragments” language in virus purification monographs (queued Round 3) |
| Claim that UC alone fully separates all enveloped viruses from EVs | No high-quality hit asserting universal clean UC separation |

---

## Round 3+ (queued)

- Full-text snowball depth 2 from every **Y** with PDF.  
- Virus purification handbooks 1960s–1980s (non-EV vocabulary).  
- Plant / non-enveloped contrast papers.  
- Systematic PubMed export with hit counts (not approximate web).  

---

## PDF request list (user fetch)

See end of session response / `P2_pdf_request.md`. High-priority historical + primary separation papers not in local `refs/`.

---

## Agent verification (2026-07-22)

| Agent | Task | Output | Consumed? |
|-------|------|--------|-----------|
| Agent A | Metrics/coding re-screen sample | `agent_reviews/P2_agentA_metrics_and_coding.md` | Yes — CSV amendments applied for P2-006/007/010/011/013/016/018 |
| Agent B | History + counterexamples | `agent_reviews/P2_agentB_history_and_counterexamples.md` | Yes — Cantin imprint fixed; synthesis hedges noted |

### Agent-driven amendments applied
- P2-006: added M-UC, M-DENS  
- P2-007: supports_dilemma=mixed; confidence=medium; dropped weak M-HIST  
- P2-010/011/016/018: confidence high→medium while abstract_only  
- P2-013: corrected to *J Immunol Methods* 2008 (velocity/AChE), not J Virol CD45  
- P2-018: claims_successful_separation=partial  

### Agent findings retained for next round (not yet all applied)
- M-EM strength weaker than provisional “moderate”  
- 2023–2025 continuity = live topic, not proven methods crisis  
- Pre-1997 DI/L-particles ≠ host EV co-purification without interpretive bridge  
- Esser 2001 CD45 foundation paper to screen  
- Devil’s advocate: velocity + AChE/CD45 + infectivity = practical partial separators  

---

*Log append-only; amend with dated notes, no silent rewrites of prior query strings.*

---

## Round 3–4 pass — 2026-09-22 (box streams agent)

**Platforms:** WebSearch + Unpaywall + EuropePMC PDF render + Crossref. No Sci-Hub.  
**CopyToBox:** unavailable in subagent — MSI `refs/` inventory deferred to parent sync manifest.

### Round 3 queries (pre-1997 / DI / L-particles / MISEV)
| Query family | Outcome |
|--------------|---------|
| HSV L-particles density gradient Szilagyi | P2-075 OA review; P2-078 primary paywalled wishlist |
| DI particles membrane co-purification | Still interpretive bridge only (Agent B hedge retained) |
| MISEV2018/2023 virus purity | P2-019 OA upgraded; P2-079 editorial OA; full MISEV2023 guidelines optional wishlist |

### Round 4 adversarial (claimed clean separation + critiques)
| Query family | Outcome |
|--------------|---------|
| CD45 immunoaffinity HIV microvesicles | P2-076 Esser OA; P2-061 Trubey OA; P2-014 Coren OA (upgrade) |
| iodixanol velocity separate HIV EV | P2-072 Pathogens 2021 OA (sucrose fails; iodixanol optimal); P2-077 JoVE OA; Cantin still paywalled |
| nano-FCM / flow virometry discriminate virion EV | P2-071 Tang 2017 OA — biochemical indistinguishability + NFC success with Env label |
| Critique CD45/AChE/Trojan | P2-073 Pérez/Ostrowski 2019 OA **weakens** CD45/AChE/iodixanol; P2-074 Park/He anti-Trojan |

### OA full texts newly readable on box (`streams/p2_oa/`)
P2-009,014,016,017,018,019,020,021,061,071–077 (+ P2-079 editorial).  
Still NEED_FETCH: Bess, Gluschankof, Cantin, Ott 2009, Szilagyi 1991, Chen 2015.

### CSV deltas
- Screened **70 → 80**; Useful **31 → 40**.  
- DOI corrections: P2-010 Bess `.8499`; P2-011 Gluschankof `.8453`; P2-013 Cantin `10.1016/j.jim.2008.07.007`.  
- Deliverables: `P2_pdf_wishlist.md` (lean), `P2_quotes.md` rebuild, `p2.md` status.

### Negative / limits logged
- No claim that UC/sucrose alone universally separates enveloped virions from EVs.  
- Separation successes are **method- and marker-conditional**; Martin 2019 is mandatory caveat for Discussion.  
- L-particles ≠ host EVs without interpretive bridge.

---

## Evening ingest — 2026-09-22 (~22:50 ET)

**Goal:** Full-text quote ingest of Tier A–C PDFs user fetched to MSI `refs/`.  
**Blocker:** `CopyToBox` + machine-targeted Shell **not exposed** to this executor subagent (same as prior Round 3–4 note). MSI paths unreachable from box.

### What ran
| Action | Result |
|--------|--------|
| EuropePMC OA fetch MISEV2023 (`10.1002/jev2.12404`, PMC10850029) | **OK** → `refs_staging/P2-019b_misev2023_guidelines.pdf`; quote skim virus/EV separation only |
| PMC/EuropePMC PDF for Chen (correct DOI `10.1016/j.cell.2015.01.032`, PMC6704014) | HTML interstitial / not OA package — **not downloaded** |
| Unpaywall | 422 (email); EuropePMC OA=N for Bess/Gluschankof/Cantin/Ott/Szilagyi/Reiter |
| Elsevier/Springer TDM endpoints | no free fulltext |
| Google Drive title search | empty |
| Sci-Hub | **not used** |

### CSV / artifact deltas
- Useful **40 → 42** (+P2-019b fulltext=Y; +P2-080 stub fulltext=N). Screened **80 → 81** (+P2-019b).  
- Chen DOI corrected `.09.032` → `.01.032` in screened + useful notes.  
- Quotes §F appended (MISEV2023 p.5–6,17–18,20).  
- Wishlist / p2.md / sync manifest updated with **parent CopyToBox list**.

### Parent next (required for remaining quote pass)
CopyToBox each MSI file → `streams/refs_staging/<same name>` then re-run pdftotext quote pass for P2-010/011/013/015/044/078/080.

---

## Night quote pass — 2026-09-22 (~22:55 ET)

**Trigger:** Parent CopyToBox completed for Tier A–C MSI PDFs into `streams/refs_staging/`.  
**Actions:** pdftotext all 7; verbatim quotes → `P2_quotes.md` §G; CSV fulltext upgrades.

| ID | PDF identity check | Quote polarity |
|----|--------------------|----------------|
| P2-010 Bess | OK | Weaken sucrose/UC; immunoaffinity suggested |
| P2-011 Gluschankof | OK | Weaken; virions minority |
| P2-013 Cantin | OK | Strengthen Optiprep velocity + AChE; dens/marker caveats |
| P2-015 Ott | OK | Strengthen subtilisin/CD45 remediation + limits |
| P2-078 Szilagyi | OK | Partial H vs L; ≠ host EV |
| P2-044 Chen | **MISFILE** = Zhai Pol IV siRNA | No Chen quotes; need correct DOI PDF |
| P2-080 Reiter | OK | Strengthen heparin VLP vs EV (gag VLP system) |
| P2-019b | Prior evening | MISEV NVEP/virus co-class |

**Counts:** Useful n=42 (fulltext Y newly: 010,011,013,015,078,080; 044 still N/misfile; 019b already Y).  
**Next:** Replace P2-044 PDF; then draft `P2_synthesis.md`.

- 2026-09-22 23:00 ET — P2-044 corrected Chen PDF ingested with `pdftotext`; §H quotes added; fulltext=Y, counterexample value=partial (weakens naked-virion-only framing), DOI `10.1016/j.cell.2015.01.032`; misfile corrected.

---

## Round 5 — non-retrovirus / historical expansion (2026-11-14)

**Rationale:** Rebalance the corpus away from the retrovirus/HIV-heavy core toward (a) non-retrovirus primary and review sources and (b) pre-1997 historical primaries, closing synthesis gaps §6.2 (non-retrovirus density tables) and §6.3 (pre-1997 purification). This also honors AX012 (HIV/phage out of the ontology scope; new load-bearing items avoid HIV as primary system).

**Platforms:** WebSearch + PMC full text + PLoS/Frontiers OA full text. No Sci-Hub; no paywalled fetch (paywalled items queued to wishlist).

### New query families (pre-registered)
| Family | Query (approx) | Outcome |
|--------|----------------|---------|
| **G — historical incomplete/DI influenza** | influenza "von Magnus" incomplete particles density gradient noninfectious | P2-081 von Magnus 1954 (paywalled B); P2-082 Ada & Perry 1956 (Y); P2-083 Morgan/Hsu/Rose 1962 (Y, OA PMC) |
| **H — pre-1997 virus purification monographs** | herpes simplex purification "cellular debris"/"membrane vesicles" | P2-086 Spear & Roizman 1972 (Y, OA PMC); P2-087 Gentry & Randall 1973 (B, paywalled) |
| **I — non-enveloped / non-retrovirus EV association** | rotavirus/poliovirus non-enveloped extracellular vesicles 2020 | P2-089 Iša 2020 (Y, OA PMC); P2-092 Altan-Bonnet 2025 review (B, paywalled) |
| **J — KSHV / herpesvirus co-purification primary** | Chugh KSHV exosome copurification CD63 | P2-084 Chugh 2013 (Y, OA PLoS); P2-088 Loret 2008 HSV virions (Y, OA PMC) |
| **K — recent persistence + EM artifact** | SARS-CoV-2 EV co-isolation safety; cup-shape TEM artifact | P2-090 Nunez Lopez 2021 (Y, OA); P2-091 Martins & Alves 2020 (Y, OA); P2-093 Defourny 2026 (B, paywalled) |

### CSV deltas
- Screened **81 → 94**; Useful **42 → 50**.  
- 8 new Y rows (P2-082, 083, 084, 086, 088, 089, 090, 091); 5 new B rows queued to wishlist (P2-081, 085, 087, 092, 093).  
- New DOI/PMID for all Y rows verified on PMC/PLoS/Frontiers. P2-085 (Marichal-Gallardo) DOI left `not_seen` (ScienceDirect pii only) per no-guess rule; P2-087 author line flagged "verify on fetch."

### Bias-control notes
- All 8 new Y are **non-retrovirus** (influenza × 3, HSV × 2, KSHV, rotavirus, SARS-CoV-2, plus the EM-artifact review).  
- Counterexamples kept: P2-088 (Ficoll purity achievable) and P2-084 (CD63 affinity separates) bound the dilemma.  
- Pre-1997 documentary evidence now reaches 1956–1972, 25–40 years earlier than the prior 1997 anchor.

### Leads deferred (no ID assigned; verify before screening)
- Santiana et al. 2018 "Vesicle-cloaked virus clusters are optimal units for intercellular transmission" (*Cell Host Microbe*) — snowball from P2-089; Altan-Bonnet lineage; verify citation/DOI before assigning an ID.
- van der Grein et al. 2018 (EV/virus classification + purification) — cited by P2-091 for the "similar size, density and composition … cannot be separated" statement; verify citation/DOI before assigning an ID.

---

## Round 5 — fetch confirm + ref-tracking refactor (2026-11-14)

**Owner dropped 12 of the 13 Round-5 PDFs into `refs/`.** Identity confirmed by title/author text
extraction (PyMuPDF) for each; a correction surfaced during confirm:

| ID | Confirm result |
|----|----------------|
| P2-081 von Magnus 1954 | ✓ *Adv Virus Res* 2:59-79 chapter author/title confirmed (21 pp) |
| P2-082 Ada & Perry 1956 | ✓ J gen Microbiol 14:623-633 |
| P2-083 Morgan, Hsu & Rose 1962 | ✓ authors "Councilman Morgan" et al., J Exp Med 116:553 |
| P2-084 Chugh 2013 | ✓ PLoS Pathog 9:e1003484 |
| P2-086 Spear & Roizman 1972 | ✓ J Virol 9:143-159 |
| P2-087 | ⚠ **author line corrected → Vahlne AG & Blomberg J, J Gen Virol 1974;22(2):297-302** (not "Gentry & Randall"; the DOI/PMID/title were right, the prior author attribution was a mis-citation from a 1985 thesis) |
| P2-088 Loret 2008 | ✓ J Virol 82:8605 |
| P2-089 Iša 2020 | ✓ Viruses 12:763 |
| P2-090 Nunez Lopez 2021 | ✓ Front Immunol 12:617042 |
| P2-091 Martins & Alves 2020 | ✓ Front Cell Infect Microbiol 10:593170 |
| P2-092 Altan-Bonnet & Panigrahi 2025 | ✓ Annu Rev Biochem 94:531-560, **open access (CC), not paywalled** |
| P2-093 Defourny et al. 2026 | ✓ FEMS Microbiol Rev 50:fuag028 (full title incl. subtitle) |

**Outstanding:** P2-085 Marichal-Gallardo 2017 (ScienceDirect; pii only) remains on the wishlist.

### Ref-tracking refactor (align to CONVENTIONS §8 / research-strategy §2-3)
- Removed the tracked `P2_pdf_catalogue.md` "Please fetch" section; the wishlist is now the gitignored
  `P2_pdf_wishlist.md` at stream root (fetch-only queue, single outstanding row).
- Split the tracked catalogue into the two bibliographies: `P2_bibliography.md` (used: quoted/currently
  contributing) and `P2_bibliography_unused.md` (fetched/read but not load-bearing: P2-008, 081, 087,
  092, 093).
- Abstracts not yet fetched remain only in `P2_screened.csv` (screening log), per the read-before-use rule.
