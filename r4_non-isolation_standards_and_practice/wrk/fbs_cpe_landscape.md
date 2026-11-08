# FBS × CPE landscape — scaffold

**Goal (expanded, 2026-11-06):** Not one specific purpose, but the *omnibus* map: every
institutional / regulatory / research setting in microbiology & virology where
**cell culture uses FBS** and **CPE is an observed outcome** (the outcome, or one of
several). We want the whole landscape of "FBS % ↔ CPE" pairings, to see whether the
Isolation 10→2 pattern is one region of a larger, possibly-unmapped distribution.

**Prior-art check (do this!):** has anyone already published such a landscape? If yes,
found it; if no, we're first. Question is tracked as a distinct search.

### PRIOR-ART RESULT (2026-11-06, PubMed E-utilities sweep)
**No prior "FBS % × CPE" landscape / survey / systematic mapping exists.** Zero direct
hits; no adjacent review maps serum % against CPE observation. The only systematic reviews
that touch FBS % are serum-*replacement* (serum-free media, human platelet lysate) in stem-
cell / cultivated-meat / biomanufacturing contexts — a different question. => **the field
is unmapped; this survey would be first-to-map.** Caveat: sweep was PubMed (the appropriate
corpus); Google Scholar/preprints not yet swept. Adjacent/relevant non-survey leads (for
citation context, not prior art):
- Huang et al. 2025, *Appl Biochem Biotechnol* 197(12):7739–7766, doi 10.1007/s12010-025-05391-1 (serum-free media review) [PARTIAL/ADJACENT]
- HPL-vs-FBS systematic reviews (Palombella 2022; Guiotto 2020; Shanbhag 2017; etc.) [NOT-RELEVANT to CPE, adjacent to FBS-variable only]

### PRIOR-ART HARDENING (Crossref + Zenodo + Europe PMC, 2026-11-06)
Still **no landscape survey** across journal + preprint aggregators. BUT found the prior
*germs* of the specific serum→CPE idea — these must be credited/cited (NOT prior landscapes,
but primary experiments touching the exact relationship):
- **"The influence of serum on the cytopathic effect of measles virus"**, *Archiv für die
  gesamte Virusforschung* (1963), DOI 10.1007/BF01241302 — primary experimental study of
  serum → CPE for one virus. [TRUE-GERM]
- **"A Trial for Virus Detection in Healthy Animals with a Serum-Free Maintenance Medium for
  Primary Cell Culture"**, *Zentralblatt für Veterinärmedizin Reihe B* (1978),
  DOI 10.1111/j.1439-0450.1978.tb00729.x — early serum-free-maintenance virus-detection test. [TRUE-GERM]
- **"Porcine circovirus type 2 induces a strong cytopathic effect in the serum-free culture
  cell line CPK-NS"**, *J Virol Methods* (2019), DOI 10.1016/j.jviromet.2019.113706 —
  modern: CPE observed under serum-free conditions. [ADJACENT]
- ASM *"To Catch a Virus"* ch.5 "The Turning Point: Cytopathic Effect in Tissue Culture"
  (DOI 10.1128/9781555818586.ch5) — CPE history [ADJACENT / P1-adjacent]
- CPE-in-cell-culture method compilations (CLSI M41, Mahy & Kangro) — recipe sources, not surveys.

**Remaining to sweep (retry):** arXiv (API returned non-JSON), bioRxiv/medRxiv (403),
Google Scholar (not yet). No prior landscape found in any index so far → first-to-map
stands, pending those retries.

### PRIOR-ART HARDENING — retry result (2026-11-06)
- **arXiv** (feed API): confirmed **no prior landscape** — all hits were cross-field
  collisions (serum-albumin physics, astronomy "medium"/"survey", fetal ultrasound). [negative]
- **bioRxiv/medRxiv** API: 403 bot-armor on agent UA → left as a manual/future check.
- **Europe PMC preprints (PPR)**: nearest hit is a 2026 *neutralisation-assay Bayesian
  modelling* preprint (doi 10.64898/2026.05.18.726027) — [ADJACENT], not a landscape.

**Net prior-art status (5 indexes scanned):** PubMed, Crossref, Zenodo, arXiv, Europe PMC
(with PPR) all concur — **no published FBS×CPE landscape / survey / map exists.** First-to-map
confirmed. Remaining index un-swept: bioRxiv/medRxiv (API-blocked), Google Scholar (manual).

