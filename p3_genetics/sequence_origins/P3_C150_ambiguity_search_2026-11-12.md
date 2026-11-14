# P3 C150 search — under-determination detectable in the viral-genetics literature

**Date:** 2026-11-12 (initial) · Expanded 2026-11-13 (at-scale quantification) · **Verified 2026-11-14** (PDFs fetched, key numbers pinned).
**Status:** 29 PDFs fetched into `p3_genetics/refs/` and title/identifier-verified against the wishlist. The
load-bearing quantities are now `[VERIFIED src]` (exact quotes under "Verified quotes" below). Retracted items
are note-only per CONVENTIONS §8 (never load-bearing); the de-discovery *load* rests on the un-retracted papers
(Paprotka 2011, Delviks-Frankenberry 2012, Naccache 2013) and the retraction notices.
**Claim under test:** C150 (Conjecture, `CLAIMS.md`) — the under-determination of culture±CPE Isolates is
*detectable* in the published viral-genetics literature (passage/provenance ambiguity, re-sequencing
divergence, assembly disagreement, retracted/corrected deposits, contamination mistaken for discovery).
C151 is rejected (see `CLAIMS.md`); this thread looks only for C150.

## Search method

- `websearch` was intermittently available; the workhorse was the Europe PMC REST API
  (`https://www.ebi.ac.uk/europepmc/webservices/rest/search`) — a legitimate source of record — used via
  `webfetch`. Every identifier below is locked from Europe PMC records (PMID + DOI), never guessed.
- **Evidence discipline:** a hit is a *candidate* until its full text is read. Abstract/title quantities are
  quoted as such and stay `[DATA REQUIRED]` until the PDF is read.

## Bucket 1 — contamination mistaken for discovery (the cleanest C150 form)

Documented cases where a claimed "viral genome" was later shown to be contamination or lab reagent, and the
discovery was retracted or reverse ("de-discovery"). **These are the canonical three:**

| Source | Year | Identifier | What happened | Status |
|--------|------|------------|---------------|--------|
| Urisman et al., PLoS Pathog 2:e25 | 2006 | PMID 16609730 · DOI 10.1371/journal.ppat.0020025 | "Novel gammaretrovirus" (XMRV) in prostate tumors | **Retracted** (PubMed `pubType: retracted publication`) |
| Paprotka et al., Science 333:97 | 2011 | PMID 21628392 · DOI 10.1126/science.1205292 | XMRV shown to be a lab recombinant of two mouse endogenous retroviruses | full text to read (paywalled) |
| Lo et al., PNAS 107:15874 | 2010 | PMID 20798047 · DOI 10.1073/pnas.1006901107 | MLV-related sequences in CFS blood | **Retracted** |
| Naccache et al., J Virol 87:11966 | 2013 | PMID 24027301 · DOI 10.1128/jvi.02323-13 | "Novel parvovirus-like hybrid genome" (PHV/NIH-CQV) traced to nucleic-acid extraction spin columns | OA (PMC3807889); full text to read |

De-discovery synthesis: Delviks-Frankenberry et al. 2012 (Curr Opin Virol 2:499, PMID 22818188) —
"Recombinant origin, contamination, and de-discovery of XMRV."

## Bucket 6 (new) — at-scale contamination / chimerism quantification (the statistical signal)

These are *published, database-wide counts* — the field's own quantification that the viral-genetics
reference layer is riddled with contamination, chimerism, and misannotation. This is the direct
"under-determination is detectable" quantity for C150.

