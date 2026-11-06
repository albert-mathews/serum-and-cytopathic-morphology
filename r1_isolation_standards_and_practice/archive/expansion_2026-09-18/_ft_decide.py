# -*- coding: utf-8 -*-
import json, urllib.request, re, time, ssl, html, sys, csv
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
dedup = set(json.load(open(exp/"_dedup_keys_repr.json", encoding="utf-8"))["keys"])
scored = json.load(open(exp/"_ft_scored.json", encoding="utf-8"))

def is_dup(pmid=None, doi=None, pmc=None):
    checks=[]
    if pmid: checks.append(f"link|pmid:{pmid}")
    if pmc:
        p=str(pmc).lower().replace("pmc","")
        checks.append(f"link|pmc:{p}")
    if doi:
        d=doi.lower().rstrip("./")
        checks.append(f"doi|{d}"); checks.append(f"link|doi:{d}")
    return any(c in dedup for c in checks)

def fetch_ft(pmcid):
    pmcid=str(pmcid).replace("PMC","")
    url=f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmcid}/fullTextXML"
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=45) as r:
            return r.read().decode("utf-8","replace")
    except Exception:
        return None

def strip(xml):
    t=re.sub(r"<[^>]+>"," ", xml)
    t=html.unescape(t)
    return re.sub(r"\s+"," ", t)

# Manual inclusion criteria (equal-weight any dual pattern):
# INCLUDE: primary/field/clinical isolation OR diagnostic culture isolation from specimen/homogenate/swab
#          OR routine lab isolation SOP for clinical specimens
#          OR vaccine/cell adaptation when inoculating field/clinical isolate with explicit growth+maint %
# EXCLUDE: pure antiviral IC50 on lab stocks; cell biology; plant natural products; gene editing without isolation protocol
# Soft-include: stock propagation with explicit GM/MM if virus was outbreak/clinical lineage AND methods state isolation/culture protocol clearly

# Review keepers + high borderline individually with methods excerpts
review_ids = [r["pmcid"] for r in scored["keepers"]] + [r["pmcid"] for r in scored["borderline"] if r["score"]>=2]
# unique preserve order
seen=set(); ids=[]
for x in review_ids:
    if x not in seen:
        seen.add(x); ids.append(x)

