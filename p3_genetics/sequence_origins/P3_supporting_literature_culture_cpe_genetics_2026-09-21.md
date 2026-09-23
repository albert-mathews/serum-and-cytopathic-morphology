# P3 supporting literature — culture/CPE isolate practice ↔ genome provenance (2026-09-21i)

**Purpose.** Tier A–B cites that buttress Step 1’s framing: (a) culture ± CPE as an operational isolate warrant in virology practice; (b) genetics/databases inheriting isolate/culture material; (c) influenza passage / metadata / MIUViG-style source labeling. Real papers only. Short paraphrases — not advocacy.

**Companion:** `P3_prior_art_genome_provenance_critiques_2026-09-21.md` (prior-art gap map). This file densifies practice + standards cites for the culture+CPE→genome census.

---

## A. Culture / CPE as operational isolate warrant

| ID | Cite | Paraphrase |
|----|------|------------|
| A1 | **Leland DS, Ginocchio CC.** Role of cell culture for virus detection in the age of technology. *Clin Microbiol Rev.* 2007;20(1):49–78. **PMID 17223623**; **DOI 10.1128/cmr.00002-06**; PMC1797634. | Classic review: virus isolation in cell culture long treated as diagnostic “gold standard”; CPE (rounding, syncytia, monolayer destruction, etc.) is the standard microscopic readout of viral proliferation, though confirmatory ID is still required. |
| A2 | **ASM MicrobeLibrary / laboratory teaching protocols** — “Cytopathic Effects of Viruses” (ASM protocol PDF). | Teaching/lab definition: morphological CPE = cytopathogenic virus; notes that some viruses produce little/no visible CPE and need hemadsorption, interference, antigen, or nucleic-acid detection instead. |
| A3 | **CLSI M41** — *Viral Culture* (CLSI document M41; 2006 era guidance). | Standards-body guidance for clinical viral culture: cell-line selection/QC, specimen prep, isolate detection/identification, and reporting — institutionalizes culture-based isolate workflows. |
| A4 | **Enders JF, Peebles TC.** Propagation in tissue cultures of cytopathogenic agents from patients with measles. *Proc Soc Exp Biol Med.* 1954;86:277–286. (classic; often cited without modern DOI). | Foundational measles isolation: “cytopathogenic agents” from clinical material in human/monkey kidney — CPE as the isolate warrant that later seed stocks (Edmonston lineage) inherit. |
| A5 | Historical CMV/adenovirus isolation literature (e.g. **Rowe et al. 1956** adenoidal cytopathogenic agents; Towne/AD169 strain histories summarized in modern resequence papers such as Bradley et al. 2009 JGV). | Laboratory strains used for defining herpesvirus genomes are historically fibroblast-passaged cytopathogenic isolates; sequence papers often omit restating CPE when stock identity is assumed. |

---

## B. Genetics / databases inheriting isolate or culture material

| ID | Cite | Paraphrase |
|----|------|------------|
| B1 | **Roux S et al.** Minimum Information about an Uncultivated Virus Genome (MIUViG). *Nat Biotechnol.* 2019;37:29–37. **PMID 30556814**; **DOI 10.1038/nbt.4306**. | GSC checklist for UViGs; mandatory `source_uvig` enumerates dataset origin including “isolate microbial genome” vs virome/metagenome paths — community acknowledgment that source type must be declared. |
| B2 | **Adriaenssens EM et al. / GSC follow-ons** — Guidelines for public database submission of uncultivated virus genome sequences for taxonomic classification. *Nat Biotechnol.* 2023 (see PMID **37430074**; **DOI 10.1038/s41587-023-01844-2**). | Updates submission expectations for uncultivated virus genomes; reinforces isolate vs uncultivated reporting discipline in public DBs. |
| B3 | **GSC MigsVi / MIxS virus checklist** — https://genomicsstandardsconsortium.github.io/mixs/0010005/ | Minimal contextual metadata for virus genome sequences (cultured-virus MIGS path complementary to MIUViG). |
| B4 | **ENA ERC000033** virus pathogen reporting checklist; NCBI BankIt source modifiers (`isolation_source`, `lab_host`, `culture_collection`, `specimen_voucher`). | Pathogen/surveillance deposit fields exist for isolate/culture context; completeness and CPE axes remain uneven (see prior-art file). |

