"""Fix the HDV-O1 row in P3_sequence_origin_events.csv.

The title contains commas and was never quoted, so the row parses as 25 fields
instead of 21. Rewrite that one raw line with proper CSV quoting.
"""
import csv, io

PATH = "p3_genetics/sequence_origins/P3_sequence_origin_events.csv"

# Correct 21-field content (commas inside fields will be quoted by csv writer).
fields = [
    "HDV-O1", "hepatitis_D", "hepatitis delta virus", "human delta agent (chimpanzee serum)",
    "origin", "1986", "Wang", "Structure, sequence and expression of the hepatitis delta (delta) viral genome",
    "Nature", "3762705", "10.1038/323508a0", "1678 nt circular RNA genome",
    "other", "chain_closed",
    "n/a - cloned directly from acute-phase chimpanzee serum (helper-dependent; no cell culture)",
    "no CPE - serum/animal-passage source, no monolayer culture in the resolved record",
    "Wang 1986 (OCR): 'HDV RNA was derived from the serum of a chimpanzee during acute HDV infection and the preparation procedure included incubation with an excess of proteinase K and phenol/chloroform extraction.'",
    "HDV chimpanzee transmission study (Rizzetto-era); Denniston 1986 Science companion",
    "user PDF (OCR'd)", "refs/P3-062_wang_1986_hdv.pdf",
    "CLOSED 2026-11-18 [VERIFIED src] via OCR: HDV genome cloned from acute-phase chimpanzee serum - animal-passage source, no culture, no CPE. path_score = other (same class as HCV chimpanzee plasma / HEV cyno). Helper-dependent (requires HBV). This was the last chain_open row - Step 1 now has 0 chain_open.",
]

# Build the correctly-quoted line.
buf = io.StringIO()
w = csv.writer(buf, lineterminator="\n")
w.writerow(fields)
new_line = buf.getvalue().rstrip("\n")

# Read raw lines, replace the HDV-O1 line, write back preserving other lines exactly.
with open(PATH, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

replaced = 0
out = []
for ln in lines:
    if ln.startswith("HDV-O1,"):
        out.append(new_line)
        replaced += 1
    else:
        out.append(ln)

# ensure no trailing empty line added
while out and out[-1] == "":
    out.pop()

with open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print(f"replaced {replaced} HDV-O1 line(s)")

# verify
rows = list(csv.reader(open(PATH, encoding="utf-8")))
hdv = [r for r in rows if r[0] == "HDV-O1"][0]
print("HDV-O1 field count now:", len(hdv))
print("path_score:", hdv[12], "| chain_status:", hdv[13])
