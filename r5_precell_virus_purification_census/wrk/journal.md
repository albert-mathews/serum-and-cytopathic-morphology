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
- **Friedewald 1944**: "purified" influenza from eggs co-purified with a normal allantoic-fluid component that
  cross-reacted serologically — the bulk/HA route did not cleanly separate "virus" from normal host material.
- **Cost strand (the counter-hypothesis a):** Enders/Weller/Robbins Nobel Lecture (1954) frames tissue culture as
  cheaper and yielding more than monkey passage — so the record contains *both* motives; R5-C is genuinely open.

Also flagged, NOT R5 (tabled for a decision):
- **Point 8 — alternative (non-viral) mechanisms of plaque/CPE formation** "if the inoculum held no virus." This
  is a cell-culture mechanistic question, not pre-cell-culture history; its natural home is an R3/CRO extension or
  a new R6 stream, not R5. Await Albert's call.

*End of journal.*
