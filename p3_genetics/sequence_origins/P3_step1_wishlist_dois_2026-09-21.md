# P3 Step 1 wishlist — DOI / stable-ID resolution

**Date:** 2026-09-21 ~10:37 ET  
**Scope:** Still-missing rows on `P3_step1_pdf_wishlist.md` only (identifiers; **no PDFs downloaded**).  
**Sources:** Crossref API, PubMed E-utilities, DOI.org metadata. No Sci-Hub / LibGen / pirate mirrors.

## Counts

| outcome | n |
|---------|---|
| Resolved unique DOI | **22** |
| Ambiguous (multiple candidates; preferred DOI listed) | **1** (RUB-P1) |
| Explicit no DOI | **0** |
| Lookup failures | **0** |
| Corrections vs prior bib/wishlist | **2** (ADE-O2 wrong PMID; HBV-O1 DOI OK / prior PDF wrong) |

Missing rows processed: **23** (including ADE-O2 / HBV-O1 / RUB-P1 flags).

## Critical polio blockers (exact DOIs)

| node_id | citation | DOI |
|---------|----------|-----|
| **POL-P4** | Lee YF, Kitamura N, Nomoto A, Wimmer E. Sequence studies of poliovirus RNA. IV. *J Gen Virol*. 1979;44:311–322. PMID 230285 | **10.1099/0022-1317-44-2-311** |
| **POL-P11** | Baltimore D, Girard M, Darnell JE. Aspects of the synthesis of poliovirus RNA and the formation of virus particles. *Virology*. 1966;29:179–189. PMID 4287327 | **10.1016/0042-6822(66)90024-9** |

Also critical-adjacent: **POL-P12** Nomoto 1979 JMB → **10.1016/0022-2836(79)90125-6** (PMID 219204).

## Full table (missing items only)

| node_id | citation | DOI | notes |
|---------|----------|-----|-------|
| POL-P4 | Lee et al. 1979 *J Gen Virol* 44:311 | 10.1099/0022-1317-44-2-311 | PMID 230285; DOI already known; still paywalled |
| POL-P11 | Baltimore, Girard, Darnell 1966 *Virology* 29:179 | 10.1016/0042-6822(66)90024-9 | PMID 4287327 |
| POL-P12 | Nomoto et al. 1979 *J Mol Biol* 128:179 | 10.1016/0022-2836(79)90125-6 | PMID 219204 |
| MEA-O1 | Crowley et al. 1988 *Virology* 164:498 | 10.1016/0042-6822(88)90564-8 | PMID 3369090 |
| MEA-Enders | Enders & Peebles 1954 *Proc Soc Exp Biol Med* 86:277 | 10.3181/00379727-86-21073 | PMID 13177653 |
| ADE-O2 | Gingeras et al. 1982 *J Biol Chem* 257:13475 | 10.1016/s0021-9258(18)33473-2 | **Correct PMID 7142161.** Prior wishlist PMID 6334081 = Roberts 1984 *wrong paper* |
| ADE-C1 | Chroboczek et al. 1992 *Virology* 186:280 | 10.1016/0042-6822(92)90082-z | PMID 1727603 |
| CMV-O1 | Chee et al. 1990 *CTMI* 154:125 | 10.1007/978-3-642-74980-3_6 | PMID 2161319 (book chapter DOI) |
| CMV-C1 | Dolan et al. 2004 *J Gen Virol* 85:1301 | 10.1099/vir.0.79888-0 | PMID 15105547 |
| COV-O2 | Rota et al. 2003 *Science* 300:1394 | 10.1126/science.1085952 | PMID 12730500; **SOM shares this DOI** (no separate SOM DOI in Crossref) |
| RHV-P3 | Stanway et al. 1984 *Arch Virol* 81:67 | 10.1007/BF01309297 | PMID 6331350 |
| RUB-P1 | Hemphill 1988 (Therien plaque stock) | **10.1016/0042-6822(88)90395-9** (preferred) | **AMBIGUOUS.** Prefer Hemphill et al. *Virology* 1988 time-course (PMID 3336944). Alt: Frey & Hemphill DI 10.1016/0042-6822(88)90615-0 (PMID 3363865). Dominguez “Hemphill et al.” (plural) favors preferred |
| RAB-O1 | Tordo et al. 1988 *Virology* 165:565 | 10.1016/0042-6822(88)90600-9 | PMID 3407152 |
| VAC-O1 | Goebel et al. 1990 *Virology* 179:247 | 10.1016/0042-6822(90)90294-2 | PMID 2219722 |
| HSV-O1 | McGeoch et al. 1988 *J Gen Virol* 69:1531 | 10.1099/0022-1317-69-7-1531 | PMID 2839594 |
| VZV-O1 | Davison & Scott 1986 *J Gen Virol* 67:1759 | 10.1099/0022-1317-67-9-1759 | PMID 3018124 |
| EBV-O1 | Baer et al. 1984 *Nature* 310:207 | 10.1038/310207a0 | PMID 6087149 |
| HPV-O1 | Seedorf et al. 1985 *Virology* 145:181 | 10.1016/0042-6822(85)90214-4 | PMID 2990099 |
| HBV-O1 | Galibert et al. 1979 *Nature* 281:646 | 10.1038/281646a0 | PMID 399327. **DOI correct;** prior Nature URL served wrong article PDF — verify title before use |
| YFV-O1 | Rice et al. 1985 *Science* 229:726 | 10.1126/science.4023707 | PMID 4023707 |
| ROTA-O1 | Mitchell & Both 1990 *Virology* 177:324 | 10.1016/0042-6822(90)90487-c | PMID 2162107 |
| SV40-O1 | Fiers et al. 1978 *Nature* 273:113 | 10.1038/273113a0 | PMID 205802 |
| DEN-O1 | Hahn et al. 1988 *Virology* 162:167 | 10.1016/0042-6822(88)90406-0 | PMID 2827375 |

