# P3 Step 1 — PDF wishlist (blocking / high-value)

**Drop PDFs here:** `p3_genetics/refs/sequence_origins/` (gitignored)  
**Updated:** 2026-09-21 ~13:10 ET (pass **21h** — 39 user PDFs inventoried; evidentiary bar clarified; many chains closed)  
**DOI companion:** `P3_step1_wishlist_dois_2026-09-21.md`; OA results: `P3_step1_wishlist_oa_unpaywall_2026-09-21.md`


## Pass 21i status flips (closed events; PDFs already **have**)
Closed this pass on existing local PDFs: COV-O5, COV-O6, COV-O1, FMDV-O1, HAV-O1, RHV-O1, HEND-O1, AAV-O1, MUM-O1, NIPAH-C1, CDV-C1, WNV-C1, RSV-C1, COV-O4, BOCA-O1.
**Still blocked (high-value missing PDFs for denser culture_cpe / upstream):**
- HEND-P2 Murray 1995 Science (`10.1126/science.7701348`) — missing; EID PMC poisoned
- COV-MERS-P1 Zaki 2012 NEJM (`10.1056/NEJMoa1211721`) — missing
- CMV-O1 production: Rowe 1956 / AD169 isolate Methods (Chee chapter thin)
- RHV-P3 Stanway 1984 Arch Virol — missing (optional; RHV-O1 closed culture_no_cpe without it)
- FMDV Kaufbeuren first-isolation paper — missing (FMDV-O1 closed on Forss plaque Methods)
- Provost & Hilleman 1979 HAV culture procedure — missing OA (HAV-O1 closed on Najarian cite)
- HSV-O1, CHIK-O1 — could_not_obtain
- BK-Seif, SFV-P1 — missing PDFs
- Marra Tor2 SOM / Poutanen NEJM — optional CPE hunt (COV-O1 left culture_no_cpe)

## Pass-21h inventory of 39 newly dropped PDFs
All 39 filenames from `refs_new_user_pdfs_2026-09-21.tar` are on disk under `refs/sequence_origins/`. Status flips below.

**Albert annotations honored:**
- **HSV-O1 McGeoch** → `could_not_obtain` (leave missing)
- **CHIK-O1 Khan** → `could_not_obtain` (leave missing)
- **RUB-P1 Hemphill** → `have` (confirmed already present; Therien plaque paper DOI 10.1016/0042-6822(88)90395-9)
- **BK-Seif DOI** → **CORRECTED** — prior wishlist DOI `…90299-5` was wrong; real DOI is `10.1016/0092-8674(79)90209-5` (PMID 229976)
- **SFV-P1 Clegg & Kennedy 1974** → Albert “no DOI”: Crossref **does** list `10.1099/0022-1317-22-3-331` for the JGV poly(A) paper; PDF still missing
- **BK-O1 Yang Science PDF** → **have** (Albert 2026-09-21 re-download under correct DOI `10.1126/science.228391`; title-verified Yang & Wu BK MM complete). Prior `…451590` was wrong DOI.
- Passes E/F/G: user not yet reviewed; statuses updated only where PDF present

**Payload / OCR notes:** Baer EBV + Fiers SV40 are image Nature PDFs (OCR OK). Gompels HHV6 OCR OK (U1102). Choo/Jiang/Rota are multi-article Science PDFs containing the target articles.

---
## Critical (polio chain — shared RNA-isolation / stock hops)

| ID | Cite | Why needed | Status | OA check | DOI / alt-ID | Suggested filename |
| ---- | ------ | ------------ | -------- | --- | -------------- | -------------------- |
| POL-P4 | Lee YF, Kitamura N, Nomoto A, Wimmer E. Sequence studies of poliovirus RNA. IV. *J Gen Virol*. 1979;44:311–322. PMID 230285 | Kitamura & Wimmer 1980 + van der Werf 1981 defer **virion RNA isolation** here | **have (processed 2026-09-21h)** | closed | **10.1099/0022-1317-44-2-311** | `POL-P4_lee_1979_jgv.pdf` |
| POL-P11 | Baltimore D, Girard M, Darnell JE. Aspects of the synthesis of poliovirus RNA… *Virology*. 1966;29:179–189. PMID 4287327 | Spector 1975 defers **type-1 production** here (Baltimore-lab hop) | **have (processed 2026-09-21h)** | closed | **10.1016/0042-6822(66)90024-9** | `POL-P11_baltimore_girard_darnell_1966.pdf` |
| POL-P12 | Nomoto A et al. Defective interfering particles of poliovirus… *J Mol Biol*. 1979;128:179–196. PMID 219204 | Kitamura Fig.2 fingerprint-stability cite (23) | **have (processed 2026-09-21h)** | closed | **10.1016/0022-2836(79)90125-6** | `POL-P12_nomoto_1979_jmb.pdf` |

