# R1 FBS parsing discrepancies — cleanup list for the R1 agent

**Source of truth:** `isolation-refs.csv` (canonical, 189 rows) and the plotting script
`plot_fbs_distributions.py` (`parse_fbs()`). Audited 2026-11-06 by the R2 agent; flagged for R1
because the R2 agent's cross-check of R2's overview against this CSV surfaced an FBS-count drift.

## Headline symptom

Three "dual-FBS" counts disagree, and they are not mistakes in R2:

| Count | Meaning | Value |
|-------|---------|-------|
| `fbs_coded=yes` | hand flag in `isolation-refs.csv` ("a value present in both serum columns") | **166** |
| plotter n | `plot_fbs_distributions.py` (`parse_fbs()` both cells → number ≤ 20) | **169** |
| archived dual list | `archive/expansion_2026-09-18/isolation-refs-dual-fbs_only.csv` | **170** (stale) |

- **166 → 169** gap = 3 rows the parser *fabricated* a % for (`set` difference below).
- **170 → 166** gap = the archived list still contains 4 IDs since re-flagged `fbs_coded=no`
  (VI33, VI34, VI227, VI232). The archive list was the input to R2's rescore passes; supersede it.

The flag is internally consistent: **no** `fbs_coded=yes` row has an empty cell, and **no**
`fbs_coded=no` row has two bare-numeric cells. The drift is in the *parser*, not in R2.

---

## Category 1 — False-positive parses (parser invents a % the paper never stated)

These 3 rows are the entire 166↔169 gap. The paper did **not** state a numeric post/pre FBS, yet
`parse_fbs()` reduced a parenthetical/date token to a number.

| ID | cell | raw text | parsed | why wrong |
|----|------|----------|--------|-----------|
| **VI33** | post | `not explicitly reduced (fresh DMEM added post-wash; typical maintenance 2%)` | `2.0` | "2" taken from the *"typical maintenance 2%"* gloss; the paper itself left post-FBS unstated |
| **VI34** | post | `not explicitly detailed (maintenance implied post-1 h adsorption)` | `1.0` | "1" taken from *"post-1 h"* (the adsorption **hours**, not a %) |
| **VI232** | pre | `(BHK companion 10% DMEM)` | `10.0` | "10" taken from a **companion cell line's** growth medium, not the test line's pre-FBS |

**Fix (recommended):** these cells should stay `fbs_coded=no` **and** be excluded from the plotter.
That removes the false "2% / 1% / 10%" points and makes plotter n = 166 (== flag n).

Root cause: `parse_fbs()`'s final fallback `NUM_RE.findall(s)[0]` grabs the *first* digit cluster
≤ 30 regardless of what it denotes, once `TYPICALLY_RE` and `RANGE_RE` fail. It has no guard for
"not explicitly stated / implied / companion / post-Xh" phrasing.

---

## Category 2 — Range → midpoint fabrication

`parse_fbs()` collapses `a–b` to `(a+b)/2`, so the plotted number is one the paper never wrote.
`fbs_coded=yes` is correct for these (a value is present); the *plot* is what's synthetic.

| ID | cell | raw | parsed |
|----|------|-----|--------|
| VI13 | pre | `5-10` | `7.5` |
| VI25 | post | `2-10` | `6.0` |
| VI230 | pre | `5-10` | `7.5` |
| VI230 | post | `1-2` | `1.5` |
| VI30 | pre | `0-2 (often serum-free + TPCK-trypsin)` | `1.0` |

Notes:
- `2-10 → 6.0` (VI25) is meaningless as a "typical maintenance" value.
- VI30's `0-2 (often serum-free …)` is midpoint-ed to `1.0` but the text also says **"often serum-free"**
  (0%); `TYPICALLY_RE` only matches the literal word "typically", not "often".

**Fix (decision needed):** pick a policy and apply it uniformly to all ranges:
(a) exclude range rows from the numeric distribution plots (report them in a "range" bucket), or
(b) plot each endpoint (adds rows), or
(c) keep midpoint but tag a `value_is_midpoint` flag and state the rule in Methods.
Also extend the "typically" rule to "often / usual(ly) / maintained in" phrasing.

---

## Category 3 — Multi-cell-line collapse (first value kept, the rest dropped)

Rows that state serums for **more than one cell line** on the same comma/space: `parse_fbs()`
keeps only the first number and silently drops the others, so the plotted pair is *one* line's pair
presented as if it were the paper's single recipe.

| ID | cell | raw | parsed | dropped |
|----|------|-----|--------|---------|
| VI220 | pre | `5 (Vero); 10 (C6/36)` | `5.0` | C6/36 = 10 |
| VI220 | post | `1 (Vero); 2 (C6/36)` | `1.0` | C6/36 = 2 |
| VI217 | post | `2 (ST); 0 (Vero76/MDBK)` | `2.0` | Vero76/MDBK = 0 |

**Fix (decision needed):** either split into one row per cell line, or exclude mixed-line rows from
the numeric distribution and report their pairings verbatim.

---

## Category 4 — "typical / implied" editorialized cells (benign but confirm)

These parse to the leading digit and are probably fine, but the gloss signals the number is a
practice default rather than a paper-specific measured value. Confirm nothing is being inflated.

| ID | cell | raw | parsed |
|----|------|-----|--------|
| VI36 | post | `2 (typical post-inoculation maintenance)` | `2.0` |
| VI38 | post | `0 (FBS-free + trypsin)` | `0.0` |

---

## Category 5 — Correct exclusions (not errors; list for completeness)

| ID | cell | raw | parse |
|----|------|-----|-------|
| VI227 | pre | `(ref. Cardoso 2000)` | None (year stripped) |
| VI233 | pre | `(not separately stated)` | None |
| VI30 | post | *(empty)* | None |

These are correctly `fbs_coded=no`. The `(ref. …)` stripper works; `(not separately stated)` /
`(BHK companion …)` are **not** covered by the parser's parenthetical handling, which is precisely
why VI232 slips through in Category 1.

---

## Category 6 — Script fragility (latent; no current break)

1. `plot_fbs_distributions.py` lines 70-82 hardcode `post_c = "FBS% post-inculcation"` (a historical
   **typo** comment) and then fall back to substring column detection. It currently lands on
   `FBS_post_inoculation` correctly, but relies on that fallback. Remove the stale typo candidate.
2. Hard fence `load_papers` line 88: `(df["pre"] <= 20) & (df["post"] <= 20)` silently drops any
   row with a serum > 20%, while `parse_fbs()` accepts 0–30. No current row exceeds 20%, but the
   two bounds disagree; reconcile to one rule.
3. `parse_fbs()` accepts `0–30` but the flag/plotter fence uses `≤ 20`; and the "year stripper"
   `\b(19|20)\d{2}\b` will delete a cell that *legitimately* reads e.g. "19" or "20" (unlikely for
   FBS, worth a comment).

---

## What R2 needs from this cleanup (non-blocking)

None of the above changes R2's scored tiers — those are read from paper text, not FBS cells. R2's
only dependency is the **denominator** sentence ("we scored N Isolation papers"). Once R1 settles
the flag↔plotter reconciliation, R2 should cite whichever of **173** (all scored) / **166** (dual
flag) is chosen as the paper's canonical frame. See `r2_negative_controls/r2.md` status note
("Dual-FBS-scoped tier distribution").