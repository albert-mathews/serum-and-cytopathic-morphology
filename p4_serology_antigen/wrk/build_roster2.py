"""Merge the subagent classification back into a final p4_r1_roster.csv + p4_r1_wishlist.csv."""

import csv
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(REPO, "r1_isolation_standards_and_practice", "isolation-refs.csv")
CLS = os.path.join(REPO, "p4_serology_antigen", "wrk", "r1_classified.tsv")
ROSTER = os.path.join(REPO, "p4_serology_antigen", "p4_r1_roster.csv")
WISH = os.path.join(REPO, "p4_serology_antigen", "p4_r1_wishlist.csv")

# refs already coded in p4 (from make_r1_roster READ dict)
import importlib.util
spec = importlib.util.spec_from_file_location("mkr", os.path.join(os.path.dirname(__file__), "make_r1_roster.py"))
mkr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mkr)
READ = mkr.READ  # ref_id -> (serology, provenance)

# parse subagent classification
classified = {}   # ref_id -> (serology, provenance, mock)
inaccessible = {} # ref_id -> reason
with open(CLS, encoding="utf-8") as fh:
    for line in fh:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if parts[0] == "INACCESSIBLE":
            inaccessible[parts[1]] = parts[2] if len(parts) > 2 else "unspecified"
        else:
            rid, ser, prov, mock = parts[0], parts[1], parts[2], (parts[3] if len(parts) > 3 else "")
            classified[rid] = (ser, prov, mock)

rows, wish = [], []
with open(SRC, newline="", encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        rid = (r.get("ID") or "").strip()
        if not rid:
            continue
        agent = (r.get("virus") or "").strip()
        acc = (r.get("access") or "").strip()
        link = (r.get("link") or "").strip()
        if rid in READ:
            ser, prov = READ[rid]
            rows.append([rid, agent, acc, "classified", ser, prov, ""])
        elif rid in classified:
            ser, prov, mock = classified[rid]
            rows.append([rid, agent, acc, "classified", ser, prov, mock])
        elif rid in inaccessible:
            rows.append([rid, agent, acc, "wishlist", "INACCESSIBLE", "", ""])
            wish.append([rid, agent, acc, link, inaccessible[rid]])
        else:
            rows.append([rid, agent, acc, "wishlist", "", "", ""])
            wish.append([rid, agent, acc, link, "paywalled/abstract (no open full text)"])

rows.sort(key=lambda x: x[0])
wish.sort(key=lambda x: x[0])

with open(ROSTER, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["ref_id", "agent", "access", "status", "serology_reported", "antigen_provenance", "matched_mock"])
    w.writerows(rows)

with open(WISH, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["ref_id", "agent", "access", "link", "reason"])
    w.writerows(wish)

c = sum(1 for r in rows if r[3] == "classified")
w_ = sum(1 for r in rows if r[3] == "wishlist")
ser = sum(1 for r in rows if r[3] == "classified" and r[4] and r[4] != "none" and r[4] != "not-stated")
print(f"roster: {len(rows)} total | classified={c} wishlist={w_} | serology-reporting(classified)={ser}")
print(f"wishlist file: {len(wish)} rows")