## High (starter-family Methods)

| ID | Cite | Why needed | Status | OA check | DOI / alt-ID | Suggested filename |
| ---- | ------ | ------------ | -------- | --- | -------------- | -------------------- |
| MEA-O1 | Crowley et al. *Virology* 1988;164:498–506. PMID 3369090 | Measles genome-completion Methods | **have (processed 2026-09-21h)** | closed | **10.1016/0042-6822(88)90564-8** | `MEA-O1_crowley_1988_virology.pdf` |
| MEA-P1 | Parks et al. *J Virol* 2001;75:910–920. PMID 11134304 | Propagation for Edmonston lineage (Parks cite 33) | **have** | — | 10.1128/JVI.75.2.910-920.2001 | `MEA-P_parks_edmonston_aa_2001_jvi.pdf` |
| MEA-Enders | Enders JF, Peebles TC. *Proc Soc Exp Biol Med* 1954;86:277–286. PMID 13177653 | First-principles Edmonston clinical isolation | **have (processed 2026-09-21h)** | closed | **10.3181/00379727-86-21073** | `MEA_enders_peebles_1954.pdf` |
| ADE-O2 | Gingeras et al. Nucleotide sequences from the adenovirus-2 genome. *JBC* 1982;257:13475–13491. **PMID 7142161** (NOT 6334081) | Ad2 sequence blocks Methods | **have (processed 2026-09-21h)** | oa_no_pdf | **10.1016/s0021-9258(18)33473-2** | `ADE-O2_gingeras_1982_jbc.pdf` |
| ADE-C1 | Chroboczek et al. *Virology* 1992;186:280–285. PMID 1727603 | Ad5 complete-genome Methods | **have (processed 2026-09-21h)** | closed | **10.1016/0042-6822(92)90082-z** | `ADE-C1_chroboczek_1992_virology.pdf` |
| CMV-O1 | Chee et al. *Curr Top Microbiol Immunol* 1990;154:125–169. PMID 2161319 | AD169 sequence chapter | **have (AD169 chapter; sample-prep thin — chain still open)** | closed | **10.1007/978-3-642-74980-3_6** | `CMV-O1_chee_1990_ctmi.pdf` |
| CMV-C1 | Dolan et al. *JGV* 2004;85:1301–1312. PMID 15105547 | Merlin Methods | **have (processed 2026-09-21h; Merlin closed)** | oa_pdf (403; not obtained) | **10.1099/vir.0.79888-0** | `CMV-C1_dolan_2004_jgv.pdf` |
| COV-O2 | Rota et al. *Science* 2003;300:1394–1399. PMID 12730500 (+ SOM) | Urbani SARS Methods/SOM | **have (processed 2026-09-21h; Urbani closed culture_cpe)** | oa_no_pdf | **10.1126/science.1085952** (SOM under same DOI; no separate SOM DOI found) | `COV-O2_rota_2003_science.pdf` |

## Tier B — newly have vs still missing

