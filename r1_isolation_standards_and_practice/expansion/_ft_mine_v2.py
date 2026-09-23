# -*- coding: utf-8 -*-
import json, urllib.request, re, time, ssl, html, sys
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
dedup = set(json.load(open(exp/"_dedup_keys_repr.json", encoding="utf-8"))["keys"])

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
    except Exception as e:
        return None

def fetch_pmc_html(pmcid):
    pmcid=str(pmcid).replace("PMC","")
    url=f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmcid}/"
    try:
        req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
            return r.read().decode("utf-8","replace")
    except Exception:
        return None

def strip(xml):
    t=re.sub(r"<[^>]+>"," ", xml)
    t=html.unescape(t)
    return re.sub(r"\s+"," ", t)

def extract_dual(text):
    pre=post=None; qpre=qpost=""; method=""
    gm=re.search(r"growth medium[^\.]{0,160}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|FCS|fetal (?:bovine|calf)|foetal)", text, re.I)
    mm=re.search(r"maintenance medium[^\.]{0,160}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|FCS|fetal (?:bovine|calf)|foetal)", text, re.I)
    mm0=re.search(r"maintenance medium[^\.]{0,180}?(?:without (?:FBS|serum|FCS)|serum[- ]free|no FBS|0\s*%\s*FBS)", text, re.I)
    if gm and mm:
        return gm.group(1), mm.group(1), gm.group(0)[:240], mm.group(0)[:240], "GM_MM"
    if gm and mm0:
        return gm.group(1), "0", gm.group(0)[:240], mm0.group(0)[:240], "GM_MM0"
    # grown/propagated X% ... virus culture/maintenance FBS reduced to Y / infection medium Y
    g=re.search(r"(?:propagated|grown|cultured|maintained)[^\.]{0,120}?(?:growth media?|medium)?[^\.]{0,80}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|FCS|fetal bovine serum|fetal calf serum)", text, re.I)
    # "FBS reduced to 2%"
    red=re.search(r"(?:FBS|FCS|serum)\s+(?:was\s+)?reduced to\s+(\d+(?:\.\d+)?)\s*%", text, re.I)
    m=re.search(r"(?:(?:maintenance|infection|isolation|inoculation) medium|after (?:adsorption|inoculation)|replaced (?:by|with)|fresh medium supplemented with)[^\.]{0,140}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|FCS|fetal)", text, re.I)
    m0=re.search(r"(?:(?:maintenance|infection|isolation) medium|after (?:adsorption|inoculation)|replaced (?:by|with))[^\.]{0,160}?(?:without (?:FBS|serum)|serum[- ]free|no FBS|0\s*%\s*FBS)", text, re.I)
    if g and red:
        return g.group(1), red.group(1), g.group(0)[:240], red.group(0)[:240], "reduced_to"
    if g and m:
        return g.group(1), m.group(1), g.group(0)[:240], m.group(0)[:240], "grown_maint"
    if g and m0:
        return g.group(1), "0", g.group(0)[:240], m0.group(0)[:240], "grown_SF"
    # DMEM with 10% and 2% sterile FCS as growth and maintenance
    pair=re.search(r"(?:DMEM|MEM|RPMI|medium)[^\.]{0,80}?(\d+(?:\.\d+)?)\s*%\s*(?:and\s+)?(\d+(?:\.\d+)?)\s*%\s*(?:sterile\s+)?(?:FBS|FCS|fetal)[^\.]{0,80}?(?:growth and maintenance|growth.*?maintenance|as a growth and maintenance)", text, re.I)
    if pair:
        return pair.group(1), pair.group(2), pair.group(0)[:240], pair.group(0)[:240], "growth_and_maint_pair"
    pair2=re.search(r"with\s+(\d+(?:\.\d+)?)\s*%\s*and\s+(\d+(?:\.\d+)?)\s*%\s*(?:sterile\s+)?(?:FBS|FCS|fetal[^\.]{0,20}serum)[^\.]{0,60}?(?:growth and maintenance|growth.*?maintenance)", text, re.I)
    if pair2:
        return pair2.group(1), pair2.group(2), pair2.group(0)[:240], pair2.group(0)[:240], "growth_and_maint_pair"
    return None, None, "", "", ""

# Curated PMC list: mix of families/decades; equal-weight any dual pattern
curated = [
    # from prior auto hits (isolation-relevant)
    ("13224474", "ranavirus fish isolation"),
    ("13556978", "GETV piglet isolation"),
    ("13184637", "PRRSV isolation"),
    ("13431588", "HEV pork isolation"),
    ("13578469", "fish pathogen?"),
    ("13086431", "SARS-CoV-2?"),
    ("12040631", "NDV"),
    ("13017990", "betanodavirus"),
    ("12298480", "gD protein? herpes"),
    ("13185581", "VV251 antiviral"),
    ("13296062", "antiviral mussel"),
    ("12474224", "anti-HIV SARS"),
    # web-found
    ("5133602", "Ebola VeroE6 10-2"),
    ("4663707", "rabies BHK 10-2"),
    ("8493110", "IBDV Vero 10-2"),
    ("7512137", "CyHV-2 FtGF"),
    ("11266174", "PRRSV rifampicin 10-2"),
    ("8106717", "PRRSV ZMAC MARC clinical isolation"),
    # additional targeted searches via known PMCs from literature
    ("7086893", "Hierholzer?"),
    ("1895586", "placeholder"),
]

