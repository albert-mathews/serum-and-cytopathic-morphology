# -*- coding: utf-8 -*-
import json, urllib.request, re, time, ssl, html, sys, csv
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ctx = ssl.create_default_context()
exp = Path(r"C:\Users\alber\Documents\virus\bechamp institute\PLOS bio\serum-and-cytopathic-morphology\r1_isolation_standards_and_practice\expansion")
root = exp.parent

def fetch_ft(pmcid):
    pmcid=str(pmcid).replace("PMC","")
    url=f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{pmcid}/fullTextXML"
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=45) as r:
            return r.read().decode("utf-8","replace")
    except Exception:
        return None

def strip(xml):
    t=re.sub(r"<[^>]+>"," ", xml); t=html.unescape(t); return re.sub(r"\s+"," ", t)

# verify hantavirus + SARS cats growth details
for pmc in ["11376573","13119600","7512137"]:
    xml=fetch_ft(pmc); time.sleep(0.2)
    text=strip(xml)
    title=re.sub(r"<[^>]+>","", re.search(r"<article-title[^>]*>(.*?)</article-title>", xml, re.I|re.S).group(1))
    print("====", pmc, title[:80])
    for m in re.finditer(r".{0,40}(?:growth|maintenance|FBS|fetal|isolation|homogenate|inoculat).{0,180}", text, re.I):
        s=m.group(0)
        if re.search(r"\d+\s*%|without serum|serum-free|trypsin", s, re.I):
            print(" ", s[:240])
            if sum(1 for _ in re.finditer(r"\d+\s*%", s))>=0:
                pass
        if m.start()>15000 and "isolation" in s.lower() and "FBS" in s:
            break

# Build coded candidates (manual verified dual only)
# Schema matches power_expansion_candidates
BATCH="expansion_2026-09-18_representative"
rows=[]

def add(**kw):
    rows.append(kw)

add(ID="VI272", year="2026", virus="Ranavirus micropterus1 (McRV)", cells="BF-2", base="L-15", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.3389/fvets.2026.1829414", access="oa",
    notes="Ornamental wrasse tissue homogenate isolation per WOAH Aquatic Manual ranavirus procedures. Growth L15+10% FBS; before inoculation replaced with L15+2% FBS. | lang=en; thread=aquatic ranavirus isolation; pattern=10->2",
    quote_pre="BF-2 cells were seeded ... using growth medium (10% FBS/L15)",
    quote_post="Before inoculation, the growth medium was replaced with maintenance medium (L15 + 2% FBS 1X Anti-anti, Gibco)",
    dual_ok="True", upserted="True", thread="aquatic / fish virus isolation", lang="en")

add(ID="VI273", year="2026", virus="Betanodavirus / NNV (gonad diagnostics)", cells="RTG-2 (luc)", base="L-15", pre="10", post="2",
    pen="100", strep="10", amph="",
    link="https://doi.org/10.1007/s00248-026-02733-2", access="oa",
    notes="Greater amberjack gonad homogenate inoculation on RTG-2 reporter cells. RTG growth L-15+10% FBS; after adsorption maintenance medium 2% FBS. pen 100 U/ml; strep 10 mg/ml as stated. | lang=en; thread=aquatic nodavirus; pattern=10->2",
    quote_pre="RTG-growth medium which consisted on Leibovitz (L-15) medium ... supplemented with 10% foetal bovine serum (FBS)",
    quote_post="After 1-h of adsorption, 750 uL of maintenance medium (2% FBS) were added to each well",
    dual_ok="True", upserted="True", thread="aquatic / fish virus isolation", lang="en")

