# Adversarial search: X≤Y FBS at/after inoculation (hold or increase)

**Date:** 2026-09-18 (America/Toronto / ET)  
**Goal:** Find PRIMARY ISOLATION / diagnostic virus-isolation methods where serum % is held constant or **increased** at/after inoculation: **X ≤ Y** (X = pre/growth, Y = post/maintenance-infection).  
**Honesty rule:** Null / sparse result is valid. Do not invent %. No paywalled PDFs into tracked paths. No git commit.

**Output dir (MSI):**  
`C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion\`

Companion files: `adversarial_X_leq_Y_candidates.csv`, `VIRPRO1013_exclusion_note.md`

---

## Executive verdict (honest)

This pass is **sparse but not null**.

| Bucket | Count (CSV HOLD rows) | Quality |
|---|---|---|
| Solid **X = Y** (equal hold) | **4** | Strong quotes / open protocols |
| Solid **X < Y** (increase) | **1** (conditional) | CDC WA1 isolation: cells may be grown at 5% then inoculated in 10% — coded increase when pre=5; hold when pre=10 |
| Borderline / soft / propagation | **4** | Same-% but not clinical primary, or post % inferred |
| Institutional X≤Y as isolation practice | **0 new** beyond noting VIRPRO is **excluded** (increase-ish but master-seed, not isolation) |

Classic **X > Y** (esp. 10→2) remains the dominant literature pattern (R1 dual CSV ~60× 10→2). Adversarial X≤Y hits exist but are uncommon, clustered in: (1) flavivirus reference-lab SOPs that never leave 5%, (2) serum-free influenza/hMPV systems (0→0), (3) some veterinary FMDV clinical isolation that returns to 10% after adsorption, (4) occasional co-seeding / limiting-dilution designs that add cells in 10% FBS onto specimens.

**Null-ish?** For **true increase (X < Y) in clinical primary isolation**, nearly null outside the CDC WA1 limiting-dilution design and the **excluded** USDA VIRPRO master-seed SOP. Equal-hold cases are few but real.

---

## Queries run (aggressive hold/increase aim)

1. `"virus isolation" "same medium" OR "growth medium" after inoculation FBS`
2. `"virus isolation" "10% FBS" maintained OR "with 10%" post inoculation` (no reduction)
3. `"primary isolation" virus "5% FBS" "5% FBS"` both stages
4. `"virus isolation" "increased" serum OR "higher serum" maintenance`
5. `protocols.io virus isolation FBS`
6. `"do not change" OR "without changing" medium serum isolation virus`
7. `protocols.io West Nile "5% FBS"` (ADV006 verify)
8. `FMDV "virus isolation" "10% FBS" after inoculation` / Fukai ZZ-R LFBK
9. `"serum-free" "virus isolation" influenza OR hMPV`
10. `"maintenance medium" "10% FBS" "virus isolation" clinical`
11. `"do not remove the virus inoculum" FBS` (WNV-style hold)
12. HEV / ASFV / EV71 restoration to 10% after adsorption (near-miss screen)
13. Cross-check R1 dual CSV for existing `10,10` / `0,0` / `5-10,10` rows (VI13, VI24, VI29)

WebFetch used for: protocols.io WNV PDF, protocols.io SARS Opti-MEM page, CDC EID 26/6/20-0516 (WA1), PMC4255371 (rabies NP), PMC2903611 (ADV017), IntechOpen 40221, ATCC guide (prior), PubMed Fukai abstract + Sage snippet quotes.

---

## Existing HOLD candidates — verification

| Prior ID | Claim | Verdict this pass |
|---|---|---|
| **ADV006** WNV protocols.io 5→5 | Equal hold | **CONFIRMED solid.** Full PDF: growth DMEM + 5% FBS; step 4: “do not remove the virus inoculum. Add cell culture medium (DMEM) with 5% FBS”. Clinical PCR+ serum/plasma/urine. → **HOLD001** |
| **ADV019** SARS Opti-MEM 3→3 | Dual-stage same % | **Soft / provisional.** Abstract/methods: monolayers “grown in Opti-Mem … supplemented with 3% foetal bovine serum” and clinical samples “inoculated onto” those monolayers. Does **not** separately state a distinct post-inoculation % (no explicit “add Opti-MEM + 3%” step like WNV). Same-medium context is reasonable but not dual-numbered. → **HOLD002** (flag) |
| **ADV010** SF 0→0 influenza/hMPV | Equal hold | **Supported** by Lednicky & Wyatt IntechOpen ch.40221 narrative (SF MDCK for influenza isolation; SF Vero E6 for hMPV/PIV4). Teaching/methods chapter, not a single clinical case report. → **HOLD003** |
| **ADV002** FMDV suspension 5→5 | Equal | **Propagation-borderline** (Dill et al. PMC5857075 suspension infection), not clinical isolation SOP. → **HOLD004** |
| **ADV017** Diplorickettsia 4%/5% | Possible B-class | **Not counted as virus HOLD.** Organism is intracellular **bacterium**; L929 MEM+4% / HEL-MRC5 MEM+5% are cultivation media in shell vials, not dual-stage virus isolation. Near-miss only. |

---

## New / strengthened X≤Y hits

### Solid equal (X = Y)

1. **HOLD001 / ADV006 — WNV Vero, 5→5** (protocols.io 2023, Nagy). Primary isolation SOP. Quotes verified from PDF.
2. **HOLD005 — FMDV ZZ-R 127 / LFBK-αvβ6, 10→10** (Fukai et al. 2015, *J Vet Diagn Invest*). Clinical samples from experimentally infected animals; OIE-manual-style isolation. Search/snippet quotes: cells seeded in commercial medium + **10% FBS**; after adsorption wash, “commercial medium … supplemented with **10% of FBS** was added.” True isolation context. Access: abstract OA; full text often paywalled — percentages from published snippet only (not invented).
3. **HOLD003 / ADV010 — serum-free 0→0** influenza (MDCK SF) / hMPV (Vero E6 SF). Lednicky methods chapter.
4. **HOLD007 / VI24 (R1) — influenza A/B Vero OptiPRO SFM, 0→0**. Already in R1 dual CSV; included here as adversarial X≤Y corpus support.

### Solid / conditional increase (X < Y)

5. **HOLD006 / VI13 — SARS-CoV-2 USA-WA1 CDC, 5–10 → 10** (Harcourt et al. EID 2020). **Primary isolation from NP/OP.** Cells “cultured … in DMEM supplemented with … FBS (**5% or 10%**)”. Isolation: specimen dilutions in serum-free DMEM, then Vero suspension in DMEM containing **10% FBS** added directly to dilutions. When growth was 5%, this is **5→10 increase**; when 10%, **10→10 hold**. Strongest open-access increase-or-hold isolation design found.

### Borderline

6. **HOLD002 / ADV019 — Opti-MEM 3→3 soft** (Mackay protocols.io SARS culture).
7. **HOLD004 / ADV002 — FMDV BHK suspension 5→5** propagation.
8. **HOLD008 — HEV genotype 3 wild boar, 10→10** (BMC Vet Res 2020). After adsorption, “maintenance medium … containing **10% FBS**” (growth also 10%). Field isolate / animal tissue context; more propagation-after-isolation than classic diagnostic tube culture — borderline primary.
9. **HOLD009 / VI29 — rabies PV on BSR, 10→10**. Explicit DMEM + 10% FBS after adsorption, but purpose is **vaccine-strain NP purification**, not clinical isolation. Propagation_borderline.

### Excluded (mentioned only)

- **ADV011 USDA VIRPRO1013**: growth ~5–10% → maintenance **5–20%** (can be increase). **User rule: NOT isolation** (master-seed extraneous-agent). Tagged `EXCLUDED_not_isolation`. See `VIRPRO1013_exclusion_note.md`.

---

## Near-misses (mostly classic X>Y or ambiguous)

| Lead | Why not HOLD |
|---|---|
| Most SARS-CoV-2 clinical isolation (Taiwan CDC, Omicron papers, etc.) | Explicit 10→2 / 10→2.5 / 10→3 |
| CIRAD/NEADL PPRV SOP | Explicit growth 10% → maintenance **2%** |
| ANSES FMDV SOP (ADV007) | Post **without FBS** (0%) — X>Y / Class C, not X≤Y |
| ATCC Virology Guide (ADV009) | Recommends **decrease** to ~2% for inoculation (except influenza →0) |
| CLSI M41 / ASM CPE protocols | Institutional classic ~10→2 |
| Japan NIID VeroE6/TMPRSS2 SARS | Inoculum mixed in 5% FBS; “fresh culture medium” at 1 dpi — % of “fresh” not explicit enough to claim 5→10 without inventing |
| Zika MDM / Vero isolation papers | Inoculum often 2%; “fresh medium” returns toward growth % — dual numbers incomplete |
| EV71 RD kinetics; dengue endothelial; some MDCK flu production | Restore to 10% after adsorption, but **stock propagation**, not clinical isolation |
| Exhibition-swine IAV SFM MDCK | Strong 0→0 isolation candidate; growth adaptation to SFM then VGM=SFM+trypsin — noted as support for HOLD003/007 class, not separately numbered without re-reading full methods for a second ID |

---

## X>Y extras for corpus (NOT adversarial target; brief list)

Classic reductions seen repeatedly this pass (do not merge into HOLD CSV): 10→2 (majority SARS/FMDV Pirbright-style), 10→2.5, 10→3, 10→1 (YFV EID), 10→0 + trypsin (influenza), ANSES FMDV →0. These reinforce that X>Y is default; X≤Y is the exception.

---

## Institution / guideline-type refs (separate from paper isolation practice)

### From prior ADV set (user-requested brief list)

| ID | Doc | Role for X≤Y question |
|---|---|---|
| **ADV007** | ANSES FMDV Virus Isolation SOP | **True isolation**; post medium **without FBS** (not X≤Y; Class C) |
| **ADV009** | ATCC Virology Culture Guide | Institutional; recommends **decreasing** serum (~2%); influenza viral medium **no FBS** |
| **ADV011** | USDA VIRPRO1013 | **EXCLUDED** — master-seed purity / extraneous agent, not isolation; maintenance can be **5–20%** (increase-capable) |
| **ADV020** | IntechOpen Lednicky methods chapter | Teaching guide; recommends **1–3%** refeed and calf-serum option; also hosts ADV010 SF narrative |

### Other institution docs seen (mostly classic X>Y; not new X≤Y)

- **CLSI M41**: ~10% growth → ~2% (or 1–3%) maintenance  
- **ASM CPE protocol**: maintenance medium with **2% serum**  
- **CIRAD / NEADL / EURL-PPR SOP**: growth 10% → maintenance **2%**  
- **WOAH / OIE** chapter examples (e.g. MERS): virus culture medium often **2% FCS**  
- **CDC measles Vero/hSLAM lab tools**: inoculation/incubation in DMEM + **2% FBS**  
- **WHO** measles/rubella lab manual: annex isolation pending/linked to CDC-style practice  

**No new institution SOP found this pass that mandates X≤Y for diagnostic isolation.** The only institutional document with post ≥ pre serum is **VIRPRO1013**, which the user ruled out.

---

## Coverage limits

- Paywalled full texts (Fukai JVDI full PDF) used only via abstract + indexed snippets; % not invented beyond those snippets.  
- protocols.io interactive pages sometimes return JS shells; WNV **PDF** endpoint worked for quotes.  
- “Increase serum for better isolation” as a deliberate experimental claim was **not** found; increases appear as co-seeding / limiting-dilution logistics (CDC WA1) or master-seed recipes (excluded).  
- Horse/lamb serum X≤Y primary isolation still not pinned with open dual numbers.

---

## Files

1. `adversarial_X_leq_Y_search_2026-09-18.md` (this file)  
2. `adversarial_X_leq_Y_candidates.csv` (HOLD001–HOLD009 + EXCL row for VIRPRO)  
3. `VIRPRO1013_exclusion_note.md`

No git commit. No paywalled PDFs stored.
