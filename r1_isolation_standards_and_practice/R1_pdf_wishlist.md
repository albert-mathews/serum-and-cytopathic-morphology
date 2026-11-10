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
- **VI43** PDF image-scanned — needs OCR.
- Orphans on disk (not corpus): VI4, VI47.

---

## Institutional PDF wishlist (every `institution-guideline-protocol-refs.csv` row needs a PDF in `refs/isolation_protocols/`)

**Rule:** one PDF per institutional row. Fetched → tell me → I confirm + clear. PDFs live in `refs/isolation_protocols/` (gitignored).

| Institution | On-disk PDF | Status / action |
|---|---|---|
| ATCC Virology Culture Guide | ✅ `ATCC Virology Guide.pdf` | — |
| CLSI M41-A (Viral Culture) | ✅ `CLSI M41.M41AE_copypaste.pdf` | — |
| ASM Cytopathic Effects Protocols | ✅ `ASM cytopathic-effects-of-viruses-protocols.pdf` | — |
| NEADL / CIRAD PPRV SOP (VI27) | ✅ `NEADL - Virus isolation of peste des petits ruminants.pdf` | — |
| WOAH Terrestrial Manual (MERS-CoV ch.) | ✅ `WOAH... Chapter 3.5.2 MERS.pdf` (+ full manual) | — |
| USDA APHIS VIRPRO1013 (9 CFR §§113.55/113.46) | ✅ **in R4** `r4_…/refs/master_seed_protocols/APHIS - VIRPRO1013.pdf` (+ SAM312) | **→ re-home to R4** (master-seed protocol, not Isolation). R1 `institution-…csv` row flagged for removal. |
| WHO EPI (Measles/Rubella laboratory manual) | ⚠️ **annexes fetched are WRONG docs** (Annex B7 = 2025 RT-qPCR presentation; B8 = GRMLN Outbreak Response.docx) | **re-fetch correct Annex B7/B8** (Vero/hSLAM propagation + virus isolation). Manual URL below. |
| ANSES FMDV Virus Isolation SOP | ❌ none | **still fetch** — site under maintenance. URL: `https://sitesv2.anses.fr/sites/default/files/221216%20-%20Virus%20Isolation.pdf` |
| CDC Measles Lab Tools — Vero/hSLAM | ⚠️ `.docx` only | **URL is 404** (`.gov/measles/lab-tools/vero-slam.html`). Need replacement URL / archive. |
| Health Canada / CCDR Measles B95-a | ✅ `Health Canada - CCDR - H12-21-24-5-eng.pdf` | — |

**Notes:**
- **APHIS VIRPRO1013** is a master-seed (MSV extraneous-agent) protocol → belongs in **R4**, not R1 Isolation. PDFs live in `r4_non-isolation_standards_and_practice/refs/master_seed_protocols/` (`APHIS - VIRPRO1013.pdf`, `APHIS - SAM312 - Detection of Extraneous Cytopathogenic Agents in Master Seed Virus.pdf`). The separate `APHIS - SAM 104.04` (Parainfluenza-3 isolation) in `refs/isolation_protocols/` **is** an Isolation SOP and stays in R1.
- **WHO EPI annexes**: the two fetched files do not match the manual's "Annex B7 (Propagation/maintenance of Vero/hSLAM)" and "Annex B8 (virus isolation in cell culture)." Re-fetch needed.
- **CDC Vero/hSLAM**: original URL is now 404; only the `.docx` (annex-b7) is local.
