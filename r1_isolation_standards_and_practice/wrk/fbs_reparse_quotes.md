# R1 FBS re-parse — verbatim quotes (audit response)

Companion to `fbs_reparse_comparison.md` and `isolation-refs_reparse.csv`.
Every quote below is verbatim from the source document (PDF or open-access full text);
provenance per item. Ellipses `…` mark elided text, not paraphrase.

---

## VI13 — SARS-CoV-2 (CDC EID, 2020)
Source: local PDF.
- "DMEM … supplemented with heat-inactivated fetal bovine serum (**5% or 10%**) and anti[biotics]"
- "DMEM containing **10% fetal bovine serum**, 2× penicillin…"

→ pre is "5% or 10%" (either/or), post = 10%. No serum reduction.

## VI25 — Ebolavirus isolation (MDPI Viruses 2019)
Source: local PDF.
- "Vero E6, Huh-7, and MDM cells were grown … in DMEM with **10% HI-FBS**"
- "…supplemented with **2%** US-origin, certified HI-FBS …" (overlay steps)
- "Each test sample was serially diluted 1:10 … in α-MEM enriched with **10%**"

→ pre = 10%; post is heterogeneous (2% overlay, 10% elsewhere), not a 2–10 range.

## VI30 — Influenza A clinical isolates, Shanghai (2022–23)
Source: local PDF.
- "We used Eagle's Minimum Essential Medium (EMEM) … supplemented with **Fetal Bovine Serum
  (FBS) and 1% Penicillin-Streptomycin (PS)** to culture the clinical samples of IAV."
  → **no serum % stated anywhere.**

→ FIXED: paper states NO numeric FBS%. Prior cell `0-2 (often serum-free…)` was editorial, not
quoted. fbs_coded=no.

## VI33 — MERS-CoV dromedary camels (2023)
Source: local PDF.
- "…with **10%** heat-inactivated fetal bovine serum (Gibco, United States)"
- "The inoculum was removed, cells were gently washed three times **with DMEM, and a fresh
  medium was added**." → no post FBS %.

→ post unstated (audit correct). fbs_coded=no.

## VI34 — Canine adenovirus type 2, raccoon dog (2024)
Source: local PDF.
- "[MDCK cells grown] … DMEM containing … fetal bovine serum (FBS; Gibco BRL, USA)" (growth)
- "After removing the fecal samples, **1 mL DMEM containing 5% FBS was added to each well.**"

→ FIXED (inverts audit): post = **5% FBS** stated verbatim. Was "not explicitly detailed" →
now fbs_coded=yes, post=5.

## VI36 — Chikungunya (Vero) (2023)
Source: local PDF.
- "Vero cells were cultured in DMEM with **10%** of FBS…"
- "…the viral inoculum was removed and **500 µL of DMEM containing 2% FBS and 1.5%
  carboxymethylcellulose** was added" (plaque overlay)

→ 2% verbatim but is a **plaque overlay**, not "maintenance". Number correct; label imprecise.

## VI38 — SARS-CoV-2 trypsin entry (2022)
Source: local PDF.
- "[Vero] … supplemented with **10% FBS**, penicillin-streptomycin"
- "…then propagated in **FBS-free medium with trypsin**"

→ post = 0 verbatim. Correct.

## VI217 — PIV/PRCV antiviral (van der Strate, Antiviral Res 2003)
Source: archived quote (original extraction); open-access full text confirmed.
- pre: "grown in Eagle's minimal essential medium (MEM) … supplemented with **10% foetal calf
  serum (FCS)**, 100 U/ml penicillin and 100 μg/ml streptomycin."
- post: "For cell-maintenance the foetal calf serum concentration was lowered to **2% for ST
  cells and to 0% for Vero76 cells and MDBK cells**, respectively."

→ multi-line: 2% (ST), 0% (Vero76/MDBK). Do not collapse.

## VI220 — JEV glycoproteins (Mason, Virology 1989)
Source: archived quote; full text (PMC) is abstract-only for this paywalled Elsevier item.
- pre: "Vero … grown … in Eagle's minimal essential medium (MEM) supplemented with **5% heated
  fetal bovine serum (FBS)** … [C6/36 with **10%**]"
- post: "containing less FBS: **1%, Vero cells; 2%, C6/36 cells**). Following 1 hr of virus
  absorption."

→ multi-line: Vero 5→1, C6/36 10→2. Do not collapse.

## VI227 — IBDV (Silva, Braz J Poult Sci 2004)
Source: redalyc PDF + archived quote.
- pre: "The growth medium for CER and Vero cells was used as described by **Cardoso et al.
  (2000)** and Ferreira et al. (2003)." → no %.
- post: "maintenance medium consisting of minimum essential medium (MEM), antibiotics and
  **2% of calf serum** was added."

→ pre defers (no %), post = 2% calf serum. fbs_coded=no.

## VI230 — Influenza rapid isolation comparison (1982)
Source: archived quote (OCR).
- pre: "**5-10%** fetal calf serum (FCS) and were maintained in"
- post: "similar medium with **1-2% FCS**. Prior to inoculation … remove the serum."

→ true ranges; no midpoint.

## VI232 — WNV assay (Deas, J Virol 2005)
Source: archived quote.
- pre: "A reporting **BHK** cell line … maintained in DMEM with **10% FBS**" (companion line)
- post: "**Vero** cells … cultured in minimal essential medium supplemented with **2% FBS**,
  2 mM L-glutamine, 0.3% sodium bicarbonate…"

→ FIXED (audit correct): pre belongs to companion BHK line → blank; post = 2 (Vero). fbs_coded=no.

## VI233 — human rhinovirus (1998)
Source: archived quote.
- pre: "[seeding growth FBS% not separately quantified in isolation paragraph]"
- post: "HeLa cells were maintained in BME … containing **2% inactivated fetal calf serum** …"

→ pre not stated, post = 2. fbs_coded=no.

---

## Un-flagged but surfaced during re-parse (for awareness)

- **VI30** also confirms the pre cell was fabricated (see above) — the audit listed it as
  "correct exclusion" for *post*, but the *pre* was equally non-verbatim.
- The parser's `NUM_RE` fallback is the single root cause of Categories 1 and 3; fixing it
  (reject cells that say "not/implied/companion/post-Xh", and stop mid-pointing ranges)
  removes both false-positive and collapse classes.