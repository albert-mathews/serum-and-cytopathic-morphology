# P3 Type-Strain / Type-Isolate Literature Audit — Protocol

**Stream:** `p3_genetics/` (parked for main paper unless expanded)  
**Pilot started:** 2026-09-19  
**Companion files:** `P3_type_strain_audit.csv`, `P3_genbank_refseq_metadata_mining.md`, `p3.md`

---

## 1. Purpose

Estimate how often **viral type material / type Isolates / ICTV-typical members / RefSeq exemplars** enter public databases via a **culture → CPE (or culture endpoint) → sequence** path, versus clinical molecular / metagenomic paths.

This is an **inheritance / under-determination** audit of *type material pathways*. Claims are limited to what the cited corpus documents about culture-derived type material and reference-path risk.

**Scoped risk (from `p3.md`):**

> High-risk path into the reference corpus: **culture-derived, CPE-justified Isolates** used as type material—not every GenBank/RefSeq row.

---

## 2. Guardrails (mandatory)

| Do | Do not |
|----|--------|
| Use **inheritance**, **under-determination**, **risk path** language | Over-claim beyond what the cited type-material path documents |
| Code **low-risk** clinical NGS rows as adversarial balance | Equate “culture used somewhere in the field” with “this accession’s type path is high” |
| Mark **unclear** when primary paper not yet read | Invent citations, accessions, or FBS% values |
| Quote sparingly in `notes` (searchable pointers) | Treat metadata wording alone as proof of particle identity |
| Keep P3 **parked** for main paper unless user expands | Smuggle P3 conclusions into R1/R2 empirical core |

This protocol describes type-strain / reference-path audit practice. Claims are limited to what the cited corpus documents about culture-derived type material and inheritance risk.

---

## 3. Unit of analysis

One row = one **named type / prototype / ICTV typical member / widely used RefSeq exemplar strain** (or a clearly scoped accession path when split paths exist, e.g. SARS-CoV-2 clinical vs culture Isolates).

Prefer:

1. ICTV “typical member” / exemplar isolate when stated  
2. NCBI RefSeq viral complete genome for that taxon/strain  
3. ATCC/BEI “type” or historical prototype strain with published genome  

---

## 4. Coding rules

### 4.1 Dichotomous / trichotomous fields

- `isolation_used_culture`: **yes** if the type material was propagated in cell culture, eggs, or explant culture before or as part of designation; **no** if sequence/type path is clinical specimen molecular only; **unclear** otherwise.
- `cpe_as_assertion`: **yes** if authors treat cytopathic effect (or synonymous culture morphology endpoint) as evidence of successful Isolation/presence for that material; **no** if explicitly not; **unclear** if culture used but CPE not verified as the assertion.
- `serum_or_dual_media_stated`: **yes** if growth vs maintenance / FBS% (or serum%) shift is described for the Isolation/propagation of that material; note pre→post in `notes` when found; **no** if media described without dual pattern; **unclear** if not checked or absent.
- `sequence_from_that_isolate`: **yes** if the public reference genome is from that isolate/strain lineage; **unclear** if only related strains sequenced.

### 4.2 `risk_path` (primary outcome for P3 pilot)

| Code | Meaning |
|------|---------|
| **high** | Culture used **and** CPE (or clear culture endpoint) asserted **and** public type/reference sequence from that culture lineage → **culture+CPE→type sequence** inheritance risk |
| **medium** | Mixed/split paths; culture without verified CPE assertion; molecular clone with later culture; species-level ambiguity |
| **low** | Type/discovery sequence from **clinical metagenome / stool-urine-serum NGS / molecular cloning without culture** for that entry |

Ambiguity → **more conservative for claims** (do not upgrade to low to “help” the thesis; do not upgrade to high without evidence). For adversarial balance, deliberately include ≥5 **low** rows.

### 4.3 What risk_path is *not*

- Not a score of “real vs fake virus.”  
- Not proof that CPE is non-specific (that is R1/R2/CRO).  
- Not a substitute for GenBank metadata mining breadth (see companion explainer).

---

## 5. Sampling plan (pilot → full)

**Pilot (this batch):** ~30–50 rows spanning:

- DNA and RNA viruses  
- Classic human prototypes (polio, measles, influenza, HSV, adenovirus, …)  
- Recent zoonotics (MERS, Nipah, Ebola, SARS-CoV-2, …)  
- ≥5 low-risk clinical NGS / non-cultivable exemplars  

**Later expansion:** ICTV report “typical member” lists per family; RefSeq viral neighbors; decade strata (pre-1960, 1960–89, 1990–2009, 2010+).

---

## 6. Sources and verification

1. ICTV Report chapters (typical member + accession)  
2. NCBI Nucleotide/RefSeq record SOURCE/FEATURES/COMMENT  
3. Primary Isolation paper (PubMed/PMC) when OA or already in local refs  
4. ATCC/BEI product history pages (passage notes)  

**Do not invent.** If only secondary sources available, code **unclear** and list URL.

---

## 7. Workflow

1. Select candidate strain/taxon.  
2. Locate ICTV/RefSeq accession.  
3. Trace Isolation paper year + method (culture? CPE?).  
4. Check whether sequenced genome is that isolate.  
5. Fill CSV row; quote ≤1 short phrase in notes if needed.  
6. Assign `risk_path`.  
7. Periodically tally high/medium/low; ensure low-risk balance.

---

## 8. Outputs and metrics

- `P3_type_strain_audit.csv` — coded corpus  
- Tallies: n; % high / medium / low; family breakdown; decade breakdown (when years filled)  
- Narrative: qualitative examples of high path vs low path (Discussion-safe)

Optional later join to metadata-mining pilot: proportion of RefSeq viral records with culture/CPE language vs type-strain audit deep reads.

---

## 9. Relation to main paper

Default: **parked**. May become a short Discussion question (`p3.md` snippet P3-S1) or remain out of scope. Do not promote pilot tallies to paper Results without explicit expansion decision.

---

*Protocol v0.1 — 2026-09-19*
