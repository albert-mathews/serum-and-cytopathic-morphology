the excluded VI44 brings up an important point. papers reflect the fbs 10->2 pattern, but are not clinical virus isolation. you had brought this up previously when we were reclassifying into classes 1,2,3, you had a boarderline group, and i incorrectly pushed back on some of your selections. i think we need a class 4, which is identified by endpoint. 
arg paragraph
'''
the primary argumnent of R1 is that virology has the '2 independent and 1 dependent variable' (2I1D) pattern represented throughout the field, not just in virus isolation. but the first argument is that it has codified this pattern for the core process of detecting the presence of,  and 'isolating' the 'main character particle' i.e. 'the virus' in its institutional protocols globally, AND that practitioners in the field generally follow this 2I1D pattern for the 'detection' and 'isolation' endpoints.
the second argument is that this 2I1D pattern persists through the field, regardless of the end point.
'''
this means that class 1 papers MUST have 'CPE=virus detection and/or isolate' as the primary end point. other endpoint are secondary. 
this means that we need a new class, class 4, which employs the 2I1D pattern, but has other endpoints. this class 4 corpus is actually also important since we dont just want to show that virus identification and isolation depended on the 2I1D pattern, but that the field as a whole does. this is the evidence for the second argument. 

i think we should add columns to the cvs for the various endpoints found in the corpus today. with 'CPE=virus detection and/or isolate' being one such endpoint. excluded-VI44 gives us another example of alternative endpoint. then we should add a column for 'class'=1 or 4 for now. and class column meaning is defined in r1.md.
so please do these task in order:
1] capture the paragraph about the argument structure above in r1.md for use in the paper prose. 
2] codify this research classification in r1.m or where appropriate
3] give exluded-VI44 a new VI ID, and move it to C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\refs\isolation_practice, parse it, and populate a row in isolation-refs.csv for it
4] reparese the entire corpus, as you go, build up the set of alternative endpoint columns needed, and populate the data for each row as you go. also populate the class column


"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\wrk\SPT references - refs.csv"
has similar data for single particle tracking papers. 
pdfs should be here: C:\Users\alber\Documents\virus\bechamp institute\virus Single virus tracking
please parse each of those, see if fbs-pre and fbs-post are reported, and if so, assign a VI ID, and add rows to isolation-refs.csv as class=4 and appropriate endpoint

class 1: VI13, VI94, VI105, VI218, VI233, VI234, VI285, VI 292. many of these are multi-endpoint, but have CPE-detection/isolation as one, or the main endpoint. be sure to capture all end points for each.
VI270 is a masters or doctoral thesis. meither make new class 5 for these, or group in class 3.
class 4: VI273, VI274 (make note in p6.md so thta agent looks at this paper), VI282


VI107: cat=1, class=1.
VI74: cat=1, class=1. multi endpoint
VI254 (mizuta 2019), cat=3 i think, the methods_review_teaching cat
VI270, move to methods_review_teaching folder
anything cateogry 2 or 3, should not be localed in 'C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\refs\isolation_practice', it should be located where it belongs, in either 'C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\refs\isolation_protocols', or 'C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\refs\methods_review_teaching '. please make the mechanical moves so that this is resolved. 

any ref not in \refs\isolation_practice\ shall have its VI ID striped from the file name, and it isolation-refs.csv row moved to a different csv. it is ok to create new ID prefixes to analogous to VI but used in other refs folders. and each folder with some class/cat pdfs, needs to have its own csv files tracking the data from the refs there. 

i want category organized by the folder in which the ref appears, and class organized by columns in csv. the folders make the split between what is a paper reporting whats done in practice, and all other refs, while class is endpoint differentiating among the 'reporting in practice' set. i think this disctinction is clear. please code it in r1.md, and clean out any text there that overlaps, or makes this ambiguous. 