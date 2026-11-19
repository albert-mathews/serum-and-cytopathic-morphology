# R1 abstract-only compliance sweep — record (2026-11-06)

**Rule applied:** abstract-only research is not permitted (new agent guidance). Any corpus
value must be backed by full text, not an abstract/snippet.

**Method:** scanned `isolation-refs_reparse.csv` `access` field. Found **12** rows coded from
abstracts (`access=abstract`), all carrying `fbs_coded=yes` + FBS values + abstract-snippet
"quotes". The 7 `paywall_needed` rows are clean (no values) and already function as wishlist
stubs — no action.

**Resolution:**
- **VI247** → open-access full text (PMC8606911) fetched and read; "10% FBS growth / 2.5% FBS
  infection+maintenance" confirmed verbatim. `access=fulltext_verified`.
- **11 rows** → not open access (or no PMC record). Marked `access=abstract_full_text_outstanding`.
  Their FBS values are **provisional** until PDFs are fetched and re-extracted. Added to
  `R1_pdf_wishlist.md` §B.

**Standing note:** the 11 outstanding rows should NOT be used to make any paper claim until
their full text is read and quotes extracted. They are a correctness debt, not evidence.

**Also flagged for correctness (not part of this sweep):** rows with `legacy_coded` (n=27)
have empty quote fields — their FBS values were typed early without quote capture. They predate
the abstract-only rule (they were coded from PDFs at the time), but for full quote-backing they
too should eventually get verbatim quotes. Lower priority than the 11 abstract rows (the legacy
values are believed PDF-derived, not abstract-derived), but worth a hardening pass.

---

## RESOLVED 2026-11-19 (supersedes the "provisional" note above)

The "11 abstract-only" rows and the "7 paywall_needed" rows were **not actually missing their PDFs** — all
9 unique documents (VI234/239/240/243/244/246/249/266/267) plus the 7 paywall PDFs (VI97/103/104/108/114/
119/120) were **already on disk** in `refs/isolation_practice/` under conforming filenames. The `access`
tags were stale (never flipped), and in some paywall rows the FBS values were placeholder defaults without
quote backing.

**Actions taken (2026-11-19):**
1. Re-read all 18 rows' PDFs; extracted verbatim full-text FBS quotes.
2. Corrected VI104 post 1→2 (the "1% FBS" was a post-wash reincubation detail, not maintenance).
3. Corrected VI246 `link`/`DOI` to `10.1177/1040638715584156` (the old PMID 26082457 was wrong).
4. Flipped all 18 rows `access` → `fulltext_verified`.

**Current `access` distribution:** `oa`=114, `fulltext_verified`=28, `legacy_coded`=26, `pdf_extracted`=18.
No `abstract_full_text_outstanding` or `paywall_needed` rows remain. Every corpus ID has a PDF on disk.