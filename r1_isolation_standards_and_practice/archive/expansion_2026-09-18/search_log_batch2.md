# Search log — batch2 (pre-2005 / veterinary / arbovirus)

Agent: Grok executor (batch2, IDs VI200+)  
Date: 2026-09-14 (America/Toronto)

## Dedup baseline
- Skipped links in `/workspace/r1/existing_links.txt` (29 URLs).
- Skipped IDs already in overview CSV (VI2–VI47 / SPT10).
- Explicitly skipped PMC273643 / europepmc 6999024 (existing VI46 rabies).

## Search channels
1. **WebSearch** angles: `"maintenance medium" "2% FBS"`, `"Eagle's MEM" "2 per cent"`, veterinary journals, virus-name lists (FMDV, NDV, IBDV, PRRSV, BVDV, arboviruses, measles/mumps/rubella/polio historical).
2. **Europe PMC REST API** (`OPEN_ACCESS:y`, `FIRST_PDATE:[1965 TO 2005]`):
   - `"maintenance medium" AND "2%" AND (fetal OR FBS OR FCS)` → 134+ hits
   - `"virus isolation" AND "2%" AND (FBS OR FCS OR fetal)` → 194 hits
   - Combined veterinary virus names + maintenance medium → 82 hits
   - Deduped ~500+ unique records; filtered ~400 virus-related titles
3. **PMC HTML / Europe PMC `?pdf=render` / JSTAGE / Redalyc / Arch Razi** full-text pulls for quote verification.
4. **pdftotext** on ~40 OA PDFs for dual-serum sentence mining.

## Inclusion rule
- Only rows with **verbatim quotes** for serum % (no invented numbers).
- Prefer papers with both growth (pre) and maintenance/post-inoculation (post) stated.
- Allowed partial pre when post is explicit and pre is cited to a named prior method (noted).

## Yield
- **34 rows** written to `new_isolation_refs_batch2.csv` (VI200–VI233).
- **33/34** year ≤2005; focus pre-2005 / veterinary / arbovirus / classic isolation.
- Paywall / incomplete duals documented in `paywall_wishlist_batch2.md`.

## Notable virus coverage in this batch
TGEV, PEDV, PRRSV, IBR/BHV-1, FIPV, IBDV, ISAV, measles/SSPE, rhinovirus, enterovirus/adenovirus, influenza, parainfluenza, human CoV 229E, rat CoV, CHIKV, California encephalitis, JEV/YFV, WNV (borderline 2005), rabies (non-VI46 system), SARS-CoV 2004.

## Gaps remaining (for later batches)
FMDV primary BTY/IB-RS-2 dual quotes; ASFV/CSFV; NDV; bluetongue/AHSV full OA; canine distemper; feline calicivirus; Lassa culture methods; mumps/rubella classic with clean OA extract; polio historical.

