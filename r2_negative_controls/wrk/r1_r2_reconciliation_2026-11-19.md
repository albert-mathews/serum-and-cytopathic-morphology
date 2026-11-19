# R1 ↔ R2 concordance — reconciliation report (2026-11-19)

**Rule being enforced:** R2 follows R1. R1's `isolation-refs.csv` is the reviewed single source of truth for the
category-1 (Isolation-practice) corpus; R2 does **not** maintain a parallel corpus. Any disagreement between an R2
row and current R1 is corrected on the R2 side, justified by quotes from (a) R1 records, (b) R2 records, and (c) the
source PDFs.

---

## 1. What R1's reviewed records say (the source of truth)

### 1.1 `isolation-refs.csv` (category-1) — current schema

R1's `r1.md` states the category-1 CSV is "184 rows — single source of truth", one row per report, with a
three-way `fbs_coded` flag and an endpoint axis (`class`). Quoted:

> "`isolation-refs.csv` — **Category-1 corpus (184 rows — single source of truth).** One row per report for
> growth+maintenance FBS% (`fbs_coded` = yes / post_only / no), quote-backed, plus **`endpoint_*` columns and
> `class`** (1 = CPE detection/Isolate endpoint, 4 = 2I1D pattern with other endpoint). Category-2 (protocols) and
> category-3 (methods-review) refs live in their own folders + CSVs." *(r1.md, entrypoints table)*

And the class axis:

> "| **1** | **CPE read as virus detection and/or Isolate** (CPE = 'we found / Isolated the virus'). … |
>  | **4** | **2I1D serum pattern present, but a different primary endpoint** (titration/TCID₅₀, antigen detection,
>  neutralization, plaque, hemagglutination/hemadsorption, molecular, purification, characterization)." *(r1.md, §Corpus
> organization Axis 2)*

And the category axis (folder = category):

> "| `refs/isolation_practice/` | **category 1** | A publication **reporting what was done in practice** (a primary
> virus-culture/Isolation paper) … |
>  | `refs/isolation_protocols/` | **category 2** | A **protocol / SOP / institutional guideline** … |
>  | `refs/methods_review_teaching/` | **category 3** | A **methods-review / teaching chapter / thesis** …
>  describes how to culture, or reviews method, without being a field practice report. |
>  … A reference moved out of `isolation_practice` has its `VI###` prefix stripped and gets the folder's own ID prefix,
>  and its row moves to that folder's CSV." *(r1.md, §Corpus organization Axis 1)*

### 1.2 The R1 category moves that R2 was missing (r1.md TODO #8, COMPLETE 2026-11-10)

> "**Category/folder moves — COMPLETE (2026-11-10).** VI254 (Mizuta 2019) + VI270 (thesis) →
> `refs/methods_review_teaching/` (as MR001/MR002); VI237 (WNV protocol) → `refs/isolation_protocols/` (as PR001).
> VI107 and VI74 stay category 1. VI74 re-coded class 1 (multi-endpoint)." *(r1.md TODO #8)*

### 1.3 The moved rows, as recorded in the destination CSVs

