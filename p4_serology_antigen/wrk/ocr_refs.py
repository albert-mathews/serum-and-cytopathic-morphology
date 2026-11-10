"""OCR a scanned (image-only) PDF to a collocated .md text file.

Usage (from the repo root, using the gitignored r3 viz venv):
  .venv/Scripts/python wrk/ocr_refs.py "<path/to/ref.pdf>" [more.pdf ...]

Writes "<ref>.md" next to the PDF (inside gitignored refs/, so the derived
full text stays local-only). Auto-generated with RapidOCR; treat as a reading
aid, verify any quote against the original page before reuse.
"""

import os
import sys

import fitz
from rapidocr_onnxruntime import RapidOCR

DPI_SCALE = 4  # ~288 dpi


def ocr_pdf(pdf_path: str) -> str:
    engine = RapidOCR()
    doc = fitz.open(pdf_path)
    n = doc.page_count
    name = os.path.basename(pdf_path)
    out_parts = [
        f"# OCR text - {name}",
        "",
        "*Auto-generated from a scanned image PDF via RapidOCR (venv `r3_image_labeling/wrk/viz/.venv`). "
        "Machine OCR only; verify any quote against the original page before reuse.*",
        "",
    ]
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(DPI_SCALE, DPI_SCALE))
        tmp_png = os.path.join(
            os.path.dirname(pdf_path), f"._ocr_tmp_{os.path.splitext(name)[0]}_{i}.png"
        )
        pix.save(tmp_png)
        result, _ = engine(tmp_png)
        os.remove(tmp_png)
        out_parts.append(f"---\n\n## Page {i + 1}/{n}\n")
        if result:
            out_parts.append("\n".join(item[1] for item in result))
        else:
            out_parts.append("*(no text detected)*")
        out_parts.append("")
    doc.close()

    out_md = os.path.splitext(pdf_path)[0] + ".md"
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out_parts))
    return out_md, n


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        path = os.path.abspath(arg)
        out, pages = ocr_pdf(path)
        print(f"OCR {out} ({pages} pages)")