add(ID="VI274", year="2021", virus="IBDV (LC-75 Vero adaptation)", cells="Vero", base="DMEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.2147/VMRR.S326479", access="oa",
    notes="Ethiopia NVI Vero cell adaptation of IBDV vaccine strain; DMEM+10% FCS growth; after adsorption DMEM+2% FCS. FCS coded as FBS-equivalent fetal calf serum. Field challenge isolate used in efficacy. | lang=en; thread=veterinary vaccine adaptation; pattern=10->2",
    quote_pre="DMEM ... supplemented with 10% FCS (Gibco) ... Dulbecco's Modified Eagle's Medium (DMEM) with 10% and 2% sterile fetal calf serum (FCS) was used as a growth and maintenance medium",
    quote_post="After 1 hr incubation, 10mL DMEM with 2% FCS was added into an infected flask",
    dual_ok="True", upserted="True", thread="veterinary vaccine / IBDV", lang="en")

add(ID="VI275", year="2025", virus="PPRV (in vitro isolation from domestic/wild ruminants)", cells="Vero; SEK", base="DMEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.3390/v17091231", access="oa",
    notes="In vitro virus isolation from blood/tissues/discharges; Vero and SEK cultured DMEM+10% FBS; after washes fresh maintenance DMEM+2% FBS. Blind passages if no CPE. Distinct from prior Gujarat PPRV / CDC measles. | lang=en; thread=PPRV veterinary isolation; pattern=10->2",
    quote_pre="Vero and SEK, were also cultured in DMEM with the addition of 10% FBS and the same antibiotic supplementation",
    quote_post="fresh maintenance medium (DMEM with 2% FBS and antibiotics) was added",
    dual_ok="True", upserted="True", thread="PPRV veterinary isolation", lang="en")

add(ID="VI276", year="2024", virus="Mammalian orthoreovirus (bat MRV2)", cells="Vero; SH-SY5Y; HepG2", base="DMEM / RPMI", pre="10", post="0",
    pen="", strep="", amph="",
    link="https://doi.org/10.1128/spectrum.01762-23", access="oa",
    notes="Newly isolated bat-origin MRV; cells grown DMEM/RPMI+10% FBS; after absorption maintenance medium is basal+TBP/YE/trypsin WITHOUT FBS (serum-free trypsin MM). Pattern 10->0. | lang=en; thread=bat reovirus isolation; pattern=10->0",
    quote_pre="cultured in DMEM plus 10% FBS (growth media); ... RPMI 1640 medium plus 10% FBS (growth media)",
    quote_post="After 2-h absorption, the fresh maintenance medium was added (DMEM supplemented with 0.3% TBP, 0.02% YE, and 4 ug/ml trypsin) [no FBS]",
    dual_ok="True", upserted="True", thread="bat / reovirus isolation", lang="en")

add(ID="VI277", year="2024", virus="Duck enteritis virus (DEV field outbreak)", cells="CEF", base="DMEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.1080/01652176.2024.2350668", access="oa",
    notes="DEV/India/IVRI-2016 isolated from Kerala outbreak field samples; CEF grown DMEM+10% FBS; post-infection DMEM MM+2% FBS. | lang=en; thread=avian herpesvirus isolation; pattern=10->2",
    quote_pre="CEF cell monolayers were grown ... in Dulbecco's modified Eagle's medium (DMEM) ... supplemented with 10% fetal bovine serum (FBS)",
    quote_post="replaced with DMEM maintenance medium containing 2% FBS",
    dual_ok="True", upserted="True", thread="avian herpesvirus / DEV", lang="en")

add(ID="VI278", year="2024", virus="Fowl adenovirus 8a (FAdV-8a)", cells="LMH", base="DMEM", pre="10", post="1",
    pen="", strep="", amph="",
    link="https://doi.org/10.1016/j.heliyon.2024.e26578", access="oa",
    notes="FAdV-8a CY21 isolated from livers of infected chickens; LMH grown DMEM+10% FBS; after adsorption maintenance medium 1% FBS. Non-classic 10->1. | lang=en; thread=avian adenovirus isolation; pattern=10->1",
    quote_pre="grown in Dulbecco's Modified Eagle Medium (DMEM) ... supplemented with 10% fetal bovine serum (FBS)",
    quote_post="5 mL of maintenance medium containing 1% fetal bovine serum (FBS) was added",
    dual_ok="True", upserted="True", thread="avian adenovirus", lang="en")

