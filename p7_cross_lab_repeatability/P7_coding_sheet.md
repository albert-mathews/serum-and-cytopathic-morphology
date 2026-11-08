# P7 coding sheet — cross-lab repeatability of Isolation-linked claims

**Frozen:** 2026-11-07. Changes require a logged amendment below. Amending is allowed and expected when a
column is found wrong or missing; what is *not* allowed is changing codes row-by-row as the corpus grows.
An amendment must be logged **and** every existing row re-scored under the new version, so all rows in the
file were coded under the same version.

Operationalizes the prediction in `P7_prediction.md` into a fixed extraction form. One row per
inter-laboratory comparison (a ring trial / EQA / proficiency-test round, a multi-lab aliquot split, or a
multi-rater image set). Rows live in `p7_repeatability_corpus.csv`.

## Scope

**In scope.** Any published inter-laboratory or inter-rater comparison whose endpoint rests on Isolation
culture or on culture-derived reagents, particles, antigens, or sequences. Two first-class tiers and one
secondary tier:

- **Isolation / CPE endpoint** (first class): panels scored on virus Isolation, cell-culture detection, or
  CPE reading.
- **Culture-derived downstream endpoint** (first class where the reference is culture): titer (TCID₅₀/plaque),
  antigen/IFA on culture isolates, neutralization against culture stock, assemblies of a shared stock.
- **Molecular / serology EQA** (secondary): molecular or serological proficiency panels. Coded for P3/P4
  inheritance via `p3_inheritance_flag` *only when* the assay's reference/positive material traces to culture;
  otherwise it is out of scope for the P7 headline and is recorded for the inheritance ledger rather than
  scored as a repeatability claim (failure mode 5, P7_prediction.md).

**Equal weight.** Animal / veterinary panels count as equal-weight rows alongside human ISNs (mirrors P4).
The `domain` column records which, so human-only subsets can still be cut later.

**Excluded.** HIV and bacteriophage systems (repo-wide ontology exclusion). No other hard exclusions.

**Sampling order.** Public ring-trial / EQA reports first (prefer WHO/OIE-style network and reference-lab
schemes), then multi-lab aliquot-split papers on named stocks, then explicit inter-rater image sets. Do not
reshape the sample toward low-serum recipes.

## Row id

`P7-###`, assigned in the order rows are entered and never reused. A superseded row keeps its id and is
marked in `status`.

## Columns and allowed values

| # | Column | Allowed values | Notes |
|---|--------|----------------|-------|
| 1 | `row_id` | `P7-###` | never reused |
| 2 | `source_type` | `eqa_report`, `ring_trial`, `proficiency_panel`, `aliquot_split`, `rater_image_set`, `network_report` | what kind of comparison was run |
| 3 | `source_ref` | free text | study / product / scheme identifier, no personal names beyond authors |
| 4 | `source_id` | free text | PMID, DOI, or URL; or the id of a PDF kept in gitignored `refs/` |
| 5 | `year` | integer | publication year |
| 6 | `domain` | `human`, `veterinary`, `both` | equal weight; for subsetting only |
| 7 | `agent_label` | free text | organism label as the source names it |
| 8 | `endpoint_class` | `isolation_cpe`, `titer`, `antigen`, `assembly`, `morphology_rater`, `molecular`, `serology` | primary endpoint scored by the comparison |
| 9 | `n_labs_or_raters` | integer | number of participating labs (or raters, if `morphology_rater`) |
| 10 | `serum_disclosed` | `yes`, `no`, `partial` | does the report state the serum/medium used at the scored step? |
| 11 | `c_tier_link_r2` | `A`, `B`, `C`, `D`, `na` | matched-negative-control quality of the scored Isolation step, per R2 tiers; `na` for non-Isolation endpoints |
| 12 | `discordance_metric` | free text | what was measured (e.g. "% labs getting all correct", "VI success rate", "kappa") |
| 13 | `discordance_value` | free text | the number, quoted from the source |
| 14 | `evidence_tag` | `VERIFIED`, `FIGURE`, `SUPPLIER`, `UNVERIFIED`, `DATA_REQUIRED` | house tag; `DATA_REQUIRED` until the full text is read (abstract-only research is not allowed) |
| 15 | `harmonization_changed_serum_or_threshold` | `yes`, `no`, `unclear` | did concordance rise only after serum/threshold/SOP were forced identical? |
| 16 | `p3_inheritance_flag` | `yes`, `no`, `unclear` | for molecular endpoints: does the assay's reference/positive material trace to culture (code P3 inheritance)? |
| 17 | `evidence_quote` | free text, <= 40 words | verbatim from the source, or empty |
| 18 | `coder_note` | free text | reasoning, ambiguities, what still needs the full text |
| 19 | `status` | `active`, `superseded`, `excluded` | |

## Filling rules

- Code only what the source itself states. Never infer a serum %, a control design, or an accession that is
  not printed.
- Absent information is `no` (for `serum_disclosed`) or `na`/`no` (for `c_tier_link_r2`); genuinely
  contradictory or unreadable information goes in `coder_note`, not silently into a value.
- `discordance_value` carries the number **and its denominator or unit** so a rate is never a bare count.
- **Abstract-only research is not allowed.** A row scored only from an abstract/snippet is `evidence_tag =
  DATA_REQUIRED` and carries `full text outstanding` in `coder_note`; it is a *deferred* row, not a claim.
  Only after the full text (or free full text) is read and the number is re-confirmed there may the tag be
  upgraded to `VERIFIED`.
- Quotes are short and attributed by PMID/DOI or `refs/` id. No PDFs in tracked paths.
- Role codes only in tracked files; no personal names of scheme staff beyond what the byline already prints.

## Hierarchy of the headline

The P7 prediction (C057) distinguishes **template-following concordance from robustness under deliberate
serum/matrix/control variation**. Coding priority reflects that:

1. A panel whose discordance is **explained by** serum lot / medium / threshold / SOP variation is the
   strongest evidence (strengthens C057).
2. A panel whose concordance **rises only after protocol harmonization** (serum/threshold forced identical)
   is high-information for the process-template reading.
3. A panel with high concordance *and* strong matched controls *and* stated serum is a candidate falsifier.
4. A molecular/serology EQA is secondary and, where its reference is culture-derived, is an inheritance
   observation (P3/P4), not a particle-proof observation.

## Amendment log

| Date | Amendment | Reason |
|------|-----------|--------|
| 2026-11-07 | Sheet frozen at 19 columns | Initial freeze before corpus collection |