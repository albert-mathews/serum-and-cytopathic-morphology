import csv
from pathlib import Path

rows = list(csv.DictReader(open("P1_useful.csv", encoding="utf-8")))
fields = list(rows[0].keys())
by_id = {r["id"]: r for r in rows}


def upsert(d):
    by_id[d["id"]] = d


upsert(
    {
        "id": "P1-001",
        "year": "1949",
        "authors": "Enders JF, Weller TH, Robbins FC",
        "title": "Cultivation of the Lansing strain of poliomyelitis virus in cultures of various human embryonic tissues",
        "citation": "Science. 1949;109(2822):85-87",
        "document_type": "primary_methods",
        "virus_or_agent": "poliomyelitis Lansing",
        "culture_system": "suspended tissue fragments",
        "cell_or_tissue": "human embryonic arm/leg intestine brain; premature infant tissues",
        "enrichment_propagation": "balanced salt solution 3 parts + ox serum ultrafiltrate 1 part (25% ultrafiltrate by volume)",
        "enrichment_infection_or_observation": "same fluid system; serial subculture with dilution",
        "enrichment_change": "no",
        "change_timing": "NA - single fluid type described",
        "rationale_quoted": "none_stated",
        "endpoint": "virus multiplication (mouse/monkey infectivity); later CPE lineage",
        "comparison_of_media": "no",
        "uninoculated_under_same_medium": "unclear",
        "quotes_medium": "The cultures consisted of tissue fragments suspended in 3 cc of a mixture of balanced salt solution (3 parts) and ox serum ultrafiltrate (1 part).",
        "quotes_endpoint": "multiplication of the virus in this medium has been comparable to that in the other types",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-20",
        "confidence": "high",
        "notes": "Full PDF re-extract from p1_history/refs; confirms Nobel lecture medium description",
    }
)

upsert(
    {
        "id": "P1-002",
        "year": "1950",
        "authors": "Robbins FC, Enders JF, Weller TH",
        "title": "Cytopathogenic effect of poliomyelitis viruses in vitro on human embryonic tissues",
        "citation": "Proc Soc Exp Biol Med. 1950;75 (as in PDF)",
        "document_type": "primary_methods",
        "virus_or_agent": "poliomyelitis Lansing Brunhilde",
        "culture_system": "suspended cell flask + plasma hanging drop + roller tube",
        "cell_or_tissue": "human embryonic skin-muscle",
        "enrichment_propagation": "Hanks-Simms 1:3 for suspended cultures; flask medium 9 parts Hanks-Simms + 1 part beef embryo extract; plasma drop: fowl plasma + chick + beef embryo extracts; pen/strep in medium",
        "enrichment_infection_or_observation": "same systems; fresh medium every 3-5 days; antiserum experiments",
        "enrichment_change": "no formal growth-vs-maintenance percent; medium replenishment",
        "change_timing": "supernatant removed and fresh medium added on indicated days",
        "rationale_quoted": "none_stated",
        "endpoint": "cytopathogenic effect; cell migration failure; pH differential vs controls",
        "comparison_of_media": "no",
        "uninoculated_under_same_medium": "yes",
        "quotes_medium": "The medium used in these experiments consisted of 9 parts of the Hanks-Simms solution adopted as routine for the suspended cell cultures (1:3) and 1 part of beef embryo extract. Plasma hanging drop: 2 drops heparinized fowl plasma, one drop chick embryo extract and one drop beef embryo extract.",
        "quotes_endpoint": "cytopathogenic effect; specific inhibition by immune serum of the cytopathogenic effect; normal monkey serum fails to protect the cells against the cytopathogenic action of the virus",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-20",
        "confidence": "high",
        "notes": "Full PDF; pH and migration controls; immune serum protection",
    }
)

