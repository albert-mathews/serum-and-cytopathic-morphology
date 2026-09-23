# P3 warrant definition & process-code research note

**Date:** 2026-09-21 (evening ET)  
**Status:** Methodological lock for Step 1 continuation — **not** a mass recode of `path_score`.

---

## 1. Warrant (use everywhere)

**Warrant** = the *documentary claim or procedure a paper treats as establishing that the starting material / stock contains “virus”* (or is a viral isolate/stock suitable for genetics).

Examples of warrants (illustrative, not exhaustive):

| Warrant class | What the authors rely on |
|---------------|--------------------------|
| `culture_cpe` | CPE, plaques, foci, syncytia (or clear CPE-equivalent morphology) as the isolate/stock assertion |
| `animal_disease` | Animal illness + organ harvest (or similar animal-pathology readout) as the detection/production claim |
| `serology_antigen` | Antigen/serology marker (CF, ELISA, neutralizing Ab, etc.) as the primary presence claim |
| `em_density` | EM morphology ± density band (historically weak as sole warrant) |
| `named_stock_only` | Named lab stock / ATCC / vaccine vial with **no** re-demonstration of virus presence in the cited production paper |
| `sequencing_circular` | Sequence itself offered as the proof that the input was virus (circular) |
| `unclear` | Text does not state a usable warrant |

**Warrant ≠ proof.** It is what the authors *rely on in the text*. Soft evidentiary bar unchanged: documentary method↔deposit link within reasonable doubt — not forensic custody.

---

## 2. Two layers (do not conflate)

| Layer | What it scores | Where recorded |
|-------|----------------|----------------|
| **Immediate path (`path_score`)** | Production path of the *material that was sequenced* for that O/C event, once method↔deposit is adequate | `P3_sequence_origin_events.csv` → `path_score` |
| **Stock-origin warrant** | Warrant used in the *origin / isolation / first-principles stock* paper reached by hopping upstream from named lab stocks | `P3_stock_origin_hops_2026-09-21.md` + provenance nodes |

**Rule this pass:** Keep current `path_score` as the immediate sequenced-material path (documentary). Add/fill the stock-origin layer separately. **Do not** silently mass-recode the CSV to process codes because an upstream isolation paper shows CPE.

**Example (CMV-O1):** Immediate path remains Fleckenstein 1982 Ad169 virion-DNA → cosmids → Chee annotation = `culture_no_cpe` (no CPE warrant in Fleckenstein Methods). Rowe 1956 Ad169 isolation warrant (`culture_cpe` / cytopathogenic agent) is recorded at the **stock-origin** layer only.

---

## 3. Process-over-medium hypothesis (research program)

Albert’s working view: codes should eventually track **process**, not growth medium.

Putative shared thin process:

> growth system → add “virus source” → observe changes → interpret changes as virus presence

Implications framed as **research questions**, not mass recodes:

1. **Eggs without a detection step** ≈ same *thin* process class as many `culture_no_cpe` stocks (propagate → extract → sequence).
2. **Animal illness / organ harvest** is the main *other* historical detection family besides culture ± CPE.
3. **Reverse-genetics (RG) paths that end with CPE/plaque readout** as the claim that the sequence is viral should be understood as using a **culture_cpe-class warrant** (inverted order: sequence → culture → CPE), even if the sequenced material itself was plasmid-derived.
4. **Hypothesis to test via stock-origin hops:** essentially all lab stocks / genome paths eventually trace to a `culture_cpe`-class (or `animal_disease`) origin paper if searched far enough.

This pass **tests** (1)–(4) by documenting hops; Albert decides later whether to recode.

---

## 4. How RG / eggs / animal fit (open questions)

| Path pattern | Immediate `path_score` (current Step 1) | Stock-origin / process question |
|--------------|----------------------------------------|----------------------------------|
| Culture stock sequenced; CPE only in distant isolation paper | Often `culture_no_cpe` | Does hop close to `culture_cpe`? |
| Eggs / allantoic fluid; no CPE-equivalent detection stated | Often `other` or thin culture analogue | Process-equivalent to `culture_no_cpe`? |
| Animal disease + organ → culture or direct extract | `other` / `animal` family | Primary alternate detection family? |
| RG: infectious clone → CPE/plaque as “virus recovered” | Immediate may be clone/`culture_cpe` if deposit Methods use plaque/CPE as warrant | Treat terminal CPE as culture_cpe-class warrant (inverted order)? |
| Named stock only; production paper never opened | `named_stock_only` risk at origin layer | Keep hopping |

---

## 5. Operational checklist for later process recode (not this pass)

1. Leave `path_score` = immediate sequenced-material path.
2. For each priority O-event, record stock-origin hop status + origin warrant class.
3. Only after hop census: Albert decides whether to add a process code column or remap.

Exploration, not advocacy. No Sci-Hub. PDFs under gitignored `refs/sequence_origins/`.
