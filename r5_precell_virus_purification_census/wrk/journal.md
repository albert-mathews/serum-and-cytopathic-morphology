# R5 working journal

**Role:** Founding record and live working notes for the r5 pre-cell-culture bulk-purification census. Paper
text stays in `tex/` and `r5.md` Snippets; this file is where the *how/why/what-next* lives.

## Founding (2026-11-17)

**Trigger.** While drafting the Introduction, a historical claim needed support: that bulk virus
purification/crystallization was confined to plant viruses and bacteriophages before cell culture, and that no
animal virus was crystallized until after cell culture (poliovirus, 1955). Albert asked *why* this asymmetry
exists and *exactly how many* viruses were bulk-isolated pre-1949, "by what methods" — and directed that we
**know, not guess**.

**Placement decision.** This is a distinct research object (purification/crystallization history) from P1 (serum
/ nutrient medium practice). P1's protocol explicitly excludes "pure purification literature" and non-cell-culture
plant/egg work, so it cannot host this without violating its own scope. → new stream **r5**, folder
`r5_precell_virus_purification_census/`, sibling to `p1_history`. (Re-home if Albert prefers another slot; nothing
here is load-bearing yet.)

## The question, precisely

> Before cell culture (Enders–Weller–Robbins 1949), how many viruses were bulk-isolated and physically
> characterized, by what methods, across three groups (plant / phage / animal)? And was any animal virus
> crystallized before cell culture?

## What "we know, not guess" requires

1. An **exhaustive per-item table**, not a range repeated from memory.
2. **Primary citations** for each item; secondary corroboration is labelled, not treated as the primary.
3. An explicit **per-candidate table for "0 animal viruses crystallized pre-1949"** (absence needs enumeration).
4. Evidence tags per CONVENTIONS §3 — `[DATA REQUIRED]` until a primary full text is read.

## Asymmetry mechanism (why bulk was easy for plant/phage, hard for animal)

Working list to keep grounded against primaries:

1. **Yield** (decisive): TMV ≈ large fraction of infected-leaf protein → grams/plant; animal viruses low-yield/host.
2. **Host scalability/cost**: plants + broth scale trivially; animals/eggs don't.
3. **Stability**: TMV naked/rigid/stable survives salt+acid; most animal viruses enveloped/labile.
4. **Starting-material cleanliness**: leaf sap vs animal tissue/fluid (host protein/lipid/membrane).

Actual scale contrast (full text, R5-009/010): influenza bulk prep used **1,395 embryonated eggs → 7.8 L
allantoic fluid → 1–10 mg virus/cc**; Stanley 1944 (J Exp Med 79:255), 1945 (J Exp Med 81:193).

## Immediate next steps

- [ ] Albert drops the `R5W-*` PDFs into `refs/`; assistant confirms + removes wishlist rows.
- [ ] Round 2 systematic queries (plan in `R5_research.md` §6) — do after seeds are fetched.
- [ ] Adversarial Round 4: enumerate pre-1949 animal-virus candidates and confirm each one's purification status.
- [ ] Reconcile "more than a dozen plant viruses crystallized by 1938" (secondary) against primaries.
- [ ] Freeze → `R5_synthesis.md` → add `OB###`/comparable claim to `CLAIMS.md` → back the Introduction wording.

## Provisional tallies live in `r5.md` and `R5_synthesis.md` (single source of truth: `R5_synthesis.md` once frozen).

## Scope sharpened by Albert (2026-11-17, evening)

Albert's skepticism reframed what R5 must answer. The naive census ("how many bulk-purified pre-1949") is **R5-A,
necessary but insufficient**. The deeper question — and the one that makes R5 relevant to the paper — is **R5-B:
the evidence audit**. For each pre-1949 "virus," on what warrant was the purified/observed entity declared *the
virus* / *the disease-causing agent*?

Working summary of that warrant (to be filled per item in `virus_identity_warrant`):

- **Plant viruses:** *infectivity-transmission* — inoculate purified fraction/crystals into a healthy plant →
  local lesions / mosaic at high dilution (Holmes local-lesion ~1929); plus absence-from-healthy and serology.
- **Bacteriophages:** *bacterial lysis* is the whole readout (no host "disease" beyond lysis).
- **Influenza (eggs):** *hemagglutination* (Hirst 1941) + embryo/mouse *infectivity* — an activity titer, not a
  particle observation.
- **EM "imaging a virus" (TMV 1939, influenza 1944):** *particle–activity correlation* — the homogeneous,
  preferentially sedimenting particle is equated with the infectious/HA fraction by co-purification +
  proportionality. Not molecular identification; it was corrigible (Stanley's "protein" → Bawden & Pirie's
  nucleoprotein; "crystals" → liquid-crystalline).

Key inference Albert named: **the pre-1949 warrant is transmission-and-correlation, resting on the same
"disease / death / degeneration read as 'virus present'" endpoints the paper scrutinizes in CPE.** So pre-1949
"successes" are not independent corroboration of CPE; they are earlier instances of the same epistemic move.
R5-B makes this explicit rather than citing them as molecular proof.

Also flagged for the Introduction (next revision): the **plaque assay is CPE under an overlay** (a countable
zone of cell death), not a distinct, more-validating endpoint; and **"permissive lines grew a vast range" is, on
the paper's own thesis, a census of which lines degenerate under the standard serum-drop protocol, not of true
viral replication.** Both must not be over-claimed in prose.

*End of journal (Round 1) + 2026-11-17 scope note.*

