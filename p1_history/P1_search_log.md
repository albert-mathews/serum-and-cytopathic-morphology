# P1 search log

Protocol: `P1_research.md` v0.1  
Operator: grok-primary  
Start date: 2026-07-20

---

## Round 0 — Scaffold

**Date:** 2026-07-20  
**Status:** complete

- [x] Query list frozen before execution (N/A for scaffold)
- [x] Created `P1_screened.csv`, `P1_useful.csv`, this log
- [x] Created `p1_history/refs/`
- [x] Protocol `P1_research.md` used as frozen v0.1 for execution

**Round complete.**

---
## Round 1 — Seeds

**Date:** 2026-07-20  
**Operator:** grok-primary  
**Query list frozen:** seed set only (Enders lineage, Melnick, Dulbecco, repo manuals as end-marker candidates)

Seeds screened:
- Enders/Weller/Robbins 1949 Science → P1-001 Y
- Robbins et al 1950 CPE → P1-002 Y
- Nobel lecture 1954 → P1-003 Y (full text)
- Melnick protein-free media → P1-004 Y
- Dulbecco Vogt 1954 → P1-005 Y
- Melnick 1955 techniques → P1-006 B
- Morgan Morton Parker 199 → P1-034 B
- Weller Enders related 1950 → P1-024 B

**Round complete:** seeds + one-hop neighbors logged in P1_screened.csv.

---

## Round 2 — Systematic queries

**Date:** 2026-07-20  
**Operator:** grok-primary  

### Query list (frozen before execution)

Family A:
- Enders Weller Robbins poliomyelitis tissue culture medium serum 1949 1950
- cytopathogenic effect tissue culture serum concentration virus 1950s 1960s
- Melnick tissue culture methods poliovirus medium serum

Family B:
- "maintenance medium" virus isolation serum tissue culture
- Eagle medium virus propagation maintenance medium 2% serum
- "maintenance medium" OR "maintenance fluid" virus 1952..1956 serum

Family C:
- Leland Ginocchio role of cell culture virus detection
- Hematian traditional modern cell culture virus diagnosis 2016

Family D (counterexamples):
- virus isolation 10% serum throughout OR "maintenance medium" 10% serum
- Rift Valley serum-free maintenance medium
- vaccinia sheep kidney maintenance medium serum

Family E (end markers):
- CLSI M41 viral culture FBS
- ATCC Virology Culture Guide serum 2%
- UK SMI cell culture maintenance medium 2%

### Platforms
- Web search / Scholar-equivalent (multiple queries; hit lists not bulk-exported)
- PMC snippets (Fenner PMC7173454; Moffat; Schmidt pointers)
- ATCC web guide full fetch
- Nobel PDF full extract
- Project repo protocols (CLSI/ATCC/ASM notes)

### Outcomes
- New useful: Fenner P1-009; CLSI/ATCC/ASM/SMI end markers; Moffat P1-015; Subramanyam P1-017; Boyle P1-018; Rosenbaum P1-035
- Not useful: Hematian no medium recipe; modern SFM papers out of window; Wikipedia noise

**Round complete** (coverage adequate for provisional synthesis; not claimed exhaustive for all PubMed hits).

---

## Round 3 — Citation snowball

**Date:** 2026-07-20  

From useful seeds:
- Enders → Medium 199 (P1-034 B); foreskin paper (P1-024 B)
- Melnick → Howes 1960 secondary cite 2% calf serum (P1-031 B)
- Dulbecco → CSH 1953 plaque (P1-030 B)
- Schmidt lineage → Lennette manuals (P1-036 Y end-marker); Maverakis 1973 (P1-021 B)
- Fenner → eggs contrast (P1-027 N)

Depth 2 not exhaustively expanded (paywall/time); logged as partial snowball.

**Round complete (partial depth-2).**

---

## Round 4 — Adversarial

**Date:** 2026-07-20  

Emerging pattern tested: "maintenance always low serum after Enders."

Adversarial finds:
- P1-017: maintenance with **10% sheep serum** (1961 vaccinia)
- P1-018: **serum-free** maintenance used for inoculation (1964 RVF)
- P1-019/020: maintenance medium literature not always virus-Isolation-specific (B)

Emerging pattern tested: "continuous published 10→2 FBS titration exists."
- Not recovered in this pass despite Family B/D searches.

Emerging pattern tested: "only polio."
- Vaccinia, RVF, diagnostic general manuals included.

**Round complete.**

---

## Round 5 — QC / provisional stop

**Date:** 2026-07-20  

QC performed:
- [x] Quotes file cross-checked against Nobel PDF extract and ATCC/ASM/Fenner/CLSI project text
- [x] Hematian full text checked → correctly N (no medium %)
- [x] Counts: screened 40; useful 16
- [x] Counterexample family run
- [x] End markers identified
- [ ] Full second-operator replication (deferred; protocol allows reopening)
- [ ] Fulltext OCR of all 1950s primaries (deferred)