add(ID="VI279", year="2026", virus="Getah virus (GETV) from diseased piglets", cells="Vero; N2a", base="DMEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.1080/21505594.2026.2714605", access="oa",
    notes="Natural GETV variant isolated from brain of diseased piglets; cells maintained DMEM+10% FBS; post-inoculation DMEM+2% FBS. Alphavirus clinical/field isolation. | lang=en; thread=arbovirus / alphavirus isolation; pattern=10->2",
    quote_pre="N2a ... cells were maintained in Dulbecco's Modified Eagle Medium (DMEM) ... supplemented with 10% fetal bovine serum (FBS)",
    quote_post="Cells were then maintained in 500 uL of DMEM supplemented with 2% FBS",
    dual_ok="True", upserted="True", thread="arbovirus / GETV", lang="en")

add(ID="VI280", year="2026", virus="PEDV (intestinal tissue isolation)", cells="Vero", base="DMEM", pre="10", post="0",
    pen="", strep="", amph="",
    link="https://doi.org/10.1155/tbed/1340053", access="oa",
    notes="Two PEDV strains isolated from PEDV-positive intestinal tissues. Vero maintained DMEM+10% FBS; after adsorption washed with serum-free DMEM and maintenance medium containing trypsin (no FBS). Pattern 10->0. | lang=en; thread=PEDV veterinary isolation; pattern=10->0",
    quote_pre="Vero cells were maintained in Dulbecco's modified Eagle's medium (DMEM) ... supplemented with 10% fetal bovine serum (FBS)",
    quote_post="After adsorption ... inoculum was removed, cells were washed twice with serum-free DMEM, and maintenance medium containing 5 ug/mL trypsin was added [no FBS]",
    dual_ok="True", upserted="True", thread="PEDV veterinary isolation", lang="en")

add(ID="VI281", year="2026", virus="Hepatitis E virus (retail pork pate)", cells="A549-D3", base="MEM", pre="5", post="5",
    pen="", strep="", amph="",
    link="https://doi.org/10.3390/v18070760", access="oa",
    notes="EQUAL-HOLD 5->5. A549-D3 cultured in MEM+5% FBS; after inoculation infection medium still 5% FBS (+DMSO). Foodborne HEV infectivity detection/isolation attempt. | lang=en; thread=HEV food isolation; pattern=5->5",
    quote_pre="Cells were cultured in maintenance medium: Minimal Essential Medium (MEM) ... supplemented with 5% fetal bovine serum (FBS)",
    quote_post="maintained in infection medium (maintenance medium supplemented with 2% dimethyl sulfoxide (DMSO) and 5% FBS)",
    dual_ok="True", upserted="True", thread="HEV food / clinical culture", lang="en")

add(ID="VI282", year="2016", virus="Ebola virus outbreak variants (Mayinga/Kikwit/Makona)", cells="VeroE6", base="DMEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.1038/srep38293", access="oa",
    notes="Outbreak-variant Ebola stocks cultured for disinfection study. Explicit: growth DMEM+10% FBS; virus maintenance medium same with FBS reduced to 2%. Distinct DOI from prior EBOV Makona row. | lang=en; thread=filovirus culture practice; pattern=10->2",
    quote_pre="VeroE6 cells ... were propagated in growth media consisting of Dulbecco's modified eagle medium (DMEM) ... which included 10% Fetal Bovine Serum (FBS)",
    quote_post="For virus culture, virus maintenance medium was the same as growth medium with FBS reduced to 2%",
    dual_ok="True", upserted="True", thread="filovirus / Ebola culture", lang="en")

