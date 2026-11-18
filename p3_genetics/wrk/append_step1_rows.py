"""Append new Step 1 provenance rows (HPV18, dengue 4, dengue 3) to P3_sequence_origin_events.csv."""
import csv, os

PATH = "p3_genetics/sequence_origins/P3_sequence_origin_events.csv"

# 20 columns: event_id,family,virus,strain,event_type,year,first_author,title,journal,pmid,doi,accession,path_score,chain_status,culture_system,cpe_evidence,sample_prep_quote,upstream_cites,access,pdf_local,notes
rows = [
    [
        "HPV18-O1","papillomavirus","human papillomavirus 18","HPV18 prototype (cervical carcinoma clone)",
        "origin","1987","Cole","Nucleotide sequence and comparative analysis of the human papillomavirus type 18 genome",
        "J Mol Biol","3039146","10.1016/0022-2836(87)90382-7","X05015","clinical_direct","chain_closed",
        "n/a - cloned directly from a cervical carcinoma (no culture step)",
        "no CPE (clinical-direct; no cell culture in the resolved record)",
        "Cole & Danos 1987: 'we have determined the complete nucleotide sequence of the HPV 18 genome, originally cloned from a cervical carcinoma of a Brazilian patient (Boshart et al.)'.",
        "Boshart et al. 1984 (HPV18 clone from cervical carcinoma)",
        "user PDF","refs/P3-061_cole_danos_1987_hpv18.pdf",
        "VISIT 2026-11-18: clinical_direct - same path as HPV16 (HPV-O1); cloned from cervical carcinoma biopsy, no culture. Closes the HPV18 bucket-3 lead. [VERIFIED src].",
    ],
    [
        "DEN4-O1","dengue","dengue virus type 4","dengue 4 (Caribbean strain 814669)",
        "origin","1987","Mackow","The nucleotide sequence of dengue type 4 virus: analysis of genes coding for nonstructural proteins",
        "Virology","3039728","10.1016/0042-6822(87)90458-2","M14931","culture_cpe","chain_closed",
        "LLC-MK2 (plaque-purified x2) then C6/36 (mosquito) for stock",
        "plaque-purified two times on LLC-MK2 (plaque = CPE-equivalent warrant)",
        "Mackow 1987: 'Dengue virus was plaque-purified two times on LLC-MK2 cells, a continuous simian cell line, prior to infection of C6/36 cells... Extracellular virus present in culture medium of C6/36 cells 6-7 days after infection was precipitated.'",
        "Russell & Nisalak 1967 (C6/36 stock); prototype 814669 Dominican Republic isolate",
        "user PDF","refs/P3-063_mackow_1987_dengue4.pdf",
        "VISIT 2026-11-18: culture_cpe - plaque purification is the CPE-equivalent warrant (protocol line 59); matches DEN-O1 (dengue 2) culture_cpe. [VERIFIED src].",
    ],
    [
        "DEN3-O1","dengue","dengue virus type 3","dengue 3 (strain H87)",
        "origin","1990","Osatomi","Complete nucleotide sequence of dengue type 3 virus genome RNA",
        "Virology","2345967","10.1016/0042-6822(90)90456-4","M93130","culture_no_cpe","chain_closed",
        "C6/36 (mosquito) cell suspension; no plaque/CPE stated in this O paper",
        "no CPE/plaque stated in the resolved record (C6/36 growth only)",
        "Osatomi 1990: 'DEN3 was inoculated into C6/36 cells suspension and virus was obtained from the infected fluid by the purification steps of PEG precipitation, ultracentrifugation, and linear sucrose gradient centrifugation.'",
        "Osatomi et al. 1988 (same purification scheme)",
        "user PDF","refs/P3-064_osatomi_1990_dengue3.pdf",
        "VISIT 2026-11-18: culture_no_cpe on the immediate record (no plaque stated). H87 prototype has a plaque/mouse lineage upstream (Hammon-era) - optional bucket-2 chase to upgrade to culture_cpe per protocol line 65. [VERIFIED src].",
    ],
]

with open(PATH, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)

print(f"appended {len(rows)} rows to {PATH}")

# verify
with open(PATH, newline="", encoding="utf-8") as f:
    allrows = list(csv.reader(f))
print("total rows:", len(allrows))
print("last 5 event_ids:", [r[0] for r in allrows[-5:]])
