# P3 Step 1 Results — draft (exploration)

**Date:** 2026-09-21 (pass **21N** snapshot)  
**Status:** Working draft for paper-facing Results / Methods. **Step 1 is not finished** — 1 chain still open (LASSA-O1); wishlist lean.  
**Tone:** Parallel to P2 (hypothesis → predict X → find X). Census and documentation, not advocacy.

---

## 1. Locked spine

1. **Culture ± CPE is not virus-specific** (same physical/operational detector problem developed in P2).
2. Therefore genetics that **samples material produced by culture ± CPE “isolation”** inherits that non-specificity.
3. **If a large share of origin / type genome deposits — the foundation of viral genetics — document culture ± CPE (or closely related culture-propagated) sample production, that is a major concern:** the reference graph is built on the same non-specific detector.

Step 1 asks an empirical census question: for named viruses, what fraction of first (and major confirming) public genomes rest on **culture ± CPE** vs clinical-direct, other, or still-open paths?

---

## 2. Methods one-pager

### Bar
Adequate **documentary** evidence linking **sample-production method ↔ deposited genome** within reasonable scientific doubt — **not** forensic chain-of-custody. Acceptable patterns include (examples only): deposit Methods stating how sequenced material was produced; methods-citation chains to stock/isolate papers clearly used for that material; seed-lot / vaccine-seed history; GenBank/paper Methods blocks. Close when method↔deposit is clear; quote Methods. Prefer honest `culture_cpe` when CPE / plaques / syncytia warrant exists; do **not** inflate `culture_no_cpe` into `culture_cpe`.

### Event types
- **O (origin):** first/defining complete (or near-complete) sequence report for that named virus/strain ontology.
- **C (confirmation):** later resequence / independent complete genome / major correction of the same type material.
- **P (provenance node):** upstream paper that does not itself deposit the genome but supplies sample/stock/RNA/DNA used by an O/C.

### path_score (closed events)
| Code | Meaning |
|------|---------|
| `culture_cpe` | Sequenced material from cell culture; resolved record documents CPE / plaques / syncytia as isolate or stock warrant |
| `culture_no_cpe` | Culture/propagated stock clear; CPE/plaques never stated as warrant in resolved record |
| `clinical_direct` | Sequenced from clinical/tumor specimen without culture passage for that material |
| `other` | Eggs, animal-only, synthetic/clone/reverse-genetics confirmation, etc. |
| `unclear` | Reserved; open chains remain `chain_open` rather than forced unclear |

### Access
Prefer OA/PMC; paywalled PDFs only when user-supplied into gitignored `refs/sequence_origins/`. No Sci-Hub.

---

## 3. Counts (snapshot 2026-09-21 ~22:15 ET, pass **21N**)

| Metric | n |
|--------|---|
| Events (O+C) | **102** |
| `chain_closed` | **101** (99%) |
| `chain_open` | **1** (1%) |

### path_score among closed

| path_score | n closed | % of closed |
|------------|----------|-------------|
| `culture_cpe` | **36** | 36% |
| `culture_no_cpe` | **45** | 45% |
| `clinical_direct` | **11** | 11% |
| `other` | **9** | 9% |

| Culture-propagated (`culture_cpe` + `culture_no_cpe`) | **81** / 101 closed (**80%**) |
| `culture_cpe` alone | **36** / 101 closed (**36%**) |

**Read for the spine:** among closed events, culture-propagated paths dominate; the CPE-warranted subset is substantial but not the whole culture story — report both separately.

**Pass 21N closes:** COV-O7, HSV-O1, CHIK-O1, CMV-O1 — all `culture_no_cpe` (see `P3_step1_path_type_map_2026-09-21.md`). Still open: LASSA-O1 only.


## 4. All closed `culture_cpe` events (36)

