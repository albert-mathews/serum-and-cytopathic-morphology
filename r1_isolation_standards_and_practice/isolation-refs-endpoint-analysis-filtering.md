# Description
These notes capture the re-review of the isolation-refs-overview.csv sources.
The goal here is to filter them based on "use of CPE as an end point in culture analsyis".
The initial review was performed by SuperGrok, using the follwing prompt, and the PDF version of the papers.

For some refs, I read the paper in detail. My comments from that are indicated "Albert:" in the sections below.
Note: I have previously read many of not all of these papers in full. Memory is not always the best, whihc is why I also use Ai to review and filter sources.

This process was also iused to indefiy any instances of control cultures, and the details around that.
See control-cultures-overview.csv for those results.

## Prompt
this is the final list of papers collected that explicitly state a reduction of FBS% in culture medium during cell culture infection.

ATCC Virology Culture Guide
CLSI M41a
ASM - Cytopathic Effects of Viruses Protocols

those are institutional guidelines that define protocols for virus isolation in cell culture. they outline the same protocol: grow cells in high (10%) FBS, decrease FBS to low concentration (2%) and infect cultures, wait and observe cytopathic effect (CPE).

i would like you to carefully review each article in isolation-refs-overview, and identify those which do not employ CPE as part of their infected culture observations.
you will not do them all at once, you will review them 5 to 6 at a time as I will give you pdfs for then 5-6 at a time, so you dont have to find the information from the internet. please start with the 6 attached. when done, i'll upload the next 5, and so on.

this is the specific information I want from you, and I want it formatted this way.
pure text
paper id (e.g. VI27), bulleted list.
-was CPE used as an end point to confirm infection, yes/no
	-quotes form the paper to justify, as many as you can find
-were any control cultures employed, yes/no
	-were the culture conditions of the controls explicitly stated, yes/no
	-if yes, quotes from paper describing the control culture conditions
	-were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes/no
what other endpoints were used in culture analysis, a concise comma separated list


# summary
VI4 excluded because IFA is the end point, not CPE. VI4 will still be used and referenced in the research, just excluded as source when making a speciifc point.



# review
below is the raw Grok output

## VI4

was CPE used as an end point to confirm infection, no
"There was no visible cytopathic effect (CPE) in the antigen-positive cultures."
"There was no visible cytopathic effect (CPE) in the antigen-positive cultures. Whole-culture preparations containing the infectious agent was prepared by one cycle of freezing-thawing in the antigen-positive cultures."

were any control cultures employed, no
N/A (no mention of mock, uninfected, or control cultures in the methods or results sections)

what other endpoints were used in culture analysis, IFA antigen staining, percentage of antigen-positive cells, IFA endpoint titration

Note: after reading, the main problem with this paper is that the methods are losely documented and it difficult to follow what was actually done.
certainly the lack of CPE as an end point makes it not a useful reference in this case. although it does suport the claim thta in practice FBS% is reduced during infection, it is not a high quality reference for tis research. 
excluded. 

## VI14

was CPE used as an end point to confirm infection, yes
"Cells that showed cytopathic effect (CPE) were then confirmed by indirect immunofluorescence assay"
"The cytopathic effect (CPE) of inoculated Hep-2 cells was observed everyday for seven days. CPE negative samples at the seventh day after inoculation were blindly inoculated for two consecutive passages and CPE positive samples recorded"
"HRSV positive isolates showed typical CPE. The infected cells became round and fused together forming giant cells"

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
"CPE positive and uninfected (mock) Hep-2 cells were digested by 0.02 % EDTA"
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, IFA, RT-PCR, HVR2 sequencing

## SPT10

was CPE used as an end point to confirm infection, yes
"When the cytopathic effect (CPE) was progressed through 70 to 80%, the culture supernatants"

were any control cultures employed, no
N/A (no mention of mock or uninfected control cultures in the virus propagation or imaging sections)

what other endpoints were used in culture analysis, virus rescue and propagation by transfection, IFA, RT-PCR, TEM (electron microscopy)

## VI13

was CPE used as an end point to confirm infection, yes
"CPE was not observed in mock infected cells (Figure 1, panel A)"
"We observed CPE 2 days postinoculation and harvested viral lysate on day 3 postinoculation"
"SARS-CoV-2 infection of Vero E6 cells produced CPE with areas of cell clearance"
"observed for cytopathic effects (CPEs) daily"
"Major CPE was not observed until 60 h postinoculation and peaked at 72 h postinoculation"

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
"CPE was not observed in mock infected cells"
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, plaque assays, PFU viral titers, qRT-PCR, genome sequencing

## VI2

