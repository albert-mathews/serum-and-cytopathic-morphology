#!/usr/bin/env python3
"""Score the 25 pending R1 category-1 papers and append to the R2 overview.

Reads each PDF once (text already extracted to wrk/_pending_txt/), applies the
A-D framework (control-cultures.md), and appends 25 rows to
r2_negative_controls/control-cultures-overview.csv.

Scoring basis per paper is documented in the `notes` field and key quotes
in control-cultures-justification-notes.md (Pass5 section).

Regenerate:  tools/venv/Scripts/python r2_negative_controls/wrk/score_pending_25.py
"""
from __future__ import annotations
import csv
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OV = REPO / "r2_negative_controls" / "control-cultures-overview.csv"

# one row per pending paper; core 22 fields (id,tier,c_reason,nc_any,...,notes)
ROWS = [
    # --- class 1 ---
    dict(id="VI98", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="SINUV Isolation from mosquito homogenates on C6/36 (blind passage)",
         endpoint_for_control_comparison="CPE",
         notes="Uninfected C6/36 cells appear only as IFAT assay control (Fig.3b using HMAF), not a parallel Isolation-stage NC."),
    dict(id="VI100", tier="C", c_reason="C-stage", nc_any="yes", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="HAdV-7 Isolation from throat swabs on HEp-2 (neutralization/ELISA follow-up)",
         endpoint_for_control_comparison="CPE",
         notes="Positive and negative controls only in the neutralization assay (wrong stage); 'healthy controls' = human subjects, not cultures."),
    dict(id="VI102", tier="B", c_reason="NA", nc_any="yes", nc_isolation_stage="yes",
         m1="yes", m2="yes", m3="unknown", m4="unknown", m5="unknown", m6="unknown", match_basis="NA",
         control_cpe_reported="yes", control_cpe_claimed_negative="yes", control_images="no",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="CxFV Isolation from mosquito homogenates on C6/36 (3 blind passages)",
         endpoint_for_control_comparison="CPE",
         notes="'Mild CPE observed in all cultures with the exception of mock-infected control cultures' (results only); mock preparation/medium (L15+2% FBS) not methods-defined -> B."),
    dict(id="VI104", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="PRCV (1Q90) re-isolation from pig tissues on ST cells",
         endpoint_for_control_comparison="syncytia / CPE",
         notes="'No virus isolated from the control piglets' = animal arm, not a culture NC; no mock/uninfected ST culture described."),
    dict(id="VI106", tier="C", c_reason="C-stage", nc_any="yes", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="HAdV-11a Isolation from throat swabs on HEp-2",
         endpoint_for_control_comparison="CPE",
         notes="Positive and negative controls only in the neutralization assay; 'control population' = human serum samples, not cultures."),
    dict(id="VI107", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="Enterovirus isolation from wastewater/fecal in parallel cell systems",
         endpoint_for_control_comparison="CPE / plaque",
         notes="'Control on virus content of specimens' = verification inoculation, not a negative culture NC."),
    dict(id="VI113", tier="C", c_reason="C-stage", nc_any="yes", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="Enterovirus/adenovirus/reovirus isolation from sewage effluent (roller phials)",
         endpoint_for_control_comparison="CPE",
         notes="'Simultaneous virus titration and suitable controls' only in the microneutralization/typing step (wrong stage)."),
    dict(id="VI116", tier="B", c_reason="NA", nc_any="yes", nc_isolation_stage="yes",
         m1="yes", m2="yes", m3="yes", m4="unknown", m5="unknown", m6="yes", match_basis="NA",
         control_cpe_reported="yes", control_cpe_claimed_negative="yes", control_images="yes",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="C. difficile toxin cytotoxic effect vs viral CPE (HFDL/CMK microtiter)",
         endpoint_for_control_comparison="CPE / cytotoxicity",
         notes="Uninoculated HFDL/CMK cells (Fig.1B,D) = no-inoculum morphology baseline in 2% FBS maintenance; figure-only (not a methods-described parallel mock) -> B."),
    dict(id="VI117", tier="A", c_reason="NA", nc_any="yes", nc_isolation_stage="yes",
         m1="yes", m2="yes", m3="yes", m4="yes", m5="yes", m6="yes", match_basis="allowed_inference",
         control_cpe_reported="yes", control_cpe_claimed_negative="partial", control_images="no",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="Miniature (1-dr vial) cell-culture virus infection for field Isolation",
         endpoint_for_control_comparison="CPE / yield",
         notes="'Comparable uninfected cultures were maintained as controls' (Methods) in L-15+1% FCS. Uninfected stored monolayers spontaneously degenerate over days-weeks (rounding, abnormal morphology, detachment) in 1-2% FCS maintenance with no virus (Table 1) - matches protocol CPE descriptors (detachment, nonspecific degeneration); the paper attributes it to storage/aging, not virus."),
    dict(id="VI120", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="Bovine adenovirus types 4/7 isolation and propagation in calf testicle cells",
         endpoint_for_control_comparison="CPE",
         notes="No culture-level mock/uninfected NC described."),
    # --- class 4 ---
    dict(id="VI97", tier="A", c_reason="NA", nc_any="yes", nc_isolation_stage="yes",
         m1="yes", m2="yes", m3="yes", m4="yes", m5="yes", m6="yes", match_basis="allowed_inference",
         control_cpe_reported="yes", control_cpe_claimed_negative="yes", control_images="no",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="BHV-1 isolation from clinical swab on MDBK (gC subtyping follow-up)",
         endpoint_for_control_comparison="CPE",
         notes="'MDBK cells without sample inoculation was also incubated as control' in DMEM+2% FBS maintenance (universal medium statement). class=4 (R1): molecular subtyping primary endpoint, but isolation arm has matched uninoculated control."),
    dict(id="VI101", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="Shell vial vs conventional enterovirus/adenovirus detection from fecal specimens",
         endpoint_for_control_comparison="IF / CPE",
         notes="'no cells in shell vial culture' = cell culture failure, not a negative control."),
    dict(id="VI103", tier="C", c_reason="C-stage", nc_any="yes", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="IBDV mutant selection under immune pressure + chicken pathogenicity",
         endpoint_for_control_comparison="titer / animal",
         notes="TCID50 'cell control' (last column, no virus) + 'uninoculated/sham' chicken groups = wrong stage (titration/animal), no Isolation-stage culture NC."),
    dict(id="VI108", tier="B", c_reason="NA", nc_any="yes", nc_isolation_stage="yes",
         m1="yes", m2="yes", m3="unknown", m4="unknown", m5="unknown", m6="unknown", match_basis="NA",
         control_cpe_reported="yes", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="BHV-1 detection in spiked bovine semen (dot blot / PCR / isolation)",
         endpoint_for_control_comparison="CPE / FA",
         notes="'Control denotes negative control, i.e. no virus' in the isolation CPE/FA table; semen toxicity matrix complicates matched conditions -> B."),
    dict(id="VI114", tier="C", c_reason="C-stage", nc_any="yes", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="PRRSV isolation + polypeptide/antigen characterization",
         endpoint_for_control_comparison="protein labeling / RIPA",
         notes="'mock-infected ... DMEM+2% FBS' only for radioisotopic labeling/RIPA (characterization); animal mock piglets. Primary Isolation lacks culture NC -> C-stage."),
    dict(id="VI119", tier="B", c_reason="NA", nc_any="yes", nc_isolation_stage="yes",
         m1="yes", m2="yes", m3="yes", m4="unknown", m5="unknown", m6="yes", match_basis="NA",
         control_cpe_reported="yes", control_cpe_claimed_negative="yes", control_images="yes",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="RD/GPE cell sensitivity to group A coxsackieviruses",
         endpoint_for_control_comparison="CPE",
         notes="'Uninfected RD cells' Fig.1 vs CPE in 2% FBS maintenance (figure-only); 'control (medium alone)' is in suckling mice (animal arm)."),
    dict(id="VI294", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="DENV NS1 antigen detection in mosquito cells",
         endpoint_for_control_comparison="antigen / WB",
         notes="'infected to uninfected mosquitoes' = mosquito arm, no culture-level NC."),
    dict(id="VI295", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="Influenza single-virus imaging",
         endpoint_for_control_comparison="live-cell imaging",
         notes="Dye-labeling controls only; no culture-level mock/uninfected NC."),
    dict(id="VI296", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="HIV-1 single-particle tracking",
         endpoint_for_control_comparison="live-cell imaging",
         notes="No culture-level mock/uninfected NC."),
    dict(id="VI297", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="HBV VLP single-particle tracking",
         endpoint_for_control_comparison="live-cell imaging",
         notes="No culture-level mock/uninfected NC."),
    dict(id="VI298", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="SARS-CoV-2 single-virus tracking",
         endpoint_for_control_comparison="live-cell imaging",
         notes="No culture-level mock/uninfected NC."),
    dict(id="VI299", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="VSV high-speed 3D single-virus tracking",
         endpoint_for_control_comparison="live-cell imaging",
         notes="No culture-level mock/uninfected NC."),
    dict(id="VI300", tier="C", c_reason="C-stage", nc_any="yes", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="yes",
         positive_control_present="no", ambiguous="yes",
         primary_experiment="Vaccinia virus entry mechanism (macropinocytosis)",
         endpoint_for_control_comparison="imaging / plaque / flow",
         notes="Mock/uninfected Vero cells used for SEM/dextran entry assays; poliovirus as a route 'negative control' - not Isolation-stage CPE NC."),
    dict(id="VI301", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="Poliovirus entry kinetics (RNA release, NRIC assay)",
         endpoint_for_control_comparison="live-cell imaging / infectivity",
         notes="R78206 drug, light-exposure and drug-treated 'controls' only; no no-virus culture NC."),
    dict(id="VI302", tier="D", c_reason="NA", nc_any="no", nc_isolation_stage="no",
         m1="NA", m2="NA", m3="NA", m4="NA", m5="NA", m6="NA", match_basis="NA",
         control_cpe_reported="no", control_cpe_claimed_negative="NA", control_images="no",
         positive_control_present="no", ambiguous="no",
         primary_experiment="Murine polyoma VLP single-particle tracking",
         endpoint_for_control_comparison="live-cell imaging",
         notes="'control cells' = actin/disruption assay tracer controls; no no-virus culture NC."),
]

