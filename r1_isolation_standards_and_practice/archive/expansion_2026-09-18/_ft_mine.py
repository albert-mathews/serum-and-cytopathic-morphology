import json, urllib.request, urllib.parse, re, time, ssl, html
from pathlib import Path
from collections import defaultdict
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
dedup = set(json.load(open(exp/"_dedup_keys_repr.json"))["keys"])

def is_dup(pmid=None, doi=None, pmc=None):
    checks=[]
    if pmid: checks.append(f"link|pmid:{pmid}")
    if pmc:
        p=str(pmc).lower().replace('pmc','')
        checks.append(f"link|pmc:{p}")
    if doi:
        d=doi.lower().rstrip('./')
        checks.append(f"doi|{d}"); checks.append(f"link|doi:{d}")
    return any(c in dedup for c in checks)

def epmc_search(q, pageSize=50):
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({
        'query': q, 'format': 'json', 'pageSize': pageSize, 'resultType': 'core'
    })
    with urllib.request.urlopen(url, context=ctx, timeout=60) as r:
        return json.loads(r.read().decode())

# Focused OA fulltext queries - representative isolation
queries = [
    'OPEN_ACCESS:Y HAS_FT:Y "maintenance medium" "2% FBS" "10% FBS" (isolation OR inoculated OR specimen)',
    'OPEN_ACCESS:Y HAS_FT:Y "MEM supplemented with 10% FBS" "2% FBS" (virus isolation OR "clinical specimen" OR inoculated)',
    'OPEN_ACCESS:Y HAS_FT:Y "DMEM" "10% FBS" "2% FBS" ("virus isolation" OR "isolated from" OR "clinical samples") Vero',
    'OPEN_ACCESS:Y HAS_FT:Y "growth medium" "10% FBS" "maintenance medium" "2% FBS" virus',
    'OPEN_ACCESS:Y HAS_FT:Y "shell vial" ("10% FBS" OR "10% fetal") ("2% FBS" OR "2% fetal")',
    'OPEN_ACCESS:Y HAS_FT:Y (enterovirus OR adenovirus OR measles OR rubella OR HSV OR "herpes simplex" OR RSV) isolation "10% FBS" "2% FBS"',
    'OPEN_ACCESS:Y HAS_FT:Y (PRRSV OR "African swine" OR FMDV OR PPRV OR "canine distemper" OR "infectious bronchitis") isolation "10% FBS" "2% FBS"',
    'OPEN_ACCESS:Y HAS_FT:Y (dengue OR "West Nile" OR Zika OR chikungunya OR yellow fever) isolation ("10% FBS" OR "10% fetal") ("2% FBS" OR "2% fetal")',
    'OPEN_ACCESS:Y HAS_FT:Y (influenza) isolation MDCK ("10% FBS") (trypsin OR "2% FBS" OR serum-free)',
    'OPEN_ACCESS:Y HAS_FT:Y Numazaki OR "microplate method" isolation virus FBS',
]

cands=[]
seen=set()
for q in queries:
    try:
        data=epmc_search(q, 40)
        hits=data.get('resultList',{}).get('result',[])
        print(f'hitCount={data.get("hitCount")} got={len(hits)} | {q[20:70]}...')
        for h in hits:
            pmid=h.get('pmid'); pmcid=h.get('pmcid'); doi=h.get('doi')
            key=pmid or pmcid or doi
            if not key or key in seen: continue
            seen.add(key)
            if is_dup(pmid=pmid, doi=doi, pmc=pmcid): 
                continue
            if h.get('isOpenAccess')!='Y' and not pmcid:
                continue
            cands.append({
                'pmid':pmid,'doi':doi,'pmcid':pmcid,
                'title':h.get('title'),'year':h.get('pubYear'),
                'journal':h.get('journalTitle'),
            })
        time.sleep(0.3)
    except Exception as e:
        print('ERR', e)

print('OA candidates nondup:', len(cands))

# Fetch full text from EuropePMC for up to 80
def fetch_ft(pmcid):
    pmcid=pmcid.replace('PMC','')
    url=f'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmcid}/fullTextXML'
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=45) as r:
            return r.read().decode('utf-8','replace')
    except Exception as e:
        return None

