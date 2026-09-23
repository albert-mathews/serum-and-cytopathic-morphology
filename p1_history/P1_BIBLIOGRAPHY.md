# P1 research bibliography (public)

**File of record:** [`P1_screened.csv`](P1_screened.csv)  
**Purpose:** Full list of sources **screened** during P1 historical research (useful, borderline, not useful).  
The published paper can point reviewers here.

**Paper-facing subset:** [`P1_for_paper.md`](P1_for_paper.md)  
**Extracts:** [`P1_useful.csv`](P1_useful.csv), [`P1_quotes.md`](P1_quotes.md)

---

## Integrity rule (read this)

**If an identifier is not certain, the field is left blank.**

We do **not** invent DOI, PMID, PMCID, volume, or pages to look complete.  
A reviewer who needs more can use `citation` + `title` + `authors` + `year` + `notes` / `id_basis`.

| Field | When filled |
|-------|-------------|
| `doi` | Printed on held PDF, or PSGBM DOI matching article number on PDF/filename (documented in `id_basis`) |
| `pmid` | Only if verified on a held source (currently often blank) |
| `pmcid` | Only if in our PMC-sourced PDF filename or printed on PDF |
| `other_id` | DTIC AD on PDF, CLSI code, PSGBM article number on PDF, book key, etc. |
| `stable_url` | Only when it is a durable resolver for a filled ID (e.g. `https://doi.org/...`) or official Nobel URL |

`id_basis` always explains **why** any machine ID is present (or is empty).

---

## Counts (this build)

| Metric | n |
|--------|---|
| Screened rows | 57 |
| Rows with any machine ID | 19 |
| With DOI | 2 |
| With PMID | 0 |
| With PMCID | 2 |
| With other_id | 16 |
| Paper spine (`paper_spine=Y`) | 8: P1-001, P1-002, P1-008, P1-018, P1-046, P1-047, P1-048, P1-206 |

---

## Column dictionary

| Column | Meaning |
|--------|---------|
| `id` | Project ID `P1-###` |
| `year` | Year if known; else blank |
| `authors` / `title` / `journal_or_source` / `citation` | Bibliographic text (may be incomplete if unknown) |
| `doi` / `pmid` / `pmcid` | Machine IDs **only if certain** |
| `other_id` / `other_id_type` | Non-DOI/PMID identifier when certain |
| `stable_url` | Resolver URL only when justified |
| `id_basis` | Evidence for any filled machine ID |
| `useful` | `Y` / `B` / `N` screen result |
| `reason` | Screen reason |
| `fulltext` | `Y` / `partial` / `N` |
| `lead_source` / `round` | How/when entered |
| `paper_spine` | `Y` / `optional` / `institutional` / `N` |
| `alias_of` | Canonical ID if duplicate |
| `notes` | Free notes |

---

## Aliases

| Alias | Canonical |
|-------|-----------|
| P1-019 | P1-048 |
| P1-020 | P1-014 |
| P1-028 | P1-010 |
| P1-036 | P1-008 |
| P1-203 | P1-018 |
| P1-204 | P1-035 |

---

## Rebuild

```text
python p1_history/_notes/build_p1_bibliography.py
```

Edit `ROWS` in that script; re-run; commit CSV + this README.

---

*Incomplete identifiers are intentional. Incorrect identifiers are not.*
