import csv
from pathlib import Path

# --- Screened updates ---
rows = list(csv.DictReader(open("P1_screened.csv", encoding="utf-8")))
fields = list(rows[0].keys())
by = {r["id"]: r for r in rows}


def set_y(rid, reason, notes, year="", short=""):
    if rid not in by:
        by[rid] = {
            "id": rid,
            "year": year,
            "short_cite": short,
            "lead_source": "user_pdf",
            "useful": "Y",
            "reason": reason,
            "fulltext": "Y",
            "round": "9",
            "notes": notes,
        }
    else:
        by[rid]["useful"] = "Y"
        by[rid]["fulltext"] = "Y"
        by[rid]["reason"] = reason
        by[rid]["notes"] = ((by[rid].get("notes") or "") + "; " + notes).strip("; ")
        by[rid]["round"] = "9"
        if year:
            by[rid]["year"] = year
        if short:
            by[rid]["short_cite"] = short


set_y(
    "P1-006",
    "Melnick 1955 methods; lactalbumin + 2% calf serum; isolation CPE",
    "Full PDF Round 9",
    "1955",
    "Melnick Ann NY Acad Sci 1955 tissue culture techniques polio orphan",
)
set_y(
    "P1-034",
    "Morgan Morton Parker 1950 Medium 199 synthetic medium foundation",
    "Full PDF Round 9",
    "1950",
    "Morgan Morton Parker Nutrition animal cells synthetic medium 199",
)
set_y(
    "P1-042",
    "Li Schaeffer 1953 Medium E plasma hydrolysate; horse serum inhibitory",
    "Full PDF Round 9",
    "1953",
    "Li Schaeffer Science 1953 simplified polio tissue culture",
)
set_y(
    "P1-043",
    "Melnick Opton assay; nutrient medium + 2.0% calf serum; lactalbumin base",
    "Full PDF Round 9",
    "1956",
    "Melnick Opton WHO assay polio neutralizing antibody plastic panels",
)
set_y(
    "P1-205",
    "Schmidt AJCP 1972 diagnostic TC review; isolation CPE; bibliography leads",
    "Full PDF user Round 9",
    "1972",
    "Schmidt Tissue Culture Laboratory Diagnosis Viral Infections AJCP",
)
set_y(
    "P1-206",
    "Melnick 1953 growth 10% bovine serum+199; wash; serum-free maintenance 199+Earle",
    "Full PDF Round 9",
    "1953",
    "Melnick PSGBM 1953 poliomyelitis virus tissue culture dry tube bottle",
)

leads = [
    (
        "P1-045",
        "1952",
        "Weller Enders Robbins Stoddard methods 1952",
        "round9_snowball",
        "B",
        "Cited by Melnick 1955; Enders-group methods",
        "N",
        "9",
        "Lead from P1-006 refs",
    ),
    (
        "P1-046",
        "1953",
        "Youngner Ward Salk monkey testis culture methods",
        "round9_snowball",
        "B",
        "Cited by Li 1953 and Melnick",
        "N",
        "9",
        "Lead from P1-042",
    ),
    (
        "P1-047",
        "1953",
        "Scherer Syverton Gey HeLa J Exp Med 1953",
        "round9_snowball",
        "B",
        "HeLa continuous line foundational",
        "N",
        "9",
        "Lead from P1-206",
    ),
    (
        "P1-048",
        "1958",
        "Baron Low New Maintenance Medium Cell Culture Science 1958",
        "round9_snowball",
        "B",
        "Schmidt cites new maintenance medium Science 1958",
        "N",
        "9",
        "Related P1-019",
    ),
    (
        "P1-049",
        "1961",
        "Hayflick Moorhead human diploid Exp Cell Res 1961",
        "round9_snowball",
        "B",
        "Diploid strain standard; Schmidt 1972 cites",
        "N",
        "9",
        "Lead from P1-205",
    ),
    (
        "P1-050",
        "1952",
        "Robbins Weller Enders J Immunol 1952 cultivation methods",
        "round9_snowball",
        "B",
        "Enders group methods cited Melnick 1953",
        "N",
        "9",
        "Lead from P1-206",
    ),
]
for L in leads:
    by[L[0]] = {
        "id": L[0],
        "year": L[1],
        "short_cite": L[2],
        "lead_source": L[3],
        "useful": L[4],
        "reason": L[5],
        "fulltext": L[6],
        "round": L[7],
        "notes": L[8],
    }

