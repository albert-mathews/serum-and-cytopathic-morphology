import json, urllib.request, re, time, ssl, html
from pathlib import Path
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
cands = json.load(open(exp/"_ft_cands_repr.json", encoding="utf-8"))

def fetch_ft(pmcid):
    pmcid = str(pmcid).replace("PMC","")
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmcid}/fullTextXML"
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=40) as r:
            return r.read().decode("utf-8","replace")
    except Exception:
        return None

def analyze_ft(xml, meta):
    if not xml: return None
    text = re.sub(r"<[^>]+>", " ", xml)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    isol = bool(re.search(r"\b(isolat(?:e|ed|ion)|clinical (?:specimen|sample)|patient (?:sample|specimen)|nasopharyngeal|throat swab|fecal|stool|inoculat)", text, re.I))
    if not isol:
        return None
    pre=None; post=None; qpre=""; qpost=""; method="none"
    # 1) explicit growth + maintenance medium
    gm = re.search(r"growth medium[^\.]{0,140}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|fetal bovine serum|foetal bovine serum)", text, re.I)
    mm = re.search(r"maintenance medium[^\.]{0,140}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|fetal bovine serum|foetal bovine serum)", text, re.I)
    # maintenance with trypsin / serum-free coded as 0
    mm0 = re.search(r"maintenance medium[^\.]{0,160}?(?:without (?:FBS|serum)|serum[- ]free|no FBS|crystallized trypsin|TPCK[- ]trypsin)", text, re.I)
    if gm and mm:
        pre, post = gm.group(1), mm.group(1)
        qpre, qpost = gm.group(0)[:220], mm.group(0)[:220]
        method = "GM_MM"
    elif gm and mm0:
        pre, post = gm.group(1), "0"
        qpre, qpost = gm.group(0)[:220], mm0.group(0)[:220]
        method = "GM_MM0"
    else:
        g2 = re.search(r"(?:cells (?:were )?(?:grown|maintained|cultured|propagated)[^\.]{0,160}?)(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|fetal bovine serum|foetal bovine serum)", text, re.I)
        m2 = re.search(r"(?:(?:maintenance|infection|isolation|inoculation) medium|after (?:adsorption|inoculation)|medium was (?:then )?(?:changed|replaced)|replaced with|added[^\.]{0,50}?(?:MEM|DMEM|Eagle))[^\.]{0,140}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|fetal bovine serum|foetal bovine serum)", text, re.I)
        m2_0 = re.search(r"(?:(?:maintenance|infection|isolation) medium|after (?:adsorption|inoculation)|replaced with)[^\.]{0,160}?(?:without (?:FBS|serum)|serum[- ]free|no FBS|0%\s*FBS)", text, re.I)
        if g2 and m2:
            pre, post = g2.group(1), m2.group(1)
            qpre, qpost = g2.group(0)[:220], m2.group(0)[:220]
            method = "grown_maint"
        elif g2 and m2_0:
            pre, post = g2.group(1), "0"
            qpre, qpost = g2.group(0)[:220], m2_0.group(0)[:220]
            method = "grown_SF"
    if pre is None or post is None:
        return None
    # collect FBS windows for QC
    windows=[]
    for m in re.finditer(r".{0,80}(?:\d+(?:\.\d+)?\s*%\s*(?:FBS|fetal bovine|foetal bovine)|(?:FBS|fetal bovine serum)[^\.]{0,30}\d+(?:\.\d+)?\s*%).{0,80}", text, re.I):
        windows.append(m.group(0)[:180])
        if len(windows)>=6: break
    return {**meta, "pre":pre, "post":post, "quote_pre":qpre, "quote_post":qpost, "method":method, "sample_windows":windows}

# Stratify lightly by year for representative scan
from collections import defaultdict
by_dec = defaultdict(list)
for c in cands:
    y = int(c.get("year") or 0)
    dec = (y//10)*10 if y else 0
    by_dec[dec].append(c)
# take up to 20 per decade + fill
scan=[]
for dec in sorted(by_dec):
    scan.extend(by_dec[dec][:22])
# also add remaining until ~120
seen=set(id(x) for x in scan)
for c in cands:
    if len(scan)>=130: break
    if id(c) not in seen:
        scan.append(c)

print(f"scanning {len(scan)} of {len(cands)}")
results=[]; soft=[]
for i,c in enumerate(scan):
    xml = fetch_ft(c["pmcid"])
    time.sleep(0.22)
    if not xml:
        continue
    a = analyze_ft(xml, c)
    if a:
        results.append(a)
        print(f"HIT {a['pre']}->{a['post']} | {c['year']} | PMC{str(c['pmcid']).replace('PMC','')} | {(c['title'] or '')[:60]}")
    if (i+1)%15==0:
        print(f"... {i+1}/{len(scan)} hits={len(results)}")

print("TOTAL HITS", len(results))
# pattern counts
from collections import Counter
pat=Counter(f"{r['pre']}->{r['post']}" for r in results)
print("patterns:", dict(pat.most_common()))
with open(exp/"_ft_hits_repr.json","w",encoding="utf-8") as f:
    json.dump(results, f, indent=2)
print("saved")
