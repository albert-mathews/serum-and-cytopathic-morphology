"""Dump full text of a PDF to <same>.txt (gitignored refs/) and print grep-style
matches around load-bearing terms for P3 confirmation.

Usage: tools/venv/Scripts/python p3_genetics/wrk/dump_and_search.py <pdf> <term1> [term2 ...]
"""
import sys, os, re
import fitz

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def dump_text(path):
    doc = fitz.open(path)
    parts = []
    for i, pg in enumerate(doc):
        parts.append(f"\n\n===== PAGE {i+1} =====\n\n" + pg.get_text())
    doc.close()
    out = os.path.splitext(path)[0] + ".txt"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("".join(parts))
    return "".join(parts), out

def main(argv):
    pdf = argv[0]
    terms = argv[1:]
    text, out = dump_text(pdf)
    print(f"DUMPED: {out}  ({len(text)} chars)")
    if not terms:
        return
    flat = re.sub(r"\s+", " ", text)
    for term in terms:
        print("\n" + "#" * 90)
        print(f"TERM: {term!r}")
        print("#" * 90)
        for m in re.finditer(re.escape(term), flat, re.IGNORECASE):
            s = max(0, m.start() - 260)
            e = min(len(flat), m.end() + 320)
            print("\n..." + flat[s:e] + "...")

if __name__ == "__main__":
    main(sys.argv[1:])