was CPE used as an end point to confirm infection, yes
"Virus titre was determined in Vero E6 cells by cytopathic effect (CPE) counts."
"CPE was observed using an inverted microscope 2 days after inoculation."

were any control cultures employed, no
N/A (negative control serum was used only in the separate neutralization assay; no mock/uninfected infection controls described for the primary culture isolation or growth)

what other endpoints were used in culture analysis, virus infectivity assays in different cell lines (including ACE2-expressing cells), neutralization test by CPE suppression, qRT-PCR

## VI8

was CPE used as an end point to confirm infection, yes
"Clear cytopathogenic effects were observed in cells after incubation for three days"
"The cells were incubated at 37 °C and observed daily for cytopathogenic effects."

were any control cultures employed, no
N/A (no mention of mock or uninfected controls in the virus isolation or propagation sections)

what other endpoints were used in culture analysis, qRT-PCR from culture supernatant, virus neutralization by patient sera

## VI15

was CPE used as an end point to confirm infection, no
No mention of cytopathic effect (or CPE) observation anywhere in the virus isolation protocol, blind passages, or growth kinetics sections.
Isolation success was determined solely after three blind passages: “This was repeated three times to achieve passage 3 (P3) isolates. Viral titers in the supernatant was measured by plaque assays on BHK-21 cells”

were any control cultures employed, no
N/A (no mention of mock-infected, uninfected, or negative controls in the isolation or growth kinetics methods)

what other endpoints were used in culture analysis, plaque assay (BHK-21 titers), growth kinetics curves (MOI 0.1, 24/48/72 hpi), RT-PCR serotyping, full-genome sequencing

## VI16

was CPE used as an end point to confirm infection, yes
“routine examination of the cell cultures were done the next day (12–16 h) following the day of specimen inoculation, for any evidence of CPE”
“Cytopathic effect (CPE) (fig. 2) was seen in the tube cultures at 48 h (>50% of the cells were refractile, showed rounding and ballooning)”
“Shell vial culture showed such changes in few cells (< 10%) at 12–16 h post-infection”
“two of the specimens inoculated into the HCE showed CPE during routine examination of cultures at 12 h and 16 h”
“HCE showing CPE. Conventional tube culture”

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
“Scrapings obtained from 10 patients with infectious keratitis of non-viral origin were included as controls”
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, indirect immunofluorescence/immunoperoxidase assay, quantitative infectious foci (IF) counting

## VI18

was CPE used as an end point to confirm infection, no
No mention of cytopathic effect (CPE) observation as an endpoint. Isolation/adaptation relied on plaque size and growth kinetics: “the virus mixture from passage 20 could form significantly larger plaques”; “plaque phenotypes”, “plaque assay”, and immunostaining were used.

were any control cultures employed, no
N/A (no mock-infected or uninfected controls described in Vero passage or recombinant virus experiments)

what other endpoints were used in culture analysis, plaque assay (size and formation), viral growth kinetics (titration on MDCK), hemagglutination inhibition (HI) assay, luciferase reporter assay, strand-specific real-time RT-PCR, immunocytochemistry/confocal microscopy

## VI24

was CPE used as an end point to confirm infection, yes
“the presence of virus was assessed by the appearance of the cytopathic effect and then confirmed by the presence of hemagglutination activity”
CPE was routinely monitored in Vero cell cultures during isolation from clinical specimens and growth experiments.

were any control cultures employed, no
N/A (no explicit mock-infected controls described for the clinical specimen isolation or AmB supplementation experiments)

what other endpoints were used in culture analysis, hemagglutination activity/titer, TCID50 titration, NP staining (immunofluorescence and flow cytometry), plaque assay, electron microscopy (virus entry/fusion)

## VI23

was CPE used as an end point to confirm infection, yes
“We observed the cells daily and harvested when 40%–50% demonstrated cytopathic effect”
CPE observation was the explicit trigger for harvest in the parallel virus culture protocol across all three Vero lines.

were any control cultures employed, no
N/A (methods focus on clinical specimen inoculation; no mock-infected controls are described)

what other endpoints were used in culture analysis, TCID50 titration assay, whole-genome sequencing (ARTIC POLAR), Western blot (viral protein detection)

These five papers continue the pattern: most rely on classic CPE observation (VI16, VI24, VI23) or plaque/growth endpoints (VI15, VI18), with very few explicit mock controls. Ready for the next batch of PDFs whenever you upload them.

## VI29

