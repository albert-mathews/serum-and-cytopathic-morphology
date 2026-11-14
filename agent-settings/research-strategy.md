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

1. Create/update **`<STREAM>_pdf_wishlist.md`** (where `<STREAM>` is the stream ID, e.g. `R2_pdf_wishlist.md`,
   `P4_pdf_wishlist.md`).
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

4. **Open-access papers go on the wishlist too.** Even an open-access paper read online is added to
   `<STREAM>_pdf_wishlist.md`, because all research should eventually rest on the **fetched PDF**, not the
   online/HTML rendering. It is acceptable to read the online version when it is found and read in the same
   prompt, and to keep relying on that reading until the PDF is fetched. Once the PDF is fetched, the PDF
   becomes the source.

### Wishlist lifecycle (working document, not a bibliography)

The wishlist is an **agent ↔ human coordination queue** for fetching documents. It must stay clean and lean
so Albert can use it effectively.

- **Location:** every wishlist lives at the **stream root** and is **gitignored** (the stream root wishlist
  is local-only, like `refs/`).
- **On fetch:** confirm the fetched file is actually the correct document (title/authors/identifier match the
  row). If confirmed, **remove the row from the wishlist** — do not mark it "received" and leave it in place.
  If the fetched file is *not* the correct document, report it back on the row and do not remove it.
- **Not a bibliography:** the wishlist records only what still needs fetching. What was fetched and read is
  captured in the stream's **two bibliographies** (Step 3), never in the wishlist.

## Step 2b — retracted articles: note-only, never load-bearing

Retracted articles **may not** be used as references or knowledge for building arguments, forming statistical
views of publishing landscapes, asserting conclusions, or anything else core to the project/stream's
truth-seeking goals. They may be used **only** as interesting informative notes on the topic.

- **Label:** any retracted reference in a bibliography or wishlist carries a **`RETRACTED`** label.
- **Filename:** any fetched retracted PDF uses the `_RETRACTED` suffix, e.g.
  `<ID>_<short name>_RETRACTED.pdf`.
- This applies whether the retraction happened before or after the item entered the wishlist/bib.

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

## Step 3 — extract and record (two-bibliography discipline)

Once a fetched PDF is confirmed as the correct document (and removed from the wishlist), extract into the
stream's CSV/notes following its coding sheet, attach the evidence tag that matches how the material was read
(`[VERIFIED src]`, `[VERIFIED-ABSTRACT]`, `[FIGURE]`), and record the document in **one of the stream's two
bibliographies**:

1. **Used bibliography** — for references read and used in the research knowledge (carry cited/used items).
2. **Read-but-unused bibliography** — for every *other* document that was fetched/read but did not yield
   valuable information.

These two bibliographies are what retain the record of what was fetched and read. The wishlist is **not**
either of them; it holds only the outstanding fetch queue.

**Codes.** Every bibliography and wishlist item carries a project-wide unique code (stream prefix, e.g.
`P3-001`), used whenever the item is referred to. The code is internal-only (never in the published
bibliography); it appears in the internal bib records, the wishlist, and (for un-fetched items) the drop-name.

**Separate paper text from reference-list text.** When reading/grepping a PDF, keep a hit in the paper's
body distinct from a hit in its **reference list**. A grep match inside a cited reference's title is not the
same as a match in the paper's own text, and must not be treated as the paper making that statement. Quote
or tag accordingly (e.g. "cited-title match only", not a `[VERIFIED src]` claim from the paper body).

Evidence tags: `[VERIFIED src]`, `[VERIFIED-ABSTRACT]`, `[FIGURE]`, `[SUPPLIER]`, `[IN-HOUSE]`,
`[UNVERIFIED]`, `[DATA REQUIRED]`. See `CONVENTIONS.md` §3.