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

## 3. Evidence tags
Every quantitative or extractive claim carries one of the house tags:
`[VERIFIED src]` (read in the document), `[VERIFIED-ABSTRACT]` (snippet/abstract only), `[FIGURE]` (read
off a plot), `[SUPPLIER]`, `[IN-HOUSE]`, `[UNVERIFIED]`, `[DATA REQUIRED]`.

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