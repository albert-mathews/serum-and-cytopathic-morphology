"""Confirm fetched P3 PDFs are the correct documents and dump first-page text + title metadata.

Usage (share venv):
    tools/venv/Scripts/python p3_genetics/wrk/extract_confirmation.py <pdf-or-dir>

For each PDF it prints: filename, page count, whether a text layer exists, and the
first ~1200 chars of extracted text (usually title/authors/abstract) so the agent can
confirm identity against the wishlist row.
"""
import sys, os
import fitz  # PyMuPDF

# Force UTF-8 stdout on Windows to avoid cp1252 UnicodeEncodeError.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def first_text(path, chars=1200):
    doc = fitz.open(path)
    npages = doc.page_count
    text = ""
    total_chars = 0
    has_layer = False
    for p in doc:
        t = p.get_text()
        if t.strip():
            has_layer = True
        total_chars += len(t)
        if len(text) < chars:
            text += t
        if len(text) >= chars:
            break
        if len(text) > 0 and total_chars > chars * 2:
            break
    doc.close()
    return npages, has_layer, total_chars, text

def main(argv):
    targets = []
    for a in argv:
        if os.path.isdir(a):
            for f in sorted(os.listdir(a)):
                if f.lower().endswith(".pdf"):
                    targets.append(os.path.join(a, f))
        elif os.path.isfile(a) and a.lower().endswith(".pdf"):
            targets.append(a)
    for t in targets:
        fname = os.path.basename(t)
        npages, has_layer, total_chars, text = first_text(t)
        print("=" * 100)
        print(f"FILE: {fname}")
        print(f"pages={npages} text_layer={has_layer} total_chars={total_chars}")
        print("-" * 100)
        print(text[:1500].strip())
        print()

if __name__ == "__main__":
    main(sys.argv[1:])