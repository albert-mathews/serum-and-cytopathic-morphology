# R6 search log

Round-by-round queries, dates, hit counts, decisions. Audit trail; never delete prior rows.

---

## Round 1 — Mechanism framework seed (2026-11-17)

**Operator:** R6 agent session.
**Aim:** Seed the mechanism framework (`R6_mechanisms.md`) from (a) the on-disk CRO/CLSI anchors, (b) full-text
reads already fetchable open-access, and (c) a first web sweep — not conclusions.
**Lead source:** `r6.md` scope + CRO result (OB024/OB025) + CLSI Table 7 (`tex/tables/clsi-table7-descriptors.tex`)
+ the R3-flagged prior art (Deig/Rie/Watkins 1970, VI117, `r1_…/wrk/summaries/VI117_summary.md`).

### Queries run (web search)

1. `serum starvation Vero E6 cells morphology rounding detachment apoptosis growth factor withdrawal`
2. `cell culture monolayer spontaneous degeneration maintenance medium low serum uninfected negative control morphology`
3. `plaque assay agarose overlay mechanism focal cell death diffusion limiting nutrient not virus specific`
4. `mycoplasma contamination cell culture cytopathic effect mimic morphological changes`

### Full texts read in round 1 (open access → `[VERIFIED src]`)

| ID | Source | Verdict |
|----|--------|---------|
| R6-001 | Ammerman 2008 PMC2657228 | **R6-M3** verbatim ("stop growing and start to die" at confluence) + **R6-M8** (mycoplasma invisible/common). |
| R6-002 | Vander Heiden 2001 PMC87309 | **R6-M1** ("abrupt changes… result in cell death"; high-GF-adapted more vulnerable) + **R6-M2** (glucose limitation → same apoptotic pathway). Scope caveat: IL-3 line. |
| R6-003 | Fenner ch.3 PMC7173454 | **R6-M11 + framing** ("each infective particle → localized focus"; "single particle sufficient to form a plaque"; overlay restricts spread; CPE = rounding→pyknosis→detachment; continuous lines aneuploid). |

### Abstract-only leads → wishlist (not yet load-bearing)

R6-004 (Vero nutrient-depletion morphology); R6-005 (Vero nutritional-stress adhesion); R6-006 (Vero serum factor
G2); R6-007 (Nahapetian Vero metabolites); R6-008 (Abedon & Yin plaque theory); R6-009 (Dulbecco 1952);
R6-010 (Cooper 1984); R6-011 (Oaks Shigella plaque); R6-013 (Lopes HEp-2 mycoplasma); R6-014 (Mycoplasmas in
tissue culture 1966); R6-015 (Uphoff mycoplasma eradication); R6-016 (Vero bioreactor serum-free death);
R6-017 (Vero CTGF autophagy); R6-019 (WNV plaque assay — open).

### Mechanism list

Drafted 12 mechanisms R6-M1…R6-M12 in `R6_mechanisms.md` (see that file for the table, predictions, and the two
framing points: (1) "one plaque = one particle" is a stated theoretical equivalence; (2) focal clearing is a
generic diffusion-limited spatial pattern).

### Open threads (Round 2+)

- Fetch R6-004…R6-019 PDFs; confirm matches; remove wishlist rows; extract into `R6_useful.csv`.
- Read Dulbecco 1952 + Cooper 1984 + Abedon & Yin for the plaque "assumption vs demonstration" characterization.
- Get a **Vero-specific** serum-withdrawal morphology primary (R6-004/005/006/016/017) so R6-M1/M2 are not
  carried only by an IL-3-line analogy.
- Hunt primary literature for **bystander / secondary-necrosis wave** (R6-M5) — the focal "plaque" producer —
  currently `[DATA REQUIRED]`.
- Confirm peer-review status of R6-004 (ResearchGate DOI) before any load-bearing use.

---

*Round 2 (systematic per-mechanism queries) not yet run.*
