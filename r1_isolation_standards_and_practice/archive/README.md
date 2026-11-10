# Archive

Superseded and scratch material from R1 isolation-practice corpus work.
Nothing here is a source of truth for drafting; the live corpus is
`../isolation-refs.csv` (189 rows) + `../institution-guideline-protocol-refs.csv`.

## Contents

| Path | What it was | Status |
|------|-------------|--------|
| `expansion_2026-09-18/` | Former `expansion/` dir (agent-generated) | Retired. Contains raw intake CSVs, search logs, `_*.py`/`_*.json` scratch, `.bak` files |
| `expansion_2026-09-18/isolation-refs-overview_expanded.csv` | Prior merged corpus (VI2–VI293) | Superseded by `../isolation-refs.csv` |
| `expansion_2026-09-18/isolation-refs-dual-fbs_only.csv` (+ baks) | Hand-maintained dual-FBS subset | Archived (regenerate from master instead) |
| `isolation-refs-overview.csv` | Legacy 28-row subset | Superseded |
| `updated_isolation-refs-overview.csv` | Legacy + "Accuracy Assessment" column | Superseded (flag folded into `notes` column of master) |
| `institution-guideline-protocol-refs.csv.bak_*` | Backup files | Superseded |

## Notes

- The master builder is `../wrk/consolidate_isolation_refs.py`; it reads the
  archived expanded CSV OR can be repointed to the live master if re-run.
- Figure tooling was *not* archived: `../plot_fbs_distributions.py` and
  `../fbs_distribution_plots/` remain live (referenced by `../R1_for_paper_2026-09-19.md`).
- Paywall wishlist and extracted-quote archives: the wishlist was later renamed to
  `../R1_pdf_wishlist.md` (live) and the extraction-status file was removed as redundant.
  The verbatim quote archive `../quotes_paywall_extracted_2026-09-18.md` remains live.