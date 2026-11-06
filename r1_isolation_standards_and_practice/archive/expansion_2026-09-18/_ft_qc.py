import json, urllib.request, re, time, ssl, html
from pathlib import Path
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
hits = json.load(open(exp/"_ft_hits_repr.json", encoding="utf-8"))

def fetch_ft(pmcid):
    pmcid = str(pmcid).replace("PMC","")
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmcid}/fullTextXML"
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=40) as r:
            return r.read().decode("utf-8","replace")
    except Exception as e:
        return f"ERR:{e}"

# For each hit, pull broader methods context around FBS and virus isolation sentences
out=[]
for h in hits:
    xml = fetch_ft(h["pmcid"])
    time.sleep(0.2)
    if xml.startswith("ERR"):
        h["qc"]="fetch_fail"; out.append(h); continue
    text = re.sub(r"<[^>]+>", " ", xml)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    # isolation context sentences
    isol_sents = []
    for m in re.finditer(r"[^\.]{0,40}(?:virus isolat|isolated from|clinical specimen|patient sample|inoculat(?:ed|ion) with|throat swab|nasopharyngeal|fecal|homogenate)[^\.]{0,200}", text, re.I):
        isol_sents.append(m.group(0).strip()[:260])
        if len(isol_sents)>=5: break
    # cell/virus names
    cells = re.findall(r"\b(Vero(?:\s*E6)?|MDCK|HEp-?2|A549|RD(?:-?A)?|LLC-MK2|C6/36|BHK-?21|MARC-145|HeLa|MA104|CRFK|FKN|RTG-2|EPC|BF-?2|GF|CHSE|SHK|TO cells?|RK-?13|MRC-5|WI-38|NCI-H292|GMK|HEF)\b", text, re.I)
    from collections import Counter
    cell_top = [c for c,_ in Counter([c.upper() if len(c)<=6 else c for c in cells]).most_common(5)]
    viruses = re.findall(r"\b(SARS-CoV-2|influenza|HSV|herpes|adenovirus|enterovirus|measles|rubella|RSV|PRRSV|PPRV|dengue|Zika|chikungunya|West Nile|rabies|rotavirus|norovirus|ASFV|FMDV|IBV|CDV|HEV|hepatitis E|betanodavirus|ranavirus|NDV|Newcastle|AAV|HIV)\b", text, re.I)
    vir_top = [v for v,_ in Counter([v.lower() for v in viruses]).most_common(5)]
    # exclusion heuristics
    exclude_reason=[]
    title=(h.get("title") or "").lower()
    blob = text[:5000].lower()
    if any(x in title for x in ["adipocyte","endothelial dysfunction","aav vector toolkit","wolbachia","polystyrene microplastic","lipid-induced"]):
        exclude_reason.append("not_virus_isolation_primary")
    if "aav" in vir_top and "isolation" not in title:
        pass
    # check quotes still present
    h2=dict(h)
    h2["isol_sents"]=isol_sents
    h2["cells"]=cell_top
    h2["viruses"]=vir_top
    h2["exclude_reason"]=exclude_reason
    # longer quotes
    gm = re.search(r".{0,60}growth medium.{0,160}?(?:\d+(?:\.\d+)?\s*%\s*(?:FBS|fetal)|without FBS|serum-free).{0,80}", text, re.I)
    mm = re.search(r".{0,60}maintenance medium.{0,160}?(?:\d+(?:\.\d+)?\s*%\s*(?:FBS|fetal)|without FBS|serum-free|trypsin).{0,80}", text, re.I)
    if gm: h2["quote_pre_long"]=gm.group(0)[:280]
    if mm: h2["quote_post_long"]=mm.group(0)[:280]
    out.append(h2)
    print(f"{h['pre']}->{h['post']} | {h['year']} | PMC{h['pmcid']} | cells={cell_top[:3]} | vir={vir_top[:3]} | excl={exclude_reason} | {(h.get('title') or '')[:50]}")
    for s in isol_sents[:2]:
        print("   isol:", s[:140])

with open(exp/"_ft_hits_qc.json","w",encoding="utf-8") as f:
    json.dump(out, f, indent=2)
print("QC done", len(out))
