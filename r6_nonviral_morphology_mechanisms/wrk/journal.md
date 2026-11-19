# R6 working journal

**Role:** Founding record and live working notes for the r6 non-viral-mechanism stream. Paper text stays in
`tex/` and `r6.md` Snippets; this file is where the *how/why/what-next* lives.

## Founding (2026-11-17)

**Trigger.** `r6.md` was scaffolded as "not started — awaiting the R6 agent," with a directive to develop, from
the cell-biology literature and the CRO data, the **mechanisms by which CPE-like morphology and plaques form
under the no-virus assumption.** Explicit guardrail: R6 is the no-virus explanation developed on its own terms,
**not** a claim that no infectious agent exists (AX011), and it must **never** state or insinuate that the
CPE/plaque methods are validated.

**Relation to siblings.** R5 (`r5_precell_virus_purification_census/`) had explicitly flagged this object and
tabled it: *"Point 8 — alternative (non-viral) mechanisms of plaque/CPE formation … its natural home is an
R3/CRO extension or a new R6 stream."* R6 is that home. Two R5 inferences land directly in R6: (1) the plaque
assay is **CPE under an overlay** (a countable zone of cell death), not a distinct, more-validating endpoint; and
(2) "permissive lines grew a vast range" is, on the paper's own thesis, a census of which lines degenerate under
the standard serum-drop protocol. Both are held in `R6_mechanisms.md` framing.

## The question, precisely

> Assume the inoculum held no virus / no disease-causing agent. By what cell-biological mechanisms do focal
> cell rounding, detachment, granularity, vacuolation, and countable zones of death (plaques) actually form —
> and what predicts their size, shape, timing, and serum dependence?

## What "develop the no-virus explanation" requires

1. An **enumerated mechanism list** (done: `R6_mechanisms.md`, R6-M1…R6-M12), each with a literature warrant and
   a **distinguishing prediction** testable against the CRO/Zenodo record + CLSI Table 7.
2. **Primary full-text** backing per mechanism, `[VERIFIED src]`, with the cell-line caveat stated (e.g.
   Vander Heiden is IL-3-line; the Vero-specific primaries to fetch are Mendonça 2009, Genari 1998, Engelhardt
   & Mao 1977, Quesney 2001, Nahapetian 1986, Peng 2026).
3. The **"one plaque = one particle" step characterized as assumption vs demonstration**, from primaries
   (Dulbecco 1952; Fenner chapter; Abedon & Yin; Cooper 1984).
4. Evidence tags per CONVENTIONS §3 throughout; abstract-only sources → wishlist, tagged `[DATA REQUIRED]`.

## Anchor facts (re-read first)

- OB024/OB025: CPE-type terms 1/9 (A, 10% FBS) vs 10/13 (B, 2% FBS); B terms rounded(8), dying cells(7),
  granularity(6), vacuolation(4), detached(2), refractile(1). Raters score more CPE in B.
- **OB082 (added 2026-11-17):** neither CRO culture exceeded ~80% confluence → post-confluent degeneration
  (R6-M3) is *excluded* as an explanation; serum/nutrient withdrawal (M1/M2) strengthened.
- CLSI M41 Table 7 descriptors (ten): rounded, ballooned/enlarged, syncytia, vacuolation, detachment,
  granularity, refractile, cytoplasmic strands, **nonspecific degeneration**, no CPE. The field's own table
  includes "nonspecific degeneration" — degeneration is acknowledged to be non-specific.
- VI117 (Deig/Rie/Watkins 1970): stored uninfected monolayers in 1–2% FCS visibly round/degenerate/detach over
  days-weeks with no virus; the authors frame it as cell-viability loss, but the morphology is CPE-adjacent.

## Immediate next steps

- [ ] Albert drops `R6-0xx` PDFs into `refs/`; assistant confirms + removes wishlist rows.
- [ ] Round 2 systematic per-mechanism queries (plan in `R6_research.md` §6).
- [ ] Fetch+read Dulbecco 1952, Cooper 1984, Abedon & Yin 2009 → characterize the plaque step.
- [ ] Hunt R6-M5 (bystander/secondary-necrosis wave) primary — currently `[DATA REQUIRED]`, the gap that matters
      most for the "focal plaque without virus" claim.
- [ ] Freeze → `R6_synthesis.md` → add/update claims in `CLAIMS.md` (CNJ059 seeded) → back Discussion wording.

## Round 1 close (2026-11-17, same session)

- **Confluence correction (OB082).** Albert: in the CRO experiment *neither* Path A nor Path B exceeded ~80%
  confluence. → post-confluent degeneration (R6-M3, from Ammerman 2008) is **excluded** as an explanation of
  the CRO result; serum/nutrient withdrawal (M1/M2) strengthened. Recorded in `CLAIMS.md` OB082 + `R6_mechanisms.md`.
- **Off-limits rule.** Albert added a hard rule that two named external control-experiment sources (and the
  self-published writeup they sit alongside) are off limits — not references, not read/consulted/searched. Rule
  recorded in the gitignored `grok_guardrails.md`; every trace of those sources was removed from R6 tracked
  files (bibliography, screened CSV, search log).
- **Fetch.** 13 of 15 wishlist PDFs dropped (into `r5_…/refs/` by mistake) → moved to
  `r6_nonviral_morphology_mechanisms/refs/`, confirmed against title/authors/id, rows removed from the wishlist.
  Still missing: **R6-007** (Nahapetian 1986) and **R6-014** (Mycoplasmas in tissue culture 1966).