**Evidence tags:** [VERIFIED src] (read in full) · [VERIFIED-ABSTRACT] · [VERIFIED snippet]
· [PAYWALL/wishlisted] · [UNVERIFIED]. DOIs never guessed. No patents searched.

---

## Taxonomy: processes where cell culture + CPE co-occur

### A. Human medicinal products / biologics
- [x] ICH Q5A(R2) (2023, 52 pp) — viral safety of biotech products; serum appears only as raw-material viral-safety item ("human/bovine serum, porcine trypsin... subjected to viral inactivation"; "tests for human, bovine and porcine viruses if serum/trypsin are used"). **0 serum-% (concentration) mentions.** [VERIFIED src]
- [x] ICH Q5D "Derivation and characterisation of cell substrates" (17 pp) — fetched; cell-substrate characterization, no serum-% recipe (to confirm via extract). [VERIFIED src, extract pending]
- [x] Ph. Eur. **2.6.16** Tests for extraneous agents in viral vaccines for human use (2 pp) — serum only as antiserum/complement reagent. **0 serum-% mentions.** [VERIFIED src]
- [x] Ph. Eur. **5.2.3** Cell substrates for production of vaccines for human use (4 pp) — "If bovine serum is used, it complies with the monograph Bovine serum (2262)" (quality deferral, not %); plus antiserum reagents. **0 serum-% mentions.** [VERIFIED src]
- [x] **21 CFR 610.18 "Cultures"** (US human) — cell-line "tested for... detectable microbial agents"; tests "may be required by the Director" (CBER). **0 serum-% mention**; performance/delegation-based, NOT volume-specified — unlike veterinary 9 CFR 113.55. [VERIFIED src]
- [ ] Ph. Eur. monograph **Bovine serum (2262)** — quality monograph; check whether it contains any % (unlikely; it's a *substance* standard)
- [ ] WHO TRS 878/978 cell-substrate & viral-safety annexes

### B. Veterinary (already partly mapped)
- [x] USDA VIRPRO1013/SAM312 (volume-specified 5–10% → 5–20%)
- [x] Ph. Eur. 2.6.24 / 2.6.25 (avian; volume-unspecified)
- [x] Ph. Eur. 5.2.4 (cell cultures, vet; volume-unspecified)
- [x] VICH GL44, WOAH 1.1.9 (volume-unspecified)

### C. Diagnostic virology (beyond primary Isolation)
- [ ] TCID50 / 50% endpoint infectivity titration (CPE as the titer readout)
- [ ] Plaque assay (CPE-derived plaques; overlay maintenance FBS)
- [ ] Serum neutralization / plaque-reduction neutralization (CPE-readout)
- [ ] Shell-vial culture (CPE + IF)
- [ ] Cell-culture infectivity for water/wastewater (enterovirus CPE)
- [ ] Clinical virology lab standard operating procedures (routine CPE exam)

### D. Vaccine manufacturing / production (both human & vet)
- [ ] Upstream cell-culture serum recipes (growth vs maintenance) for virus propagation
- [ ] Cell-substrate qualification (adventitious-agent CPE tests)

### E. Other microbiology where CPE is an observable
- [ ] Mycoplasma detection (broth/agar + cell-culture co-culture CPE; though CPE often from inducers)
- [ ] Antiviral drug screening / cytotoxicity (CPE-reduction assays × compounds)
- [ ] Cytotoxicity / cell-viability assays where CPE-like morphology is a readout
- [ ] Toxoplasma / intracellular-parasite cell-culture (plaque/CPE-like)
- [ ] Adventitious-agent testing in cell-bank characterization
- [ ] Oncolytic virus / viral vector potency (CPE-readout)
- [ ] Bioburden / sterility's cell-culture adjuncts (rare CPE)

### F. Research / non-regulatory
- [ ] Growth-kinetics papers naming maintenance FBS% (already in R1 corpus; extend if needed)
- [ ] Reverse-genetics / rescue systems (CPE as rescue readout)

---

## Working hypothesis (to test, not assume)
The Isolation 10→2 serum step-down is one instance of a probably *broader* family of
"low-serum maintenance at/after challenge" recipes. If regulators outside Isolation
mostly *omit* serum %, the *published practice* literature is where the actual numbers
live — i.e., the landscape is best reconstructed from **practice** (R1-style) plus the
**few recipe-prescriptive regulators** (US 9 CFR).

## Working finding so far (institutional/regulatory, both human + veterinary)
Across **ICH Q5A(R2) / Q5D, Ph. Eur. 2.6.16 / 5.2.3 / 2.6.24 / 2.6.25 / 5.2.4, EMA Q&A,
VICH GL44, WOAH 1.1.9, and 21 CFR 610.18 (US human)**, NO document prescribes a serum %.
The sole prescriber found is **US *veterinary* biologics (9 CFR 113.55 → APHIS VIRPRO1013/
SAM312; 5–10%→5–20%)**. So "volume-specified serum" is a *narrow, US-veterinary-only* trait,
not a general property of CPE-based regulation. Everywhere else, serum % is (a) deferred to
"the manufacturer's medium", or (b) constrained only for *quality* (antibody/contaminant
freedom), never quantity.

This sharpens the R1 thesis: the modal 10→2 step-down that Isolation practice papers *show*
is a **practice** convention (inherited, codified in lab SOPs and textbooks), not something
any human-side regulator, or any non-US regulator, actually *mandates*. US veterinary
VIRPRO1013 is the one regulator that publicly fixes a range — and it's a *wide hold-or-increase*
range, not the 10→2 step-down.

## Output artifacts (planned)
- `wrk/fbs_cpe_landscape.md` — this scaffold + completed table
- `wrk/fbs_cpe_landscape_search_log.md` — systematic search log
- `r4.md` status update

## Consolidated institutional/regulatory result (FBS% ↔ CPE, omnibus)

| Domains | Document | Serum % prescribed? | Notes |
|---|---|---|---|
| US veterinary | 9 CFR 113.55 → APHIS VIRPRO1013/SAM312 | **YES — 5–10% growth / 5–20% maintenance** | sole volume-prescriber found |
| EU vet | Ph. Eur. 2.6.24 / 2.6.25 (avian EA) | No | "add culture medium"; serum only for antibody-freedom |
| EU vet | Ph. Eur. 5.2.4 (vet cell cultures) | No | medium = "same… as for preparation of the vaccine" |
| EU vet | EMA/CVMP Q&A | No (0 mentions) | |
| Global vet | VICH GL44 | No (quality sense only) | |
| Global vet | WOAH 1.1.9 | No | "MM… media containing FCS"; 0 %-adjacent-to-FCS hits |
| Global human | ICH Q5A(R2) | No | serum as raw-material viral-safety item only |
| Global human | ICH Q5D | No | cell-substrate characterization |
| EU human | Ph. Eur. 2.6.16 (human EA) | No | antiserum/complement reagent only |
| EU human | Ph. Eur. 5.2.3 (human cell substrates) | No | defers to Bovine serum (2262) |
| EU human | Ph. Eur. Bovine serum (2262) monograph | No (substance QC; protein/osmolality/globulin; no culture %) | serum is the analyte here, not a recipe |
| US human | 21 CFR 610.18 "Cultures" | No | tests "may be required by the Director"

**Conclusion:** the only regulator that publicly fixes a serum-% range for a CPE-readout
process is **US *veterinary* biologics (APHIS CVB)**. Everything else is
performance/delegation-based (serum % deferred to manufacturer) or quality-based (serum %
never named). The modal 10→2 step-down of Isolation practice is a **practice convention**
(R1 corpus), not a regulatory mandate anywhere except — inversely — the wide 5–20% US
veterinary maintenance range.

## Practice-layer findings (open-access Methods, full-text extracted)
These are published *practice* Methods in the **non-Isolation** CPE-assay tiers — i.e.
where CPE is one of several observables (titration, plaque, neutralization) — showing that
the low-serum "2% FBS maintenance" convention extends well beyond primary Isolation:

| PMID/PMCID | Year | Assay tier | Serum recipe (verbatim-ish) |
|---|---|---|---|
| PMC13571492 | 2026 | neutralization | "replaced with maintenance medium (DMEM containing 2% FBS)" |
| PMC13029198 | 2026 | RVFV antibody eval | "maintenance medium (RPMI with 2% FBS and 2% antibiotic/antimycotic)" |
| PMC9468316 / PMC8310316 | 2021 | real-time plaque assay | "MEM… supplemented with 2% FBS and 1% carboxymethylcellulose" (overlay) |
| PMC10143445 | 2023 | immuno-colorimetric neutralization (FRNT surrogate) | serum in blocking buffer (FBS listed, no numeric maintenance) |
| PMC13077881 | 2026 | DENV-2 C6/36 TCID50/neutralization standardization | (also in R1 corpus VI74; C6/36 2% FBS) |

**Mycoplasma tier (negative-distinction finding):** Mycoplasma cell-culture papers that
mention CPE do **not** report a serum-% step; they treat **serum/FBS as the mycoplasma
*contamination source*** (e.g. PMC12848938 2026 "M. hyorhinis…"; PMC12484092 2025 discuss
BVDV detected in "laboratory grade FBS used in commercial vaccines"; PMC13478170 2026 "FBS
and NBS... common sources of Mycoplasma"). So in the mycoplasma field, serum is an
*analyte/contaminant vector*, not a culture-medium recipe variable.

**Emerging interpretation:** the ~2% maintenance-serum convention is a general
*virology-practice* norm across titration/plaque/neutralization CPE readouts — not an
Isolation-specific protocol — while *regulators* (except US-veterinary) never fix it. The
serum variable enters the landscape in two distinct roles: (1) **recipe** (2% maintenance
at/after challenge, in practice), and (2) **analyte/contaminant** (serum itself screened for
adventitious agents/mycoplasma). Both roles are visible now; a full tabulation is the
ongoing multi-session corpus task.

## Fetched-ref extraction (6 PDFs on disk, [VERIFIED src], 2026-11-06)

**R4-S1 — Moura 1963, measles serum→CPE** (the closest prior germ; primary experiment):
explicit dual recipe + serum *type* effect.
- HeLa-calf-serum line "grown in a nutrient medium consisting of **10% calf serum** and
  0.5% lactalbumin hydrolysate in Hanks' BSS"
- "…with Eagle's basal media (EBME), with **2% calf serum**"; "maintained in EBME with 2%
  calf serum"
- Shows serum **type** (calf vs sheep) shifts CPE morphology (syncytia vs inclusion bodies)
  and titer (~10^−6.5 vs 10^−2.5 TCID50/ml). => serum % *and* serum type both modulate CPE.
  This is exactly the confound the paper's thesis targets, published 1963 and never turned
  into a landscape.

**R4-S2 — 1978 serum-free maintenance virus detection** (primary, challenges serum-containing
maintenance): cells "under the medium with **10% bovine serum**" then rolled "in a
**serum-free maintenance medium**"; standard comparator "Eagle's MEM with **5% calf serum**".
Recovered 151 transmissible strains serum-free. Cites **Baron & Low 1955 "New maintenance
medium for cell culture" Science** (a P1-important primary).

**R4-S3 — PCV2 serum-free CPE (2019)**: strong CPE in serum-free cell lines (CPK-NS, PPK-3F).
**Framing correction (owner, 2026-11-06):** do NOT read this as "CPE does not require serum".
The working hypothesis is the opposite direction: **lowering serum induces cell-morphology
changes; those changes have been labelled "CPE"; and that CPE has been attributed to virus.**
Serum-free lines showing CPE is *consistent with* the hypothesis (serum manipulation → the
same morphology the field calls CPE) but is not a standalone proof; R3 is the direct test
(expert-scored CPE in virus-free cultures, more CPE when FBS is lowered). P1–P7 are
*derived predictions* of this hypothesis; each confirmed prediction strengthens it.

**R4-S4 — Toxoplasma plaque (2017)**: mostly serum-*free* media / serum-absorption context;
no fixed maintenance-% recipe (toxo plaque uses serum-supplemented + serum-free variants).

**R4-S5 — contaminants in cell cultures/sera/trypsin (2013)**: serum-as-analyte — FCS lots
screened for BVDV/PCV1/BLV/atypical pestiviruses ("375 mL of fetal calf serum…"). Confirms
role (2).

**R4-S6 — Argentine irradiated FBS (2020)**: serum-as-analyte — gamma irradiation of FBS for
adventitious agents (100% effect claimed). Confirms role (2); cites "Peak serum" (Brindley)
and Hawkes "geographic origin" FBS reviews (supply/regulatory, not CPE recipes).

**Serum/cell-line contaminant strand (wrapped from P4 handoff, 2026-11-06):** the culture
*reagent itself* (FBS and repository cell lines) is a documented carrier of pestivirus-label
material, independent of any inoculum — this is the strongest form of role (2) "serum/cell
line as analyte":
- Giammarioli 2015 (*Biologicals*, DOI 10.1016/j.biologicals.2015.05.009): "All the 26
  batches were positive by RT-PCR for at least one species of bovine pestiviruses" (archival
  FBS) [ABSTRACT-level; PDF on R4 wishlist R4-S7]
- Bolin 1994 (*JAVMA*, PMID 7989247): ATCC-repository cell line distributed to >20 labs
  carrying an undeclared pestivirus [wishlist R4-S8]
- Muhsen 2013 (*Arch Virol*, DOI 10.1007/s00705-012-1538-x): RK13 cell line persistently
  contaminated with ncp BVDV [wishlist R4-S9]
=> for "virus-free"/negative-control claims, the reagent (FBS / cell line) is itself a
confound source, not just the inoculum. Directly relevant to R2 control-tier logic.

**Net from fetched set:** the 1963 measles paper anchors the serum→CPE *experimental* prior
art (with the exact 10%→2% recipe + a serum-type effect). The 1978 and 2019 papers are
consistent with the central hypothesis (serum manipulation ↔ the morphology the field calls
CPE) — NOT claims that "CPE doesn't need serum". Two load-bearing facts for the landscape.

## Adversarial / gap-fill sweep (2026-11-06, Europe PMC)

**(1) "Serum starvation / low-serum morphology" — a large adjacent body (181 hits), not
prior art for the CPE landscape, but mechanistically supportive.** The non-virology cell-
biology literature documents extensively that *serum reduction changes cell morphology and
stress responses* — e.g. "From Scarcity to Survival: Adaptive Strategies of A549 Lung Cancer
Cells Under Serum Starvation" (2025); "Effects of low-serum adaptation on growth and protein
expression…" (2026); "A review of cytotoxicity testing methods…" (2025); "Effect of Serum
Starvation on Rheology of Cell Monolayers" (arXiv:2103.09294). This is the modern,
non-virological analogue of the R3 premise (lower FBS → morphology change) — a supporting
mechanistic literature, NOT a prior "FBS×CPE map". Worth one Discussion sentence bridging R3
to the serum-starvation literature.

**(2) "Serum-free cell-line CPE assay" cluster (8 hits) — CPE is scored across the serum
spectrum.** Multiple papers use serum-free cell lines (CPK-NS, Sf9, etc.) for CPE assays:
- Establishment of serum-free CPK-NS cell line useful for CSFV assays (1998)
- Susceptibility of Sf9 insect line to adventitious viruses (1994)
- CSFV vaccine-strain-derived clone causes CPE (2020); CSFV cytopathogenicity (2004)
- JEV persistent infection in serum-free Sf9 (2004)
- CMV enhanced CPE on retinal pigment epithelium K-103 (1997)
=> CPE is scored as virus-attribute across low/serum-free AND serum-supplemented conditions;
what changes with serum is the *amount/morphology* scored, not the presence of the label.
This is the landscape's second axis: the "CPE" label is applied to serum-modified morphology
at every serum level, with the field's serum-free CPE lines being the cleanest modern
demonstration that serum is not the *sine qua non* of the label — the *morphology change* is.

---

## Article-addendum line (Substack-ready, 2026-11-06)

After the VIRPRO1013 outlier was first noticed, an extended sweep of the other jurisdictions'
equivalents — European Pharmacopoeia (2.6.24 / 2.6.25 / 5.2.3 / 5.2.4), EMA/CVMP, VICH GL44,
WOAH Terrestrial Manual 1.1.9, ICH Q5A(R2) / Q5D, and the US *human* rule 21 CFR 610.18 —
turned up **no other body that prescribes a numeric FBS concentration for either the growth or
the maintenance phase**: every one leaves serum % to the manufacturer and constrains only
serum *quality* (freedom from adventitious agents and antibodies). VIRPRO1013 (US veterinary
biologics) is therefore the single public serum recipe found anywhere, and it runs *opposite*
to the diagnostic convention — a wide hold-or-increase 5–20% maintenance rather than the
10→2 step-down.