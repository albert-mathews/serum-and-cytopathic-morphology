# -*- coding: utf-8 -*-
import urllib.request, re, ssl, html, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx=ssl.create_default_context()
for pmc in ["10083141","11143356"]:
    with urllib.request.urlopen(f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmc}/fullTextXML", context=ctx, timeout=45) as r:
        xml=r.read().decode("utf-8","replace")
    text=re.sub(r"<[^>]+>"," ", xml); text=html.unescape(text); text=re.sub(r"\s+"," ", text)
    print("====", pmc, "len", len(text))
    # all FBS percent mentions with context
    for m in re.finditer(r".{0,100}\d+(?:\.\d+)?\s*%\s*(?:FBS|fetal bovine|foetal).{0,100}", text, re.I):
        print("-", m.group(0)[:220])
    print("---isolation---")
    for m in re.finditer(r".{0,80}(?:isolat|inoculat|clinical specimen|maintenance|infection medium).{0,160}", text, re.I):
        if re.search(r"FBS|fetal|serum|% ", m.group(0), re.I):
            print("*", m.group(0)[:240])
