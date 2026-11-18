# P3 — Virus sequence-progeny tracking board (living)

**Purpose.** One board for the P3 question "*does this virus's deposited reference sequence trace back to
culture ± CPE?*" — organized into the three buckets Albert asked for: **trails complete**, **partially
tracked**, and **not attempted yet**. This is a *view* over the existing Step 1 apparatus
(`P3_sequence_origin_events.csv`, `P3_step1_path_type_map_2026-09-21.md`, `P3_stock_origin_hops_2026-09-21.md`),
not a replacement for it. The CSVs and family sheets remain the source of record; this board is the index that
tells us, per virus, where the trail stands and where there is still a virus worth probing.

**Last updated:** 2026-11-18.

---

## How the three buckets are defined

| Bucket | Meaning | Where the detail lives |
|--------|---------|------------------------|
| **Trail complete** | The sequence→production chain for the named virus/strain is `chain_closed` and a `path_score` is assigned (`culture_cpe` / `culture_no_cpe` / `clinical_direct` / `other`). | `P3_sequence_origin_events.csv` + `P3_step1_path_type_map_2026-09-21.md` |
| **Partially tracked** | A sequence path is closed, but a **stock-origin** question is still open (lineage gap, vaccine/plaque-vs-clinical isolate, `hop_open_need_pdf`, abstract-only P-node, `could_not_obtain` residual), or the virus is in the corpus but only a sub-genomic / non-reference deposit is closed. Worth finishing before the trail counts as airtight. | `P3_stock_origin_hops_2026-09-21.md` + family sheets + event `notes` |
| **Not attempted yet** | A named reference virus (or strain/serotype) with a well-defined public reference sequence that has **no** Step 1 event row at all. Candidate queue for future passes. | `P3_step1_family_expansion_list.md` (Tier C) + this board |

`path_score` is a documentary code (how the census papers describe production of the sequenced material), **not**
an endorsement that a culture isolate is a virus. Soft evidentiary bar throughout (see `P3_step1_protocol.md`).

---

## Bucket 1 — Trails complete (109 O/C events; all `chain_closed`, 0 open)

*(HDV — the former single `chain_open` row — was closed 2026-11-18 via OCR of Wang 1986 → `other`.)*

All 109 Step 1 events are `chain_closed` with an assigned `path_score`. The authoritative virus→path table is
`P3_step1_path_type_map_2026-09-21.md` §3; reproduced here at a glance (event ids in parentheses). **One event
row = one O or C sequence-deposit; a virus family may contribute events to more than one path.**

### `culture_cpe` — 39 events

adenovirus 2 (ADE-O1, O2) · astrovirus HAstV-1 (ASTRO-O1) · bluetongue virus (BTV-O1, C1, C2) ·
BVDV (BVDV-O1, C1, C2) · canine distemper (CDV-C1, C3) · dengue 2 (DEN-O1) · Ebola Zaire/Mayinga (EBO-O1) ·
enterovirus 71 (EV71-O1, C1, C2) · FMDV (FMDV-O1, C1) · Hendra (HEND-O1) · JC polyomavirus (JC-O1) ·
human metapneumovirus 00-1 (HMPV-O1) · Lassa Josiah (LASSA-O1) · measles Edmonston (MEA-O1, C1) · MERS-CoV (COV-O6) · mumps Jeryl Lynn (MUM-O1) ·
NDV LaSota (NDV-O1) · Nipah (NIPAH-O1, C1) · RSV A2 (RSV-C1) · rubella Therien (RUB-O1) ·
SARS-CoV Urbani (COV-O2) · SARS-CoV-2 WIV04 (COV-C5) · HCoV-NL63 (COV-O5) · Sindbis (SIN-O1) ·
VSV Indiana C1 (VSV-C1) · West Nile (WNV-O1, C1) · dengue 4 (DEN4-O1)

### `culture_no_cpe` — 47 events