add(ID="VI283", year="2024", virus="PRRSV-2 (Marc-145 culture after inoculation)", cells="Marc-145", base="DMEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.3389/fvets.2024.1439015", access="oa",
    notes="Marc-145/Vero cultured DMEM+10% FBS; after 2-h PRRSV inoculation fresh medium +2% FBS. Lab strains but explicit dual practice pattern used in PRRSV culture. | lang=en; thread=PRRSV culture practice; pattern=10->2",
    quote_pre="Marc-145 cells and Vero cells were cultured in Dulbecco's modified Eagle's medium (DMEM) ... with 10% FBS",
    quote_post="Following a 2-h inoculation with PRRSV, the inoculum was removed ... Subsequently, fresh medium supplemented with 2% FBS was added",
    dual_ok="True", upserted="True", thread="PRRSV culture practice", lang="en")

add(ID="VI284", year="2025", virus="Negevirus (mosquito isolation)", cells="C6/36; Aag2; BHK-21; Vero E6", base="RPMI 1640 / DMEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.1186/s12985-025-02961-x", access="oa",
    notes="Novel negevirus strains from mosquito collections. Insect cells RPMI+10% FBS; after inoculation maintenance RPMI/DMEM+2% FBS. | lang=en; thread=insect / negevirus isolation; pattern=10->2",
    quote_pre="C6/36 and Aag2 cells were maintained ... in Roswell Park Memorial Institute (RPMI) 1640 medium containing 10% fetal bovine serum (FBS)",
    quote_post="was removed and replaced with maintenance medium (RPMI 1640 for C6/36 and DMEM for mammalian cells) containing 2% FBS",
    dual_ok="True", upserted="True", thread="insect virus / negevirus", lang="en")

add(ID="VI285", year="2026", virus="SARS-CoV-2 (feline primary isolation)", cells="Vero E6", base="DMEM", pre="4", post="4",
    pen="", strep="", amph="",
    link="https://doi.org/10.3390/vetsci13040374", access="oa",
    notes="EQUAL-HOLD 4->4. Primary isolation from PCR-positive cats; viruses propagated in DMEM maintenance medium with 4% FBS. Text also notes 5% for some maintenance formulations; coded 4->4 from explicit primary-isolation propagation statement. | lang=en; thread=SARS feline isolation; pattern=4->4",
    quote_pre="Viruses were propagated in a 24 h monolayer culture with DMEM maintenance medium (with 4% FBS)",
    quote_post="For primary isolation, the infected cell cultures were monitored until day... [same DMEM maintenance medium with 4% FBS]",
    dual_ok="True", upserted="True", thread="SARS feline clinical isolation", lang="en")

add(ID="VI286", year="2025", virus="Feline parvovirus (FPV) from anal swab", cells="CRFK", base="DMEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.3389/fmicb.2025.1658838", access="oa",
    notes="FPV013 isolated from anal swab of cat with panleukopenia; CRFK cultured DMEM+10% FBS; post-inoculation maintenance DMEM+2% FBS. | lang=en; thread=feline parvovirus isolation; pattern=10->2",
    quote_pre="cultured in Dulbecco's Modified Eagle Medium (DMEM) supplemented with 10% fetal bovine serum (FBS)",
    quote_post="maintenance medium (DMEM + 2% FBS + 1% penicillin-streptomycin) was added to each well",
    dual_ok="True", upserted="True", thread="feline parvovirus", lang="en")

add(ID="VI287", year="2022", virus="SARS-CoV-2 (clinical swab isolation Alpha)", cells="Vero-E6-TMPRSS2", base="DMEM", pre="10", post="2.5",
    pen="", strep="", amph="",
    link="https://doi.org/10.1172/jci.insight.155944", access="oa",
    notes="Clinical patient swab isolation on Vero-E6-TMPRSS2. Complete media DMEM+10% FBS; infection medium identical with FBS reduced to 2.5%. Non-classic 10->2.5. | lang=en; thread=SARS clinical isolation; pattern=10->2.5",
    quote_pre="Vero-E6-TMPRSS2 cells ... were cultured in complete media (CM) consisting of DMEM containing 10% FBS",
    quote_post="infection medium (IM), which is identical to CM but with the FBS reduced to 2.5%, and 150 uL of the viral transport media containing a swab from a patient",
    dual_ok="True", upserted="True", thread="SARS clinical isolation", lang="en")

