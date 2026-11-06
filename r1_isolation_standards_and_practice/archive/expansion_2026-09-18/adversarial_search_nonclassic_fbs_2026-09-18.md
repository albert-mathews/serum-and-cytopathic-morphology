# Adversarial literature search: non-classic FBS / serum protocols in virus isolation

**Date:** 2026-09-18 (America/Toronto)  
**Goal:** Find virus-isolation / cell-culture papers and institutional SOPs whose serum protocol does **not** match classic **10% growth → 2% maintenance**, to show the R1 corpus is not cherry-picked.  
**Machine outputs:** `expansion/adversarial_search_nonclassic_fbs_2026-09-18.md`, `expansion/adversarial_candidates.csv`  
**Corpus check:** Compared against `isolation-refs-dual-fbs_only.csv` (n=103 dual-coded) and `isolation-refs-overview_expanded.csv` (n=129). Candidate URLs in ADV* are **new** relative to known links in those CSVs (Ebola MDPI 10→2–10 already known as VI25; excluded from ADV set).

---

## Methods

### Existing corpus baseline (not adversarial hits)

From `isolation-refs-dual-fbs_only.csv` pair distribution:

| Pre → Post | n |
|---|---|
| **10 → 2** | **60** |
| 10 → 5 | 5 |
| 5 → 2 | 4 |
| 10 → 1 | 4 |
| 10 → 3 | 3 |
| 10 → 0 | 3 |
| Other explicit non-10→2 | ~24 more rows |

So R1 already contains non-classic pairs; this adversarial pass seeks **additional external** counterexamples (and institutional guidelines) rather than re-listing VI59, VI73, VI216, etc.

### WebSearch queries run (box)

1. `"virus isolation" "maintenance medium" "5%" FBS OR FCS`
2. `"virus isolation" "serum-free" OR "without serum" cell culture`
3. `"virus isolation" "10% FBS" OR "10% fetal" maintenance same after inoculation`
4. `"primary isolation" virus "2% horse" OR "lamb serum" OR "calf serum" NOT fetal`
5. `WHO CDC EU virus isolation cell culture serum concentration guideline FBS maintenance` (weak hit set)
6. `"shell vial" isolation medium FBS OR FCS percentage OR "5%" OR "10%" OR serum-free`
7. `influenza OR enterovirus OR adenovirus isolation "serum free" OR "0% FBS" OR "without FBS" OR trypsin overlay`
8. `veterinary virus isolation "5% FBS" OR "15% FBS" OR "10% horse serum"`
9. `"5% FBS" OR "5% fetal bovine" OR "5% FCS" "virus isolation" OR "after inoculation" OR "maintenance medium"`
10. `"horse serum" OR "tryptose phosphate" OR TPB virus isolation cell culture`
11. `"maintenance medium containing" OR "maintained with" FBS virus isolation`
12. `"maintained with 5% FBS" OR "maintenance media" "5% FBS" herpes OR "shell vial"`

### WebFetch / open sources used for numbers

- PMC5857075 (Dill et al. FMDV)  
- ANSES FMDV Virus Isolation PDF  
- USDA APHIS VIRPRO1013.pdf  
- EID YFV appendix PDF (24-0108-app1)  
- IntechOpen Lednicky chapter 40221  
- ATCC Virology Culture Guide  
- PLOS One Zika isolation (abstract/methods via search + PMC mirror)  
- PubMed / DOI abstracts for Johnston 1990, McSwiggan 1981, bovine enterovirus 1962, CMV Cytometry 1988, Vaccines 2020, protocols.io WNV & SARS-CoV-2  

**Policy:** No copyrighted full PDFs downloaded into tracked paths beyond open institutional PDFs already public. Percentages recorded only when explicit.

### Classification scheme

- **Class A:** Documented dual FBS (or same serum type) with **pre→post ≠ 10→2**  
- **Class B:** **Same %** both stages (e.g. 5→5, 3→3, 0→0)  
- **Class C:** Serum-free / **0% post** (trypsin overlays, ACFM, “without FBS”)  
- **Class D:** Non-FBS serum (NBCS, adult bovine, horse, TPB as major supplement, calf instead of FBS)  
- **Class E:** Promising but paywalled / FBS unclear (few reserved; most ADV entries have explicit numbers)

Entries may carry multiple tags (e.g. `A;D`).

---

## Results summary

| Pattern class (tag) | Mentions in ADV001–ADV020 |
|---|---|
| A | 10 |
| B | 4 |
| C | 7 |
| D | 5 |

**Solid non-classic candidates with explicit numbers:** **20** (ADV001–ADV020), all new vs R1 dual/overview URLs checked.

Honesty note: Classic **10→2** remains very common in the literature (and in R1). Adversarial search does **not** claim 10→2 is rare—only that **other documented patterns exist** across viruses, cells, decades, and **institutional SOPs**, so a corpus dominated by 10→2 is a sampling skew, not a universal law.

---

## Hits by class (selected)

