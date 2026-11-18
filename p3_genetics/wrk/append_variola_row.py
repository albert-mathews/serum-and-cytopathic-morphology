"""Append the variola (VAR-O1) Step 1 row to P3_sequence_origin_events.csv."""
import csv

PATH = "p3_genetics/sequence_origins/P3_sequence_origin_events.csv"

row = [
    "VAR-O1","poxvirus","variola virus","smallpox variola major Bangladesh-1975 (VAR-BSH)",
    "origin","1994","Massung","Analysis of the complete genome of smallpox variola major virus strain Bangladesh-1975",
    "Virology","8184534","10.1006/viro.1994.1188","L22579","other","chain_closed",
    "chick chorioallantoic membrane (CAM) of 12-day eggs, pock-picked, then chick embryo fibroblast (CEF) passage; DNA from second CEF passage",
    "no monolayer CPE - egg CAM 'pock' + CEF; poxvirus egg/embryo route, not cell-culture CPE",
    "Massung 1994 (OCR): 'Virus was isolated from scab material from the last naturally occurring case of variola major in the world... in Kuralia, South Dingaldi, Bhola Island, Bangladesh (Fenner et al., 1988). Virus was grown on the chorioallantoic membrane (CAM) of 12-day-old fertile eggs, and a single pock was picked for passaging virus into chick embryo fibroblast (CEF) cells. Virus DNA was prepared from the second [CEF passage].'",
    "Fenner et al. 1988 (Bangladesh smallpox eradication, WHO); variola major Bangladesh-1975 isolate",
    "user PDF (OCR'd)","refs/P3-066_massung_1994_variola.pdf",
    "ADDED 2026-11-18 [VERIFIED src] via OCR: variola reference genome is egg/CEF-derived (CAM 'pock' + chick embryo fibroblast passage), NOT monolayer CPE. path_score = other (eggs/animal route, parallel to influenza PR8 eggs / YFV-17D). Closes the variola bucket-3 lead.",
]

with open(PATH, "a", newline="", encoding="utf-8") as f:
    csv.writer(f, lineterminator="\n").writerow(row)

rows = list(csv.reader(open(PATH, encoding="utf-8")))
hdr = rows[0]
bad = [(r[0], len(r)) for r in rows[1:] if len(r) != len(hdr)]
print("total data rows:", len(rows)-1)
print("bad field-count rows:", bad if bad else "NONE")
var = [r for r in rows if r[0] == "VAR-O1"][0]
print("VAR-O1 path_score:", var[12], "| chain:", var[13])