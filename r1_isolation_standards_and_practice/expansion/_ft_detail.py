# -*- coding: utf-8 -*-
import json, urllib.request, re, time, ssl, html, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")

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

pmcs = [
"13224474","13017990","8493110","12474081","10913406","11089916","10907662",
"13556978","13184637","13431588","5133602","11266174","12581222","13119600",
"12411486","5081539","8983140","7512137","7907832","13517838","12172445",
"11346336","4663707","8106717","3866114"
]

for pmc in pmcs:
    xml=fetch_ft(pmc)
    time.sleep(0.12)
    if not xml:
        print(f"\n### PMC{pmc} NOFT"); continue
    text=strip(xml)
    title_m=re.search(r"<article-title[^>]*>(.*?)</article-title>", xml, re.I|re.S)
    title=re.sub(r"<[^>]+>"," ", title_m.group(1) if title_m else "")
    title=re.sub(r"\s+"," ", title).strip()
    year_m=re.search(r"<pub-date[^>]*>.*?<year>(\d{4})</year>", xml, re.I|re.S)
    year=year_m.group(1) if year_m else "?"
    doi_m=re.search(r'<article-id pub-id-type="doi">(10\.[^<]+)</article-id>', xml)
    pmid_m=re.search(r'<article-id pub-id-type="pmid">(\d+)</article-id>', xml)
    print(f"\n### PMC{pmc} | {year} | PMID{pmid_m.group(1) if pmid_m else ''} | DOI{doi_m.group(1) if doi_m else ''}")
    print("TITLE:", title[:100])
    # focused windows
    for label, rx in [
        ("GROW", r".{0,30}(?:growth medium|grown in|propagated in|maintained in|cultured in|seeded).{0,160}?(?:\d+(?:\.\d+)?\s*%\s*(?:FBS|FCS|fetal|foetal)|10% FBS|5% FBS).{0,60}"),
        ("MAINT", r".{0,30}(?:maintenance medium|infection medium|isolation medium|FBS reduced|without serum|serum-free|2% FBS|1% FBS|2% FCS|after adsorption).{0,180}"),
        ("ISOL", r".{0,40}(?:virus isolation|isolated from|tissue homogenate|clinical specimen|anal swab|nasopharyngeal|inoculated with).{0,200}"),
    ]:
        ms=list(re.finditer(rx, text, re.I))
        for m in ms[:2]:
            print(f"  {label}:", m.group(0)[:220].replace("\n"," "))
