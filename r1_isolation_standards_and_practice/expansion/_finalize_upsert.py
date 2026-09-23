# -*- coding: utf-8 -*-
import csv, re, shutil, datetime
from pathlib import Path
from collections import Counter

exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
root = exp.parent
BATCH = "expansion_2026-09-18_representative"
core_fields = ["ID","year","virus","cells*","Base Medium","FBS% pre-inoculation","FBS% post-inculcation","penicillin (IU/ml)","streptomycin (mg/ml)","amphotericin (mg/ml)","link","access","notes","quote_pre","quote_post","source_batch"]
cand_fields = core_fields + ["dual_ok","upserted","thread","lang"]

# Load existing candidates and fix VI285
with open(exp/"representative_expansion_candidates_2026-09-18.csv", encoding="utf-8", newline="") as f:
    cands = list(csv.DictReader(f))

for r in cands:
    if r["ID"] == "VI285":
        r["FBS% pre-inoculation"] = "10"
        r["FBS% post-inculcation"] = "5"
        r["notes"] = ("Feline primary SARS-CoV-2 isolation. Explicit: 10% FCS for cell culture (growth) and 5% for maintenance medium; primary isolation monitored on DMEM maintenance. Pattern 10->5. | lang=en; thread=SARS feline isolation; pattern=10->5")
        r["quote_pre"] = "Ten percent fetal calf serum (FCS) (Sigma) was added for cell culture"
        r["quote_post"] = "and 5% was added for maintenance medium"
        r["virus"] = "SARS-CoV-2 (feline primary isolation)"

# Additional rows VI292-VI295
extras = [
 {
  "ID":"VI292","year":"2023","virus":"SARS-CoV-2 (clinical isolates; Caco-2/HuH-6 systems)","cells*":"Caco-2; HuH-6; RD; Calu-3",
  "Base Medium":"DMEM / MEM","FBS% pre-inoculation":"10","FBS% post-inculcation":"10",
  "penicillin (IU/ml)":"","streptomycin (mg/ml)":"","amphotericin (mg/ml)":"0.0005",
  "link":"https://doi.org/10.1016/j.isci.2023.106634","access":"oa",
  "notes":"EQUAL-HOLD 10->10. Cell-culture systems paper for isolation of SARS-CoV-2 clinical specimens. Multiple lines maintained ~10% FBS; after 1h specimen incubation DMEM+10% FBS (+gentamicin/amphotericin) added. | lang=en; thread=SARS clinical isolation systems; pattern=10->10",
  "quote_pre":"RD cells ... were maintained in DMEM ... containing 10% FBS ... Calu-3 cells ... containing 10% FBS",
  "quote_post":"Following 1h incubation at 37C ... 1 ml of 1X DMEM supplemented with 10% FBS, 50 ug/ml of Gentamycin, and 0.5 ug/ml of Amphotericin B was added to each well",
  "source_batch":BATCH,"dual_ok":"True","upserted":"True","thread":"SARS clinical isolation systems","lang":"en"
 },
 {
  "ID":"VI293","year":"2024","virus":"Rabies virus (Vero-adapted Flury HEP)",
  "cells*":"Vero","Base Medium":"DMEM","FBS% pre-inoculation":"5","FBS% post-inculcation":"2",
  "penicillin (IU/ml)":"","streptomycin (mg/ml)":"","amphotericin (mg/ml)":"",
  "link":"https://doi.org/10.1038/s41598-024-63337-9","access":"oa",
  "notes":"Vero cell adaptation of rabies Flury HEP. Growth medium DMEM+5% FBS; later passages incubated in maintenance medium DMEM+2% FBS after inoculation. Pattern 5->2. | lang=en; thread=rabies vaccine adaptation; pattern=5->2",
  "quote_pre":"for 1 h at 37 C in growth medium (DMEM supplemented with 5% FBS)",
  "quote_post":"inoculated to 80% confluent Vero cells, and incubated in maintenance medium (DMEM supplemented with 2% FBS)",
  "source_batch":BATCH,"dual_ok":"True","upserted":"True","thread":"rabies Vero adaptation","lang":"en"
 },
 {
  "ID":"VI294","year":"2024","virus":"Orthohantavirus hantanense (patient isolates)",
  "cells*":"Vero-E6","Base Medium":"MEM","FBS% pre-inoculation":"10","FBS% post-inculcation":"2",
  "penicillin (IU/ml)":"","streptomycin (mg/ml)":"","amphotericin (mg/ml)":"",
  "link":"https://doi.org/10.3390/v16081245","access":"oa",
  "notes":"Patient HTNV isolation on Vero-E6 with 28-day passage protocol; 13 isolates recovered. Grown MEM+10% FBS; replaced with maintaining media MEM+2% FBS. NOTE: link may be PMC11376573 DOI - verify. | lang=en; thread=hantavirus clinical isolation; pattern=10->2",
  "quote_pre":"Vero-E6 cells were grown in the minimal essential medium (MEM) ... containing 10% fetal bovine",
  "quote_post":"replaced with 5 mL fresh maintaining media (MEM+2% FBS)",
  "source_batch":BATCH,"dual_ok":"True","upserted":"True","thread":"hantavirus clinical isolation","lang":"en"
 },
]