ordered = sorted(by.values(), key=lambda r: r["id"])
with open("P1_screened.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in ordered:
        w.writerow({k: r.get(k, "") for k in fields})

# --- Useful ---
urows = list(csv.DictReader(open("P1_useful.csv", encoding="utf-8")))
ufields = list(urows[0].keys())
uby = {r["id"]: r for r in urows}


def up(d):
    uby[d["id"]] = {k: d.get(k, "") for k in ufields}


up(
    {
        "id": "P1-006",
        "year": "1955",
        "authors": "Melnick JL",
        "title": "Tissue culture techniques and their application to original isolation, growth, and assay of poliomyelitis and orphan viruses",
        "citation": "Ann N Y Acad Sci. 1955;61:754-773",
        "document_type": "primary_methods",
        "virus_or_agent": "poliomyelitis and orphan viruses",
        "culture_system": "trypsinized monkey kidney tubes bottles",
        "cell_or_tissue": "monkey kidney epithelial",
        "enrichment_propagation": "0.5% lactalbumin hydrolysate + 2% calf serum + 97.5% Hanks BSS",
        "enrichment_infection_or_observation": "After inoculum replace with lactalbumin medium (Earle solution); observe CPE days 2-10",
        "enrichment_change": "yes",
        "change_timing": "after inoculum replace fluid",
        "rationale_quoted": "Inexpensive simple medium for trypsinized cells",
        "endpoint": "CPE isolation typing neutralization",
        "comparison_of_media": "yes",
        "uninoculated_under_same_medium": "unclear",
        "quotes_medium": "0.5 per cent lactalbumin enzymatic hydrolysate, 2 per cent calf serum, and 97.5 per cent Hank's salt solution. After inoculum replaced with fresh lactalbumin hydrolysate medium in Earle's solution.",
        "quotes_endpoint": "cytopathic changes induced by the presence of the virus on 2nd 4th 7th 10th days",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-21",
        "confidence": "high",
        "notes": "Cites Diagnostic Procedures 2nd ed; Melnick-Riordan 1952",
    }
)

up(
    {
        "id": "P1-034",
        "year": "1950",
        "authors": "Morgan JF, Morton HJ, Parker RC",
        "title": "Nutrition of Animal Cells in Tissue Culture. I. Initial Studies on a Synthetic Medium",
        "citation": "Proc Soc Exp Biol Med. 1950;73:1-8",
        "document_type": "primary_methods",
        "virus_or_agent": "NA (chick embryo cells; Medium 199 foundation)",
        "culture_system": "roller tube chick embryo muscle",
        "cell_or_tissue": "11-day chick embryo leg muscle",
        "enrichment_propagation": "Seek synthetic medium without serum/embryo extract; often preliminary horse serum + embryo extract then synthetic",
        "enrichment_infection_or_observation": "NA virus",
        "enrichment_change": "yes experimental",
        "change_timing": "after 3-5 days preliminary natural medium",
        "rationale_quoted": "Complexity and variability of natural substrates (plasma serum extracts) impede nutrient studies",
        "endpoint": "cell survival multiplication",
        "comparison_of_media": "yes",
        "uninoculated_under_same_medium": "NA",
        "quotes_medium": "synthetic medium... in the absence of blood serum and embryo extract. Although a completely adequate synthetic mixture has not yet been achieved... preliminary feeding mixture containing horse serum and embryo extract",
        "quotes_endpoint": "cell growth microscopic examination",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-21",
        "confidence": "high",
        "notes": "Medium 199 origin; later used with serum for virus TC growth",
    }
)

up(
    {
        "id": "P1-042",
        "year": "1953",
        "authors": "Li CP, Schaeffer M",
        "title": "A Simplified Method for Cultivation of Poliomyelitis Virus in Tissue Culture",
        "citation": "Science. 1953;118:107-109",
        "document_type": "primary_methods",
        "virus_or_agent": "poliomyelitis",
        "culture_system": "stationary monkey testicular tissue tubes",
        "cell_or_tissue": "monkey testis",
        "enrichment_propagation": "Medium E: 75% Hank-Simms + 25% bovine plasma hydrolysate; Simms ultrafiltrate optional/omittable",
        "enrichment_infection_or_observation": "same Medium E; fewer medium changes; clearer CPE; less nonspecific degeneration in uninfected tissue",
        "enrichment_change": "yes vs horse serum + embryo extract",
        "change_timing": "replacement of prior medium components",
        "rationale_quoted": "Horse serum frequently inhibitory to virus; chick embryo extracts contamination sources",
        "endpoint": "cytopathogenic effect degrees of degeneration",
        "comparison_of_media": "yes",
        "uninoculated_under_same_medium": "yes",
        "quotes_medium": "Horse serum is frequently inhibitory to virus, and chick embryo extracts are at times sources of contamination. Medium E... 75% Hank-Simms... and 25% bovine plasma hydrolyzate. Simms serum ultrafiltrate may be omitted entirely. nonspecific degeneration does not readily occur in uninfected tissue",
        "quotes_endpoint": "cytopathogenic effect... degrees of cellular degeneration",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-21",
        "confidence": "high",
        "notes": "Cites Melnick-Riordan lactalbumin; Youngner Ward Salk",
    }
)

up(
    {
        "id": "P1-043",
        "year": "1956",
        "authors": "Melnick JL, Opton EM",
        "title": "Assay of poliomyelitis neutralizing antibody in disposable plastic panels",
        "citation": "Bull World Health Organ (PMC2538105)",
        "document_type": "primary_methods",
        "virus_or_agent": "poliomyelitis",
        "culture_system": "plastic panel metabolic color test monkey kidney",
        "cell_or_tissue": "monkey kidney",
        "enrichment_propagation": "Simple lactalbumin hydrolysate medium; nutrient medium = lactalbumin-Hanks base + 2.0% calf serum",
        "enrichment_infection_or_observation": "same simple medium for color assay",
        "enrichment_change": "partial (199 replaced by lactalbumin+2% calf)",
        "change_timing": "medium choice for assay system",
        "rationale_quoted": "Substitute simple lactalbumin medium for more complex Connaught No. 199",
        "endpoint": "metabolic color/pH phenol red",
        "comparison_of_media": "yes",
        "uninoculated_under_same_medium": "yes",
        "quotes_medium": "simple lactalbumin hydrolysate medium is used. The nutrient medium, used for cell suspensions and cell titrations, is prepared by adding 2.0% calf serum. substitution of the simple lactalbumin hydrolysate medium for the more complex media like Connaught No. 199",
        "quotes_endpoint": "colour test... acid products of metabolism lower the pH of the medium",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-21",
        "confidence": "high",
        "notes": "Confirms 2% calf serum nutrient medium mid-1950s",
    }
)

up(
    {
        "id": "P1-205",
        "year": "1972",
        "authors": "Schmidt NJ",
        "title": "Tissue Culture in the Laboratory Diagnosis of Viral Infections",
        "citation": "Am J Clin Pathol. 1972;57:820-828 approx",
        "document_type": "review",
        "virus_or_agent": "diagnostic viruses",
        "culture_system": "diagnostic TC overview",
        "cell_or_tissue": "diploid MK continuous",
        "enrichment_propagation": "not primary recipe source",
        "enrichment_infection_or_observation": "isolation CPE; micro methods save medium",
        "enrichment_change": "unclear",
        "change_timing": "n/a",
        "rationale_quoted": "none detailed for serum percent",
        "endpoint": "CPE isolation; intersecting serum pools",
        "comparison_of_media": "no",
        "uninoculated_under_same_medium": "unclear",
        "quotes_medium": "micro tests require about one-tenth of the amounts of cells and medium used for tube cultures",
        "quotes_endpoint": "isolation of viruses; CPE diagnostic practice",
        "window_status": "end_marker late secondary",
        "extractor": "grok-primary",
        "extract_date": "2026-07-21",
        "confidence": "medium",
        "notes": "Bibliography leads: Hayflick diploid, etc.",
    }
)

up(
    {
        "id": "P1-206",
        "year": "1953",
        "authors": "Melnick JL",
        "title": "Poliomyelitis Virus in Tissue Culture (dry-tube and bottle culture methods)",
        "citation": "Proc Soc Exp Biol Med. 1953;84:558-563 approx",
        "document_type": "primary_methods",
        "virus_or_agent": "poliomyelitis",
        "culture_system": "monkey kidney on glass stationary tubes bottles",
        "cell_or_tissue": "monkey kidney epithelial",
        "enrichment_propagation": "Complete medium: 9 parts Medium 199 + 1 part bovine serum (10%); 10% serum with 199 satisfactory for outgrowth (Fig 3)",
        "enrichment_infection_or_observation": "Remove complete medium; wash Earle salt solution remove inhibitors in bovine serum; maintenance = 1 part 199 + 1 part Earle salt solution (serum-free)",
        "enrichment_change": "yes",
        "change_timing": "after 10-14 days epithelial sheet before virus",
        "rationale_quoted": "Wash removes poliomyelitis virus inhibitory substances present in bovine serum",
        "endpoint": "cytopathogenic effect",
        "comparison_of_media": "yes serum percent and fluid depth",
        "uninoculated_under_same_medium": "unclear",
        "quotes_medium": "Complete medium... 9 parts of mixture No. 199 and 1 part bovine serum. washed with Earle's salt solution (to remove poliomyelitis virus inhibitory substances present in bovine serum)... maintenance medium consisting of 1 part of No. 199 and 1 part of Earle's salt solution. concentrations of 10% when used with No. 199 were satisfactory for good outgrowth.",
        "quotes_endpoint": "reaction to virus (cytopathogenic effect)",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-21",
        "confidence": "high",
        "notes": "Key dual-medium primary: 10% growth then serum-free maintenance + inhibitor wash",
    }
)

ordered = sorted(uby.values(), key=lambda r: r["id"])
with open("P1_useful.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ufields, extrasaction="ignore")
    w.writeheader()
    for r in ordered:
        w.writerow({k: r.get(k, "") for k in ufields})

print("screened", len(list(csv.DictReader(open("P1_screened.csv", encoding="utf-8")))))
print("useful", len(ordered))
print([r["id"] for r in ordered])
