# GenBank / RefSeq metadata mining — what it means (P3 companion)

**Audience:** Albert (plain-language methods note)  
**Status:** pilot run 2026-09-19 — results in `genbank_mining/` (`P3_genbank_mining_results_2026-09-19.md`, `mining_summary.json`)  
**Date:** 2026-09-19  
**Related:** `P3_type_strain_audit_protocol.md`, `P3_type_strain_audit.csv`, `p3.md`, `genbank_mining/`

---

## 1. One-sentence definition

**GenBank/RefSeq metadata mining** means programmatically downloading and searching the *text fields that describe* public viral sequence records—not re-analyzing every base of every genome—to estimate how often those records **advertise** a culture / Isolate / CPE path in their own labels.

Think: reading millions of “library card catalog” entries for wording, not re-sequencing the books.

---

## 2. What you download (metadata), vs what you do not

### 2.1 What you pull

For each GenBank or RefSeq record, tools such as **NCBI E-utilities**, **NCBI Datasets**, or **Biopython Entrez** can fetch structured text, including:

| Field / region | Why it matters for P3 |
|----------------|------------------------|
| **DEFINITION** | One-line name (“…isolate…complete genome”) |
| **SOURCE / ORGANISM** | Taxonomic label |
| **FEATURES → source qualifiers** | Rich annotations: `isolation_source`, `host`, `cell_line`, `lab_host`, `note`, `strain`, `isolate`, `collection_date` |
| **COMMENT** | Free text; often passage history, assembly notes |
| **REFERENCES** | Papers tied to the deposit |
| **Submitter / Journal / dates** | Who deposited, when |

These fields are **claims written by submitters** (and sometimes curated by RefSeq). They are excellent for **breadth and trends**. They are weak as standalone ontology of particle identity.

### 2.2 What you are *not* doing in a metadata pilot

- Not re-calling SNPs across all viral RefSeq  
- Not proving assemblies are wrong  
- Not BLAST-everything-vs-everything  
- Not inferring particle identity from a keyword hit  

Sequence re-analysis can be a *later* project; metadata mining is the cheap complementary layer.

---

## 3. Typical keyword / filter ideas

Search (case-insensitive) across DEFINITION + COMMENT + source qualifiers for language that **advertises** culture pathways, for example:

- Cell systems: `Vero`, `Vero E6`, `MRC-5`, `HEp-2`, `HeLa`, `MDCK`, `BHK`, `A549`, `Huh7`, `cell line`, `cell culture`, `tissue culture`  
- Process: `passage`, `passaged`, `plaque`, `TCID`, `isolated in`, `propagated in`, `lab_host`  
- Endpoint: `CPE`, `cytopathic`, `syncytia`, `cytopathogenic`  
- Contrast filters (clinical path): `bronchoalveolar`, `BALF`, `nasopharyngeal`, `stool`, `serum`, `metagenom`, `clinical specimen`, `patient`

**Important:** absence of keywords ≠ absence of culture (under-annotation). Presence of “Vero” ≠ proof that CPE justified the species label. Mining estimates **advertised** paths.

---

## 4. What it CAN show

1. **Prevalence of culture language** among viral RefSeq (or a defined GenBank slice).  
2. **Temporal trends** (e.g., fraction of new viral complete genomes mentioning culture/CPE by year).  
3. **Taxon / family breakdowns** (which families are metadata-culture-heavy).  
4. **Complementary statistics** next to the type-strain audit (breadth vs depth).  
5. **Leads** for which records deserve deep paper reading.

---

## 5. What it CANNOT show (alone)

1. **Cannot prove** sequences lack virion identity, or settle “not a virion genome,” from metadata alone.  
2. **Cannot detect silent mislabeling** (culture used but not written; or clinical written but culture actually done).  
3. **Cannot replace** type-strain / Isolation paper reading (`P3_type_strain_audit_*`).  
4. **Cannot** support database-wide conclusions about particle identity from metadata alone.  
5. **Cannot** fix the Isolation-stage CPE confound (that remains R1/R2/CRO).

Metadata mining answers: *“How often do public records talk like culture Isolates?”*  
Type-strain audit answers: *“For exemplar type material, what was the actual Isolation→sequence path?”*

---

## 6. How it complements the type-strain audit

