# Draft paper

## introduction
This article identifies virology cell culture methods for virus isolation—particularly the reliance on cytopathic effects (CPE) as a primary indicator of viral presence amid changes in fetal bovine serum (FBS) concentration—as a methods question that needs controlled evidence. These methods are widely used in infectious-disease research; medium composition is a plausible confounder of CPE interpretation.
Standard guidelines in virology recommend reducing FBS concentration in cell culture media from approximately 10% during cell growth to 2% during virus propagation phases. These same guidelines position the observance of CPE in inoculated cell cultures as the primary indication of viral presence.

Guidelines recommending reduction of FBS concentration simultaneously with innoculation:
ATCC Virology Culture Guide [11]:
	- “Viral growth medium is usually supplemented with a lower percentage of serum than cell growth medium, often ranging between 2-10% depending on the virus”
	- “NOTE 5: For viral inoculation, ATCC recommends decreasing the percentage of serum to 2% as it can interfere with viral attachment. This can vary from strain to strain, and is not applicable for influenza viruses.”
CLSI M41a [10]:
	- section “5.3.1.2 Cell Density”: “Once the cultures have reached the required density, maintenance medium containing 2% fetal bovine serum (FBS) can be used in place of growth medium, which usually contains 10% FBS. Medium with the lower concentration of FBS will maintain cell viability and will slow monolayer overgrowth.”
	- section “5.3.2 Maintenance”: “Refeed monolayers that are at 75% or greater confluence with fresh maintenance medium containing a low concentration of FBS (e.g., 2%) when the medium color indicates that the pH is below 7.0 (yellow-orange to yellow).”
	- section “5.4.1 Medium Composition”: “Typically 10% FBS is used for growth medium intended for the propagation of cell culture monolayers, while a concentration of 1 to 3% is utilized to maintain subconfluent to confluent monolayers both before and after inoculation.”
	- section “7.1.2 Preinoculation Assessment of Monolayers”: “Inspect cell culture microscopically and macroscopically as described in Section 5.3.1 just prior to specimen inoculation. In summary: the cell culture medium must not be cloudy or turbid; cells should be adherent and healthy in appearance; and the monolayer should be 75 to 90% confluent, but not overgrown.”
ASM - Cytopathic Effects of Viruses Protocols
	- page 9 "Carefully remove growth medium from cells taking care not to touch the dish to any surfaces to avoid contamination; try to avoid leaving residual medium around edges of wells. Add 1 ml of maintenance medium (fresh medium with 2% serum) to each well."
NEADL-30(LP-01)-F/1
	- section "2.3 Reagents": "Growth media (DMEM with 10% FBS and 1% antibiotics).
								Maintenance media (DMEM with 2% FBS and 1% antibiotics)"
WOAH Terrestrial Manual 2021. Chapter 3.5.2
	- section "1.2 Isolation in cell cultre": 
		g) Retrieve the plate and add 700 µl of virus culture medium (DMEM [Dulbecco’s modified Eagle’s medium] with 1% Pen/Strep, 1% sodium pyruvate and 2% fetal calf serum) into each well. Treated cells are then cultured in a CO2 incubator for 24 hours.
		h) Inoculum is removed after the incubation and 1 ml of fresh virus culture medium is added into each well. Treated cells are then cultured for another 3–5 days.

Others:
	- Source note (protocol listing):
		- VI27,~2020-2021,PPRV (peste des petits ruminants virus),Vero dog-SLAM (Vero/hSLAM derivatives),DMEM,10,2,100,0.1,0 (1% of 10000 IU/ml pen + 10 mg/ml strep stock) (protocol; similar in multiple PPRV papers)

Guidelines stating CPE is the primary detection method for viral presence:
	- ATCC Virology Culture Guide: section “Viral authentication and viability testing”
	- CLSI M41a: section “7.4.2 Viral Effects”
	- ASM  Cytopathic Effects of Viruses Protocols: literally the title of the doc.

Given the above, it is reasonable to state that in cell culture experiments where a virus is being “isolated,” there are two independent variables being manipulated and one dependent variable being observed:
	- Independent variables:
		- Virus added or not
		- FBS concentration
	- Dependent variable:
		- CPE in cell culture

