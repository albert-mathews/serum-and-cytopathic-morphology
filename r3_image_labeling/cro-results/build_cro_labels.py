#!/usr/bin/env python3
"""Build the processed CRO labels from the CRO's light-microscopy image descriptions.

Source of truth: the CRO image-description report (docx, 2025-06-23), exported verbatim to
`cro_image_descriptions.txt` in this folder (paragraph text only; document metadata not exported).
Re-export after a new report version with:
    python build_cro_labels.py --export-docx "<path to report .docx>"     (needs python-docx)

Outputs (this folder)
- cro_cpe_detections.csv  CANONICAL per-frame CRO labels: one row per frame that has its OWN
                          single-image description (22 frames of the 100-frame EXP passage-4 set).
                          CPE-type (Table 7) terms CRO_Dy/Ro/V/D/G/Re and healthy-type (CRO) terms
                          CRO_H_*; binary: 1 = named in that frame's own description, 0 = not named.
- cro_group_level_notes.csv  Group/range descriptions (e.g. EXP_path2_passage4_301-310), coded with the
                          same rules, kept SEPARATELY. Lower specificity: never applied to member frames
                          and not used in any per-frame incidence, agreement statistic or figure.
- cpe_detection_results_cro.json  JSON view of the canonical CPE-type columns (derived; same values).

Labeling rule (conservative, single-frame): a frame's labels come only from a description that names
that frame individually (e.g. "EXP_path2_passage4_303:" or the enumerated "EXP_path2_passage4_503 & 504:").
A group/range description is not evidence about any specific member frame (annotation unit = analysis unit).

Term rules (lower-cased description; negated clauses "no (obvious|clear) (signs|evidence) of ..." removed):
  Dy  dying | cell death | dead cell(s)          Ro  rounded | round cell(s)
  V   vacuol* | vesicle(s)                        D   detach* | floating
  G   granular*                                   Re  refractile   ("bright reflective points" is NOT Re)
  H_Look_Healthy healthy        H_Mitotic mitotic | mitosis | dividing | division
  H_Bright  "bright" not followed by reflective/spot(s)/point(s)/vesicle(s), and not in a sentence that
            calls those cells dying/debris
  H_Adherent adherent | attach* (not detach*)     H_Elongated elongated | spindle
  H_Polygonal polygonal | cobblestone             H_Cytoplasmic_extensions (cytoplasmic) extension(s)
  H_well_defined_nuclei well-defined | distinct nuclei
hedged_terms lists terms whose match follows a hedge word (might, could, probably, most likely,
potentially, possibly) earlier in the same sentence. Hedged mentions still count as named.
Frame ids: path1 = Culture A (10% FBS), path2 = Culture B (2% FBS); id = <day><field 01-10>; the
blinded id follows ../images_rater_blinded_mapping.csv (path2 day-3 ids 303/307/308 refer to the
original captures, as described by the CRO).
Confluence is recorded in the text but is never used as a healthy/stressed label.

Run: python build_cro_labels.py
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TXT = HERE / "cro_image_descriptions.txt"
OUT_FRAMES = HERE / "cro_cpe_detections.csv"
OUT_GROUPS = HERE / "cro_group_level_notes.csv"
OUT_JSON = HERE / "cpe_detection_results_cro.json"

CPE = [("CRO_Dy", r"\bdying\b|\bcell death\b|\bdead cells?\b"),
       ("CRO_Ro", r"\brounded\b|\bround cells?\b"),
       ("CRO_V", r"\bvacuol\w*|\bvesicles?\b"),
       ("CRO_D", r"\bdetach\w*|\bfloating\b"),
       ("CRO_G", r"\bgranular\w*"),
       ("CRO_Re", r"\brefractile\b")]
HEALTHY = [("CRO_H_Look_Healthy", r"\bhealthy\b"),
           ("CRO_H_Mitotic", r"\bmitotic\b|\bmitosis\b|\bdividing\b|\bdivision\b"),
           ("CRO_H_Bright", r"\bbright\b(?!\s+(?:reflective|spots?|points?|vesicles?)\b)"),
           ("CRO_H_Adherent", r"\badherent\b|\battach\w*"),
           ("CRO_H_Elongated", r"\belongated\b|\bspindle\b"),
           ("CRO_H_Polygonal", r"\bpolygonal\b|\bcobblestone\b"),
           ("CRO_H_Cytoplasmic_extensions", r"\b(?:cytoplasmic\s+)?extensions?\b"),
           ("CRO_H_well_defined_nuclei", r"\bwell-defined nuclei\b|\bdistinct nuclei\b")]
TERMS = CPE + HEALTHY
CPE_JSON = {"CRO_Dy": "dying cells", "CRO_Ro": "rounded", "CRO_V": "vacuoles", "CRO_D": "detached",
            "CRO_G": "granular", "CRO_Re": "refractile"}
NEGATION = re.compile(r"\bno\s+(?:obvious\s+|clear\s+)?(?:signs?|evidence)\s+of\b[^.]*", re.I)
HEDGE = re.compile(r"\b(might|could|probably|most likely|potentially|possibly)\b", re.I)
HEAD = re.compile(r"EXP_path([12])_passage4_([0-9a-z ,&\-]+?):", re.I)


def export_docx(path: Path) -> None:
    import docx  # python-docx
    d = docx.Document(str(path))
    lines = [p.text for p in d.paragraphs]
    TXT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"exported {len(lines)} paragraphs -> {TXT.name}")


def parse_ids(spec: str):
    """'101-110' / '301-310, 301a-310a' -> ('group', ...); '307 and 308' / '503 & 504' / '405, 406' -> singles."""
    spec = spec.strip()
    if "-" in spec:
        return "group", spec
    ids = [int(x) for x in re.split(r"\s*(?:,|&|\band\b)\s*", spec) if x.strip()]
    return "frame", ids


def segments(text: str):
    """Yield (path, kind, ids_or_range, head_text, description) for the EXPERIMENT section."""
    start = text.find("EXPERIMENT P4")
    body = text[start:]
    heads = list(HEAD.finditer(body))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        desc = body[m.end():end]
        desc = re.sub(r"EXPERIMENT P4 Day \d+:", " ", desc)
        desc = re.sub(r"\s+", " ", desc).strip()
        kind, ids = parse_ids(m.group(2))
        yield int(m.group(1)), kind, ids, m.group(0)[:-1], desc


def code(desc: str) -> tuple[dict, list]:
    text = NEGATION.sub(" ", desc.lower())
    sentences = re.split(r"(?<=[.;])\s+", text)
    marks, hedged = {}, []
    for col, rx in TERMS:
        hit, hedge_only = False, True
        for s in sentences:
            for m in re.finditer(rx, s):
                if col == "CRO_H_Bright" and re.search(r"\bdying\b|\bdebris\b", s):
                    continue  # bright cells described as dying/debris are not the healthy-type 'Bright'
                hit = True
                h = HEDGE.search(s)
                if not (h and h.start() < m.start()):
                    hedge_only = False
        marks[col] = int(hit)
        if hit and hedge_only:
            hedged.append(col.replace("CRO_", ""))
    return marks, hedged


def blinded(path: int, fid: int) -> str:
    return f"Culture{'AB'[path - 1]}_day{fid // 100}_{fid % 100:02d}"


def build():
    text = TXT.read_text(encoding="utf-8")
    frames, groups = {}, []
    for path, kind, ids, head, desc in segments(text):
        marks, hedged = code(desc)
        if kind == "frame":
            for fid in ids:
                if (path, fid) in frames:
                    raise ValueError(f"two single-image descriptions for path{path} {fid}")
                frames[(path, fid)] = dict(path=path, id=fid, **marks, blinded_id=blinded(path, fid),
                                           culture=f"Culture{'AB'[path - 1]}", day=fid // 100,
                                           described_as=head.split("passage4_")[1], hedged_terms=";".join(hedged),
                                           description=desc)
        else:
            first = int(re.match(r"(\d+)", ids).group(1))
            groups.append(dict(path=path, culture=f"Culture{'AB'[path - 1]}", day=first // 100, frames=ids,
                               scope="group/range description (lower specificity)",
                               used_in_per_frame_analysis=0, **marks, hedged_terms=";".join(hedged),
                               description=desc))
    rows = [frames[k] for k in sorted(frames)]
    return rows, groups


def write_csv(path: Path, rows: list[dict]):
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator="\r\n")
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--export-docx", help="re-export the report .docx to cro_image_descriptions.txt first")
    a = ap.parse_args()
    if a.export_docx:
        export_docx(Path(a.export_docx))
    rows, groups = build()
    write_csv(OUT_FRAMES, rows)
    write_csv(OUT_GROUPS, groups)
    js = {}
    for r in rows:
        types = [CPE_JSON[c] for c, _ in CPE if r[c]]
        js[f"EXP_path{r['path']}_passage4_{r['id']}.png"] = {"cpe_detected": bool(types), "cpe_types": types or None}
    OUT_JSON.write_text(json.dumps(js, indent=2) + "\n", encoding="utf-8", newline="\r\n")
    print(f"{OUT_FRAMES.name}: {len(rows)} frames with their own description "
          f"({sum(r['path'] == 1 for r in rows)} path1 / {sum(r['path'] == 2 for r in rows)} path2)")
    print(f"{OUT_GROUPS.name}: {len(groups)} group/range descriptions (not used per frame)")
    print(f"{OUT_JSON.name}: derived CPE-type view")


if __name__ == "__main__":
    main()