upsert(
    {
        "id": "P1-005",
        "year": "1954",
        "authors": "Dulbecco R, Vogt M",
        "title": "Plaque formation and isolation of pure lines with poliomyelitis viruses",
        "citation": "J Exp Med. 1954;99:167-182",
        "document_type": "primary_methods",
        "virus_or_agent": "poliomyelitis types 1-3",
        "culture_system": "monolayer primary monkey kidney",
        "cell_or_tissue": "monkey kidney monolayers",
        "enrichment_propagation": "Earle saline 8 parts + horse serum 6 parts + chicken embryo extract 3 parts",
        "enrichment_infection_or_observation": "Agar overlay: 2.7% agar + neutral red + 4x Earle saline + embryo extract (no horse serum listed in overlay parts)",
        "enrichment_change": "yes",
        "change_timing": "after monolayer formation; infection under agar overlay",
        "rationale_quoted": "none_stated as modern FBS reduction",
        "endpoint": "plaques PFU pure line isolation",
        "comparison_of_media": "partial",
        "uninoculated_under_same_medium": "yes",
        "quotes_medium": "Tissue Culture Fluid.--Earle's saline (ES), 8 parts, horse serum, 6 parts, chicken embryo extract (1:1 in ES), 3 parts. Overlay consisted of 12 parts 2.7 per cent agar, 12 parts neutral red solution, 8 parts fourfold Earle's saline, and 5 parts of embryo extract.",
        "quotes_endpoint": "Plaques have been produced with the three types of poliomyelitis viruses",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-20",
        "confidence": "high",
        "notes": "Full PDF; rich horse-serum growth fluid vs serum-not-listed plaque overlay",
    }
)

upsert(
    {
        "id": "P1-015",
        "year": "1969approx",
        "authors": "Moffat MAJ",
        "title": "Some Cell Culture Procedures in Diagnostic Medical Virology",
        "citation": "Diagnostic methods chapter (PDF supplied)",
        "document_type": "manual",
        "virus_or_agent": "diagnostic viruses general",
        "culture_system": "monolayer tube roller Petri",
        "cell_or_tissue": "MK HeLa HEp-2 amnion RK13 etc",
        "enrichment_propagation": "199 or Eagle Basal Medium + 10% calf serum",
        "enrichment_infection_or_observation": "maintenance medium 1% serum or serum-free after about 3 days",
        "enrichment_change": "yes",
        "change_timing": "after about 3 days",
        "rationale_quoted": "none_stated",
        "endpoint": "CPE neutralization hemadsorption FA",
        "comparison_of_media": "no",
        "uninoculated_under_same_medium": "unclear",
        "quotes_medium": "Growth medium usually consists of a synthetic medium such as 199 or Eagle's Basal Medium with added 10% calf serum. The serum may be varied in type or amount according to the virus or cells being cultured. After about 3 days the cultures are changed to maintenance medium which may contain 1% serum or be serum-free. Antibiotics are usually included.",
        "quotes_endpoint": "cytopathogenic effect (CPE) was produced in the cells by the virus",
        "window_status": "end_marker",
        "extractor": "grok-primary",
        "extract_date": "2026-07-20",
        "confidence": "high",
        "notes": "Full PDF re-extract; dual medium diagnostic prescription",
    }
)

upsert(
    {
        "id": "P1-017",
        "year": "1961",
        "authors": "Subramanyam P et al",
        "title": "Cultivation of vaccinia virus in sheep kidney cell cultures",
        "citation": "Bull World Health Organ (PMC2555548)",
        "document_type": "primary_methods",
        "virus_or_agent": "vaccinia Barnes strain",
        "culture_system": "primary sheep kidney monolayers",
        "cell_or_tissue": "sheep kidney",
        "enrichment_propagation": "HBSS 80% + sheep serum 20% + lactalbumin 0.5% + yeast extract 0.1%",
        "enrichment_infection_or_observation": "EBSS + 10% sheep serum maintenance; used for virus inoculation",
        "enrichment_change": "yes",
        "change_timing": "after monolayer 6-9 days then virus inoculum on maintenance",
        "rationale_quoted": "none_stated",
        "endpoint": "cytopathic effects serial passage",
        "comparison_of_media": "no",
        "uninoculated_under_same_medium": "unclear",
        "quotes_medium": "growth medium consisting of HBSS, 80%; sheep serum, 20%; lactalbumin hydrolysate, 0.5%; yeast extract, 0.1%. After good monolayer formation, usually 6 to 9 days after the preparation of the cultures, the medium was replaced with a maintenance medium consisting of EBSS with 10% sheep serum, the concentration of other substances being the same as in the growth medium. This medium was used for virus inoculation.",
        "quotes_endpoint": "examined for cytopathic effects every 24 hours. After the lapse of 5 days, when the cytopathic effects were at a maximum",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-20",
        "confidence": "high",
        "notes": "COUNTEREXAMPLE: maintenance still 10% serum (growth was 20%)",
    }
)