## Scope direction locked by Albert (2026-11-17, later that evening)

Albert's synthesis named what R5 must ultimately decide, and it is now **R5-C / CNJ058**: did the 1920–1950 field
adopt cell culture because the prior methods were **(a) adequate-but-costly**, or **(b) documented as
unreliable/inconsistently-reproducible/repeatedly-wrong**, with cell culture arriving as a "supposedly better"
method amid known dissatisfaction? CNJ058 predicts (b).

Early CNJ058 instances already in hand (no new fetch needed for the framing, but primaries go on the wishlist):
- **Stanley 1935 → 1936**: "crystalline protein" corrected within a year to a liquid-crystalline *nucleoprotein*
  (Bawden, Pirie, Bernal & Fankuchen, *Nature* 138:1051).
- **Sabin & Olitsky 1936**: the settled negative that poliovirus would not grow outside nervous tissue — a prior
  methodological dogma overturned in 1949 (this is *why* monkeys were the only route).
- **Knight 1944**: "purified" influenza from eggs co-purified with a normal allantoic-fluid component that
  cross-reacted serologically — the bulk/HA route did not cleanly separate "virus" from normal host material.
- **Cost strand (the counter-hypothesis a):** Enders/Weller/Robbins Nobel Lecture (1954) frames tissue culture as
  cheaper and yielding more than monkey passage — so the record contains *both* motives; R5-C is genuinely open.

Also flagged, NOT R5 (tabled for a decision):
- **Point 8 — alternative (non-viral) mechanisms of plaque/CPE formation** "if the inoculum held no virus." This
  is a cell-culture mechanistic question, not pre-cell-culture history; its natural home is an R3/CRO extension or
  a new R6 stream, not R5. Await Albert's call.

*End of journal.*

## Batch-2 processing note (2026-11-18, evening)

18 more PDFs landed (cumulative 30/36). All confirmed + recorded in `_notes/R5_extract_batch_2026-11-18_b.md`.
Two more mis-captures surfaced: **R5W-10** (fetched file is the *Lancet* 2000 Ruska essay, not the 1938 primary)
and the already-known **R5W-05** (Schlesinger). Both are **not blockers** (corroborated by in-hand secondaries:
Ackermann 2011; Northrop 1938 + Kalmanson 1939). Corrections applied: Eggers 2000→**1999** (J Virol 73:4533);
Markham 1942 → **Markham, Smith & Lea**; van Helvoort 2019 → **van Helvoort & Sankaran**; R5-015 primary = Klin
Wochenschr 17(27):921–925 (DOI 10.1007/BF01775798), secondary Lancet 2000 in hand. Books are Archive.org-borrow /
hard-copy only (no purchasable PDF) — wishlist marked LOW/optional.

**Synthesis (the "enough?" judgment).** Core R5-C is now answerable: 28 full-text sources span the primaries
(Stanley 1935, Bawden–Pirie 1936/37, Knight 1944, Smadel 1939, Sabin–Olitsky 1936, Hirst 1941, Ellis–Delbrück
1939, Hershey–Chase 1952) and the historiography (van Helvoort 1991/1992/1994/2019, Kay 1986, Méthot 2016,
Summers 1993, Eggers 1999, Ackermann 2011, Hsiung 1984). The remaining wishlist items are optional depth, not
required for certainty.

## Final note (2026-11-18, end of processing)

- **R5W-10 re-fetched correctly** as the 1938 Klin Wochenschr primary (confirmed `Bakterien und Virus in
  übermikroskopischer Aufnahme`, Mausektromelie EM); the earlier mis-captured file renamed `R5-045 - Lancet 2000…`.
- **R5W-017 (McClelland & Hare 1941) unavailable — dropped** (only corroborates Hirst 1941, already held).
- **`R5_synthesis.md` drafted**: R5-A census, R5-B evidence audit, R5-C transition motive, plus paper-ready
  Introduction prose (§6).
- **CNJ058** advanced predicted → **supported** in `CLAIMS.md`.

## Batch-1 processing note (2026-11-18)

12 PDFs landed in `refs/`. Processed: extracted text (PyMuPDF via `wrk/extract_pdf_text.py`) or OCR'd the two
image scans (R5W-05, R5W-12), confirmed identity, and recorded quote-sized extracts in
`_notes/R5_extract_batch_2026-11-18.md`.

- **Confirmed + marked [VERIFIED src]:** R5-001 Stanley 1935; R5-002 Bawden/Pirie 1937; R5-006 (Kausche 1939);
  R5-013 Goodpasture 1931; R5-014 Bernal/Fankuchen 1941; R5-016 Bawden 1936 (the Stanley correction);
  R5-017 Hirst 1941; R5-018 (allantoic component — **Knight CA 1944**, not Friedewald); R5-020 Enders Nobel
  1954; R5-022 Kay 1986; R5-029 (**Hsiung GD 1984**, not "2014/author TBC").
- **Not confirmed:** R5-007/R5W-05 Schlesinger — the fetched PDF is mis-captured *Nature* pages (position
  effect, eel-grass, Allium letters; no phage content). Left on wishlist for re-fetch; kept [DATA REQUIRED].
- **Corrections this exposed (errors I'd recorded earlier, now fixed):** "Friedewald 1944" → **Knight CA 1944**
  in `CLAIMS.md` CNJ058, `r5.md`, and this journal; Hsiung author/year; R5W-11 also confirmed as Smadel/Rivers/
  Pickels 1939 (still needs the PDF fetched).
