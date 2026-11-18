# check_pdfs.py — confirm each R6 refs/ PDF identity + text-layer presence (one-off confirm step)
# Usage: tools/venv/Scripts/python r6_nonviral_morphology_mechanisms/wrk/check_pdfs.py
import glob, os, sys
import fitz  # PyMuPDF

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

here = os.path.dirname(os.path.abspath(__file__))
refs = os.path.abspath(os.path.join(here, "..", "refs"))

for p in sorted(glob.glob(os.path.join(refs, "*.pdf"))):
    name = os.path.basename(p)
    doc = fitz.open(p)
    page1 = doc[0].get_text().strip()
    n = doc.page_count
    has_text = bool(page1)
    preview = " ".join(page1.split())[:360] if has_text else "[NO TEXT LAYER - image-only]"
    print("=" * 80)
    print(f"{name}  [{n} pages]")
    print(preview)
