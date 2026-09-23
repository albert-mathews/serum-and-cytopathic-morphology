# Agent 3 review

**Role:** Independent adversarial reviewer of Isolation-stage negative-control (NC) tier scoring.  
**Framework:** `control-cultures.md` v0.1 (decision tree §5; M1–M6; allowed inference §4; prefer worse tier when ambiguous).  
**Sources checked:** `control-cultures-overview.csv`, `control-cultures-justification-notes.md`, extracts under `wrk/isolation_practice/_txt/`, full text where needed, and for **VI43** the image PDF via `read_file` (Materials and methods / Fig. 1 pages).  
**Assigned papers:** VI40, VI41, VI42, VI43, VI45, VI46, VI47, SPT10.  
**Reviewer rule:** Do not invent quotes; score from paper text alone; no “standard practice” guesswork.

---

## Per-paper findings

### VI40 — assigned **A** → agent recommends **B** (DOWNGRADE)

**Primary experiment (as scored):** Multi-strain RSV infection of HEp-2 and A549 vs mock (lab infection, not clinical Isolation).  
**Endpoint:** IF morphology (actin / RSV), RNA-seq vs mock, cytokines/LDH/caspase.  
**Special scrutiny:** Yes (assigned A).

#### What the paper actually says

**Infection medium (methods — infected cells only):**
> "Nearly confluent HEp-2 and A549 cells were infected with RSV/… at an MOI of 0.01 for 1.5 h then the inoculum was removed, washed with PBS, and 2% FBS/MEM was added and incubated for a period of 24, 48, 72, or 96 hpi."

**Growth medium (methods — stock culture only):**
> "HEp-2 and A549 cells were cultured in minimum essential medium (MEM…) supplemented with 10% fetal bovine serum…"

**Mock language (results / figure legends only — not methods):**
> "Mock-infected HEp-2 and A549 cells also differed in the morphology of their actin cytoskeleton…"

> "Cells were either mock-treated or infected with RSV/… at a multiplicity of infection of 0.01 for 24, 48, 72, or 96 h."

> "we subjected RSV-infected and mock-infected A549 and HEp2 cells to high-throughput, short-read RNA sequencing"

> "The cultured supernatants were harvested from mock-infected and RSV-infected cells at 24, 48, 72, or 96 h postinoculation (hpi)."

**IF methods** restate only infection (“infected with RSV strains as described above”); RNA-seq methods restate only “RSV infections… as described above.” Neither paragraph defines mock preparation, mock medium, or “identical except no virus.”

#### Decision-tree application

| Step | Finding |
|------|---------|
| 1 `nc_any` | **yes** — mock-treated / mock-infected used as parallel comparator for morphology, transcriptomics, cytokines |
| 2 Isolation-stage | **yes** for the primary infection arm (actin morphology / CPE notes at 96 hpi; mock panels in Figs. 3–4) |
| 3 M1–M6 | **not all yes** |

