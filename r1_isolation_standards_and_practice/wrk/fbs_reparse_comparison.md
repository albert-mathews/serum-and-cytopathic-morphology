# R1 FBS re-parse — comparison & decisions (audit response)

**Trigger:** `wrk/fbs_parsing_discrepancies.md` (R2 audit, 2026-11-06).
**Method:** for each flagged row, re-pulled full text (local PDF via pymupdf, or Europe PMC / NCBI
full text) and extracted verbatim serum sentences. Every below claim is quote-backed; raw dumps
in `%TEMP%\opencode\r1_reparse\` (not tracked).

**Scope honesty:** items with a local PDF were verified against the PDF. Items without a local
PDF (VI217, VI220, VI230, VI232, VI233, VI227) were verified against the open-access full text
where available, else against the archived `quote_*` fields recorded by the original extraction.
Per-item provenance is stated.

**Canonical file compared against:** `isolation-refs.csv` (189 rows).

---

## Per-item findings

### Category 1 (audit claimed the parser *invented* a % the paper never stated)

| ID | Audit claim | Verbatim evidence | Verdict |
|----|-------------|-------------------|---------|
| VI33 | parser pulled "2" from `typical maintenance 2%` gloss; paper leaves post-FBS unstated | "The inoculum was removed, cells were gently washed three times **with DMEM, and a fresh medium was added**" (no %). Pre verified: "**10% heat-inactivated FBS**". | **AUDIT CORRECT.** post genuinely unstated → `fbs_coded=no`, no post value. |
| VI34 | parser pulled "1" from `post-1 h` (hours); paper leaves post-FBS unstated | "After removing the fecal samples, **1 mL DMEM containing 5% FBS** was added to each well." | **AUDIT WRONG — INVERTED.** The paper DOES state post = **5% FBS**. The original CSV *under-captured* (recorded "not explicitly detailed"). Fix: post = **5**, `fbs_coded=yes`. This is the opposite of the audit's premise. |
| VI232 | parser pulled "10" from `(BHK companion 10% DMEM)` companion line, wrong cell | qpre: "A reporting **BHK** cell line … maintained in DMEM with 10% FBS"; qpost: "**Vero** cells … 2% FBS". | **AUDIT CORRECT in spirit.** pre belongs to a *companion* BHK line, not the test cell. But post=2 (Vero) is stated. Fix: pre = unstated (companion), post = 2. |

### Category 2 (range → midpoint fabrication)

| ID | cell | raw | parsed (midpoint) | Verbatim | Verdict |
|----|------|-----|-------------------|----------|---------|
| VI13 | pre | `5-10` | 7.5 | "heat-inactivated fetal bovine serum **(5% or 10%)**" | **Either/or, not a range.** Not a true 5–10 step; midpoint 7.5 is synthetic. |
| VI25 | post | `2-10` | 6.0 | both "**10%** HI-FBS" (growth/dilution) and "**2%** … HI-FBS" (overlay) appear in *different steps* | **Heterogeneous, not one range.** Midpoint 6.0 meaningless. |
| VI230 | pre | `5-10` | 7.5 | "5-10% fetal calf serum (FCS)" (OCR of a range) | True range; midpoint synthetic. |
| VI230 | post | `1-2` | 1.5 | "similar medium with **1-2% FCS**… remove the serum" | True range; midpoint synthetic. |
| VI30 | pre | `0-2 (often serum-free…)` | 1.0 | "…supplemented with Fetal Bovine Serum (FBS)… + **TPCK-treated trypsin**" (influenza; often serum-free + trypsin) | The "0-2" was an editorial guess; paper uses FBS-then-trypsin, no single pre-% quoted as 0–2. Needs the growth-% sentence. |

### Category 3 (multi-cell-line collapse)

| ID | cell | raw | Verbatim | Verdict |
|----|------|-----|----------|---------|
| VI220 | pre | `5 (Vero); 10 (C6/36)` | qpre "Vero … **5%** heated FBS" (C6/36 10% in same sentence) | Two lines collapsed; keeping first drops C6/36=10. |
| VI220 | post | `1 (Vero); 2 (C6/36)` | qpost "less FBS: **1%, Vero; 2%, C6/36**" | Same. |
| VI217 | post | `2 (ST); 0 (Vero76/MDBK)` | qpost "lowered to **2% for ST** and **0% for Vero76/MDBK**" | Collapsed to 2, drops 0. |

### Category 4 (typical/implied gloss — verify not inflated)

| ID | cell | raw | Verbatim | Verdict |
|----|------|-----|----------|---------|
| VI36 | post | `2 (typical post-inoculation maintenance)` | "**500 µL of DMEM containing 2% FBS and 1.5% carboxymethylcellulose**" (plaque overlay) | 2% is verbatim BUT it is a **plaque overlay**, not "maintenance". The gloss word "maintenance" is imprecise; the number is right. |
| VI38 | post | `0 (FBS-free + trypsin)` | "**then propagated in FBS-free medium with trypsin**" | Verbatim; correct. |

### Category 5 (correct exclusions — confirm)

All three (VI227 pre `(ref. Cardoso 2000)`, VI233 pre `(not separately stated)`, VI30 post empty) are
correctly `fbs_coded=no`. Confirmed — VI227 pre genuinely defers to Cardoso 2000; VI233 pre is
"not separately quantified"; VI30 post is genuinely empty (paper uses trypsin maintenance, no FBS% post).

---

## Policy decisions (ADOPTED as strict defaults; PLEASE SIGN OFF)

1. **False positives (Cat 1):** a cell is only counted if the *paper* states a numeric serum % for
   the *test cell at that step*. "not stated / implied / companion / post-Xh" → blank. → VI33 post blank,
   VI34 post=5 (fix), VI232 pre blank.
2. **Ranges (Cat 2):** DO NOT midpoint. Represent verbatim (e.g. `5-10`, `2-10`, `5 or 10`). Plotter
   should *exclude* range cells from the numeric KDE and report them in a separate "range" bucket.
3. **Multi-line (Cat 3):** DO NOT collapse. Split into one row per cell line (with a `_cline` suffix
   on the ID), so each line's true pair is preserved. (Alternatively keep one row and record both
   verbatim in notes + exclude from numeric plot — I implemented SPLIT.)
4. **Parser fence:** reconcile `parse_fbs` (0–30) and `load_papers` fence (≤20) to one bound. Adopted
   **≤ 20** as the plausible-culture-serum ceiling for *plotted* values.

---

## Items flagged for ALBERT human review

The following need your read before the second CSV is treated as final (you said you've read up to
~VI30–40; these are at/just past that boundary or are judgment calls):

1. **VI34** — I claim the paper states post = 5% FBS ("1 mL DMEM containing 5% FBS"). This *changes*
   a `fbs_coded=no`→`yes` and inverts the audit. Please confirm the sentence is at the *isolation*
   step (not the VN/neutralization step).
2. **VI36** — number (2%) is verbatim but it's a **plaque overlay**, not "maintenance". Decide whether
   the corpus means "any post-inoculation serum" (keep) or "maintenance-liquid only" (the overlay
   still counts). I kept it as post=2.
3. **VI30** — the pre cell `0-2 (often serum-free…)` was editorial, not a quoted %; the paper's real
   growth serum sentence needs pinning (influenza often grows with serum then trypsin maintenance).
   I left pre as-is (needs your read of the growth Methods).
4. **VI13** — "5% or 10%" is an either/or, not a range. I recorded it verbatim and excluded from
   numeric plot. Confirm you're OK treating it as "range/either-or" not "10".
5. **VI220 / VI217** — multi-line split is mechanical; confirm you're happy with one-row-per-line IDs.