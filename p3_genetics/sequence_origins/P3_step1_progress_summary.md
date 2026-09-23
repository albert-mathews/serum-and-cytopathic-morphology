# P3 Step 1 — Progress summary

**Updated:** 2026-09-21 ~21:30 ET (pass **21M**). **Step 1 IN PROGRESS — not done.**

## Evidentiary-bar clarification (USER 2026-09-21) — still in force
Adequate documentary evidence linking **sample-production method ↔ deposited genome** within reasonable scientific doubt — **not** forensic chain-of-custody. Patterns 1–2 are examples only. Close when method↔deposit clear; quote Methods. Prefer honest `culture_cpe` when CPE/plaque/syncytia warrant present; do **not** inflate `culture_no_cpe` into `culture_cpe`.

## Counts before → after (pass 21M)

| Metric | Before (21L / ~20:45 ET) | After (21M) |
|--------|--------------------------|-------------|
| Events | 101 | **102** (+BK-O2 Seif Dunlop) |
| chain_closed | **85** | **97** (+12) |
| chain_open | 16 | **5** |
| Provenance nodes | 69 | **70** (+FMDV-P_kupper_1981) |
| Local PDFs in refs/sequence_origins | ~137+ | **+22 evening batch** (titles verified) |

### path_score breakdown (closed events only)

| path_score | Before (21L) | After (21M) |
|------------|--------------|-------------|
| culture_cpe | **32** | **36** (+NIPAH-O1, ASTRO-O1, BVDV-O1, BTV-O1) |
| culture_no_cpe | **36** | **41** (+HPIV1-O1, FCV-O1, CDV-O1, CSFV-O1, BK-O2) |
| clinical_direct | **10** | **11** (+SAPO-O1) |
| other | **7** | **9** (+ZIKV-O1, MARB-O1) |
| unclear | 0 | 0 |

## New closes this pass (11 + 1 new event)

| event_id | path_score | 1-line warrant |
|----------|------------|----------------|
| **NIPAH-O1** | culture_cpe | Harcourt: brain→Vero E6; harvest at maximal CPE; RNA from infected cells. |
| **ASTRO-O1** | culture_cpe | Willcocks: CaCo-2 from stool (p1); RNA before appearance of c.p.e. |
| **BVDV-O1** | culture_cpe | Collett: NADL three-times plaque-purified; cytopathic on MDBK. |
| **BTV-O1** | culture_cpe | Fukusho: BTV-10 CA-8 plaque-cloned on BHK-21; dsRNA. |
| **HPIV1-O1** | culture_no_cpe | Newman: LLC-MK2 supernatant virion RNA; TCID50 only. |
| **FCV-O1** | culture_no_cpe | Carter: F9/CRFK CsCl virion RNA; no CPE word. |
| **CDV-O1** | culture_no_cpe | Sidhu (OCR): Onderstepoort/HeLa spinner infected-cell RNA. |
| **CSFV-O1** | culture_no_cpe | Meyers: Alfort×pig lymphoma 38A,D virion RNA; no Alfort CPE. |
| **BK-O2** (new) | culture_no_cpe | Seif: Dunlop HEK culture Hirt DNA; PFU=MOI only. |
| **SAPO-O1** | clinical_direct | Numata: stool RNA + EM; no culture (3′ partial O). |
| **ZIKV-O1** | other | Kuno: RNA from suckling-mouse-brain suspension (p1–3). |
| **MARB-O1** | other | Bukreyev: Popp RNA from guinea-pig-blood–purified virions (9 GP passages). |

## New culture_cpe IDs this pass (Methods warrant)

- **NIPAH-O1** — “harvested when the cytopathic effect was maximal”
- **ASTRO-O1** — “before the appearance of c.p.e.” (CPE as named culture phenotype)
- **BVDV-O1** — “three-times plaque purified” + “cytopathic to cells in culture”
- **BTV-O1** — “plaque-cloned using monolayers of BHK-21 cells”

## New other closes

- **ZIKV-O1** — mouse-brain RNA (not cell culture)
- **MARB-O1** — guinea-pig blood virions (animal-only)

## Full closed culture_cpe list (36)

ADE-O1, ADE-O2, ASTRO-O1, BTV-C1, BTV-C2, BTV-O1, BVDV-C1, BVDV-C2, BVDV-O1, CDV-C1, CDV-C3, COV-C5, COV-O2, COV-O5, COV-O6, DEN-O1, EBO-O1, EV71-C1, EV71-C2, EV71-O1, FMDV-C1, FMDV-O1, HEND-O1, JC-O1, MEA-C1, MEA-O1, MUM-O1, NDV-O1, NIPAH-C1, NIPAH-O1, RSV-C1, RUB-O1, SIN-O1, VSV-C1, WNV-C1, WNV-O1

## Still open (5)

- **CMV-O1** — Chee chapter thin; need Bankier/Oram/Fleckenstein/Rowe production Methods
- **COV-O7** — Thiel 2001 JGV Inf-1 Methods still missing (Hamre P now have)
- **LASSA-O1** — PDF have; Methods insufficient (“viral RNA templates” only)
- **HSV-O1** — **could_not_obtain**
- **CHIK-O1** — **could_not_obtain**

## Wishlist / bib hygiene (21M)

- `P3_step1_pdf_wishlist.md` — rewritten lean (missing / could_not_obtain / have-insufficient / optional only)
- `P3_sequence_origins_bibliography.md` — rewritten as used-only bibliography
- `P3_sequence_origins_read_but_unused.md` — **new** (SFV Clegg tangential; LASSA insufficient; CDC Urbani dump)

## Supporting literature
`P3_supporting_literature_culture_cpe_genetics_2026-09-21.md` — unchanged this pass (no new wet genetics-beyond-census paper).

## Success-criteria check (21M)

- [x] 22 evening-batch PDFs title-verified; text/OCR extracted
- [x] Soft-bar closes with Methods quotes; no CPE inflation
- [x] Family notes / wishlist / progress / results updated
- [x] Used-bib + read-unused cleaned
- [x] Docs-only tar packed
- [x] No Sci-Hub; no git commit of PDFs; no Kolabtree
- [ ] Step 1 **not** marked done

## Pass 21N (~22:15 ET)
- Closed **COV-O7, HSV-O1, CHIK-O1, CMV-O1** all `culture_no_cpe`.
- Totals: n=102, closed=101, open=1 (LASSA-O1 only).
- path_score closed: culture_cpe=36, culture_no_cpe=45, clinical_direct=11, other=9.
- Deliverables: `P3_step1_path_type_map_2026-09-21.md`, `P3_step1_path_type_counts_2026-09-21.png`, `P3_step1_path_type_by_family_2026-09-21.png`.
