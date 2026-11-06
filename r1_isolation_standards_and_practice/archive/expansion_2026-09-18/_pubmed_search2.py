import json, urllib.request, urllib.parse, re, time, ssl
ctx = ssl.create_default_context()
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

queries = [
    ('maint 2 fetal growth 10', '"virus isolation"[tiab] AND "fetal bovine"[tiab] AND ("maintenance medium"[tiab] OR "maintenance media"[tiab])'),
    ('10 percent FBS 2 percent isolation', '("10 percent" OR "10%") AND ("2 percent" OR "2%") AND FBS AND (isolation OR "cell culture") AND virus'),
    ('growth medium 10 FBS maintenance 2', '"growth medium" AND FBS AND "maintenance" AND virus AND isolation'),
    ('MEM 10 FBS 2 FBS virus isolation', 'MEM AND "fetal bovine serum" AND isolation AND (enterovirus OR adenovirus OR herpes OR measles OR rubella OR RSV)'),
    ('Vero 10 FBS 2 FBS isolation clinical', 'Vero AND isolation AND "fetal bovine serum" AND (clinical OR specimen OR patient) AND virus'),
    ('Hierholzer virus isolation', 'Hierholzer[Author] AND (isolation OR "cell culture") AND virus'),
    ('Mizuta isolation FBS', 'Mizuta[Author] AND Yamagata AND (isolation OR microplate) AND virus'),
    ('shell vial virus isolation FBS', '"shell vial" AND isolation AND "fetal bovine" AND virus'),
    ('diagnostic virology laboratory isolation FBS', '("diagnostic virology" OR "clinical virology") AND isolation AND "fetal bovine"'),
    ('WHO measles isolation Vero', 'measles AND isolation AND (Vero OR SLAM) AND "fetal bovine"'),
    ('rubella virus isolation cell culture FBS', 'rubella AND isolation AND ("fetal bovine" OR FBS) AND (Vero OR RK13 OR SIRC)'),
    ('enterovirus RD isolation FBS', 'enterovirus AND isolation AND (RD OR "GMK" OR "HEp-2") AND "fetal bovine"'),
]

all_pmids = {}
for label, q in queries:
    params = urllib.parse.urlencode({'db':'pubmed','term':q,'retmax':30,'retmode':'json'})
    url = base + 'esearch.fcgi?' + params
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=30) as r:
            data = json.loads(r.read().decode())
        ids = data['esearchresult']['idlist']
        count = data['esearchresult']['count']
        print(f'{label}: count={count} n={len(ids)}')
        all_pmids[label] = ids
        time.sleep(0.4)
    except Exception as e:
        print('ERR', label, e)

uniq=[]; seen=set()
for ids in all_pmids.values():
    for i in ids:
        if i not in seen:
            seen.add(i); uniq.append(i)
print('Unique', len(uniq))

# Get abstracts via efetch XML for first 80
def fetch_abstracts(pmids):
    results=[]
    for i in range(0, len(pmids), 20):
        batch=pmids[i:i+20]
        params=urllib.parse.urlencode({'db':'pubmed','id':','.join(batch),'retmode':'xml','rettype':'abstract'})
        url=base+'efetch.fcgi?'+params
        with urllib.request.urlopen(url, context=ctx, timeout=90) as r:
            xml=r.read().decode('utf-8','replace')
        # split articles
        arts=re.split(r'<PubmedArticle>', xml)[1:]
        for art in arts:
            pmid=re.search(r'<PMID[^>]*>(\d+)', art)
            title=re.search(r'<ArticleTitle>(.*?)</ArticleTitle>', art, re.S)
            year=re.search(r'<PubDate>.*?<Year>(\d{4})</Year>', art, re.S)
            abstract=' '.join(re.findall(r'<AbstractText[^>]*>(.*?)</AbstractText>', art, re.S))
            abstract=re.sub(r'<[^>]+>','',abstract)
            title_t=re.sub(r'<[^>]+>','',title.group(1) if title else '')
            # look for FBS percentages
            fbs_hits=re.findall(r'.{0,40}(?:FBS|fetal bovine|foetal bovine|SVF|FKS).{0,40}', abstract, re.I)
            pcts=re.findall(r'(\d+(?:\.\d+)?)\s*%\s*(?:FBS|fetal|foetal|HI-?FBS|heat)', abstract, re.I)
            pcts2=re.findall(r'(?:FBS|fetal bovine serum)\s*[(\[]?\s*(\d+(?:\.\d+)?)\s*%', abstract, re.I)
            allpct=list(dict.fromkeys(pcts+pcts2))
            results.append({
                'pmid': pmid.group(1) if pmid else '',
                'year': year.group(1) if year else '',
                'title': title_t[:200],
                'pcts': allpct,
                'fbs_context': fbs_hits[:4],
                'abstract': abstract[:1500],
            })
        time.sleep(0.5)
        print('fetched batch', i, '->', len(results))
    return results

abs_data = fetch_abstracts(uniq[:100])
# filter those with at least 2 different percentages mentioned or 10 and 2
candidates=[]
for a in abs_data:
    pcts=set(a['pcts'])
    blob=(a['abstract']+' '+a['title']).lower()
    has_isolation = any(w in blob for w in ['isolat','inoculat','clinical specimen','patient sample','nasopharyngeal','throat swab','stool'])
    if len(pcts)>=2 or ('10' in pcts and '2' in pcts) or re.search(r'10\s*%.*2\s*%|2\s*%.*10\s*%', a['abstract']):
        a['has_isolation_kw']=has_isolation
        candidates.append(a)

print('\nCandidates with multi-%:', len(candidates))
for c in candidates:
    print(f"PMID{c['pmid']}|{c['year']}|pcts={c['pcts']}|isol={c['has_isolation_kw']}|{c['title'][:80]}")

with open(r'C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion\_pubmed_abstracts_repr.json','w',encoding='utf-8') as f:
    json.dump({'queries':all_pmids,'candidates':candidates,'all':abs_data}, f, indent=2)
print('saved')
