# R3 rater-morphology figures (`wrk/viz`)

Figure toolkit for the R3 image-labelling results (CRO / IR1 / IR2 ...). Public role codes only: no real
names in code, config, data file names, figures or captions. The PNG/HTML outputs are **not tracked**;
they are regenerated from the tracked data deposits with the command below.

## Regenerate

From the repo root (any OS; Python 3.10+):

```
cd r3_image_labeling/wrk/viz
python -m venv .venv
# Windows PowerShell: .venv\Scripts\python -m pip install -r requirements.txt
# macOS / Linux:      .venv/bin/python -m pip install -r requirements.txt
.venv/Scripts/python make_figures.py --no-overlay     # Windows (macOS / Linux: .venv/bin/python ...)
```

- `--no-overlay` = the public set, built only from tracked deposits; it also rewrites `GALLERY.md`.
- Without `--no-overlay`, an optional untracked config (`settings.local_overlay`, `local/` folder, gitignored)
  adds local-only raters; the gallery then goes to `local/GALLERY_local.md` and `GALLERY.md` is left alone.
- `--only c0 h` regenerates a subset (figure-name prefixes).
- `.venv/` is gitignored (root `.gitignore`).

Outputs (all gitignored): `figures/*.png` (220 dpi), `j_styled_summary_table.html`, `index.html`,
`metrics/*.csv` (item deltas, pair agreement, coverage). `GALLERY.md` (tracked) lists every figure with
caption, key message and trade-off. Research basis for the chart choices: `VISUALIZATION_RESEARCH.md`.
Figure review thread: `../viz_figures_review.md`.

## Data sources (all tracked, repo-relative paths in `raters.toml`)

| Rater | Dataset | File |
|---|---|---|
| IR1 | Pass 1 text + Pass 2 checklist | `ir-results/cpe_detection_results_ir_gk.json` |
| IR2 | Pass 1 text + Pass 2 checklist | `ir-results/cpe_detection_results_ir2_gk.json` |
| IR1 / IR2 | CRO-comparable coding (six CRO descriptors + extras) | `ir-results/ir_cpe_detections.csv`, `ir-results/ir2_cpe_detections.csv` |
| CRO | CPE-type (CRO_Dy…CRO_Re) and healthy-type (CRO_H_*) labels, 22 frames with their own CRO description (binary) | `cro-results/cro_cpe_detections.csv` (canonical; built from `cro-results/cro_image_descriptions.txt` by `cro-results/build_cro_labels.py`) |
| — | Blinded image name ↔ path / id | `images_rater_blinded_mapping.csv` |

Computed values reproduce `ir-results/IR1_IR2_pass2_side_by_side.md` (incidence, mean scores, sums, κ).

## Layout

| Path | What |
|---|---|
| `raters.toml` | **The only file to edit**: conditions, raters, their files, colours |
| `r3viz/items.py` | 10 checklist items, vocabulary → graded 0–1 scorer (unchanged from the IR1 Pass-2 scorer), Pass-1 lexicon |
| `r3viz/loaders.py` | Reads Pass-1 text, Pass-2 checklists (CSV / XLSX / `*_gk.json`), CRO-comparable and CRO healthy-type coding |
| `r3viz/metrics.py` | Per-arm means, B − A with bootstrap CIs, Cohen's κ (undefined when a rater is constant) |
| `r3viz/figures/*.py` | One module per figure family (a … j) |
| `r3viz/gallery.py` | Captions / key-message tags / trade-offs → `GALLERY.md`, `index.html` |

Rules built in: confluence / coverage is never scored as healthy vs stressed; strict incidence =
Yes / Partial / Mild (/partial); "CPE-type" is a descriptor grouping, not a causal label; every figure
prints coverage (n per arm) and flags partial deliveries (< 90 % of the expected frames).

## CRO healthy-type descriptors

Healthy-type terms come from the same canonical file as the CRO CPE-type labels, under the
single-frame rule: a term counts for a frame only when that frame's own CRO description names it
(22 frames: 9 A / 13 B). The CRO's 10-frame group descriptions are lower-specificity, kept in
`cro-results/cro_group_level_notes.csv`, and not used in any figure. The CRO terms fill the three healthy rows (Looks healthy, Nuclei well defined, Cytoplasmic extensions) of
a, b1, c1, c2, d and j, and the healthy-type panel of the CRO row in c0 (share of the seven healthy-type descriptor keys,
Mitotic/Bright counted as one, matching the Pass-1 lexicon). CRO CPE-type rows stay blank ("—") in those
figures because the CRO's CPE-type labels use a different descriptor set (c0, e, h show them).
Footnotes on every affected figure say the CRO coding is binary, from single-frame descriptions,
and not graded; the CRO frame notes are short, so "not named" is not "absent".

## Adding a rater or condition (no code changes)

Add a `[[rater]]` block (public code, `condition`, colour, file paths) pointing at its tracked deposit
(a `*_gk.json` like IR1/IR2, or CSV/XLSX in the instrument layout). New briefing levels go in a
`[[condition]]` block (`key`, short `label`, `description`); order there = order on figure h.
Conditions without data show as "awaiting data". `note = "..."` adds a `*` to the rater's label and a
footnote (used now for CRO: briefing status to confirm). `expected_frames` overrides the partial check.

Unseen mark wording (e.g. "Moderate") falls back to the graded CPE boundary; check `metrics/` and add the
word to `CPE_SCORE` / `HEALTH_SCORE` in `r3viz/items.py` if it needs its own value.