AAV-2 (AAV-O1) · adenovirus 5 (ADE-C1) · BK polyomavirus (BK-O1, O2) · chikungunya S27 (CHIK-O1) ·
CMV AD169/Merlin/Towne (CMV-O1, C1, C2, C3) · coxsackievirus B3 Nancy (COX-O1) ·
CSFV Alfort (CSFV-O1, C1) · HCoV-OC43 (COV-O3, C2) · HCoV-229E (COV-O7, C4) ·
SARS-CoV Tor2 (COV-O1, C1) · EBV B95-8 (EBV-O1) · feline calicivirus (FCV-O1) · Hantaan (HANTA-O1) ·
HAV LA/attenuated (HAV-O1, C1) · HHV-6 U1102 (HHV6-O1) · HPIV-1 (HPIV1-O1) · HPIV-3 JS (HPIV3-O1) ·
HSV-1 strain 17 (HSV-O1) · HSV-2 HG52 (HSV2-O1) · LCMV (LCMV-O1) · poliovirus Mahoney/Sabin (POL-O1, O3, O4, C1) ·
rabies Pasteur PV (RAB-O1) · reovirus Dearing (REO-O1) · rhinovirus 14 (RHV-O1) · rotavirus SA11 (ROTA-O1) ·
RSV A2 gene-set (RSV-O1) · Semliki Forest (SFV-O1) · SV40 (SV40-O1) · vaccinia Copenhagen (VAC-O1) ·
VSV Indiana composite (VSV-O1) · VZV Dumas (VZV-O1) · canine distemper Onderstepoort/SA (CDV-O1, C2) ·
Zika French Polynesia (ZIKV-C2) · dengue 3 (DEN3-O1)

### `clinical_direct` — 12 events (11%)

human bocavirus (BOCA-O1) · HBV ayw (HBV-O1) · HPV16 (HPV-O1) · HCoV-HKU1 (COV-O4) ·
Merkel cell polyomavirus (MCPYV-O1) · norovirus Norwalk (NOR-O1) · parvovirus B19 (B19-O1) ·
sapovirus (SAPO-O1, C1) · SARS-CoV-2 Wuhan-Hu-1 (COV-O8) · Zika Yap serum (ZIKV-C1) · HPV18 (HPV18-O1)

### `other` — 11 events (10%)

influenza A PR8 eggs (FLU-O1) · influenza B eggs (FLU-B-O1) · yellow fever 17D (YFV-O1) ·
HAV HM-175 wt marmoset (HAV-O2) · HCV chimpanzee plasma (HCV-O1) · HEV cyno (HEV-O1) ·
Marburg Popp guinea-pig (MARB-O1) · Zika MR-766 mouse-brain (ZIKV-O1) · measles Edmonston B clone (MEA-C2) ·
HDV chimpanzee serum (HDV-O1) · variola Bangladesh-1975 eggs/CEF (VAR-O1)

**Summary:** culture-propagated (`culture_cpe` + `culture_no_cpe`) = **86 / 109 (79%)**; `culture_cpe` alone = 39 / 109 (36%).

---

## Bucket 2 — Partially tracked (worth finishing)

These have a **closed sequence path** but an **open stock-origin / lineage / first-principles question**, or a
residual `hop_open_need_pdf` / `could_not_obtain` / abstract-only P-node. They are the natural next move before
the census is airtight. Sorted by the largest unresolved gap.