| event_id | virus | year | 1-line Methods warrant |
|----------|-------|------|------------------------|
| ADE-O1 | human adenovirus 2 | 1986 | Upstream ADE-O2 Gingeras: Ad2 preparations including one from recently plaque-purified stock — plaque warrant for sequenced Ad2... |
| ADE-O2 | human adenovirus 2 | 1982 | Gingeras explicitly notes Ad2 preparations including one derived from a recently plaque-purified stock; heterogeneity persists ... |
| BTV-C1 | bluetongue virus | 2010 | KC passage without CPE; BHK-21 passage causing 100% CPE at 4 dpi; SNT plates also read for CPE. Genome amplicons from culture s... |
| BTV-C2 | bluetongue virus | 2020 | Plaque-selected on Vero; harvested when cytopathic effect was advanced. |
| BVDV-C1 | bovine viral diarrhea virus | 2013 | Yes — cytopathic vs noncytopathic biotypes defined by effect on cultured cells; separation/cloning by plaque formation; SuwaCp ... |
| BVDV-C2 | bovine viral diarrhea virus | 2019 | Yes for cp isolate — SLO/2416/2002 produced cytopathic effect on BT cells; SLO/1170/2000 explicitly no CPE (ncp) |
| CDV-C1 | canine distemper virus | 2004 | yes — viral CPE in Vero (granular cytoplasm/vacuolization); 2001 viruses formed large syncytia in tissue and during primary iso... |
| CDV-C3 | canine distemper virus | 2021 | Daily CPE observation; syncytial effect/detachment; third passage JA88 confluent CPE (~80%) at 48 h; CPE-positive cultures → wh... |
| COV-C5 | SARS-CoV-2 | 2020 | Clear cytopathogenic effects after 3 days; IF + rising qPCR; EM coronavirus morphology |
| COV-O2 | SARS-CoV | 2003 | Vero E6 isolation with CPE standard for Urbani (accompanying CDC/Drosten era); Rota Science Methods/SOM reference cultured Urbani |
| COV-O5 | human coronavirus NL63 | 2004 | yes — CPE first noted day 8 on tertiary monkey kidney (diffuse refractive CPE then detachment); more pronounced CPE on LLC-MK2 ... |
| COV-O6 | MERS-CoV (HCoV-EMC/2012) | 2012 | yes — cultures checked daily for cytopathic changes; day-3 Vero supernatant used for genome characterization; COV-MERS-P1 Zaki ... |
| DEN-O1 | dengue virus type 2 | 1988 | plaque morphology discussed; culture-propagated DEN-2 |
| EBO-O1 | Zaire ebolavirus | 1993 | plaque-purified 3 times; passaged in E6/Vero |
| EV71-C1 | enterovirus 71 | 1999 | prior Brown 1995 total-CPE harvest path for BrCr lineage |
| EV71-C2 | enterovirus A71 | 2025 | Yes — RD cultures showing cytopathic effects harvested; plaque-purified twice in Vero |
| EV71-O1 | enterovirus 71 | 1995 | harvested by freezing/thawing when total cytopathic effect was seen |
| FMDV-C1 | foot-and-mouth disease virus | 2022 | Yes — plaque purification (agar overlay, plaques picked for sequencing); classical plaque warrant |
| FMDV-O1 | foot-and-mouth disease virus | 1984 | yes — plaque-purified at beginning of passages and again after passage 16 (plaque = CPE-equivalent warrant per protocol) |
| HEND-O1 | Hendra virus (equine morbillivirus) | 2000 | yes — Wang 1998: HeV isolated and plaque purified as previously described (17,29); HEND-P2 Murray abstract: syncytia in endothe... |
| JC-O1 | JC polyomavirus | 1984 | Padgett: cytopathic effect in human fetal glial cultures |
| MEA-C1 | measles virus | 2001 | MEA-P1: harvest when CPE in 70–80% monolayer; Enders 1954 cytopathogenic origin of Edmonston |
| MEA-O1 | measles virus | 1988 | Upstream Enders & Peebles 1954: cytopathogenic agents from measles throat washings/blood in human/monkey kidney (syncytial gian... |
| MUM-O1 | mumps virus | 2000 | yes — well-isolated virus plaque picked from vaccine; rMUV-induced plaques on Vero (ELISA); MUV-induced syncytia on Vero |
| NDV-O1 | Newcastle disease virus | 1999 | plaque-purified three times on primary chicken embryo fibroblasts |
| NIPAH-C1 | Nipah virus | 2005 | yes — characteristic cytopathic effect, syncytium formation on Vero E6 |
| RSV-C1 | human respiratory syncytial virus | 1995 | yes — plaques showed cytopathic effects characteristic of RSV, notably syncytium formation; F-stained and neutral-red plaques |
| RUB-O1 | rubella virus | 1990 | Hemphill: plaque-purified Therien additional two times in Vero |
| SIN-O1 | Sindbis virus | 1984 | small-plaque variant (plaque phenotype); scored culture_cpe via plaques |
| VSV-C1 | vesicular stomatitis Indiana virus | 2019 | Explicit: Once 80 to 90% of the cells exhibited a cytopathic effect, the supernatant was harvested. Title/abstract: plaque isol... |
| WNV-C1 | West Nile virus | 2004 | yes — plaque-purified variants; mouse virulence PFU; plaques used for glycosylation-motif variants |
| WNV-O1 | West Nile virus | 1999 | Cells examined for cytopathologic effect for up to 7 days after inoculation |

---

## 5. Contrast: `clinical_direct` and `other`

### clinical_direct (n=10)
Examples:
- **B19-O1** (human parvovirus B19, 1986): no culture
- **BOCA-O1** (human bocavirus, 2005): n/a — clinical_direct; no culture for sequenced genomes DQ000495/496
- **COV-O4** (human coronavirus HKU1, 2005): isolation unsuccessful; no CPE-based stock for sequenced material
- **COV-O8** (SARS-CoV-2, 2020): no culture/CPE for sequenced material
- **HBV-O1** (hepatitis B virus, 1979): n/a (serum Dane particles; no culture isolation)
- **HPV-O1** (human papillomavirus type 16, 1985): no culture for sequenced HPV16 DNA
- **MCPYV-O1** (Merkel cell polyomavirus, 2008): Feng 2008 Science abstract/PMC record: studied MCC samples by digital transcriptome subtraction; identification and sequence an...
- **NOR-O1** (Norwalk virus, 1990): no culture (Norwalk historically non-cultivable); stool particles
- **SAPO-C1** (sapovirus (Sapporo virus), 2017): Total RNA was extracted from 200-μL aliquots of two stool supernatants (S3 and S6)… Ion total RNA-seq… SaV contigs → KY040366. ...
- **ZIKV-C1** (Zika virus, 2008): n/a — no isolate obtained

### other (n=7)
Examples:
- **FLU-B-O1** (influenza B virus, 1982): n/a (eggs)
- **FLU-O1** (influenza A virus, 1981): n/a (eggs; not cell-culture CPE)
- **HAV-O2** (hepatitis A virus, 1987): n/a (animal liver)
- **HCV-O1** (hepatitis C virus, 1989): no culture isolate (HCV not cultured then)
- **HEV-O1** (hepatitis E virus, 1991): n/a (animal passage)
- **MEA-C2** (measles virus, 1995): Syncytia/plaques documented for rescued virus only — not the production path of the cloned antigenome sequence
- **YFV-O1** (yellow fever virus, 1985): eggs/vaccine adaptation (not cell-culture CPE path for 17D seed)

These contrast paths matter for honesty: the spine concerns culture ± CPE foundations, not a claim that every genome is culture-derived.

---

## 6. Limitations

- **5 chains still open**, many wishlist-blocked: ASTRO-O1, BTV-O1, BVDV-O1, CDV-O1, CHIK-O1, CMV-O1, COV-O7, CSFV-O1, FCV-O1, HPIV1-O1, HSV-O1, LASSA-O1, MARB-O1, NIPAH-O1, SAPO-O1, ZIKV-O1.
- **HSV-O1 / CHIK-O1** marked could_not_obtain (Albert).
- Soft bar closes documentary method↔deposit links; it does **not** reconstruct forensic tube custody.
- O/C mix and family coverage are opportunistic (OA + user PDFs), not a random sample of viral taxonomy.
- Some closed consensus/compilation events (e.g. ADE-O1) inherit warrant from constitutive upstream Methods.
- **Step 1 is not done.** Fractions will move as wishlist PDFs arrive.

---

## 7. Prior-art pointer

See `P3_prior_art_genome_provenance_critiques_2026-09-21.md` and `P3_framing_parallel_to_P2_2026-09-21.md`. Prior critiques of thin INSDC isolate metadata, MIUViG isolate-vs-UViG, and passage-history gaps make the census question legitimate; Step 1 supplies a paper-first method↔deposit count rather than metadata scraping alone.

---

*Draft only — for internal paper assembly. Do not overclaim completeness.*


---

## Pass 21M census snapshot (2026-09-21 ~21:30 ET)

**Step 1 still not done.** Evening wishlist batch (22 PDFs) processed.

| Metric | 21L | 21M |
|--------|-----|-----|
| Events | 101 | **102** |
| chain_closed | 85 | **97** |
| chain_open | 16 | **5** |
| culture_cpe (closed) | 32 | **36** |
| culture_no_cpe | 36 | **41** |
| clinical_direct | 10 | **11** |
| other | 7 | **9** |

**New culture_cpe closes (Methods warrants):** NIPAH-O1 (maximal CPE on Vero E6); ASTRO-O1 (CaCo-2, RNA before c.p.e.); BVDV-O1 (plaque×3 + cytopathic); BTV-O1 (plaque-cloned BHK-21).

**New other closes:** ZIKV-O1 (suckling-mouse-brain RNA); MARB-O1 (guinea-pig blood virions).

**Still open (as of 21M):** CMV-O1, COV-O7, LASSA-O1 (PDF insufficient), HSV-O1 / CHIK-O1 (could_not_obtain). *(Superseded by 21N — see below.)*

Soft bar unchanged: method↔deposit within reasonable doubt; quote Methods; no CPE inflation.

---

## Pass 21N census snapshot (2026-09-21 ~22:15 ET)

Four former blockers closed on newly obtained Methods PDFs (all `culture_no_cpe`). Fleckenstein 1982 Gene obtained for CMV-O1.

| Metric | 21M | 21N |
|--------|-----|-----|
| Events | 102 | **102** |
| chain_closed | 97 | **101** |
| chain_open | 5 | **1** |
| culture_cpe (closed) | 36 | **36** |
| culture_no_cpe | 41 | **45** |
| clinical_direct | 11 | **11** |
| other | 9 | **9** |

**21N closes:** COV-O7 (Thiel 2001 MRC-5→cDNA→vaccinia insert); HSV-O1 (McGeoch 1988 strain 17 plasmid DNA); CHIK-O1 (Khan 2002 S27 C6/36); CMV-O1 (Chee 1990 + Fleckenstein 1982 Ad169 virion DNA cosmids).

**Still open:** LASSA-O1 only (Auperin Methods = “viral RNA templates”; upstream Josiah production still needed).

Deliverables: `P3_step1_path_type_map_2026-09-21.md`; `P3_step1_path_type_counts_2026-09-21.png`; `P3_step1_path_type_by_family_2026-09-21.png`; tar `P3_step1_findings_resync_2026-09-21N.tar.gz`.
