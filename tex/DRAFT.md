# Draft paper

## Review comments

paper review items:
intro::

1. " citing slower monolayer
   34 overgrowth, maintained viability and reduced interference of serum with viral attachment (verbatim guideline
   35 text is compiled in tex/DRAFT.md, section “introduction” and “rationale”)", this rationale here doesn't really do the findings justice. we want to keep the rationale found in each protocol guide for later when we show that they propose the SAME protocol, but for DIFFERENT rationale. the different rationale is a core finding that points to the fact that the whole institution of virology doesn't actually know why they are reducing the FBS at inoculation. our findings indicate that we know why they are doing it, and it is because it produces the outcome (CPE) that they have associated with virus presence. it is very important that we expose this massive discrepancy in rationale for a protocol which is un-scientific, and unanimously applied.
2. "By Isolation we mean virology’s operational product of culture, cytopathic readout and passage (an Iso42 late), not chemical purity of a particle preparation (r1 isolation standards and practice/r1.md, snippet
   43 R1-S2).", we might get in trouble for that one. i agree it is important to point out, and most important of us to retain mentally when operating this research project, but maybe not say it in THIS paper


Materials and methods::

1. "The working table is r1 isolation standards and practice/expans59 (n = 170 rows; search logs in expansion/)", why do we have this sentence? is it a working note or what?
2. "Eight guidelines with parseable dual percentages form the plotted overlay.", why 'parseable' here?
3. "USDA APHIS VIRPRO1013 is
   64 retained in the table but excluded from plots because it addresses master-seed extraneous-agent testing
   65 rather than diagnostic Isolation. ", sentence doesn't belong here. i think we rope the APHIS content in by saying that we then researched non-isolation cell culture protocols to see if the dual serum was ubiquitous. we found APHIS (and others we may find now that we want to search for them, i just thought of searching this way), so we want to say "we search for isolation protocols, isolation paper, and then we searched for non-isolation protocols to see if dual serum exists outside isolation, and then we searched for papers or other reporting documents that capture what was done following the non-isolation protocols". we need to add item to our TODO to expand the non-isolation protocol research path. this feecback should also clear out the paragraph that follows the sentence.
4. "plus three Isolation papers scored from the earlier
   73 unfiltered overview", that doesn't come across as through research. why say it like that? cant we just say how many isolation papers we looked at for negative controls?
5. " or
   78 full text unavailable.", that is not an acceptable reason to classify a paper. either we get the full text, or we exclude the item from our research
6. " three scoring passes
   80 are logged", no we dont say how many times we iterated. we just say that we researched the topic across some corpus, and cataloged findings as blah blah blah
7. "[TODO-ALBERT] Medium base,
   88 seeding density, feeding schedule and TEM sampling days from the CRO report.", the zenodo record has the protocol details and culture progress details. we do not need to repeat them here. just high level. two cultures, same stock, one 10 and one 2 % FBS for 5 days, then TEM. 
8. " One Culture B day-4
   111 field appears twice in the set: the CRO originals for path 2 frames 407 and 408 are the same file (identical
   112 checksum), so every rater described that field twice", that and its follow on, we dont need to say this here. 
9. "[TODO-ALBERT] Describe the brief119 ing condition only after the IR3v rater has completed Pass 2 and been debriefed (anonymity and debrief
   120 guardrail).", the paper at this point can say the rater was told the path B was inoculated with a virus
10. "IR3v Pass 1 text was scored with the unchanged shared lexicon and, separately, with a clarified
    121 coding that applies the rater’s own answers to five clarification questions", i think if we expand the lexicon to include what we needed from andres clarifications, and re-scroe daniel and abdolreza, daniel and abdolreza's scores wont change, so we can just do that, and then we can say we used the same lexicon for all three. i dont want to expose in methods sections thta we had to deal some some minor language barriers, that is distracting to the reader. 
11. "[ASSUMED – pending FOIA]", we dont need this here. we'll have a seperate results section for non-isolation protocols and the 'practice' reported by following those protocols. essetially we'll have the duals in this paper: isolation protocols and their practice, non-isolation protocols and their practice. we'll have two methods sections, and two results sections, bringing it together in the discussion
12. i want the figures in the pdf. have the python scripts produce the fig pngs, jpegs or whatever meets figure insertion in PLOS bio paper, place those files in the tex\figures\, and then have them appear in the PDF. i want to be reviewing how they look. i think we cannot use color, so we need to iterate how we show the data
13. "Matched-medium negative controls are rarely reported", we want to tabulate the results, or bar/pie chart. we also want to indicate here which teir A controls exhibited CPE, i/e/ the negative control falsified the test culture CPE specificity.
14. "Lowering FBS alone produces CPE-classified morphology in uninoculated Vero
    163 E6 cells", same, lets show this information as illustration. table, plot, graph, infographic. the text is impossible for a human to parse, we'll provide the raw results data if they want to see it. 
15. this repeating of the 100 vs 99 frames needs to stop. we just say when we describe the zenodo record, that there are 50 path A and 49 path B images. and then we say blinded rater process all 99. that's it. 
16. "[TODO-ALBERT] Add κ table summary", thats your job
17. "Historical context (P1)", the paragraph does at all capture the intent of this prediction arm. the prediction is that "when cell culture became the tool for virus isolation, dual medium protocols developed quick afterwards so that the protocol would produce the positive outcome, PCE observed, virus present. and thta is what we found is it not?
18. "Particle-level context (P2)", the paragraph does at all capture the intent of this prediction arm.  the prediction is that if CPE is not specific to viral presence, then many culture CPE experiments that did not have any virus would have inadvertently characterized non-viral particles as viral. parallel work on non-inoculated culture characterizing particles would characterize the same particles, but assign different object class. therefore we should find in the literature a well documented distinguishability problem, in that viral particles are indistinguishable from some class of non-viral particles. and this is exactly what we find
19. "The literature corpora describe reported methods; reporting omissions (R2) cannot distinguish controls
    239 not run from controls not described.", i dont understand this. 
20. the references section should be like 300 items long or more. you mentioned >170 R1 papers, where are the citations?

### Status
Grok bot failed to address all review comments because prompts were getting blocked by safety checks. it's last useful response was:
"""
The isolation vs non-isolation restructure is now in the paper, and `main.pdf` rebuilt cleanly.
- **Methods:** a new "Search structure" paragraph sets out the four parts: isolation protocols, isolation papers, non-isolation protocols, and practice under non-isolation protocols. The old APHIS exclusion sentence is gone. A new R4 subsection describes the non-isolation search and now holds the FOIA request paragraph.
- **Results:** a new "Non-isolation protocols and practice" subsection opens with VIRPRO1013. It prescribes 5–10% serum for growth and 5–20% later, so serum is held or raised rather than lowered. The FOIA assumption block moved here from the isolation results.
- **TODO:**
  - Your R2 item now lists the 10 papers excluded for lacking full text, so you can fetch them and bring them back into the analysis.
  - A new CPE item covers expanding the R4 search.

Still to do:
- the rationale comparison table;
- rewriting the P1 and P2 discussion;
- the expanded lexicon and rescore;
- grayscale figures in the PDF;
- the full bibliography.

Next up is the rationale table.
"""


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

