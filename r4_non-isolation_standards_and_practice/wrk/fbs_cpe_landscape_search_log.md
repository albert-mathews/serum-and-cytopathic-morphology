# FBS × CPE landscape — search log

**Task:** omnibus survey — every institutional/regulatory/research setting where FBS is
used in cell culture AND CPE is an observed outcome (the outcome, or one of several).
Also: prior-art check (has anyone mapped this?).

**Evidence tags:** [VERIFIED src] read in full · [VERIFIED snippet] · [PAYWALL/wishlisted].

---

## Round 1 — human biologics (direct fetches, [VERIFIED src])

| Document | Source | Page count | Serum-% result |
|---|---|---|---|
| ICH Q5A(R2) 2023 | database.ich.org | 52 | 0 concentration mentions; serum = raw-material viral-safety item |
| ICH Q5D | database.ich.org | 17 | cell-substrate characterization; no serum-% recipe |
| Ph. Eur. 2.6.16 (human EA) | drugfuture EP7 20616E.PDF | 2 | serum = antiserum/complement reagent only |
| Ph. Eur. 5.2.3 (human cell substrates) | drugfuture EP7 50203E.PDF | 4 | "complies with Bovine serum (2262)" — quality deferral |
| Ph. Eur. Bovine serum (2262) | drugfuture EP7 2262E.PDF | — | protein/osmolality/globulin QC; serum tested FOR CPE agents; no culture % |
| 21 CFR 610.18 "Cultures" (US human) | ecfr.gov | — | tests "may be required by the Director"; no serum % |

## Round 2 — prior-art check (delegated; PubMed E-utilities)
Result: **no prior FBS×CPE landscape exists** (first-to-map). Full lead list + tags in
`fbs_cpe_landscape.md`. Caveat: PubMed only; Scholar/preprints unswept.

## Round 3 — search-engine availability note
DuckDuckGo began CAPTCHA-blocking after ~3 queries; Bing returns dictionary drift
("USP"→UPS shipping). Reliable routes that worked: **direct known-document fetches**
(eCFR, database.ich.org, drugfuture.com EP7 mirror, woah.org, ema.europa.eu, vichsec.org)
and **PubMed E-utilities**. Future rounds should prefer these.

## Open (next steps)
- Diagnostic-virology practice (TCID50/plaque/neutralization/shell-vial) at institutional
  level: WHO Global Influenza/measles manuals already partly in R1; need the titration-
  assay serum recipes (practice corpus, not regulator).
- Vaccine-manufacturing upstream serum practice (human & vet) — publisher Methods.
- Other CPE disciplines: mycoplasma, toxoplasma, antiviral/cytotoxicity screens,
  oncolytic/vector potency, bioburden adjuncts.
- Sweep Google Scholar / preprints to harden the prior-art negative.

## Round 6 — bioRxiv/medRxiv + Google Scholar (prior-art closure attempt)
- **bioRxiv/medRxiv API**: 403 Forbidden even with browser UA (CloudFront IP-level bot
  armor). Needs a human/browser check — see `r4.md` TODO.
- **Google Scholar**: bot "session verification" wall (same class of armor). Needs manual.
- Both are the only two remaining indexes un-swept; everything else (PubMed, Crossref,
  Zenodo, arXiv, Europe PMC incl. preprints) already concurs on **no prior landscape**.

## Round 7 — fetched-ref extraction (6 PDFs → text, [VERIFIED src])
Owner fetched the 6 wishlist PDFs; extracted full text to `refs/_txt/` (gitignored) and
pulled serum-% / growth-vs-maintenance lines. Findings summarized in
`fbs_cpe_landscape.md` §"Fetched-ref extraction". Highlights:
- 1963 measles (Moura): explicit **10% calf-serum growth → 2% maintenance**, plus a
  serum-*type* (calf vs sheep) effect on CPE morphology & titer — the closest prior
  experimental germ.
- 1978 serum-free maintenance: **10% bovine growth → serum-free maintenance** recovered 151
  strains; cites Baron & Low 1955 (Science) "New maintenance medium" (P1 lead).
- 2019 PCV2: CPE in serum-free cell lines (CPE not serum-dependent).
- 2013 contaminants + 2020 Argentine FBS: serum-as-analyte (screened for pestivirus/mycoplasma).

## Round 8 — full read + gitignored reading notes
Read all 6 fetched refs in full; wrote `refs/_notes/R4_fetched_reading_notes.md`
(gitignored) with verbatim quotes + thesis relevance. Wrapped P4 handoff (3 pestivirus
serum/cell-line refs → R4 wishlist R4-S7/S8/S9 + landscape serum-contaminant strand);
deleted `P4_handoff_to_R1.md`. Flagged 1978 paper to P1 (`p1.md` TODO #9).

## Round 9 — adversarial / gap-fill sweep (Europe PMC)
Two gap-fill findings recorded in `fbs_cpe_landscape.md` §"Adversarial / gap-fill sweep":
(1) "serum starvation / low-serum morphology" literature (181 hits) — modern non-virology
body showing serum reduction → morphology change (supports R3 premise; not prior art).
(2) "serum-free cell-line CPE assay" cluster (CPK-NS, Sf9, etc.) — CPE scored across the
serum spectrum; serum changes amount/morphology scored, not the presence of the label.

## Round 4 — practice-trawl reconnaissance (Europe PMC batch queries)
Abstracts for the non-Isolation CPE disciplines (TCID50/plaque ~6 hits; antivirals ~7;
mycoplasma ~54; toxoplasma ~14) show: **serum % almost never appears in abstracts** — it
lives in Methods full-text (paywalled/open). So the practice layer needs full-text Methods
extraction (the R1 dual-FBS approach extended to non-Isolation assays). Key identified
landscape-relevant papers (for the practice corpus):
- Toxoplasma gondii plaque assays revisited (2017), PMID 28011168 — plaque/CPE protocol
- Detection of contaminants in cell cultures, sera and trypsin (2013), PMID 24071554
- Analysis of irradiated Argentinean FBS for adventitious agents (2020), PMC7649553
  (full-text endpoint 503s — retry)
- Serum-free maintenance / CPE studies (1963 measles serum→CPE; 1978 SF-maintenance
  virus-detection; 2019 PCV2 serum-free CPE — see landscape prior-art section)
**Conclusion:** disciplinary practice-trawl = multi-session R1-style corpus build; scoped
and logged, not half-executed.

## Round 5 — prior-art hardening (Crossref, Zenodo, arXiv, Europe PMC PPR)
No landscape in any index. Prior *germs* (credit-worthy, not landscapes) identified:
1963 "influence of serum on CPE of measles virus" (10.1007/BF01241302); 1978 serum-free
maintenance virus detection (10.1111/j.1439-0450.1978.tb00729.x); 2019 PCV2 serum-free CPE
(10.1016/j.jviromet.2019.113706). bioRxiv/medRxiv API 403-blocked (agent UA); Google Scholar
not swept. See `fbs_cpe_landscape.md` prior-art section for the full credit list.