### Class A — dual FBS ≠ 10→2

| ID | Pre→Post | Virus / cells | Why useful |
|---|---|---|---|
| ADV001 | 10→5 | FMDV / BHK adherent | Explicit infection medium 5% |
| ADV003 | 10→5 | HSV clinical / RD, ML, MRC-5 vials | Diagnostic isolation; 5% maintenance |
| ADV004 | 10→5 | ZIKV / C6/36 | Primary mosquito isolation; also TPB |
| ADV005 | 10→1 | YFV / Vero | Open EID methods; 1% not 2% |
| ADV011 | ~5–10 → 5–20 | USDA CVB master-seed passage | Institutional: maintenance **up to 20%** |
| ADV012 | 10→3 | Ophthalmic viruses / Hep2 | Primary isolation 3% serum |
| ADV016 | 10→5 | CMV shell vial / fibroblasts | Classic shell-vial feed 5% |

### Class B — same % both stages

| ID | Pattern | Notes |
|---|---|---|
| ADV006 | 5→5 | WNV Vero isolation SOP |
| ADV010 | 0→0 | SF MDCK / SF Vero E6 isolation |
| ADV019 | 3→3 | SARS-CoV-2 Opti-MEM 3% FBS |

### Class C — serum-free / 0% post

| ID | Pattern | Notes |
|---|---|---|
| ADV007 | →0 | **ANSES FMDV isolation SOP** “without FBS” |
| ADV008 | 10→0 + trypsin | Clinical H3N2 MDCK isolation |
| ADV009 | →0 | **ATCC**: influenza viral medium no FBS |
| ADV015 | 5→0 | Bovine enterovirus primary isolation |
| ADV018 | 5→0 / SF | Vero influenza MDV work |

### Class D — non-FBS serum / TPB

| ID | Serum | Notes |
|---|---|---|
| ADV013/014 | Newborn calf serum | HEK 10→2 NBCS; HEI **15→2** NBCS |
| ADV015 | Adult bovine serum | Growth 5%; maintenance none |
| ADV004/017 | Tryptose phosphate broth | C6/36 10% TPB; XTC-2 2% TPB |
| ADV020 | Calf serum for maintenance | Lednicky methods chapter |

### Class E / guidelines (partial)

- WHO/CDC/EU **generic** “virus isolation serum %” search returned little beyond virus-specific SOPs (ANSES, USDA, ATCC, CDC measles still often 10→2). Divergence is clearest in **veterinary FMDV**, **influenza**, and **shell-vial CMV/HSV** practice.

---

## Top 10 most useful counterexamples (pre→post)

These most clearly refute “everyone does 10→2”:

1. **ADV007 — ANSES FMDV SOP — post = 0% FBS** (lactalbumin / Ab media; official isolation).  
2. **ADV011 — USDA VIRPRO1013 — maintenance 5–20% FBS** (growth ~5–10%).  
3. **ADV001 — FMDV BHK — 10% → 5%** during infection (PMC OA).  
4. **ADV003 — HSV diagnostic — 10% → 5%** maintenance (shell vials/tubes).  
5. **ADV005 — YFV Vero — 10% → 1%** (EID OA appendix).  
6. **ADV006 — WNV — 5% → 5%** (same both stages).  
7. **ADV008 — Influenza H3N2 clinical — 10% → 0% + trypsin**.  
8. **ADV004 — ZIKV C6/36 — 10% → 5%** (+ TPB in growth).  
9. **ADV015 — Bovine enterovirus — 5% bovine serum → 0%**.  
10. **ADV014 — Ophthalmic HEI — 15% NBCS → 2% NBCS** (nonclassic pre % + non-FBS).

Honorable: ADV009 ATCC influenza **no FBS**; ADV010 serum-free diagnostic isolation narrative; ADV019 Opti-MEM **3%** SARS-CoV-2 culture.

---

## Coverage limits (honest)

- Horse / lamb serum as **explicit 2% horse maintenance** for primary isolation was hard to pin with open full-text numbers in this pass (many hits were transport media, cardiomyocyte culture, or calf not horse). Class D leans toward **NBCS / adult bovine / TPB**.  
- Some strong leads remain abstract-only (ADV003, ADV012–015, ADV016): quotes are from abstracts/search snippets; full Methods PDFs not ingested.  
- Propagation / vaccine / master-seed protocols (ADV001/002/011/018) are included where serum numbers are explicit; flag in CSV `notes` when not clinical primary isolation.  
- Did **not** re-export known R1 nonclassic IDs (VI59 10→5 BVDV, VI216 SARS 10→5, VI219 PEDV 10→0, VI29 rabies 10→10, etc.); they already support the same thesis inside R1.

---

## Files written

- `.../expansion/adversarial_search_nonclassic_fbs_2026-09-18.md` (this file)  
- `.../expansion/adversarial_candidates.csv` (ADV001–ADV020; merge-ready columns)

No git commit. No paywalled PDF bulk download.