## Related (named hop, not a separate wishlist row)

| related | citation | DOI | notes |
|---------|----------|-----|-------|
| Frey 1986 (RUB RNA hop) | Frey et al. Molecular cloning… rubella E1. *Virology* 1986. PMID 3755848 | 10.1016/0042-6822(86)90446-0 | Dominguez also defers RNA isolation here; not on wishlist as its own ID |

## Method notes

- Crossref `works?query.bibliographic=` + PubMed `esummary` articleids `doi`.
- Gingeras PubMed record (7142161) has no DOI field; DOI taken from Crossref work `10.1016/s0021-9258(18)33473-2` (title/authors/vol match).
- No item required a “no DOI” fallback; all missing rows either have a DOI or an explicit preferred DOI among candidates.
- Files updated: this companion + `P3_step1_pdf_wishlist.md` (DOI column added; “have” rows preserved).

## Pass e new blocker DOIs (Crossref/PubMed 2026-09-21)
- ZIKV-O1 Kuno: 10.1007/s00705-006-0903-z
- NIPAH-O1 Harcourt 2000: 10.1006/viro.2000.0340
- MARB-O1 Bukreyev: 10.1007/BF01322532
- LASSA-O1 Auperin: 10.1016/0042-6822(89)90287-0
- ASTRO-O1 Willcocks: 10.1099/0022-1317-75-7-1785
- HPIV1-O1 Newman: 10.1023/a:1014042221888
- FCV-O1 Carter: 10.1016/0042-6822(92)91231-i
- MCPYV-O1 Feng: 10.1126/science.1152586
- BVDV-O1 Collett: 10.1016/0042-6822(88)90672-1

## Pass f new blocker DOIs (Crossref/PubMed/Unpaywall 2026-09-21 ~11:51 ET)
- HEND-P2 Murray Science: 10.1126/science.7701348 (closed; EID 10.3201/eid0101.950107 PMC PDF poisoned/wrong Lyme article — do not use)
- COV-MERS-P1 Zaki NEJM: 10.1056/NEJMoa1211721 (Unpaywall green; no usable PDF URL / NEJM+Erasmus blocked)
- NIPAH-P1 Chua Science: 10.1126/science.288.5470.1432 (closed)
- ZIKV-P1 Dick 1952: 10.1016/0035-9203(52)90042-4 (closed)
- BTV-O1 Fukusho 1989 JGV: 10.1099/0022-1317-70-7-1677 (closed)
- CDV-O1 Sidhu 1993: 10.1006/viro.1993.1103 (closed)
- CSFV-O1 Meyers 1989: 10.1016/0042-6822(89)90625-9 (closed)
- SAPO-O1 Numata 1997: 10.1007/s007050050178 (closed)
- FMDV Küpper 1981 Nature (cDNA/expression): 10.1038/289555a0 (closed; Kaufbeuren field isolation paper still unlocated as OA)

## Pass g new blocker DOIs (2026-09-21 ~11:55 ET)
- COV-O7 Thiel 2001 JGV Inf-1: **10.1099/0022-1317-82-6-1273** (PMID 11369870; closed)
- COV-229E-P_hamre Hamre 1966: **10.3181/00379727-121-30734** (PMID 4285768)
- (have, not blockers) Farsani 10.1007/s11262-012-0807-9; Wu 10.1038/s41586-020-2008-3; Zhou 10.1038/s41586-020-2012-7; Thiel JVI 10.1128/jvi.75.14.6676-6681.2001
