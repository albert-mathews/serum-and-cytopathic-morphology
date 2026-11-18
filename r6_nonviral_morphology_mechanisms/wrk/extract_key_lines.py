# extract_key_lines.py — pull mechanism-relevant lines from fetched R6 PDFs (one-off)
# Usage: tools/venv/Scripts/python r6_nonviral_morphology_mechanisms/wrk/extract_key_lines.py
import glob, os, re, sys
import fitz

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TARGETS = {
    "R6-004": ["detach", "bleb", "apoptot", "round", "brightness", "vacuol", "shin", "granul"],
    "R6-016": ["apoptosis", "necrosis", "serum-free", "death", "LDH", "detach", "viab"],
    "R6-008": ["diffusion", "plaque formation failure", "virion inviabil", "walk", "radius", "motility"],
    "R6-011": ["overlay", "glucose", "diameter", "nutrient", "MEM", "DMEM"],
    "R6-005": ["adhesion", "fibronectin", "multilayer", "spheroid", "detach", "stress", "transformed"],
    "R6-006": ["serum", "G2", "divid", "arrest", "factor", "saturated", "transition"],
    "R6-010": ["reproducib", "plaque", "requirement", "principle", "assay", "condition", "overlay", "agar"],
    "R6-013": ["vacuol", "elongat", "morpholog", "cytopath", "alter", "filament"],
    "R6-015": ["mycoplasma", "eradication", "detect", "culture", "contaminat"],
    "R6-017": ["autophag", "starv", "apoptosis", "adhesion", "LC3", "EBSS"],
    "R6-018": ["overlay", "agarose", "CMC", "carboxymethyl", "Avicel", "plaque", "liquid"],
}

refs = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "refs"))
for name, kws in TARGETS.items():
    for p in glob.glob(os.path.join(refs, name + "*.pdf")):
        print("\n### " + os.path.basename(p))
        doc = fitz.open(p)
        seen = set()
        for i in range(doc.page_count):
            text = doc[i].get_text() or ""
            for line in text.split("\n"):
                low = line.lower()
                if any(k in low for k in kws):
                    s = re.sub(r"\s+", " ", line).strip()
                    if s and s not in seen:
                        seen.add(s)
                        print("  >", s[:240])