upsert(
    {
        "id": "P1-200",
        "year": "1961",
        "authors": "Smith SE",
        "title": "A Maintenance Medium for Tissue Culture Virus Studies",
        "citation": "Br J Exp Pathol. 1961 (PDF brjexppathol00357-0048)",
        "document_type": "primary_methods",
        "virus_or_agent": "poliovirus and others on monkey kidney",
        "culture_system": "primary monkey kidney and others",
        "cell_or_tissue": "monkey kidney; various",
        "enrichment_propagation": "lactalbumin hydrolysate medium with added serum (cells usually grown)",
        "enrichment_infection_or_observation": "liver digest ultrafiltrate 5-10% in Earle BSS; serum-free maintenance for polio titration up to 12 days; vaccine safety testing up to 28 days serum-free",
        "enrichment_change": "yes",
        "change_timing": "maintenance medium for virus studies after growth",
        "rationale_quoted": "keep infected cells healthy without inhibitory effect on virus; growth media not generally suitable; better than lactalbumin+serum growth medium or SM199 for maintenance; crude digest less satisfactory especially in medium with low serum content",
        "endpoint": "virus titration; long maintenance",
        "comparison_of_media": "yes",
        "uninoculated_under_same_medium": "unclear",
        "quotes_medium": "special requirement for a type of medium usually referred to as maintenance medium. The liver digest is used at a 10 per cent dilution in Earle's balanced salt solution to form the basic maintenance medium. For titrations of poliovirus the cultures are kept on a serum free medium for periods of up to 12 days from infection. cells are usually grown on a lactalbumin hydrolysate medium with added serum.",
        "quotes_endpoint": "maintenance for virus titration and safety testing of poliomyelitis vaccine up to 28 days",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-20",
        "confidence": "high",
        "notes": "User-supplied as P1-200; defines serum-free maintenance vs serum growth",
    }
)

upsert(
    {
        "id": "P1-201",
        "year": "1961",
        "authors": "Hsiung GD",
        "title": "Applications of Primary Cell Cultures in the Study of Animal Viruses",
        "citation": "Yale J Biol Med. 1961;33:359-371",
        "document_type": "review",
        "virus_or_agent": "enteroviruses polio Coxsackie ECHO and others",
        "culture_system": "primary kidney monolayers plaque and fluid",
        "cell_or_tissue": "primate and non-primate kidney",
        "enrichment_propagation": "not single recipe; review of systems",
        "enrichment_infection_or_observation": "agar overlay factors: bicarbonate amino acids serum proteins lactalbumin; 2% horse serum can inhibit plaques; protein-free synthetic overlay discussed",
        "enrichment_change": "discussed as variable",
        "change_timing": "overlay vs fluid culture",
        "rationale_quoted": "serum inhibitors of plaque formation; lactalbumin can accelerate some ECHO plaques",
        "endpoint": "plaques; CPE fluid culture",
        "comparison_of_media": "yes",
        "uninoculated_under_same_medium": "unclear",
        "quotes_medium": "2 percent horse serum from certain horses when added to the overlay caused inhibition of 90 percent of the plaques produced by poliovirus type 1. protein-free synthetic overlay medium. addition of lactalbumin hydrolysate in the overlay medium",
        "quotes_endpoint": "certain ECHO viruses produced plaques under agar overlay but were incapable of producing cytopathic changes in parallel fluid cultures",
        "window_status": "in_window",
        "extractor": "grok-primary",
        "extract_date": "2026-07-20",
        "confidence": "high",
        "notes": "User-supplied as P1-201; serum as inhibitor supports low/no-serum logic",
    }
)

ordered = sorted(by_id.values(), key=lambda r: r["id"])
# normalize: only known fields; drop None keys
clean = []
for r in ordered:
    clean.append({k: (r.get(k) or "") for k in fields})
with open("P1_useful.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(clean)
print("useful rows", len(clean))
print([r["id"] for r in clean])