def analyze_ft(xml, meta):
    if not xml: return None
    # strip tags for search but keep some structure
    text=re.sub(r'<[^>]+>',' ', xml)
    text=html.unescape(text)
    text=re.sub(r'\s+',' ', text)
    # Find methods-ish windows mentioning FBS percentages
    windows=[]
    for m in re.finditer(r'.{0,120}(?:\d+(?:\.\d+)?\s*%\s*(?:FBS|fetal bovine|foetal bovine|HI-FBS)|(?:FBS|fetal bovine serum)[^\.]{0,40}\d+(?:\.\d+)?\s*%).{0,120}', text, re.I):
        windows.append(m.group(0))
    # Extract paired growth/maintenance patterns
    patterns=[]
    # classic phrases
    for rx, lab in [
        (r'(?:grown|cultured|maintained|propagated|seeded)[^\.]{0,100}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|fetal bovine serum|foetal bovine serum)', 'growth_like'),
        (r'(?:growth medium|GM)[^\.]{0,80}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|fetal)', 'growth_med'),
        (r'(?:maintenance medium|MM|infection medium|inoculation medium|after (?:adsorption|inoculation)|post[- ]inoculation)[^\.]{0,100}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|fetal)', 'maint_like'),
        (r'(?:supplemented with|containing)\s+(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|fetal bovine serum)', 'supp'),
    ]:
        for m in re.finditer(rx, text, re.I):
            patterns.append((lab, m.group(1), m.group(0)[:160]))
    # Look for explicit 10 and 2 near growth/maint vocabulary
    pre=None; post=None; qpre=''; qpost=''
    # Prefer explicit growth + maintenance
    gm = re.search(r'growth medium[^\.]{0,120}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|fetal bovine|foetal)', text, re.I)
    mm = re.search(r'maintenance medium[^\.]{0,120}?(\d+(?:\.\d+)?)\s*%\s*(?:FBS|fetal bovine|foetal)', text, re.I)
    if gm and mm:
        pre, post = gm.group(1), mm.group(1)
        qpre, qpost = gm.group(0)[:200], mm.group(0)[:200]
    else:
        # grown/maintained X% ... then Y% after inoculation / maintenance
        g2 = re.search(r'(?:cells (?:were )?(?:grown|maintained|cultured|propagated)[^\.]{0,150}?)(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|fetal bovine serum)', text, re.I)
        m2 = re.search(r'(?:(?:maintenance|infection|isolation) medium|after (?:adsorption|inoculation)|medium was (?:then )?changed|replaced with|added[^\.]{0,40}?(?:MEM|DMEM|medium))[^\.]{0,120}?(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:FBS|fetal bovine serum)', text, re.I)
        # also: containing 10% FBS ... containing 2% FBS in close proximity for growth vs infection
        if g2 and m2 and g2.group(1)!=m2.group(1):
            pre, post = g2.group(1), m2.group(1)
            qpre, qpost = g2.group(0)[:200], m2.group(0)[:200]
        elif g2 and m2 and g2.group(1)==m2.group(1):
            # equal hold possible
            pre, post = g2.group(1), m2.group(1)
            qpre, qpost = g2.group(0)[:200], m2.group(0)[:200]
    # isolation keyword check
    isol = bool(re.search(r'\b(isolat(?:e|ed|ion)|clinical (?:specimen|sample)|patient (?:sample|specimen)|nasopharyngeal|throat swab|fecal|stool|serum sample inoculated)', text, re.I))
    # virus mention
    return {
        **meta,
        'pre': pre, 'post': post,
        'quote_pre': qpre, 'quote_post': qpost,
        'isolation_kw': isol,
        'n_fbs_windows': len(windows),
        'sample_windows': windows[:8],
        'n_patterns': len(patterns),
    }

results=[]
# prioritize pmcid
with_pmc=[c for c in cands if c.get('pmcid')]
print('with pmcid', len(with_pmc))
for i,c in enumerate(with_pmc[:90]):
    xml=fetch_ft(c['pmcid'])
    time.sleep(0.25)
    if not xml:
        continue
    a=analyze_ft(xml, c)
    if a and a.get('pre') and a.get('post') and a.get('isolation_kw'):
        results.append(a)
        print(f"HIT {c['pmcid']} PMID{c['pmid']} {c['year']} {a['pre']}->{a['post']} | {(c['title'] or '')[:55]}")
    if (i+1)%10==0:
        print(f'... scanned {i+1}, hits {len(results)}')

print('TOTAL HITS', len(results))
with open(exp/'_ft_hits_repr.json','w',encoding='utf-8') as f:
    json.dump(results, f, indent=2)
# also dump unresolved for manual
print('done')
