import json, urllib.request, urllib.parse, re, time, ssl, csv
from pathlib import Path
ctx = ssl.create_default_context()

exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
dedup = set(json.load(open(exp/"_dedup_keys_repr.json"))["keys"])

def is_dup(pmid=None, doi=None, pmc=None, link=None):
    checks=[]
    if pmid: checks.append(f"link|pmid:{pmid}")
    if pmc: checks.append(f"link|pmc:{str(pmc).lower().replace('pmc','')}")
    if doi:
        d=doi.lower().rstrip('./')
        checks.append(f"doi|{d}")
        checks.append(f"link|doi:{d}")
    if link:
        # crude
        m=re.search(r'pubmed\.ncbi\.nlm\.nih\.gov/(\d+)', link or '')
        if m: checks.append(f"link|pmid:{m.group(1)}")
        m=re.search(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', link or '', re.I)
        if m: checks.append(f"doi|{m.group(0).lower().rstrip('./')}")
    return any(c in dedup for c in checks), checks

# EuropePMC search
queries = [
    '"maintenance medium" "2% FBS" "10% FBS" virus isolation',
    '"MEM containing 10% FBS" "2% FBS" isolation',
    '"DMEM supplemented with 10%" "2% FBS" virus isolation',
    '"grown in" "10% fetal bovine" "maintenance" "2%" virus',
    '"cells were maintained" "10% FBS" inoculated "2% FBS"',
    'Numazaki microplate "fetal bovine"',
    '"shell vial" "2% FBS" "10%" cytomegalovirus OR HSV OR adenovirus',
    'adenovirus isolation A549 "10% FBS" "2%"',
    'measles isolation "Vero" "10% FBS" "2% FBS"',
    'enterovirus isolation "RD cells" "10%" "2% FBS"',
    'HSV isolation "Vero" "10% FBS" "maintenance" "2%"',
    'rabies isolation "N2a" OR "BSR" "FBS" "2%"',
    'PRRSV isolation "MARC-145" "10% FBS" "2%"',
    'ASFV OR "African swine fever" isolation "2% FBS" "10%"',
    '"West Nile" isolation Vero "10% FBS" "2% FBS"',
    'dengue isolation "C6/36" "10%" "2% FBS"',
    'rubella isolation "Vero" OR "RK-13" "FBS"',
    '"infectious bronchitis" isolation "2% FBS" "10%"',
    'canine distemper isolation "Vero" "10% FBS" "2%"',
    'rotavirus isolation "MA104" "10% FBS"',
]

def epmc_search(q, pageSize=25):
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({
        'query': q, 'format': 'json', 'pageSize': pageSize, 'resultType': 'core'
    })
    with urllib.request.urlopen(url, context=ctx, timeout=60) as r:
        return json.loads(r.read().decode())

all_hits=[]
seen=set()
for q in queries:
    try:
        data=epmc_search(q)
        hits=data.get('resultList',{}).get('result',[])
        print(f'Q: {q[:60]}... -> {data.get("hitCount")} (got {len(hits)})')
        for h in hits:
            pid=h.get('id') or h.get('pmid') or h.get('doi')
            if pid in seen: continue
            seen.add(pid)
            all_hits.append({
                'pmid': h.get('pmid'),
                'doi': h.get('doi'),
                'pmcid': h.get('pmcid'),
                'title': h.get('title'),
                'year': h.get('pubYear'),
                'isOpenAccess': h.get('isOpenAccess'),
                'journal': h.get('journalTitle'),
                'abstract': (h.get('abstractText') or '')[:1200],
            })
        time.sleep(0.35)
    except Exception as e:
        print('ERR', q[:40], e)

print('Total unique hits', len(all_hits))

# score for dual FBS mentions in abstract
def extract_pcts(text):
    text=text or ''
    pcts=re.findall(r'(\d+(?:\.\d+)?)\s*%\s*(?:FBS|fetal|foetal|HI.?FBS|heat-inactivated FBS)', text, re.I)
    pcts += re.findall(r'(?:FBS|fetal bovine serum)\s*(?:\([^)]*\))?\s*(?:at\s*)?(\d+(?:\.\d+)?)\s*%', text, re.I)
    pcts += re.findall(r'supplemented with (\d+(?:\.\d+)?)\s*%\s*(?:FBS|fetal)', text, re.I)
    pcts += re.findall(r'(\d+(?:\.\d+)?)\s*%\s*(?:heat[- ]inactivated\s+)?(?:fetal bovine serum|FBS)', text, re.I)
    return list(dict.fromkeys(pcts))

scored=[]
for h in all_hits:
    blob=(h['abstract'] or '') + ' ' + (h['title'] or '')
    pcts=extract_pcts(blob)
    # also look for classic pattern phrases even if abstract sparse
    classic=bool(re.search(r'10\s*%[\s\S]{0,80}2\s*%|2\s*%[\s\S]{0,80}10\s*%', blob))
    dup, checks = is_dup(pmid=h['pmid'], doi=h['doi'], pmc=h.get('pmcid'))
    scored.append({**h, 'pcts':pcts, 'classic':classic, 'dup':dup})

multi=[s for s in scored if (len(s['pcts'])>=2 or s['classic']) and not s['dup']]
print('\nNon-dup multi-% or classic pattern in abstract:', len(multi))
for s in multi[:50]:
    print(f"PMID{s['pmid']}|{s['year']}|OA={s['isOpenAccess']}|pcts={s['pcts']}|classic={s['classic']}|{ (s['title'] or '')[:70]}")

with open(exp/'_epmc_repr_hits.json','w',encoding='utf-8') as f:
    json.dump({'multi':multi,'all_scored':scored}, f, indent=2)
print('saved epmc')
