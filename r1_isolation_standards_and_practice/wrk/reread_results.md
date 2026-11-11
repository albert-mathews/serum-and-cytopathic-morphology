# R1 corpus — page-by-page re-read results (2026-11-10)

**Scope:** every corpus PDF re-read page-by-page (4 parallel subagent batches), plus the SPT
(single-particle-tracking) paper set parsed into new VI rows. This supersedes the earlier
`notes`-only classification and is the authoritative endpoint/class/FBS pass.

## Headline result

| metric | before | after |
|---|---|---|
| rows | 186 | **194** (+8 SPT) |
| distinct papers | 177 | **184** |
| Class 1 (CPE=detection/Isolate endpoint) | 169 | **140** |
| Class 4 (2I1D pattern, other endpoint) | 17 | **54** |
| `fbs_coded` yes / post_only / no | 162/5/18 | **179/10/5** |

The re-read **substantially grew Class 4**: many papers that run the 10%→2% (or →0%) serum
pattern were doing **titration / neutralization / antigen detection / molecular characterization /
antiviral screening / protein or particle purification** as their primary endpoint, not
CPE-as-detection of a field/clinical specimen. This is the Arg-2 evidence (the 2I1D pattern
persists across the field regardless of endpoint).

## Class 1 → Class 4 reclassifications (high confidence)

VI36, VI38, VI40, VI41, VI43, VI73, VI76, VI90, VI101, VI121, VI201, VI204, VI205, VI206,
VI209, VI214, VI215, VI216, VI217, VI222, VI224, VI228, VI229, VI231, VI244, VI281, VI289,
VI290, VI293. (29 papers.)

## FBS corrections (18 rows)

| ID | change |
|---|---|
| VI208 | pre 8 → 10 |
| VI253 | post 2 → 0 (serum-free trypsin) |
| VI269 | → post_only (pre blank; 1% is inoculation/post) |
| VI97, VI100, VI106, VI116 | → post_only, post=2 |
| VI98, VI102, VI104, VI108, VI114, VI117, VI118, VI119, VI120, VI107 | → populated (were blank) |

## NEW: SPT rows (Class 4, single-particle-tracking endpoint)

8 single-particle/virus-tracking papers added as VI295–VI302 (all Class 4, live-cell imaging /
entry-mechanism endpoint). FBS pre 10% in all; post varies (0% serum-free, 2%, or 10% hold):

- VI295 influenza (CHO) 10→0 · VI296 HIV (macrophages) 10→0 · VI297 HBV-VLP (COS-7) 10→0
- VI298 SARS-CoV-2 (HEK) 10→10 (equal hold) · VI299 VSV (HeLa) 10→2 · VI300 vaccinia (Vero) 10→2
- VI301 poliovirus (HeLa) 10→0 · VI302 polyoma VLP (3T6) 10→0 (FCS, not FBS)

**Not added (no FBS % or PDF missing):**
- SPT1 (AAV, Seisenberger 2001) — no serum % reported anywhere.
- SPT11 (HIV/HEK293T), SPT12 (influenza/MDCK), SPT13 (HCMV/MRC5) — **PDFs missing** from
  `…\virus Single virus tracking\`. Add to wishlist when fetchable.
- Review/method papers ("Virus trafficking…", "A Superhighway…", "Tracking single viruses…
  quantum dots", "Single Virion Tracking Microscopy…", "Orbital SPT…") — no FBS serum value.

## Owner-review flags (NOT silently changed)

`[OWNER_REVIEW]` tag added to notes; class held provisional. These need your read:

| ID | issue |
|---|---|
| VI13 | post=10 (no reduction); fbs_coded "yes" may be wrong |
| VI94 | deltacoronavirus surveillance; ISOLATION FAILED, primary=molecular → lean class 4 |
| VI105 | mixed 5% fetal + 5% calf serum (HRV susceptibility) |
| VI218 | detection comparison: shell-vial IFA (antigen) vs conventional CPE |
| VI233 | RT-PCR vs isolation comparison (molecular vs CPE) |
| VI234 | serum-replacement (Omni serum) comparison; endpoint is HSV isolation |
| VI270 | lymphocystivirus thesis — characterization vs isolation |
| VI273 | NNV reporter/luciferase diagnostics → lean class 4 |
| VI274 | IBDV Vero-adaptation → lean class 4 |
| VI282 | Ebola disinfection (TCID50) → lean class 4 |
| VI285 | feline SARS-CoV-2: internal 4% vs 5% FBS propagation inconsistency |
| VI292 | SARS-CoV-2 cell-systems: growth 10–20%, post 2–4% (stored 10/10 wrong) |

## FINAL owner resolutions (2026-11-10)

| ID | final class | endpoints recorded |
|---|---|---|
| VI13 | **1** | CPE + molecular |
| VI94 | **1** | CPE + molecular |
| VI105 | **1** | CPE + titration_TCID50 |
| VI218 | **1** | CPE + antigen_detection |
| VI233 | **1** | CPE + molecular |
| VI234 | **1** | CPE |
| VI285 | **1** | CPE + molecular |
| VI292 | **1** | CPE + titration_TCID50 + molecular |
| VI270 | **5** (thesis) | CPE |
| VI273 | **4** | characterization (reporter diagnostics) |
| VI274 | **4** | characterization (Vero adaptation) — also noted in p6.md |
| VI282 | **4** | titration_TCID50 |

Final class distribution: **Class 1 = 136, Class 4 = 57, Class 5 = 1** (194 rows).

## SPT CSV data-quality notes

- SPT references CSV `FBS` col already encodes 10% for SPT2–5, SPT10, SPT13; `FBS starve` for
  SPT10 (2%) and SPT3/SPT4 (0%).
- SPT4 CSV `year=2017` is **wrong** — paper is 2011 (DOI 10.1002/smll.201002020).
- SPT9 uses FCS (fetal calf serum), not FBS — flagged.
