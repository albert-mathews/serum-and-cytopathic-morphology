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