FIELDS = ["id","tier","c_reason","nc_any","nc_isolation_stage","m1_cells","m2_base_medium",
          "m3_serum_enrichment","m4_additives","m5_timeline","m6_inoculum_only_diff","match_basis",
          "control_cpe_reported","control_cpe_claimed_negative","control_images","positive_control_present",
          "ambiguous","primary_experiment","endpoint_for_control_comparison","scorer","score_date","notes"]


def main():
    with OV.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        header = list(rd.fieldnames)
        existing = list(rd)

    existing_ids = {r["id"].upper() for r in existing}
    new_rows = []
    for rm in ROWS:
        # map this script's keys to CSV column names
        row = {
            "id": rm["id"], "tier": rm["tier"], "c_reason": rm["c_reason"],
            "nc_any": rm["nc_any"], "nc_isolation_stage": rm["nc_isolation_stage"],
            "m1_cells": rm["m1"], "m2_base_medium": rm["m2"], "m3_serum_enrichment": rm["m3"],
            "m4_additives": rm["m4"], "m5_timeline": rm["m5"], "m6_inoculum_only_diff": rm["m6"],
            "match_basis": rm["match_basis"], "control_cpe_reported": rm["control_cpe_reported"],
            "control_cpe_claimed_negative": rm["control_cpe_claimed_negative"],
            "control_images": rm["control_images"], "positive_control_present": rm["positive_control_present"],
            "ambiguous": rm["ambiguous"], "primary_experiment": rm["primary_experiment"],
            "endpoint_for_control_comparison": rm["endpoint_for_control_comparison"],
            "scorer": "r2-agent", "score_date": "2026-11-19", "notes": rm["notes"],
            "r1_status": "cat1", "r1_current_id": rm["id"], "r2_universe": "yes",
        }
        if rm["id"].upper() in existing_ids:
            print("SKIP (already present):", rm["id"])
            continue
        new_rows.append(row)

    header = [h for h in header if h]  # drop empties
    # ensure r1_* columns present
    for c in ("r1_status", "r1_current_id", "r2_universe"):
        if c not in header:
            header.append(c)

    for r in existing:
        for c in ("r1_status", "r1_current_id", "r2_universe"):
            r.setdefault(c, "")

    all_rows = existing + new_rows
    with OV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=header)
        w.writeheader()
        for r in all_rows:
            w.writerow({k: r.get(k, "") for k in header})

    print("appended", len(new_rows), "rows; total now", len(all_rows))


if __name__ == "__main__":
    main()