**Provisional completion declared** for synthesis v1 with limits stated in `P1_synthesis.md`.  
Reopen triggers: full Melnick/Dulbecco/Schmidt PDFs; non-English manuals; peer review cites.

---

## Round 6 — User PDF ingestion (2026-07-20)

**PDFs found in `p1_history/refs/`:**
- P1-001 Enders 1949 Science (full) → re-extracted high confidence
- P1-002 Robbins 1950 CPE (full) → re-extracted high confidence
- P1-005 Dulbecco Vogt 1954 (full) → re-extracted high confidence
- P1-015 Moffat diagnostic procedures (full) → re-extracted high confidence
- P1-017 Subramanyam vaccinia 1961 (full) → re-extracted high confidence; counterexample confirmed (maintenance 10% sheep serum; growth 20%)
- P1-200 Smith SE 1961 maintenance medium liver digest (user new ID) → added as useful Y
- P1-201 Hsiung GD 1961 primary cell cultures animal viruses (user new ID) → added as useful Y

**Not present (still wanted if available):** P1-004 Melnick protein-free; P1-006/008 Lennette-Schmidt; P1-018 Boyle; P1-035 Rosenbaum; etc.

**Totals after Round 6:** screened 42; useful 18 (Y in screened matches).


## Round 7 — User PDF batch + re-initiated search (2026-07-20)

### PDFs processed
| User file | Canonical ID | Result |
|-----------|--------------|--------|
| P1-04 Melnick protein-free | **P1-004** | Full extract HIGH confidence |
| P1-203 Boyle RVF AD0437967 | **P1-018** (alias P1-203) | Full extract HIGH; serum-free CPE phenomenon |
| P1-204 Rosenbaum AD0411928 | **P1-035** (alias P1-204) | Full extract HIGH; growth 10% FCS, MACRO maint 5% horse serum |
| P1-036 Diagnostic Procedures 4th ed | **P1-036** | Only AJPH book notice (2 pp) — NOT full Schmidt chapter |
| P1-020 Hematian | **P1-020** | Confirmed no medium recipe (N); old EAS P1-020 renumbered **P1-041** if present |

### Re-search (Family B/D + snowball from Melnick)
Queries run:
- Melnick Li Schaeffer poliomyelitis tissue culture medium
- "maintenance medium" 2% OR 5% serum virus tube 1958-1962
- Salk poliovirus roller tube medium 199
- Li Schaeffer simplified method 1953

New screened IDs: **P1-042** (Li & Schaeffer 1953 B), **P1-043** (Melnick Opton 2% calf snippet B), **P1-044** (Melnick methods chapter B)

### Key scientific update from Boyle (P1-018)
Serum removal can **create** CPE for RVF where serum-containing culture yields virus without CPE — strongest in-window evidence that medium enrichment is not a neutral background for CPE endpoints.


## Round 8 — Full Schmidt Chapter 3 (P1-008) ingested

User provided complete chapter screenshots (book pp ~79-178). Readable via image render.

**Headline extract:** 1969 diagnostic standard already specifies dual media with **typical growth 10-20% FBS** and **maintenance ~2% FBS** (or serum-free when possible), wash before inoculation, CPE + uninoculated controls for Isolation.

See P1_quotes.md Round 8 and P1_useful.csv P1-008 (confidence high).


## Round 9 — Process new PDFs + snowball leads (2026-07-21)

### Inventory of all PDFs in p1_history/refs (19 files)
P1-001, 002, 005, 006, 008, 015, 017, 020, 034, 036, 04(=004), 042, 043, 200, 201, 203(=018), 204(=035), 205, 206

### Newly fully extracted this round
- P1-006 Melnick 1955 Ann NY Acad Sci
- P1-034 Morgan et al 1950 Medium 199
- P1-042 Li & Schaeffer 1953 Science
- P1-043 Melnick & Opton WHO assay 2% calf serum
- P1-205 Schmidt 1972 AJCP diagnostic review
- P1-206 Melnick 1953 PSGBM 10% growth / serum-free maintenance

### New screened leads from bibliographies
P1-045 Weller et al 1952; P1-046 Youngner Ward Salk; P1-047 Scherer Syverton Gey HeLa 1953;
P1-048 Baron Low maintenance medium Science 1958; P1-049 Hayflick Moorhead 1961; P1-050 Robbins Weller Enders 1952

---

## Round 10 — Priority-A PDF ingestion (2026-07-22)

**User-supplied PDFs processed:** P1-013, P1-046, P1-047, P1-048, P1-051 (extracts in _notes/).

**Actions:**
- Screened rows updated to useful Y (046/047/048/051) or B (013).
- Useful CSV + quotes + synthesis **§7 medium-vs-inoculation history**.
- No new web search round; focus was full-text extraction of existing refs.

**Key result:** Dual-medium at inoculation step operational by ~1953–54 (Youngner, Scherer, Melnick); Baron 1958 names maintenance + quantifies serum inhibition of polio.
