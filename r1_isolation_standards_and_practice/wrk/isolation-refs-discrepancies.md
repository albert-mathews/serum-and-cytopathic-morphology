# R1 isolation-refs — 3-way discrepancies & resolution

**Generated 2026-11-10** by a full PDF re-read of the quote-less early batch (VI2–VI46) + a 3-way diff across:
- `isolation-refs.csv` (canonical, 186 rows)
- `isolation-refs_reparse.csv` (2026-11-06 audit fixes applied, 186 rows)
- `isolation-refs-reparse2.csv` (this pass: quote backfill + PDF-verified corrections, 186 rows)

**Method:** for each of the 20 early rows lacking verbatim quotes, re-extracted the serum sentences from the local PDF full text (pymupdf; VI43 via `tools/ocr_pdf.py` because its PDF is image-scanned). 19 of 20 resolved cleanly; 3 required value corrections; 1 flagged for Albert.

---

## ⭐ OWNER RULINGS — FINAL (2026-11-10)

These supersede the provisional statuses in sections B–C below. **All applied to all three CSVs** (`isolation-refs.csv`, `isolation-refs_reparse.csv`, `isolation-refs-reparse2.csv`).

| Row | Owner ruling | Final state |
|---|---|---|
| **VI14** | I mis-read: fbs-post is 2% (Hep-2 cultured in DMEM + 2% FBS). Pre not stated. | `pre=10 (assumed)`, `post=2`, `fbs_coded=post_only` |
| **VI15** | Inoculum treated in 2% FBS, cells maintained in 2% FBS; growth/passaging FBS never stated. | `pre=10 (assumed)`, `post=2`, `fbs_coded=post_only` |
| **VI18** | Agreed. | `pre=10`, `post=0` (serum-free; 0.2% was BSA not FBS), `fbs_coded=yes` |
| **VI24** | **Removed.** Three recipes (Vero, epithelial/HCE, A549); pre=10% for all; **not virus isolation** (amphotericin-B drug-effect paper). | row deleted from all three CSVs |
| **VI43** | pre=5%, post=2%. | unchanged (already `5→2`, `yes`) |

### New coding rule (owner, 2026-11-10)

> **Any paper that states fbs-post only has its fbs-pre assumed to be the ATCC recommendation for the cell line, which is always 10%.**

Coded as `fbs_coded=post_only`, `FBS_pre_inoculation=10`, and a `[post_only: pre assumed 10% ATCC]` note tag. `post_only` is **distinct** from `yes` (dual-FBS): it is **not** counted in the dual-FBS statistic because pre is an assumption, not a stated value.

Under this rule, the following post-only rows were **auto-coded** to `pre=10, fbs_coded=post_only` (please confirm these three are intended under the same rule):
- **VI227** (IBDV; pre had deferred to "Cardoso 2000" reference)
- **VI232** (WNV; pre belonged to a companion BHK line)
- **VI233** (rhinovirus; pre "not separately stated")

---

## A. Discrepancies already resolved before this pass (csv → reparse, stable in reparse2)

These are the 2026-11-06 audit fixes (see `wrk/fbs_reparse_comparison.md`). They differ between `isolation-refs.csv` and the two reparse CSVs, and are **correct as-is** in reparse2:

| ID | field | csv (old) | reparse / reparse2 (fixed) | Note |
|---|---|---|---|---|
| VI13 | pre | `5-10` | `5 or 10` | either/or, not a range |
| VI227 | pre | `(ref. Cardoso 2000)` | `` | deferral removed; pre blank |
| VI232 | pre | `(BHK companion 10% DMEM)` | `` | companion line, not test cell |
| VI233 | pre | `(not separately stated)` | `` | blank |
| VI25 | post | `2-10` | `2 (overlay); 10 (dilution)` | heterogeneous, split |
| VI30 | pre | `0-2 (often serum-free + TPCK-trypsin)` | `` | editorial gloss removed |
| VI33 | post | `not explicitly reduced …` | `` | post genuinely unstated |
| VI34 | post | `not explicitly detailed …` | `5` | paper states 5% FBS post-feed |
| VI34 | fbs_coded | `no` | `yes` | inverted by the fix |
| VI36 | post | `2 (typical post-inoculation maintenance)` | `2` | number verbatim (plaque overlay) |
| VI38 | post | `0 (FBS-free + trypsin)` | `0` | verbatim, cleaned |

## B. NEW discrepancies this pass (reparse2 ≠ reparse) — from PDF re-read

### B1. VI14 — HRSV, Guizhou (doi:10.1016/j.bjid.2019.10.007)

- **Change:** `FBS_pre_inoculation` `10` → `` (blank); `fbs_coded` `yes` → `no`.
- **Evidence:** the only serum sentence is *"Hep-2 cells (ATCC) cultured in Dulbecco's modified Eagle's medium (DMEM) supplemented with 2% fetal bovine serum."* There is **no separate growth-FBS percentage**; the Hep-2 isolation culture is a single 2% FBS condition.
- **Previously stored `pre=10` was unsupported by the PDF.** A `post=2` remains (verbatim).
- **Status:** resolved (correction applied). `fbs_coded=no` because only one serum value is stated.

