# Category re-categorization decisions (owner-reviewed, 2026-11-10)

Record of owner decisions on the re-parse of `isolation-refs*.csv` for category 2 (institutional/SOP) vs category 3 (methods-review/teaching) moves. **No physical moves done yet** in this pass unless noted.

## Definitions used
- **Category 1** = primary virus-isolation publication (default corpus member).
- **Category 2** = institutional / SOP / protocol (lives in `institution-guideline-protocol-refs.csv` + `refs/isolation_protocols/`).
- **Category 3** = methods-review / teaching / comparison-without-primary-isolate (lives in `refs/methods_review_teaching/`).

## Owner decisions

| ID | Decision | Rationale (owner) | Action taken |
|---|---|---|---|
| **VI237** | Move to **category 2** | protocols.io clinical-isolation SOP (Nagy, Hungarian NPHC). Equal 5→5 hold, non-stepdown | **Agreed.** Destination = institutional set. Physical move pending confirmation of target (see note below). |
| **VI107** | **Undecided** | — | Summary written (`VI107_summary.md`). Recommended category 3 (cell-system comparison, no single primary isolate). Await owner call. |
| **VI252** | **Keep in VI** | "looks like virus isolation, but swapping the cell lines" | Summary written. Keep category 1. |
| **VI230** | **Keep in VI** | "developing a protocol… but doing virus isolation practically… to evaluate lower-cost cells" | Summary written. Keep category 1. |
| **VI225** | **Keep in VI** | "same as VI252 and 230" | Summary written. Keep category 1. |
| **VI111** | **Keep in VI** | "they were sort of looking for viruses" | No summary requested. Keep category 1. |
| **VI117** | **Undecided** | "is this not an interesting experiment for us? are all their cultures 'infected' or some uninfected?" | Summary written (`VI117_summary.md`). Answer: uninfected controls existed; viruses were laboratory-propagated (not field isolates); recommended category 3 but flag as substantively interesting for the confounding question. Await owner call. |
| **VI91** | **Keep in VI** | "not doing isolation, but cell culture with virus addition, following the protocol. it's a data point that the protocol is followed." | No action. Keep category 1. |
| **VI108** | **Keep in VI** | "a data point that the protocol is followed" | No action. Keep category 1. |
| **VI119** | **Keep in VI** | "same as VI108" | No action. Keep category 1. |

## My additional recommendation (awaiting owner confirmation)

| ID | Recommendation | Rationale |
|---|---|---|
| **VI254** (Mizuta JJID 2019) | Move to **category 3** | 20-year retrospective **overview/synthesis** ("Overview of activities at YPIPH 1999–2018"), not a new primary-isolation effort; its SOP Table 1 is methodological. See `Mizuta_2008_vs_2019_summary.md`. |
| **VI262** (Mizuta JJID 2008) | **Keep in VI (category 1)** | Genuine 2-year primary surveillance-isolation report (4,107 specimens → 1,551 isolates). Owner already leaned this way. |

## FINAL owner rulings (2026-11-10, second pass)

| ID | Final category | Note |
|---|---|---|
| **VI262** (Mizuta JJID 2008) | **Category 1** | Confirmed by owner. |
| **VI254** (Mizuta JJID 2019) | **Category 3** | Confirmed by owner. |
| **VI117** (Deig et al. 1970) | **Category 1** | Owner: "doesn't matter if they start with clinical samples or isolates purchased from ATCC — if they are performing the protocol, it's a data point as to whether they do according to the protocol or not." Also flagged in R2 + R3 TODOs for future processing. |
| **VI252, VI230, VI225, VI91, VI108, VI119, VI111** | **Category 1** | Confirmed by owner (prior pass). |
| **VI107, VI74** | **TBD** | Owner to read summaries/papers and comment. |

