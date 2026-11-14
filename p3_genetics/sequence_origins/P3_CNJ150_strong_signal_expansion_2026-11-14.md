# P3 CNJ150 — strong-signal corpus expansion (same-strain re-sequencing → inconsistent consensus)

**Date:** 2026-11-14 · **PDFs fetched + read 2026-11-14** (all `[VERIFIED src]` below).
**Purpose:** Expand the corpus that supports the *strongest* items in the P3.v1 prediction list
(`../p3.md` §P3.v1): item 1 (same-strain re-sequencing → inconsistent consensus, Ortigas-Vasquez type)
and item 2 (assembly fragility / corrected deposits, DEF005). These two items are the field-specific
core of CNJ150 — the deposited "reference genome" of a named, culture-derived stock is repeatedly shown
to be non-unique, wrong, or a single haplotype of a mixed population.

**Method:** `websearch` + Europe PMC REST (identifier lock), then full-text extraction (PyMuPDF via shared
venv) against the fetched PDFs. Every PMID/DOI below was verified against a Europe PMC core record, not
guessed. All quantitative claims in "Verified quotes" are `[VERIFIED src]` (read from the fetched PDF).
No retracted items below.

---

## A. Same-stock / same-strain re-sequencing divergence (item 1 — strongest)

The single strongest P3.v1 signal. The Szpara-lab / alphaherpesvirus-genomics thread documented that the
"reference genome" is one haplotype of a mixed, passage-drifted population, and that re-sequencing the
*same named strain* yields an inconsistent consensus. This expands the P3-030 … P3-037 thread with
additional verified cases across HSV-1, PRV, and the HPV reference-clone errors.

### HSV-1 (the reference strain 17 thread)

| Code | Source | Year | Identifier | Finding ([VERIFIED src]) |
|------|--------|------|------------|---------------------------------------|
| P3-040 | **Parsons et al., mBio 6:e02213-14** | 2015 | PMID 25827418 · DOI 10.1128/mbio.02213-14 · PMC4453532 | VirGA intrastrain assembly: KOS Large/Syncytial/Hypersyncytial subclones are 99.5% identical at DNA level; F Large/Syncytial 98.6%; syncytial variants share an identical gB (UL27) tail mutation. OA. |
| P3-041 | **Renner et al., Microbiol Resour Announc 10:e01146-19** | 2021 | PMID 33766904 · DOI 10.1128/MRA.01146-19 · PMC7996463 | HSV-1 McKrae "at least two widely used variant strains": prior McKrae stocks (JQ730035, JX142173, MN136524) *disagree in key genes*; UL56 ORF truncated in some lab stocks, full-length in others. OA. |
| P3-042 | **Bowen et al., Virology 492:179** | 2016 | PMID 26950505 · DOI 10.1016/j.virol.2016.02.013 · PMC5056906 | "Viral forensic genomics": KOS63 and KOS79 (both "attributed to the same source individual") are *genetically unrelated* strains; "reiteration lengths in several published strains are artificially matched to strain 17." Free (authored/manuscript). |
| P3-043 | **Bowen et al., J Virol 93:e01824-18** | 2019 | PMID 30760568 · DOI 10.1128/JVI.01824-18 · PMC6450105 | Finnish HSV-1: VirGA assembles every isolate *against* reference strain 17 (JN555585); the reference strain 17+ replicates to 10–100× higher titer in Vero than any circulating clinical isolate (culture adaptation of the reference). OA. |

Key theme: the HSV-1 reference (strain 17, JN555585) is the anchor every assembly is built against, and
the named "strains" (KOS, McKrae) themselves harbor ≥2 lab-specific variants with key-gene discrepancies
and repeat tracts *artificially matched to the reference*.

### PRV — the reference genome was a chimera of six strains