| Virus (strain) | Sequence path | Open trail | Why it matters | Next move |
|----------------|---------------|------------|----------------|-----------|
| **poliovirus (Mahoney)** | `culture_no_cpe` (HeLa/Baltimore × Enders) | Mahoney ≠ Lansing lineage gap; Enders 1949 is `hop_closed_other` (mouse assay, no CPE) | The type picornavirus genome — is it "produced by culture+CPE" or by culture without CPE + animal assay? | Find the Mahoney stock's own plaque/CPE isolation paper (not Lansing) |
| **vaccinia (Copenhagen)** | `culture_no_cpe` (deposit clone) | `hop_open_need_pdf` — Copenhagen lymph/vaccine history unopened; only lumped plaque-clone warrant | Whether the poxvirus reference is culture+CPE at origin | Lock the Copenhagen derivation cite |
| **HSV-1 (strain 17)** | `culture_no_cpe` (McGeoch) | Brown 1973 closes it `hop_closed_cpe` (plaque×3) — **actually complete**; keep only because the *immediate* score is no_cpe | Reference strain IS a plaque/CPE isolate at stock origin | Complete — downgrade to bucket 1 on next pass (score stays documentary) |
| **RSV (A2)** | `culture_no_cpe` (Stec HEp-2) | Chanock 1957 = Long/Snyder syncytial CPE, **A2 not named** | Syncytial CPE documented at species, not A2 lineage | Find A2's own isolation (A2 = patient Ash 1961?) |
| **HPIV-3 (JS)** | `culture_no_cpe` (LLC-MK2) | Chanock 1958 = Type-1 hemadsorption, **JS not named** | Hemadsorption (not CPE) is the origin warrant; JS lineage gap | Find JS isolate paper |
| **HAV (LA / HM-175)** | `culture_no_cpe` (both) | Provost 1979 CR326 = **no CPE** (IF/IA); LA≠CR326; HM-175 wt marmoset | HAV is the textbook "non-cytopathic" case — the no-CPE culture path is itself the finding | Keep no-CPE out (counterexample visible); no fetch |
| **rabies (Pasteur PV)** | `culture_no_cpe` | Kissling 1958 = HKTC **no CPE**, mouse LD50; PV≠CVS | Fixed rabies grew serially **without** CPE — strong no-CPE case | Keep as no-CPE out; PV lineage gap recorded |
| **BK (MM)** | `culture_no_cpe` (Yang) | Gardner 1971 = B.K. CPE (MK day-18/Vero), **MM≠B.K.** | Culture+CPE at origin but MM is tumor+urine strain | Resolve MM lineage or leave gap noted |
| **VZV (Dumas)** | `culture_no_cpe` (Davison clones) | Weller 1953 = focal CPE + inclusions, **Dumas not named** | CPE+inclusion origin documented at species | Species soft-bar close; leave gap noted |
| **EBV (B95-8)** | `culture_no_cpe` | Miller 1973 = **transformation** (`hop_closed_other`), not monolayer CPE | EBV has no classical monolayer CPE — transformation is its "effect" | No-CPE-class out; documented |
| **AAV-2 (2H)** | `culture_no_cpe` (helper-dependent) | 2H lineage to a named clinical isolate not documented; Ad-helper CPE is the only "effect" | AAV is helper-dependent — can't plaque alone; CPE is the *helper's* | Document as helper-dependent-no-CPE |
| **mumps (Jeryl Lynn)** | `culture_cpe` (plaque from Mumpsvax) | JL is a **vaccine** strain, not the original clinical isolate | The sequenced reference is a vaccine artifact (passage-drifted) | Note vaccine provenance; optional JL derivation fetch |
| **CDV (Onderstepoort)** | `culture_no_cpe` (HeLa spinner) | Onderstepoort is a **vaccine**/lab strain; field CPE is on raccoon C-events | Reference is vaccine lineage | Note; optional Onderstepoort isolation fetch |
| **NDV (LaSota)** | `culture_cpe` (plaque×3 CEF) | LaSota is a **vaccine** strain | Reference = vaccine lineage | Note vaccine provenance |
| **FMDV (O1K)** | `culture_cpe` (plaque×2 BHK) | 1966-67 Kaufbeuren **field isolation** not opened | Plaque documented but first-principles field isolate open | Optional Kaufbeuren isolation chase |
| **CSFV (Alfort)** | `culture_no_cpe` (pig lymphoma) | Explicit "most CSFV grow **without** CPE" (Ruggli) | Textbook no-CPE pestivirus | Keep as no-CPE out; documented |
| **VSV (Indiana composite)** | `culture_no_cpe` (O) / `culture_cpe` (C1 Russell) | First-principles Indiana field-isolation/plaque pedigree not in chain | Composite J02428 reference vs field isolate | Optional field-isolation chase |
| **CHIK (S27)** | `culture_no_cpe` (C6/36) | Ross 1956 = **animal_disease** (baby-mouse lethal), no CPE | Origin warrant is animal, not culture | Documented as animal-out |
| **SV40 (776)** | `culture_no_cpe` (Fiers thin) | Sweet & Hilleman = `culture_cpe` (vacuolation, ≥50% CPE) | Origin IS CPE (vacuolating agent) | Already `hop_closed_cpe` — complete |

*"Keep as no-CPE out" = a documented case where the origin warrant is **not** CPE — these are adversarial
counterexamples to the "everything is culture+CPE" reading, and are retained by design (the `clinical_direct` /
`other` / no-CPE rows stay visible rather than being upgraded or buried), not fetched further.*

---

## Bucket 3 — Not attempted yet (candidate queue)

Named reference viruses with well-defined public reference sequences that have **no** Step 1 event row. These are
the concrete "other viruses we could probe" answer. Candidates are grouped by the family-expansion list's Tier C +
a fresh pass over obvious gaps. Each row is a *proposal*, not yet screened; adding one means opening an O paper and
running the standard chain.

