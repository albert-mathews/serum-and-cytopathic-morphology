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
- **Off-limits rule.** Albert: the control experiments of Dr. Stefan Lanka and of the Virology Control Studies
  Project (Jamie Andrews) are **off limits** — not references, not read/consulted/searched. Rule recorded in
  the gitignored `grok_guardrails.md`; any trace removed from R6 tracked files (a Substack item + a Lanka
  preprint had been logged as "encountered-excluded" in Round 1; both scrubbed).
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

*End of journal (Round 1).*
