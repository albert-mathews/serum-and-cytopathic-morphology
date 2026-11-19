"""Descriptor-grounded negative-control CPE outcome assignments (re-pass 2026-11-19).

One entry per Isolation-stage NC paper (nc_isolation_stage=yes) in the R1 category-1
universe, coded against the protocol CPE descriptor set (CLSI M41 Table 7 + ASM
"Cytopathic Effects of Viruses" theory) — see control-cultures.md §7.5b.

Codes:
  1 = control's reported appearance includes a protocol CPE descriptor (any timescale)
  2 = control explicitly normal / no CPE / healthy / intact / uninfected
  3 = morphology alluded to but ambiguous / partial / unclear
  4 = control present but its morphology/CPE outcome not described

Each entry: id -> (code, free_text, verbatim_quote)
"""
from __future__ import annotations

# (code, free, quote). Quotes are verbatim, quote-sized.
ASSIGN = {
    # ---- Tier A ----
    "VI33": ("2",
        "Uninoculated (PBS) control well on each plate; the control is shown as '(A) Normal uninfected cells' "
        "(no CPE stated).",
        "A control well inoculated with sterile phosphate-buffered saline (PBS) was included on each plate. "
        "... (A) Normal uninfected cells."),
    "VI97": ("2",
        "Uninoculated MDBK control; the paper states the control stayed healthy.",
        "The control cells remained healthy during the period. ... MDBK cells without sample inoculation was "
        "also incubated as control."),
    "VI117": ("1",
        "Uninfected monolayers showed detachment, nonspecific degeneration and abnormal gross morphology "
        "(rounding) under L-15 + 1-2% FCS maintenance, no virus - protocol CPE descriptors (detached, "
        "nonspecific degeneration). The paper attributes deterioration to storage/aging, not virus.",
        "Comparable uninfected cultures were maintained as controls. [Table 1: morphology 2+ = 'cells not "
        "confluent and abnormal in gross morphology'; 1+ = 'severe degeneration and many have detached'; "
        "0 = 'complete degeneration and most or all have detached' - decayed under L-15+1%/2% FCS, no virus.]"),
    "VI121": ("2",
        "Normal, uninfected WI-38 microcultures served as the IFAT control throughout the study.",
        "... control microcultures of adenoviruses types 2, 4, and 7 and normal, uninfected WI-38 "
        "microcultures were stained by the IFAT ..."),
    "VI272": ("2",
        "Sterile-medium control wells: CPE absent.",
        "No CPE was observed in control wells (Figure 1B)."),
    "VI288": ("2",
        "Control cells inoculated with maintenance medium (no virus): CPE absent.",
        "No CPE was observed in the control cells inoculated with maintenance medium."),
    "VI16": ("4",
        "Control = scrapings from non-viral infectious keratitis (specimen-source), cultured in parallel; only "
        "a negative YIELD ('None of the controls yielded HSV-1') is reported - the control's cell morphology / "
        "CPE outcome is not described.",
        "Scrapings obtained from 10 patients with infectious keratitis of non-viral origin were included as "
        "controls. ... None of the controls yielded HSV-1."),
    "VI38": ("4",
        "Mock-infected Vero E6 used as the no-infection baseline across viability / titer / IFA assays; the "
        "mock control's morphology/CPE outcome is not described (endpoints are infectivity and viability).",
        "Vero E6 cells ... were mock infected or infected with SARS-CoV-2 (P3) at an MOI of 1 ..."),
    "VI57": ("4",
        "Mock-infected wells with 2% FBS L-15 maintenance; match is real but the readout is ELISA/OD, and no "
        "CPE/morphology outcome for the mock is stated.",
        "mock infected with 2% FBS media. ... For mock-infected wells, this was done with 2% FBS L-15 Leibovitz "
        "media instead."),
    "VI249": ("4",
        "Negative-control well seeded with SFM-adapted MDCK; control used for flow-cytometry gating "
        "(FMO / lectin-negative), no CPE-morphology outcome described.",
        "One of the 4 wells in each empty column of wells was also seeded with SFM-adapted MDCK cells to serve "
        "as a negative control."),
    "VI281": ("4",
        "Negative control = PBS / hepatitis-E-negative culture medium; endpoint immunostaining / RNA yield; "
        "no cell CPE outcome described.",
        "Cells were then inoculated with 100 µL of virus extract or medium (negative control) in duplicate."),
    "VI43": ("3",
        "Uninoculated control = surviving-cell baseline in 2% FBS DMEM; morphology framed as survival/cell "
        "number rather than a CPE-vs-no-CPE claim.",
        ""),
    "VI53": ("3",
        "Medium-only 'cell control' wells and an uninfected (uninoculated) control group were cultured under "
        "the same conditions for 72 h and observed microscopically; the control's morphology outcome is not "
        "stated in the text (figure-labelled 'Negative Control').",
        "wells containing only cell culture medium served as cell controls. ... MDBK cells infected with the "
        "HB2411 strain (experimental group) and uninfected cells (control group) were cultured under similar "
        "conditions for 72 h, followed by systematic observation using microscopy."),
    "VI93": ("3",
        "Blank uninfected control under identical 2% FBS conditions; morphology observed only as the reference "
        "('morphology similar to uninfected controls'), no distinct blank-no-CPE sentence.",
        "Both uninfected (blank control) and virus-infected (positive control) groups were maintained under "
        "identical culture conditions at 37 °C with 5% CO₂."),

    # ---- Tier B ----
    "VI102": ("2",
        "Mild CPE and/or clumping appeared in all inoculated cultures EXCEPT the mock-infected control "
        "(mock = no CPE).",
        "Mild CPE and/or clumping of cells were observed in all cell cultures with the exception of "
        "mock-infected control cultures."),
    "VI13": ("2",
        "CPE absent in mock-infected cells (explicit).",
        "CPE was not observed in mock infected cells (Figure 1, panel A)."),
    "VI14": ("2",
        "Mock Hep-2 labelled 'uninfected', set against 'CPE positive' cells (the mock is the no-CPE "
        "counterpart).",
        "CPE positive and uninfected (mock) Hep-2 cells ..."),
    "VI211": ("2",
        "Control cells remained morphologically normal (explicitly, under low-serum 'Bristol' medium).",
        "Control cells appeared to remain morphologically normal for longer periods under this \"Bristol\" "
        "medium than under the Eagle's medium."),
    "VI221": ("2",
        "Uninoculated control cultures (and non-hepatitis serum-inoculated controls) failed to yield a "
        "cytopathic agent after 6+ blind passages; uninoculated monolayer shown for comparison.",
        "Two sets of control cultures, one uninoculated, and the other inoculated with serum from patients "
        "having no clinical or chemical evidence of hepatitis, failed to yield a cytopathic agent after 6 or "
        "more blind passages. ... Uninoculated monolayer is included for comparison."),
    "VI265": ("2",
        "PBS-inoculated negative-control monolayer did not show the (CPE) changes seen in infected cells.",
        "The monolayer infected with sterile PBS (negative control) did not show such changes (Plate 1)."),
    "VI266": ("2",
        "Intact (uninfected) HeLa, HEp-2 and Vero cells used as the plate controls.",
        "Intact HeLa, HEp-2, and Vero cells were used as controls in each plate."),
    "VI276": ("2",
        "All mock-infected cells showed normal morphology (explicit).",
        "All mock-infected cells showed normal morphology."),
    "VI280": ("2",
        "No cytopathic changes in mock-infected controls (explicit); infected cells showed rounding, fusion, "
        "syncytium formation.",
        "infected cells developed characteristic cytopathic effects (CPE), including cell rounding, fusion, "
        "and syncytium formation, whereas no cytopathic changes were observed in mock-infected controls "
        "(Figure 3A)."),
    "VI52": ("2",
        "Normal (uninfected) Vero cells used as the reference control (explicit 'normal').",
        "Left, normal Vero cells as control."),
    "VI59": ("2",
        "Mock-infected cells showed no CPE (explicit); mock-inoculated cultures gave no RT-PCR amplification.",
        "mock-infected cells (no CPE). ... no amplification was obtained from mock-inoculated control "
        "cultures maintained in parallel (Figure 5)."),
    "VI60": ("2",
        "Significant CPE in the PIV5 group but not the mock group (explicit contrast).",
        "significant CPE was observed in the first-generation blind passages of PIV5 group as opposed to "
        "Mock group (Figure 1A)."),
    "VI74": ("2",
        "Untreated C6/36 negative-control cells maintained NORMAL morphology - while cells exposed to SERUM "
        "(complement) or DENV-2 showed similar cytopathic changes (a virus-independent CPE observation in the "
        "same assay).",
        "untreated C6/36 cells (negative control) maintained their normal morphology, while cells exposed to "
        "serum (complement) or DENV-2 NGC exhibited similar cytopathic changes."),
    "VI76": ("2",
        "Mock (CMNV-negative healthy-shrimp tissue extract) control confirmed the CPE is virus-specific.",
        "SUPPLEMENTARY FIGURE 2 Mock-controlled infection assay confirms virus-specific CPE of CMNV in EPC, "
        "TiB and S2 cell lines."),
    "VI77": ("2",
        "Uninfected/mock control cells remained flat and adherent; mock-inoculated LLC-PK shown as normal "
        "cells.",
        "Uninfected control cells (Figures 2A-D) remained flat and adherent to the culture plate. ... "
        "(A-D) Mock-inoculated LLC-PK cell culture displays normal cells."),
    "VI83": ("2",
        "Control cells remained normal while infected cells showed shrinkage and detachment (explicit).",
        "infected cells gradually exhibited CPEs characterized by cell shrinkage and detachment, whereas "
        "control cells remained normal (Figure 1C)."),
    "VI87": ("2",
        "Mock-infected control cells maintained normal morphology throughout (explicit).",
        "mock-infected control cells maintained a normal morphology throughout the experiment (Figure 1E)."),
    "VI108": ("3",
        "'Control denotes negative control, i.e. no virus' in the CPE/FA table, but the semen matrix makes the "
        "control's exact morphology ambiguous (cytotoxicity vs no-CPE not cleanly separated).",
        "Control denotes negative control, i.e. no virus [table note]."),
    "VI111": ("1",
        "Control (non-Crohn's) tissue cultures developed CPE descriptors (rounded/refractile HeLa; narrowed "
        "cells, irregular surface, intercellular gaps in MRC5) after a longer delay; a blind study found the "
        "cytopathic effect more often in control-subject than Crohn's material. Specimen-source control, not "
        "an uninoculated mock.",
        "The control tissue cultures remained healthy for longer but similar changes occurred in them "
        "eventually. ... The blind study revealed that a similar cytopathic effect was observed even more "
        "often in tissue cultures inoculated with material from control subjects."),
    "VI116": ("3",
        "Uninoculated HFDL/CMK monolayers shown as the no-effect baseline (Fig 1 B/D). The paper is a "
        "PUBLISHED virus-independent-CPE confound: C. difficile toxin (non-viral) produces 'a cytopathic "
        "effect ... similar to a viral cytopathic effect' (rounding + elongated cytoplasmic processes) in "
        "routine Isolation cultures; the negative control (uninoculated) itself did not show CPE.",
        "uninoculated HFDL cells [Fig 1B]; uninoculated CMK cells [Fig 1D]. ... The cytotoxicity of C. "
        "difficile toxin can be distinguished from a viral cytopathic effect by characteristic rounding of "
        "the cells and elongated cytoplasmic processes ..."),
    "VI119": ("3",
        "Uninoculated RD cells shown as the reference ('(A) Uninfected RD cells'); no verbal no-CPE/normal "
        "statement about the control in the extracted text.",
        "(A) Uninfected RD cells"),
    "VI253": ("3",
        "Uninfected Vero E6 shown (figure) at 22 days after preparation as the no-infection reference; no "
        "verbal 'normal/no CPE' statement.",
        "(g) Uninfected Vero E6 cells 22 days after preparation."),
    "VI286": ("3",
        "Infected cells showed partial rounding/shrinkage/elongation 'compared to the mock-infected control'; "
        "the mock's normal state is contrast-implied but not explicitly stated.",
        "Compared to the mock-infected control group, partial cell rounding, shrinkage, and elongation were "
        "evident at 48 h post-infection (hpi) (Figure 1A)."),
    "VI8": ("3",
        "Mock-virus-infected Vero E6 shown (figure) versus 2019-nCoV; mock cells named as controls but no "
        "explicit 'mock stayed normal / no CPE' sentence.",
        "Vero E6 cells are shown at 24 h after infection with mock virus (a) or 2019-nCoV (b)."),
    "VI203": ("4",
        "Control = non-viral keratitis scrapings (specimen-source), negative by HSV-1 yield; uninfected-cell "
        "IF counterstain shown, but no culture CPE outcome described.",
        "Scrapings obtained from 10 patients with infectious keratitis of non-viral origin were included as "
        "controls. ... None of the controls yielded HSV-1."),
    "VI208": ("4",
        "Uninfected (sham, diluent-only) monolayers used as controls for a chemoattractant assay; their CPE "
        "outcome is not stated (only 'no CPE in inactivated-virus monolayers' is noted).",
        "Cell monolayers handled in an identical fashion, except that they were sham inoculated with the "
        "diluent ... instead of R39, were used as uninfected controls."),
    "VI215": ("4",
        "Uninfected flask served as control for replication comparison; control morphology not described.",
        "five flasks were infected and one uninfected flask served as control."),
    "VI217": ("4",
        "Untreated / uninfected cells used for cytotoxicity and plaque-inhibition comparisons; no control-CPE "
        "statement.",
        "Controls consisted of infected untreated Vero cell monolayers."),
    "VI219": ("4",
        "Non-inoculated control pigs remained healthy (animal); in culture, mock-inoculated cultures are "
        "mentioned without a stated CPE outcome.",
        "Non-inoculated control 2-day old pigs kept under the same conditions remained healthy."),
    "VI220": ("4",
        "Uninfected cells used for radiolabelling/immunoprecipitation controls; no CPE-morphology statement.",
        "could not be immunoprecipitated from radiolabeled uninfected cells ..."),
    "VI227": ("4",
        "'CER uninfected cell' / 'Vero uninfected cell' figures; no verbal no-CPE statement.",
        "B) CER uninfected cell; D) Vero uninfected cell."),
    "VI267": ("4",
        "Mock-infected control cells incubated without passage; no CPE/morphology outcome stated for the mock "
        "(the paper notes Vero showed no CPE overall, unrelated to the mock).",
        "MNT-1, LLC-MK2, and Vero cells were inoculated with clinical specimens of HPIV1-4 ... or "
        "mock-infected control and incubated at 34°C and 5% CO2 without passage or medium change."),
    "VI291": ("4",
        "Uninfected Vero-E6 flask passaged in parallel as control; outcome reported only by IFA (no green "
        "dots), not cell CPE.",
        "a flask of uninfected Vero-E6 cells was passaged as a control. ... the control Vero-E6 cells show no "
        "bright green fluorescent dots (B)."),
    "VI36": ("4",
        "Controls are animal-level mock/titration and molecular negative controls; no culture CPE outcome for "
        "a no-virus control described.",
        "Mock infected and UV-inactivated CHIKV infected females were included as control groups."),
    "VI40": ("4",
        "Mock-infected HEp-2/A549 used as the transcriptional baseline; no control-CPE statement (endpoint is "
        "RNA-seq/cytokine).",
        "Cell Line- and Strain-Dependence of RSV Infections ... infected versus mock-infected controls."),
    "VI42": ("4",
        "Mock-treated/mock-infected cultures used for protein-localization assays; no control-CPE statement.",
        "cells were infected with AdORF29 at an MOI of 50 ... or mock infected (lane 1)."),
    "VI51": ("4",
        "Mock-infected cells served as negative controls for IFA/viability readouts; no control-CPE "
        "statement.",
        "Mock-infected cells served as negative controls."),
    "VI58": ("4",
        "PBS-inoculated mock control; no control-morphology outcome stated.",
        "As a mock-infected control, PBS was inoculated in each study."),
    "VI63": ("4",
        "Mock-infected pig controls remained clinically normal (animal); culture control-CPE outcome not "
        "described.",
        "The control group remained clinically normal ... throughout the entire experimental period."),
    "VI67": ("4",
        "DMEM/uninfected cells served as negative controls for IFA; no control-CPE statement.",
        "DMEM was added to the first well of the plate as a negative control."),
    "VI79": ("4",
        "Uninfected control cells/compartments compared to RSV-infected for EMV yield; no control-CPE "
        "statement.",
        "The same conditions were applied to uninfected control cells."),
    "VI82": ("4",
        "Non-infected cells used as controls; no control-morphology outcome stated. ('No CPE' appears in the "
        "paper only about infected cells, not the control.)",
        "Non-infected cells were used as controls."),
    "VI91": ("4",
        "Mock-treated SHS cells used as the sncRNA baseline; no control-CPE statement.",
        "small RNA from mock-treated SHS cells (n = 2/group), or RSV- or MeV-infected SHS cells (n = 3/group) ..."),
    "VI92": ("4",
        "Untreated (no-drug) and uninfected-treated (cytotoxicity) controls for NDGA antiviral study; no "
        "control-CPE statement.",
        "Uninfected cells treated with NDGA were used as the cytotoxicity control (TC) ..."),

    # ---- Tier C ----
    "VI85": ("3",
        "Unchallenged F81 'normal controls' kept typical epithelioid morphology, but were also described as "
        "showing 'minimal age-related morphological changes attributable to prolonged culture duration' - an "
        "aging (non-viral) morphology noted in the control.",
        "control cells exhibited minimal age-related morphological changes attributable to prolonged culture "
        "duration (Figure 1). ... This contrasted with control cells maintaining typical epithelioid "
        "morphology."),
}