decisions=[]
for pmc in ids:
    xml=fetch_ft(pmc)
    time.sleep(0.12)
    if not xml: continue
    text=strip(xml)
    # find methods-ish FBS blocks
    blocks=[]
    for m in re.finditer(r".{0,100}(?:growth medium|maintenance medium|FBS reduced|fetal (?:bovine|calf) serum|foetal bovine|FCS).{0,200}", text, re.I):
        blocks.append(m.group(0)[:300])
        if len(blocks)>=8: break
    isol=[]
    for m in re.finditer(r".{0,60}(?:virus isolation|isolated from|inoculat(?:ed|ion).{0,80}(?:specimen|sample|homogenate|swab|filtrate|tissue)|clinical specimen).{0,250}", text, re.I):
        isol.append(m.group(0)[:320])
        if len(isol)>=4: break
    meta=next((r for r in scored["all"] if r["pmcid"]==pmc), {})
    title=(meta.get("title") or "")
    # heuristic decision
    include=False; reason=""
    tl=title.lower()
    hard_excl = any(x in tl for x in [
        "antiviral effect","inhibitor","repurposing","impedimetric","silencing herpes",
        "monoclonal antibod","structure-based discovery","from nicotine","papain-like",
        "combination therapy of oncolytic","gene editing of pigs","wolbachia","adipocyte",
        "endothelial","aav vector","polystyrene","limonoids","microRNA activity",
        "removal of transmissible","many but not all pathogen","targeted disruption of pi",
        "hiv-1 replication in hiv-infected","integrins modulate","comparison of α-glucosyl",
        "apoptosis induced by a cytopathic hepatitis a",
        "accumulation of mutations in nsp4",  # serial passaging lab evolution focus
        "preparation of monoclonal",
        "in vitro screening of thai",
        "in vitro antiviral effects of green",
        "an anti-hiv drug is highly",
        "the oral nucleoside",
        "waste management and disease",  # no positives isolation
        "prevalence, clinical signs, diagnosis and treatment of pos", # may be soft
    ])
    # stronger include signals
    hard_incl = bool(re.search(r"(?:virus isolation|isolated from (?:the |a )?(?:brain|gonad|tissue|swab|clinical|field|patient|diseased|intestinal|liver|bat|mosquito|pork|p[aâ]té|specimen))", text[:8000]+title, re.I))
    has_specimen_inoc = bool(re.search(r"inoculat(?:ed|ion).{0,100}(?:specimen|sample|homogenate|swab|filtrate|tissue)", text, re.I))
    is_adaptation = bool(re.search(r"adapt(?:ed|ation).{0,40}(?:vero|cell)|vero cell.?adapted", tl+text[:2000], re.I))
    is_field = bool(re.search(r"field (?:isolate|sample|outbreak)|outbreak|diseased|clinical sample|retail pork|bat|mosquito|ornamental fish|piglets", tl+text[:3000], re.I))

    if hard_excl and not (hard_incl and has_specimen_inoc and "isolation" in tl):
        include=False; reason="exclude_antiviral_or_offtopic"
    elif hard_incl and (has_specimen_inoc or "isolation" in tl or is_field):
        include=True; reason="field_or_clinical_isolation"
    elif is_adaptation and is_field:
        include=True; reason="adaptation_with_field_context"
    elif meta.get("pre") and meta.get("post") and has_specimen_inoc and is_field:
        include=True; reason="specimen_inoc_field"
    else:
        include=False; reason="insufficient_isolation_practice"

    # Override includes for known good from manual knowledge
    force_in = {
        "PMC13224474": "ranavirus ornamental fish tissue isolation",
        "PMC13556978": "GETV from diseased piglet brain",
        "PMC13184637": "PEDV from intestinal tissues",
        "PMC13431588": "HEV retail pork pate culture attempt",
        "PMC13017990": "betanodavirus gonad diagnosis/isolation context",
        "PMC8493110": "IBDV Vero adaptation 10/2 FCS practice",
        "PMC12474081": "PPRV isolation cell cultures",
        "PMC10913406": "bat MRV isolation",
        "PMC11089916": "DEV field outbreak isolate / CEF line",
        "PMC10907662": "FAdV isolated from livers",
        "PMC5081539": "respiratory viruses clinical diagnostic isolation",
        "PMC12581222": "negevirus mosquito isolation",
        "PMC12411486": "FPV isolated from anal swab",
        "PMC5133602": "Ebola outbreak variants culture 10->2 (stock from outbreak; borderline practice)",
        "PMC11266174": "PRRSV Marc-145 10->2 after inoculation (practice pattern; lab strains)",
        "PMC13517838": "rabies/JEV culture HA antigen - check",
        "PMC12172445": "TMUV - check isolation",
        "PMC13119600": "SARS-CoV-2 isolated from cats",
        "PMC11346336": "IAV tissue homogenate MDCK - atypical 5->10",
        "PMC8983140": "SARS clinical isolate culture 10->2.5?",
        "PMC10044120": "SARS Vero - may be antiviral",
        "PMC4663707": "rabies BHK 10->2 FCS adaptation",
        "PMC7512137": "CyHV-2 FtGF isolation diseased fish",
        "PMC8106717": "PRRSV clinical VI ZMAC/MARC",
    }
    force_out = {
        "PMC12040631","PMC12298480","PMC13185581","PMC13296062","PMC12474224",
        "PMC7118997","PMC3341398","PMC7114468","PMC6264763","PMC7126431",
        "PMC3438744","PMC4157854","PMC4008601","PMC4413797","PMC3749529",
        "PMC4111870","PMC4682342","PMC7127220","PMC13086431","PMC11439533",
        "PMC13018305","PMC12017303","PMC12368721","PMC7804308","PMC4395333",
        "PMC13067622","PMC3073889","PMC13296062",
    }
    if pmc in force_out:
        include=False; reason="force_out_antiviral_or_not_isolation"
    if pmc in force_in:
        include=True; reason="force_in:"+force_in[pmc]

    decisions.append({
        **meta,
        "include": include,
        "decision_reason": reason,
        "blocks": blocks[:5],
        "isol": isol[:3],
    })
    mark = "IN " if include else "OUT"
    print(f"{mark} {meta.get('pre')}->{meta.get('post')} | {meta.get('year')} | {pmc} | {reason[:60]} | {title[:50]}")

ins=[d for d in decisions if d["include"]]
print("\nINCLUDED", len(ins))
from collections import Counter
print("patterns", Counter(f"{d['pre']}->{d['post']}" for d in ins))
with open(exp/"_ft_decisions.json","w",encoding="utf-8") as f:
    json.dump(decisions, f, indent=2, ensure_ascii=False)
