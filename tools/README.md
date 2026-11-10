# tools/ — shared tooling

## Shared Python venv

The repository uses **one** shared venv for all stream Python work:

```
tools/venv/            (gitignored — recreate locally, never commit)
tools/requirements.txt (tracked — the source of truth for dependencies)
```

### One-time setup (a fresh machine)

```bash
# from repo root
python -m venv tools/venv
# Windows:
tools/venv/Scripts/pip install -r tools/requirements.txt
# macOS / Linux:
tools/venv/bin/pip install -r tools/requirements.txt
```

### Using it

- Windows: `tools\venv\Scripts\python.exe <script>`
- macOS/Linux: `tools/venv/bin/python <script>`

### Adding a package

`pip install <pkg>` into `tools/venv`, then add it to `tools/requirements.txt` (with a version floor)
so the next person recreates the same set.

### Notes

- `tools/venv` is gitignored (see root `.gitignore`). Only `tools/requirements.txt` and this README travel
  with the repo.
- The former per-stream venv at `r3_image_labeling/wrk/viz/.venv` is superseded by `tools/venv` and may be
  deleted at any time (it is also gitignored).
- For agents: see `agent-settings/environment.md` for the working rule (never create per-stream venvs).

## OCR tool (scanned / image-only PDFs)

Some fetched PDFs are page scans with no embedded text layer. `tools/ocr_pdf.py` renders each page to a
bitmap and runs RapidOCR, writing `<name>.md` next to the PDF (inside a gitignored `refs/`, so the derived
full text stays local-only).

```bash
# Windows
tools\venv\Scripts\python tools/ocr_pdf.py "r2_negative_controls/refs/some_scan.pdf"
# macOS/Linux
tools/venv/bin/python tools/ocr_pdf.py "r2_negative_controls/refs/some_scan.pdf"
```

- `--dpi-scale N` raises/lowers the render resolution (default 4 ≈ 288 dpi) for dense or light scans.
- Requires `PyMuPDF` and `rapidocr-onnxruntime` — already in `tools/requirements.txt`.
- OCR output is a reading aid: verify any quote against the original page before reuse.

### Improving the OCR technique

If you get better extraction on a hard scan (resolution, preprocessing, model, language, multi-column),
update `tools/ocr_pdf.py` (keep the current behavior the default unless the new one is clearly better),
add a dated line + example to the changelog below, and re-OCR any source you previously extracted so the
improvement is not lost.

**Changelog:**

- 2026-11-08 — absorbed from the P4 stream (`p4_serology_antigen/wrk/ocr_refs.py`): RapidOCR over PyMuPDF
  page renders at ~288 dpi (`DPI_SCALE=4`); collocated `.md` output. Changed only the venv reference to
  `tools/venv` and added `--dpi-scale`.

## Dependency source

Third-party imports across the tracked scripts are: `matplotlib`, `numpy`, `pandas`, `scipy`, `openpyxl`,
`python-docx` (`import docx`), `PyMuPDF` (`import fitz`), and `rapidocr-onnxruntime` (`RapidOCR`) — the last
pulls in its own OCR stack (onnxruntime, opencv, pillow, shapely, pyclipper, PyYAML). `tomli` covers
Python < 3.11 config parsing; 3.11+ uses stdlib `tomllib`.