| ID | Cite | Status | OA check | DOI / alt-ID | Suggested filename |
| ---- | ------ | -------- | --- | -------------- | -------------------- |
| RHV-P1 | Cann et al. 1983 NAR PMID 6298739 | **have** | — | 10.1093/nar/11.5.1267 | `RHV-P_cann_1983_nar.pdf` |
| RHV-P2 | Minor 1980 JVI PMID 6246264 | **have** | — | 10.1128/JVI.34.1.73 | `RHV-P_minor_1980_jvi.pdf` |
| RHV-P3 | Stanway 1984 Arch Virol;81:67–78. PMID 6331350 | missing | closed | **10.1007/BF01309297** | `RHV-P_stanway_1984_archvirol.pdf` |
| HAV-O1 | Najarian 1985 PNAS PMID 2986127 | **have** | — | 10.1073/pnas.82.9.2627 | `HAV-O_najarian_1985_pnas.pdf` |
| HAV-O2 | Cohen wt 1987 JVI PMID 3023706 | **have** | — | 10.1128/JVI.61.1.50 | `HAV-O2_cohen_wt_1987_jvi.pdf` |
| HAV-C1 | Cohen attenuated 1987 PNAS PMID 3031686 | **have** | — | 10.1073/pnas.84.8.2497 | `HAV-O1_cohen_attenuated_1987_pnas.pdf` |
| RUB-O1 | Dominguez 1990 Virology PMID 2353453 | **have** | — | 10.1016/0042-6822(90)90474-6 | `RUB-O1_dominguez_1990_virology.pdf` |
| RUB-P1 | Hemphill 1988 (Therien plaque stock) — see notes | **have (Albert: already there — confirmed Hemphill 1988 Therien plaques; DOI 10.1016/0042-6822(88)90395-9)** | closed (both DOIs) | **AMBIGUOUS** — prefer **10.1016/0042-6822(88)90395-9** (Hemphill et al. Virology 1988; PMID 3336944); alt Frey & Hemphill DI **10.1016/0042-6822(88)90615-0** (PMID 3363865) | `RUB-P_hemphill_1988.pdf` |
| RAB-P1 | Tordo 1986 NAR PMID 3008096 | **have** | — | 10.1093/nar/14.6.2671 | `RAB-P_tordo_leader_np_1986_nar.pdf` |
| RAB-O1 | Tordo 1988 Virology;165:565–576. PMID 3407152 | **have (processed 2026-09-21h)** | closed | **10.1016/0042-6822(88)90600-9** | `RAB-O1_tordo_1988_virology.pdf` |
| FLU-P1 | Winter & Fields 1980 NAR PMID 6927841 | **have** | — | 10.1093/nar/8.9.1965 | `FLU-P_winter_fields_1980_nar.pdf` |
| FLU-P | Winter 1981 NAR subgenomic PMID 7335495 | **have** | — | 10.1093/nar/9.24.6907 | `FLU-P_winter_subgenomic_1981_nar.pdf` |
| VAC-O1 | Goebel 1990 Virology PMID 2219722 | **have (processed 2026-09-21h)** | closed | **10.1016/0042-6822(90)90294-2** | `VAC-O1_goebel_1990_virology.pdf` |
| HSV-O1 | McGeoch et al. Complete DNA sequence of HSV-1 UL. *JGV* 1988;69:1531–1574. PMID 2839594 | **could_not_obtain (Albert 2026-09-21)** | closed | **10.1099/0022-1317-69-7-1531** | `HSV-O1_mcgeoch.pdf` |
| VZV-O1 | Davison AJ, Scott JE. Complete DNA sequence of VZV. *JGV* 1986;67:1759–1816. PMID 3018124 | **have (processed 2026-09-21h)** | closed | **10.1099/0022-1317-67-9-1759** | `VZV-O1_davison.pdf` |
| EBV-O1 | Baer 1984 Nature PMID 6087149 | **have (image PDF; OCR processed 2026-09-21h; closed culture_no_cpe)** | closed | **10.1038/310207a0** | `EBV-O1_baer_1984_nature.pdf` |
| HPV-O1 | Seedorf et al. HPV16 DNA sequence. *Virology* 1985;145:181–185. PMID 2990099 | **have (processed 2026-09-21h)** | closed | **10.1016/0042-6822(85)90214-4** | `HPV-O1_seedorf_hpv16.pdf` |
| HBV-O1 | Galibert et al. HBV genome (ayw) cloned in *E. coli*. *Nature* 1979;281:646–650. PMID 399327 | **have** (OA PDF downloaded and title verified; DOI below is correct) | oa_pdf (have) | **10.1038/281646a0** | `HBV-O1_galibert_1979_nature.pdf` |
| YFV-O1 | Rice et al. *Science* 1985;229:726–733. PMID 4023707 | **have (processed 2026-09-21h; closed other/17D eggs)** | closed | **10.1126/science.4023707** | `YFV-O1_rice.pdf` |
| ROTA-O1 | Mitchell & Both 1990 Virology;177:324–331. PMID 2162107 | **have (processed 2026-09-21h)** | closed | **10.1016/0042-6822(90)90487-c** | `ROTA-O1_mitchell_both_1990.pdf` |
| SV40-O1 | Fiers et al. Complete nucleotide sequence of SV40 DNA. *Nature* 1978;273:113–120. PMID 205802 | **have (image PDF; OCR processed 2026-09-21h; closed culture_no_cpe)** | closed | **10.1038/273113a0** | `SV40-O1_fiers_1978_nature.pdf` |
| DEN-O1 | Hahn et al. *Virology* 1988;162:167–180. PMID 2827375 | **have (processed 2026-09-21h)** | closed | **10.1016/0042-6822(88)90406-0** | `DEN-O1_hahn_1988_virology.pdf` |

## Ambiguity / correction flags (2026-09-21 DOI pass)

1. **ADE-O2 Gingeras — wrong PMID on prior wishlist/bib.** PMID **6334081** is Roberts RJ et al. *JBC* 1984 “DNA sequences from the adenovirus 2 genome” (different paper). Correct Gingeras 1982 paper is PMID **7142161**, DOI **10.1016/s0021-9258(18)33473-2**. Events CSV already had the correct DOI.
2. **HBV-O1 Galibert — DOI is correct** (`10.1038/281646a0`, Nature 1979;281:646–650). Prior failure was a **wrong PDF payload** from a Nature URL, not a wrong bibliographic ID. Verify title/authors before trusting any download.
3. **RUB-P1 Hemphill — two 1988 Virology candidates.** Dominguez cites “Hemphill et al., 1988” (plural) for plaque-purified Therien → prefer Hemphill ML et al. time-course paper (PMID 3336944 / DOI 10.1016/0042-6822(88)90395-9). Alternate: Frey & Hemphill DI paper (PMID 3363865). Open Dominguez reference list to confirm before PDF chase.
4. **COV-O2 Rota SOM** — no separate Crossref DOI; Science supporting material rides under **10.1126/science.1085952**.

