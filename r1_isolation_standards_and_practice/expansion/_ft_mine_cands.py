import json, urllib.request, urllib.parse, re, time, ssl, html
from pathlib import Path
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
dedup = set(json.load(open(exp/"_dedup_keys_repr.json"))["keys"])

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

def epmc_search(q, pageSize=40):
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({
        "query": q, "format": "json", "pageSize": pageSize, "resultType": "core"
    })
    with urllib.request.urlopen(url, context=ctx, timeout=60) as r:
        return json.loads(r.read().decode())

# Equal-weight: any dual numeric pre/post. Pattern-agnostic queries.
queries = [
    'OPEN_ACCESS:Y HAS_FT:Y "maintenance medium" FBS (isolation OR inoculated OR specimen) virus',
    'OPEN_ACCESS:Y HAS_FT:Y "growth medium" "maintenance medium" FBS virus (isolation OR clinical)',
    'OPEN_ACCESS:Y HAS_FT:Y "infection medium" OR "isolation medium" FBS (Vero OR MDCK OR "HEp-2" OR A549 OR RD)',
    'OPEN_ACCESS:Y HAS_FT:Y "shell vial" FBS (cytomegalovirus OR HSV OR adenovirus OR virus)',
    'OPEN_ACCESS:Y HAS_FT:Y (enterovirus OR adenovirus OR measles OR rubella OR HSV OR RSV) isolation FBS (Vero OR RD OR A549)',
    'OPEN_ACCESS:Y HAS_FT:Y (PRRSV OR "canine distemper" OR "infectious bronchitis" OR PPRV) isolation FBS',
    'OPEN_ACCESS:Y HAS_FT:Y (dengue OR "West Nile" OR Zika OR chikungunya) isolation (Vero OR C6/36) FBS',
    'OPEN_ACCESS:Y HAS_FT:Y influenza isolation MDCK FBS (trypsin OR maintenance OR serum)',
    'OPEN_ACCESS:Y HAS_FT:Y (Numazaki OR microplate) isolation virus FBS',
    'OPEN_ACCESS:Y HAS_FT:Y "fetal bovine serum" isolation (specimen OR clinical OR patient) (DMEM OR MEM) virus',
    'OPEN_ACCESS:Y HAS_FT:Y "serum-free" OR "without FBS" OR "0% FBS" virus isolation (MDCK OR Vero OR LLC)',
    'OPEN_ACCESS:Y HAS_FT:Y "5% FBS" maintenance OR infection virus isolation',
]

cands=[]; seen=set()
for q in queries:
    try:
        data=epmc_search(q, 40)
        hits=data.get("resultList",{}).get("result",[])
        print(f"hitCount={data.get('hitCount')} got={len(hits)} | {q[30:85]}")
        for h in hits:
            pmid=h.get("pmid"); pmcid=h.get("pmcid"); doi=h.get("doi")
            key=pmid or pmcid or doi
            if not key or key in seen: continue
            seen.add(key)
            if is_dup(pmid=pmid, doi=doi, pmc=pmcid): continue
            if not pmcid: continue
            cands.append({"pmid":pmid,"doi":doi,"pmcid":pmcid,"title":h.get("title"),"year":h.get("pubYear"),"journal":h.get("journalTitle")})
        time.sleep(0.3)
    except Exception as e:
        print("ERR", e)

print("OA candidates nondup:", len(cands))
with open(exp/"_ft_cands_repr.json","w",encoding="utf-8") as f:
    json.dump(cands, f, indent=2)
print("saved cands")
