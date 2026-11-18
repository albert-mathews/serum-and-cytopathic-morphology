# R6 — extract (processed items: overlay, mycoplasma, autophagy, adhesion)

Grouped note for the remaining fetched PDFs read 2026-11-18. All `[VERIFIED src]` (full text in `refs/`).

## R6-M11 / plaque-shape control (extend framing-2)

**R6-011 — Oaks, Wingfield & Formal 1985 (Shigella plaque, HeLa).**
> "One factor that had a significant effect on plaque size was the overlay medium. Tissue culture media such as
> MEM did not permit the formation of large plaques… when DMEM is present in the overlay. Compared with MEM, DMEM
> has a higher concentration of several nutrients… MEM was supplemented with glucose, pyruvate, or iron. The
> overlay containing MEM supplemented with a high concentration of glucose permitted plaques of normal size to
> form."

⇒ plaque *diameter* is set by **overlay nutrient content (glucose)**, even for a bona-fide intracellular
replicator — so plaque size is medium-controlled, not particle-controlled. Also: "Plaque formation was a result
of intracellular multiplication… (gentamicin) killing extracellular [bacteria]"; temperature-dependent
(30°C → no plaques; 37°C → plaques) — plaque formation is condition-sensitive.

**R6-018 — Baer & Kehn-Hall 2014 (J Vis Exp; overlay systems).**
> "Plaque morphology can vary dramatically under differing growth conditions… Plaque size, clarity, border
> definition [vary]." "Minor modifications in plaque assay conditions can significantly alter results." Overlays:
> VEEV plaques larger in agarose/liquid than CMC ("lower viral inhibition"); influenza sensitive to "differing
> brands of agarose."

⇒ framework support (R6-M11): plaque size/border is an **overlay+medium property**.

**R6-010 — Cooper 1984 (Methods in Virology, 69 pp).** Sections "Mode of Development of a Local Lesion";
"Criteria and Requirements for a Reproducible Plaque Assay" — the canonical mechanics review; underpins the
above, key content already captured via Fenner/Dulbecco/Abedon.

## R6-M8 / mycoplasma CPE-mimic + the rule-out control

**R6-013 — Lopes et al. 2021 (HEp-2 mycoplasma).**
> morphological alterations "cytoplasm elongation, cell-to-cell spacing, thin plasma membrane projections,
> cytoplasmic vacuoles, fusion with neighboring cells"; a "severe cytopathic effect"; mycoplasma "may alter the
> course of viral infection"; but "did not alter the turbidity of culture medium."

**R6-015 — Uphoff & Drexler 2002.**
> "mycoplasma contamination as the single biggest problem in the culture of continuous cell lines. Mycoplasma
> infection can affect virtually every parameter and functional activity of the eukaryotic cells." (236 chronically
> contaminated lines; antibiotic cure 66–85%/round, 95% overall; detect by ≥3 assays incl. PCR.)

⇒ M8 is a real confound (frank CPE mimic, invisible, ubiquitous) AND is **ruled in/out by a defined test**
(PCR/Hoechst + antibiotic eradication). This is the operative control that separates M8 from M1/M2 in the CRO
record (which used a single stock split into two arms — a mycoplasma contaminant does not by itself produce a
clean serum-dose A vs B split, placing M8 lower in the prior for *this* experiment).

## R6-M10 / Vero starvation autophagy (vacuolation)

**R6-017 — Peng et al. 2026 (Vero CTGF).**
> "adaptation to serum-free suspension culture is hindered by excessive autophagy"; EBSS starvation → autophagy
> (LC3-II/I ↑, autophagosomes by TEM); "Cells at 70–80% confluence were starved"; starvation → apoptosis;
> CTGF knockdown "reduce[s] autophagy and adhesion."

⇒ Vero responds to serum/nutrient starvation with **autophagy + reduced adhesion + apoptosis** — supplying the
CLSI "vacuolation"/"granularity" descriptors (M10) and the adhesion-loss (M6) in the same stress response.

## R6-M6 / adhesion loss & R6-M1 Vero growth arrest

**R6-005 — Genari, Gomes & Wada 1998 (Vero nutritional stress).**
> stressed Vero "presented multilayered growth, with aggregate or spheroid formation which detached on the flask
> surface"; "adhesion index and fibronectin synthesis and distribution were altered"; stressed cells were
> "transformed by nutritional stress conditions." (A stress-induced adhesion/spheroid phenotype; relevant to M6.)

**R6-006 — Engelhardt & Mao 1977 (Vero serum factor → G2).**
> serum depletion → Vero "cannot pass through a transition point in G2… accumulating in the late S and G2 period";
> a serum factor (fetuin/albumin) is required for division. (Supporting — serum step → growth arrest, the
> proliferative complement to the death read; not the immediate-death mechanism.)

*End. IDs R6-005/006/010/011/013/015/017/018 all read & recorded in `R6_useful.csv`.*
