"""Rebuild p4_r1_roster.csv from the REVISED isolation-refs.csv (184 rows).

The revision added authoritative endpoint columns from a full PDF re-read:
  class (1 = CPE detection/Isolate endpoint; 4 = 2I1D serum pattern + OTHER endpoint)
  endpoint_CPE_detection_isolate, endpoint_titration_TCID50, endpoint_antigen_detection,
  endpoint_neutralization, endpoint_plaque, endpoint_hemagglutination_hemadsorption,
  endpoint_molecular, endpoint_purification, endpoint_characterization

P4 is about serology/antigen provenance. Two distinct serology signals are now separable:
  (a) serology/antigen as a PRIMARY/co ENDPOINT  -> endpoint_antigen_detection /
      endpoint_neutralization / endpoint_hemagglutination_hemadsorption = yes
  (b) serology/antigen as CONFIRMATION of a CPE isolate -> carried in the webfetch
      classification (r1_classified.tsv) as the method-level finding.

This builder joins (a) from the revised CSV and (b) from r1_classified.tsv, and outputs a
roster with: ref_id, recipe, agent, access, class, primary_endpoint, endpoint_sero (agg of a),
sero_method_confirmation (from b), and matched_mock (from b where read).
"""

import csv
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(REPO, "r1_isolation_standards_and_practice", "isolation-refs.csv")
CLS = os.path.join(REPO, "p4_serology_antigen", "wrk", "r1_classified.tsv")
OUT = os.path.join(REPO, "p4_serology_antigen", "p4_r1_roster.csv")

# (a) authoritative endpoint serology flags from revised CSV
SERO_ENDPOINT_COLS = [
    "endpoint_antigen_detection",
    "endpoint_neutralization",
    "endpoint_hemagglutination_hemadsorption",
]

# (b) webfetch confirmation classification (ref_id -> serology, provenance, mock)
confirm = {}
with open(CLS, encoding="utf-8") as fh:
    for line in fh:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if parts[0] == "INACCESSIBLE":
            continue
        if len(parts) >= 3:
            confirm[parts[0]] = (parts[1], parts[2], parts[3] if len(parts) > 3 else "")

rows_out = []
with open(SRC, newline="", encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        rid = (r.get("ID") or "").strip()
        if not rid:
            continue
        recipe = (r.get("recipe") or "").strip()
        agent = (r.get("virus") or "").strip()
        acc = (r.get("access") or "").strip()
        cls = (r.get("class") or "").strip()
        primary = (r.get("primary_endpoint") or "").strip()
        # (a) endpoint-level serology flags
        ep_flags = []
        for c in SERO_ENDPOINT_COLS:
            if r.get(c) == "yes":
                ep_flags.append(c.replace("endpoint_", "").replace("hemagglutination_hemadsorption", "hemagglutination"))
        endpoint_sero = "+".join(ep_flags) if ep_flags else ""
        # (b) confirmation-level (webfetch) method + mock
        csero = cmock = ""
        if rid in confirm:
            csero = confirm[rid][0]
            cmock = confirm[rid][2]
        rows_out.append([rid, recipe, agent, acc, cls, primary, endpoint_sero, csero, cmock])

rows_out.sort(key=lambda x: (x[0], x[1]))
with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["ref_id", "recipe", "agent", "access", "class", "primary_endpoint",
                "endpoint_sero", "sero_confirmation_webfetch", "matched_mock_webfetch"])
    w.writerows(rows_out)

# report
total = len(rows_out)
cls1 = sum(1 for r in rows_out if r[4] == "1")
cls4 = sum(1 for r in rows_out if r[4] == "4")
endpoint_sero = sum(1 for r in rows_out if r[6])
webfetch_sero = sum(1 for r in rows_out if r[7] and r[7] not in ("none", "not-stated", "INACCESSIBLE"))
print(f"roster rebuilt: {total} rows | class1={cls1} class4={cls4}")
print(f"  endpoint-level serology (a): {endpoint_sero} rows")
print(f"  webfetch confirmation serology (b): {webfetch_sero} rows")