## Already have (do not re-download)
See `refs/sequence_origins/` — Kitamura user PDF, Racaniello, van der Werf, Nomoto Sabin, Flanegan/Spector/Yogo/Lee1977/Hewlett/Dorsch-Häsler/Kitamura1980 circle, Marra Tor2, Parks measles (both papers), Radecke, Stanway HRV-14, Cann, Minor, HAV trio, Dominguez, Tordo 1986, Winter 1980/1981, etc.

## Notes
- Drop any wishlist PDF into `refs/sequence_origins/`; next dig pass will quote Methods.
- Prefer publisher/library copies you may keep locally; we do not commit these.
- OA audit 2026-09-21: HBV-O1 PDF obtained and verified; CMV-C1 direct repository PDF returned HTTP 403 and was not bypassed; all other OA candidates lacked a direct PDF URL or were closed.
- Cross-refs: `P3_step1_progress_summary.md`; nodes CSV; bib; `P3_step1_wishlist_dois_2026-09-21.md`.


## New blockers / starts (2026-09-21 ~11:10 ET dig)

| ID | Cite | Status | OA check | DOI | Suggested filename |
| ---- | ------ | -------- | --- | --- | -------------------- |
| HBV-O1 | Galibert 1979 Nature | **have** (processed) | oa_pdf | 10.1038/281646a0 | `HBV-O1_galibert_1979_nature.pdf` |
| HBV-P1 | Charnay 1979 PNAS | **have** | PMC383570 | 10.1073/pnas.76.5.2222 | `HBV-P_charnay_1979_pnas.pdf` |
| HBV-P2 | Summers 1975 PNAS | **have** | PMC388770 | 10.1073/pnas.72.11.4597 | `HBV-P_summers_1975_pnas.pdf` |
| B19-O1 | Shade 1986 JVI | **have** | PMC253001 | 10.1128/jvi.58.3.921-936.1986 | `B19-O1_shade_1986_jvi.pdf` |
| B19-P1 | Cotmore 1986 JVI | **have** | PMC288924 | 10.1128/jvi.60.2.548-557.1986 | `B19-P_cotmore_1986_jvi.pdf` |
| JC-O1 | Frisque 1984 JVI | **have** | PMC254460 | 10.1128/jvi.51.2.458-469.1984 | `JC-O1_frisque_1984_jvi.pdf` |
| AAV-O1 | Srivastava 1983 JVI | **have** | PMC256449 | 10.1128/jvi.45.2.555-564.1983 | `AAV-O1_srivastava_1983_jvi.pdf` |
| HEV-O1 | Tam 1991 Virology | **have** | PMC7130833 | 10.1016/0042-6822(91)90760-9 | `HEV-O1_tam_1991_virology.pdf` |
| HEV-P1 | Reyes 1990 Science PMID 2107574 | **missing** | closed | **10.1126/science.2107574** | `HEV-P_reyes_1990_science.pdf` |
| MUM-O1 | Clarke 2000 JVI | **have** | PMC112006 | 10.1128/jvi.74.10.4831-4838.2000 | `MUM-C_clarke_2000_jvi.pdf` |
| VSV-P1/P2 | Rose/Gallione 1981 JVI | **have** | PMC171362/171363 | see events | `VSV-P_rose_1981_jvi.pdf` etc. |
| HCV-O1 | Choo 1989 Science PMID 2523562 | **have (Science multi-article PDF; Choo article present; closed other/chimp plasma)** | closed | **10.1126/science.2523562** | `HCV-O1_choo_1989_science.pdf` |
| RUB-P1 | Hemphill 1988 Virology 162:65-75 | **have (Albert: already there — confirmed Hemphill 1988 Therien plaques; DOI 10.1016/0042-6822(88)90395-9)** | closed | **10.1016/0042-6822(88)90395-9** | `RUB-P_hemphill_1988.pdf` |

## New blockers / starts (2026-09-21 ~11:35 ET dig — pass c)

