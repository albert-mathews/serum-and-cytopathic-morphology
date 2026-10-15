# Paper draft - working notes

**Manuscript:** [`tex/main.tex`](../main.tex) is a driver only; prose lives in [`tex/sections/`](../sections/) (one file per section), large tables in [`tex/tables/`](../tables/), packages and marker macros in [`tex/preamble.tex`](../preamble.tex). Journal-neutral; PLOS Biology structure. Compiles with pdflatex + bibtex (checked 2026-10-14, 8 pages). Started 2026-10-14; split into files 2026-10-14.
**Source notes:** [`tex/DRAFT.md`](../DRAFT.md) holds the verbatim guideline quotes (ATCC, CLSI M41-A, ASM, NEADL, WOAH) and the earlier R1 insert; it is kept unchanged as the quote source. `main.tex` cites it rather than re-typing quotes.
**Framing / limitations / anonymity:** [`tex/FRAMING_LIMITATIONS_ANONYMITY.md`](../FRAMING_LIMITATIONS_ANONYMITY.md) (limitations 1-5 are in the Limitations list).

Leave comments as `@Albert:` lines under the relevant row; replies as `@CPE:`.

## Section status

| Section | Status | Source files |
|---|---|---|
| Title, author block | placeholder | - |
| Abstract | drafted; FOIA sentence assumed | R1, R2, R3 results |
| Author summary | stub | - |
| Introduction | drafted | `tex/DRAFT.md`, `r1.md` snippets |
| Methods R1 (corpus, guidelines) | drafted | `R1_for_paper_2026-09-19.md` |
| Methods R1 (FOIA) | drafted, agency/scope missing | `wrk/foia_status.md` |
| Methods R2 | drafted | `r2.md`, `control-cultures.md` |
| Methods R3 (experiment, descriptors, CRO, raters) | drafted; CRO culture details missing | `r3.md`, `cro_labels_consolidation.md`, `ir-results/README.md` |
| Methods R3 (IR3v) | drafted with briefing condition withheld; Pass 2 pending | gitignored pilot review |
| Statistics | stub (test choice) | - |
| Results R1 | drafted; FOIA paragraph assumed | `fbs_distribution_summary.txt` |
| Results R2 | drafted | `r2.md` status 2026-09-22 |
| Results R3 CRO + IR1/IR2 | drafted | `IR1_IR2_pass2_side_by_side.md`, `IR1_IR2_pass1_side_by_side.md`, `cro_labels_consolidation.md` |
| Results R3 IR3v | provisional numbers | see register below |
| Figures | Fig 1 path set; Fig 2 awaiting selection | `viz_figures_review.md` |
| Discussion: principal finding, P1, P2 | drafted (short) | `P1_for_paper.md`, `P2_synthesis.md` |
| Discussion: P3 | deferred (coding not finished) | `p3_genetics/p3.md` |
| Discussion: P4-P7 | stub | `P4_P7_index.md` |
| Limitations | drafted | framing file |
| Data availability | drafted; repo release DOI missing | - |
| Back matter (contributions, funding, competing interests, ethics) | stubs | - |

## Assumption register (replace before submission)

All assumed text is wrapped in `\assumed{...}` (orange, "[ASSUMED -- pending FOIA]") or `\prov{...}` (blue, "[PROVISIONAL -- IR3v]") in `main.tex`, so it can be found by searching for those macros.

**A1 - FOIA outcome (R1).** Assumed by Albert 2026-10-14: most released protocols show a serum shift from 10% to a mean of about 15% at or after inoculation; distribution with many 10->10 and 10->20, few or zero 10->5. Appears in: Abstract (one sentence), Results R1 (paragraph after corpus numbers), Fig 1 caption, Discussion "Relation to practice", Limitations item 7. Replace with coded records when they arrive (`r1_isolation_standards_and_practice/wrk/foia_status.md`).

**A2 - IR3v Pass 1 coding (R3). Resolved 2026-10-14** by the rater's answers (private log in the gitignored pilot folder; public coding rules in `r3_image_labeling/ir-results/IR3v_pass1_side_by_side.md`). Shrinking -> rounded/shrinking (Ro); "vaculation" -> vacuolation, with the rater's single large vacuole coded separately (not V); refraction/refractive -> refractile (Re, not when describing the vacuole); projections: rule thin+late = stressed, thick+early = healthy-type, but no description states thickness, so all uncoded. Clarified counts (99 unique frames, duplicate excluded): any CRO-six A 36/50, B 40/49; V 31/30; Ro 8/12; Re 17/21; D 0/2; single vacuole 14/24; projections mentioned 10/32. Still wrapped in `\prov{...}` because Pass 2 is in progress.

**A3 - IR3v Pass 2.** In progress: checklist sent by Albert 2026-10-14, rater has started; marked `[PENDING]` until delivered and processed. The IR3v briefing condition is not described in tracked text until the rater has finished and been debriefed.

**Data note. Resolved 2026-10-14.** `CultureB_day4_08` = `CultureB_day4_07` (identical CRO source files 407/408). Decision: exclude the duplicate for all raters (IR1, IR2, IR3v, CRO) through `r3_image_labeling/frames_excluded_from_analysis.csv`; per-arm counts use 99 unique frames (50 A / 49 B). Methods sentence updated; numbers in Results and Table r3-cpe-by-source recomputed (e.g. IR1 Pass-2 CPE sum B 1.66 -> 1.65; IR2 Pass-1 any CPE B 26/50 -> 25/49; IR3v any CRO-six B 41/50 -> 40/49; BE kappa 0.45 -> 0.44). CRO 22 frames unchanged (408 has no single-frame description).

## Open author decisions (also in TODO.md)

1. Title and scope: does P3 enter this paper or a companion paper? Keep P2 as a Discussion paragraph?
2. CRO culture details for Methods (medium base, seeding, feeding, TEM days).
3. Inferential test for the A-B contrast.
4. R3 figure set (Fig 2).
5. FOIA agency/date/scope wording for Methods.
6. Composition of the 4 R2 rows beyond the 170 dual-FBS papers.
7. Zenodo AI-benchmark citation year/DOI.

## Build

`pdflatex main && bibtex main && pdflatex main && pdflatex main` in `tex/`. For PLOS submission flatten to one file (`latexpand main.tex > main_flat.tex`). Build outputs (`*.aux`, `*.log`, `*.pdf`) should stay untracked. Swap to the official PLOS template before submission.