add(ID="VI288", year="2020", virus="Cyprinid herpesvirus-2 (CyHV-2)", cells="FtGF", base="L-15", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.7717/peerj.9373", access="oa",
    notes="CyHV-2 isolation from diseased goldfish tissue homogenate on FtGF line. Cells routinely passaged L-15+10% FBS; after adsorption maintenance L-15+2% FBS. | lang=en; thread=aquatic herpesvirus isolation; pattern=10->2",
    quote_pre="The cell line has been passaged up to 56 times in L-15 with 10% FBS",
    quote_post="After 1 h adsorption, 6.5 mL of the maintenance medium (L-15 medium with 2% FBS) was added to the FtGF flasks",
    dual_ok="True", upserted="True", thread="aquatic herpesvirus / CyHV-2", lang="en")

add(ID="VI289", year="2026", virus="Japanese encephalitis virus (JEV) culture", cells="Vero", base="DMEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://doi.org/10.3390/v18080850", access="oa",
    notes="JEV genotype strains (historical mosquito/pig isolates) cultured for HA antigen. Cells DMEM+10% FBS; after inoculation maintenance 2% FBS. Practice dual for flavivirus culture. | lang=en; thread=flavivirus / JEV culture; pattern=10->2",
    quote_pre="were cultured in Dulbecco's modified Eagle's medium supplemented with 10% fetal bovine serum and 1% antibiotics",
    quote_post="the inoculum was replaced with a maintenance medium containing 2% fetal bovine serum",
    dual_ok="True", upserted="True", thread="flavivirus / JEV", lang="en")

add(ID="VI290", year="2024", virus="Influenza A (tissue homogenate MDCK isolation)", cells="MDCK", base="DMEM", pre="5", post="0",
    pen="", strep="", amph="",
    link="https://doi.org/10.1080/22221751.2024.2387449", access="oa",
    notes="IAV isolation from pig tissue homogenates on MDCK. Cells maintained DMEM+5% FBS; virus maintenance medium is DMEM+albumin/vitamins/antibiotics+TPCK-trypsin (no FBS). Pattern 5->0. | lang=en; thread=influenza serum-free MM; pattern=5->0",
    quote_pre="MDCK cells were maintained in Dulbecco's Modified Eagle Medium (DMEM) ... supplemented with 5% fetal bovine serum (FBS)",
    quote_post="virus maintenance medium (DMEM supplemented with 0.3% bovine albumin serum, 1% MEM vitamin, 1% antibiotic-antimycotic, and 1 ug/mL TPCK-treated trypsin) [no FBS]",
    dual_ok="True", upserted="True", thread="influenza isolation MDCK", lang="en")

add(ID="VI291", year="2024", virus="Orthohantavirus (genetic variants isolation)", cells="Vero E6", base="MEM", pre="10", post="2",
    pen="", strep="", amph="",
    link="https://pmc.ncbi.nlm.nih.gov/articles/PMC11376573/", access="oa",
    notes="Isolation and characterization of Orthohantavirus genetic variants. Cells grown MEM+10% FBS; after inoculation replaced with maintaining media MEM+2% FBS. | lang=en; thread=hantavirus isolation; pattern=10->2",
    quote_pre="grown in the minimal essential medium (MEM) ... containing 10% fetal bovine",
    quote_post="replaced with 5 mL fresh maintaining media (MEM+2% FBS)",
    dual_ok="True", upserted="True", thread="hantavirus isolation", lang="en")

# Optional additional from detail: TMUV 10->2 weaker - skip
# SARS cats carefully kept as 4->4

print("candidates", len(rows))
pat=Counter(f"{r['pre']}->{r['post']}" for r in rows)
print("patterns", dict(pat.most_common()))