| ID | Cite | Status | OA check | DOI | Suggested filename |
| ---- | ------ | -------- | --- | --- | -------------------- |
| HBV-P3 | Robinson et al. 1974 *J Virol* 14:384 | **have** (processed) | oa_pdf | 10.1128/jvi.14.2.384-391.1974 | `HBV-P_robinson_1974_jvi.pdf` |
| HBV-P4 | Kaplan et al. 1973 *J Virol* 12:995 | **have** (processed) | oa_pdf | 10.1128/jvi.12.5.995-1005.1973 | `HBV-P_kaplan_1973_jvi.pdf` |
| AAV-P1 | Hoggan/Blacklow/Rowe 1966 *PNAS* 55:1467 | **have** | oa_pdf | 10.1073/pnas.55.6.1467 | `AAV-P_hoggan_1966_pnas.pdf` |
| AAV-P2 | Rose et al. 1969 *PNAS* 64:863 | **have** | oa_pdf | 10.1073/pnas.64.3.863 | `AAV-P_rose_1969_pnas.pdf` |
| JC-P1 | Grinnell/Padgett/Walker 1983 *J Virol* 45:299 | **have** | oa_pdf | 10.1128/jvi.45.1.299-308.1983 | `JC-P_grinnell_1983_jvi.pdf` |
| JC-P2 | Frisque 1983 *J Virol* 46:170 | **have** | oa_pdf | 10.1128/jvi.46.1.170-176.1983 | `JC-P_frisque_1983_origin_jvi.pdf` |
| JC-P3 | Padgett et al. 1971 *Lancet* | **have (Padgett 1971; processed)** | closed | 10.1016/s0140-6736(71)91777-6 | `JC-P_padgett_1971_lancet.pdf` |
| VSV-P3 | Rose/Lodish/Brock 1977 *J Virol* 21:683 | **have** | oa_pdf | 10.1128/jvi.21.2.683-693.1977 | `VSV-P_rose_1977_jvi.pdf` |
| B19-P2 | Cossart et al. 1975 *Lancet* | **have (Cossart 1975; processed)** | closed | 10.1016/s0140-6736(75)91074-0 | `B19-P_cossart_1975_lancet.pdf` |
| HBV-Maupas | Maupas 1976 *Lancet* immunization | **have (Maupas 1976 immunization — supporting; not genome O)** | closed | 10.1016/s0140-6736(76)93023-3 | `HBV-P_maupas_1976_lancet.pdf` |
| RSV-O1 | Stec et al. 1991 *Virology* L gene | **have (processed 2026-09-21h)** | closed | 10.1016/0042-6822(91)90140-7 | `RSV-O1_stec_1991_virology.pdf` |
| RSV-P1 | Collins/Wertz 1985 *PNAS* G | **have** | oa_pdf | 10.1073/pnas.82.12.4075 | `RSV-P_collins_1985_G_pnas.pdf` |
| HPIV3-O1 | Stokes et al. 1992 *Virus Res* JS | **have (processed 2026-09-21h)** | closed | 10.1016/0168-1702(92)90102-f | `HPIV3-O1_stokes_1992_virusres.pdf` |
| NDV-O1 | de Leeuw & Peeters 1999 *JGV* LaSota | **have (processed 2026-09-21h)** | green metadata only | 10.1099/0022-1317-80-1-131 | `NDV-O1_deleeuw_1999_jgv.pdf` |
| NOR-O1 | Jiang et al. 1990 *Science* | **have (Science multi-article; Jiang Norwalk present; closed clinical_direct)** | closed | 10.1126/science.2177224 | `NOR-O1_jiang_1990_science.pdf` |
| NOR-P1 | Hardy et al. 1997 *Virus Genes* completion | **have (Hardy 1997)** | closed | 10.1007/BF00284649 | `NOR-P_hardy_1997_virusgenes.pdf` |
| BK-O1 | Yang & Wu 1979 *Science* | **have (title-verified; CLOSED culture_no_cpe 2026-09-21)** | closed | **10.1126/science.228391** | `BK-O1_yang_1979_science.pdf` |
| BK-Seif | Seif et al. 1979 *Cell* | **missing; DOI CORRECTED: wishlist had 10.1016/0092-8674(79)90209-5 — WRONG. Correct DOI is 10.1016/0092-8674(79)90209-5 (PMID 229976, Cell 1979;18:963-977 “The genome of human papovavirus BKV”). Albert was right to doubt.** | closed | 10.1016/0092-8674(79)90209-5 | `BK-P_seif_1979_cell.pdf` |
| HHV6-O1 | Gompels et al. 1995 *Virology* U1102 | **have (encrypted/image PDF; OCR processed; closed culture_no_cpe U1102/JJhan)** | hybrid/doi HTML | 10.1006/viro.1995.1228 | `HHV6-O1_gompels_1995_virology.pdf` |
| EBO-O1 | Sanchez et al. 1993 *Virus Res* | **have (processed 2026-09-21h)** | closed | 10.1016/0168-1702(93)90063-s | `EBO-O1_sanchez_1993_virusres.pdf` |
| CHIK-O1 | Khan et al. 2002 *JGV* S27 | **could_not_obtain (Albert 2026-09-21)** | closed | 10.1099/0022-1317-83-12-3075 | `CHIK-O1_khan_2002_jgv.pdf` |
| WNV-O1 | Lanciotti et al. 1999 *Science* NY99 | **have (processed 2026-09-21h)** | closed | 10.1126/science.286.5448.2333 | `WNV-O1_lanciotti_1999_science.pdf` |

