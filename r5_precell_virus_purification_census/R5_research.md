# R5 research protocol — pre-cell-culture bulk purification census

**Status:** v0.1 scaffold (2026-11-17). Mirrors `p1_history/P1_research.md` where the machinery applies,
adapted to a *census* of purification/crystallization rather than serum practice.
**Stance:** There is no preferred outcome. The goal is an **exhaustive, dated, per-item count** of which
viruses were bulk-isolated and physically characterized before cell culture, and by what methods — so the
Introduction/Discussion claim is backed by enumeration, not impression.

## 1. What R5 is (and is not)

**Is:** a census of pre-cell-culture (pre-1949) **bulk isolation / purification / crystallization** of viruses
in the broad historical sense (plant viruses, bacteriophages, animal viruses), plus the **physical
characterization** applied to them (X-ray, electron microscopy, analytical ultracentrifugation / molecular
mass, chemical analysis, serology).

**Is not:** a history of serum/nutrient medium practice (that is P1); a history of filtration/"virus" ontology;
an EV-purification review (P2); a post-1949 methods catalog (out of window, except boundary markers).

## 2. Window and definitions

| Term | Definition used here |
|------|----------------------|
| **Window end** | Pre-cell-culture = before the Enders–Weller–Robbins 1949 monolayer method became the routine route for animal-virus isolation. Items 1949+ are **out of window** and excluded, except recorded as **boundary markers** where they prove the post-cell-culture dependency. |
| **Bulk isolation** | Obtaining the agent in quantity and relative purity sufficient for physical characterization — typically ~mg to g scale, or a crystalline / single-component preparation. |
| **Physical characterization** | X-ray diffraction, electron microscopy, analytical ultracentrifugation (sedimentation / molecular mass), chemical analysis (protein/nucleic-acid/lipid), serology. |
| **Crystallized** | True 3-D crystal, liquid-crystalline, or paracrystalline needles — recorded as distinct physical forms; "crystallized" is not conflated with "purified nucleoprotein." |

## 3. Inclusion / exclusion

**Include** a source if it is a primary report of bulk purification / crystallization / physical
characterization of a virus (or an agent then-designated as a virus) dated pre-1949, **or** a post-1949
boundary marker of the animal-virus dependency (e.g., poliovirus crystallization 1955).

**Exclude:** post-1949 routine purification; modern reviews without primary methods (log as screened-not-useful
unless they supply lead citations); serum/nutrient practice (P1); EV purification (P2).

## 4. Epistemic rules (bias control)

1. Log every candidate in `R5_screened.csv` (Y/N/B + reason), never silently drop.
2. Extract the same purification fields from every useful item (Section 5) whether plant, phage, or animal.
3. **Secondary citations of a primary method are corroboration, not the primary.** Wishlist the primary; tag
   `[DATA REQUIRED]` until its full text is read.
4. Do not upgrade silence ("not crystallized" is only assertable after an explicit negative or exhaustive
   enumeration of the pre-1949 animal-virus record).
5. Devil's-advocate pass: actively hunt for any pre-1949 animal virus that WAS crystallized or bulk-characterized
   by a non-cell-culture route (the expected answer is "none / influenza+vaccinia via eggs"; look to break it).
6. Separation of roles: enumerate first; interpret ("what this means for the paper") only after the table freezes.

## 5. Extraction schema (`R5_useful.csv`)

`id · year · author_short · agent · agent_type · source_material · bulk_production · purification_method ·
physical_form · characterization · yield · stability · cell_culture_required · window_status · citation ·
identifier · evidence_tag · confidence · extract_date · notes`

| Field | Meaning |
|-------|---------|
| `agent_type` | plant / phage / animal |
| `source_material` | leaf sap, bacterial lysate, allantoic fluid, animal skin/tissue, serum, etc. |
| `bulk_production` | how the agent was grown to bulk (field/glasshouse plants; bacterial culture; embryonated eggs; live animal) |
| `purification_method` | ammonium-sulfate precipitation, differential / analytical ultracentrifugation, adsorption–elution, chemical crystallization, chromatography, etc. |
| `physical_form` | crystal_3d / liquid_crystal / paracrystal_needles / amorphous / nucleoprotein_noncrystalline / unknown |
| `characterization` | xray / em / sedimentation_mass / chemical / serology (comma list) |
| `yield` | free text (e.g., "grams per plant", "~1 mg/L lysate", "1–10 mg/cc") |
| `stability` | stable / labile / envelope_labile / unknown |
| `cell_culture_required` | Y / N / n_a (was cell culture required to produce the material?) |
| `window_status` | in_window_pre1949 / boundary_post1949 |
| `evidence_tag` | [VERIFIED src] / [DATA REQUIRED] / etc., per CONVENTIONS §3 |

## 6. Rounds

- **Round 1 (done 2026-11-17):** seed from the already-verified cases surfaced during Introduction drafting
  (Stanley 1935; Bawden & Pirie 1937–42; Eriksson-Quensel & Svedberg 1936; Kausche et al. 1939; Schlesinger
  1933–36; Northrop 1938; Stanley 1944–45 influenza; Lauffer & Stanley 1944; Goodpasture 1931; Schaffer &
  Schwerdt 1955). See `R5_search_log.md`.
- **Round 2:** systematic queries — plant-virus crystallography history; bacteriophage purification history
  (Schlesinger/Northrop/Anderson/Bawden); animal-virus purification history (influenza, vaccinia, papillomavirus,
  foot-and-mouth); "first X crystallized" claims. Databases: PubMed/PMC, Google Scholar, Internet Archive/HathiTrust,
  Nobel/ASM/Rockefeller archives, and historical reviews (e.g., Creager's *The Life of a Virus* bibliography).
- **Round 3:** snowball from the bibliographies of each useful primary and of the historical reviews.
- **Round 4:** adversarial — enumerate candidate pre-1949 animal viruses and confirm each one's purification status
  individually (the "0 crystallized" claim needs a positive enumeration, not an absence assertion).
- **Round 5+:** saturation; reconcile the "more than a dozen by 1938" secondary claim; freeze counts; synthesize.

## 7. Stop / "we know" criteria

Declare the census **provisionally complete** only when:

1. Rounds 1–4 logged.
2. Every pre-1949 **plant**, **phage**, and **animal** virus that could plausibly have been bulk-purified is
   either enumerated with a primary citation, or logged as searched-and-not-found with the search documented.
3. The "0 animal viruses crystallized pre-1949" claim is backed by an explicit per-candidate table, not absence.
4. Each count carries a confidence and an explicit "still open" list (paywalled primaries → wishlist).

## 8. Revision log

| Version | Date | Change |
|---------|------|--------|
| v0.1 | 2026-11-17 | Scaffold: window, inclusion, schema, rounds, stop criteria. |