**Owner's general principle (recorded):** the categorical test for a category-1 primary is **"are they performing the isolation protocol?"** — not the provenance of the inoculum (clinical vs ATCC reference strain). A methods paper that runs real isolation is still a category-1 data point on protocol adherence.

---

## RESOLVED (2026-11-10): folder=category, column=class

The category/class split is now codified in `r1.md` §"Corpus organization":
- **category** = which FOLDER a ref lives in (isolation_practice = primary practice reports; isolation_protocols = protocols; methods_review_teaching = reviews/teaching/theses).
- **class** = the `class` column, endpoint-based, category-1 only (1 = CPE-detection, 4 = other endpoint).

**Mechanical moves executed:**
- **VI254** (Mizuta 2019) → `refs/methods_review_teaching/` as **MR001.A–H** (8 recipes); PDF renamed (VI prefix stripped).
- **VI270** (lymphocystivirus thesis) → `refs/methods_review_teaching/` as **MR002.A**; PDF renamed (VI prefix stripped).
- **VI237** (WNV protocols.io SOP) → `refs/isolation_protocols/` as **PR001.A**; PDF renamed (VI prefix stripped).
- **VI74** → class 1 (multi-endpoint: CPE + titration + neutralization), stays in isolation_practice.
- **VI107** → confirmed class 1, category 1 (stays).

**Folder CSVs created:** `refs/methods_review_teaching/methods-review-refs.csv` (MR prefix), `refs/isolation_protocols/protocol-refs.csv` (PR prefix). Each tracks its folder's refs.

The old "class 5 (thesis)" concept is retired — a thesis is a *category* (methods_review_teaching), not a class (endpoint).

---

## Institutional-set home correction (owner, 2026-11-10)

- **Master-seed / extraneous-agent protocols are NOT Isolation protocols** — they live in **R4** (`r4_non-isolation_standards_and_practice/refs/master_seed_protocols/`). This applies to **APHIS VIRPRO1013** (9 CFR §§113.55/113.46, MSV safety testing) and **APHIS SAM312**. The R1 institutional CSV row `USDA APHIS VIRPRO1013 …` is therefore **misplaced** and should be re-homed to R4 (pending: confirm whether to delete the R1 row or just annotate it). The separate **APHIS SAM 104.04** (Parainfluenza-3 *isolation*) in `refs/isolation_protocols/` **is** an Isolation SOP and stays in R1.

## Remaining institutional-PDF gaps (not yet fetched / wrong docs)

- **WHO EPI Annex B7/B8** — fetched files are wrong documents (B7 = 2025 RT-qPCR presentation; B8 = GRMLN Outbreak Response Plan `.docx`). Need the manual's actual "Annex B7 (Propagation/maintenance of Vero/hSLAM)" + "Annex B8 (virus isolation in cell culture)."
- **ANSES FMDV SOP** — site still under maintenance; no PDF.
- **CDC Measles Vero/hSLAM** — original URL 404; only `.docx` local; need replacement/archive URL.

## Open mechanical question (for owner)

VI237 → category 2: the protocol is a protocols.io SOP. To move it cleanly I need to know the target:
- (a) Add it as a new row to `institution-guideline-protocol-refs.csv`, **remove** VI237 from `isolation-refs.csv` + `isolation-refs_reparse.csv`, and move `VI237 - West-Nile-virus.pdf` → `refs/isolation_protocols/`; **or**
- (b) Some other destination.

Note also: VI262 currently has only 2 recipe rows in the CSV (HEF, RD-18S), but its Table 1 lists 6 cell lines. This is a pre-existing under-count detail, flagged for a later reconcile pass — not changed in this pass.

## Summary files written (this pass)
- `wrk/summaries/VI107_summary.md`
- `wrk/summaries/VI117_summary.md`
- `wrk/summaries/VI252_summary.md`
- `wrk/summaries/VI230_summary.md`
- `wrk/summaries/VI225_summary.md`
- `wrk/summaries/Mizuta_2008_vs_2019_summary.md`