## New blockers / starts (2026-09-21 ~11:40 ET dig — pass d)

| ID | Cite | Status | OA check | DOI | Suggested filename |
| ---- | ------ | -------- | --- | --- | -------------------- |
| FLU-B-P1 | Shaw/Air 1982 PNAS NA | **have** | oa_pdf | 10.1073/pnas.79.22.6817 | `FLU-B_P_shaw_air_NA_1982_pnas.pdf` |
| FLU-B-P2 | Briedis 1983 JVI NP | **have** | oa_pdf | 10.1128/jvi.47.3.642-648.1983 | `FLU-B_P_briedis_NP_1983_jvi.pdf` |
| FLU-B-P3 | Berton 1984 JVI HA | **have** | oa_pdf | 10.1128/jvi.52.3.919-927.1984 | `FLU-B_P_berton_webster_HA_1984_jvi.pdf` |
| SFV-O1 | Takkinen 1986 NAR | **have** | oa_pdf | 10.1093/nar/14.14.5667 | `SFV-O1_takkinen_1986_nar.pdf` |
| SFV-P1 | Clegg & Kennedy 1974 JGV | **missing PDF; Albert “no DOI” — Crossref DOES have DOI 10.1099/0022-1317-22-3-331 for Clegg & Kennedy JGV 1974;22:331 (Polyadenylic Acid Sequences… SFV). Note DOI exists.** | unknown | **10.1099/0022-1317-22-3-331** (Crossref; Albert thought none) | `SFV-P_clegg_kennedy_1974.pdf` |
| SIN-O1 | Strauss 1984 Virology | **have (processed 2026-09-21h)** | closed | 10.1016/0042-6822(84)90428-8 | `SIN-O1_strauss_1984_virology.pdf` |
| SIN-P1/P2 | Rice 1982 / Strauss 1983 PNAS | **have** | oa_pdf | 10.1073/pnas.79.17.5235 / 10.1073/pnas.80.17.5271 | `SIN-P_*.pdf` |
| ROTA-P1/2/3 | Both 1982/84/89 NAR | **have** | oa_pdf | see nodes | `ROTA-P_both_*.pdf` |
| BK-P1 | Yang 1980 JVI | **have** | oa_pdf | 10.1128/jvi.34.2.416-430.1980 | `BK-P_yang_wu_1980_jvi.pdf` |
| EV71-O1 | Brown 1995 Virus Res | **have (processed 2026-09-21h)** | closed | 10.1016/0168-1702(95)00087-9 | `EV71-O1_brown_1995_virusres.pdf` |
| EV71-C1 | Brown 1999 JVI | **have** | oa_pdf | 10.1128/jvi.73.12.9969-9975.1999 | `EV71-C_brown_1999_jvi.pdf` |
| COX-O1 | Lindberg 1987 Virology | **have (processed 2026-09-21h)** | closed | 10.1016/0042-6822(87)90435-1 | `COX-O1_lindberg_1987_virology.pdf` |
| HANTA-O1 | Schmaljohn 1987 Virology | **have (processed 2026-09-21h)** | closed | 10.1016/0042-6822(87)90310-2 | `HANTA-O1_schmaljohn_1987.pdf` |
| LCMV-O1 | Salvato 1989 Virology | **have (processed 2026-09-21h)** | closed | 10.1016/0042-6822(89)90216-x | `LCMV-O1_salvato_1989_virology.pdf` |
| LCMV-P1 | Salvato 1991 JVI | **have** | oa_pdf | 10.1128/JVI.65.4.1863-1869.1991 | `LCMV-P_salvato_1991_jvi.pdf` |
| REO-O1 | Cashdollar 1982 PNAS | **have** | oa_pdf | 10.1073/pnas.79.23.7644 | `REO-P_cashdollar_S2_1982_pnas.pdf` |
| REO-S3 | Richardson 1983 NAR | **have (Richardson S3 title-verified reovirus — prior PMC was wrong chloroplast payload)** | PMC326381 **wrong PDF payload** (chloroplast) — do not trust | 10.1093/nar/11.18.6399 | `REO-P_richardson_S3_1983_nar.pdf` |
| WNV-C1 | Beasley 2004 EID | **have** | oa_pdf | 10.3201/eid1012.040647 | `WNV-C_beasley_mexico_2004_eid.pdf` |
| RSV-C1 | Collins 1995 PNAS | **have** | oa_pdf | 10.1073/pnas.92.25.11563 | `RSV-C_collins_1995_pnas_rescue.pdf` |
| AAV-P3 | Rose/Hoggan/Shatkin 1966 PNAS | **have** | oa_pdf | 10.1073/pnas.56.1.86 | `AAV-P_rose_hoggan_shatkin_1966_pnas.pdf` |

