# P3 archive - earlier attempts (index)

Superseded P3 material, moved here 2026-10-14 so the base `p3_genetics/` folder holds only the current work. Files were moved, not edited or deleted (git history follows the moves). The current work is the Step 1 genome-origin path census in [`../sequence_origins/`](../sequence_origins/); the stream summary and discussion thread is [`../p3.md`](../p3.md).

| Folder | Dates | What the attempt was | Contents | Superseded by |
|---|---|---|---|---|
| [`01_type_strain_audit_2026-09-19/`](01_type_strain_audit_2026-09-19/) | 2026-09-19 | First pilot: literature audit of type / prototype strains, coding a `risk_path` for whether type material came through culture. | `P3_type_strain_audit_protocol.md` (coding rules), `P3_type_strain_audit.csv` (first batch, ~45 entries) | Step 1 event/node coding with documentary path_score (`../sequence_origins/P3_step1_protocol.md`) |
| [`02_genbank_metadata_mining_2026-09-19/`](02_genbank_metadata_mining_2026-09-19/) | 2026-09-19 | Pilot of automated GenBank/RefSeq metadata mining (isolation-source and host fields) as a fast proxy for sample origin. | `P3_genbank_refseq_metadata_mining.md` (plain-language explainer + Entrez recipe), `genbank_mining/` (results note, `mining_summary.json`, metadata sample CSV, `run_pilot.py`) | Paper-by-paper Methods reading in Step 1 (the pilot note itself records that metadata keywords are under-annotated and reports prevalence only, e.g. culture terms in 18.1% and CPE in 0.05% of records) |
| [`03_prediction_B_angle_2026-09-20/`](03_prediction_B_angle_2026-09-20/) | 2026-09-20 | First write-up of the "Prediction B" research angle that set up the census. | `P3_prediction_B_research_angle_2026-09-20.md` | `../sequence_origins/P3_research_plan_refined_2026-09-21.md` (moved into `sequence_origins/`, still the agreed plan) |
| [`04_step1_toplevel_snapshot_2026-09-21/`](04_step1_toplevel_snapshot_2026-09-21/) | 2026-09-21 (through about 17:30 ET) | Step 1 working files as they sat at the top of `p3_genetics/` before work was consolidated into `sequence_origins/`. 70 files: 30 identical to the `sequence_origins/` copy, 40 earlier versions (every differing file is older and, except `family_cmv.md` and `family_vsv.md`, shorter than its `sequence_origins/` counterpart). | `P3_*` notes, `P3_sequence_origin_events.csv`, `P3_sequence_provenance_nodes.csv`, 60 `family_*.md` | The same-named files in `../sequence_origins/` |

Not tracked and not moved: the `*.tar` / `*.tar.gz` sync bundles at the top of `p3_genetics/` (operational files, gitignored) and `refs/` (PDFs, gitignored).

Earlier wishlist files (`P3_step1_pdf_wishlist.md`, DOI and Unpaywall audits) were folded into `../sequence_origins/P3_pdf_catalogue.md` on 2026-10-14.
