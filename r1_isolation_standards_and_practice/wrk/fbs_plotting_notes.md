# R1 FBS plotting — decisions & notes (v2)

Companion to `plot_fbs_distributions_v2.py` and `fbs_distribution_plots_v2/`.

## Health Canada — range consolidation decision (owner, 2026-11-06)

**Row:** `institution-guideline-protocol-refs.csv` — "Health Canada / CCDR Measles
Surveillance Lab Support (B95-a)".

**Source wording (verbatim, from the institution notes field):**
> "B95-a growth sustained by adding **5% to 10% FBS**; FBS used at **2%** for cell
> maintenance during viral isolation."

**Decision:** For the numeric institutions overlay, the growth range **5–10%** is
consolidated to a **single representative value of 7.5%** (the midpoint), and treated as a
plottable data point rather than excluded. The post/maintenance value is the clean **2%**.

**Rationale (owner):** the guideline does genuinely specify a 5-to-10% growth window; 7.5%
is the midpoint used only to put *one* consumable point on the distribution. This is data
consolidation for readability, not an assertion that Health Canada wrote "7.5%". The verbatim
"5% to 10%" remains preserved in the institution CSV notes field and the quotes doc.

**Traceability rule:** wherever this 7.5% appears in a figure/table, it shall be accompanied
by (or link to) the fact that it represents the 5–10% range. Do not silently render it as a
measured value.

## Implementation status

**IMPLEMENTED (option (a), 2026-11-06).** `plot_fbs_distributions_v2.py::load_institutions`
special-cases the Health Canada row: it maps the growth cell `5-10%` → `7.5%` *before*
`parse_fbs()` runs (which otherwise excludes range cells), with a code comment pointing to
this note. Result: Health Canada reappears in the institutions overlay at pre=7.5, post=2;
institutions n = 8.

- The paper-side range policy (exclude ranges from the numeric KDE) is **unchanged** — the
  consolidation applies to the institutional overlay only.
- The verbatim `5-10%` / "5% to 10% FBS" wording remains in
  `institution-guideline-protocol-refs.csv` (Notes) and is not edited.

**Traceability reminder:** any figure/table showing Health Canada at 7.5% growth must carry
(or link) the note that 7.5% is the consolidated midpoint of the stated 5–10% range.