Pass-c abstract-only O blockers rechecked Unpaywall: still closed (Stec, Stokes, Jiang, Yang Science, Seif, Gompels hybrid no PDF, Sanchez, Khan, Lanciotti). NDV WUR green landing still no usable PDF URL. CMV-C1 CSU repo still HTTP 403.

## New blockers / starts (2026-09-21 ~11:50 ET dig — pass e)

| ID | Cite | Status | OA check | DOI | Suggested filename |
| ---- | ------ | -------- | --- | --- | -------------------- |
| FMDV-O1 | Forss 1984 NAR | **have** | oa_pdf | 10.1093/nar/12.16.6587 | `FMDV-O1_forss_1984_nar.pdf` |
| BOCA-O1 | Allander 2005 PNAS | **have** | oa_pdf | 10.1073/pnas.0504666102 | `BOCA-O1_allander_2005_pnas.pdf` |
| COV-O4 | Woo 2005 HKU1 JVI | **have** | oa_pdf | 10.1128/JVI.79.2.884-895.2005 | `COV-HKU1_woo_2005_jvi.pdf` |
| COV-O5 | van der Hoek 2004 Nat Med | **have** | oa_pdf (PMC7095789) | 10.1038/nm1024 | `COV-NL63_vanderhoek_2004_natmed.pdf` |
| COV-O6 | van Boheemen 2012 mBio | **have** | oa_pdf | 10.1128/mBio.00473-12 | `COV-MERS_vanboheemen_2012_mbio.pdf` |
| NIPAH-C1 | Harcourt 2005 EID | **have** | oa_pdf | 10.3201/eid1110.050513 | `NIPAH-C_harcourt_bangladesh_2005_eid.pdf` |
| HEND-O1 | Wang 2000 JVI | **have** | oa_pdf | 10.1128/jvi.74.21.9972-9979.2000 | `HEND-O1_wang_2000_jvi.pdf` |
| HEND-P1 | Wang 1998 JVI | **have** | oa_pdf | 10.1128/JVI.72.2.1482-1490.1998 | `HEND-P_wang_1998_jvi_PVC.pdf` |
| ZIKV-C1 | Lanciotti 2008 EID | **have** | oa_pdf | 10.3201/eid1408.080287 | `ZIKV-C_lanciotti_2008_eid.pdf` |
| ZIKV-C2 | Baronti 2014 GenomeA | **have** | oa_pdf | 10.1128/genomeA.00500-14 | `ZIKV-C_baronti_2014_genomea.pdf` |
| ZIKV-O1 | Kuno 2007 Arch Virol | **missing** | Unpaywall oa but Springer PDF HTML | **10.1007/s00705-006-0903-z** | `ZIKV-O1_kuno_chang_2007.pdf` |
| NIPAH-O1 | Harcourt 2000 Virology | **missing** | oa metadata no pdf | **10.1006/viro.2000.0340** | `NIPAH-O1_harcourt_2000_virology.pdf` |
| MARB-O1 | Bukreyev 1995 Arch Virol | **missing** | closed | **10.1007/BF01322532** | `MARB-O1_bukreyev_1995.pdf` |
| LASSA-O1 | Auperin 1989 Virology | **missing** | closed | **10.1016/0042-6822(89)90287-0** | `LASSA-O1_auperin_1989.pdf` |
| ASTRO-O1 | Willcocks 1994 JGV | **missing** | closed | **10.1099/0022-1317-75-7-1785** | `ASTRO-O1_willcocks_1994.pdf` |
| HPIV1-O1 | Newman 2002 Virus Genes | **missing** | closed | **10.1023/a:1014042221888** | `HPIV1-O1_newman_2002.pdf` |
| FCV-O1 | Carter 1992 Virology | **missing** | closed | **10.1016/0042-6822(92)91231-i** | `FCV-O1_carter_1992.pdf` |
| MCPYV-O1 | Feng 2008 Science | **missing** | PMC2740911 render failed | **10.1126/science.1152586** | `MCPYV-O1_feng_2008_science.pdf` |
| BVDV-O1 | Collett 1988 Virology | **missing** | closed | **10.1016/0042-6822(88)90672-1** | `BVDV-O1_collett_1988.pdf` |

Pass-e Unpaywall recheck on Stec/Stokes/Jiang/Lanciotti-WNV/Khan: still closed. Kuno/Feng flagged oa without usable PDF URL this pass.

## New blockers / starts (2026-09-21 ~11:51 ET dig — pass f)