- **Metadata corrections on confirm:** R6-004 = Mendonça et al. *Acta Microscopica* 2009 (not "ReTO 2015");
  R6-005 = Genari et al. 1998 (not "Miranda"); R6-006 = Engelhardt & Mao 1977; R6-013 = Lopes et al. *Braz J Biol*
  2021; R6-016 = Quesney et al. 2001; R6-018 = Baer & Kehn-Hall *J Vis Exp* 2014; R6-019 = Neupane & Bai.
- **Extracted (read, `[VERIFIED src]`):** Dulbecco 1952 (OCR'd), Mendonça 2009, Quesney 2001, Abedon & Yin 2009,
  Neupane & Bai 2024 → `_notes/` + `R6_useful.csv`. The two framing points in `R6_mechanisms.md` now carry the
  precise Dulbecco dilution-linearity argument (not "theoretical equivalence") and the Abedon & Yin
  "plaque-formation-failure ≠ virion-inviability" fact. `CNJ059` updated to match.
- **Next in-queue reads:** Cooper 1984 (R6-010), Oaks 1985 (R6-011), Engelhardt & Mao 1977 (R6-006),
  Genari 1998 (R6-005), Lopes 2021 (R6-013), Uphoff & Drexler 2002 (R6-015), Peng 2026 (R6-017),
  Baer & Kehn-Hall 2014 (R6-018). Plus the R6-M5 bystander-wave hunt (still `[DATA REQUIRED]`).

## Provisional synthesis lives in `R6_mechanisms.md` (single source of truth).

## Round 2 (2026-11-18)

- **R6-006 / R6-014 (Albert's fetch questions).** R6-006 (Engelhardt & Mao 1977) is **already fetched** in
  `refs/` — no fetch needed. R6-007 (Nahapetian 1986) and R6-014 (Macpherson 1966, "Mycoplasmas in tissue
  culture", *J Cell Sci* 1(2):145–168) are **both non-critical**: M1/M2 are already Vero-anchored (Quesney,
  Mendonça, Engelhardt), and M8 is already anchored (Lopes 2021, Uphoff 2002, Ammerman 2008). R6-014's full
  citation is now resolved (wishlist carries it).
- **Processed all 8 remaining fetched PDFs** (R6-005/006/010/011/013/015/017/018) → `_notes/R6_processed_items.md`;
  bib + `R6_useful.csv` updated (all `[VERIFIED src]`).
- **M5 closed.** Internet hunt surfaced the bystander/secondary-necrosis-wave literature: R6-020 Riegman 2019
  (ferroptosis "spread[s] between cells in a wave-like manner, eliminating entire cell populations") and
  R6-021 Cheng & Ferrell 2018 (apoptosis "initiates at a single discrete focus… and then spreads"), both read in
  full. Underlying primaries R6-022…R6-026 (Garcia-Perez 2012 ROS wave; Linkermann 2014; Kim 2016; Pacher &
  Hajnóczky 2001; Tang 2026) logged on the wishlist as optional upgrades.
- **New synthesis chain** added to `R6_mechanisms.md`: serum step → ↓ cystine/GSH → lipid-ROS → ferroptosis-capable
  → propagative wave (M5), plus the apoptotic focus-and-spread and Vero-specific apoptosis/autophagy/adhesion
  branches. This is the single M1/M2→M10→M6→M5 story that explains the CRO signature with no virus (OB024/OB025,
  OB082 sub-confluence).
- **Blocked on:** nothing further (Round-2 sources found openly). Optional remains: fetch R6-022…026 primaries
  + R6-007/014 (non-critical).

*End of journal (Round 2).*

## Round 2b (2026-11-19) — R6-M5 primaries fetched & read

- **Albert dropped R6-022…R6-026** into `refs/`. All five confirmed (title/authors/ID), read in full
  `[VERIFIED src]`, recorded in `_notes/R6-M5_ferroptosis_wave_primaries.md` + `R6_useful.csv`; wishlist rows
  removed; `R6_bibliography.md` statuses `pending → read`; `R6_mechanisms.md` M5 upgraded to primary-backed at
  both spatial scales.
- **Two scales now distinct in the M5 evidence:** *intracellular* relay (Pacher & Hajnóczky 2001 mitochondrial
  waves; Garcia-Perez 2012 Bid→cyto *c* ROS wave) and *intercellular* wave (Linkermann 2014 cell-to-cell tubular
  ferroptosis; Kim 2016 "propagate[s] from cell to cell in a wave-like manner… unlike… apoptosis"; Tang 2026
  multiscale perspective). Corrected the wishlist's "intercellular" tag on R6-022 (it is *intermitochondrial*).
- **M1→M5 bridge now primary/perspective-backed:** serum step-down → ↓cystine (system xc⁻)/GSH → lipid-ROS →
  ferroptosis-capable → propagative wave, with Kim 2016 (amino-acid deprivation + GSH depletion) and Tang 2026
  (starvation lowers the propagation threshold) naming the nutrient/glutathione trigger explicitly.
- **Devil's-advocate (kept honest):** Tang 2026's own caution — spatial clustering ≠ causal propagation; three
  criteria (spatially-defined initiation site, mechanistic continuity, ferroptosis specificity); and wave geometry
  best-documented in *confluent* monolayers. The CRO was ~80% sub-confluent, so the R6-M5 claim leans on the
  serum-dose (2% vs 10%) differential and the M1/M2 metabolic trigger, not on confluency per se.

*End of journal (Round 2b).*