Literature on virus isolation aligns with these guidelines [1-8], often employing reduced FBS during propagation and relying on CPE for detection. For example [1,3,4]:
	- In Ge et al. (2013), Vero E6 cells were maintained in DMEM with 10% FCS, but virus propagation used DMEM with 2% FCS. CPE was observed daily to detect viral presence.
	- In Zhou et al. (2020), Vero E6 cells were cultured in DMEM with 10% FBS, with clear CPE observed after three days of incubation as a key indicator of viral infection.
	- In Zhao et al. (2019), methods involved virus isolation in cell cultures with CPE as a general indicator, consistent with standard practices.

FBS concentration could act as a confounder in inducing CPE in cell cultures, potentially making CPE non-specific to the presence of virus particles. Controlled comparisons are needed before treating CPE under dual-media Isolation conditions as virus-specific.



The control experiment offers preliminary evidence: Reduced FBS alone induced CPE-like changes without virus, aligning with literature but exposing a media control gap. Public data enables re-analysis for quantification.

If CPE under dual-media Isolation conditions is not virus-specific, Isolation-dependent culture endpoints inherit that limitation. This draft restricts itself to the culture confound and related practice evidence; see also `tex/FRAMING_LIMITATIONS_ANONYMITY.md`.

## rationale provied for deviating from the standat 10% FBS

### ATCC
section: GROWTH MEDIA FOR TISSUE CULTURE-ADAPTED VIRUSES
subsection: MEDIA SUPPLEMENTS
subsubsection: SERUM
Note 5: FBS "can interfere with viral attachment."

### CLSI
section "5.3.1.2 Cell Density"
"Medium with the lower concentration of FBS will maintain cell viability and will slow monolayer overgrowth"
section “5.4.1 Medium Composition”
"Serum may also contain specific and nonspecific viral inhibitors and their presence may vary by lot.
"The lower serum concentration supports cell viability while permitting virus replication."

### ASM
no rationale.

### NEADL
no rationale.

### WOAH Terrestrial Manual 2021. Chapter 3.5.2
no rationale.

### USDA APHIS VIRPRO
no rationale.



## R1 Isolation practice corpus

*Empirical description of dual-serum Isolation practice and institutional recipes. This section describes how Isolation is commonly done; claims are limited to what the cited corpus documents about growth/maintenance serum practice.*

### Methods (corpus construction)

We assembled two related reference sets for capital-I **Isolation** (culture → cytopathic readout → passage / Isolate as an operational product):

1. **Practice papers (dual-FBS corpus).** Peer-reviewed Isolation or primary diagnostic isolation Methods that state **both** a numeric pre-inoculation (growth) serum percentage and a numeric post-inoculation (maintenance / virus culture) serum percentage (including explicit 0%). Rows were coded only when both values were explicit in the source; percentages were not invented from context alone. Any dual numeric pair was retained with **equal weight**—including the common 10%→2% pattern and less common equal-holds, increases, or near-serum-free maintenance—without preferential sampling or apology for modal recipes. Sources include open-access full texts and extracted Methods quotes; the working table is `r1_isolation_standards_and_practice/expansion/isolation-refs-dual-fbs_only.csv` (**n = 170** file rows).

2. **Institutional guidelines / SOPs (overlay).** Separate from the practice-paper corpus, we recorded published institutional recipes that prescribe growth versus maintenance serum for diagnostic Isolation (e.g., ATCC Virology Culture Guide, CLSI M41-A, ASM CPE protocols, NEADL/CIRAD PPRV SOP, WOAH Terrestrial Manual chapter material, WHO EPI, CDC measles lab tools, Health Canada / CCDR B95-a measles support). Plot overlays use **n = 8** guidelines with parseable dual percentages.

**Exclusions from plots.** USDA APHIS VIRPRO1013 (9 CFR §§ 113.55/113.46) is retained in the institutional reference table for completeness but **excluded from distribution plots**: it addresses master-seed / extraneous-agent safety testing rather than diagnostic Isolation practice.

Distribution figures were regenerated with `expansion/plot_fbs_distributions.py` into `expansion/fbs_distribution_plots/`. The plotter successfully parsed **n = 169** practice rows (one file row lacked a soft-numeric parse, as in prior passes).

### Results (descriptive)

In the plotted dual-FBS practice set (**n = 169**):

| | Pre-inoculation FBS (%) | Post-inoculation FBS (%) |
|--|--:|--:|
| Mean | 9.30 | 2.24 |
| Median | 10.00 | 2.00 |