# Fix VI291/VI294 DOI - get correct from earlier: PMC11376573
# Fetch DOI quickly from prior knowledge - was printed as Isolation and characterization... 
# Use PMC link to be safe if DOI uncertain
extras[2]["link"] = "https://pmc.ncbi.nlm.nih.gov/articles/PMC11376573/"
# Remove duplicate if VI291 already is same paper
# VI291 was Orthohantavirus with same PMC - REMOVE VI294 as dup of VI291, use VI294 for something else

# Instead of VI294 dup, add bocavirus only if dual clear - skip weak
# Add TMUV 10->2 from PMC12172445 as culture of duck TMUV - borderline
# Better: add Health Canada institution + one more practice

# Remove VI294 from extras (dup of VI291); renumber not needed - just don't add VI294
extras = extras[:2]  # VI292, VI293 only

# Also remove old VI291 if it's the same as we'd add - VI291 already in cands with PMC11376573

# Dedup extras against cands links
exist_links=set()
for r in cands:
    exist_links.add((r.get("link") or "").lower())
    exist_links.add(r["ID"])

new_extras=[]
for e in extras:
    if e["ID"] in exist_links or e["link"].lower() in exist_links:
        print("skip dup", e["ID"]); continue
    new_extras.append(e)
    cands.append(e)

# Write candidates
with open(exp/"representative_expansion_candidates_2026-09-18.csv","w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f, fieldnames=cand_fields)
    w.writeheader(); w.writerows(cands)

# Upsert into expanded: replace VI285, add new IDs
exp_csv=exp/"isolation-refs-overview_expanded.csv"
dual_csv=exp/"isolation-refs-dual-fbs_only.csv"
with open(exp_csv,encoding="utf-8-sig",newline="") as f:
    expanded=list(csv.DictReader(f))

by_id={r["ID"]:i for i,r in enumerate(expanded)}
# update VI285
if "VI285" in by_id:
    i=by_id["VI285"]
    src=next(r for r in cands if r["ID"]=="VI285")
    for k in core_fields:
        expanded[i][k]=src.get(k,"")
    print("updated VI285 to", src["FBS% pre-inoculation"], "->", src["FBS% post-inculcation"])

added=0
for e in new_extras:
    if e["ID"] in by_id:
        continue
    expanded.append({k:e.get(k,"") for k in core_fields})
    added+=1
    print("added", e["ID"], e["FBS% pre-inoculation"], "->", e["FBS% post-inculcation"])

with open(exp_csv,"w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f, fieldnames=core_fields)
    w.writeheader(); w.writerows(expanded)

# rebuild dual
dual=[]
for r in expanded:
    a=str(r.get("FBS% pre-inoculation") or "").strip()
    b=str(r.get("FBS% post-inculcation") or "").strip()
    if re.search(r"\d", a) and re.search(r"\d", b):
        dual.append({k:r.get(k,"") for k in core_fields})
with open(dual_csv,"w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f, fieldnames=core_fields)
    w.writeheader(); w.writerows(dual)

print(f"expanded n={len(expanded)} dual n={len(dual)} candidates n={len(cands)} newly added this step={added}")

# Institution: Health Canada measles B95-a
inst=root/"institution-guideline-protocol-refs.csv"
with open(inst,encoding="utf-8-sig",newline="") as f:
    ireader=csv.DictReader(f)
    ifields=ireader.fieldnames
    irows=list(ireader)
if not any("Health Canada" in (r.get("Institution / Guideline") or "") for r in irows):
    irows.append({
        "Institution / Guideline":"Health Canada / CCDR Measles Surveillance Lab Support (B95-a)",
        "Context / Goal":"Diagnostic measles virus isolation (B95-a)",
        "Pre-inoculation FBS (growth)":"5-10%",
        "Post-inoculation FBS (maintenance)":"2%",
        "CPE as primary visual endpoint?":"Yes",
        "Notes":"CCDR guidelines: B95-a growth sustained by adding 5% to 10% FBS; FBS used at 2% for cell maintenance during viral isolation. source_batch=expansion_2026-09-18_representative; URL=https://publications.gc.ca/collections/collection_2015/sc-hc/H12-21-24-5-eng.pdf"
    })
    with open(inst,"w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f, fieldnames=ifields)
        w.writeheader(); w.writerows(irows)
    print("added Health Canada measles institution row")
else:
    print("Health Canada already present")

# Pattern summary for new batch
pat=Counter(f"{r['FBS% pre-inoculation']}->{r['FBS% post-inculcation']}" for r in cands)
print("candidate patterns:", dict(pat))
print("n 10->2", pat.get("10->2",0), "other", sum(v for k,v in pat.items() if k!="10->2"))
