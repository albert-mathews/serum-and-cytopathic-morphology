"""Extract text from all R1 isolation_practice PDFs; report which are image-only (need OCR).

Uses PyMuPDF (fitz) from the shared r3 viz venv. Writes plain text to
_pdf_extract_tmp/ and prints, for each PDF, page count + text char count +
'empty' flag for those with no usable text layer.
"""

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REFS = os.path.join(REPO, "r1_isolation_standards_and_practice", "refs", "isolation_practice")
TMP = os.path.join(REPO, "p4_serology_antigen", "_pdf_extract_tmp")
os.makedirs(TMP, exist_ok=True)

import fitz

def main():
    pdfs = sorted(f for f in os.listdir(REFS) if f.lower().endswith(".pdf"))
    empty, total_chars = [], 0
    for f in pdfs:
        path = os.path.join(REFS, f)
        try:
            doc = fitz.open(path)
        except Exception as e:
            print(f"OPEN-FAIL\t{f}\t{e}")
            continue
        txt = ""
        for page in doc:
            txt += page.get_text()
        doc.close()
        nchar = len(txt.strip())
        total_chars += nchar
        # write plain text
        out = os.path.join(TMP, os.path.splitext(f)[0] + ".txt")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(txt)
        if nchar < 200:
            empty.append(f)
    print(f"extracted {len(pdfs)} PDFs -> {TMP}")
    print(f"total text chars: {total_chars}")
    print(f"image-only / near-empty ({len(empty)}):")
    for f in empty:
        print("  ", f)

if __name__ == "__main__":
    main()