---

## C. Influenza passage / metadata / source labeling (transferable lesson)

| ID | Cite | Paraphrase |
|----|------|------------|
| C1 | **Bush RM et al.** Effects of passage history and sampling bias on phylogenetic reconstruction of human influenza A evolution. *PNAS.* 2000;97:6974–6980. **PMID 10860959**; **DOI 10.1073/pnas.97.13.6974**. | Egg-cultured isolates show excess host-mediated HA mutations on terminal branches — passage history changes the deposited sequence relative to the clinical virus. |
| C2 | **McWhite CD, Meyer AG, Wilke CO.** Sequence amplification via cell passaging creates spurious signals of positive adaptation in influenza virus H3N2 hemagglutinin. *Virus Evol.* 2016;2:vew026. **PMID 27713835**; **DOI 10.1093/ve/vew026**. | Even modest cell passaging (MDCK and others) can create false adaptation signals — deposited “isolate” genomes are not interchangeable with clinical-direct sequences. |
| C3 | **DuPai CD et al.** Influenza passaging annotations: what they tell us and why we should listen. *Virus Evol.* 2019;5:vez016. **PMID 31275610**; **DOI 10.1093/ve/vez016**. | Passage metadata (`lab_host`, GISAID passage history) are inconsistently populated across databases; authors argue for mandatory standardized Egg/Cell/Original labels. |

---

## How these map to P3 Step 1

- **A-series** justify treating documented culture ± CPE/plaque/syncytia as the primary concern path when method↔deposit is adequate (soft evidentiary bar).
- **B-series** show the standards community already separates isolate vs metagenome/UViG sources — Step 1 asks the parallel question inside *named* origin/type deposits: culture±CPE vs clinical-direct vs other.
- **C-series** are the densest empirical precedent that **how the sequenced sample was produced** changes the genetic record; influenza is egg/cell-heavy, but the metadata lesson transfers.

**Not claimed here:** that GenBank is “invalid,” or that culture±CPE genomes are false. Exploration: densify the census of documented production paths behind foundational viral genomes.

## Pass 21j additions (OA culture_cpe → genome exemplars)

| Cite | Why relevant |
|------|----------------|
| Maan et al. 2010 PLoS ONE (BTV-C1) | Blood→KC→BHK with **100% CPE**; genome from culture supernatants — orbivirus culture_cpe exemplar. |
| Coetzee et al. 2020 MRA (BTV-C2) | Vaccine bottle plaque selection on Vero; harvest at advanced CPE → complete genomes. |
| Russell et al. 2019 MRA (VSV-C1) | Vero to **80–90% CPE**; plaque isolates sequenced — rhabdovirus lab-strain CPE→genome. |
| da Costa et al. 2021 Sci Rep (CDV-C3) | VerodogSLAM **syncytia/CPE** → complete field CDV genome (MW460905). |
| Gingeras et al. 1982 JBC (ADE-O2 upgrade) | HeLa/KB culture + **plaque-purified** Ad2 stock for sequenced DNA. |
| Willcocks et al. 1994 JVI (ASTRO-P) | HEK blind passage; **CPE from passage 6** for culture-adapted HAst prototypes (O PDF still missing). |


## Pass 21k additions (OA culture_cpe → genome exemplars)

| Cite | Why relevant |
|------|----------------|
| Marques Antunes de Oliveira et al. 2013 Genome Announc (BVDV-C1) | Plaque-separated Cp/Ncp BVDV-1k pair; Cp RNA from infected turbinate → complete genomes. |
| Toplak et al. 2019 MRA (BVDV-C2) | Cytopathogenic BVDV-1d on BT cells; supernatant RNA → near-complete genome. |
| Palinski et al. 2022 MRA (FMDV-C1) | Agar plaque purification of SAT1 from buffalo OPF → near-complete genomes. |
| Jagtap et al. 2025 MRA (EV71-C2) | RD CPE + double Vero plaque → supernatant RNA → BrCr-like EV-A71 genomes. |