was CPE used as an end point to confirm infection, no
No mention of cytopathic effect (CPE) observation or monitoring anywhere in the virus inoculation, incubation, or harvest sections.
"the monolayer of the cells was washed with 20 mL phosphate buffered saline (PBS) ... Then, 9 mL of PV suspension was inoculated on to each monolayer and incubated for 1 hour ... After virus adsorption, the cell monolayers were washed with 20 mL PBS by adding Dulbecco's modified Eagle's medium (DMEM) containing 10% FBS" (infection confirmed solely by subsequent NP extraction and purification)

were any control cultures employed, no
N/A (no mention of mock-infected, uninfected, or negative control cultures in the infection or extraction methods)

what other endpoints were used in culture analysis, NP extraction and purification (CsCl ultracentrifugation), SDS-PAGE (50 kDa band confirmation), Western blot (anti-NP conjugate), protein concentration measurement (spectrophotometer at 280 nm)

## VI32

was CPE used as an end point to confirm infection, yes
"If the CRFK cells in the second passage did not show any cytopathic effects (CPE) after 7 days, the samples were considered negative for virus isolation"
"CRFK cells in the second passage did not show any cytopathic effects (CPE)"
"specific CPE, including cell rounding and syncytia formation"

were any control cultures employed, no
N/A (no mock-infected or uninfected controls described in the isolation protocol or growth kinetics)

what other endpoints were used in culture analysis, indirect immunofluorescence assay (IFA), electron microscopy (EM), PCR (TK and gB genes), growth kinetics/TCID50 titration, hemagglutination (HA) assay

## VI28

was CPE used as an end point to confirm infection, yes
"Cells were observed daily under a microscope. The virus isolation assay was considered positive when CPEs were observed"
"Virus isolation was considered negative when no CPEs were observed by 6 days post-inoculation"
"CPEs were observed" (used as the explicit trigger for harvest and confirmation across all Vero lines)

were any control cultures employed, no
N/A (methods describe only clinical specimen inoculation; no mock-infected or uninfected controls are mentioned)

what other endpoints were used in culture analysis, qRT-PCR from culture supernatant (N2 set confirmation), TCID50 titration, whole-genome sequencing (ARTIC POLAR)

## VI30

was CPE used as an end point to confirm infection, yes
"monitoring of cytopathic effects (CPE) during IAV growth on MDCK cells"
"After 5–7 days of incubation at 35 °C, the supernatant was harvested based on the monitoring of cytopathic effects (CPE)"
"MDCK cells were observed for 5 days post-inoculation for typical CPE"

were any control cultures employed, no
N/A (no mock-infected or uninfected controls described in the MDCK or embryonated egg isolation protocol)

what other endpoints were used in culture analysis, plaque assay (PFU/mL titer), hemagglutination assay, immunofluorescence assay (IFA for HA protein), qRT-PCR (Cq values and RNA concentration), electron microscopy (TEM for morphology), whole-genome sequencing (Illumina + Sanger)

## VI25

was CPE used as an end point to confirm infection, no
No mention of cytopathic effect (CPE) as an endpoint for isolation success in any cell type (Vero E6, Huh-7, MDM) or in suckling mice. Isolation success determined by TCID50 titration or plaque assay after 10–14 days incubation.
"Following 10 days of incubation, cell culture supernatant was collected and titered by plaque assay"

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
"matrix diluent was added to two control rows of each plate" (for TCID50); "The process was repeated with virus diluted in single donor semen, breast milk, or cell culture media" (matrix controls)
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, plaque assay, TCID50 titration, qRT-PCR (RNA genome equivalents), immunostaining (p2 confirmation of isolation), matrix toxicity assessment (cell monolayer imaging)


## VI39

was CPE used as an end point to confirm infection, yes
"Cytopathic effects (CPE), characterized by cell detachment, were observed 4 days after blind passage in cells inoculated with two swab samples"
"CPE was observed in Vero-RcACE2 cells inoculated with OITV 321/2022"

were any control cultures employed, no
N/A (no mention of mock-infected controls in the bat swab isolation or growth kinetics sections)

what other endpoints were used in culture analysis, TCID50 titration (Vero-RcACE2), real-time RT-PCR (viral replication confirmation), growth kinetics curves in multiple cell lines (including bat-, primate-, human-, rodent-, and arthropod-derived), electron microscopy (virus particles), phylogenetic analysis (full-genome sequencing)

## VI33

was CPE used as an end point to confirm infection, yes
"the infected cells were monitored daily for 7 days to check for cytopathic effects (CPE) using an inverted microscope"
"When 70–90% CPE was observed, the supernatant and cells were harvested"

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
"A control well inoculated with sterile phosphate-buffered saline (PBS) was included on each plate"
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, RT-qPCR (upE and ORF1a confirmation of isolation), whole genome sequencing (NGS + long read), phylogenetic and recombination analysis

## VI34

