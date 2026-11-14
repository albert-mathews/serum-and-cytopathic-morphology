# Gen2P3 handover — C150 under-determination literature search

**From:** general agent (Gen) → **To:** P3 agent
**Date:** 2026-11-14
**Reason:** The "search more / expand the wishlist / statistical signal for C150" prompt was meant for the
P3 agent but was answered here by accident. This file hands the findings and artifacts over so P3 owns and
completes the thread per stream discipline.

**Do not re-fetch or re-search what is already here.** Pick up from "Remaining work" at the bottom.

---

## 1. What C150 is (for context)

C150 (Conjecture, `CLAIMS.md`): the under-determination of culture±CPE Isolates is **detectable in the
published viral-genetics literature** — passage/provenance ambiguity, re-sequencing divergence, assembly
disagreement, retracted/corrected deposits, and contamination mistaken for discovery, i.e. "the field
already found it and published it, framed as technical noise." C151 (non-determinism *papers over* the
ambiguity) is **rejected** (C080 / P7-014: the detection layer is reproducible even blinded), so this thread
is C150-only.

## 2. What was already there before this accidental pass

- `sequence_origins/P3_C150_ambiguity_search_2026-11-12.md` — initial title/abstract sweep (Buckets 1–5),
  XMRV / MLV-in-CFS / PHV-NIH-CQV, prior-art pointers.
- `sequence_origins/P3_A3_same_stock_resequencing_2026-11-13.md` + `.csv` + `P3_A3_pdf_wishlist.md` —
  18 same-stock correction/divergence cases (the culture+CPE-scoped C150 probe).

## 3. What this pass added

### 3a. At-scale quantification (the "statistical signal" you asked for)

These are **published, database-wide counts** — not anecdotes. All identifiers locked from Europe PMC
records (PMID + DOI), never guessed:

| Source | Identifier | Documented quantity | OA |
|--------|-----------|---------------------|-----|
| Steinegger & Salzberg 2020, *Genome Biol* 21:115 | PMID 32398145 · DOI 10.1186/s13059-020-02023-1 | **>2,000,000 contaminated GenBank entries** | PMC7218494 |
| Astashyn et al. 2024 (FCS-GX), *Genome Biol* 25:60 | PMID 38409096 · DOI 10.1186/s13059-024-03198-7 | NCBI screened **1.6M assemblies → 36.8 Gbp contamination (0.16% of bases)** | PMC10898089 |
| Chen et al. 2022, *mSystems* 7:e00907-22 | PMID 36286492 · DOI 10.1128/msystems.00907-22 | **766 nt + 276 aa problematic viral sequences; 85.5% chimeric** | PMC9765019 |
| Lamperti et al. 1992 (via Chorlton) | — | vector contamination in **0.23%** of GenBank sequences | — |
| Cornet et al. 2018 (via Chorlton) | — | chimeric contigs in **≥0.5%** of cyanobacterial assemblies | — |
| Chorlton 2024, *Front Bioinform* 4:1278228 (umbrella) | PMID 38560517 · DOI 10.3389/fbinf.2024.1278228 | "Ten common issues with reference sequence databases" | PMC10978663 |

### 3b. Three canonical "de-discovery" retractions (already in the 11-12 note, identifiers re-confirmed)

- Urisman 2006 XMRV (PMID 16609730) — **retracted**.
- Lo 2010 MLV-related in CFS (PMID 20798047) — **retracted**.
- Naccache 2013 PHV/NIH-CQV spin-column origin (PMID 24027301) — OA.
- Synthesis: Delviks-Frankenberry 2012 "de-discovery of XMRV" (PMID 22818188) — OA.

### 3c. Tool/QC literature (detection-at-scale is itself C150 evidence)

- Peng 2026 ViralQC (PMID 42635218 · DOI 10.1093/bioinformatics/btag463) — OA.
- Chin 2025 RVDB (PMID 40548747 · DOI 10.1128/msphere.00286-25) — OA.
- Bolaji & Duggan 2024 Nanopore thresholds (PMID 39159257 · DOI 10.1371/journal.pcbi.1011539) — OA.
- Dovrolis 2021 ZWA chimeric reads (PMID 34370725 · DOI 10.1371/journal.pcbi.1009304) — OA.
- Hegarty 2024 benchmark-informatics caution (PMID 38376167 · DOI 10.1128/msystems.01105-23) — OA.
- Salter 2014 reagent contamination (PMID 25387460) · Laurence 2014 NGS contaminants (PMID 24837716) ·
  Jurasz 2021 viral-metagenomics contamination review (DOI 10.3389/fmicb.2021.745076) — OA.

### 3d. Voucher/type-material transferable analogy

- Carné 2025 tetrapod voucher errors (PMID 40458985 · DOI 10.1111/mec.17812) — OA.

## 4. Files this pass touched (owner: P3 agent)

| File | Status | Notes |
|------|--------|-------|
| `sequence_origins/P3_C150_pdf_wishlist.md` | **created** | 20 rows, every one with locked PMID + DOI + OA/PMC + drop-as filename. OA items wishlisted too (PDF-is-the-source rule). Drop into `p3_genetics/refs/sequence_origins/`. |
| `sequence_origins/P3_C150_ambiguity_search_2026-11-12.md` | **rewritten** | added Bucket 6 (at-scale counts) + "statistical signal" reading + adversarial scope guards. |
| `p3.md` | TODO item 3 + status tick | one dated line added under item 3. |

**Wishlist location answer (the explicit question):** the new C150 wishlist is at
`p3_genetics/sequence_origins/P3_C150_pdf_wishlist.md` (NOT in `P3_pdf_catalogue.md`, which is the Step 1
holdings catalogue). A3's separate wishlist is `p3_genetics/sequence_origins/P3_A3_pdf_wishlist.md`.

## 5. Adversarial scope guards (carry these forward)

- Steinegger & Salzberg 2020 **explicitly excluded viruses** from the >2M scan — cross-kingdom, not
  viral-specific. **Chen 2022 (766/276/85.5%) is the viral-specific number.**
- XMRV / MLV-in-CFS / PHV are metagenomic–clinical, one step outside culture±CPE; they are C150 evidence
  (contamination mistaken for discovery) but **not** culture+CPE-inheritance evidence. A3 is the
  culture+CPE-scoped probe.

## 6. Remaining work (P3 agent, in priority order)

1. **Fetch OA PDFs** from `P3_C150_pdf_wishlist.md` (owner fetch) → read → tag `[VERIFIED src]`; pin the
   exact sentences (Chen 766/276/85.5%; Astashyn 1.6M/36.8 Gbp; Steinegger >2M; DuPai McWhite passage
   ambiguity proportion).
2. **Read the three de-discovery retraction notices** (XMRV retraction, Paprotka, Naccache) — the hard C150
   propositions.
3. **Add read sources to the two P3 bibliographies** (`P3_sequence_origins_bibliography.md` = used;
   `P3_sequence_origins_read_but_unused.md` = read-but-set-aside).
4. **C150 upgrade decision with Albert** — whether C150 moves from Conjecture to Observation/Lemma in
   `CLAIMS.md` (per claim rules: keep the ID, change kind + status).

## 7. Normative notes for P3 agent

- This thread is C150-only (C151 rejected). Keep evidence tags house-standard (`[VERIFIED src]` only after
  reading the actual PDF; title/abstract quantities stay `[DATA REQUIRED]`).
- Do not let these materials drift into anti-virology framing; they are "the field's own quality-control
  findings," which is the whole point of C150 ("detectable, published, framed as noise").

*End of handover.*