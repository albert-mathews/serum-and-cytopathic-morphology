import json, urllib.request, urllib.parse, re, time, ssl
ctx = ssl.create_default_context()

queries = [
    ('enterovirus isolation FBS 10% 2%', '"enterovirus" AND isolation AND ("10% fetal" OR "10% FBS") AND ("2% fetal" OR "2% FBS")'),
    ('adenovirus isolation 10 2', 'adenovirus AND isolation AND ("10% fetal bovine" OR "10% FBS") AND ("2% FBS" OR "2% fetal")'),
    ('HSV isolation 10% 2%', '("herpes simplex" OR HSV) AND isolation AND ("10% FBS" OR "10% fetal") AND ("2% FBS" OR "2% fetal")'),
    ('measles rubella isolation FBS', '(measles OR rubella) AND isolation AND ("10% FBS" OR "10% fetal") AND ("2% FBS" OR "2% fetal")'),
    ('RSV isolation 10 2 FBS', '("respiratory syncytial" OR RSV) AND isolation AND ("10% FBS" OR "10% fetal") AND ("2% FBS" OR "2% fetal")'),
    ('arbovirus isolation Vero 10 2', '(arbovirus OR flavivirus OR dengue OR "West Nile" OR Zika OR chikungunya) AND isolation AND ("10% FBS" OR "10% fetal") AND ("2% FBS" OR "2% fetal") AND (Vero OR C6/36)'),
    ('Numazaki isolation', 'Numazaki AND (isolation OR "cell culture") AND (virus OR viral)'),
    ('clinical virus isolation maintenance medium 2% FBS', '"virus isolation" AND "maintenance medium" AND ("2% FBS" OR "2% fetal bovine") AND ("10% FBS" OR "10% fetal")'),
    ('diagnostic virology growth medium 10% maintenance 2%', '("growth medium" OR "growth media") AND ("maintenance medium") AND (FBS OR "fetal bovine") AND ("virus isolation" OR "viral isolation")'),
    ('influenza isolation MDCK 10% FBS', 'influenza AND isolation AND MDCK AND ("10% FBS" OR "10% fetal") AND ("2% FBS" OR "trypsin")'),
]

base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
all_pmids = {}
for label, q in queries:
    params = urllib.parse.urlencode({'db':'pubmed','term':q,'retmax':40,'retmode':'json'})
    url = base + 'esearch.fcgi?' + params
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=30) as r:
            data = json.loads(r.read().decode())
        ids = data['esearchresult']['idlist']
        count = data['esearchresult']['count']
        print(f'\n=== {label} | count={count} | returned={len(ids)} ===')
        all_pmids[label] = ids
        time.sleep(0.34)
    except Exception as e:
        print('ERR', label, e)

# unique pmids
uniq = []
seen=set()
for ids in all_pmids.values():
    for i in ids:
        if i not in seen:
            seen.add(i); uniq.append(i)
print('\nUnique PMIDs:', len(uniq))

# fetch summaries in batches
def fetch_summaries(pmids):
    out=[]
    for i in range(0,len(pmids),50):
        batch=pmids[i:i+50]
        params=urllib.parse.urlencode({'db':'pubmed','id':','.join(batch),'retmode':'json'})
        url=base+'esummary.fcgi?'+params
        with urllib.request.urlopen(url, context=ctx, timeout=60) as r:
            data=json.loads(r.read().decode())
        for pid in batch:
            rec=data['result'].get(pid,{})
            out.append({
                'pmid':pid,
                'title':rec.get('title',''),
                'pubdate':rec.get('pubdate',''),
                'source':rec.get('source',''),
                'authors':'; '.join(a.get('name','') for a in rec.get('authors',[])[:3]),
            })
        time.sleep(0.34)
    return out

summaries = fetch_summaries(uniq[:120])
with open(r'C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion\_pubmed_repr_search.json','w',encoding='utf-8') as f:
    json.dump({'queries':{k:v for k,v in all_pmids.items()},'summaries':summaries}, f, indent=2)
for s in summaries[:40]:
    print(f"{s['pmid']}|{s['pubdate'][:4]}|{s['source'][:20]}|{s['title'][:90]}")
print('... total summaries', len(summaries))
