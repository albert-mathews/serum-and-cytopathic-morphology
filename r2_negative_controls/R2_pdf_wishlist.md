# R2 PDF wishlist (buy list only)

**Status (2026-11-18):** Albert fetched the outstanding items. **6 of 7 confirmed on disk and read** (removed from wishlist below; re-scored in `control-cultures-overview.csv` + `control-cultures-justification-notes.md` §Pass4):

| ID | Fetched as | Verdict |
|----|-----------|---------|
| VI44 | `r1_…/refs/isolation_practice/VI44 - enteroviruses_2003.pdf` | correct (Int J Infect Dis 7:138–142) → re-scored D |
| VI249 | `…/VI249 - IAV_swine_SFM_2013.pdf` | correct (JVDI 25(1):82–90, DOI 10.1177/1040638712470449) → **A** |
| VI251 | `…/VI251 - RSV-nasopharyngeal-aspirates.pdf` | correct (Mem Inst Oswaldo Cruz 101(4):451–453, **2006** — wishlist said 2004, which is the specimen window) → D |
| VI266 | `…/VI266 - HRSV_2023.pdf` | correct (JIDC 17(2):251–259, 10.3855/jidc.17462) → **B** |
| VI267 | `…/VI267 - HPIV_MNT1_2016.pdf` | correct (Microbiol Immunol, 10.1111/1348-0421.12446) → **B** |
| VI270 | `…/refs/methods_review_teaching/Lymphocystivirus-Iridoviridae_thesis.pdf` | correct (Le Deuff 1990 DEA, Archimer 51774 — wishlist said 1995; **1990** is right) → D |

> VI270 note: the IFREMER Archimer identifier (`https://archimer.ifremer.fr/doc/00406/51774/`) resolves to **Le Deuff Rose-Marie (1990)**, "Mise au point de méthodologies pour le diagnostic et l'étude de Lymphocystivirus (Iridoviridae)". The year in the old wishlist row (1995) was wrong; the fetched thesis is the correct document.

**Drop folder:** `r1_isolation_standards_and_practice/refs/` (shared with R1; gitignored) for isolation-practice items; VI270 landed in `methods_review_teaching/` (R1's area).

**Rule:** Only verified DOI / PMID / stable URL + exact drop name. These upgrade Tier D / abstract-only scores.

---

## Please fetch

| ID | Cite key | DOI / PMID / URL | Drop as |
| -- | -------- | ---------------- | ------- |
| VI271 | measles (clinical isolation) CDC Vero/hSLAM lab-tools page | `[DATA REQUIRED]` — old URL `https://www.cdc.gov/measles/lab-tools/vero-slam.html` is a live HTML page (not a PDF) and was reported "link not good". Need a **better identifier**: the CDC page's stable URL, an Internet Archive snapshot URL, or the underlying WHO/CDC guidance PDF it cites. | `R2_VI271_measles_clinical_isolation_n_d.pdf` |

## Notes

- **VI271** is a CDC lab-tools page (often unstable) — treat as optional / may stay D. It is the only remaining open wishlist row.
- After drop: re-open the R2 tier for VI271 in `control-cultures-overview.csv` + justification notes.
- Fetched/read items are recorded in the scored corpus (`control-cultures-overview.csv`) and `control-cultures-justification-notes.md` — not kept here.
