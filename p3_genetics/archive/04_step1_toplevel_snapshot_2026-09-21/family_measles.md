# Family: Measles (Morbillivirus / Edmonston)

**Date explored:** 2026-09-21 (ET), provenance-chain re-open  
**Status:** Step 1 IN PROGRESS — all events `chain_open`.

## Provenance chains
### MEA-O1 Crowley 1988
Paywalled. Abstract only: overlapping genomic cDNA library from MV-infected cells. **Must open Methods** for cell line, RNA prep, stock, any syncytia/CPE. `chain_open`.

### MEA-C1 Parks 2001 (OA PDF)
Quote: “Cell culture and MV propagation was performed as described in an accompanying article (33). The Edmonston wt isolate (11, 16) was a gift from Judy Beeler … Viral genome sequence was determined directly from … RNA extracted from infected Vero cells (33).” Edmonston wt “passaged 13 times (39)” before this analysis.  
Open pointers: accompanying paper (33); Beeler gift; passage-13 paper (39); vaccine lots from Bellini/Rota and commercial vials. Recoded off `culture_no_cpe`. `chain_open`.

### MEA-C2 Radecke 1995 (OA PDF)
Rescue in 293-3-46; Vero amplification; plaque purification by transferring syncytium — CPE-equivalent **for rescued virus**. Under stricter bar, the sequenced clone’s RNA/cDNA source is still an open pointer (not chased this pass). Previously `culture_cpe`; now `path_score=unclear`, `chain_open`.

Ballart/Cattaneo 1990 remains **retracted — excluded**.


## 2026-09-21 ~09:50 ET addendum — MEA-P1 opened
Parks accompanying article (cite 33) = Parks et al. *J Virol* 2001;75:910–920 PMID 11134304. OA PDF saved.

**Quote:** “Stocks of MV were prepared by infection of Vero cell monolayers at a multiplicity of infection of approximately 0.1 PFU per cell. Infected cells were harvested by scraping the monolayer when the cytopathic effect was detectable in 70 to 80% of the cell monolayer.” RNA: Trizol from infected Vero cells. Edmonston wt still “gift from Judy Beeler”; 13 passages historically.

**Status:** CPE harvest criterion now documented for sequenced-material production. Enders & Peebles 1954 (clinical isolation) still missing. **MEA-C1 remains `chain_open`.** Do not close path_score.

## Pass 21h (bar clarification)
- **MEA-O1 Crowley** `chain_closed` / `culture_cpe` — Edmonston/HeLa genomic RNA; Enders & Peebles 1954 cytopathogenic isolation upstream.
- **MEA-C1 Parks** `chain_closed` / `culture_cpe` — Vero harvest at 70–80% CPE + Enders lineage.
- Node MEA-Enders added.
