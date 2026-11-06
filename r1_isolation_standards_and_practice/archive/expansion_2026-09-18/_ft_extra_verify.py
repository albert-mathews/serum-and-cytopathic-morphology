# -*- coding: utf-8 -*-
import json, urllib.request, re, time, ssl, html, sys, csv, shutil
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
BATCH="expansion_2026-09-18_representative"

def fetch_ft(pmcid):
    pmcid=str(pmcid).replace("PMC","")
    try:
        with urllib.request.urlopen(f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmcid}/fullTextXML", context=ctx, timeout=45) as r:
            return r.read().decode("utf-8","replace")
    except Exception:
        return None

def strip(xml):
    t=re.sub(r"<[^>]+>"," ", xml); t=html.unescape(t); return re.sub(r"\s+"," ", t)

# Verify key extras
for pmc in ["10083141","11143356","11852709","13056563","13426916","12502754"]:
    xml=fetch_ft(pmc); time.sleep(0.15)
    if not xml:
        print("NOFT", pmc); continue
    text=strip(xml)
    title=re.sub(r"<[^>]+>","", re.search(r"<article-title[^>]*>(.*?)</article-title>", xml, re.I|re.S).group(1))
    year=re.search(r"<year>(\d{4})</year>", xml)
    doi=re.search(r'<article-id pub-id-type="doi">(10\.[^<]+)</article-id>', xml)
    pmid=re.search(r'<article-id pub-id-type="pmid">(\d+)</article-id>', xml)
    print(f"\n### PMC{pmc} | {year.group(1) if year else ''} | PMID{pmid.group(1) if pmid else ''} | {doi.group(1) if doi else ''}")
    print(title[:90])
    for lab,rx in [
        ("G", r".{0,20}(?:growth medium|grown|maintained|cultured|propagated).{0,140}?\d+(?:\.\d+)?\s*%\s*(?:FBS|FCS|fetal).{0,40}"),
        ("M", r".{0,20}(?:maintenance|infection|FBS reduced|2% FBS|1% FBS|5% FBS|after adsorption).{0,160}"),
        ("I", r".{0,30}(?:isolat(?:ed|ion) from|clinical specimen|patient sample|tissue homogenate).{0,160}"),
    ]:
        ms=list(re.finditer(rx, text, re.I))[:2]
        for m in ms:
            print(f" {lab}:", m.group(0)[:200])