# Write candidate CSV
fields=["ID","year","virus","cells*","Base Medium","FBS% pre-inoculation","FBS% post-inculcation","penicillin (IU/ml)","streptomycin (mg/ml)","amphotericin (mg/ml)","link","access","notes","quote_pre","quote_post","source_batch","dual_ok","upserted","thread","lang"]
out_rows=[]
for r in rows:
    out_rows.append({
        "ID":r["ID"],"year":r["year"],"virus":r["virus"],"cells*":r["cells"],"Base Medium":r["base"],
        "FBS% pre-inoculation":r["pre"],"FBS% post-inculcation":r["post"],
        "penicillin (IU/ml)":r["pen"],"streptomycin (mg/ml)":r["strep"],"amphotericin (mg/ml)":r["amph"],
        "link":r["link"],"access":r["access"],"notes":r["notes"],
        "quote_pre":r["quote_pre"],"quote_post":r["quote_post"],
        "source_batch":BATCH,"dual_ok":r["dual_ok"],"upserted":r["upserted"],"thread":r["thread"],"lang":r["lang"],
    })

cand_path=exp/"representative_expansion_candidates_2026-09-18.csv"
with open(cand_path,"w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f, fieldnames=fields)
    w.writeheader(); w.writerows(out_rows)
print("wrote", cand_path)

# Upsert into expanded + rebuild dual
exp_csv=exp/"isolation-refs-overview_expanded.csv"
dual_csv=exp/"isolation-refs-dual-fbs_only.csv"
# backup
import shutil, datetime
ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
shutil.copy2(exp_csv, exp/f"isolation-refs-overview_expanded.csv.bak_repr_{ts}")
shutil.copy2(dual_csv, exp/f"isolation-refs-dual-fbs_only.csv.bak_repr_{ts}")

core_fields=["ID","year","virus","cells*","Base Medium","FBS% pre-inoculation","FBS% post-inculcation","penicillin (IU/ml)","streptomycin (mg/ml)","amphotericin (mg/ml)","link","access","notes","quote_pre","quote_post","source_batch"]

with open(exp_csv,encoding="utf-8-sig",newline="") as f:
    expanded=list(csv.DictReader(f))
before_exp=len(expanded)
before_dual=sum(1 for r in expanded if str(r.get("FBS% pre-inoculation","")).strip() and str(r.get("FBS% post-inculcation","")).strip()
                and re.search(r"\d", str(r.get("FBS% pre-inoculation",""))) and re.search(r"\d", str(r.get("FBS% post-inculcation",""))))

# existing IDs
exist_ids={r["ID"] for r in expanded}
added=0
for r in out_rows:
    if r["ID"] in exist_ids:
        print("SKIP exist id", r["ID"]); continue
    # dual numeric check
    if not (re.search(r"\d", r["FBS% pre-inoculation"]) and re.search(r"\d", r["FBS% post-inculcation"])):
        print("SKIP non-dual", r["ID"]); continue
    expanded.append({k:r.get(k,"") for k in core_fields})
    added+=1

with open(exp_csv,"w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f, fieldnames=core_fields)
    w.writeheader(); w.writerows(expanded)

# rebuild dual: rows with both numeric
dual=[]
for r in expanded:
    a=str(r.get("FBS% pre-inoculation") or "").strip()
    b=str(r.get("FBS% post-inculcation") or "").strip()
    if re.search(r"\d", a) and re.search(r"\d", b):
        dual.append({k:r.get(k,"") for k in core_fields})
with open(dual_csv,"w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f, fieldnames=core_fields)
    w.writeheader(); w.writerows(dual)

print(f"expanded {before_exp} -> {len(expanded)} (added {added})")
print(f"dual ~{before_dual} -> {len(dual)}")
pat2=Counter()
for r in out_rows:
    pat2[f"{r['FBS% pre-inoculation']}->{r['FBS% post-inculcation']}"] += 1
print("new patterns", dict(pat2))
n_10_2=pat2.get("10->2",0)
n_other=sum(v for k,v in pat2.items() if k!="10->2")
print(f"new 10->2={n_10_2} other={n_other}")
