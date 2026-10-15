# Prior-art map: critiques of thin sample-production provenance for deposited viral / pathogen genomes

**Date:** 2026-09-21 (America/Toronto)  
**Scope:** Published papers, reviews, commentaries, INSDC/GenBank policy-adjacent docs, and reputable society/standards pieces documenting problems with **inadequate documentation of how sequenced viral (or pathogen) material was obtained** — culture vs clinical-direct vs unknown; missing voucher/type material; poor metadata; circular strain citation; MAG-as-isolate; sequence-only taxonomy debates.  
**Framing:** Literature map for citation / community-debate context — **not** an advocacy brief. Exploration of what has already been said.

---

## Executive summary (honest)

**On the user’s narrow claim** — that allowing genome deposits without detailed Methods for *acquiring* the sequenced sample (culture±CPE isolate vs clinical-direct vs other paths) builds a weakly founded viral genetic database — **exact prior art is sparse for viruses as a class**.

**What exists instead:**

| Density | Topic |
|--------|--------|
| **Denser (Tier A-ish)** | **Influenza** specifically: passaging history / clinical specimen vs culture is a well-documented metadata and interpretive problem. |
| **Denser (Tier A standards)** | **Uncultivated virus genomes (UViGs):** MIUViG and ICTV/INSDC submission guidelines *require* declaring source type (isolate microbial genome vs virome vs metagenome, etc.). |
| **Denser (Tier B)** | General **metadata incompleteness / inconsistency** in GenBank, BioSample, GISAID for pathogen genomes (host, geo, lab fields) — usually not culture±CPE vs clinical. |
| **Denser (Tier A/C adjacent, transferable)** | **Bacteria:** false “type strain” labels, voucher gaps, composite MAGs deposited like isolates. |
| **Sparse** | Broader viral literature that explicitly treats **culture±CPE vs clinical-direct sample-production provenance** as a foundational database epistemology problem (analogous to EV–virus physical-overlap debates). |

**Nearest neighbors for the user’s claim:** DuPai et al. 2019 + McWhite et al. 2016 (influenza passage); Roux et al. 2019 MIUViG `source_uvig`; Timme et al. 2023 Pathogen DOM (methods/contextual data placement); bacterial voucher / false-type-strain literature as transferable analogy.

---

## Tier A — Sample-source / isolation / culture provenance for deposited genomes