| | Type-strain audit | Metadata mining |
|--|-------------------|-----------------|
| Depth | High (paper → Isolate → accession) | Shallow (field text) |
| Breadth | Tens–hundreds | Thousands–millions |
| Best for | Inheritance risk on **type material** | Population trends on **wording** |
| Failure mode | Slow; sampling bias | Under-annotation; keyword false positives |

Together: audit grounds the mechanistic story for exemplars; mining shows whether culture advertising is rare or common in the public corpus—**without** overclaiming.

---

## 7. Concrete starter recipe (Entrez)

NCBI asks that you set a contact email and rate-limit requests. Example pattern with EDirect-style / URL API (illustrative):

### 7.1 Count viral RefSeq complete genomes (sketch)

```bash
# Install Entrez Direct (edirect) once, then:
esearch -db nucleotide -query 'Viruses[Organism] AND srcdb_refseq[PROP] AND "complete genome"[Title]' \
  | efetch -format docsum \
  | xtract -pattern DocumentSummary -element Caption AccessionVersion CreateDate
```

### 7.2 Pull GenBank flatfiles and grep metadata (sketch)

```bash
esearch -db nucleotide -query 'Viruses[Organism] AND srcdb_refseq[PROP] AND "complete genome"[Title]' \
  | efetch -format gb \
  > viral_refseq_complete.gb

# Then parse DEFINITION / COMMENT / /cell_line= / /lab_host= / /isolation_source=
# with Biopython SeqIO or a small Python parser — do not regex the sequence blocks.
```

### 7.3 Biopython Entrez sketch

```python
from Bio import Entrez
Entrez.email = "you@example.com"  # required courtesy

handle = Entrez.esearch(
    db="nucleotide",
    term='Viruses[Organism] AND srcdb_refseq[PROP] AND "complete genome"[Title]',
    retmax=0,  # useCount
)
record = Entrez.read(handle)
print("count", record["Count"])

# For a pilot, retmax=500–2000 IDs, then Entrez.efetch(db="nucleotide", id=..., rettype="gb", retmode="text")
# Parse only header/feature metadata; score keyword hits; aggregate by year and family.
```

### 7.4 NCBI Datasets alternative

```bash
datasets summary virus genome taxon Viruses --refseq --as-json-lines \
  | head  # inspect available metadata fields for a cleaner JSON pilot
```

(Exact CLI flags evolve; check current NCBI Datasets docs before a production run.)

---

## 8. Proposed metrics for a later pilot

| Metric ID | Definition | Use |
|-----------|------------|-----|
| M1 | % viral RefSeq complete genomes with any culture-cell keyword | Overall culture advertising |
| M2 | % with explicit CPE/cytopathic language | Stronger culture-endpoint advertising |
| M3 | M1 and M2 by year of deposit | Temporal trend |
| M4 | M1/M2 by family (ICTV / NCBI taxid) | Which taxa are culture-heavy in metadata |
| M5 | % with clinical-specimen keywords **and** no culture keywords | Lower-bound “clinical-looking” slice |
| M6 | Overlap: type-strain audit `high` rows that also hit M1/M2 | Concordance check |
| M7 | Audit `low` rows that nonetheless have culture keywords | Annotation noise / dual-path flag |

**Pilot scope suggestion:** start with RefSeq viral *complete genomes* only (manageable, curated), n in the low thousands—not all of GenBank.

**Reporting language:** “X% of sampled RefSeq viral complete genomes *mention* culture/CPE terms in metadata,” not “X% of viral genomes are culture artifacts.”

---

## 9. Tie-back to P3 parking note

From `p3.md`: sequence claims that use CPE-defined Isolates as type material **inherit** under-determination. Metadata mining can show how often public records *present themselves* in that culture register. Claims are limited to what the cited metadata corpus documents; this pilot does not replace deep type-material reading.

---

*Explainer v0.1 — 2026-09-19*

---

## 10. Pilot run 2026-09-19

Status: **pilot run 2026-09-19**. Outputs under `genbank_mining/`:

- `P3_genbank_mining_results_2026-09-19.md`
- `mining_summary.json`
- `refseq_viral_complete_metadata_sample.csv` (n=2000)
- `run_pilot.py`

See results write-up for M0–M7 and guardrails.
