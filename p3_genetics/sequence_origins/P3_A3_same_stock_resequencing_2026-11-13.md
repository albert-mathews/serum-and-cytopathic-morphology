# P3 A3 — same-stock re-sequencing divergence

**Date:** 2026-11-13
**Status:** Census in progress. Eighteen cases recorded (12 in-house `[VERIFIED src]` + 6 new literature, of which
the Ortigas-Vasquez 2024 flagship is `[VERIFIED src]`); wishlist open for a few identifiers. Systematic scoring of
the full Step 1 O/C pairs is the next step.
**Claim under test:** C150 (Conjecture) — the under-determination of culture±CPE Isolates is *detectable* in the
published viral-genetics literature. A3 is the culture+CPE-specific C150 probe: **when a named stock / Isolate /
accession lineage is re-sequenced years or groups apart, how much do published assemblies differ** (length, gene
content, consensus polymorphisms, "complete genome" boundaries)?

## What A3 is (and why it is the right C150 probe)

A3 was flagged by Albert in `p3.md` ("did we do this research?"). The inheritance logic: if a "viral genome" is a
culture-product consensus rather than a fixed natural particle genome, then re-sequencing the *same named stock*
should produce divergent assemblies. Conversely, tight reproducibility across groups would *constrain* the
culture-consensus reading. So A3 is a direct, culture+CPE-scoped test of C150 — unlike the XMRV/PHV contamination
cases (recorded in `P3_C150_ambiguity_search_2026-11-12.md`), which sit one step outside the P3 scope.

## Method

- Primary source: the Step 1 origin/confirmation corpus (`P3_sequence_origin_events.csv`) — its O and C events are
  already coded for the *same named stocks*, and its `notes` field already quotes several corrections and
  divergences. Reading the full text was already done for Step 1, so these records inherit `[VERIFIED src]`.
- Secondary source: Europe PMC REST API (the `websearch` tool stayed down) for new correction/divergence papers;
  broad keyword queries returned mostly noise, so the census here is in-house-first.
- Data record: `P3_A3_same_stock_resequencing.csv`; wishlist: consolidated stream-root `../P3_pdf_wishlist.md`.

## Divergence types coded

| a3_type | Meaning |
|---------|---------|
| `correction` | A later paper/publication notes the deposited "complete genome" had errors or was incomplete |
| `parallel_divergence` | The same stock was sequenced independently by two+ groups with non-identical results |
| `retraction` | A deposited genome/infectious clone was withdrawn |
| `genome_size_correction` | The reported genome length was corrected after deposit |
| `passage_divergence` | High-passage vs low-passage material of the same lineage diverged |
| `heterogeneity` | The stocked material itself was mixed, and the single consensus hides that |

## Findings (eighteen cases)

Eighteen cases: twelve mined from the Step 1 corpus (already `[VERIFIED src]`) plus six new literature cases
(the flagship Ortigas-Vasquez 2024 is `[VERIFIED src]`; the other five are identified, full text to read):

