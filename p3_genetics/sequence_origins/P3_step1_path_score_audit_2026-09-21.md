# P3 Step 1 — path_score quality audit (2026-09-21)

**Pass:** 21O · **Design:** priority-forced borderlines + fill to **≥12 `culture_cpe` and ≥12 `culture_no_cpe`**.

**Re-read basis:** event CSV `cpe_evidence` / `sample_prep_quote`; local PDFs for CMV Rowe/Oram/Spector, Hamre, Enders, Auperin, Fleckenstein, and other extracts under `_extract/`.

**Rule:** Soft documentary bar unchanged. Do **not** inflate immediate `path_score` only because a stock-origin hop finds CPE (see `P3_warrant_and_process_codes_2026-09-21.md`).

## Summary counts

| Verdict | n |
|---------|---|
| `ok` | 24 |
| `possible_inflate_to_cpe` | 0 |
| `possible_deflate_from_cpe` | 0 |
| `needs_reopen` | 0 |
| **Total audited** | **24** |

**CSV fixups applied this pass:** **none** (no clear immediate-path miscodes; borderlines listed for Albert, not thrashed).

## A. `culture_cpe` sample

| event_id | one-line warrant quote | verdict | note |
|----------|------------------------|---------|------|
| MEA-O1 | Upstream Enders & Peebles 1954: cytopathogenic agents from measles throat washings/blood in human/monkey kidney (syncytial giant cells) — Edmonston lineage origin | `ok` | Crowley HeLa Edmonston RNA + Enders 1954 cytopathogenic origin — culture_cpe OK. |
| MUM-O1 | yes — well-isolated virus plaque picked from vaccine; rMUV-induced plaques on Vero (ELISA); MUV-induced syncytia on Vero | `ok` | Plaque-picked Jeryl Lynn + syncytia/plaques; RG paper still culture_cpe under current rule. |
| RUB-O1 | Hemphill: plaque-purified Therien additional two times in Vero | `ok` | Hemphill plaque-purified Therien stock — plaque warrant. |
| ADE-O2 | Gingeras explicitly notes Ad2 preparations including one derived from a recently plaque-purified stock; heterogeneity persists after plaque purification — plaque warrant present for sequenced Ad2 DNA  | `ok` | Gingeras plaque-purified Ad2 stock explicit. |
| COV-O5 | yes — CPE first noted day 8 on tertiary monkey kidney (diffuse refractive CPE then detachment); more pronounced CPE on LLC-MK2 (cell rounding/enlargement); sequenced material = supernatant of CPE-posi | `ok` | CPE on tertiary monkey kidney day 8. |
| EV71-O1 | harvested by freezing/thawing when total cytopathic effect was seen | `ok` | Harvest at total CPE. |
| NIPAH-O1 | yes — harvested when the cytopathic effect was maximal (Harcourt Methods) | `ok` | Harcourt harvest when CPE maximal. |
| FMDV-O1 | yes — plaque-purified at beginning of passages and again after passage 16 (plaque = CPE-equivalent warrant per protocol) | `ok` | Plaque-purified at start and after p16. |
| JC-O1 | Padgett: cytopathic effect in human fetal glial cultures | `ok` | Padgett HFG cytopathic effect upstream. |
| COV-O6 | yes — cultures checked daily for cytopathic changes; day-3 Vero supernatant used for genome characterization; COV-MERS-P1 Zaki abstract: rounding/detachment/syncytia | `ok` | Daily cytopathic-change checks; day-3 supernatant. |
| MEA-C1 | MEA-P1: harvest when CPE in 70–80% monolayer; Enders 1954 cytopathogenic origin of Edmonston | `ok` | Parks CPE harvest 70–80% + Enders lineage. |
| EV71-C2 | Yes — RD cultures showing cytopathic effects harvested; plaque-purified twice in Vero | `ok` | RD CPE harvest; plaque-purified ×2 Vero. |

## B. `culture_no_cpe` sample