Institutional overlay (**n = 8**, VIRPRO excluded) clusters near the same operational split (typically ~10% growth → ~2% maintenance; one measles support recipe coded at mid-range growth ~7.5% → 2%).

**Pattern mix (descriptive only).** Pre-inoculation values are dominated by 10% (139/169), with smaller counts at 5%, 8%, 7.5%, 15%, and occasional low or zero serum. Post-inoculation values are dominated by 2% (113/169), with a long tail including 0%, 1%, 5%, 10%, and other maintenance levels. The corpus therefore shows a **modal** growth→maintenance step-down consistent with institutional recipes, together with a minority of other dual combinations. These frequencies describe practice as sampled; they are not evidence that any single recipe is uniquely correct, and they are not a cherry-picked contrast set.

**Figure.** Overlapping pre/post distributions with institutional spines and delta emphasis:  
`r1_isolation_standards_and_practice/expansion/fbs_distribution_plots/styleF_overlap_plus_delta_institution.png`  
(Summary: `.../fbs_distribution_summary.txt`.)

**Scope.** This corpus is a **representative practice description** of dual-serum Isolation Methods wording. It does not by itself establish CPE virus-specificity, and it does not substitute for controlled experiments that vary serum without inoculum. Claims about control quality and medium confounds are scored separately.

**Bridge to R2.** Negative-control and media-control reporting in Isolation papers is evaluated in the R2 stream (`r2_negative_controls/`) on an independent tier scheme; dual-FBS coding here does not imply that matched uninfected low-serum controls were present or adequate.

## methods

### experiment
To explore this hypothesis, a control experiment was commissioned through a certified U.S.-based CRO using Vero E6 cells (ATCC-CRL-1586), with no virus added. Two identical paths differed only in FBS: Path A at 10%, Path B at 2%. After preparation (thawing and passaging) and experimental stages (daily imaging), greater CPE-like changes appeared in Path B, shown in over 50 light microscope images (EVOS FL at 10x/20x) and 170 TEM images (Tecnai G2 Spirit BioTWIN). Raw data is on Zenodo [9] for analysis and replication.

### Identification of standard CPE descriptors
\subsection{Standard CPE descriptors}
Characteristic CPE descriptors were extracted from Table 7 of the CLSI M41 Guideline \cite{clsi} through an iterative review process. First, the full table was examined to identify a set of ten descriptors: rounded, ballooned/enlarged, syncytia, vacuolation, detachment, granularity, refractile, cytoplasmic strands, nonspecific degeneration, and no CPE. An incidence table was then constructed by identifying every instance of these terms (or close semantic correlates) in text entries of the ``Appearance'' column, see Table 1 below.

\input{clsi-table7-descriptors.tex}

Next, the same mapping procedure was applied to the CRO image descriptions to generate a second incidence table (CLSI descriptor set + image descriptions). Only five of the original ten CLSI descriptors appeared in the CRO descriptions. A sixth term, ``Dying Cells'', emerged directly from the CRO text and was retained as a distinct category (Dy) rather than being forced into the CLSI ``nonspecific degeneration'' bin. The resulting \textit{CPE descriptor set} used for ground truth and all subsequent analyses therefore consisted of: Dying cells (Dy), Rounded (Ro), Vacuolation (V), Detached (D), Granularity (G), and Refractile (Re).

### Indentification of Healthy cell culture descriptors
The CRO descriptions were also reviewed for healthy cell culture descriptors. 
looked for repeated terms 
AI verified.

### attempt to label all 101 images of the EXP stages
An attemnpt was made to identify a suitable automated method for detecting CPE in the entire 101 EXP stage image set. The 22 images with descriptions, some indicating CPE were used as the labeled evaluation images set or tsting various AI models on the task of identifying CPE. Unfortunately none of the tools exhibited adequate accuracy to give confidence in their ability to accurately detect CPE in the remaining 82 images of the EXP stage. The consequence of this is that this study relies on the 22 images with CRO descriptions to assess any correlation between FBS % and CPE presence.

## results


## discussion
-using CLSI, ATCC, and/or ASM CPE refs, and the CRO incidence table, which viruses could have been asserted present in the uninoculated cultures?
-why were inclusions/inclusion bodies or syncytia not mentioned? these typilcally require fixation and staining
	- **Fenner F**, et al. Cultivation and Assay of Viruses. In: *Medical Virology*. 2014. PMC7173454.
	- find more refs supporting this.



