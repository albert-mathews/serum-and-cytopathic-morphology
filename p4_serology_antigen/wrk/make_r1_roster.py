"""Generate p4_r1_roster.csv: one row per R1 isolation ref, classified for serology/antigen.

Reads r1's isolation-refs.csv; overlays the P4-coded serology classifications for the refs whose
full text is read in this repo (the _txt extracts + endpoint analysis). Everything else is marked
`unread` so the coverage is honest rather than guessed.
"""

import csv
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(REPO, "r1_isolation_standards_and_practice", "isolation-refs.csv")
OUT = os.path.join(REPO, "p4_serology_antigen", "p4_r1_roster.csv")

# ref_id -> (serology_reported, antigen_provenance)
READ = {
    "VI2": ("neutralization (CPE-suppression)", "culture-native"),
    "VI8": ("neutralization (patient sera)", "culture-native"),
    "VI13": ("none (plaque/qPCR)", "n/a"),
    "VI14": ("IFA", "culture-native"),
    "VI15": ("none (plaque/PCR)", "n/a"),
    "VI16": ("IFA/immunoperoxidase", "culture-native"),
    "VI18": ("HI + immunostaining", "culture-native"),
    "VI23": ("western blot", "culture-native"),
    "VI24": ("HA confirmation", "culture-native"),
    "VI25": ("immunostaining", "culture-native"),
    "VI28": ("none (CPE/qPCR)", "n/a"),
    "VI29": ("western blot (NP)", "culture-native"),
    "VI30": ("HA + IFA", "culture-native"),
    "VI32": ("IFA + HA", "culture-native"),
    "VI33": ("none (qPCR/NGS)", "n/a"),
    "VI34": ("IFA + HA + cross-neutralization", "culture-native"),
    "VI36": ("PRNT + western blot", "culture-native"),
    "VI38": ("immunostaining (anti-N MAb)", "recombinant (N protein MAb)"),
    "VI39": ("none (TCID50/qPCR)", "n/a"),
    "VI40": ("IFA (M2-1)", "culture-native"),
    "VI41": ("none (plaque)", "n/a"),
    "VI42": ("IFA + western blot", "culture-native"),
    "VI43": ("western blot + IFA", "culture-native"),
    "VI45": ("FAT/DFA", "culture-native"),
    "VI46": ("FAT", "culture-native"),
    "VI47": ("western blot (NP)", "culture-native"),
    "SPT10": ("IFA", "culture-native"),
}

rows = []
with open(SRC, newline="", encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        rid = (r.get("ID") or "").strip()
        if not rid:
            continue
        agent = (r.get("virus") or "").strip()
        if rid in READ:
            ser, prov = READ[rid]
            basis = "read"
        else:
            ser, prov, basis = "", "", "unread"
        rows.append([rid, agent, (r.get("access") or "").strip(), basis, ser, prov])

rows.sort(key=lambda x: x[0])
with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["ref_id", "agent", "access", "basis", "serology_reported", "antigen_provenance"])
    w.writerows(rows)

print(f"wrote {OUT}: {len(rows)} rows  "
      f"({sum(1 for r in rows if r[3]=='read')} read / {sum(1 for r in rows if r[3]!='read')} unread)")