### High-value (named reference viruses, strong paper trail, would expand the denominator meaningfully)

Verified O-paper leads are listed where identified (2026-11-14 search pass). A lead here cuts the next coding
pass to "open Methods → quote → code path_score" (no discovery hunt). Identifiers are from the actual records;
do not guess further ones.

| Virus / strain | Why it matters for P3 | O-paper lead (verified) |
|----------------|-----------------------|-------------------------|
| **variola** (major/minor) | ~~The "eradicated" poxvirus~~ — now done (`other`, egg CAM/CEF) | ✅ **Massung 1994** — DONE 2026-11-18 (`other`, `[VERIFIED src]`) |
| **HTLV-1** (optional, not HIV) | Listed in Tier B but never opened; retrovirus culture path vs clinical | Seiki 1983 PNAS / Yoshida (lock cite before coding) |
| **HPV18** | ~~Only HPV16 done~~ — HPV18 now done (`clinical_direct`) | ✅ **Cole & Danos 1987** — DONE 2026-11-18 (`clinical_direct`, `[VERIFIED src]`) |
| **dengue 4** | ~~Only DEN-2 done~~ — DEN-4 now done (`culture_cpe`) | ✅ **Mackow 1987** — DONE 2026-11-18 (`culture_cpe`, `[VERIFIED src]`) |
| **dengue 3** | ~~Only DEN-2 done~~ — DEN-3 now done (`culture_no_cpe`) | ✅ **Osatomi 1990** — DONE 2026-11-18 (`culture_no_cpe`, `[VERIFIED src]`) |
| **dengue 1** | Same — DEN-1 prototype (Nauru/Hawaii lineage) | lock: original DEN-1 complete genome (Mason-era / Fu 1992) — identifier to verify |
| **human rotavirus (Wa)** | Only simian SA11 done; the human reference group (G1P[8] segment-era composite) | segment-era Wa papers (Both / Flores 1980s); lock the composite O |
| **enterovirus D68** | Modern EV reference; complements EV71/polio/CB3; Fermon strain is the type | Oberste/2014 era; lock the Fermon complete-genome O |
| **adenovirus 7 / 17 / 40/41** | Only Ad2/Ad5 done; Ad7 is in the AAV origin story; Ad17 has a known corrected sequence | Davison/Reddy Ad genomes (lock per type) |
| **measles wild-type (non-vaccine)** | Only Edmonston lineage done — a fresh-patient MV would test vaccine-drift vs clinical | any 1990s+ wt MV O |
| **rubella RA27/3** | Only Therien done; the vaccine reference | vaccine-seed O |
| **mumps Urabe / non-JL** | Non-JL mumps reference | Urabe AM9 lineage |
| **Ebola Kikwit / Makona** | Only Mayinga (1993) done; 2014 Makona is the modern reference | Gire 2014 Science / Baize (lock) |
| **Marburg Musoke/Ravn** | Only Popp done | comparison strains |
| **VZV (Oka vaccine)** | Only Dumas done; Oka vaccine reference | vaccine O |
| **SARS-CoV (Sin3408 / other)** | Tor2/Urbani done; additional prototype isolates | 2003-04 isolates |
| **influenza C / D** | A/B done (eggs); C/D reference genomes untouched | segment-era papers |
| **norovirus GII.4** | Only Norwalk GI prototype done | modern GII.4 O |
| **sapovirus full-length prototype** | Only 3′ partial done (SAPO-O1) — a full-length O missing | newer WGS |
| **EV-A71 other genotypes** | Only BrCr (A) + C-events; full modern B/C genotype references | modern EV71 WGS |

### Lower-value / optional (fill-in, veterinary, arthropod, obscure serotypes)

- **HSV other type strains** (KOS, McKrae, etc.)
- **alphaherpesviruses** (BHV-1, EHV-1, PRV)
- **pestivirus** (border disease, BVDV-2)
- **calicivirus** (RHDV, norovirus animal)
- **arbovirus expansions** (dengue all serotypes, JEV, TBEV, Kunjin)
- **hemorrhagic-fever arenaviruses** (Junin, Machupo, Guanarito)
- **bunyaviruses** (RVFV, CCHFV, SFTSV, hantavirus New-world)
- **paramyxoviruses** (PIV-2/4, MuV non-JL, morbillivirus CDV/hot others)
- **picornaviruses** (EVD68, EV-A/C all, rhino non-14, hepatitis A other)
- **hepadnaviruses** (HDV is helper; avian DHBV)
- **flaviviruses** (all four dengue + JEV + TBEV + Kunjin/WNV other lineages)

