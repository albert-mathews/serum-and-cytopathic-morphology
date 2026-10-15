# P3 Step 1 — Progress summary

**Updated:** 2026-09-21 ~17:45 ET (pass **21i**). **Step 1 IN PROGRESS — not done.**

## Evidentiary-bar clarification (USER 2026-09-21) — still in force
Adequate documentary evidence linking **sample-production method ↔ deposited genome** within reasonable scientific doubt — **not** forensic chain-of-custody. Patterns 1–2 are examples only. Close when method↔deposit clear; quote Methods. Prefer honest `culture_cpe` when CPE/plaque/syncytia warrant present; do **not** inflate `culture_no_cpe` into `culture_cpe`.

## Counts before → after (pass 21i)

| Metric | Before (21i start / ~16:30 ET) | After (21i) |
|--------|--------------------------------|-------------|
| Events | 94 | **94** |
| chain_closed | **38** | **53** |
| chain_open | 56 | **41** |
| provenance_gap | 0 | **0** |
| Provenance nodes | 61 | **61** (no new P nodes this pass) |
| Local PDFs in refs/sequence_origins | 126 | **126** |

### path_score breakdown (closed events only)

| path_score | Before | After |
|------------|--------|-------|
| culture_cpe | **13** | **22** |
| culture_no_cpe | **19** | **23** |
| clinical_direct | **4** | **6** |
| other | **2** | **2** |
| unclear | 0 | 0 |

## New culture_cpe closes this pass (9)

| event_id | 1-line warrant |
|----------|----------------|
| **COV-O5** | van der Hoek 2004: VIDISCA/genome from **CPE-positive LLC-MK2** supernatant (NPA→tMK/LLC-MK2 CPE). |
| **COV-O6** | van Boheemen 2012: cultures checked daily for **cytopathic changes**; day-3 Vero supernatant → genome (~6 culture passages). |
| **FMDV-O1** | Forss 1984: BHK O1K RNA **plaque-purified** at start and after p16. |
| **MUM-O1** | Clarke 2000: **plaque-picked** Jeryl Lynn from Mumpsvax; syncytia/plaques; AF201473. |
| **HEND-O1** | Wang 2000 via Wang 1998: HeV **plaque-purified** on Vero; sequenced from purified genomic RNA. |
| **NIPAH-C1** | Harcourt 2005: Vero E6 **CPE/syncytia**; AY988601 from first culture isolate. |
| **CDV-C1** | Lednicky 2004: raccoon tissue→Vero primary isolation with **CPE/syncytia**. |
| **WNV-C1** | Beasley 2004: raven brain→Vero V2; **plaque-purified** variants; AY660002. |
| **RSV-C1** | Collins 1995: A2 reverse-genetics; **syncytial CPE/plaques** on HEp-2. |

## Other new closes this pass (6)

| event_id | path_score | warrant |
|----------|------------|---------|
| **COV-O1** | culture_no_cpe | Marra Tor2: Vero E6 growth↔deposit clear; **CPE word absent** — not inflated. |
| **HAV-O1** | culture_no_cpe | Najarian: stool→tissue culture per Provost; RNA from virions; CPE not stated. |
| **RHV-O1** | culture_no_cpe | Stanway: Ohio HeLa culture clear; CPE never stated for HRV-14. |
| **AAV-O1** | culture_no_cpe | Srivastava: HeLa+Ad2 helper culture; Ad 4+ CPE = helper assay, not AAV culture_cpe. |
| **COV-O4** | clinical_direct | Woo HKU1: culture failed; genome from clinical NPA RNA. |
| **BOCA-O1** | clinical_direct | Allander: clinical NPA molecular screen; no culture for sequenced material. |

## Still open / high-value blockers (examples)

- **CMV-O1** Chee AD169 chapter (have PDF; production Methods thin) — leave open.
- **HEND-P2** Murray 1995 Science PDF **missing** (abstract syncytia only; HEND-O1 closed on Wang 1998 plaques).
- **COV-MERS-P1** Zaki 2012 NEJM PDF **missing** (abstract CPE used as support; COV-O6 closed on van Boheemen Methods).
- **HSV-O1**, **CHIK-O1** could_not_obtain.
- **BK-Seif**, **SFV-P1** PDFs missing (SFV-O1 still open).
- **MEA-C2** Radecke left open (rescue CPE ≠ proven clone-antigenome production path).
- Many expansion-list O events still abstract-only / PDF-blocked (Zika O, Marburg, Lassa, Astro, etc.).

## Supporting literature (new)

`P3_supporting_literature_culture_cpe_genetics_2026-09-21.md` — Tier A–B cites for (a) culture/CPE isolate practice, (b) MIUViG/MigsVi source labeling, (c) influenza passage metadata. Pointer also added to prior-art file.

## Full closed culture_cpe list (22)

CDV-C1, COV-C5, COV-O2, COV-O5, COV-O6, DEN-O1, EBO-O1, EV71-C1, EV71-O1, FMDV-O1, HEND-O1, JC-O1, MEA-C1, MEA-O1, MUM-O1, NDV-O1, NIPAH-C1, RSV-C1, RUB-O1, SIN-O1, WNV-C1, WNV-O1

## Success-criteria check (21i)

- [x] Priority dig targets worked with local PDFs / OA
- [x] New culture_cpe closes preferred over mass culture_no_cpe
- [x] Methods quotes in CSV fields
- [x] Supporting literature file created
- [x] Progress counts before→after
- [x] No Sci-Hub; no git commit of PDFs
- [ ] Step 1 **not** marked done
- [ ] MSI CopyFromBox sync (docs only)

