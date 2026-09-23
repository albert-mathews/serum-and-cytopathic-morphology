# -*- coding: utf-8 -*-
import json, urllib.request, re, time, ssl, html, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
dec = json.load(open(exp/"_ft_decisions.json", encoding="utf-8"))
ins = [d for d in dec if d.get("include")]

# Also fetch a few more known OA isolation papers
extra = ["4663707","7512137","8106717","3866114","7907832","105078","12784899","4593780","7040968","10659126"]
# skip if already

def fetch_ft(pmcid):
    pmcid=str(pmcid).replace("PMC","")
    url=f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmcid}/fullTextXML"
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=45) as r:
            return r.read().decode("utf-8","replace")
    except Exception as e:
        return None

def strip(xml):
    t=re.sub(r"<[^>]+>"," ", xml)
    t=html.unescape(t)
    return re.sub(r"\s+"," ", t)

def extract_all(text):
    out={}
    # antibiotics
    pen=re.search(r"(\d+)\s*(?:U|IU|units?)\s*(?:/?\s*mL)?[^\.]{0,20}penicillin|penicillin[^\.]{0,40}?(\d+)\s*(?:U|IU|units|/mL)", text, re.I)
    strep=re.search(r"streptomycin[^\.]{0,40}?(\d+(?:\.\d+)?)\s*(?:µg|ug|mg|/mL)|(\d+(?:\.\d+)?)\s*(?:µg|ug)\s*(?:/?\s*mL)?[^\.]{0,20}streptomycin", text, re.I)
    amph=re.search(r"amphotericin[^\.]{0,40}?(\d+(?:\.\d+)?)|(\d+(?:\.\d+)?)\s*(?:µg|ug|/mL)[^\.]{0,20}amphotericin", text, re.I)
    # growth/maint quotes
    quotes=[]
    for rx in [
        r".{0,40}growth medium.{0,200}",
        r".{0,40}maintenance medium.{0,200}",
        r".{0,40}FBS reduced to.{0,120}",
        r"cells (?:were )?(?:grown|maintained|cultured|propagated).{0,200}?%?\s*(?:FBS|FCS|fetal).{0,80}",
        r"(?:after (?:adsorption|inoculation)|infection medium|isolation medium).{0,200}?%?\s*(?:FBS|FCS|fetal|serum-free|without).{0,80}",
        r"DMEM with \d+% and \d+%.{0,120}",
        r"supplemented with \d+%.{0,40}(?:FBS|FCS).{0,80}",
    ]:
        for m in re.finditer(rx, text, re.I):
            quotes.append(m.group(0)[:260])
            if len(quotes)>=12: break
        if len(quotes)>=12: break
    isol=[]
    for m in re.finditer(r".{0,50}(?:virus isolation|isolated from|inoculat.{0,100}(?:homogenate|specimen|sample|swab|tissue|filtrate)).{0,280}", text, re.I):
        isol.append(m.group(0)[:300])
        if len(isol)>=5: break
    return quotes, isol

verified=[]
for d in ins:
    pmc=d["pmcid"]
    xml=fetch_ft(pmc)
    time.sleep(0.15)
    if not xml:
        print("NOFT", pmc); continue
    text=strip(xml)
    quotes, isol = extract_all(text)
    print("\n====", pmc, d.get("year"), d.get("pre"), "->", d.get("post"), "|", (d.get("title") or "")[:60])
    print("QUOTES:")
    for q in quotes[:6]:
        print("  Q:", q[:200])
    print("ISOL:")
    for q in isol[:3]:
        print("  I:", q[:200])
    verified.append({**d, "quotes_extra":quotes[:8], "isol_extra":isol[:4]})

# extras
print("\n\n===== EXTRAS =====")
for pmc in extra:
    xml=fetch_ft(pmc)
    time.sleep(0.15)
    if not xml:
        print("NOFT extra", pmc); continue
    text=strip(xml)
    title_m=re.search(r"<article-title[^>]*>(.*?)</article-title>", xml, re.I|re.S)
    title=re.sub(r"<[^>]+>","", title_m.group(1)) if title_m else ""
    year_m=re.search(r"<pub-date[^>]*>.*?<year>(\d{4})</year>", xml, re.I|re.S)
    year=year_m.group(1) if year_m else ""
    quotes, isol = extract_all(text)
    # quick dual detect
    gm=re.search(r"growth medium[^\.]{0,140}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|FCS|fetal)", text, re.I)
    mm=re.search(r"maintenance medium[^\.]{0,140}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|FCS|fetal)", text, re.I)
    red=re.search(r"(?:FBS|FCS|serum)\s+(?:was\s+)?reduced to\s+(\d+(?:\.\d+)?)\s*%", text, re.I)
    g=re.search(r"(?:propagated|grown|maintained).{0,100}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|FCS|fetal bovine)", text, re.I)
    pre=post=None
    if gm and mm: pre,post=gm.group(1),mm.group(1)
    elif g and red: pre,post=g.group(1),red.group(1)
    elif gm and red: pre,post=gm.group(1),red.group(1)
    print(f"\nEXTRA PMC{pmc} {year} dual={pre}->{post} | {title[:70]}")
    for q in quotes[:5]:
        print("  Q:", q[:180])
    for q in isol[:2]:
        print("  I:", q[:180])
    if pre and post:
        verified.append({"pmcid":"PMC"+pmc,"year":year,"title":title,"pre":pre,"post":post,"quotes_extra":quotes[:8],"isol_extra":isol[:4],"include":True,"decision_reason":"extra_fetch","pmid":"","doi":""})

with open(exp/"_ft_verified_raw.json","w",encoding="utf-8") as f:
    json.dump(verified, f, indent=2, ensure_ascii=False)
print("\nsaved verified", len(verified))
