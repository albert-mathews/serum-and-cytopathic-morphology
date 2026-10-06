"""Item definitions, Pass-2 vocabulary normalization, Pass-1 lexicon.

Scoring logic copied unchanged from the IR1 Pass-2 scorer used for the side-by-side analysis:
  CPE items:     Yes 1.0 | Mild, Mild/partial 0.66 | Partial 0.5 | Minimal 0.25 | No/minimal 0.15 | No, Not apparent 0
  Healthy items: Yes 1.0 | Partial, Mild, Mild/partial 0.5 | else 0
Strict incidence: Yes / Partial / Mild / Mild-partial = present.
Pass-1 lexicon: identical HEALTHY/CPE regex sets used for IR1/IR2/pilot Pass 1.
Confluence / coverage is never scored as healthy vs stressed.
"""
from __future__ import annotations

import re

# (key, short label, kind)
ITEMS = [
    ("H_Look_Healthy", "Looks healthy", "healthy"),
    ("H_well_defined_nuclei", "Nuclei well defined", "healthy"),
    ("H_Cytoplasmic_extensions", "Cytoplasmic extensions", "healthy"),
    ("CPE_Vacuolation_V", "Vacuolation", "cpe"),
    ("CPE_Granularity_G", "Granularity", "cpe"),
    ("CPE_Ballooned_Enlarged_BE", "Ballooned / enlarged", "cpe"),
    ("CPE_Syncytia_Sy", "Syncytia", "cpe"),
    ("CPE_Cytoplasmic_strands_CS", "Cytoplasmic strands", "cpe"),
    ("CPE_Cell_death_Dy", "Cell death", "cpe"),
    ("CPE_Nonspecific_degeneration_ND", "Nonspecific degeneration", "cpe"),
]
ITEM_KEYS = [k for k, _, _ in ITEMS]
LABEL = {k: l for k, l, _ in ITEMS}
KIND = {k: t for k, _, t in ITEMS}
HEALTHY_KEYS = [k for k in ITEM_KEYS if KIND[k] == "healthy"]
CPE_KEYS = [k for k in ITEM_KEYS if KIND[k] == "cpe"]

# Instrument-layout header number -> item key
CHECKLIST_NUM = {i + 1: k for i, k in enumerate(ITEM_KEYS)}

# CRO six descriptor columns (+ checklist extras present in merged IR coding)
CRO_SIX = ["Dy", "Ro", "V", "D", "G", "Re"]
CRO_LABEL = {"Dy": "Cell death", "Ro": "Rounded", "V": "Vacuolation", "D": "Detachment",
             "G": "Granularity", "Re": "Refractile"}

HEALTH_SCORE = {"yes": 1.0, "partial": 0.5, "mild/partial": 0.5, "mild": 0.5, "minimal": 0.0,
                "no/minimal": 0.0, "no": 0.0, "not apparent": 0.0}
CPE_SCORE = {"yes": 1.0, "mild/partial": 0.66, "mild": 0.66, "partial": 0.5, "minimal": 0.25,
             "no/minimal": 0.15, "no": 0.0, "not apparent": 0.0}
STRICT_PRESENT = {"yes", "partial", "mild", "mild/partial"}

# Ordinal display levels for the diverging (Likert-style) chart, low -> high.
LEVELS = ["absent", "trace", "partial", "mild", "yes"]
LEVEL_LABEL = {"absent": "No / not apparent", "trace": "Minimal / no-minimal",
               "partial": "Partial", "mild": "Mild (/partial)", "yes": "Yes"}
PRESENT_LEVELS = ["partial", "mild", "yes"]   # right of the zero line (strict presence)
ABSENT_LEVELS = ["trace", "absent"]           # left of the zero line, inner -> outer


def norm(s) -> str:
    return re.sub(r"\s+", " ", str(s).strip().lower())


def score_health(a: str) -> float:
    a = norm(a)
    if a in HEALTH_SCORE:
        return HEALTH_SCORE[a]
    if "yes" in a and not a.startswith("no"):
        return 1.0
    if "partial" in a or "mild" in a:
        return 0.5
    if a.startswith("no") or "not apparent" in a or "minimal" in a:
        return 0.0
    raise KeyError(f"unmapped healthy assessment: {a!r}")


