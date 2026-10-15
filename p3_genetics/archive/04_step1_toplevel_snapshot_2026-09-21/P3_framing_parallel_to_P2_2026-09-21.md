# P3 framing — parallel to P2 (hypothesis → predict X → find X)

**Date:** 2026-09-21 (revised same day)  
**Status:** Working framing for Step 1 / paper. Exploration, not advocacy.  
**Related:** `P3_prior_art_genome_provenance_critiques_2026-09-21.md`, `P3_step1_protocol.md`, `../p3.md`

## Main spine (locked)

1. **Culture + CPE is not virus-specific** (core paper: FBS/inoculum confound; P2 physical overlap).
2. Therefore any genetics that **samples material produced by culture±CPE “isolation”** inherits that non-specificity.
3. **If most origin/type genome deposits — the foundation of viral genetics — come from culture±CPE (or closely related culture-propagated) samples, that is a major concern:** the reference graph is built on the same non-specific detector the paper criticizes.

This is the P3 concern. Prior art (thin INSDC metadata, MIUViG isolate-vs-UViG, flu passage) makes the question legitimate; Step 1 is the empirical census.

## Predict-X form (same mold as P2)

| | **P2 (physical)** | **P3 (genetic)** |
|--|-------------------|------------------|
| Hypothesis | Culture±CPE does not isolate a distinct physical virus class | Culture±CPE is not virus-specific; genetics built by sampling those culture products inherits the flaw |
| Predict **X** | Dual / overlapping characterizations (virus vs EV, etc.) | Origin/type genomes predominantly document **culture±CPE** (and related culture-propagated) sample-production paths — not an independent warrant that escapes that practice |
| Look | Morphology / composition; raters | Paper-first method↔deposit census (Step 1) |
| Find **X** | Overlap / dual labels | Closed-set path_score dominated by `culture_cpe` (+ `culture_no_cpe` as culture-without-CPE-warrant); `clinical_direct` / `other` as contrast cases |

**One-line thesis:** *Culture+CPE is not virus-specific; if the foundation of viral genetics is genomes from culture±CPE samples, that is a major concern — and Step 1 counts how often origin deposits document exactly those paths.*

## Scoring note for the spine

- Primary concern path: **`culture_cpe`**.
- **`culture_no_cpe`**: still culture-propagated stock; supports “genetics from culture products,” weaker on the CPE-specific half of the spine — report separately, do not hide inside CPE.
- **`clinical_direct`**: contrast path (contig/taxonomy warrant, not culture±CPE) — important for honesty, not the main “foundation = culture+CPE” claim unless the fraction is small.
- Open/unclear remain visible; never force closes.

## What this does *not* require

- P2-style “same object, two class names” in sequence space (optional secondary finding).
- Conspiracy; only non-specific culture detector + sequence-as-identity + databases that store labels.

## Paper use

1. Lead Discussion/Results for P3 with the spine above.  
2. Cite prior-art map for legitimacy.  
3. Report Step 1 fractions with `culture_cpe` highlighted; break out `culture_no_cpe` and `clinical_direct`.  
4. Tie back: genetics does not independently ground a virus class if type material is culture±CPE product.
