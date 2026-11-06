# P4 coding sheet - antigen / immunogen provenance

**Frozen:** 2026-10-15, amended 2026-10-19 (amendment 2, applied; all rows re-scored).
Changes require a logged amendment below. Amending is allowed and expected when a column
is found to be wrong or missing; what is not allowed is changing codes row-by-row as the
corpus grows. An amendment must be logged **and** every existing row re-scored under the
new version, so that all rows in the file were coded under the same version.

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
| 9 | `disclosure_level` | `substrate_and_strain_named`, `substrate_named_only`, `format_only`, `none_disclosed` | **amendment 2.** How much provenance the document discloses *at all*, independent of what that provenance is. A kit that never says what is on the plate cannot be assessed for inheritance in either direction |
| 10 | `immunogen_source` | `culture_isolate_lysate`, `purified_culture_particles`, `inactivated_culture_virus`, `recombinant_from_culture_ref`, `recombinant_source_unclear`, `synthetic_peptide`, `clinical_specimen`, `not_stated`, `unclear`, `not_applicable` | **amendment 2.** What raised the antibody / immunised the host. `not_applicable` for assays that detect the patient's own antibodies |
| 11 | `reference_antigen_source` | same value set as 10 | **amendment 2.** What is physically on the plate, slide, strip or membrane. Can differ from 10 within one product |
| 12 | `upstream_source_pointer` | `repository_accession_given`, `strain_designation_only`, `passage_history_given`, `none`, `not_applicable` | **amendment 2.** Naming an ATCC/BEI deposit or a strain does not establish independence; it points at a second provenance question one hop upstream. Record whether the document gives a traceable pointer, and resolve it in a separate upstream row rather than inside this one |
| 13 | `isolate_justification` | `cpe`, `plaque`, `tcid50`, `pcr_only`, `serology_only`, `unspecified`, `not_applicable` | field 3: how the Isolate was historically justified |
| 14 | `matched_mock_run` | `yes`, `no`, `unclear`, `not_stated` | field 4. `no` means the document addresses uninfected material but does not run it as a matched antigen; `not_stated` means it is never mentioned |
| 15 | `mock_reactivity_reported` | `reactive`, `nonreactive`, `not_reported`, `not_applicable` | only meaningful when 14 is `yes` |
| 16 | `serum_or_maintenance_language` | `dual_serum_shift`, `serum_pct_stated`, `serum_free_claimed`, `serum_mentioned_no_detail`, `not_stated` | field 5; link to R1 where `dual_serum_shift` |
| 17 | `particle_separation_claim` | `density_gradient`, `filtration_or_pellet_only`, `ev_markers_assessed`, `purity_claimed_no_method`, `not_applicable`, `unclear` | field 6; apply P2 overlap codes when "purified virus" is claimed |
| 18 | `sequence_path` | `culture_cpe`, `culture_no_cpe`, `clinical_direct`, `unclear`, `not_applicable` | field 7; same vocabulary as P3 `risk_path` |
| 19 | `accession_or_strain` | free text | only as printed in the source |
| 20 | `inheritance_score` | `inherits`, `partial`, `independent`, `undetermined` | summary judgement, derived from 9-18 |
| 21 | `evidence_quote` | free text, <= 25 words | verbatim from the source, or empty |
| 22 | `coder_note` | free text | reasoning, ambiguities |
| 23 | `status` | `active`, `superseded`, `excluded` | |

## Filling rules

- Code only what the source itself states. Never infer a cell-substrate, strain or
  accession that is not printed, and never carry a value over from a sibling product.
- Absent information is `not_stated`; genuinely contradictory or unreadable information
  is `unclear`. The two are not interchangeable, and the split between them is itself a
  finding (inserts that simply never say).
- `undetermined` in `inheritance_score` is not a weak `inherits`. It means the document
  does not permit a judgement, which is what `disclosure_level` now records separately.
- Quotes are short and attributed by URL or `refs/` id. No PDFs in tracked paths.
- `inheritance_score` is a judgement, not a measurement: it must be defensible from the
  other columns alone, and the reasoning goes in `coder_note`.
- Role codes only in tracked files; no manufacturer contact names or staff names.

## Amendment log

| Date | Amendment | Reason |
|------|-----------|--------|
| 2026-10-15 | Sheet frozen at 20 columns | Initial freeze before corpus collection |
| 2026-10-19 | **Amendment 2, applied.** Split `immunogen_or_reference_source` into `immunogen_source` + `reference_antigen_source`; added `disclosure_level` and `upstream_source_pointer`. 20 -> 23 columns. All 8 existing rows re-scored under v2 | P4-008 carries different sources for immunogen and plate antigen, so one column forced a false choice. Non-disclosure was the strongest pilot signal and was being absorbed into `undetermined`. Naming an ATCC/BEI deposit or strain defers the provenance question upstream rather than answering it (Albert, 2026-10-15) |
