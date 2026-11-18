"""Extract the text layer of PDFs to a collocated <stem>.md (inside gitignored refs/),
so full text stays local-only. Reports PDFs with no usable text layer (needs OCR).

Usage:
    tools/venv/Scripts/python r5_precell_virus_purification_census/wrk/extract_pdf_text.py <pdf_or_dir> [more...]

Note: this mirrors tools/ocr_pdf.py's "write .md next to the PDF" convention, but for
the embedded text layer (no OCR). Add it to tools/ if a second stream needs it.
"""
import sys, os
import fitz  # PyMuPDF


def process(path):
    stem = os.path.splitext(path)[0]
    out = stem + ".md"
    doc = fitz.open(path)
    try:
        txt = "\n".join(page.get_text() for page in doc)
    finally:
        doc.close()
    n = len(txt.strip())
    if n < 200:
        print(f"IMAGE-ONLY (text {n} chars, needs tools/ocr_pdf.py): {path}")
        return
    with open(out, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"TEXT {n} chars -> {out}")


def main(args):
    paths = []
    for a in args:
        if os.path.isdir(a):
            for fn in sorted(os.listdir(a)):
                if fn.lower().endswith(".pdf"):
                    paths.append(os.path.join(a, fn))
        else:
            paths.append(a)
    for p in paths:
        if os.path.exists(p):
            process(p)
        else:
            print(f"MISSING: {p}")


if __name__ == "__main__":
    main(sys.argv[1:])
