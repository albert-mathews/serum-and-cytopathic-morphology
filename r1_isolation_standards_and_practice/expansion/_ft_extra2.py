# -*- coding: utf-8 -*-
import json, urllib.request, urllib.parse, re, time, ssl, html, sys, csv, shutil
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
dedup = set(json.load(open(exp/"_dedup_keys_repr.json", encoding="utf-8"))["keys"])
# refresh dedup with just-added
with open(exp/"representative_expansion_candidates_2026-09-18.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        link=(r.get("link") or "").lower()
        m=re.search(r"10\.\d{4,9}/[-._;()/:a-z0-9]+", link)
        if m: dedup.add("doi|"+m.group(0).rstrip("./"))
        m=re.search(r"pmc/articles/pmc(\d+)", link)
        if m: dedup.add("link|pmc:"+m.group(1))

def is_dup(pmid=None, doi=None, pmc=None):
    checks=[]
    if pmid: checks.append(f"link|pmid:{pmid}")
    if pmc: checks.append(f"link|pmc:{str(pmc).lower().replace('pmc','')}")
    if doi:
        d=doi.lower().rstrip("./"); checks += [f"doi|{d}", f"link|doi:{d}"]
    return any(c in dedup for c in checks)

def epmc(q,n=25):
    url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode({"query":q,"format":"json","pageSize":n,"resultType":"core"})
    with urllib.request.urlopen(url, context=ctx, timeout=60) as r:
        return json.loads(r.read().decode())

def fetch_ft(pmcid):
    pmcid=str(pmcid).replace("PMC","")
    try:
        with urllib.request.urlopen(f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmcid}/fullTextXML", context=ctx, timeout=40) as r:
            return r.read().decode("utf-8","replace")
    except Exception:
        return None

def strip(xml):
    t=re.sub(r"<[^>]+>"," ", xml); t=html.unescape(t); return re.sub(r"\s+"," ", t)

qs=[
 'OPEN_ACCESS:Y HAS_FT:Y "isolated from" "maintenance medium" "2% FBS" "10% FBS" (Vero OR MDCK OR BHK OR A549 OR RD)',
 'OPEN_ACCESS:Y HAS_FT:Y "clinical specimens" "2% FBS" "10% FBS" virus isolation',
 'OPEN_ACCESS:Y HAS_FT:Y "tissue homogenate" "2% FBS" "10% FBS" (isolation OR inoculated) virus',
 'OPEN_ACCESS:Y HAS_FT:Y "FBS reduced to 2%" virus (isolation OR culture OR Vero)',
 'OPEN_ACCESS:Y HAS_FT:Y PUB_YEAR:[1985 TO 2000] "2% FBS" "10% FBS" virus (isolation OR shell)',
]
cands=[]; seen=set()
for q in qs:
    data=epmc(q,20)
    print("q hits", data.get("hitCount"))
    for h in data.get("resultList",{}).get("result",[]):
        pmc=h.get("pmcid");
        if not pmc or pmc in seen: continue
        if is_dup(pmid=h.get("pmid"), doi=h.get("doi"), pmc=pmc): continue
        seen.add(pmc); cands.append(h)
    time.sleep(0.25)
print("cands", len(cands))

extra=[]
for h in cands[:40]:
    xml=fetch_ft(h["pmcid"]); time.sleep(0.15)
    if not xml: continue
    text=strip(xml)
    title=h.get("title") or ""
    tl=title.lower()
    if any(x in tl for x in ["antiviral","inhibitor","repurposing","cytotoxicity","silencing","monoclonal","gene editing","adipocyte"]):
        continue
    gm=re.search(r"(?:growth medium|grown in|propagated in|maintained in|cultured in).{0,120}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|FCS|fetal bovine|foetal bovine)", text, re.I)
    mm=re.search(r"(?:maintenance medium|infection medium|FBS reduced to|after (?:adsorption|inoculation)|replaced with).{0,120}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|FCS|fetal bovine|foetal bovine)", text, re.I)
    mm0=re.search(r"(?:maintenance medium|after (?:adsorption|inoculation)).{0,140}?(?:without (?:FBS|serum)|serum[- ]free|no FBS)", text, re.I)
    if not gm: continue
    if mm:
        pre,post=gm.group(1),mm.group(1); qp,qo=gm.group(0)[:200],mm.group(0)[:200]
    elif mm0:
        pre,post=gm.group(1),"0"; qp,qo=gm.group(0)[:200],mm0.group(0)[:200]
    else:
        continue
    if not re.search(r"(?:isolat(?:ed|ion) from|clinical (?:specimen|sample)|tissue homogenate|patient|swab|outbreak)", text, re.I):
        continue
    # cells
    cells=re.findall(r"\b(Vero(?:\s*E6)?|MDCK|HEp-?2|A549|RD|BHK-?21|MARC-145|HeLa|C6/36|CRFK|LLC-MK2|MRC-5)\b", text, re.I)
    cell=", ".join([c for c,_ in Counter(cells).most_common(3)]) or ""
    year=h.get("pubYear") or ""
    doi=h.get("doi") or ""
    pmid=h.get("pmid") or ""
    print(f"EXTRA {pre}->{post} | {year} | {h['pmcid']} | {cell} | {title[:55]}")
    extra.append({"pmcid":h["pmcid"],"pmid":pmid,"doi":doi,"year":year,"title":title,"pre":pre,"post":post,"qp":qp,"qo":qo,"cells":cell})

print("extra usable", len(extra))
with open(exp/"_ft_extra2.json","w",encoding="utf-8") as f:
    json.dump(extra,f,indent=2,ensure_ascii=False)
