#!/usr/bin/env python3
"""OCR scanned (image-only) PDFs to collocated Markdown text.

Extracts text from PDFs that are page-scans (i.e. no usable embedded text layer) by
rendering each page to a bitmap and running RapidOCR. Writes "<pdf-stem>.md" next to
the PDF — inside a gitignored refs/ folder, so the derived full text stays local-only.

Technique absorbed from the P4 stream (2026-11-08): RapidOCR over PyMuPDF page
renders at ~288 dpi. Auto-generated text is a reading aid — always verify any quote
against the original page before reuse.

Usage (shared venv, from the repo root):
    Windows:     tools/venv/Scripts/python tools/ocr_pdf.py "<path/ref.pdf>" [more.pdf ...]
    macOS/Linux: tools/venv/bin/python  tools/ocr_pdf.py "<path/ref.pdf>" [more.pdf ...]

Options:
    --dpi-scale N   render scale factor (default 4, roughly 288 dpi). Raise it for
                    small/dense scans; lower it for speed.

Improving this tool (for agents):
    If you find a better recipe while processing a hard scan — higher --dpi-scale,
    image preprocessing, a newer OCR model, language packs, two-column handling —
    change THIS file, add a dated note and an example to tools/README.md, and re-OCR
    any source you previously extracted, so the improvement is available to every
    future agent. Keep the current behavior as the default unless the new one is
    clearly better across a range of pages.
"""

import argparse
import os
import sys

import pymupdf as fitz  # PyMuPDF (new import name)
from rapidocr_onnxruntime import RapidOCR

DEFAULT_DPI_SCALE = 4


def ocr_pdf(pdf_path: str, dpi_scale: int = DEFAULT_DPI_SCALE):
    engine = RapidOCR()
    doc = fitz.open(pdf_path)
    pages = doc.page_count
    name = os.path.basename(pdf_path)
    out_parts = [
        f"# OCR text - {name}",
        "",
        "*Auto-generated from a scanned image PDF via RapidOCR (tools/venv). "
        "Machine OCR only; verify any quote against the original page before reuse.*",
        "",
    ]
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi_scale, dpi_scale))
        base = os.path.splitext(name)[0]
        tmp_png = os.path.join(os.path.dirname(pdf_path), f"._ocr_tmp_{base}_{i}.png")
        pix.save(tmp_png)
        try:
            result, _ = engine(tmp_png)
        finally:
            if os.path.exists(tmp_png):
                os.remove(tmp_png)
        out_parts.append(f"---\n\n## Page {i + 1}/{pages}\n")
        if result:
            out_parts.append("\n".join(item[1] for item in result))
        else:
            out_parts.append("*(no text detected)*")
        out_parts.append("")
    doc.close()

    out_md = os.path.splitext(pdf_path)[0] + ".md"
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out_parts))
    return out_md, pages


def main(argv):
    parser = argparse.ArgumentParser(description="OCR scanned PDFs to collocated Markdown.")
    parser.add_argument("pdfs", nargs="+", help="one or more scanned PDF paths")
    parser.add_argument(
        "--dpi-scale",
        type=int,
        default=DEFAULT_DPI_SCALE,
        help=f"render scale factor (default {DEFAULT_DPI_SCALE} ~ 288 dpi)",
    )
    args = parser.parse_args(argv)

    for arg in args.pdfs:
        path = os.path.abspath(arg)
        out, pages = ocr_pdf(path, dpi_scale=args.dpi_scale)
        print(f"OCR {out} ({pages} pages)")


if __name__ == "__main__":
    main(sys.argv[1:])