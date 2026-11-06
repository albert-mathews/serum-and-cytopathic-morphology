# -*- coding: utf-8 -*-
import json, urllib.request, urllib.parse, re, time, ssl, html, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
dedup = set(json.load(open(exp/"_dedup_keys_repr.json", encoding="utf-8"))["keys"])

def is_dup(pmid=None, doi=None, pmc=None):
    checks=[]
    if pmid: checks.append(f"link|pmid:{pmid}")
    if pmc: checks.append(f"link|pmc:{str(pmc).lower().replace('pmc','')}")
    if doi:
        d=doi.lower().rstrip("./")
        checks += [f"doi|{d}", f"link|doi:{d}"]
    return any(c in dedup for c in checks)

def epmc(q, n=20):
    url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode({"query":q,"format":"json","pageSize":n,"resultType":"core"})
    with urllib.request.urlopen(url, context=ctx, timeout=60) as r:
        return json.loads(r.read().decode())

def fetch_ft(pmcid):
    pmcid=str(pmcid).replace("PMC","")
    url=f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmcid}/fullTextXML"
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=40) as r:
            return r.read().decode("utf-8","replace")
    except Exception:
        return None

def strip(xml):
    t=re.sub(r"<[^>]+>"," ", xml); t=html.unescape(t); return re.sub(r"\s+"," ", t)

qs=[
 'OPEN_ACCESS:Y HAS_FT:Y PUB_YEAR:[1990 TO 2012] "maintenance medium" "2% FBS" "10% FBS" (HSV OR adenovirus OR enterovirus OR measles OR rubella OR CMV OR "shell vial")',
 'OPEN_ACCESS:Y HAS_FT:Y "rubella" isolation (SIRC OR Vero OR RK) ("10% FBS" OR "10% fetal") ("2% FBS" OR "2% fetal")',
 'OPEN_ACCESS:Y HAS_FT:Y "shell vial" (CMV OR HSV) ("10% FBS" OR "10% fetal") ("2%" OR maintenance)',
 'OPEN_ACCESS:Y HAS_FT:Y "B95" measles isolation FBS',
 'OPEN_ACCESS:Y HAS_FT:Y canine adenovirus OR "CAV-2" isolation "FBS"',
 'OPEN_ACCESS:Y HAS_FT:Y "infectious bronchitis virus" isolation "2% FBS" "10%"',
]
found=[]
for q in qs:
    data=epmc(q, 15)
    print(f"hits {data.get('hitCount')} | {q[40:90]}")
    for h in data.get("resultList",{}).get("result",[]):
        pmc=h.get("pmcid")
        if not pmc or is_dup(pmid=h.get("pmid"), doi=h.get("doi"), pmc=pmc):
            continue
        found.append(h)
    time.sleep(0.3)

print("new pmc candidates", len(found))
# scan first 25 for dual
hits=[]
for h in found[:30]:
    xml=fetch_ft(h["pmcid"])
    time.sleep(0.15)
    if not xml: continue
    text=strip(xml)
    gm=re.search(r"growth medium[^\.]{0,140}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|FCS|fetal)", text, re.I)
    mm=re.search(r"maintenance medium[^\.]{0,140}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|FCS|fetal)", text, re.I)
    g=re.search(r"(?:grown|maintained|propagated|cultured).{0,100}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|fetal bovine)", text, re.I)
    red=re.search(r"(?:FBS|serum)\s+(?:was\s+)?reduced to\s+(\d+(?:\.\d+)?)\s*%", text, re.I)
    m2=re.search(r"(?:after (?:adsorption|inoculation)|infection medium|replaced with).{0,100}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|fetal)", text, re.I)
    pre=post=None; qp=qo=""
    if gm and mm:
        pre,post,qp,qo=gm.group(1),mm.group(1),gm.group(0)[:180],mm.group(0)[:180]
    elif g and red:
        pre,post,qp,qo=g.group(1),red.group(1),g.group(0)[:180],red.group(0)[:180]
    elif g and m2 and g.group(1)!=m2.group(1):
        pre,post,qp,qo=g.group(1),m2.group(1),g.group(0)[:180],m2.group(0)[:180]
    if not pre: continue
    if not re.search(r"isolat|clinical|specimen|patient|inoculat", text, re.I): continue
    title=h.get("title") or ""
    print(f"HIT {pre}->{post} | {h.get('pubYear')} | {h.get('pmcid')} | {title[:70]}")
    print("  ", qp[:120]); print("  ", qo[:120])
    hits.append({"pmid":h.get("pmid"),"doi":h.get("doi"),"pmcid":h.get("pmcid"),"year":h.get("pubYear"),"title":title,"pre":pre,"post":post,"qp":qp,"qo":qo})

with open(exp/"_ft_more_hits.json","w",encoding="utf-8") as f:
    json.dump(hits,f,indent=2,ensure_ascii=False)
print("more hits", len(hits))
