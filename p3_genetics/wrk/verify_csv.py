import csv
from collections import Counter

rows = list(csv.reader(open("p3_genetics/sequence_origins/P3_sequence_origin_events.csv", encoding="utf-8")))
hdr = rows[0]
assert len(hdr) == 21, f"header not 21: {len(hdr)}"
bad = [(r[0], len(r)) for r in rows[1:] if len(r) != 21]
print("CSV integrity: header=21 fields; bad rows =", bad if bad else "NONE")

d = list(csv.DictReader(open("p3_genetics/sequence_origins/P3_sequence_origin_events.csv", encoding="utf-8")))
print("events:", len(d), "| chain_closed:", sum(1 for r in d if r["chain_status"] == "chain_closed"))
print("path_score:", dict(Counter(r["path_score"] for r in d)))
for nid in ["HPV18-O1", "DEN3-O1", "DEN4-O1", "VAR-O1", "HDV-O1"]:
    r = [x for x in d if x["event_id"] == nid][0]
    print(f"  {nid}: path_score={r['path_score']}  chain={r['chain_status']}  pmid={r['pmid']}")