| event_id | one-line warrant quote | verdict | note |
|----------|------------------------|---------|------|
| CMV-O1 | CPE/plaques not stated in Fleckenstein 1982 Materials and Methods for Ad169 DNA production. Historical Rowe 1956 cytopathogenic isolation is upstream history, not this deposit Methods — not inflated. | `ok` | Fleckenstein Ad169 virion DNA — no CPE warrant. Rowe/Oram/Spector CPE-class = stock-origin layer only; do not inflate. |
| COV-O7 | CPE/plaques used for vaccinia recombinant isolation and for Inf-1 rescue validation ("cytopathic effects characteristic of human coronavirus infection"; plaque purified) — not the production warrant f | `ok` | Immediate path = MRC-5 poly(A)+ → 229E cDNA insert. Hamre CPE = stock-origin; Thiel CPE validates vaccinia rescue. |
| HSV-O1 | CPE/plaques not used as isolate warrant in McGeoch 1988 Methods. Syncytial plaque phenotype mentioned only as gene-function discussion (UL53), not DNA production. | `ok` | Strain-17 plasmid clones; syncytial plaque = gene phenotype discussion only. |
| CHIK-O1 | CPE/plaques not stated in Khan 2002 Methods for S27 stock production or RNA harvest. | `ok` | C6/36 propagation; Khan Methods lack CPE/plaque warrant. |
| POL-O1 | CPE not stated; PFU as MOI; plaques as RNA-infectivity readout upstream only | `ok` | PFU as MOI / plaque as RNA-infectivity assay ≠ isolate warrant. |
| POL-O4 | CPE not used as isolate warrant; PFU/MOI only; fingerprint stability via Nomoto 1979 | `ok` | Mahoney/HeLa; PFU/MOI only. |
| VAC-O1 | CPE not stated | `ok` | Cloned Copenhagen genome; plaque-cloning of termini is purity step — borderline for process recode, keep culture_no_cpe. |
| VZV-O1 | CPE not stated in Davison Methods excerpt | `ok` | Dumas clone libraries; Davison Methods no CPE. |
| EBV-O1 | no classical monolayer CPE; productive subset of B95-8 cells | `ok` | B95-8 producer line; no classical monolayer CPE. |
| SV40-O1 | plaque assays discussed for mutants; production Methods thin in Nature article | `ok` | Strain 776 lab DNA; plaque history not production warrant in Fiers Methods. |
| RSV-O1 | CPE not stated in Stec Methods excerpt | `ok` | A2 in HEp-2; Stec Methods no CPE warrant. |
| AAV-O1 | Ad helper CPE (4+) used as assay endpoint in Hoggan — NOT scored as AAV plaque/CPE isolate warrant for sequenced AAV2 stock | `ok` | Helper Ad CPE assay endpoint ≠ AAV isolate warrant. |

## Borderline list (no CSV change)

1. **CMV-O1** — Fleckenstein immediate = `culture_no_cpe`; Rowe 1956 cytopathogenic Ad.169 + Oram 1982 (“twice plaque-purified”; harvest ~90% CPE) + Spector 1982 (“80% cytopathic effect”) live at **stock-origin / companion** layer.
2. **COV-O7** — sequenced Inf-1 cDNA from MRC-5 RNA (`culture_no_cpe`); Hamre 1966 HEL/WI-38 CPE = stock-origin; Thiel CPE/plaque validates vaccinia recombinant, not insert production.
3. **VAC-O1** — Goebel plaque-cloned Copenhagen termini vs clone-library genome path; keep `culture_no_cpe` pending process recode decision.
4. **POL-O1 / POL-O4** — PFU/plaque as MOI or RNA-infectivity assay, not isolation warrant under current codes.
5. **AAV-O1** — helper adenovirus CPE endpoint ≠ AAV warrant.
6. **HSV-O1** — syncytial plaque phenotype in gene discussion ≠ DNA production warrant.
7. **MUM-O1** — already `culture_cpe` via plaque-picked vaccine stock; RG→CPE order is a process-hypothesis example, not a rescore.

## Possible inflate / deflate / reopen

- **possible_inflate_to_cpe:** none under *immediate-path* rule (stock-origin CPE for CMV/COV-229E recorded in hop doc instead).
- **possible_deflate_from_cpe:** none.
- **needs_reopen:** none in this sample.

## Audited IDs

**culture_cpe:** MEA-O1, MUM-O1, RUB-O1, ADE-O2, COV-O5, EV71-O1, NIPAH-O1, FMDV-O1, JC-O1, COV-O6, MEA-C1, EV71-C2

**culture_no_cpe:** CMV-O1, COV-O7, HSV-O1, CHIK-O1, POL-O1, POL-O4, VAC-O1, VZV-O1, EBV-O1, SV40-O1, RSV-O1, AAV-O1


---

## 21P addendum — LASSA-O1

| event_id | change | verdict |
|----------|--------|---------|
| LASSA-O1 | Was `unclear`/`chain_open`. Soft-bar closed via **Auperin 1986** Josiah Methods (plaque×3 Vero E6; BHK-21 purified virion RNA) cited by Auperin 1989. Immediate `path_score` → **`culture_cpe`**; `chain_closed`. | `ok` — plaque purification is CPE-class warrant (same rule as RUB/FMDV/ADE). Do **not** inflate from Buckley alone: Buckley is species isolation (Nigeria 1969), not Josiah (Sierra Leone 1976). Clegg 1985 = GA391 Nigerian, not sequenced Josiah path. |

CSV culture_cpe count after fix: **37**; chain_open remaining: **0**.