| Code | Source | Year | Identifier | Finding ([VERIFIED src]) |
|------|--------|------|------------|---------|
| P3-044 | **Klupp et al., J Virol 78:424** | 2004 | PMID 14671123 · DOI 10.1128/jvi.78.1.424-440.2004 · PMC303424 (has Erratum) | The "complete" PRV genome (NC_006151) was assembled from **fragments of six different strains** (Kaplan, Becker, Rice, Indiana-Funkhauser, NIA-3, TNL). The deposited "reference genome" is a chimera, not one strain. Free. |
| P3-045 | **Szpara et al., PLoS Pathog 7:e1002282** | 2011 | PMID 22022263 · DOI 10.1371/journal.ppat.1002282 · PMC3192842 | "The only available PRV genome sequence to date is a **mosaic of six strains**"; re-sequencing Kaplan/Becker/Bartha and comparing to the mosaic revealed **frameshifts in the mosaic's non-Kaplan-sourced genes** (e.g. gG/US4 46-aa frameshift from strain Rice); 14 HSV-1 SSRs "set to match the reference genome length." Propose Kaplan as the new reference. OA. |
| P3-046 | **Tombácz et al., Genome Announc 2:e00628-14** | 2014 | PMID 25035325 · DOI 10.1128/genomea.00628-14 · PMC4102862 | "The currently available genome sequences of PRV contain **several discrepancies**, mainly in intergenic repetitive regions"; the fully annotated genome is a composite of six strains. Re-sequenced Kaplan (143,423 bp) by PacBio to upgrade the draft. OA. |
| P3-047 | **Ye et al., Virol J 15:195** | 2018 | PMID 30594230 · DOI 10.1186/s12985-018-1102-8 · PMC6310976 | Serial in-vitro passaging of a virulent PRV (F50/F91/F120) accumulates a large gE deletion, SNVs, in-frame indels, and **frameshifts** (truncated, overexpressed pUL46) — the genome of "the strain" is a moving target under passage. OA. |

Key theme (exceptional DEF005 + DEF006 material): the deposed/implicitly-chimeric reference genome
*inherited* sequence that did not exist in any single strain, and re-sequencing exposed frameshifts the
mosaic carried; passaging demonstrably rewrites the consensus.

### HPV — the reference clone was corrected (resolves wishlist P3-029)

| Code | Source | Year | Identifier | Finding ([VERIFIED src] unless noted) |
|------|--------|------|------------|---------|
| P3-048 | **Meissner JD, "Sequencing errors in reference HPV clones," *Human Papillomaviruses 1997* (Los Alamos), III-110–123** | 1997 | chapter (not indexed in PubMed) | The canonical account that the reference HPV clones (HPV-1a/5a/6b/16/18…) carried sequencing errors, and that "no clone or completely characterized HPV-16 isolate has been identified with a sequence identical to HPV-16R"; documents per-position corrections for HPV-16 (nt 2926 G→A) and HPV-18. **This is the source that pins the A3-002 HPV16 reference-correction case** (previously `P3-029` wishlist item with "not seen" identifier). **Not yet fetched** — chapter text read only via pave.niaid.nih.gov web copy. |
| P3-049 | **Van Doorslaer et al., Nucleic Acids Res 41:D571** | 2013 | (PMID/DOI to verify — PaVE founding paper) | The Papillomavirus Episteme (PaVE): purpose-built to host **corrected, uniformly annotated reference genomes** because the Los Alamos HPV database (last updated 1997) had left "uncorrected sequences [that] will continue to generate unnecessary confusion." **Not yet fetched** — web copy read. |
| P3-050 | **Van Doorslaer et al., Nucleic Acids Res 45:D499** | 2017 | (PMID/DOI to verify — PaVE update) | PaVE update: genomes are "manually edited to restore a viral ORF" where sequencing errors interrupted ORFs; edited genomes noted in the DB with links to the original GenBank record. **Not yet fetched** — web copy read. |
| P3-051 | **Wang et al., Cell Biosci 4:5** | 2014 | PMID 24410913 · DOI 10.1186/2045-3701-4-5 · PMC3903022 | HPV58: long-PCR template cloning + Sanger introduces nucleotide substitutions/indels absent from the authentic genome; RCA-seq of three clinical HPV58s gives 52 substitutions vs reference that PCR+cloning then *further* distorts (Tgo polymerase error ~0.149%). Pipeline choice changes the reported genome. OA — **fetched + read**. |

## B. Assembly fragility / incomplete reference (item 2 — DEF005)

