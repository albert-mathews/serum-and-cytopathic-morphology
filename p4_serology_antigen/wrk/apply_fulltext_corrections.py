"""Apply the full-text corrections to p4_r1_roster.csv.

Adds a `fulltext_serology` column (the read-on-PDF classification), and drops the wishlist
(both R1's and P4's wishlists are empty — every ref PDF is in refs/isolation_practice/).
"""

import csv
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# full-text result for the serology-relevant subset: ref_id -> fulltext classification
# c = culture-native (confirmatory); r = recombinant (partial); x = clinical/kit (challenging);
# n = not serology after full-text read; - = not part of this read (leave empty)
FULLTEXT = {
    "VI74": "c", "VI101": "c", "VI121": "c", "VI205": "r", "VI228": "c", "VI244": "c",
    "VI281": "c", "VI289": "c", "VI294": "c", "VI103": "c", "VI114": "c", "VI229": "c",
    "VI108": "c", "VI104": "x", "VI97": "x", "VI71": "n", "VI232": "n", "VI218": "c",
}

ROSTER = os.path.join(REPO, "p4_serology_antigen", "p4_r1_roster.csv")
rows = list(csv.DictReader(open(ROSTER, encoding="utf-8-sig")))
with open(ROSTER, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["ref_id", "recipe", "agent", "access", "class",
                                        "primary_endpoint", "endpoint_sero",
                                        "sero_confirmation_webfetch", "matched_mock_webfetch",
                                        "fulltext_serology"])
    w.writeheader()
    for r in rows:
        ft = FULLTEXT.get(r["ref_id"], "")
        w.writerow({**r, "fulltext_serology": ft})

WISH = os.path.join(REPO, "p4_serology_antigen", "p4_r1_wishlist.csv")
with open(WISH, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["ref_id", "agent", "access", "link", "DOI", "status"])
    # wishlist is now empty — every PDF is in refs/isolation_practice/
    w.writerow(["", "", "", "", "", "empty — all R1 refs are readable in refs/isolation_practice/ (2026-11-11)"])

print("roster updated: fulltext_serology column added")
print("wishlist cleared")
