# VIRPRO1013 analogs — search log

**Task:** Find master-seed / extraneous-agent testing SOPs in jurisdictions other than
USDA APHIS, and capture growth vs maintenance FBS% (esp. the maintenance-medium range,
which for VIRPRO1013.04 is 5–20%).

**Anchor (already known):** USDA APHIS CVB VIRPRO1013 / SAM312 — vaccine master-seed
(MSV) extraneous cytopathogenic-agent testing. Growth medium ~5–10% FBS; maintenance
medium ~5–20% FBS (hold or increase); endpoint = CPE for extraneous agents.

**Evidence tags:** [VERIFIED src] read in document · [VERIFIED-ABSTRACT] snippet/abstract
only · [PAYWALL/wishlisted] · [UNVERIFIED]. DOIs never guessed. No patents searched.

---

## Search round 1 (targeted fetches)

| # | Query / URL | Result | Notes |
|---|-------------|--------|-------|
| 1 | EMA veterinary quality page (`.../veterinary-regulatory/research-development/quality`) | 404 | wrong URL; need CVMP guidance path |
| 2 | WOAH terrestrial manual online access landing page | nav shell only | no protocol text; need specific chapter PDF |
| 3 | Guessed EMA guideline PDF + WOAH vaccine PDF | 404 both | stopped guessing URLs |
| 4 | DuckDuckGo "European Pharmacopoeia extraneous agents test veterinary vaccines virus seed" | **fruitful** | located: EMA Q&A (EA mgmt IVMPs), Ph.Eur. 2.6.24 (drugfuture EP7 mirror), VICH GL44, EDQM "new approach" paper, Ph.Eur. 5.2.4 |
| 5 | DuckDuckGo "Pharmacopoeia 5.2.4 cell cultures veterinary vaccines serum concentration growth maintenance" | **fruitful** | located drugfuture EP7 `50204E.PDF` (5.2.4) + BP Appendix XV J mirror (plain HTML) |

## Fetched in full ([VERIFIED src])

- Ph. Eur. **5.2.4** Cell cultures for production of veterinary vaccines — via BP
  Appendix XV J (Vet) 1 mirror (plain HTML). → **no serum % specified**; medium = "same
  medium and additives... as those used for the preparation of the vaccine".
- Ph. Eur. **2.6.24** Avian viral vaccines: tests for extraneous agents in seed lots —
  via drugfuture EP7 `20624E.PDF` (pymupdf text). → **no serum % specified**; serum only
  constrained by §7 antibody-freedom. Also captured 2.6.25 (finished product).

## Fetched in snippet only ([VERIFIED snippet])

- EMA/CVMP Q&A "management of extraneous agents in IVMPs" (PDF) — located, not yet read.
- VICH GL44 (general principles & lists for EA testing) — located, not yet read.
- EDQM "new approach" 2020 paper — located (context; not a serum question).

## Findings to record

(see `VIRPRO1013_analogs.md`)