| Code | Source | Year | Identifier | Finding ([VERIFIED src] unless noted) |
|------|--------|------|------------|---------|
| P3-052 | **Price et al., bioRxiv 2019.12.13.876037** | 2019 | DOI 10.1101/2019.12.13.876037 | Ad5 reference (AC_000008) "is incomplete"; re-annotation by short+long-read RNA-seq found SNPs at ~100% penetrance; flag "the original reference sequence contains errors" vs passage mutation as an unresolved question. **Preprint — fetched + read; note status, not load-bearing until peer review.** |
| P3-053 | **Seto et al., Virology 404:180** | 2010 | PMID 20627349 · DOI 10.1016/j.virol.2010.05.010 | **Adversarial counterexample (ADVR-style, kept visible):** HAdV-C5 genome is *stable* across 45 years and across laboratory passage (prototype vs ARM reference material); the paper also notes "a single sequencing error in the HAdV-C5_ARM genome" — i.e. even the stable case carries a deposited-reference error. **Fetched + read.** |

## C. Reading

The expansion adds ~11 same-stock / same-strain cases (plus one adversarial counterexample and one preprint)
to the strong-signal thread, all in the item-1/item-2 zone. Fetched items are now read in full and
`[VERIFIED src]` (exact quotes below); the three HPV reference-clone items (P3-048/049/050) remain
abstract/web-copy level pending fetch.

- **Two named reference strains** (HSV-1 strain 17/NC_001806 anchor; PRV NC_006151) are now documented as
  (a) one haplotype of a mixed population (strain 17: 8 plaque-purified derivatives vary by 50 SNPs / 13 gC
  variants — P3-030), and (b) a **six-strain chimera** that carried sequence no single strain possesses
  (PRV — P3-044/045/046), later corrected by re-sequencing that exposed frameshifts.
- **"The same named strain" is not one genome**: KOS has KOS63/KOS79 ("genetically unrelated"), McKrae has
  ≥2 variant strains with UL56 truncated in some holdings, and repeat tracts are "artificially matched to
  strain 17" across multiple published sequences (P3-040/041/042).
- **The reference clonе error thread is now closed at the deposit level for HPV**: Meissner 1997 + PaVE
  (P3-048/049/050) supply the exact correction lineage for the HPV16/HPV18 reference clones, resolving the
  previously open wishlist item `P3-029`.
- **Passage demonstrably rewrites the consensus** (PRV F50/F91/F120 — P3-047), and **pipeline choice
  changes the reported genome** (HPV58 RCA-seq vs PCR+cloning — P3-051).

The counterexample (Seto 2010, Ad5 stability over 45 years) is retained and logged so the strong-signal
claim stays scoped to "detectable, multi-form, across many families" and not "every reference genome is
wrong."

## D. Verified quotes (`[VERIFIED src]`, extracted from fetched PDFs 2026-11-14)

**PRV reference genome = six-strain chimera (DEF005+DEF006):**

- **P3-044 Klupp 2004:** "using sequence fragments derived from **six different strains***" (Kaplan, Becker, Rice,
  Indiana-Funkhauser, NIA-3, TNL) — the deposited "complete" PRV genome NC_006151 is a chimera.
- **P3-045 Szpara 2011:** "the only available PRV genome sequence to date is a **mosaic of six strains**";
  "Strain Kaplan contributed **86%** of the sequence in the mosaic reference genome, while the remainder included
  sequences from strains Becker, Rice, Indiana-Funkhauser, NIA-3, and TNL"; "Several of these sequence
  differences significantly affect the resulting protein because of **frameshifts in the strains used for the
  mosaic genome**. The largest frame-shift changes **46 AAs** in the extracellular domain of gG (US4)… The gG
  sequence in the mosaic genome was derived from PRV strain Rice."
- **P3-045 Szpara 2011 (assembly prior):** "In the only previous publication comparing full-length genomes of HSV-1
  (strains 17, H129, and F), the length of fourteen major SSRs throughout the genome were not determined and were
  instead **set to match the reference genome length**."
- **P3-046 Tombácz 2014:** "The currently available genome sequences of PRV contain **several discrepancies**,
  mainly in intergenic repetitive regions"; "the totally annotated version of genome sequence is a **composite of
  six different PRV strains**."

**PRV passage rewrites the consensus (DEF006):**

- **P3-047 Ye 2018:** "Genome sequencing of F50, F91, and F120 showed **deletion of a large fragment containing
  gE**"; "In-frame and **frameshift indels** were also detected in specific genes of passaged strains. Particularly
  frameshift mutations were observed in highly passaged strains, resulting in a **truncated but overexpressed
  pUL46**."

**HSV-1 "same strain" is not one genome (item 1):**

