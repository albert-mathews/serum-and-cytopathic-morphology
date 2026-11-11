# R1 corpus — research method codification: "instance" = the atomic unit (2026-11, revised)

**Status: IMPLEMENTED** in `isolation-refs.csv` (single source of truth, 2026-11-10 consolidation). The prior `isolation-refs_reparse.csv` and `isolation-refs-reparse2.csv` audit layers were merged into `isolation-refs.csv` and archived.

## The research question R1 answers

> Does virology change more than one thing when doing virus Isolation?

- Institutional protocol says **yes**: it prescribes a growth→maintenance serum switch at/near
  inoculation (e.g. ~10% → ~2% FBS) *while also* reading CPE as the viral readout.
- R1's corpus asks: does that dual change actually happen **in practice**, across the
  published record of practicing virologists?

Only after that is established can we ask the *next* question (R2/R3/CRO): does changing two
things at once confound the observable — is the CPE result under-determined, non-specific, or
still valid? R1 does not answer that; R1 supplies the *premise* (the practice-level dual
change is real and widespread).

## The atomic unit: the "instance"

An **instance** = one cell-culture virus-Isolation recipe as it appears in the publication
record. Each instance is an atomic data point and **adds 1 to n unconditionally** — it has no
relation to any other instance for counting purposes.

Counting rules (this is the defensible core):

1. **Two independent researchers using the same recipe** (same cells, same FBS-pre, same
   FBS-post) = **2 instances** → +2 to n. Both are independent evidence of what practicing
   virologists actually do. We never merge by "same recipe."
2. **One paper reporting M distinct recipes** (different cells and/or different FBS pre/post)
   = **M instances** → +M to n. Each distinct recipe is its own data point.
3. **One paper reporting many cultures of the *same* recipe** (e.g. 100 replicate wells all
   grown 10%→2%) = **1 instance** → +1 to n. It tells us this researcher does *that one*
   recipe; the repetition adds no new practice information.

In short: **one row = one (paper, recipe) pair**, where `recipe` letters (A, B, C…) split a
single paper into its distinct recipes. Two papers never merge; one paper's repeated recipe
never splits.

## Schema

- `ID` = paper (the publication's `VIxxx`), repeated across that paper's recipe rows.
- `recipe` = `A`, `B`, `C`, … distinct recipe within the paper (single-recipe paper → `A`).
- Recipe-specific columns (cells, FBS_pre, FBS_post, base_medium, antibiotics, quote_pre,
  quote_post) differ per recipe row; paper-level columns (year, virus, link, DOI, access,
  source_batch) are identical across a paper's rows.

## n — what it means and how we report it

- **Total n = number of rows = number of distinct (paper, recipe) instances.**
- **Dual-FBS n = instances where both FBS pre AND post are stated numerically** (`fbs_coded=yes`).
  These are the instances usable for the "pre→post serum switch" statistic.
- We report: *"we observed **n** Isolation instances across **j** papers, of which **k** state
  a dual (pre+post) serum; among those, the modal pattern is growth≈10% → maintenance≈2%…"*

### `fbs_coded` values (3-way, codified 2026-11-10)

| value | meaning | counts toward dual-FBS? |
|---|---|---|
| `yes` | both pre and post stated numerically (verbatim) | **yes** |
| `post_only` | post stated verbatim; pre **not** stated → pre **assumed = 10%** (ATCC-standard default for the cell line, always 10%) | **no** (pre is an assumption, not a stated value) |
| `no` | neither stated, or pre-only | no |

**Owner rule (2026-11-10):** *any paper that states fbs-post only has its fbs-pre assumed to be
the ATCC recommendation for the cell line, which is always 10%.* This is coded as
`fbs_coded=post_only` with `FBS_pre_inoculation=10` and a `[post_only: pre assumed 10% ATCC]`
note tag. `post_only` rows are **distinct** from `yes` (dual) rows: they are not counted in the
dual-FBS statistic because their pre is an assumption, not a stated value.

### Current numbers (2026-11-10, post-corrections)
- Total instances (rows): **185** across **j = 176** distinct papers (VI24 removed as a
  non-isolation drug-effect paper).
- `fbs_coded=yes` (dual, both stated): **162**.
- `fbs_coded=post_only` (post stated, pre assumed 10%): **5** (VI14, VI15, VI227, VI232, VI233).
- `fbs_coded=no`: **18**.

## Recipe categories we care about (for downstream grouping, not for n)

Roughly, each dual-FBS instance falls into one of:
- **"follows protocol"** — growth→maintenance serum reduction in the ~10→2 direction.
- **"doesn't exactly follow, but directionally same"** — some reduction (e.g. 8→2, 10→5).
- **"doesn't follow, directionally different"** — hold or increase (e.g. 10→10, 5→20).
We do **not** need per-category n in the corpus; this is the *analytic* framing for the
Results sentence, derived from the pre/post pairs.

## Why this is defensible (for a methods-critique reader)

Denominating by **instance** (not paper, not unique-recipe-value) is the only choice that
answers "how prevalent is the dual-serum switch among practicing virologists?" without
double- or under-counting: it counts every published demonstration of practice exactly once,
merges nothing, and splits only when one publication genuinely reports multiple distinct
recipes.