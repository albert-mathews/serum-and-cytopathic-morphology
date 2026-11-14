# R1 PDF wishlist

**Rule:** every corpus row should have a local PDF in `refs/isolation_practice/` (gitignored). Fetched → tell me → I confirm + clear.

**Still missing: 0 rows (corpus complete).**

Full title of the last-fetched item (VI279, confirmed on disk): "A conserved E1 stem motif functions as a virulence switch in the emerging Getah virus." *Virulence* 2026;17. Authors Xiang, Li, Wang, Ma, Ge, Gao, et al.

## Housekeeping (not fetch items)
- **VI254–VI261** (Mizuta JJID 2019) covered by `refs/isolation_practice/VI254 - Mizuta2019_JJID2018.500_microplate_isolation.pdf`.
- **VI262–VI263** (Mizuta JJID 2008) covered by `refs/isolation_practice/VI262 - Mizuta2008_JJID2008.196_microplate_isolation.pdf`.
- **VI245** → category-3 (`refs/methods_review_teaching/`).
- **VI271** removed (dup of institutional CDC Vero/hSLAM row).
- **VI238** removed (dup of institutional ANSES FMDV SOP row — post=0% FBS, pre not stated).
- **VI24** removed (2026-11-10, non-Isolation amphotericin-B drug-effect paper).
- **VI43** PDF image-scanned — OCR text present alongside; verify quotes before citing.
- Orphans on disk (not corpus): VI4, VI47.
- **Non-VI-ID PDFs in `refs/isolation_practice/`** (screened candidates / citation-chain support, not corpus rows): AHSV‑1968, AJVR1991 (PRRSV sows), Cardoso2000 + Ferreira2003 (VI227 growth-medium citations), Virus isolation titration 1975 (Fuchs & Wigand). See §"Orphan/support PDFs" below.
- **Duplicate PDF copies:** VI241 + VI242 are byte-identical to VI240 (McSwiggan ophthalmic 1981) — redundant.
- `excluded_pdfs/VI44` = Dengue NS1 antigen-detection method paper (*Viruses* 2020, 12:1105) — **not** an Isolation paper; misnamed "VI44" (collides with corpus VI44 = enteroviruses). Awaiting delete/keep call.

---

## Institutional PDF wishlist (every `institution-guideline-protocol-refs.csv` row needs a PDF in `refs/isolation_protocols/`)

**Rule:** one PDF per institutional row. Fetched → tell me → I confirm + clear. PDFs live in `refs/isolation_protocols/` (gitignored). Master-seed / extraneous-agent protocols are **not** Isolation protocols → they live in **R4** (`r4_non-isolation_standards_and_practice/refs/master_seed_protocols/`).

**Status (last reconciled 2026-11-14):** 5 institutional rows fully covered by a PDF; 3 outstanding (WHO EPI Annex B7/B8 wrong-doc, ANSES site down, CDC URL 404). USDA APHIS **VIRPRO1013** is **out of scope for R1** (non-Isolation master-seed protocol, handled by R4) and is therefore not an R1 fetch item.

| Institution | On-disk PDF | Status / action |
|---|---|---|
| ATCC Virology Culture Guide | ✅ `ATCC Virology Guide.pdf` | — |
| CLSI M41-A (Viral Culture) | ✅ `CLSI M41.M41AE_copypaste.pdf` | — |
| ASM Cytopathic Effects Protocols | ✅ `ASM cytopathic-effects-of-viruses-protocols.pdf` | — |
| NEADL / CIRAD PPRV SOP (VI27) | ✅ `NEADL - Virus isolation of peste des petits ruminants.pdf` | — |
| WOAH Terrestrial Manual (MERS-CoV ch.) | ✅ `WOAH... Chapter 3.5.2 MERS.pdf` (+ full manual) | — |
| WHO EPI (Measles/Rubella laboratory manual) | ⚠️ **annexes fetched are WRONG docs** (Annex B7 = 2025 RT-qPCR presentation; B8 = GRMLN Outbreak Response.docx) | **re-fetch correct Annex B7/B8** (Vero/hSLAM propagation + virus isolation). Manual URL below. |
| ANSES FMDV Virus Isolation SOP | ❌ none | **still fetch** — site under maintenance. URL: `https://sitesv2.anses.fr/sites/default/files/221216%20-%20Virus%20Isolation.pdf` |
| CDC Measles Lab Tools — Vero/hSLAM | ⚠️ `.docx` only | **URL is 404** (`.gov/measles/lab-tools/vero-slam.html`). Need replacement URL / archive. |
| Health Canada / CCDR Measles B95-a | ✅ `Health Canada - CCDR - H12-21-24-5-eng.pdf` | — |

**Notes:**
- **APHIS VIRPRO1013** is **out of scope for R1** (master-seed / extraneous-agent testing, not diagnostic Isolation); it lives in R4 and is not tracked here. The separate `APHIS - SAM 104.04` (Parainfluenza-3 isolation) in `refs/isolation_protocols/` **is** an Isolation SOP and stays in R1.
- **WHO EPI annexes**: the two fetched files do not match the manual's "Annex B7 (Propagation/maintenance of Vero/hSLAM)" and "Annex B8 (virus isolation in cell culture)." Re-fetch needed.
- **CDC Vero/hSLAM**: original URL is now 404; only the `.docx` (annex-b7) is local.
