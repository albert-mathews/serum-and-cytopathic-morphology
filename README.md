# serum-and-cytopathic-morphology

Working research repository and draft materials for a methods paper on **cell-culture growth medium (including FBS concentration)**, **cytopathic-effect (CPE) morphology**, and **virus Isolation practice**.

This repo is both a **record-keeping** archive and a **working** workspace: stream notes, extraction tables, and draft text live here so the project can be continued without re-deriving the literature trail from scratch.

## What is tracked vs ignored

### Tracked (intended for readers)

- Stream notes and synthesis (folders r1–r3 and p1–p3)
- Screening / overview CSVs and quote compilations
- Bibliography files (for example tex/references.bib, p1_history/P1_BIBLIOGRAPHY.md, and the stream useful/screened CSVs)
- Anonymized morphology result tables under r3_image_labeling/cro-results/ and r3_image_labeling/ir-results/
- Draft and framing text under tex/

Bibliographies and citation tables are the public pointer to sources. Readers can retrieve the same papers from publishers, libraries, or open repositories using those citations.

### Ignored (local only; do not commit)

Local copies of full-text references were kept on disk during research so authors could re-read and search sources without repeatedly downloading them. Many of those files are copyrighted publisher PDFs. They are **not** part of the public repository.

| Local path pattern | Why ignored |
|--------------------|-------------|
| Any folder named refs/ | Local reference corpora (PDFs and related full-text extracts used while working) |
| PDF files (*.pdf) | Publisher PDFs and similar binaries (copyright / size) |
| r3_image_labeling/images/ and images_rater_blinded/ | Large microscopy image packages |
| r3_image_labeling freelancer project folders and university_outreach.md | Expert-annotation project workspace and outreach identity materials |
| _private/ | Author-private notes |
| FOIA email export PDFs under p1_history/ | Personal correspondence about records requests |

See root .gitignore and r3_image_labeling/.gitignore for the exact patterns.

Typical local refs/ locations used while working (present on author machines, not in git):

- p1_history/refs/
- p2_virus_EV_indistinguishable_refs/refs/
- r1_isolation_standards_and_practice/refs/ (including isolation_practice/, isolation_protocols/, and related subfolders)
- r3_image_labeling/refs/

## Structure

| Kind | Folders | Role |
|------|---------|------|
| Research streams | r1_isolation_standards_and_practice, r2_negative_controls, r3_image_labeling | Isolation/guideline corpus, negative-control notes, morphology labeling |
| Discussion streams | p1_history, p2_virus_EV_indistinguishable_refs, p3_genetics | Medium-practice history, EV–virus particle indistinguishability notes, genetics (parked) |
| Draft | tex/ | Working narrative (DRAFT.md), framing notes, bibliography |

Each stream’s main markdown (r1.md, r2.md, p1.md, …) is the entry point for that topic.

## Scope note

This is a **methods / process** project about culture conditions and morphology readouts, scoped to Isolation practice and laboratory readouts rather than etiology claims.

Participant anonymity: contract laboratory and independent morphology raters are referred to only by role codes (for example CRO, IR1) in public files. See tex/FRAMING_LIMITATIONS_ANONYMITY.md.
