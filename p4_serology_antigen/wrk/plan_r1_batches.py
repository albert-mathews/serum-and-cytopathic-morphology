"""Build the P4 processing plan for R1 refs: local vs web vs wishlist.

Emits batch list files under wrk/ that the subagents read, and prints a summary.
"""

import csv
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(REPO, "r1_isolation_standards_and_practice", "isolation-refs.csv")
WRK = os.path.dirname(os.path.abspath(__file__))

MAIN_TXT = os.path.join(REPO, "r1_isolation_standards_and_practice", "refs", "isolation_practice", "_txt")
ARCH_TXT = os.path.join(REPO, "r1_isolation_standards_and_practice", "archive", "expansion_2026-09-18", "_pdf_extract_tmp")

# refs already classified in p4_r1_roster (the READ dict lives in make_r1_roster.py)
import importlib.util
spec = importlib.util.spec_from_file_location("mkr", os.path.join(WRK, "make_r1_roster.py"))
mkr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mkr)
READ = mkr.READ

def local_path(rid):
    # a text extract starting with the ref id in either folder
    for folder in (MAIN_TXT, ARCH_TXT):
        if os.path.isdir(folder):
            for f in os.listdir(folder):
                if f.startswith(rid) and f.lower().endswith((".txt", ".md")):
                    return os.path.join(folder, f)
    return None

rows = []
with open(SRC, newline="", encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        rid = (r.get("ID") or "").strip()
        if not rid:
            continue
        if rid in READ:
            continue  # already classified
        acc = (r.get("access") or "").strip()
        virus = (r.get("virus") or "").strip()
        link = (r.get("link") or "").strip()
        srcb = (r.get("source_batch") or "").strip()
        lp = local_path(rid)
        if lp:
            action = "local"
        elif acc == "oa":
            action = "web"
        else:  # abstract, paywall_needed, legacy_coded without extract
            action = "wishlist"
        rows.append([rid, virus, acc, srcb, link, action, lp or ""])

rows.sort(key=lambda x: x[0])

# write plan; then split
with open(os.path.join(WRK, "r1_processing_plan.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["ref_id", "virus", "access", "source_batch", "link", "action", "local_path"])
    w.writerows(rows)

local = [r for r in rows if r[5] == "local"]
web = [r for r in rows if r[5] == "web"]
wish = [r for r in rows if r[5] == "wishlist"]

def dump(path, data, cols):
    with open(path, "w", encoding="utf-8") as fh:
        for r in data:
            line = "\t".join(r[i] for i in cols)
            fh.write(line + "\n")

dump(os.path.join(WRK, "r1_batch_local.txt"), local, [0, 1, 6])          # id, virus, localpath
dump(os.path.join(WRK, "r1_batch_wishlist.txt"), wish, [0, 1, 2, 4])    # id, virus, access, link
# split web into 4 equal shards
k = max(1, len(web) // 4 + (1 if len(web) % 4 else 0))
for i in range(4):
    dump(os.path.join(WRK, f"r1_batch_web_{i+1}.txt"), web[i*k:(i+1)*k], [0, 1, 4])

print(f"total unprocessed: {len(rows)}  (local={len(local)}, web={len(web)}, wishlist={len(wish)})")
