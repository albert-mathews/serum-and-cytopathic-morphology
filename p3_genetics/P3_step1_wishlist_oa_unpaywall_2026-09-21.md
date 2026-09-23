# P3 Step 1 wishlist — Unpaywall OA audit

**Checked:** 2026-09-21 (ET)  
**Scope:** Every DOI in the wishlist DOI table, including both RUB-P1 candidates and the related Frey 1986 DOI.  
**Source:** Unpaywall API (`email=albert.mathews.research@gmail.com`), queried politely at approximately 1.1 seconds per DOI. No Sci-Hub, LibGen, pirate mirrors, or paywalled-PDF scraping used.

## Counts

| classification | n |
|---|---:|
| OA with direct PDF (`oa_pdf`) | **2** |
| OA but no direct PDF (`oa_no_pdf`) | **2** |
| Closed (`closed`) | **21** |
| **Total DOI records** | **25** |

Classification is based on `is_oa` plus Unpaywall `best_oa_location.url_for_pdf`; an OA landing page without a PDF endpoint is `oa_no_pdf`.

## Full results

| # | node / related | DOI | is_oa | oa_status | best PDF URL | host | license | version | classification |
|---:|---|---|---:|---|---|---|---|---|---|
| 1 | CMV-C1 | 10.1099/vir.0.79888-0 | True | green | <https://researchoutput.csu.edu.au/files/207614026/166388770_Published_article.pdf> | repository | other-oa | submittedVersion | oa_pdf |
| 2 | HBV-O1 | 10.1038/281646a0 | True | bronze | <https://www.nature.com/articles/281646a0.pdf> | publisher | — | publishedVersion | oa_pdf |
| 3 | ADE-O2 | 10.1016/s0021-9258(18)33473-2 | True | hybrid | — | publisher | cc-by | publishedVersion | oa_no_pdf |
| 4 | COV-O2 | 10.1126/science.1085952 | True | green | — | repository | other-oa | submittedVersion | oa_no_pdf |
| 5 | POL-P11 | 10.1016/0042-6822(66)90024-9 | False | closed | — | — | — | — | closed |
| 6 | POL-P4 | 10.1099/0022-1317-44-2-311 | False | closed | — | — | — | — | closed |
| 7 | ADE-C1 | 10.1016/0042-6822(92)90082-z | False | closed | — | — | — | — | closed |
| 8 | CMV-O1 | 10.1007/978-3-642-74980-3_6 | False | closed | — | — | — | — | closed |
| 9 | DEN-O1 | 10.1016/0042-6822(88)90406-0 | False | closed | — | — | — | — | closed |
| 10 | EBV-O1 | 10.1038/310207a0 | False | closed | — | — | — | — | closed |
| 11 | Frey 1986 (RUB RNA hop) | 10.1016/0042-6822(86)90446-0 | False | closed | — | — | — | — | closed |
| 12 | HPV-O1 | 10.1016/0042-6822(85)90214-4 | False | closed | — | — | — | — | closed |
| 13 | HSV-O1 | 10.1099/0022-1317-69-7-1531 | False | closed | — | — | — | — | closed |
| 14 | MEA-Enders | 10.3181/00379727-86-21073 | False | closed | — | — | — | — | closed |
| 15 | MEA-O1 | 10.1016/0042-6822(88)90564-8 | False | closed | — | — | — | — | closed |
| 16 | POL-P12 | 10.1016/0022-2836(79)90125-6 | False | closed | — | — | — | — | closed |
| 17 | RAB-O1 | 10.1016/0042-6822(88)90600-9 | False | closed | — | — | — | — | closed |
| 18 | RHV-P3 | 10.1007/BF01309297 | False | closed | — | — | — | — | closed |
| 19 | ROTA-O1 | 10.1016/0042-6822(90)90487-c | False | closed | — | — | — | — | closed |
| 20 | RUB-P1 | 10.1016/0042-6822(88)90395-9 | False | closed | — | — | — | — | closed |
| 21 | RUB-P1 | 10.1016/0042-6822(88)90615-0 | False | closed | — | — | — | — | closed |
| 22 | SV40-O1 | 10.1038/273113a0 | False | closed | — | — | — | — | closed |
| 23 | VAC-O1 | 10.1016/0042-6822(90)90294-2 | False | closed | — | — | — | — | closed |
| 24 | VZV-O1 | 10.1099/0022-1317-67-9-1759 | False | closed | — | — | — | — | closed |
| 25 | YFV-O1 | 10.1126/science.4023707 | False | closed | — | — | — | — | closed |

## Direct OA/publisher checks and download log

| DOI / node | check | result |
|---|---|---|
| `10.1099/vir.0.79888-0` / CMV-C1 | Unpaywall green repository PDF: `https://researchoutput.csu.edu.au/files/207614026/166388770_Published_article.pdf` | **Not downloaded:** repository returned HTTP 403 to a normal `curl -L`; skipped rather than bypassing the block. |
| `10.1038/281646a0` / HBV-O1 | Unpaywall bronze publisher PDF: `https://www.nature.com/articles/281646a0.pdf` | **Downloaded and verified:** `/workspace/p3_genetics/refs/sequence_origins/HBV-O1_galibert_1979_nature.pdf` (PDF magic; title/authors match Galibert et al. HBV ayw genome paper). |
| `10.1016/s0021-9258(18)33473-2` / ADE-O2 | Unpaywall publisher location is `hybrid`, `cc-by`, but supplies DOI landing page only (`url_for_pdf` absent). | **No download:** landing page only; no PDF scraped. |
| `10.1126/science.1085952` / COV-O2 | Unpaywall green Erasmus repository locations (`http://hdl.handle.net/1765/3917` and `http://repub.eur.nl/pub/3917`), submitted version, but no `url_for_pdf`. | **No download:** repository landing page only in Unpaywall record. |

### Downloaded OA PDFs

- `/workspace/p3_genetics/refs/sequence_origins/HBV-O1_galibert_1979_nature.pdf` — success; `%PDF-` magic and bibliographic title verified.

### Skipped / failed direct-PDF candidates

- `/workspace/p3_genetics/refs/sequence_origins/CMV-C1_dolan_2004_jgv.pdf` — not created; CSU repository returned HTTP 403.
- No other `url_for_pdf` values were present for the 25 DOI records.

## Notes

- The two critical polio DOI records are both `closed`: POL-P4 Lee (10.1099/0022-1317-44-2-311) and POL-P11 Baltimore (10.1016/0042-6822(66)90024-9).
- All records were retained, including the alternate RUB-P1 DOI and the related Frey DOI.
