# Adversarial merge log — 2026-09-18

## Summary
- Expanded practice rows: **129 → 142** (+13)
- Dual-FBS-only rows: **112 → 123** (+11 = +12 new adversarial dual rows − VI233, whose pre was (not separately stated) and fails both-numeric rebuild)
- source_batch for new practice rows: dversarial_2026-09-18
- Institution ANSES FMDV SOP added: **True**
- VIRPRO1013: excluded (user rule); plotter already excludes APHIS/VIRPRO from institution dens.

## Included → new VI IDs

| provisional | new ID | pre→post | dual |
|---|---|---|---|
| ADV003 | VI234 | 10→5 | yes |
| ADV004 | VI235 | 10→5 | yes |
| ADV005 | VI236 | 10→1 | yes |
| ADV006/HOLD001 | VI237 | 5→5 | yes |
| ADV007 | VI238 | (missing)→0 | no |
| ADV008 | VI239 | 10→0 | yes |
| ADV012 | VI240 | 10→3 | yes |
| ADV013 | VI241 | 10→2 | yes |
| ADV014 | VI242 | 15→2 | yes |
| ADV015 | VI243 | 5→0 | yes |
| ADV016 | VI244 | 10→5 | yes |
| HOLD003/ADV010 | VI245 | 0→0 | yes |
| HOLD005 | VI246 | 10→10 | yes |

## Excluded (not merged into practice dual)

- **ADV001**: FMDV propagation/infection experiments — not clinical isolation
- **ADV002**: FMDV suspension propagation/infection — not clinical isolation (HOLD004 borderline)
- **ADV009**: ATCC Virology Culture Guide — already in institution corpus; do not duplicate as practice
- **ADV011**: USDA VIRPRO1013 master-seed extraneous-agent testing — USER EXCLUDED (not isolation)
- **ADV017**: Diplorickettsia — bacterium, not virus
- **ADV018**: Vaccine MDV propagation on Vero — borderline; not isolation-quality primary culture
- **ADV019/HOLD002**: Soft Opti-MEM 3→3 — protocol does not separately number distinct post FBS%; soft hold skipped
- **ADV020**: IntechOpen teaching guide general 1–3% — redundant with CLSI/ATCC institution rows; not new practice paper
- **HOLD004**: Maps ADV002 — propagation_borderline
- **HOLD006**: Maps existing VI13 (CDC WA1); already dual-coded 5-10→10 — no new row
- **HOLD007**: Maps existing VI24 (influenza SF 0→0) — already in corpus
- **HOLD008**: HEV wild-boar multi-cell — propagation_borderline; not listed as solid include
- **HOLD009**: Rabies vaccine-strain NP prep — not clinical primary isolation; maps VI29

## Institution CSV

- Added: **ANSES FMDV Virus Isolation SOP** — post=0% (without FBS); pre not stated in SOP (will not enter plot density until pre is numeric).
- Did **not** re-add CLSI/ASM/ATCC/NEADL/VIRPRO.
- Did **not** add ADV020 teaching guide (redundant with existing 1–3% / ATCC notes).

## Plots

Regenerated via expansion/plot_fbs_distributions.py (box /workspace/r1/plots/.venv) into expansion/fbs_distribution_plots/ on MSI.

Plotter papers n after parse fence: **122** (dual CSV n=123; VI227 pre=(ref. Cardoso 2000) fails parse_fbs — pre-existing).
Institutions in dens: **6** (APHIS VIRPRO excluded by plotter; ANSES in CSV but pre not numeric so not in dens).

Refreshed:
- styleA_overlapping_kde_leaders.png
- styleB_split_pre_post_panels.png
- styleC_histogram_plus_kde.png
- styleD_ridge_baselines.png
- styleE_papers_vs_guideline_spines_delta.png
- styleF_overlap_plus_delta_institution.png (speaking figure)
- bs_distribution_summary.txt

### Summary excerpt
`
papers n=122
  pre:  mean=9.28 median=10.00
  post: mean=2.28 median=2.00
institutions n=6 (APHIS VIRPRO excluded)
  pre:  [10.0, 10.0, 10.0, 10.0, 10.0, 10.0]  names=['ATCC Virology Culture Guide', 'CLSI M41-A (Viral Culture)', 'ASM Cytopathic Effects of Viruses Protocols', 'NEADL / CIRAD PPRV SOP (VI27)', 'WOAH Terrestrial Manual (MERS-CoV chapter)', 'WHO EPI']
  post: [2.0, 2.0, 2.0, 2.0, 2.0, 2.0]

Paper pre value counts:
pre
0.0       2
2.0       1
4.0       1
5.0      10
7.5       3
8.0       3
10.0    100
15.0      2

Paper post value counts:
post
0.0      8
0.2      1
1.0      9
1.5      1
2.0     84
3.0      5
4.0      1
5.0      9
6.0      1
10.0     3
`

## Notes

- HOLD equals intentionally included in dual (5→5, 10→10, 0→0) to skew distribution toward non-stepdown.
- ADV007 in expanded with blank pre + post=0 (not dual); institution row documents the SOP.
- ADV013/ADV014 coded with NBCS % in FBS columns; serum type called out in notes.
- No paywalled PDFs copied into tracked paths.
- No git commit.
- CSV backups: *.bak_20260918_094624 beside originals.