| Source | Year | Identifier | Documented quantity | OA |
|--------|------|------------|---------------------|----|
| Steinegger & Salzberg, Genome Biol 21:115 | 2020 | PMID 32398145 · DOI 10.1186/s13059-020-02023-1 | **>2,000,000 contaminated entries** in GenBank | PMC7218494 |
| Astashyn et al. (FCS-GX), Genome Biol 25:60 | 2024 | PMID 38409096 · DOI 10.1186/s13059-024-03198-7 | NCBI screened **1.6M assemblies → 36.8 Gbp contamination (0.16% of bases)** | PMC10898089 |
| Chen et al., mSystems 7:e00907-22 | 2022 | PMID 36286492 · DOI 10.1128/msystems.00907-22 | **766 nt + 276 aa problematic viral sequences; 85.5% chimeric** (668 contaminated viral sequences per Chorlton's citation) | PMC9765019 |
| Lamperti et al. (via Chorlton) | 1992 | — | vector sequence contamination in **0.23%** of GenBank sequences | — |
| Cornet et al. (via Chorlton) | 2018 | — | chimeric contigs in **≥0.5%** of cyanobacterial assemblies | — |
| Chorlton, Front Bioinform 4:1278228 | 2024 | PMID 38560517 · DOI 10.3389/fbinf.2024.1278228 | "Ten common issues with reference sequence databases" — umbrella review | PMC10978663 |

## Bucket 2 — chimeric / contaminated reference entries (prior-art, now identifier-locked)

- Chen et al. 2022 mSystems (above) — 766 nt / 276 aa problematic viral sequences, 85.5% chimeric. Already
  read in `P3_prior_art_genome_provenance_critiques_2026-09-21.md` §B4 (`[VERIFIED src]`).
- Steinegger & Salzberg 2020 (above) — >2M contaminated entries; **viruses excluded** from that scan, an
  important bound on the C150 claim (recorded as a scope note).

## Bucket 3 — assembly hindered by chimerism / contamination thresholds

- Dovrolis et al. 2021 PLoS Comput Biol 17:e1009304 (PMID 34370725 · DOI 10.1371/journal.pcbi.1009304) —
  "ZWA: viral genome assembly and characterization hindrances from virus–host chimeric reads." OA.
- Bolaji & Duggan 2024 PLoS Comput Biol 20:e1011539 (PMID 39159257 · DOI 10.1371/journal.pcbi.1011539) —
  contamination thresholds for Nanopore SARS-CoV-2. OA.

## Bucket 4 — the field built tools to detect the contamination (detection is itself the evidence)

- Peng et al. 2026 Bioinformatics 42(s2):btag463 (PMID 42635218 · DOI 10.1093/bioinformatics/btag463) —
  "ViralQC: completeness and contamination of predicted viral contigs." OA.
- Chin et al. 2025 mSphere 10(7):e0028625 (PMID 40548747 · DOI 10.1128/msphere.00286-25) — "Refinement of
  the Reference Viral Database (RVDB)." OA.
- Astashyn et al. 2024 — FCS-GX (above). Note: the *existence* of a dedicated NCBI contamination-screening
  suite that has removed contaminants at scale is itself C150 evidence — the field treats contamination of
  deposited genomes as a routine, large-scale problem to detect.

## Bucket 5 — voucher / type-material errors (transferable analogy)

- Carné et al. 2025 Mol Ecol 34(13):e17812 (PMID 40458985 · DOI 10.1111/mec.17812) — "In Vouchers We
  (Hope to) Trust: hidden errors in GenBank's tetrapod taxonomic foundations." Viral voucher/type-material
  error census is the P3-scoped mirror; listed as transferable prior art, not a viral result.

## Reading

**Statistical signal for C150.** The literature does not merely contain a few anecdotes of
contamination mistaken for discovery — it contains **database-scale quantifications**:

- >2,000,000 contaminated GenBank entries (Steinegger & Salzberg 2020);
- 1.6M assemblies screened → 36.8 Gbp contamination by NCBI's own FCS-GX (Astashyn 2024);
- 766 nt + 276 aa problematic viral reference sequences, 85.5% chimeric (Chen 2022);
- plus vector contamination in 0.23% of entries already by 1992 (Lamperti 1992).

Combined with the A3 census (18 same-stock correction/divergence cases, `P3_A3_same_stock_resequencing.csv`)
and the three canonical "de-discovery" retractions (XMRV, MLV-in-CFS, PHV/NIH-CQV), this is the "already
published, framed as technical noise" pattern that C150 predicts. The field itself runs a national
contamination-screening program (FCS-GX) and a dedicated virome-QC tool literature (ViralQC, RVDB, ZWA).

**Scope guards (adversarial, kept visible):**
- Steinegger & Salzberg 2020 *explicitly excluded viruses* from their contamination screen — so their >2M
  figure is cross-kingdom, not viral-specific. Chen 2022 (766/276, 85.5%) is the viral-specific quantity.
- XMRV / MLV-in-CFS / PHV are metagenomic–clinical de-discoveries, one step outside the culture±CPE scope;
  they are C150 evidence (contamination mistaken for discovery) but not culture+CPE-inheritance evidence.
  The culture+CPE-scoped C150 probe is A3 (re-sequencing divergence/corrections).

## Verified quotes (fetched + read 2026-11-14, `[VERIFIED src]`; codes internal-only)

At-scale quantification:

- **P3-006 Chen et al. 2022** (mSystems 7:e00907-22): "a total of **766 nucleotide** PVSs and **276** [amino-acid
  PVSs]" … "They were either full-length sequences (14.5%) or **chimeric fragments (85.5%)**" — problematic
  viral sequences (PVSs) from 39 viral families, classed into misclassification / vectors / LCD / hosts.