# Non-CPE outcome reported for the same control (serology / IFA-antigen / RNA-PCR / viability / yield /
# particle count). Recorded so other streams (P-serology, R6, ...) can reuse; "CPE not described" !=
# "nothing recorded" (CONVENTIONS.md §8). Empty string = no non-CPE readout stated.
OTHER = {
    "VI33": "Control = sterile PBS well (per plate); no separate molecular readout of the control stated.",
    "VI97": "PCR: specific amplicon in positive control + sample, not in the no-inoculation control lane; "
            "control cells shown 'healthy'.",
    "VI117": "Endpoint viral yield/titre on passage (not IFA/PCR); uninfected controls reported only by "
             "morphology (Table 1).",
    "VI121": "IFAT: control microcultures (adenovirus + normal uninfected WI-38) stained as the fluorescence "
             "reference; normal WI-38 = antigen-negative reference.",
    "VI272": "Sterile-medium + tissue-homogenate negative controls; 'All negative controls tested negative' (PCR).",
    "VI288": "Control = maintenance-medium wells; 'fish from control group were negative' by PCR.",
    "VI16": "Control (non-viral keratitis scrapings) negative by HSV-1 yield/IFA: 'None of the controls yielded "
            "HSV-1'; uninfected cells shown by IF counterstain.",
    "VI38": "Mock-infected Vero E6 = infectivity/titre baseline; MTT viability 'Control 100%'; IFA negative for mock.",
    "VI57": "Mock (2% FBS) = ELISA/OD baseline ('positive if >2x negative-control wells'); no fluorescence/CPE discussed.",
    "VI249": "Negative-control well = flow-cytometry gating (FMO + lectin-negative); not a CPE readout.",
    "VI281": "Negative control = HEV-negative medium / PBS; immunostaining negative; RNA-extraction negative "
             "controls (PBS/RNase-free water).",
    "VI43": "Uninoculated control = surviving-cell / cell-number baseline (persistent-SARS infection assay).",
    "VI53": "Untreated/uninfected control cultured 72 h and observed microscopically; PCR positive/negative "
            "controls separate.",
    "VI93": "Blank uninfected control (2% FBS) = reference for drug treatment and IFA ('weaker fluorescence' vs "
            "untreated infected).",
    "VI102": "Mock-infected control = the exception with no CPE/clumping (the only clean culture).",
    "VI13": "Mock (Fig 1A) negative for CPE (CDC isolation letter).",
    "VI14": "CPE-positive vs 'uninfected (mock)' Hep-2 compared by IFA spot slide.",
    "VI211": "Control cells 'morphologically normal' under low-serum 'Bristol' medium (CPE readout; no separate "
             "molecular endpoint).",
    "VI221": "Uninoculated + non-hepatitis-serum controls 'failed to yield a cytopathic agent after 6+ blind "
             "passages' (CPE readout).",
    "VI265": "PBS-inoculated negative-control monolayer did not show the infected-cell changes (CPE readout).",
    "VI266": "'Intact HeLa/HEp-2/Vero cells as controls' (stated intact; no molecular endpoint).",
    "VI276": "Mock-infected cells normal (Fig); mock cell-lysate = mouse control inoculum; 'control mice "
             "behaved normally'.",
    "VI280": "Mock-infected controls: no cytopathic changes + IFA negative for N protein + RT-PCR reference.",
    "VI52": "'normal Vero cells as control' (phase-contrast reference); qPCR/positive controls separate.",
    "VI59": "Mock-infected cells (no CPE) AND 'no amplification from mock-inoculated control cultures' (RT-PCR).",
    "VI60": "Mock group: no CPE (Fig 1A), no NP band (WB), no NP staining (IFA).",
    "VI74": "Untreated C6/36 negative control normal; serum (complement)-exposed cells showed dengue-like "
            "cytopathic changes (see non-viral CPE note).",
    "VI76": "Mock = CMNV-negative shrimp-tissue extract; Supp Fig 2 confirms virus-specific CPE; CCK-8 viability.",
    "VI77": "Uninfected/mock control = flat adherent cells; IFA negative; 'no viral RNA in control group'.",
    "VI83": "Control cells normal (Fig 1C); WB/IFA/ELISA: specific bands/signal in infected, 'not in controls'.",
    "VI87": "Mock-infected control normal morphology; control group also = normal duck-embryo homogenate (animal).",
    "VI108": "Control = 'no virus' wells in the CPE/FA table; FA staining + cytotoxicity columns (semen matrix).",
    "VI111": "Blind study read CPE by morphology across passage; control-tissue cultures developed CPE (code-1).",
    "VI116": "Toxin neutralization: antitoxin neutralized 100-1000 TCD50 of C. difficile toxin; the concurrent "
             "control = a known toxin-positive specimen (not a no-virus control).",
    "VI119": "Uninoculated RD cells = reference (Fig); neutralization 'virus+PBS' control; typing by "
             "suckling-mouse/neutralization.",
    "VI253": "Uninfected Vero E6 shown by microscopy at 22 days (no molecular readout of the control).",
    "VI286": "Mock vs infected metabolomics/LC-MS clustering; 'partial rounding/shrinkage/elongation' contrasted "
             "to mock.",
    "VI8": "Mock-virus Vero E6 = IFA/fluorescence reference (Fig); 'mock-transfected cells used as controls'.",
    "VI203": "Control (non-viral keratitis scrapings) negative by HSV-1 yield: 'None of the controls yielded "
             "HSV-1' (same control wording as VI16).",
    "VI208": "Uninfected sham monolayers: chemoattractant assay (medium attracted 12±2 vs 87±6 PMNL); 'no CPE in "
             "inactivated-virus monolayers'.",
    "VI215": "Uninfected flask control for replication comparison (RT-PCR/IFA based).",
    "VI217": "Uninfected/untreated cells = plaque-inhibition + neutral-red viability denominator.",
    "VI219": "Non-inoculated control pigs healthy and antibody-negative; 'no fluorescing cells in uninoculated "
             "control' (IFA).",
    "VI220": "Uninfected cells = radiolabel/immunoprecipitation negative for viral glycoprotein.",
    "VI227": "'CER uninfected cell / Vero uninfected cell' figures; viral-antigen negative controls listed.",
    "VI267": "Mock-infected control incubated for IF/RT-PCR readout; no CPE statement for the mock.",
    "VI291": "Uninoculated Vero-E6 control: IFA 'no bright green dots'; RT-PCR negative control (nuclease-free water).",
    "VI36": "Animal mock: IHC 'not observed in ... mock-infected dams'; molecular negative controls.",
    "VI40": "Mock = RNA-seq/gene-set baseline (transcriptional, not CPE).",
    "VI42": "Mock-treated/mock-infected cultures = western/imaging baseline for VZV protein localization.",
    "VI51": "Mock-infected cells: IFA 'remained [unstained]' negative control; UnaG fluorescence readout.",
    "VI58": "PBS-inoculated mock control (no stated endpoint for the control).",
    "VI63": "Mock-infected pig controls: seronegative + 'no signal in mock-infected PAMs' (IFA); culture endpoint IFA.",
    "VI67": "DMEM negative-control well; 'no signal in uninfected control cells' (IFA); mice received sterile DMEM.",
    "VI79": "Uninfected cells = EMV/NTA particle baseline (particle count, not CPE).",
    "VI82": "'Non-infected cells used as controls' (no stated endpoint); mock-infected fish (animal).",
    "VI91": "Mock-treated SHS cells = sncRNA/miRNA baseline (RNA-seq, not CPE).",
    "VI92": "Uninfected+NDGA 'cytotoxicity control (TC)'; microtubule-alteration % vs untreated control.",
    "VI85": "Unchallenged F81 controls: IPMA serology 'controls remained seronegative'; control cells 'typical "
            "epithelioid morphology' (with age-related changes).",
}