### B2. VI15 — DENV-2, New Delhi (PMC6823047)

- **Change:** `FBS_pre_inoculation` `10` → `2`.
- **Evidence:** *"Blood samples were diluted 1:10 in MEM containing 2% FBS … added onto C6/36 cells"*, then *"After 1 hour, the inoculum was removed and cells were cultured for 7 days in MEM with 2% FBS and antibiotics."* Both steps are **2% FBS**; no 10% growth appears.
- **Previously stored `pre=10` was unsupported (likely a template default).** Now `pre=2, post=2` (equal-hold).
- **Status:** resolved (correction applied).

### B3. VI18 — influenza (Vero-adapted vaccine donor; PubMed 25448099)

- **Change:** `FBS_post_inoculation` `0.2` → `0`.
- **Evidence:** pre is *"cells maintained in DMEM supplemented with 10% FBS."* Post is *"The Vero cell culture medium was changed to DMEM containing 0.2% bovine serum albumin (BSA) with 1 μg/ml TPCK-trypsin."* — i.e., the **0.2% is bovine serum albumin, NOT FBS**; the virus-passage medium is **serum-free + trypsin**.
- **Previously stored `post=0.2` mislabeled BSA as FBS.** Now `post=0` (serum-free), with the BSA/trypsin detail in notes.
- **Status:** resolved (correction applied).

---

## C. Flagged for ALBERT (not changed — needs your read)

### C1. VI24 — "Amphotericin B Promotes Influenza Virus Replication in Cell Culture" (PMC3194987)

- **Current record:** `FBS_pre=0`, `FBS_post=0`, `base_medium = OptiPRO SFM (serum-free) or EMEM`, `fbs_coded=yes`.
- **What the PDF shows:** the *cells* (MDCK, Vero, etc.) are **grown in 10% FBS**; the *influenza virus cultivation* is done **serum-free** (OptiPRO SFM + trypsin).
- **The question:** does "pre" mean the *cell-growth* serum (10%) or the *virus-cultivation* serum (0%)? The corpus convention for other papers treats "pre" as the **growth-medium serum**, which here would be **10%**, contradict the stored `0`. But this paper is not a classic clinical isolation — it measures how amphotericin B alters influenza yields in serum-free culture.
- **Decision wanted:** (a) keep `0→0` (serum-free virus-cultivation framed as the "isolation" step), or (b) re-code as `pre=10` (cell growth) `post=0` (serum-free virus step), or (c) mark `fbs_coded=no` / exclude as a non-standard (drug-effect) paper.
- Quote added to reparse2 (both pre and post) so you can judge from the verbatim text.

### C2. VI43 — VERIFY the OCR quote before reuse

- VI43's PDF is image-scanned; its pre/post (`5→2`) were **confirmed correct** via OCR, and quotes were added from OCR output. Rule: machine OCR is a reading aid — **confirm the `5%`/`2%` sentences against the original page** before citing them in the paper. (No value change; just a verification note.)

---

## D. Quote-coverage improvement (this pass)

| | csv | reparse | reparse2 |
|---|---|---|---|
| quote_pre populated | 143 | 150 | **169** |
| quote_post populated | 152 | 159 | **179** |
| rows | 186 | 186 | 186 |

The 20 early rows (VI2, VI8, VI14–16, VI18, SPT10, VI23–24, VI28–29, VI32, VI39–46) now carry verbatim quotes.

## E. Summary of net corpus changes introduced by reparse2

| Row | Field | Old | New |
|---|---|---|---|
| VI14 | pre / fbs_coded | 10 / yes | (blank) / no |
| VI15 | pre | 10 | 2 |
| VI18 | post | 0.2 | 0 |

No row-count change (186 rows throughout).

---

## Resolution status (FINAL, post-owner-ruling)

- **VI14, VI15, VI18, VI24, VI43**: settled per owner ruling (see top section). Applied to all three CSVs.
- **Audit fixes promoted to canonical** (VI13, VI25, VI30, VI33, VI34, VI36, VI38): the 2026-11-06 verified fixes were carried from reparse → `isolation-refs.csv`, so all three CSVs now agree on FBS values and `fbs_coded`.
- **VI227, VI232, VI233**: auto-coded `post_only` per the new rule — **awaiting owner confirmation** that the ATCC-10% assumption applies to these three too (they each had a distinct audit reason for a blank pre).
- **VI107, VI117, VI252, VI230, VI225, VI74**: summaries/papers still pending owner read (category calls deferred).
- **Final counts** (all three CSVs agree): **185 rows**; `fbs_coded`: `yes=162`, `post_only=5`, `no=18`.
- **Quote completeness by layer** (expected, not a discrepancy): `reparse2` most complete (quote_pre=169, quote_post=179); `reparse` mid (150/159); canonical carries the audit-fix quotes only. The FBS **value** fields are identical across all three.