# P3 PDF catalogue and wishlist (sequence origins, Step 1)

**Single source of truth** for P3 literature holdings: what is on disk, what was used (bibliography), and what is still needed. Folded in on 2026-10-14 from six files (now removed):

- `sequence_origins/P3_step1_pdf_wishlist.md` (lean buy list, 2026-09-22) and its older, longer copy `p3_genetics/P3_step1_pdf_wishlist.md`;
- `sequence_origins/P3_step1_wishlist_dois_2026-09-21.md` and its identical copy at `p3_genetics/` (see "What the DOI file was" below);
- `sequence_origins/P3_step1_wishlist_oa_unpaywall_2026-09-21.md` and its identical copy at `p3_genetics/`.

**Drop folder:** `p3_genetics/refs/sequence_origins/` (gitignored; never commit PDFs). Verified DOI + exact drop name only; no Sci-Hub.
**Bibliography (used):** [`P3_sequence_origins_bibliography.md`](P3_sequence_origins_bibliography.md). **Read but unused:** [`P3_sequence_origins_read_but_unused.md`](P3_sequence_origins_read_but_unused.md). **Hop ledger:** [`P3_stock_origin_hops_2026-09-21.md`](P3_stock_origin_hops_2026-09-21.md).
**Last checked against disk:** 2026-10-14.

## Counts

| Measure | n |
|---|--:|
| Files in `refs/sequence_origins/` | 171 (170 PDF + 1 text extract) |
| Used: numbered entries in the bibliography (events + provenance nodes) | 159 |
| Used: hop / provenance sources added to the bibliography appendix 2026-10-14 | 22 |
| Read but unused | 3 |
| Items resolved in the 2026-09-21 DOI pass (43 IDs) now on disk | 42 |
| Still needed (see below) | 1 optional + 3 without a verified DOI |

## Please fetch

*Nothing required.* All Step 1 events that can be closed from literature are closed or recorded as such in `P3_step1_progress_summary.md`.

Optional:

| ID | Citation | DOI | Drop as | Note |
|---|---|---|---|---|
| RHV-P3 | Stanway et al. 1984 *Arch Virol* 81:67-78 (PMID 6331350) | `10.1007/BF01309297` | `RHV-P_stanway_1984_archvirol.pdf` | RHV-O1 closed without it (Stanway 1984 *NAR* HRV-14 is held and used) |
| Frey 1986 | Frey et al. 1986 *Virology*, rubella E1 cloning (PMID 3755848) | `10.1016/0042-6822(86)90446-0` | `RUB-P_frey_1986_virology.pdf` | Related RNA hop for RUB-O1; not a separate event |

Not requested (no verified DOI or not acquirable):

- Enders, Weller & Robbins 1952 *J Immunol* (`10.4049/jimmunol.69.6.673`): optional CPE companion to Enders 1949; Albert could not acquire. Drop name if found: `POL-P_enders_weller_robbins_1952_jimmunol.pdf`.
- Vaccinia Copenhagen calf-lymph / pre-Goebel history: cite not yet locked.
- FMDV Kaufbeuren first-isolation paper: not located; FMDV-O1 closed on Forss 1984 plaque Methods.

## What the DOI file was

`P3_step1_wishlist_dois_2026-09-21.md` was a one-off identifier-resolution pass (2026-09-21, Crossref + PubMed) over the rows that were then missing from the wishlist. It found a DOI for every row (one ambiguous: RUB-P1), plus later "pass e/f/g" blocker DOIs, 43 IDs in total. The companion Unpaywall file checked open-access status for 25 of those DOIs (2 OA with PDF, 2 OA landing page only, 21 closed). Those rows were then fetched by Albert; as of 2026-10-14, 42 of the 43 are on disk (the exception is RHV-P3, listed above). Both files were working records, not live wishlists. Their lasting content is kept here:

- **ADE-O2 Gingeras 1982 *JBC***: correct PMID is 7142161 (6334081 is Roberts 1984). Corrected in the bibliography 2026-10-14.
- **RUB-P1**: preferred Hemphill et al. 1988 *Virology* `10.1016/0042-6822(88)90395-9` (PMID 3336944); alternate Frey & Hemphill `10.1016/0042-6822(88)90615-0`. Held as `RUB-P_hemphill_1988.pdf`.
- **HBV-O1 Galibert 1979 *Nature*** `10.1038/281646a0`: an earlier publisher URL served the wrong article; the held file is title-verified.
- **HEND-P2**: the EID PMC PDF for `10.3201/eid0101.950107` was a wrong (unrelated) article; do not use. Murray 1995 *Science* is held.
- **COV-O2 Rota 2003**: the Science supplement shares the article DOI.

## Held, by role

- **Event (O/C) papers**: genome-deposit papers coded for path type; all listed in the bibliography with local file names.
- **Provenance (P) papers**: upstream stock-origin and method hops (e.g. HPIV3 Chanock 1958, HAV Provost 1979, RAB Kissling 1958); in the bibliography main list or its 2026-10-14 appendix.
- **Read but unused**: SFV Clegg & Kennedy 1974, LASSA Auperin 1989, CDC Urbani sequence dump.