- **P3-008 Astashyn et al. 2024** (Genome Biol 25:60, FCS-GX): "We used FCS-GX to screen **1.6 million GenBank
  assemblies** and identified **36.8 Gbp of contamination, comprising 0.16% of total bases**, with half from
  161 assemblies." … "We updated assemblies in NCBI RefSeq to reduce detected contamination to 0.01%."
- **P3-007 Steinegger & Salzberg 2020** (Genome Biol 21:115): "Our analysis reports contamination of **2,161,746**
  [entries]" — title: "Terminating contamination: large-scale search identifies more than 2,000,000 contaminated
  entries in GenBank." (Viruses explicitly excluded from that scan — see scope guard.)

De-discovery (contamination mistaken for discovery):

- **P3-004 Naccache et al. 2013** (J Virol 87:11966): the parvovirus-like hybrid genome's "exact origin … was
  eventually traced to **contaminated silica-binding spin columns** used for nucleic acid extraction."
- **P3-002 Paprotka et al. 2011** (Science 333:97): XMRV "was **generated by recombination of two proviruses** during
  tumor passaging in mice."
- **P3-005 Delviks-Frankenberry et al. 2012** (Curr Opin Virol 2:499): "XMRV-positive patients were due to
  **contamination with mouse DNAs, XMRV plasmid DNA**…" — "de-discovery of XMRV."

Passage/provenance ambiguity:

- **P3-016 McWhite et al. 2016** (Virus Evol 2:vew026): "passaging leaves **distinct signals of adaptation, which can
  confound evolutionary analyses** of the viral sequences."

Retracted (note-only per CONVENTIONS, never load-bearing — axis RETRACTED):

- **P3-001** Urisman 2006 (XMRV discovery) — RETRACTED; the retraction event is established by PubMed `pubType: retracted`
  and by the de-discovery papers (P3-002 / P3-005), not by the retracted content.
- **P3-003** Lo 2010 (MLV-related in CFS) — RETRACTED (same).
- **P3-021** Ballart 1990 measles infectious clone (A3) — RETRACTED (P3-022 Eschle 1991 retraction notice).

## Next steps

1. ~~Fetch OA PDFs + pin exact quantitative sentences~~ — **done 2026-11-14** (29 PDFs verified; key quantities pinned `[VERIFIED src]` above).
2. Add the fetched C150/A3 sources to the two-bib structure (`P3_sequence_origins_bibliography.md` = used; `_read_but_unused.md` = read-but-set-aside) with `RETRACTED` labels where applicable.
3. ~~Read the de-discovery papers~~ — **done** (Paprotka, Naccache, Delviks read; retracted Urisman/Lo treated as note-only).
4. **C150 upgrade decision with Albert** — whether C150 moves Conjecture → Observation/Lemma, scoped to "detectable" (existence), not "prevalent" (rate).

## Bibliography (two-bib discipline)

- **Used** (`P3_sequence_origins_bibliography.md`): add once full texts are read.
- **Read but unused** (`P3_sequence_origins_read_but_unused.md`): add if a candidate is read and set aside.
- Wishlist: consolidated stream-root `../P3_pdf_wishlist.md`.