### A1. DuPai CD, McWhite CD, Smith CB, Garten R, Maurer-Stroh S, Wilke CO. (2019). Influenza passaging annotations: what they tell us and why we should listen. *Virus Evolution* 5(1):vez016.  
**DOI:** [10.1093/ve/vez016](https://doi.org/10.1093/ve/vez016) · **PMID:** 31263560 · **OA:** [PMC6599686](https://pmc.ncbi.nlm.nih.gov/articles/PMC6599686/)

**What they criticize:** Heterogeneous, missing, and non-machine-parsable **passage-history annotations** across GISAID / IRD / OpenFlu (and GenBank `lab_host` import quirks). Passaging introduces spurious adaptation signals; clinical-direct vs egg/MDCK/SIAT/monkey-cell history is essential to interpret deposited sequences, yet ~1/3 of H3N2 records in the study window were ambiguous or lacked clear passage info.

**Quote (≤40 words):** “Making sense of influenza passaging annotations is a daunting task. … awareness … of the negative impact of cell passaging on sequence fidelity is easily and currently attainable…”

**Helps user’s claim?** **Strong yes (influenza-specific).** Closest published community critique of deposited genomes where *how the material was obtained/propagated* (clinical specimen vs culture passage) is treated as critical and currently inadequate. Does **not** generalize the claim to all viral DBs or CPE specifically.

---

### A2. McWhite CD, Meyer AG, Wilke CO. (2016). Sequence amplification via cell passaging creates spurious signals of positive adaptation in influenza virus H3N2 hemagglutinin. *Virus Evolution* 2(2):vew026.  
**DOI:** [10.1093/ve/vew026](https://doi.org/10.1093/ve/vew026) · **OA:** [PMC5049878](https://pmc.ncbi.nlm.nih.gov/articles/PMC5049878/)

**What they criticize:** Cell/egg passaging creates **false adaptation signals** in deposited HA sequences; analyses that ignore passage status misread natural evolution. Implies metadata on passage vs original specimen is scientifically load-bearing.

**Helps?** **Yes (Tier A, influenza).** Empirical sister paper to A1: shows *why* provenance of culture vs clinical matters for database reuse — not a general GenBank-policy critique.

---

### A3. Roux S, et al. (2019). Minimum Information about an Uncultivated Virus Genome (MIUViG). *Nature Biotechnology* 37:29–37.  
**DOI:** [10.1038/nbt.4306](https://doi.org/10.1038/nbt.4306) · **OA:** [PMC6871006](https://pmc.ncbi.nlm.nih.gov/articles/PMC6871006/)

**What they criticize / require:** UViG deposits must report **mandatory** metadata including **Source of UViGs** (enumeration: metagenome, viral-fraction metagenome, sequence-targeted metagenome, metatranscriptome, microbial SAG, viral SAG, **isolate microbial genome**, other), plus assembly software, virus-identification software, genome type/structure, detection type, assembly quality. Motivated by the fact that UViGs now dominate public virus sequence space and are not interchangeable with isolate genomes.

**Quote:** “Community-wide adoption of MIUViG standards … will improve the reporting of uncultivated virus genomes in public databases.”

**Helps?** **Yes — standards-side Tier A.** Does not argue “databases are weakly founded” rhetorically; it **operationalizes** the distinction isolate vs metagenome/SAG as deposit metadata. Highly citable as prior community recognition that *source path* must be explicit.

---

### A4. Adriaenssens EM, Roux S, Brister JR, Karsch-Mizrachi I, Kuhn JH, et al. (2023). Guidelines for public database submission of uncultivated virus genome sequences for taxonomic classification. *Nature Biotechnology* (ICTV/INSDC-oriented guidance).  
**DOI:** [10.1038/s41587-023-01844-2](https://doi.org/10.1038/s41587-023-01844-2) · **OA:** [PMC10526704](https://pmc.ncbi.nlm.nih.gov/articles/PMC10526704/)

**What they criticize / require:** Exemplar genomes for ICTV taxa must be in INSDC with proper naming, completeness, and **MIUViG-structured metadata** including source of UViG; warn against tagging “complete genome” without experimental termini verification; push BioSample linkage and FAIR source modifiers.

**Helps?** **Yes (Tier A standards).** Explicit isolate-vs-UViG handling for GenBank/ENA deposits. Still not a critique of culture±CPE vs clinical-direct for cultivated human pathogens.

---

### A5. Timme RE, Karsch-Mizrachi I, Waheed Z, Arita M, MacCannell D, Maguire F, et al. (2023). Putting everything in its place: using the INSDC compliant Pathogen Data Object Model to better structure genomic data submitted for public health applications. *Microbial Genomics* 9:001145.  
**DOI:** [10.1099/mgen.0.001145](https://doi.org/10.1099/mgen.0.001145) · **OA:** [PMC10763499](https://pmc.ncbi.nlm.nih.gov/articles/PMC10763499/)

**What they criticize:** Patchwork INSDC submission routes leave **contextual / methods metadata** inconsistently placed (GenBank flat-file source modifiers vs BioSample/BioProject/raw reads). Viral submissions historically often omit BioSample and raw reads; early SARS-CoV-2 often had assemblies without linked BioSample. Propose Pathogen DOM so sample processing, sequencing methods, and project context are structured and queryable.

**Quote:** “…users trying to access the wealth of INSDC pathogen data may be unable to identify important relationships between genomes because the available metadata are often stored inconsistently.”

**Helps?** **Partial Tier A.** Strong on *methods and contextual data structure* for pathogen deposits; not specifically culture±CPE vs clinical-direct, but argues thin structured provenance undermines public-health reuse — closest general pathogen-DB analogue.

---

### A6. Salvà-Serra F, Jaén-Luchoro D, Karlsson R, Bennasar-Figueras A, Jakobsson HE, Moore ERB. (2019). Beware of False “Type Strain” Genome Sequences. *Microbiology Resource Announcements* 8:e00369-19.  
**DOI:** [10.1128/MRA.00369-19](https://doi.org/10.1128/MRA.00369-19) · **OA:** [PMC6544187](https://pmc.ncbi.nlm.nih.gov/articles/PMC6544187/)

**What they criticize:** Bacterial genomes **mislabelled as type strains** in publications/deposits; ANI shows they are not descended from authentic nomenclatural types — “fake news” reference points that propagate error.

**Quote:** “…type strains serve as important ‘reference points’ … The presence of sequences erroneously reported as type strains is a real example of ‘fake news’…”

**Helps?** **Transferable Tier A (bacteria).** Exact analogue for *voucher / type-material provenance failure*, not viral culture±CPE. Useful to cite as microbiology’s stronger tradition of insisting deposits track authentic living material.

---

### A7. Renner SS, et al. (2024). Improving the gold standard in NCBI GenBank and related databases: DNA sequences from type specimens and type strains. *Systematic Biology* 73:486–494.  
**DOI:** [10.1093/sysbio/syad068](https://doi.org/10.1093/sysbio/syad068) · **PMID:** 37956405 · **OA PDF (author site):** [markscherz.com PDF](https://www.markscherz.com/wp-content/uploads/Renner-et-al.-2024-Improving-the-gold-standard-in-NCBI-GenBank-and-related-databases-DNA-sequences-from-type-specimens-and-type-strains.pdf)

**What they criticize:** INSDC reliability for identification depends on sequences linked to **type specimens / type strains / vouchers**; many BLAST hits lack usable voucher metadata, propagating taxonomic error.

**Helps?** **Adjacent Tier A.** Cellular-organism voucher critique transferable to “what physical/living material backs this deposited genome?” Viruses lack equivalent nomenclatural type culture practice for most taxa — the gap itself is informative.

---

### A8. Buckner JC, Sanders RC, Faircloth BC, Chakrabarty P. (2021). The critical importance of vouchers in genomics. *eLife* 10:e68264.  
**DOI:** [10.7554/eLife.68264](https://doi.org/10.7554/eLife.68264) · **OA:** [PMC8186901](https://pmc.ncbi.nlm.nih.gov/articles/PMC8186901/)

**What they criticize:** Most vertebrate genome assemblies lack **specimen vouchers**; without vouchers, taxonomy and re-sampling cannot be verified.

**Helps?** **Adjacent.** Same epistemology (sequence without anchored material). Not pathogen/virus-specific.

---

## Tier B — Metadata quality / misannotation / contamination (not specifically culture vs clinical)

### B1. Schriml LM, Chuvochina M, Davies N, Eloe-Fadrosh EA, Finn RD, Hugenholtz P, et al. (GSC board). (2020). COVID-19 pandemic reveals the peril of ignoring metadata standards. *Scientific Data* 7:188.  
**DOI:** [10.1038/s41597-020-0524-5](https://doi.org/10.1038/s41597-020-0524-5) · **OA:** full text at Nature

**What they criticize:** Despite MIxS packages in INSDC, SARS-CoV-2 BioSamples commonly leave fields blank/`missing` (e.g. host missing in 2416/5198); wrong package choice; unstandardized disease strings. Contextual WHO/WHAT/HOW/WHERE/WHEN metadata treated as critical infrastructure.

**Quote:** “…poorly described data are still all too common across genomic and metagenomic studies.”

**Helps?** **Tier B → near A on “HOW”.** Mentions sample-collection protocols among critical descriptors but focuses on host/geo/disease completeness, not culture vs clinical-direct methods detail.

---

### B2. Gozashti L, Corbett-Detig R. (2021). Shortcomings of SARS-CoV-2 genomic metadata. *BMC Research Notes* 14:189.  
**DOI:** [10.1186/s13104-021-05649-x](https://doi.org/10.1186/s13104-021-05649-x) · **OA:** [PMC8128092](https://pmc.ncbi.nlm.nih.gov/articles/PMC8128092/)

**What they criticize:** ~9.8% / ~11.6% of GISAID originating/submitting lab fields have spelling/inconsistency errors; ambiguous lab names impair association studies. Notes completeness/detail matter as much as consistency.

**Helps?** **Tier B.** Lab identity metadata, not sample-production path (culture vs clinical).

---

### B3. Gonçalves RS, Musen MA. (2019). The variable quality of metadata about biological samples used in biomedical experiments. *Scientific Data* 6:190021.  
**DOI:** [10.1038/sdata.2019.21](https://doi.org/10.1038/sdata.2019.21) · **OA:** [PMC6380228](https://pmc.ncbi.nlm.nih.gov/articles/PMC6380228/)

**What they criticize:** NCBI BioSample attribute quality is highly variable (custom attribute names, invalid ontology/Boolean values) — foundational sample-description infrastructure is unreliable.

**Helps?** **Tier B infrastructure.** Supports “thin metadata → weak reuse”; not virus provenance-specific.

---

### B4. Chen J, Sun Y, Yan X, et al. (2022). Elimination of Foreign Sequences in Eukaryotic Viral Reference Genomes Improves the Accuracy of Virome Analysis. *mSystems* 7:e00907-22.  
**DOI:** [10.1128/msystems.00907-22](https://doi.org/10.1128/msystems.00907-22) · **OA:** [PMC9765019](https://pmc.ncbi.nlm.nih.gov/articles/PMC9765019/)

**What they criticize:** **766 nt + 276 aa problematic viral sequences** in GenBank/UniProt (host, vector, LCD, misclassification); 85.5% chimeric fragments; urge submitters to QC before deposit. Includes natural host inserts (e.g. BVDV CPE-related S27a/ubiquitin) vs unintentional contamination — interesting side-note that **culture phenotype (CPE)** can leave genomic fingerprints, but paper’s focus is contamination/misannotation, not deposit Methods for sample acquisition.

**Helps?** **Tier B (contamination).** Tangential to culture±CPE (via BVDV cytopathogenic inserts). Not a provenance-of-sampling critique.

---

### B5. Steinegger M, Salzberg SL. (2020). Terminating contamination: large-scale search identifies more than 2,000,000 contaminated entries in GenBank. *Genome Biology* 21:115.  
**DOI:** [10.1186/s13059-020-02023-1](https://doi.org/10.1186/s13059-020-02023-1) · **OA:** Springer open

**What they criticize:** Massive cross-kingdom contamination in GenBank/RefSeq; **explicitly excluded viruses** because integration confounds contamination calls.

**Helps?** **Tier B, limited.** Famous “garbage in” cite; deliberately not viral.

---

### B6. Field D, et al. (2008). The minimum information about a genome sequence (MIGS) specification. *Nature Biotechnology* 26:541–547.  
**DOI:** [10.1038/nbt1360](https://doi.org/10.1038/nbt1360)

**What they propose:** Foundational GSC checklist so genome sequences carry minimal **contextual** information for reuse — ancestor of MIxS / MIGS virus / MIUViG.

**Helps?** **Foundational Tier B/standards.** Cite as the institutional lineage that later standards extend; original MIGS is broader than viral culture provenance.

---

### B7. Yilmaz P, et al. (2011). Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications. *Nature Biotechnology* 29:415–420.  
**DOI:** [10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823)

**What they propose:** Expanded MIxS suite including environment packages; implemented across INSDC.

**Helps?** **Standards background.** Compliance still incomplete (see B1).

---

### B8. Related review (2024). Jones et al. / Frontiers Bioinformatics — “Ten common issues with reference sequence databases and how to mitigate them.”  
**DOI:** [10.3389/fbinf.2024.1278228](https://doi.org/10.3389/fbinf.2024.1278228) · **OA:** [PMC10978663](https://pmc.ncbi.nlm.nih.gov/articles/PMC10978663/)

**What they criticize:** Contamination, taxonomic errors, inclusion criteria; cites Chen et al. viral chimeric contamination stats.

**Helps?** **Tier B survey.** Good secondary cite.

---

## Tier C — ICTV sequence-based taxonomy / MAG-as-isolate critiques

### C1. Simmonds P, et al. (2017). Consensus statement: Virus taxonomy in the age of metagenomics. *Nature Reviews Microbiology* 15:161–168.  
**DOI:** [10.1038/nrmicro.2016.177](https://doi.org/10.1038/nrmicro.2016.177)

**What they argue:** ICTV can classify viruses known **only from sequences** (no isolate required) given QC, preferably coding-complete genomes, INSDC deposition. Landmark acceptance of sequence-only taxa — **opposite pole** to “must have culture isolate,” but with quality caveats.

**Helps?** **Tier C — important counterweight.** Documents community move *away* from requiring isolation; user’s culture±CPE concern sits in tension with this consensus. Cite for debate mapping, not as supporting “culture required.”

---

### C2. Simmonds P, et al. (2023). Four principles to establish a universal virus taxonomy. *PLoS Biology* 21:e3001922.  
**DOI:** [10.1371/journal.pbio.3001922](https://doi.org/10.1371/journal.pbio.3001922) · **OA**

**What they argue:** Principles for taxonomy including metagenome-inferred viruses with strict QC before taxonomic assignment (referenced by Adriaenssens et al. 2023).

**Helps?** **Tier C.** Quality-of-sequence-for-taxonomy, not sample-acquisition Methods on culture vs clinical.

---

### C3. Shaiber A, Eren AM. (2019). Composite Metagenome-Assembled Genomes Reduce the Quality of Public Genome Repositories. *mBio* 10:e00725-19.  
**DOI:** [10.1128/mBio.00725-19](https://doi.org/10.1128/mBio.00725-19) · **OA:** [PMC6550520](https://pmc.ncbi.nlm.nih.gov/articles/PMC6550520/)

**What they criticize:** **Composite MAGs** (bins combining multiple populations) deposited into public repositories degrade quality when treated like isolate genomes.

**Helps?** **Tier C transferable.** Strong analogue: computational products deposited *as if* they were isolate-derived genomes — parallel worry for viruses (UViG/MAG vs isolate) without equating to culture±CPE.

---

### C4. Bowers RM, et al. (2017). Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG) of bacteria and archaea. *Nature Biotechnology* 35:725–731.  
**DOI:** [10.1038/nbt.3893](https://doi.org/10.1038/nbt.3893)

**What they propose:** Completeness/contamination reporting standards so MAGs/SAGs are not silently treated as isolate-quality.

**Helps?** **Tier C standards.** Sibling to MIUViG.

---

### C5. Ladner JT, et al. (2014). Standards for sequencing viral genomes in the era of high-throughput sequencing. *mBio* 5:e01360-14.  
**DOI:** [10.1128/mBio.01360-14](https://doi.org/10.1128/mBio.01360-14) · **OA**

**What they propose:** Finishing categories (standard draft → finished) for viral WGS — **completeness/assembly quality**, not culture vs clinical provenance.

**Helps?** **Tier C-adjacent.** Completeness taxonomy often conflated with provenance; cite carefully as *not* addressing sample-acquisition Methods.

---

## Policy / checklist documents (not papers, but citable)

| Resource | Relevance |
|----------|-----------|
| GSC **MIGS virus (MigsVi)** checklist | Minimal contextual metadata for virus genome sequences. https://genomicsstandardsconsortium.github.io/mixs/0010005/ |
| GSC **MIUViG** checklist | Explicit `source_uvig` enumeration (isolate vs metagenome paths). https://genomicsstandardsconsortium.github.io/mixs/0010012/ |
| ENA **ERC000033** virus pathogen checklist | Surveillance/outbreak isolate-oriented pathogen metadata. |
| NCBI BankIt **source modifiers** | `isolation_source`, `lab_host`, `culture_collection`, `specimen_voucher`, `strain`/`isolate` — fields exist; enforcement/completeness vary. |
| INSDC missing-value vocabulary | Structured “missing: …” values — institutional acknowledgment that sparsity is common. |

---

## Gaps (say this plainly)

1. **No strong multi-virus paper** found that frames GenBank/INSDC as *epistemically weakly founded* specifically because deposits lack Methods distinguishing **culture±CPE isolate sampling** vs **clinical-direct** sequencing (outside influenza passaging literature).  
2. **CPE** as a deposit-metadata axis is essentially absent as a database-critique theme (appears only indirectly, e.g. BVDV cytopathogenic host-gene inserts in Chen et al. 2022).  
3. Viral **voucher / culture-collection** practice is weaker than bacterial type-strain norms; literature accordingly thinner.  
4. ICTV trajectory (Simmonds 2017) **legitimates sequence-only taxa**, so community debate runs *both* ways — standards push better source metadata while taxonomy relaxes isolation requirements.

---

## Suggested citation clusters for the user’s question

| User need | Best cites |
|-----------|------------|
| Culture vs clinical-direct *does* matter for deposited genomes | **A1 DuPai 2019**, **A2 McWhite 2016** (+ Bush 2000 / Gatherer 2010 as older influenza passage literature if expanding) |
| Databases / standards already require declaring isolate vs metagenome source | **A3 Roux MIUViG 2019**, **A4 Adriaenssens 2023** |
| Thin contextual/methods metadata in pathogen INSDC deposits | **A5 Timme Pathogen DOM 2023**, **B1 Schriml 2020**, **B3 Gonçalves 2019** |
| Transferable “no authentic material behind the label” | **A6 Salvà-Serra 2019**, **A7 Renner 2024**, **A8 Buckner 2021** |
| Sequence-only taxonomy / MAG-as-isolate neighbors | **C1 Simmonds 2017**, **C3 Shaiber & Eren 2019** |
| Contamination / misannotation (distinct claim) | **B4 Chen 2022**, **B5 Steinegger 2020** |

---

## Search note

Queries covered PubMed/Google-Scholar-style themes listed in the brief (INSDC metadata, vouchers, MIENS/MIxS/MIUViG, SARS-CoV-2 metadata, garbage-in/contamination, ICTV metagenomics, MAG-as-isolate, bacterial vouchers). Prefer OA full text; abstracts used where noted. **No Sci-Hub.** Preprint Scotch et al. 2025 (metadata-driven pathogen genomics) noted in search hits but not elevated as Tier A peer-reviewed prior art.

**Bottom line for parent/user:** Sparse on the exact culture±CPE-vs-clinical-direct / weakly-founded-DB claim for viruses broadly; **denser on influenza passaging provenance, UViG source standards, general pathogen metadata incompleteness, and bacterial voucher/type-strain + MAG analogues.** Frame as a prior-literature map with a real gap, not as settled community consensus either way.

---

## Addendum 2026-09-21i

Additional Tier A–B practice/standards cites (culture/CPE isolate warrant; MIUViG/MigsVi source labeling; influenza passage metadata) collected in:

`P3_supporting_literature_culture_cpe_genetics_2026-09-21.md`