def score_cpe(a: str) -> float:
    a = norm(a)
    if a in CPE_SCORE:
        return CPE_SCORE[a]
    if "yes" in a and "no" not in a:
        return 1.0
    if "mild" in a:
        return 0.66
    if "partial" in a:
        return 0.5
    if a.startswith("no") and "minimal" in a:
        return 0.15
    if "minimal" in a:
        return 0.25
    if a.startswith("no") or "not apparent" in a:
        return 0.0
    raise KeyError(f"unmapped CPE assessment: {a!r}")


def score(item: str, raw: str) -> float:
    return score_health(raw) if KIND[item] == "healthy" else score_cpe(raw)


def strict_present(raw: str) -> int:
    a = norm(raw)
    if a in STRICT_PRESENT:
        return 1
    if a in HEALTH_SCORE:
        return 0
    # unseen wording: fall back to the CPE graded score boundary (>= Partial)
    return int(score_cpe(a) >= 0.5)


def level(raw: str) -> str:
    a = norm(raw)
    if a == "yes" or ("yes" in a and "no" not in a):
        return "yes"
    if "mild" in a:
        return "mild"
    if "partial" in a:
        return "partial"
    if "minimal" in a:
        return "trace"
    return "absent"


# ---------------- Pass-1 lexicon (unchanged from the shared Pass-1 scorer)
P1_HEALTHY = [
    ("H_Look_Healthy", r"\b(healthy|look\s+healthy|well[\s\-]?spread|fairly\s+well\s+spread|good\s+attachment|appear\s+well\s+spread)\b"),
    ("H_Mitotic_Bright", r"\b(mitotic|mitosis|dividing|phase[\s\-]?bright|phasebright)\b"),
    ("H_Adherent", r"\b(adherent|attachment|well[\s\-]?spread)\b"),
    ("H_Elongated", r"\b(elongated|spindle[\s\-]?shaped|spindle)\b"),
    ("H_Polygonal", r"\b(polygonal|cobblestone)\b"),
    ("H_Cytoplasmic_extensions", r"\b(cytoplasmic\s+extensions?|cytoplasmic\s+processes?)\b"),
    ("H_well_defined_nuclei", r"\b(well[\s\-]?defined\s+nuclei|distinct\s+nuclei|nuclei\s+visible|well[\s\-]?defined\s+nucleus)\b"),
]
P1_CPE = [
    ("CPE_Cell_death_Dy", r"\b(cell\s+death|dying|dead\s+cells?|apoptos\w*|pyknos\w*|necro\w*)\b"),
    ("CPE_Rounded_Ro", r"\b(rounded)\b"),
    ("CPE_Ballooned_Enlarged_BE", r"\b(ballooned|swollen|enlarged\s+cells?|cells?\s+appear\s+enlarged|enlarged\s+(?:rounded|polygonal|spindle)|cell\s+enlargement)\b"),
    ("CPE_Syncytia_Sy", r"\b(syncytia|syncytium|multinucleat\w*|fused\s+cells?)\b"),
    ("CPE_Vacuolation_V", r"\b(vacuol\w*)\b"),
    ("CPE_Detachment_D", r"\b(detach\w*|non[\s\-]?adherent|floating|loss\s+of\s+adhesion|poor(?:ly)?\s+adher\w*)\b"),
    ("CPE_Granularity_G", r"\b(granular\w*|granularity)\b"),
    ("CPE_Refractile_Re", r"\b(refractile|phase[\s\-]?bright|phasebright)\b"),
    ("CPE_Cytoplasmic_strands_CS", r"\b(cytoplasmic\s+strands?)\b"),
    ("CPE_Nonspecific_degeneration_ND", r"\b(degenerat\w*|deteriorat\w*|nonspecific\s+degeneration|cellular\s+stress|signs?\s+of\s+stress)\b"),
]
P1_HEALTHY = [(k, re.compile(p, re.I)) for k, p in P1_HEALTHY]
P1_CPE = [(k, re.compile(p, re.I)) for k, p in P1_CPE]
P1_CPE_KEYS = [k for k, _ in P1_CPE]
P1_HEALTHY_KEYS = [k for k, _ in P1_HEALTHY]