| Match | Verdict | Basis |
|-------|---------|--------|
| M1 cells | yes | Same HEp-2 / A549 lines named for mock and infected |
| M2 base medium | **unknown** | Methods never state mock medium family post “treatment” |
| M3 serum/enrichment | **unknown** | 2% FBS/MEM stated only after RSV inoculum removal; mock serum never stated. Forbidden to assume mock also left 10% growth medium or switched to 2% (§4.2 #3) |
| M4 additives | **unknown** | Silent for mock |
| M5 timeline | yes (allowed inference) | Parallel 24/48/72/96 hpi harvest of mock and infected supernatants / imaging |
| M6 inoculum-only diff | yes | Mock = no RSV |

**Allowed-inference check (§4.1):**  
- No “mock performed identically except medium alone” (§4.1 #4).  
- No universal post-inoculation medium sentence that explicitly covers NC wells (§4.1 #1) — the 2% FBS sentence is inside “cells were infected with RSV…”.  
- Figure + methods do **not** jointly define mock medium (§4.1 #5).  
- §4.2 #1 explicitly blocks tier A: word “mock” with no medium/serum/identical-conditions language.

#### Why assigned A is wrong

Primary notes claim: *“Mock-treated/mock-infected under the same infection protocol including post-inoculum 2% FBS/MEM → A”* and CSV `match_basis=explicit`, all M* = `yes`.

That is **guesswork**. The methods never apply 2% FBS/MEM to mock. This is the same pattern primary correctly scored **B** for VI8, VI13, and VI14 (mock named; serum/medium for mock not verifiable). VI40 was scored inconsistently upward.

#### Agent tier: **B**

- `m2=unknown`, `m3=unknown`, `m4=unknown`  
- `match_basis` should be `NA` (or not `explicit`)  
- `ambiguous=yes` is optional but reasonable (a generous reader might stretch §4.1 #1; framework forbids stretch for A)  
- Prefer worse when ambiguous → **B** not A

**Quotes in justification notes for VI40 medium/mock are real** (verified in full text). The error is **classification**, not fabricated quotes.

---

### VI41 — assigned **D** → agent confirms **D**

**Primary experiment:** Characterization of WNV small-plaque (SP) variant vs parental WT (plaque morphology, multi-cell-line growth kinetics, mosquito in vivo).  
**Endpoint:** Plaque size / growth titer.

**NC search (full text grep for mock / uninfected / negative control / control):** no culture-level NC language. Growth and plaque comparisons are WT vs SP only. “Control” does not appear as culture NC.

**Decision:** `nc_any=no` → **D**.  
Justification notes are thin but correct. No remedy required beyond optional expansion of the notes block (no quote needed when absence is the finding).

---

### VI42 — assigned **B** → agent confirms **B** (with C-stage as secondary adversarial option)

**Primary experiment:** AdORF29 / VZV infection experiments on MeWo, U373MG, enteric ganglia; ORF29p localization and stability.  
**Endpoint:** IF localization / WB / pulse-chase (not classical clinical Isolation CPE).  
**Special scrutiny:** Yes (assigned B).

#### Verified quotes

**Mock-infected (WB / pulse-chase):**
> "MeWo and U373MG cells were infected with AdORF29 at an MOI of 50 (lanes 2 to 7) or mock infected (lane 1)."

> "MeWo (A) and U373MG (B) cells were infected with AdORF29 at an MOI of 50 (lanes 1 to 6) or mock infected (lane 7)."

**Mock-treated (drug vehicle — not culture NC):**
> "infected cultures were either mock treated, treated with MG132, or treated with cycloheximide"

**Infection-phase medium (methods):**
> "During virus infection, MeWo and U373MG cells were maintained in Eagle’s minimal essential medium supplemented with 2% fetal bovine serum, 100 U/ml penicillin, and 100 µg/ml streptomycin."

**Growth medium:** DMEM + 10% FBS (MeWo); 5% Fetal-clone II (U373MG/293A).

**“Uninfected cells” in VZV passage:**
> "serial passage of infected cells onto uninfected cells"  
→ stock passage recipients, **not** parallel NC (§2.3 / VI4-style co-culture rule).

#### Decision-tree application

| Step | Finding |
|------|---------|
| 1 `nc_any` | **yes** — mock-infected lanes for AdORF29 experiments |
| 2 Isolation-stage for primary? | **yes under §6 priority 4** (no CPE Isolation claim; score culture infection arm that defines infected vs not) |
| 3 Match | Under-specified for mock |

M1 yes (same cell lines). M2/M3/M4 **unknown** for mock: the phrase *“During virus infection…”* grammatically covers infected cultures; it does not explicitly place mock wells under 2% FBS EMEM. No “mock identically except no virus.” M5 yes (3 dpi parallel harvest). M6 yes.

→ **B** (Isolation-stage NC named; M2/M3 not verifiable).

#### Adversarial C-stage option (not adopted as primary fix)

§2.5 lists “Western blot / immunoblot loading comparisons” and “IF of a separately described expression experiment” as **non-Isolation-stage**. AdORF29 is an expression vector; mock lanes primarily serve protein-expression WB/IP. A strict stage reading → **C** (`C-stage`).

Under §6 priority 4, primary’s **B** is the framework-consistent choice for “infected vs not” culture arm. Primary already set `ambiguous=yes`. Conservatism between B and C would push **C**; between B and A, **B**.  

**Agent verdict:** Keep **B**; do **not** upgrade to A; optionally re-flag ambiguity as B vs C-stage (not B vs A). Primary’s note that this is not classical clinical Isolation is correct and should stay.

**Quote accuracy:** Verified. No invented quotes.

---

### VI43 — assigned **A** → agent confirms **A**

**Primary experiment:** Persistent SARS-CoV infection of Vero E6; mock-infected / density-matched control flasks for pathway WB and viability.  
**Endpoint:** Phosphorylation WB, cell number / viability, morphology of surviving cells.  
**Special scrutiny:** Yes (assigned A; image-only PDF).  
**Verification method:** `read_file` on `wrk/isolation_practice/VI43 - Mechanisms of establishement of persistent SARS-CoV-infected cells.pdf` (pages with Materials and methods / Fig. 1). OCR extract `VI43_pymupdf.txt` is empty/useless; page render is authoritative.

#### Quotes verified on rendered PDF (page 262 / journal p. 262–263)

**Serum switch before infection:**
> "The medium was changed to 2% FBS DMEM before virus infection."

**Controls prepared in 2% FBS DMEM:**
> "On the other hand, Vero E6 cells were prepared in T-25 flasks at several concentrations with 2% FBS containing DMEM as controls because surviving cell number is different (less than 5% of total cells) in each experiment."

**Parallel wash of survivors and controls:**
> "At 50 h.p.i., surviving cells and controls were washed with 2% FBS containing DMEM 5 times (with pipetting 25 times)."

**Mock-infected protein sample:**
> "We obtained a protein sample from mock-infected cells, with a similar cell number to persistently infected cells."

**Fig. 1 legend (methods-force):**
> "Mock-infected subconfluent cells, similar in number to surviving cells that had escaped from apoptosis by SARS-CoV infection, were also washed in the same manner."

Also confirmed: growth stock is DMEM + 5% FBS; infection/control regime is 2% FBS DMEM; Fig. 2 includes a “Mock infection” DMSO arm for inhibitor experiments.

#### M1–M6

| Match | Verdict |
|-------|---------|
| M1 | yes — Vero E6 |
| M2 | yes — DMEM |
| M3 | yes — controls / mock explicitly in **2% FBS** DMEM, same as infection |
| M4 | yes (allowed inference) — same DMEM + 2% FBS regime; antibiotics stated for routine culture; no contradictory additive regime for controls |
| M5 | yes — 50 h.p.i. parallel wash / sampling; mock washed “in the same manner” |
| M6 | yes — mock-infected / controls without SARS-CoV |

Density adjustment of controls (to match surviving cell number) is intentional loading matching, not an M1 failure (M1 = cell type/system).

#### Agent tier: **A**

Primary quotes are **not invented**; they match the rendered Materials and methods / Fig. 1. `match_basis=explicit` is justified. No downgrade.

Minor note: `control_cpe_claimed_negative` is `NA` in CSV — acceptable (endpoint is viability/WB, not classical CPE-negative claim). Optional: set `control_cpe_reported` more carefully; does not change tier.

---

### VI45 — assigned **D** → agent confirms **D** (with FAT figure caveat)

**Primary experiment:** RTCIT Isolation of street/fixed rabies on HEK-293 vs Neuro-2a vs BHK-21; FAT endpoint.  
**Endpoint:** FAT foci.

#### Verified material

**“Virus control” = positive control strain (not NC):**
> "2.2. Virus control  
> The challenge virus standard CVS-11 strain of rabies virus was used."

**Isolation maintenance medium (test cultures):**
> "replenished with maintenance medium (IMDM with 2% FBS)"

**Figure 1 (FAT assay comparator — not Isolation protocol NC):**
> "Note bright apple-green fluorescent foci in 80–90% cells (B) in comparison to un-infected cells with no fluorescent foci (A)."

**FAT-negative brains** are clinical specimens (test inocula expected negative), not culture NCs (§4.2 #5 analog).

#### Decision

- Section “Virus control” is **PC** only → does not raise NC tier (§2.4; §5.1).  
- Fig. 1 “un-infected cells” function as **FAT background / assay imaging control** (analogous to secondary-only IF / dye-specificity uninfected in SPT10). Framework §2.3 excludes pure assay controls from culture NC.  
- Isolation methods (2.5) never describe parallel uninoculated wells on RTCIT plates.

→ `nc_any=no` for Isolation/infection culture NC → **D**.  
`positive_control_present=yes` correct.

If a later scorer treats Fig. 1 uninfected as culture NC for the CVS sensitivity arm only, stage would still be **wrong for primary Isolation** → C-stage at best; conservatism between D and C when assay-control status is ambiguous favors **D** (consistent with SPT10). **No change.**

---

### VI46 — assigned **D** → agent confirms **D**

**Primary experiment:** RTCIT routine Isolation of street rabies on BHK-21; parallel MIT.  
**Endpoint:** FAT foci / endpoint dilution.

**Media (verified):**
> "Eagle basal medium with 3% fetal bovine serum was used as the cell maintenance medium, and a combination of 10% fetal bovine serum and 10% tryptose phosphate broth was used as the cell growth medium."

**“Control virus standard (CVS-27)”** = laboratory positive stock, not culture NC.

Grep for mock / uninfected / negative control culture: **none**. Parallel titrations are MIT vs RTCIT, not inoculated vs uninoculated culture wells.

→ **D**. Justification adequate.

---

### VI47 — assigned **D** → agent confirms **D**

**Primary experiment:** Propagation of PV rabies on BSR; NP extraction / CsCl purification / SDS-PAGE.  
**Relationship:** **Duplicate of VI29** (same article: Dastkhosh et al., *Jundishapur J Microbiol* 2014;7(8):e11734; identical title and methods text in both PDFs).

**Methods (verified, same in VI29 and VI47):**
> "The virus was propagated in BSR cells in the presence of Dulbecco modified Eagle’s medium (DMEM) … containing 10% fetal bovine serum (FBS)."

Post-adsorption maintenance remains DMEM + 10% FBS. No mock, uninfected, or negative culture control. SDS-PAGE is product characterization only.

→ **D**. Primary correctly scored both IDs D and noted the duplicate.

---

### SPT10 — assigned **D** → agent confirms **D**

**Primary experiment:** Construction/propagation of TC-tagged ZIKV on Vero; biarsenical labeling / live imaging.  
**Endpoint:** CPE used for harvest timing; IF / biarsenical signal for imaging claims.

**Propagation / reduced serum (verified):**
> "Vero cells were cultured in DMEM (10% FBS) for 2 to 3 days. When the cell confluence reached 90 to 95%, the viral inoculum was added. After incubation for 2 h… the cells were washed once in PBS buffer and then cultured in fresh DMEM (2% FBS) medium for another 5 to 6 days. When the cytopathic effect (CPE) was progressed through 70 to 80%, the culture supernatants…"

**“Uninfected” (assay dye specificity only):**
> "strong biarsenical fluorescent signals were detected in the infected cells, while no biarsenical fluorescent signal was detected in the uninfected cells. This result clearly showed that the biarsenical reagent FlAsH only labeled the viral components…"

Fig. 4: infected with/without NR-TC27 ZIKV then stained with FlAsH — uninfected arm tests **reagent specificity**, not Isolation-stage CPE morphology under matched 2% FBS maintenance.

→ Not culture NC under §2.3 (assay control) → `nc_any=no` → **D**. Correct; consistent with VI45 FAT-uninfected handling.

---

## Corpus completeness audit

### PDF ↔ CSV row mapping

**PDFs present in** `wrk/isolation_practice/*.pdf` **(28 files):**

| # | PDF ID | CSV row |
|---|--------|---------|
| 1 | VI2 | yes |
| 2 | VI4 | yes |
| 3 | VI8 | yes |
| 4 | VI13 | yes |
| 5 | VI14 | yes |
| 6 | VI15 | yes |
| 7 | VI16 | yes |
| 8 | VI18 | yes |
| 9 | VI23 | yes |
| 10 | VI24 | yes |
| 11 | VI25 | yes |
| 12 | VI28 | yes |
| 13 | VI29 | yes |
| 14 | VI30 | yes |
| 15 | VI32 | yes |
| 16 | VI33 | yes |
| 17 | VI34 | yes |
| 18 | VI36 | yes |
| 19 | VI38 | yes |
| 20 | VI39 | yes |
| 21 | VI40 | yes |
| 22 | VI41 | yes |
| 23 | VI42 | yes |
| 24 | VI43 | yes |
| 25 | VI45 | yes |
| 26 | VI46 | yes |
| 27 | VI47 | yes |
| 28 | SPT10 | yes |

**Result:** All 28 PDFs have exactly one CSV row. No orphan PDF; no orphan CSV ID within this folder set.

**Excluded (correctly not in scored CSV):**  
`wrk/excluded_pdfs/VI44 - Releasing Intracellular NS1 from Mosquito Cells for the Detection of Dengue Virus-Infected Mosquitoes.pdf` — not among the 28 corpus PDFs; no VI44 CSV row (appropriate if excluded).

**not-found.csv:** lists VI31 (web-only / missing PDF) — not among the 28 PDFs; no VI31 CSV score row. Fine for Isolation-practice PDF corpus.

### VI29 and VI47 relationship

| Item | Finding |
|------|---------|
| Content | Same paper (identical title, abstract, methods, authors) |
| Files | Two separate PDFs in `wrk/isolation_practice/` |
| Scoring | Both **D**, notes explicitly mark duplicate |
| Issue | Double-counts one article in n=28 tier totals |

**Recommendation:** Keep both rows if corpus is defined as “PDF files present,” but report **unique-article n** separately (27 unique articles if VI29≡VI47). Do not drop a row without documenting the policy.

### Summary counts vs CSV

**Justification notes claim:**

| Tier | n | IDs |
|------|---|-----|
| A | 6 | VI16, VI25, VI33, VI38, VI40, VI43 |
| B | 5 | VI8, VI13, VI14, VI36, VI42 |
| C | 0 | — |
| D | 17 | VI2, VI4, VI15, VI18, VI23, VI24, VI28, VI29, VI30, VI32, VI34, VI39, VI41, VI45, VI46, VI47, SPT10 |
| **Total** | **28** | |

**CSV row recount:** 28 rows. Tier letters match the ID lists above **as currently assigned**.

**After Agent 3 VI40 fix (recommended):**

| Tier | n | Change |
|------|---|--------|
| A | **5** | remove VI40 |
| B | **6** | add VI40 |
| C | 0 | — |
| D | 17 | — |
| Total | 28 | |

Primary notes summary would then be **stale** until updated.

### Filename / ID mismatches and quality notes

| Item | Note |
|------|------|
| VI42 filename | Lowercase slug (`the-cellular-localization-pattern-of-varicella-zoster-virus-orf29p-is-influenced-by-proteasome.pdf`) vs Title Case for others — ID still VI42; no score impact |
| VI43 filename | Typo `establishement` (missing “h”); PDF title uses “establishment”. ID VI43 consistent |
| VI16 filename | Truncated with `...` — ID OK |
| VI29 vs VI47 | Same title string on two files — intentional duplicate IDs |
| VI43 text extract | `VI43_pymupdf.txt` empty; scoring relied on page render — **correct approach**; do not trust empty OCR |
| ID gaps | No VI1, VI3, VI5–7, VI9–12, VI17, VI19–22, VI26–27, VI31, VI35, VI37, VI44 in scored 28 — expected if corpus is selected subset |

---

## Systematic issues

1. **Inconsistent A vs B on “mock named + infection medium stated for infected only.”**  
   VI8, VI13, VI14 correctly stayed **B**. VI40 was upgraded to **A** without “identical conditions” or NC-specific medium language. Same pattern must yield the same tier.

2. **`match_basis=explicit` overused for VI40.**  
   Explicit requires protocol-force statement of control medium/serum or clear identical-conditions language. Parallel figure panels alone are not explicit match.

3. **M\* columns set to `yes` without textual support (VI40).**  
   Framework: A requires all M1–M6 = yes. Unknown serum under reduced-serum infection regime is the central project confound — cannot be filled by assumption.

4. **Zero tier C in the whole corpus** may indicate under-use of `C-stage` when mock exists only for WB/IF expression modules. VI42 is the assigned-set exemplar; primary already flagged it. Not a hard error for VI42 under §6 priority 4, but corpus-wide C=0 deserves a second pass on D and B papers.

5. **Duplicate PDF (VI29/VI47)** inflates D count by 1 if unique-article prevalence is the reporting target.

6. **Image-only PDFs:** VI43 handled correctly via render. Empty OCR must not be treated as “no methods.”

7. **PC language traps** handled well in assigned set (VI45 “Virus control,” VI46 CVS-27).

8. **Assay uninfected vs culture NC** handled consistently for SPT10 (and acceptably for VI45 Fig. 1).

---

## Required remedies (numbered, actionable)

1. **Downgrade VI40 from A to B** in `control-cultures-overview.csv`:  
   - `tier=B`  
   - `m2_base_medium=unknown`, `m3_serum_enrichment=unknown`, `m4_additives=unknown` (keep m1/m5/m6 = yes)  
   - `match_basis=NA` (or remove `explicit`)  
   - `ambiguous=yes`  
   - Update `notes` to state mock named in results/figures; post-inoculum 2% FBS/MEM stated only for RSV-infected protocol; no identical-conditions language for mock.

2. **Rewrite VI40 section** in `control-cultures-justification-notes.md` to **B**, with the decision logic above; remove the claim that 2% FBS/MEM “applies” to mock.

3. **Update summary counts** in justification notes: A **5**, B **6**, C 0, D 17 (total 28). Remove VI40 from A list; add to B list.

4. **Leave VI43 as A**; optionally annotate that quotes were page-render verified (Materials and methods / Fig. 1) because OCR extract is empty.

5. **Leave VI41, VI45, VI46, VI47, SPT10 as D**; optionally expand VI41 notes with a one-line “grep: no mock/uninfected culture NC.”

6. **Leave VI42 as B**; add note that adversarial alternative is `C-stage` if AdORF29 mock is treated only as WB expression control; do not promote to A.

7. **Document VI29≡VI47** in any reader-facing tally: either (a) report n=28 PDF rows and n=27 unique articles, or (b) mark one row `exclude_from_corpus=yes` with reason `duplicate_pdf_of_VI29` if unique-article stats are preferred.

8. **Apply the VI40 consistency rule retroactively** to any other A papers outside this assignment that rest only on “mock in figure + infection medium for infected cells” (spot-check VI38 etc. outside Agent 3 scope unless reopened).

9. **Do not invent or paste OCR for VI43** into notes without page verification; keep render-based quotes.

10. **Corpus checklist:** re-confirm after CSV edit that row count remains 28 and summary table matches CSV.

---

## Verdict summary table

| id | assigned | agent_tier | status |
|----|----------|------------|--------|
| VI40 | A | **B** | **DISAGREE — downgrade** (mock under-specified; M2/M3 unknown; inconsistent with VI8/13/14) |
| VI41 | D | D | AGREE |
| VI42 | B | B | AGREE (flag optional C-stage alternative; not A) |
| VI43 | A | A | AGREE (quotes verified on rendered PDF) |
| VI45 | D | D | AGREE (PC ≠ NC; Fig. 1 uninfected = FAT assay control) |
| VI46 | D | D | AGREE |
| VI47 | D | D | AGREE (duplicate of VI29) |
| SPT10 | D | D | AGREE (uninfected = dye specificity only) |

**Net change from this assignment:** 1 material correction (VI40 A→B).  
**Corpus after fix:** A=5, B=6, C=0, D=17 (n=28 PDF rows; 27 unique articles if VI29/VI47 collapsed).

---

*End of Agent 3 review.*