# Also search epmc for older OA papers
def epmc_search(q, pageSize=30):
    url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode({"query":q,"format":"json","pageSize":pageSize,"resultType":"core"})
    with urllib.request.urlopen(url, context=ctx, timeout=60) as r:
        return json.loads(r.read().decode())

extra_qs = [
    'OPEN_ACCESS:Y HAS_FT:Y PUB_YEAR:[1980 TO 2005] "maintenance medium" FBS virus isolation',
    'OPEN_ACCESS:Y HAS_FT:Y PUB_YEAR:[2006 TO 2015] "growth medium" "maintenance medium" FBS (enterovirus OR adenovirus OR measles OR HSV OR RSV)',
    'OPEN_ACCESS:Y HAS_FT:Y "virus was isolated" "maintenance medium" FBS',
    'OPEN_ACCESS:Y HAS_FT:Y "clinical specimens" isolation "maintenance medium" "FBS" (HSV OR CMV OR adenovirus)',
    'OPEN_ACCESS:Y HAS_FT:Y "FBS reduced to" virus (Vero OR MDCK OR BHK)',
    'OPEN_ACCESS:Y HAS_FT:Y "2% FCS" "10% FCS" (growth OR maintenance) virus isolation',
    'OPEN_ACCESS:Y HAS_FT:Y "Omni Serum" herpes isolation',
    'OPEN_ACCESS:Y HAS_FT:Y shell vial "fetal bovine" (CMV OR HSV) isolation',
]
seen=set(p for p,_ in curated)
for q in extra_qs:
    try:
        data=epmc_search(q, 25)
        for h in data.get("resultList",{}).get("result",[]):
            pmc=h.get("pmcid")
            if not pmc: continue
            p=pmc.replace("PMC","")
            if p in seen: continue
            if is_dup(pmid=h.get("pmid"), doi=h.get("doi"), pmc=pmc): continue
            seen.add(p)
            curated.append((p, f"epmc:{h.get('pubYear')}:{(h.get('title') or '')[:40]}"))
        time.sleep(0.3)
        print("extra", q[40:80], "->", data.get("hitCount"))
    except Exception as e:
        print("ERR", e)

print("total curated scan", len(curated))
results=[]
for i,(pmc,note) in enumerate(curated[:110]):
    if is_dup(pmc=pmc):
        continue
    xml=fetch_ft(pmc)
    time.sleep(0.2)
    if not xml:
        continue
    text=strip(xml)
    # must look like isolation/culture practice
    if not re.search(r"\b(isolat|inoculat|clinical|specimen|patient|homogenate|swab|passage)", text, re.I):
        continue
    pre,post,qpre,qpost,method=extract_dual(text)
    if pre is None:
        continue
    # title/year from xml
    title_m=re.search(r"<article-title[^>]*>(.*?)</article-title>", xml, re.I|re.S)
    title=re.sub(r"<[^>]+>","", title_m.group(1)) if title_m else note
    year_m=re.search(r"<pub-date[^\>]*>.*?<year>(\d{4})</year>", xml, re.I|re.S)
    year=year_m.group(1) if year_m else ""
    pmid_m=re.search(r'<article-id pub-id-type="pmid">(\d+)</article-id>', xml)
    doi_m=re.search(r'<article-id pub-id-type="doi">(10\.[^<]+)</article-id>', xml)
    cells=re.findall(r"\b(Vero(?:\s*E6)?|MDCK|HEp-?2|A549|RD(?:-?A)?|LLC-MK2|C6/36|BHK-?21|MARC-145|HeLa|MA104|CRFK|BF-?2|EPC|CHSE|MRC-5|WI-38|GMK|HEF|FtGF|ZMAC|PAM|N2a|RK-?13|H358)\b", text, re.I)
    cell_top=[c for c,_ in Counter(cells).most_common(4)]
    # crude virus
    vir=re.findall(r"\b(SARS-CoV-2|GETV|PRRSV|HEV|hepatitis E|ranavirus|betanodavirus|Ebola|rabies|IBDV|CyHV-2|HSV|CMV|adenovirus|enterovirus|measles|rubella|RSV|influenza|dengue|Zika|chikungunya|West Nile|NDV|Newcastle|PEDV|ASFV|FMDV|CDV|rotavirus|norovirus|HIV)\b", text, re.I)
    vir_top=[v for v,_ in Counter([x.lower() for x in vir]).most_common(4)]
    # exclude obvious non-isolation primary topics
    tl=title.lower()
    exclude=False; reason=""
    for bad in ["adipocyte","endothelial dysfunction","aav vector","wolbachia","polystyrene microplastic","lipid-induced","centrocestus"]:
        if bad in tl:
            exclude=True; reason=bad; break
    if exclude:
        print(f"SKIP excl={reason} | {pre}->{post} | {year} | PMC{pmc} | {title[:50]}")
        continue
    rec={"pmcid":"PMC"+pmc,"pmid":pmid_m.group(1) if pmid_m else "","doi":doi_m.group(1) if doi_m else "","year":year,"title":title[:200],"pre":pre,"post":post,"quote_pre":qpre,"quote_post":qpost,"method":method,"cells":cell_top,"viruses":vir_top,"note":note}
    results.append(rec)
    print(f"HIT {pre}->{post} | {year} | PMC{pmc} | {cell_top[:2]} | {vir_top[:2]} | {title[:55]}")

print("TOTAL", len(results))
pat=Counter(f"{r['pre']}->{r['post']}" for r in results)
print("patterns", dict(pat.most_common()))
with open(exp/"_ft_hits_v2.json","w",encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