# references
1. Ge XY, Li JL, Yang XL, Chmura AA, Zhu G, Epstein JH, Mazet JK, Hu B, Zhang W, Peng
C, Zhang YJ, Luo CM, Tan B, Wang N, Zhu Y, Crameri G, Zhang SY, Wang LF, Daszak
P, Shi ZL. Isolation and characterization of a bat SARS-like coronavirus that uses the
ACE2 receptor. Nature. 2013 Nov 28;503(7477):535-8. doi: 10.1038/nature12711. PMID:
24172901; PMCID: PMC5389864.
2. Kitamura T, Morita C, Komatsu T, Sugiyama K, Arikawa J, Shiga S, Takeda H, Akao Y,
Imaizumi K, Oya A, Hashimoto N, Urasawa S. Isolation of virus causing hemorrhagic
fever with renal syndrome (HFRS) through a cell culture system. Jpn J Med Sci Biol.
1983 Feb;36(1):17-25. doi: 10.7883/yoken1952.36.17. PMID: 6134854.
3. Zhou P, Yang XL, Wang XG, Hu B, Zhang L, Zhang W, Si HR, Zhu Y, Li B, Huang CL,
Chen HD, Chen J, Luo Y, Guo H, Jiang RD, Liu MQ, Chen Y, Shen XR, Wang X, Zheng
XS, Zhao K, Chen QJ, Deng F, Liu LL, Yan B, Zhan FX, Wang YY, Xiao GF, Shi ZL. A
pneumonia outbreak associated with a new coronavirus of probable bat origin. Nature.
2020 Mar;579(7798):270-3. doi: 10.1038/s41586-020-2012-7. PMID: 32015507; PMCID:
PMC7095418.
4. Zhao T, Ye Z, Wang B, Cui Y, Nie Y, Yang B, Chen K, Zhang H, Hu F, Yu F. Virus
isolation and genotype identification of human respiratory syncytial virus in Guizhou
Province, China. Braz J Infect Dis. 2019 Nov-Dec;23(6):427-34. doi:
10.1016/j.bjid.2019.10.007.
5. Kar M, Nisheetha A, Kumar A, Jagtap S, Shinde J, Singla M, M S, Pandit A, Chandele A,
Kabra SK, Krishna S, Roy R, Lodha R, Pattabiraman C, Medigeshi GR. Isolation and
molecular characterization of dengue virus clinical isolates from pediatric patients in New
Delhi. Int J Infect Dis. 2019 Jul;84S:S25-33. doi: 10.1016/j.ijid.2018.12.003. PMID:
30528666; PMCID: PMC6823047.
6. Athmanathan S, Reddy SB, Nutheti R, Rao GN. Comparison of an immortalized human
corneal epithelial cell line with Vero cells in the isolation of Herpes simplex virus-1 for the
laboratory diagnosis of Herpes simplex keratitis. BMC Ophthalmol. 2002 Apr 30;2:3. doi:
10.1186/1471-2415-2-3. PMID: 11983023; PMCID: PMC113264.
7. Hu W, Zhang H, Han Q, Li L, Chen Y, Xia N, Chen Z, Shu Y, Xu K, Sun B. A
Vero-cell-adapted vaccine donor strain of influenza A virus generated by serial
passages. Vaccine. 2015 Jan 3;33(2):374-81. doi: 10.1016/j.vaccine.2014.11.007. PMID:
25448099.
8. Li S, Wang D, Ghulam A, Li X, Li M, Li Q, Ma Y, Wang L, Wu H, Cui Z, Zhang XE.
Tracking the replication-competent Zika virus with tetracysteine-tagged capsid protein in
living cells. J Virol. 2022 Apr 13;96(7):e0184621. doi: 10.1128/jvi.01846-21. PMID:
35285687; PMCID: PMC9006885.
9. Mathews A. Vero cell culture image dataset [dataset on the Internet]. Zenodo; c2025
[cited 2025 Dec 14]. Available from: https://doi.org/10.5281/zenodo.17928456
10. Clinical and Laboratory Standards Institute. (2006). Viral culture; Approved guideline
(CLSI Document M41-A).
https://clsi.org/standards/products/microbiology/documents/m41/
11. American Type Culture Collection [Internet]. Manassas (VA): The Collection; c2025 [cited
2025 Dec 14]. Virology Culture Guide. Available from:
https://www.atcc.org/resources/culture-guides/virology-culture-guide

