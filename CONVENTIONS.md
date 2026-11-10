# CONVENTIONS — repo-wide working language

Single reference for the rules every agent and every tracked file follows. Claims live in `CLAIMS.md`;
this file holds everything else that must be spoken the same way across all streams.

## 1. Claims (the argument spine)
- Every load-bearing assertion has a `C###` ID in [`CLAIMS.md`](CLAIMS.md) with a kind: **axiom**,
  **definition**, **observation**, **lemma**, **theorem**, **corollary**, **conjecture**, **counterexample**.
- Cite `C###` instead of restating a claim; put new or updated claims in `CLAIMS.md`, not in a stream file.
- When a number changes (corpus n, tier counts, rater sums), update the claim there and keep the stream's
  own table in sync.

## 2. Diagrams — Mermaid (repo-wide)
- **All** diagrams in Markdown are Mermaid code blocks (```` ```mermaid ````). No ASCII-art boxes, no
  hand-drawn arrow-in-text diagrams, no raster image used as a substitute for a sourceable diagram.
- Keep the Mermaid source beside the prose it explains. It must use standard Mermaid syntax that renders
  on GitHub (no private graph tooling).

## 3. Sources and evidence tags

**Abstract-only research is not allowed.** An abstract (or search snippet) may be used only to *identify* a
potential source that must then be read in full; it is not a basis for a load-bearing claim, a corpus field,
or a paper-ready sentence. A claim that rests only on an abstract is `[DATA REQUIRED]` until the full text is
read, not `[VERIFIED-ABSTRACT]`.

- An abstract-only source goes on the stream's PDF wishlist (full text to be fetched) and its claim is
  deferred. Until then it is flagged `full text outstanding`, never quoted as settled evidence.
- `[VERIFIED src]` means read in the full document.
- `[VERIFIED-ABSTRACT]` is retained **only** as a *provenance marker for pre-existing abstract-derived
  material* (material already recorded before this rule); it is not an acceptable evidence tag for a new
  claim. New abstract-derived material is `[DATA REQUIRED]` until the full text is read.

Every quantitative or extractive claim carries one of the house tags:
`[VERIFIED src]` (read in the full document), `[VERIFIED-ABSTRACT]` (legacy provenance marker — abstract
only, not a claim basis), `[FIGURE]` (read off a plot), `[SUPPLIER]`, `[IN-HOUSE]`, `[UNVERIFIED]`,
`[DATA REQUIRED]`.

## 4. Identity / anonymity
Tracked files use role codes only (CRO, IR1, IR2, IR2v, IR3v, or pilot codes). Real names of raters,
freelancers, and CRO staff live only in the gitignored paths named in `grok_guardrails.md`. No real names
in tracked files, commit messages, branch names, or headings.

## 5. Stream discipline
- One TODO list per stream, in that stream's main `rN.md` / `pN.md`. No parallel TODO systems.
- Prefer updating existing notes / CSVs / frameworks over replacing them.
- Prefer paper-ready sentences from a stream's Snippets section over improvised strong language.

## 6. File placement
- Full-text PDFs only under gitignored `refs/`. Never commit PDFs or other copyrighted full texts.
- Working/scratch notes under tracked `wrk/`. No new top-level scratch files.
- Quotes stay quote-sized and attributable; never paste a whole paper into a tracked file.

## 7. No commit / no push
Leave changes in the working tree for GitHub Desktop unless Albert explicitly asks to commit or push.

## 8. Research strategy (all agents)
- Literature work follows [`agent-settings/research-strategy.md`](agent-settings/research-strategy.md); find
  publications from any legitimate source of record.
- A paywalled/blocked full text is logged in the stream's `<STREAM>_pdf_wishlist.md` with columns:
  **title · year · author · identifier (PMID/DOI/stable URL) · drop-as filename** (saved into
  `<stream>/refs/`). One row per document; the owner fetches. Until the full text is read, the claim stays
  `[DATA REQUIRED]` (full text outstanding). Never guess a DOI/locator.
- A scanned (image-only) PDF is OCR'd with `tools/ocr_pdf.py` before extraction; improvements go back into
  that tool so future agents inherit them (see `tools/README.md`).

## 9. Python environment (all agents)
- Run all Python through the single shared venv `tools/venv` (gitignored), recreated from
  `tools/requirements.txt`. See [`agent-settings/environment.md`](agent-settings/environment.md). No
  per-stream venvs.