| id | virus | type | one-line divergence |
|----|-------|------|---------------------|
| A3-001 | CMV AD169 | correction | the deposited "complete" AD169 was missing 929 bp (UL42/UL43) |
| A3-002 | HPV16 | correction | HPV16 reference carries later sequencing-error corrections |
| A3-003 | poliovirus 1 Mahoney | parallel_divergence | three 1981 sequences of the same stock: 7410 vs 7433 nt |
| A3-004 | measles Edmonston | retraction | Cattaneo/Ballart 1990 infectious cDNA retracted 1991 |
| A3-005 | FMDV O1K | genome_size_correction | reported ~7802 nt corrected to ~8450 nt; 7 vs 64 passages |
| A3-006 | SARS-CoV Tor2 vs Urbani | parallel_divergence | twin 2003 first genomes differ in nucleotides |
| A3-007 | CMV AD169 vs Merlin | passage_divergence | high-passage AD169 replaced by low-passage Merlin as wild-type ref |
| A3-008 | CMV AD169 variants | parallel_divergence | varUC vs ATCC AD169 differ in Bradley 2009 |
| A3-009 | Ad2 | heterogeneity | "heterogeneity persists after plaque purification" |
| A3-010 | HCoV-229E Inf-1 vs clinical | passage_divergence | lab-adapted Inf-1 reference vs clinical 0349/J0304 |
| A3-011 | SARS-CoV-2 Wuhan-Hu-1 vs WIV04 | parallel_divergence | two first genomes from different patients/labs |
| A3-012 | CSFV Alfort | parallel_divergence | Alfort (1989) re-sequenced as Alfort/187 (1996) |
| A3-013 | MDV CVI988 + Md5 | intrastrain_variation | same strain: up to 236 pos / 13 ORFs; length 176,532–178,311 bp |
| A3-014 | Ad17 prototype | correction | "a corrected DNA sequence" (Dehghan 2011) |
| A3-015 | adenovirus (Geck ORF) | correction | "four errors in the published sequence" (Jung 1991) |
| A3-016 | AAV2 | correction | "corrected sequence" (Jang 2005) |
| A3-017 | turkey herpesvirus | correction | frameshift error corrected |
| A3-018 | CMV AD169 (UL15A) | correction | further AD169 corrections (Akter 2002) |

## Reading

**Two layers, opposite properties.** The A3 cases separate the viral-genetics toolchain into two layers with
opposite behavior:

- **Detection (PCR/qPCR) is deterministic but non-specific** (C034): reproducible even blinded (C080/P7-014), but
  *primer-driven* — it amplifies whatever nucleic acid matches the primers, viral or not. Detection reliability does
  not earn the "viral" label.
- **Assembly / "complete genome" construction is non-deterministic, and detectably so.** The nine cases split into
  two failure modes:
  1. *Assembly fragility* — the deposited "complete genome" was wrong/incomplete and had to be fixed: CMV AD169
     missing 929 bp (UL42/UL43), HPV16 sequencing-error corrections, measles Edmonston infectious clone retracted
     (Ballart 1990), FMDV size corrected ~7802→~8450 nt.
  2. *Stock drift* — the culture product itself is not a fixed object: CMV AD169 (high-passage) vs Merlin
     (low-passage), AD169 varUC vs ATCC holdings, Ad2 "heterogeneity persists after plaque purification".

**This is C150, not C151.** The assembly non-determinism is *detectable* — the corrections, retractions, and
size-corrections are published, i.e. the field found and fixed the ambiguity. That is exactly what C150 predicts
(under-determination detectable in the literature), not C151 (non-determinism papering over the ambiguity).

**Scope guard:** nine single-stock anecdotes show the *form* of A3 divergence, not its *prevalence*. A prevalence
claim requires a census over many named stocks (next steps).

## Wishlist (see consolidated stream-root `../P3_pdf_wishlist.md`)

1. Cattaneo & Ballart 1990 measles infectious cDNA + 1991 retraction — identifier not yet verified.
2. HPV16 (Seedorf 1985) sequencing-error correction — the specific notice (RefSeq-linked), identifier not verified.
3. Optional: broaden A3 with additional culture-derived "complete genome correction" papers beyond the nine.

## Next steps

1. **Prevalence census (active).** Systematically tabulate the Step 1 O/C pairs (the re-sequencing pairs already
   coded) and score each C event for divergence (correction / parallel / passage / none). This turns the 12
   anecdotes into a rate over the ~19 viruses with O+C events. Design in `p3.md` §A3.
2. Lock the two wishlist identifiers and fetch the retraction/correction notices.
3. Fold the A3 finding into the C150 assessment and decide with Albert whether C150 upgrades in `CLAIMS.md`.
4. Add the new/read sources to the two P3 bibliographies (`P3_sequence_origins_bibliography.md` for used;
   `P3_sequence_origins_read_but_unused.md` for read-but-set-aside).