# P3 Step 5 (secondary) — R1 dual-FBS Isolate→sequence fraction

**Generated:** 2026-09-23 ~10:10 ET (VI32/34/36/41/43/45 local-PDF recode)
**Corpus:** `isolation-refs-dual-fbs_only.csv` (n=170)  
**Coding CSV:** `P3_step5_r1_dual_fbs_isolate_to_sequence.csv`  
**Soft bar:** documentary method↔deposit/sequence mention within reasonable doubt — **not** forensic custody of material from CPE well to sequencer.

## Role (vs Step 1)

Step 5 is **secondary** to Step 1b / sequence-origin events. It asks whether **modern Isolation-practice papers** in the dual-FBS corpus still chain Isolate / culture±CPE → genetic characterization (sequencing, genome, GenBank/GISAID deposit, RT-PCR product sequenced, etc.).

It does **not** claim that these Isolation papers are the genesis of type / reference genomes. That warrant lives in Step 1 O-events (`P3_sequence_origin_events.csv`). Overlap of names is incidental.

## Counts

| Code | n | % of 170 |
|------|---|----------|
| `seq_yes` | 96 | 56.5% |
| `seq_no` | 58 | 34.1% |
| `seq_unclear` | 16 | 9.4% |
| **Total coded** | **170** | 100% |

- **% seq_yes among coded (all rows):** 56.5%
- **% seq_yes among yes+no (excl. unclear):** 62.3% (96/154)
- **High-confidence rows:** 114 / 170 (mostly EuropePMC full text or OA PDF)
- **Full-text (EPMC XML or OA PDF) available:** 130 / 170
- **Needs PDF/OA (insufficient text):** 0 (VI32/34/36/41/43/45 recoded from local MSI `refs/isolation_practice/` PDFs on 2026-09-23)

### Rough era pattern (supportive, not a formal stratified claim)

| Decade | seq_yes / n | % seq_yes |
|--------|-------------|----------|
| 1960s–1990s | 1 / 38 | ~3% |
| 2000s | 7 / 19 | 37% |
| 2010s | 14 / 23 | 61% |
| 2020s | 71 / 89 | 80% |

Modern dual-FBS Isolation papers commonly report sequencing or deposit; older Isolation/CPE practice papers usually do not.

## Code definitions (applied)

- **`seq_yes`:** Paper states sequencing / genome / RT-PCR product sequenced / GenBank–GISAID–ENA accession / genetic or molecular characterization tied to the isolate or culture material (soft bar).
- **`seq_no`:** Isolation/CPE (or related culture) paper with no genetic characterization claimed in available text.
- **`seq_unclear`:** Ambiguous — PCR detection only; “molecular confirmation” vague; genome-engineering / reporter constructs without clear isolate characterization; or insufficient OA text.

## Top caveats

1. **Isolation papers ≠ type-genome origins.** A 2024 dual-FBS Isolation+WGS paper does not rewrite Step 1 provenance for measles/polio/adeno/etc. Step 5 measures practice chaining, not ontology genesis.
2. **Soft bar, not custody.** We did not require unbroken chain-of-custody from a named CPE well to a named accession. Documentary co-mention of Isolate/culture and sequencing/deposit was enough.
3. **Access asymmetry.** 6 rows lack usable OA full text/abstract after EuropePMC + Unpaywall (no Sci-Hub). `seq_unclear` / low confidence there is a gap, not evidence of absence.
4. **CSV link quality.** Example: `VI8` virus field says SARS-CoV-2 (2020) but the stored PubMed link is PMID 6134854 (1983 HFRS). Coded the **linked paper** (`seq_no`); flagged in notes.
5. **Reference-section false friends.** Some hits to “sequence analysis” / “phylogenetic analysis” live only in bibliographies. References were stripped when a clear References header existed; remaining edge cases were manually overridden (e.g. `VI250` → `seq_no`).
6. **Culture used ≠ sequenced.** Example: `VI42` propagates VZV Jones isolate in MeWo but is an ORF29p localization study (protein homology accessions only) → `seq_no`.
7. **PCR ≠ sequence.** Detection/qRT-PCR confirmation without claimed sequencing → `seq_unclear` or `seq_no` (e.g. `VI264`, `VI283`).
8. **Duplicate arms / shared PDFs.** Some IDs share one paper (e.g. `VI262`/`VI263` microplate arms; `VI254`–`VI261` JJID epidemiology PDF). Codes follow the shared text.
9. **MSI `expansion/` extract sync.** This harness could not read Windows MSI (`04858ede-…`). Box already had `/workspace/r1/expansion/` + `/workspace/r1/txt/` + `/workspace/r2/extracts/`. No additional MSI expansion caches were copied. Parent should `CopyToBox` any newer MSI `r1/.../expansion` extracts if they exist beyond the box tree.
10. **Not a substitute for Step 1b.** Do not pool Step 5 `seq_yes` counts into deposit-event n≥100 claims.

## Sources used (priority)

1. EuropePMC fullTextXML when PMCID available  
2. OA PDFs via EuropePMC render / Unpaywall / J-STAGE  
3. Local R1/R2 extracts (`/workspace/r1/txt`, `/workspace/r1/pdfs`, `/workspace/r2/extracts`)  
4. EuropePMC title+abstract + CSV notes/quotes  

Cache: `/workspace/streams/p3_step5_cache/` (meta, fulltext, corpus, pdfs, unpaywall).

## Files

| Path | Role |
|------|------|
| `streams/P3_step5_r1_dual_fbs_isolate_to_sequence.csv` | Per-ID codes |
| `streams/P3_step5_r1_dual_fbs_summary.md` | This summary |
| `streams/P3_step5_r1_dual_fbs_sync_manifest.txt` | Sync manifest |
| `streams/isolation-refs-dual-fbs_only.csv` | Input corpus |
| `streams/p3_step5_cache/` | Working extracts (optional to sync) |

## 2026-09-23 local-PDF recode (VI32, VI34, VI36, VI41, VI43, VI45)

Previously `seq_unclear` / `needs_pdf_or_oa`. Soft bar applied after `pdftotext` (VI43: encrypted → `pdftoppm` + tesseract OCR).

| ID | New code | Basis |
|----|----------|-------|
| VI32 | `seq_yes` | TK + gB sequencing of culture Isolates FHV191071/72 |
| VI34 | `seq_yes` | NGS whole-genome of Isolate CAV2232 |
| VI36 | `seq_no` | RT-qPCR genome detection only; no isolate sequencing |
| VI41 | `seq_yes` | Complete SP-variant genome; GenBank EF530047 / EF657887 |
| VI43 | `seq_no` | Persistence/signaling paper; no isolate genome sequencing (ignore adjacent articles in same PDF file) |
| VI45 | `seq_no` | HEK-293 isolation utility; genetic characterization mentioned as motivation only |

Still Step 5 practice-chaining, not Step 1 type-origin ontology.