### Low-hanging fruit (verified OA identifier + rich Methods; code in one pass)

Ranked by (a) O paper already verified with PMID/DOI, (b) OA full text available or trivially fetchable,
(c) Methods will state the culture/CPE-or-clinical path unambiguously. These are the *first* things to pick up.

| # | Virus | O paper (verified) | Status |
|---|-------|--------------------|--------|
| 1 | **HSV-2 HG52** | Dolan 1998 (PMID 9499055; OA PMC109494) | ✅ **DONE** — `culture_no_cpe` (`[VERIFIED src]`, 2026-11-14) |
| 2 | **metapneumovirus 00-1** | van den Hoogen 2001 (PMID 11385510; OA) | ✅ **DONE** — `culture_cpe` (`[VERIFIED src]`, 2026-11-14) |
| 3 | **HDV** | Wang 1986 Nature (PMID 3762705) | ✅ **DONE 2026-11-18** — `other` (chimpanzee serum; OCR `[VERIFIED src]`) |
| 4 | **HPV18** | Cole & Danos 1987 (PMID 3039146) | ✅ **DONE 2026-11-18** — `clinical_direct` (`[VERIFIED src]`) |
| 5 | **dengue 4** | Mackow 1987 (PMID 3039728) | ✅ **DONE 2026-11-18** — `culture_cpe` (plaque ×2; `[VERIFIED src]`) |
| 6 | **dengue 3 (H87)** | Osatomi 1990 (PMID 2345967) | ✅ **DONE 2026-11-18** — `culture_no_cpe` (C6/36; `[VERIFIED src]`) |
| 7 | **variola Bangladesh-1975** | Massung 1994 (PMID 8184534) | ✅ **DONE 2026-11-18** — `other` (egg CAM/CEF; OCR `[VERIFIED src]`) |

**Partial-trail quick wins (Bucket 2):** the single cleanest is **vaccinia Copenhagen** — only the derivation cite is
needed (`hop_open_need_pdf`). Second: **poliovirus Mahoney** — locate the Mahoney stock's own plaque/CPE isolation
paper (the Lansing gap is already recorded).

### Excluded (by protocol constraint — see `P3_step1_protocol.md`)

- **HIV** and **phage** — outside the Step 1 census scope (protocol constraint: "No phage. No HIV (unless Albert lifts the park)."). These are not candidates in this board.

---

## How to use this board

1. **Adding a new virus:** open its O paper → build the chain per `P3_step1_protocol.md` → add a row to
   `P3_sequence_origin_events.csv` (and a `family_*.md`) → move it from Bucket 3 to Bucket 1 or 2 here.
2. **Finishing a partial trail:** chase the "Next move" in Bucket 2 → when the lineage/gap is closed (or
   explicitly recorded as a soft-bar gap that stays), move it to Bucket 1.
3. **The census numbers** (`P3_step1_progress_summary.md`, `P3_step1_path_type_map`) are re-derived from the
   CSVs, not hand-edited here. When a bucket moves, the counts change and should be reconciled there too.
4. **Adversarial discipline:** `clinical_direct` / `other` / no-CPE rows are **kept visible**, not upgraded or
   buried. The P3 payload is the *distribution*, not a claim that everything is culture+CPE.

---

## Current tallies (2026-11-18, from Step 1 CSV)

| Stat | Value |
|------|-------|
| Virus families with ≥1 event | ~66 (`family_*.md` sheets) |
| Step 1 O/C events | 109 (all `chain_closed`; HDV closed 2026-11-18) |
| `culture_cpe` / `culture_no_cpe` / `clinical_direct` / `other` | 39 / 47 / 12 / 11 |
| Culture-propagated (cpe ∪ no_cpe) | 86 / 109 (**79%**) |
| Partially-tracked rows (bucket 2) | 18 (HDV removed → closed) |
| Not-attempted candidates (bucket 3, high-value) | 14 named + a lower-value list (4 closed this push: HPV18, dengue 3/4, variola) |

*(Sequence-provenance (Step 1) and same-stock re-sequencing (A3) are **separate probes** and are tracked in
separate files. This board covers Step 1 provenance only.)*