| ID | Cite | Status | OA check | DOI | Suggested filename |
| ---- | ------ | -------- | --- | --- | -------------------- |
| CSFV-C1 | Ruggli 1996 JVI Alfort/187 | **have** | oa_pdf PMC190221 | 10.1128/JVI.70.6.3478-3487.1996 | `CSFV-C1_ruggli_alfort187_1996_jvi.pdf` |
| BTV-C1 | Maan 2010 PLoS ONE BTV-6 | **have** | oa_pdf | 10.1371/journal.pone.0010323 | `BTV-C_maan_btv6_2010_plosone.pdf` |
| CDV-C1 | Lednicky 2004 Virol J | **have** | oa_pdf PMC524033 | 10.1186/1743-422X-1-2 | `CDV-C_lednicky_2004_virolj.pdf` |
| CDV-C2 | Loots 2017 GenomeA | **have** | oa_pdf PMC5502862 | 10.1128/genomeA.00603-17 | `CDV-C_loots_2017_genomea.pdf` |
| SAPO-C1 | Hallström 2017 GenomeA | **have** | oa_pdf PMC5289670 | 10.1128/genomeA.01446-16 | `SAPO-C_yac_2017_genomea.pdf` |
| HEND-P2 | Murray 1995 Science | **missing** | closed; EID PMC poisoned | **10.1126/science.7701348** | `HEND-P_murray_1995_science.pdf` |
| COV-MERS-P1 | Zaki 2012 NEJM | **missing** | green no usable PDF | **10.1056/NEJMoa1211721** | `COV-MERS-P_zaki_2012_nejm.pdf` |
| NIPAH-P1 | Chua 2000 Science | **missing** | closed | **10.1126/science.288.5470.1432** | `NIPAH-P_chua_2000_science.pdf` |
| ZIKV-P1 | Dick 1952 TRSTMH | **missing** | closed | **10.1016/0035-9203(52)90042-4** | `ZIKV-P_dick_1952_trstmh.pdf` |
| BTV-O1 | Fukusho 1989 JGV | **missing** | closed | **10.1099/0022-1317-70-7-1677** | `BTV-O1_fukusho_1989_jgv.pdf` |
| CDV-O1 | Sidhu 1993 Virology | **missing** | closed | **10.1006/viro.1993.1103** | `CDV-O1_sidhu_1993_virology.pdf` |
| CSFV-O1 | Meyers 1989 Virology | **missing** | closed | **10.1016/0042-6822(89)90625-9** | `CSFV-O1_meyers_1989_virology.pdf` |
| SAPO-O1 | Numata 1997 Arch Virol | **missing** | closed | **10.1007/s007050050178** | `SAPO-O1_numata_1997_archvirol.pdf` |
| FMDV-Küpper | Küpper 1981 Nature | **missing** | closed | **10.1038/289555a0** | `FMDV-P_kupper_1981_nature.pdf` |

Pass-f note: Murray EID PMC2626820/CDC PDF returned **wrong Lyme disease article** — discarded. Do not trust that PMCID PDF blob.

## New blockers / starts (2026-09-21 ~11:55 ET dig — pass g mop-up)

| ID | Cite | Status | OA check | DOI | Suggested filename |
| ---- | ------ | -------- | --- | --- | -------------------- |
| COV-O7 | Thiel 2001 JGV Inf-1 229E | **missing** (abstract) | closed | **10.1099/0022-1317-82-6-1273** | `COV-229E_O_thiel_2001_jgv.pdf` |
| COV-229E-P1 | Thiel 2001 JVI replicase companion | **have** | oa_pdf PMC114390 | 10.1128/jvi.75.14.6676-6681.2001 | `COV-229E_P_thiel_replicase_2001_jvi.pdf` |
| COV-229E-P_hamre | Hamre & Procknow 1966 PSEBM | **missing** | not forced | **10.3181/00379727-121-30734** | `COV-229E_P_hamre_1966_psebm.pdf` |
| COV-C4 | Farsani 2012 Virus Genes | **have** | oa_pdf PMC7088690 | 10.1007/s11262-012-0807-9 | `COV-229E_C_farsani_2012_virusgenes.pdf` |
| COV-O8 | Wu 2020 Nature Wuhan-Hu-1 | **have (Wu 2020; CLOSED clinical_direct 2026-09-21h)** | Nature hybrid OA | 10.1038/s41586-020-2008-3 | `COV-SARS2_wu_2020_nature.pdf` |
| COV-C5 | Zhou 2020 Nature WIV04 | **have (Zhou 2020; CLOSED culture_cpe 2026-09-21h)** | Nature hybrid OA | 10.1038/s41586-020-2012-7 | `COV-SARS2_zhou_2020_nature.pdf` |

Pass-g note: Springer PDF for Farsani blocked HTML; EuropePMC title-verified OK. Thiel JGV still closed. **No Sci-Hub. OA trail for expansion-list families largely exhausted.**