was CPE used as an end point to confirm infection, yes
"CPEs resembling a bunch of grapes were observed"
"MDCK cells inoculated with the isolate after passage 5 showed clear and similar CPEs"

were any control cultures employed, no
N/A (no mock-infected or uninfected controls described in the isolation or characterization methods)

what other endpoints were used in culture analysis, immunofluorescence assay (IFA with monoclonal antibodies against CAV-1/CAV-2), electron microscopy, PCR (E3 gene for differentiation + diagnosis), hemagglutination assay, growth kinetics/TCID50 titration, cross-virus neutralization test, next-generation sequencing + phylogenetic analysis

## VI36

was CPE used as an end point to confirm infection, no
The study focuses on experimental vertical transmission/breastfeeding in mice; Vero cells are used only for virus stock propagation and titration via plaque assay or fluorescence (rCHIKV-mCherry). No explicit CPE monitoring is described as the primary endpoint for isolation or infection confirmation in the provided text.

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
Mock-infected Vero cells and UV-inactivated CHIKV controls used in multiple in vitro infection experiments
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, plaque assay titration, RT-qPCR (viral genome quantification and load), plaque reduction neutralization test (PRNT), Western blot (CHIKV antigens in milk/breast tissue), immunofluorescence (fluorescent rCHIKV-mCherry detection), immunohistochemistry

## VI38

was CPE used as an end point to confirm infection, yes
"SARS-CoV-2-specific CPE was monitored daily"
"The virus-infected cells were then maintained in the presence or absence of trypsin" and CPE photographed/observed in all experiments

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
"Mock infected" cells used in all experiments (Figs 1, 2)
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, TCID50 titration, immunostaining (anti-N MAb + fluorescence microscopy), cell viability (MTT assay)


## VI41

was CPE used as an end point to confirm infection, no
Plaque morphology (small-plaque variant) and growth kinetics were characterized in Vero cells; CPE is not explicitly used as the primary endpoint for isolation confirmation

were any control cultures employed, no
N/A (no mock-infected controls described in the Vero cell isolation or growth kinetics sections)

what other endpoints were used in culture analysis, plaque assay (plaque size measurement and morphology), growth kinetics/TCID50 titration (in Vero, DF-1, PDE, and C6/36 cells at multiple temperatures), intrathoracic and peroral infection of Culex pipiens mosquitoes (infection, dissemination, and transmission rates), full-genome sequencing (identification of prM P54S and NS2A V61A substitutions)

## VI43

was CPE used as an end point to confirm infection, no
The study focuses on persistent infection and apoptosis in Vero E6 cells; cell viability and survival of persistently infected cells (post-apoptotic events) were assessed, but CPE is not used as an isolation endpoint

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
Mock-infected Vero E6 cells were used as controls in all Western blotting, inhibitor, and N-protein expression experiments
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, Western blotting (phosphorylation status of signaling pathways: Akt, JNK, p38 MAPK, Bcl-2, Bcl-xL), cell viability/proliferation assays (WST-1 and naphthol blue-black staining after inhibitor treatment), immunofluorescence (N-protein expression via vaccinia DIs-N vector), inhibitor studies (JNK inhibitor SP600125 and PI3K/Akt inhibitor LY294002)

## VI42

was CPE used as an end point to confirm infection, no
The study examines intracellular localization of ORF29p during VZV infection in multiple cell types; CPE is not mentioned as an endpoint for isolation or infection confirmation

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
Mock-infected cells and empty adenovirus vector (Ad.MmCMV) controls were used in all immunofluorescence experiments
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, immunofluorescence microscopy (localization of ORF29p, ORF62p, gE, and actin cytoskeleton rearrangements), pulse-chase metabolic labeling and immunoprecipitation (protein stability), Western blotting (protein expression levels), Northern blotting (ORF29 transcript analysis), adenovirus vector expression (AdORF29, AdORF61, MLP-0)

## VI40

was CPE used as an end point to confirm infection, no
Viral replication was quantified by qRT-PCR (intracellular/extracellular RNA) and plaque assay; CPE is not mentioned as an endpoint

were any control cultures employed, yes
were the culture conditions of the controls explicitly stated, yes
Mock-infected HEp-2 and A549 cells were included in all RNAseq, immunofluorescence, and cytokine experiments
were the control culture conditions identical to the test cultures conditions, with exception of addition of virus source? yes

what other endpoints were used in culture analysis, qRT-PCR (RSV N gene RNA quantification), high-throughput short-read mRNA sequencing (host and viral gene expression, transcriptional readthrough), epifluorescence deconvolution microscopy (RSV M2-1 protein, actin cytoskeleton, and nuclear morphology), multiplex cytokine/growth factor assays (secreted proteins)