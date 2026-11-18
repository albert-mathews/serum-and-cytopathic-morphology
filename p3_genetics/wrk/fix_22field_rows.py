"""Fix rows with 22 fields (unquoted comma in the notes field) down to the correct 21.

For HSV2-O1 and HMPV-O1 the trailing `notes` field contained a comma and was not
quoted, so csv.reader split it into two fields (indices 20 and 21). Rejoin them
and emit a correctly-quoted line.
"""
import csv, io

PATH = "p3_genetics/sequence_origins/P3_sequence_origin_events.csv"
TARGETS = {"HSV2-O1", "HMPV-O1"}

# read all rows with quoting OFF to see raw field splits, then fix
with open(PATH, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

out = []
for ln in lines:
    first = ln.split(",")[0].strip() if ln else ""
    if first in TARGETS:
        fields = list(csv.reader([ln]))[0]
        # fields should be 22 -> merge last two into notes
        merged = fields[:20] + [fields[20] + "," + fields[21]]
        assert len(merged) == 21, f"{first}: got {len(merged)} after merge"
        buf = io.StringIO()
        csv.writer(buf, lineterminator="\n").writerow(merged)
        out.append(buf.getvalue().rstrip("\n"))
    else:
        out.append(ln)

with open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(out))

# verify
rows = list(csv.reader(open(PATH, encoding="utf-8")))
hdr = rows[0]
bad = [(r[0], len(r)) for r in rows[1:] if len(r) != len(hdr)]
print("header fields:", len(hdr))
print("rows with wrong field count:", bad if bad else "NONE (all aligned)")
print("total data rows:", len(rows) - 1)