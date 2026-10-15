# P4 coding sheet - antigen / immunogen provenance

**Frozen:** 2026-10-15. Changes require a logged amendment in the Amendment log below;
do not silently add, rename or redefine codes once rows are being collected.

Operationalizes the seven-field provenance stack in `P4_prediction.md` into a fixed
extraction form. One row per assay product or per assay-as-reported-in-a-paper.
Rows live in `p4_antigen_provenance.csv`.

## Scope

**In scope.** Serology and antigen assays of any format (ELISA, IFA/IFT, Western/immunoblot,
lateral flow / rapid antigen, complement fixation, haemagglutination inhibition, virus
neutralization) whose reference materials can be traced, plus the assays as described in
primary papers.

**Equal weight.** Animal / veterinary Isolation serology counts as equal-weight rows
alongside human diagnostics (Albert, 2026-10-15). The `domain` column records which,
so human-only subsets can still be cut later.

**Excluded.** HIV (repo-wide ontology exclusion) and bacteriophage systems. No other
hard exclusions (Albert, 2026-10-15).

**Sampling order.** Kit-insert census first, then serology reported in R1 dual-serum
Isolation papers, then 10-20 adversarial clinical-serology sources that claim to avoid
culture-derived antigen. Do not reshape the sample toward 10-to-2 serum-shift recipes.

## Row id

`P4-###`, assigned in the order rows are entered and never reused. A superseded row keeps
its id and is marked in `status`.

## Columns and allowed values

| # | Column | Allowed values | Notes |
|---|--------|----------------|-------|
| 1 | `row_id` | `P4-###` | never reused |
| 2 | `source_type` | `kit_insert`, `datasheet`, `primary_paper`, `reference_material_catalogue`, `guideline` | what was actually read |
| 3 | `source_ref` | free text | product / citation identifier, no personal names |
| 4 | `source_url_or_refs_id` | free text | public URL, or the id of a PDF kept in gitignored `refs/` |
| 5 | `domain` | `human`, `veterinary`, `both` | equal weight; for subsetting only |
| 6 | `agent_label` | free text | organism label as the source names it |
| 7 | `assay_format` | `elisa`, `ifa`, `western`, `lateral_flow`, `neutralization`, `complement_fixation`, `hai`, `other`, `unclear` | |
| 8 | `analyte_claimed` | `antibody_titer`, `antigen_capture`, `neutralizing_activity`, `western_band`, `other`, `unclear` | field 1 of the stack |
| 9 | `immunogen_or_reference_source` | `culture_isolate_lysate`, `purified_culture_particles`, `inactivated_culture_virus`, `recombinant_from_culture_ref`, `recombinant_source_unclear`, `synthetic_peptide`, `clinical_specimen`, `not_stated`, `unclear` | field 2; `recombinant_from_culture_ref` is deliberately not scored as independence |
| 10 | `isolate_justification` | `cpe`, `plaque`, `tcid50`, `pcr_only`, `serology_only`, `unspecified`, `not_applicable` | field 3: how the Isolate was historically justified |
| 11 | `matched_mock_run` | `yes`, `no`, `unclear`, `not_stated` | field 4; `not_stated` is the expected default for inserts |
| 12 | `mock_reactivity_reported` | `reactive`, `nonreactive`, `not_reported`, `not_applicable` | only meaningful when 11 is `yes` |
| 13 | `serum_or_maintenance_language` | `dual_serum_shift`, `serum_pct_stated`, `serum_free_claimed`, `serum_mentioned_no_detail`, `not_stated` | field 5; link to R1 where `dual_serum_shift` |
| 14 | `particle_separation_claim` | `density_gradient`, `filtration_or_pellet_only`, `ev_markers_assessed`, `purity_claimed_no_method`, `not_applicable`, `unclear` | field 6; apply P2 overlap codes when "purified virus" is claimed |
| 15 | `sequence_path` | `culture_cpe`, `culture_no_cpe`, `clinical_direct`, `unclear`, `not_applicable` | field 7; same vocabulary as P3 `risk_path` |
| 16 | `accession_or_strain` | free text | only as printed in the source |
| 17 | `inheritance_score` | `inherits`, `partial`, `independent`, `undetermined` | summary judgement, derived from 9-15 |
| 18 | `evidence_quote` | free text, <= 25 words | verbatim from the source, or empty |
| 19 | `coder_note` | free text | reasoning, ambiguities |
| 20 | `status` | `active`, `superseded`, `excluded` | |

## Filling rules

- Code only what the source itself states. Never infer a cell-substrate, strain or
  accession that is not printed, and never carry a value over from a sibling product.
- Absent information is `not_stated`; genuinely contradictory or unreadable information
  is `unclear`. The two are not interchangeable, and the split between them is itself a
  finding (inserts that simply never say).
- Quotes are short and attributed by URL or `refs/` id. No PDFs in tracked paths.
- `inheritance_score` is a judgement, not a measurement: it must be defensible from the
  other columns alone, and the reasoning goes in `coder_note`.
- Role codes only in tracked files; no manufacturer contact names or staff names.

## Amendment log

| Date | Amendment | Reason |
|------|-----------|--------|
| 2026-10-15 | Sheet frozen at 20 columns | Initial freeze before corpus collection |
| 2026-10-15 | Proposed (NOT applied): split `immunogen_or_reference_source` into `immunogen_source` + `reference_antigen_source` | Pilot row P4-008 has different sources for the immunogen and the plate antigen; awaiting Albert |
