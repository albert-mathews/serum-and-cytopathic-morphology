# Research strategy (all agents)

Standard workflow for literature-backed research tasks in any stream.

## Step 1 — find publications

Search legitimate sources of record: PubMed, Europe PMC, Crossref, publisher sites, preprint servers, and
institutional/repository archives. There is no preferred source; use whatever yields the document.

- Patents are left out unless the task explicitly asks for them. Skip patent hits and do not record their
  numbers.
- An abstract or search snippet may **identify** a candidate, but it cannot settle a claim. A full text must
  be read before a claim is established.

## Step 2 — obtain the full text; if blocked, log a wishlist row

When a needed full text is paywalled or blocked:

1. Create/update **`<STREAM>_pdf_wishlist.md`** at the root of the stream folder (where `<STREAM>` is the
   stream ID, e.g. `R2_pdf_wishlist.md`, `P4_pdf_wishlist.md`).
2. Add one row per document with these columns (in this order):

   | Column | Meaning |
   |--------|---------|
   | **Title** | Full document title |
   | **Year** | Publication year |
   | **Author** | First author / lead authorship |
   | **Identifier** | PMID, DOI, or stable URL that identifies it on the internet |
   | **Drop as** | Exact PDF filename to use when the owner saves it into `<stream>/refs/` |

   Optional extra columns (allowed, not required): *Why needed*, *Priority*.

3. Rules:
   - Never guess a DOI or locator. If it is built from a publisher pattern, mark it `[UNVERIFIED]`; if unknown,
     write `not seen`. PMID / DOI / stable URL from the actual record is preferred.
   - Until the full text is read, any claim that depends on it is `[DATA REQUIRED]` (full text outstanding),
     never `[VERIFIED]`.
   - The owner fetches the files; received PDFs land in `<stream>/refs/` under the **Drop as** name. PDFs are
     never committed.

## Step 2a — scanned (image-only) PDFs: OCR before extraction

When a fetched PDF is a page scan with no usable text layer, extract its text with the shared OCR tool
(absorbed from the P4 technique):

```
tools/venv/Scripts/python tools/ocr_pdf.py "<stream>/refs/<name>.pdf"    # Windows
```

The tool writes `<name>.md` next to the PDF (still inside gitignored `refs/`), so the derived full text
stays local-only. OCR output is a reading aid — verify any quote against the original page before reuse,
and only tag it `[VERIFIED src]` after actually reading the rendered page.

### Improve-and-share

OCR quality varies by scan. If you improve the recipe (higher `--dpi-scale`, image preprocessing, a newer
OCR model, two-column handling), update `tools/ocr_pdf.py`, add a dated note + example to `tools/README.md`,
and re-OCR any affected source — so every future agent inherits the better technique.

## Step 3 — extract and record

Once received, extract into the stream's CSV/notes following its coding sheet, attach the evidence tag that
matches how the material was read (`[VERIFIED src]`, `[VERIFIED-ABSTRACT]`, `[FIGURE]`), and remove the row
from the wishlist (or mark it received).

Evidence tags: `[VERIFIED src]`, `[VERIFIED-ABSTRACT]`, `[FIGURE]`, `[SUPPLIER]`, `[IN-HOUSE]`,
`[UNVERIFIED]`, `[DATA REQUIRED]`. See `CONVENTIONS.md` §3.