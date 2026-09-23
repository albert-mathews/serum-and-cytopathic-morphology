import csv, json, re
from pathlib import Path
from collections import Counter

root = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice")
exp = root / "expansion"

csv_files = list(exp.glob("*.csv")) + list(root.glob("*.csv"))
print("CSV files:", len(csv_files))

def norm_link(u):
    if not u:
        return ""
    u = u.strip().lower().rstrip("/")
    m = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", u)
    if m:
        return f"pmid:{m.group(1)}"
    m = re.search(r"ncbi\.nlm\.nih\.gov/pmc/articles/pmc(\d+)", u)
    if m:
        return f"pmc:{m.group(1)}"
    m = re.search(r"doi\.org/(10\.\S+)", u)
    if m:
        return "doi:" + m.group(1).rstrip("./")
    m = re.search(r"(10\.\d{4,9}/[-._;()/:A-Z0-9]+)", u, re.I)
    if m:
        return "doi:" + m.group(1).lower().rstrip("./")
    return u

def norm_doi(d):
    if not d:
        return ""
    d = d.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    d = re.sub(r"^doi:\s*", "", d)
    return d.rstrip("./")

keys = set()
by_src = {}
max_vi = 0
for p in csv_files:
    try:
        with open(p, encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                continue
            for r in reader:
                for fld in ("ID", "id", "vi_id"):
                    v = r.get(fld) or ""
                    m = re.search(r"VI(\d+)", str(v), re.I)
                    if m:
                        max_vi = max(max_vi, int(m.group(1)))
                link = r.get("link") or r.get("url") or r.get("URL") or ""
                doi = r.get("doi") or r.get("DOI") or ""
                nl = norm_link(link)
                nd = norm_doi(doi)
                if not nd and nl.startswith("doi:"):
                    nd = nl[4:]
                if nl:
                    keys.add(("link", nl))
                if nd:
                    keys.add(("doi", nd))
                blob = " ".join(str(v) for v in r.values() if v)
                for m in re.finditer(r"PMID[:\s]*(\d+)", blob, re.I):
                    keys.add(("link", f"pmid:{m.group(1)}"))
                for m in re.finditer(r"PMC(\d+)", blob, re.I):
                    keys.add(("link", f"pmc:{m.group(1).lower()}"))
                for m in re.finditer(r"\b(10\.\d{4,9}/[-._;()/:A-Z0-9]+)", blob, re.I):
                    keys.add(("doi", m.group(1).lower().rstrip("./")))
                by_src[p.name] = by_src.get(p.name, 0) + 1
    except Exception as e:
        print("ERR", p.name, e)

print("max_vi", max_vi)
print("n_keys", len(keys))
print("rows by file:")
for k, v in sorted(by_src.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")

with open(exp / "isolation-refs-dual-fbs_only.csv", encoding="utf-8-sig", newline="") as f:
    dual = list(csv.DictReader(f))
pat = Counter()
for r in dual:
    a = str(r["FBS% pre-inoculation"]).strip()
    b = str(r["FBS% post-inculcation"]).strip()
    pat[f"{a}->{b}"] += 1
print("Top patterns dual:")
for k, v in pat.most_common(25):
    print(f"  {k}: {v}")

# decade / virus mix
dec = Counter()
for r in dual:
    y = str(r.get("year") or "")
    m = re.search(r"(19|20)\d{2}", y)
    if m:
        decade = (int(m.group(0)) // 10) * 10
        dec[decade] += 1
print("Decades:", dict(sorted(dec.items())))

with open(exp / "_dedup_keys_repr.json", "w", encoding="utf-8") as f:
    json.dump({"max_vi": max_vi, "n_keys": len(keys), "keys": sorted([f"{a}|{b}" for a, b in keys])}, f)
print("wrote _dedup_keys_repr.json")
