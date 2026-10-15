# tex/ - manuscript sources

| Path | What |
|---|---|
| `main.tex` | Driver: document class, journal layout lines, `\input`s only (no prose) |
| `preamble.tex` | Journal-neutral packages and marker macros (`\assumed`, `\prov`, `\pending`, `\todoA`) |
| `sections/` | One file per section: frontmatter, abstract, author-summary, introduction, methods, results, discussion, backmatter |
| `tables/` | Large tables (CLSI Table 7 descriptor incidence; R3 CPE-type morphology by source) |
| `references.bib` | Bibliography |
| `DRAFT.md` | Source notes with verbatim guideline quotes (kept unchanged) |
| `FRAMING_LIMITATIONS_ANONYMITY.md` | Framing, limitations and anonymity rules for the paper |
| `wrk/paper_notes.md` | Section status, assumption register, open author decisions |

Build: `pdflatex main && bibtex main && pdflatex main && pdflatex main`. To adapt to a journal, replace the class/geometry/bibliography-style lines in `main.tex` with the journal template and keep the `\input` lines; flatten with `latexpand` if the journal requires a single file (PLOS does).
