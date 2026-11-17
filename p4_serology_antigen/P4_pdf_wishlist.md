# P4 wishlist — fetch queue only (gitignored, local-only)

**This file is a fetch-only coordination queue, not a bibliography.** It lists only documents
still needed in `refs/`. When Albert drops a PDF, the assistant confirms the file is the correct
document (title/authors/identifier match), **then removes the row**. Fetched and read material is
recorded in the stream's two bibliographies (`P4_bibliography.md` = used; a `_unused` companion if
any fetch yields nothing), never here.

**Columns:** ID · Title · Year · Author · Identifier (PMID/DOI/stable URL) · Drop-as filename · Why needed · Status.

| ID | Title | Year | Author | Identifier | Drop-as filename | Why needed | Status |
|----|-------|------|--------|-----------|------------------|------------|--------|
| P4W-04 | ID Screen Infectious Bronchitis Competition (IBVC-2P) — manufacturer insert | current | ID Screen / Innovative Diagnostics | `innovative-diagnostics.com` (no public email) | `P4W-04 - ID_Screen_IB_Competition_IBVC-2P_IFU.pdf` | Completeness only: upgrade `p4_antigen_provenance.csv` P4-005 from catalogue to manufacturer insert | 2026-11-16: rep email delivered **2 of 3** inserts (Bluetongue Competition BTC + IB Indirect 2.0 IBVARSV2) — both renamed under `refs/P4W-04 - …` and rows P4-004/-006 upgraded. **IBVC-2P insert still outstanding; low priority** (provenance is traced via the literature, not the insert — see P4_reading_notes §5) |
| P4W-32 | Purification and characterization of the major group-specific core antigen VP7 of bluetongue virus synthesized by a recombinant baculovirus | 1990 | Oldfield S | PMID 2174958 · DOI 10.1099/0022-1317-71-11-2649 | `P4W-32 - Oldfield_1990_BTV10_VP7_baculovirus.pdf` | Citable provenance of recombinant VP7 (BTV-10, Sf9 baculovirus) behind P4-004 — the "recombinant VP7" antigen class | **cannot get** (2026-11-17, Albert). **Not a blocker** — P4W-34 (Ulisse 2021, BTV-2 recVP7 in Sf9) covers the same claim and is fetched/read. Keep as optional foundational citation only |

*End of P4 wishlist.*