- **P3-040 Parsons 2015:** "we compared the percent identity at the DNA level between the genomes of KOS Large,
  KOS Syncytial, and KOS Hypersyncytial (**99.5%** identity) and of F Large and F Syncytial (**98.6%** identity)";
  "In each of the syncytial strains, we found an **identical DNA change**, affecting one residue in the gB (UL27)
  fusion protein."
- **P3-041 Renner 2021:** "Three HSV-1 strain McKrae stocks have been sequenced previously, **revealing
  discrepancies in key genes**"; "the UL56 gene… has a truncated open reading frame (ORF) in JQ730035 and
  MN136524… In contrast, the UL56 ORF in the Morrison and Davido laboratories' McKrae strain JX142173 is **full
  length** and appears to be intact."
- **P3-042 Bowen 2016:** "**Reiteration lengths in several published strains are artificially matched to strain
  17**"; KOS63 and KOS79 — "KOS79 was a **genetically unrelated strain**… these data suggest that the human source
  of KOS63 and KOS79 could have been infected with two genetically unrelated strains."
- **P3-043 Bowen 2019:** "the reference strain 17+ replicated to **significantly higher titers than any of the
  circulating clinical isolates** in Vero cells… 10- to 100-fold-higher viral amounts"; assembly: "VirGA uses Mugsy
  alignment to match these contigs to the HSV-1 **reference genome (strain 17; GenBank accession JN555585)**."

**HPV reference clone errors + pipeline non-uniqueness (item 2):**

- **P3-051 Wang 2014:** "Three HPV58 genomes decoded by RCA-seq displayed a total of **52 nucleotide
  substitutions** from reference HPV58"; "the long PCR template cloning and sequencing led to **additional
  nucleotide substitutions, insertions, and deletions** from an authentic HPV58 genome"; "the Tgo DNA polymerase
  exhibited an **error rate of ~0.149% ±0.038%**."

**Counterexample (kept visible) — Ad5 stability:**

- **P3-053 Seto 2010:** "Comparison of this genome to the sparsely amplified prototype demonstrates a **high level
  of sequence conservation and stability of this genome across 45 years**"; "a **single sequencing error** in the
  HAdV-C5_ARM (Adenovirus Reference Material) genome is noted and may lead to erroneous annotation."

**Intrastrain strong-signal thread (previously wishlist; now fetched + read):**

- **P3-031 Cudini 2019:** "high within-host HCMV diversity is the frequent presence of **mixed infections**"; title
  states "high diversity due to superinfection and evidence of within-host recombination."
- **P3-032 Rathbun 2022:** "the vast majority [of minor variants] were **shared between partners (77–100% shared
  MV)**… strongly suggests that these variants are **not random sequencing errors**."
- **P3-034 Morga 2021:** OsHV-1 "which differs from the reference genome published in 2005" (Davison) — the
  reference is the 2005 single genome, and modern diversity is measured *against* it.
- **P3-035 Kuny & Szpara 2021:** "Alphaherpesviruses… were **long considered to be genetically stable and to
  exist in a homogeneous state**"; "the creation of a single consensus genome necessarily **removes the details of
  underlying components** of the viral genetic population."
- **P3-036 Ortigas-Vasquez & Szpara 2024:** "The historical reliance on a single consensus genome to accurately
  reflect the entirety of a given herpesvirus isolate, strain, or species **needs to be reassessed**"; "consensus
  genomes of the same herpesvirus strain [are] **not as stable as is often assumed**."
- **P3-037 influenza DelVGs (bioRxiv 2026):** "**1,767 influenza samples, of which 540 (30.6%) contained one or
  more defective segments**"; "even after database submission, **471 out of 1,529 samples (30.8%) still exhibited
  defective segments**." *(Preprint — not load-bearing until peer review.)*

## E. Next steps

1. ~~Fetch OA/free PDFs → confirm → re-tag `[VERIFIED src]`~~ **done 2026-11-14** for P3-031/032/034/035/036/037
   and P3-040…047/051/052/053. Three HPV reference-clone items (P3-048/049/050) remain unfetched.
2. Verify the two PaVE PMIDs/DOIs (P3-049/050) and the Meissner chapter locator (P3-048) once a copy is obtained.
3. A3 census already carries the new same-stock rows (A3-019…A3-026); the "correction scope not yet pinned" note on
   the A3-002 CSV row now resolves to P3-048.
4. Fold into the CNJ150 upgrade decision (Conjecture → Observation/Lemma, scoped "detectable") — with Albert.