- **`methods-review-refs.csv` (MR###):**
  - `MR001` — notes: "[moved cat3 2026-11-10; ex-VI254] Mizuta et al. JJID 2019 … microplate routine isolation SOP
    Table 1." (8 sub-rows A–H: HEF, HEp-2, MDCK, GMK, LLC-MK2-N ×2, RD-A, RD-18S-N).
  - `MR002` — notes: "[cat3; thesis] [moved cat3 2026-11-10; ex-VI270] French IFREMER DEA methods."
  - `MR003` — notes: "[cat3; ex-VI245] Lednicky & Wyatt methods/teaching chapter."
- **`isolation-protocol-refs.csv` (PR###):**
  - `PR001` — notes: "[moved cat2 2026-11-10; ex-VI237] … protocols.io clinical isolation SOP."
  - `PR010` — link: `https://www.cdc.gov/measles/lab-tools/vero-slam.html`; notes: "[protocol] CDC Measles Lab Tools —
    Vero/hSLAM virus isolation." *(identical URL to R2 row VI271's fetched identifier)*.

### 1.4 Re-IDs R1 applied to legacy R2 IDs

- `VI303` carries note "[ex-SPT10]" (ZIKV single-particle imaging). → R2's `SPT10` row is R1 `VI303`.
- McSwiggan 1981 is one R1 paper `VI240`. Because R1 codes **multiple pre→post serum recipes as multiple rows
  of the same paper** (a coding rule, not an error), `VI240` appears on several recipe rows. R2's three legacy
  rows `VI240/VI241/VI242` are that one paper; only `VI240` is retained as the R2 paper key.

> **R1 coding rule (owner, quoted):** "isolation-refs.csv has multiple rows per paper per its coding rules.
> if a paper shows more than one serum pre→post recipe, this is captured in multiple rows."
> *(Albert, 2026-11-19)* — this explains the multiple `VI240`/`VI262` rows; they are recipe rows, not duplicates.

---

## 2. What R2's records said (the stale snapshot)

R2's `control-cultures-overview.csv` (173 rows) was built against an **older flat R1 snapshot** (before the
category/class re-organization). Concretely, R2's overview rows include IDs that current R1 has **moved out of
category-1** or **dropped**, and omit category-1 IDs R1 added later.

R2's own status text acknowledged part of the drift but framed it backwards:

> "…a pre-existing R1/R2 corpus-sync gap … **This gap is R1's to reconcile**; R2's headline numbers use the full
> 173-row overview…" *(r2.md, 2026-11-18 status — superseded)*

That framing is wrong: the gap is **R2's** to fix. Corrected in r2.md (see §4 below).

---

## 3. The full disposition table (R2 row → current R1)

| R2 overview ID | Current R1 disposition | Evidence |
|----------------|------------------------|----------|
| VI237 | **cat2** → `PR001` | `isolation-protocol-refs.csv` PR001 note "[moved cat2 … ex-VI237]" |
| VI254–VI261 (8 rows) | **cat3** → `MR001` A–H | `methods-review-refs.csv` MR001 notes "[moved cat3 … ex-VI254]" |
| VI263 | **merge** → `VI262` | same Mizuta JJID 2008 paper (doi 10.7883/yoken.JJID.2008.196), a second cell-line arm of the one R1 paper |
| VI245 | **cat3** → `MR003` | `methods-review-refs.csv` MR003 note "[cat3; ex-VI245]" |
| VI270 | **cat3** → `MR002` | `methods-review-refs.csv` MR002 note "[cat3; thesis] … ex-VI270" |
| VI271 | **cat2** → `PR010` | `isolation-protocol-refs.csv` PR010 link `…/vero-slam.html` = R2 VI271's identifier |
| VI241, VI242 | **merge** → `VI240` | R1 `VI240` = one McSwiggan 1981 paper (multiple serum-recipe rows) |
| SPT10 | **rename** → `VI303` | R1 `VI303` note "[ex-SPT10]" |
| VI4 | **dropped** | HFRS 1983 absent from current `isolation-refs.csv` |
| VI24 | **dropped** | AmB influenza paper absent from current `isolation-refs.csv` |

**Net:** of 173 R2 rows, **17 rows leave the scoring universe** (12 category-out + 2 dropped + 3 merged-away),
and **1 row renames** (SPT10→VI303). **In-universe scored = 156.**

## 4. What R2 still owed R1 (now closed)

R1 category-1 = 181 unique papers. R2 had scored 156; the remaining 25 were scored 2026-11-19
(`wrk/score_pending_25.py`, justification notes §Pass5), closing the gap at **181 / 181**:

- **class 1 (CPE/Isolate)** — VI98, VI100, VI102, VI104, VI106, VI107, VI113, VI116, VI117, VI120 (n=10)
- **class 4 (2I1D, other endpoint)** — VI97, VI101, VI103, VI108, VI114, VI119, VI294, VI295, VI296, VI297, VI298,
  VI299, VI300, VI301, VI302 (n=15)

Final tier distribution over the full 181-paper universe: **A / B / C / D = 14 / 44 / 20 / 103**
(Tier D = 56.9%).

---

## 5. Actions taken (see commits/edits of 2026-11-19)

1. Added `r1_status`, `r1_current_id`, `r2_universe` columns to `control-cultures-overview.csv` (builder script
   `wrk/r1_r2_align.py`), so every R2 row carries its current-R1 disposition and only `r2_universe=yes` rows feed
   the tier statistics.
2. `wrk/viz/make_figures.py` filters to `r2_universe=yes`.
3. r2.md: concordance rule + corrected frame written; stale "166 dual / 7 extras / R1-to-reconcile" text removed;
   snippet numbers S3/S4 restated on the full 181-paper universe.
4. `control-cultures.md`: added §"R2 universe = R1 category-1 (concordance rule)".
5. `CLAIMS.md` OB023 + `tex/sections/results.tex`: counts corrected to the R1-category-1 frame (181 papers).
6. Scored the 25 missing category-1 papers (`wrk/score_pending_25.py`; justification notes §Pass5); universe
   closed at 181/181.

*End of reconciliation report.*
