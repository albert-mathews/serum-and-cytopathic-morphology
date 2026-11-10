# Mizuta 2008 vs 2019 — comparison (VI262 vs VI254)

## The owner's question

"the 2008 paper seems like virus isolation from clinical samples, done over several years, tuning the culture process. this is not an institution telling labs what to do. the 2019 doc is very long. is it content different from the 2008 paper?"

**Answer: Yes — the two documents are different in kind, not just in length.**

| | **VI262 (Mizuta 2008)** | **VI254 (Mizuta 2019)** |
|---|---|---|
| Title | "Analysis of Monthly Isolation of Respiratory Viruses from Children … a Two-Year Study from 2004 to 2005" | "Longitudinal epidemiology of viral infectious diseases combining virus isolation, antigenic analysis and phylogenetic analysis as well as seroepidemiology in Yamagata, Japan between 1999 and 2018" |
| Type | **Primary surveillance report** of one 2-year window (2004–2005) | **20-year retrospective review / overview** of the lab's activities (1999–2018) |
| Scope | 4,107 specimens → 1,551 isolates (2 years) | Decades of longitudinal data, methods evolution, and "principles" narrative |
| Role | The *data paper* for one period | The *synthesis/overview* paper, incl. the SOP table |
| Length | 6 pages | 58 pages (advance-publication preprint, bilingual) |
| Contains SOP Table 1 (GM→MM recipes)? | ✅ (Table 1: 6 cell lines) | ✅ (Table 1: 6 microplate lines **+** additional lines LLC-MK2-N, RD-A, RD-18S-N) |

## What the 2019 paper is, concretely

The 2019 document is a **lab-overview / methods-and-results retrospective**, structured as:

1. **"Principles of YPIPH"** — a narrative arguing *why* the Yamagata Prefectural Institute of Public Health continues virus-isolation-based epidemiology ("we need longitudinal epidemiological studies over several decades and even centuries…").
2. **The microplate method SOP** (§3.1) — *"Routine virus isolation … The composition of the growth medium (GM) and maintenance medium (MM) are shown in Table 1."* This is where the 8 recipe rows in the corpus CSV came from.
3. **Longitudinal epidemiology** — emerging/re-emerging viruses observed across 1999–2018 (echovirus 13, EV-D68, parechovirus-A3, Saffold virus), plus longitudinal studies (EV-A71, CV-A16), and the "PeV-A3-associated myalgia/myositis" disease concept.
4. **Specimen/isolate stocking systems** and **collaborations** across Japan.

It **subsumes but is not identical to** the 2008 paper: the 2008 two-year report is cited inside the 2019 overview (as "we previously presented an outline of this system and the results of virus isolation between 2004 and 2005").

## Table 1 recipe drift: 2008 → 2019 (the "tuning" you noted)

The growth→maintenance recipes **changed** between the two papers — this is the "tuning the culture process" observation, now quantified:

| Cell line | 2008 growth → maintenance | 2019 growth → maintenance | Change |
|---|---|---|---|
| HEF | 10% FBS → 2% FBS | **15%** FBS → 2% FBS | ⬆ growth 10→15% |
| HEp-2 | 5% CS + 1.7% glucose → 2% FBS | **2% FBS + 1.7% glucose → 2% FBS + 1.7% glucose** | growth redefined; equal-hold 2→2 |
| Vero E6 | 10% FBS → 2% FBS | 10% FBS → trypsin (1 µg/ml) + vitamin | MM went **serum-free/trypsin** |
| MDCK | 5% FBS+5% CS → 2% FBS + trypsin 2 µg/ml | 8% FBS → trypsin 2 µg/ml | growth redefined |
| RD-18S | 8% FBS → 2% FBS | 8% FBS → 2% FBS | unchanged |
| GMK | 5% FBS + 5% CS → 2% FBS (+trypsin 3.5) | 10% FBS → 2% FBS | growth redefined |
| **LLC-MK2-N** | — (added 2008, not in 2008 table) | 10% FBS → 2% FBS (no trypsin, PeV) / trypsin 10 µg/ml (PIV) | new line |
| **RD-A** | — | 10% FBS → **5% FBS** | new line |
| **RD-18S-N** | — | 10% FBS → 2% FBS | new line |

**Implication:** the institutional *practice* (the microplate SOP) was actively revised over a decade — growth %s were re-tuned, Vero E6/MDCK maintenance went serum-free-with-trypsin, and three new lines (LLC-MK2-N, RD-A, RD-18S-N) were added. This is a lab iterating its own recipe, not a fixed external mandate. It also means the 2008 paper's recipe is **not** the same object as the 2019 paper's recipe, so they are correctly kept as **separate instances** in the corpus.

## Category recommendation

- **VI262 (2008): keep in VI (category 1).** It is a genuine multi-year (2-year) primary isolation report of clinical specimens — you are right that it is *not* an institution dictating practice; it's a lab reporting what it actually isolated.
- **VI254 (2019): move to category 3 (methods-review/synthesis).** It is a retrospective overview that *describes* the lab's methods (including the SOP table) and summarizes decades of findings, rather than reporting a new primary isolation effort in itself. Its SOP table is methodological/institutional in character.

If you agree, VI254's 8 recipe rows would move with the paper (they are all instances of the *same* 2019 SOP table), leaving VI254 out of the primary-isolation count.