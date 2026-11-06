# -*- coding: utf-8 -*-
import json, urllib.request, re, time, ssl, html, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
hits = json.load(open(exp/"_ft_hits_v2.json", encoding="utf-8"))

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

# Score each hit for isolation-practice relevance
scored=[]
for h in hits:
    xml=fetch_ft(h["pmcid"])
    time.sleep(0.15)
    if not xml:
        continue
    text=strip(xml)
    title=(h.get("title") or "").lower()
    score=0; flags=[]
    # positive signals
    if re.search(r"(?:primary isolation|virus isolation|isolated from|clinical (?:specimen|sample|sample)|field (?:isolate|sample)|patient|throat swab|nasopharyngeal|tissue homogenate|fecal|outbreak)", text, re.I):
        score += 2; flags.append("isol_lang")
    if re.search(r"(?:inoculat(?:ed|ion).{0,40}(?:specimen|sample|homogenate|swab|filtrate)|specimen.{0,40}inoculat)", text, re.I):
        score += 3; flags.append("inoc_specimen")
    if re.search(r"(?:diagnostic|surveillance|outbreak|diseased|clinical cases)", text, re.I):
        score += 1; flags.append("diag")
    # negative signals (antiviral / lab stock primary)
    if re.search(r"(?:antiviral|inhibitor|IC50|EC50|repurposing|in vitro screening of|monoclonal antibod)", title, re.I):
        score -= 3; flags.append("neg_title_antiviral")
    if re.search(r"(?:lab(?:oratory)? strain|reference strain|stock virus|MOI of|plaque assay only)", text[:3000], re.I) and not re.search(r"isolat(?:ed|ion) from", text[:4000], re.I):
        score -= 1; flags.append("lab_stockish")
    # extract richer isolation paragraph
    isol_para=""
    m=re.search(r".{0,80}(?:virus isolation|isolated from|inoculat(?:ed|ion) with.{0,60}(?:specimen|sample|homogenate)|tissue homogenate).{0,350}", text, re.I)
    if m: isol_para=m.group(0)[:420]
    # medium base
    base=""
    bm=re.search(r"\b(DMEM|MEM|EMEM|RPMI(?:-?1640)?|L-15|GMEM|Medium 199|Opti-?MEM)\b", h.get("quote_pre","")+" "+h.get("quote_post","")+" "+text[text.lower().find("cell"):text.lower().find("cell")+800] if "cell" in text.lower() else "", re.I)
    # better: near growth medium
    bm=re.search(r"(DMEM|MEM|EMEM|RPMI(?:-?1640)?|L-15|GMEM|Eagle.?s? minimum essential medium|Dulbecco.?s? modified Eagle.?s? medium)[^\.]{0,100}?(?:\d+(?:\.\d+)?\s*%\s*(?:FBS|FCS|fetal))", text, re.I)
    if bm: base=bm.group(1)
    rec={**h, "score":score, "flags":flags, "isol_para":isol_para, "base_guess":base}
    scored.append(rec)

scored.sort(key=lambda x: -x["score"])
print("=== TOP by isolation score ===")
for r in scored[:35]:
    print(f"score={r['score']:2d} {r['pre']}->{r['post']} | {r['year']} | {r['pmcid']} | {r['flags']} | {(r.get('title') or '')[:58]}")
    if r.get("isol_para"):
        print("   ", r["isol_para"][:180].replace("\n"," "))

keepers=[r for r in scored if r["score"]>=3]
print("\nkeepers score>=3:", len(keepers))
borderline=[r for r in scored if 1<=r["score"]<3]
print("borderline 1-2:", len(borderline))
with open(exp/"_ft_scored.json","w",encoding="utf-8") as f:
    json.dump({"keepers":keepers,"borderline":borderline,"all":scored}, f, indent=2, ensure_ascii=False)
