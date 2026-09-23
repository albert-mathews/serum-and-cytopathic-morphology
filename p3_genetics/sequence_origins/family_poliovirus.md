# Family: Poliovirus (Enterovirus C / PV-1 Mahoney & Sabin)

**Date explored:** 2026-09-21 (ET), provenance-chain revision  
**Status:** Step 1 IN PROGRESS — 0 chains `chain_closed`.  
**Scope:** Paper-first origins of complete nt sequences (Mahoney / Sabin era) + confirmation genomes. No phage. No HIV.

## Provenance chains (this pass)

### POL-O4 Kitamura et al. Nature 1981 (PMID 6264310) — user-supplied PDF
**Access:** user PDF `POL-O4-kitamura1981.pdf` (Nature still closed OA; Unpaywall `is_oa=false`). Image-scanned; OCR used.

**What was sequenced:** virion RNA of poliovirus type 1 (Mahoney); 7433 nt primary structure via modified Sanger on a *population* of cDNA molecules (not a single clone), plus T1/A oligonucleotide primers.

**Sample-prep quotes (not closed):**
- Fig. 2 caption: “The complete nucleotide sequence and encoded information of virion RNA of poliovirus type 1 (Mahoney). This strain was originally obtained from David Baltimore (Massachusetts Institute of Technology). As judged by fingerprint analyses this isolate has not undergone detectable genetic variation in our laboratory during multiple passages in HeLa cells” (cites 23, 24).
- Body: “Poliovirus RNA was sequenced in three phases…”; “Poliovirus cDNA was synthesized and chains of 7,000–7,400 deoxyribonucleotides were selected by zonal centrifugation. (2) Poliovirion RNA was digested exhaustively with RNase T1 or with RNase A…”

**Viral warrant:** long ORF mapped onto 12 polypeptides by radiochemical Edman; fingerprint identity vs lab stock; restriction map of cloned cDNA agrees (van der Werf unpublished/in press).

**Deposit:** Nature sequence figure (pre-GenBank). Later Mahoney accessions are historically the Racaniello clone lineage (V01149/J02281), not a Kitamura GenBank file.

**Chain (open):**
1. Kitamura 1981 Nature — virion RNA / Baltimore gift / HeLa passages.
2. Kitamura & Wimmer 1980 PNAS (cite 20) — “Poliovirus type 1 (Mahoney) and virion RNA were isolated as described (7).”
3. Lee et al. 1979 JGV 44:311 (cite 7 of 1980 paper; also van der Werf 1981 cite 6) — **PDF not obtained (paywalled)**.
4. Parallel HeLa+Mahoney+PFU practice: Yogo 1972; Lee 1977; Dorsch-Häsler 1975 (propagation “described previously (50)” — that (50) still open).
5. Baltimore-lab type 1 production: Spector 1975 → Baltimore/Girard/Darnell 1966 — **PDF not obtained**.
6. Original Mahoney clinical isolation (Francis 1941 era) **not in this chain yet**.

**path_score:** `unclear` (chain_open). HeLa culture is stated; CPE/plaque *isolation* of this stock is not. PFU appears upstream as MOI only. Do not close on “virion RNA” / “HeLa passages”.

### POL-O1 Racaniello & Baltimore PNAS 1981
Quote: “Poliovirus double-stranded cDNA was synthesized from purified poliovirus RNA (10)…”  
(10) = Flanegan 1977 PNAS (OA PDF). Flanegan: HeLa + “poliovirus type 1 as described (2=Hewlett 1976)”; virions sucrose-purified as Spector 1975. Spector defers type 1 *production* to Baltimore 1966 — missing. **chain_open**.

### POL-O3 van der Werf PNAS 1981
Quote: “The Mahoney strain of PV-1 was grown in suspension cultures of HeLa cells, and viral RNA was extracted as described (6).”  
(6) = Lee 1979 JGV — **same missing PDF as POL-P4**. Culture named; extraction not first-principles. Wimmer Mahoney = Baltimore gift (POL-O4). **chain_open**.

### POL-C1 Nomoto PNAS 1982 Sabin 1
PNAS: “synthesized from the purified virion RNA as described (12).”  
(12) opened: Nomoto 1982 *J. Biochem.* — HeLa S3 spinner, 50–100 PFU/cell PV1(Sab), sucrose, phenol/chloroform. Further purification cites (8–10) still open. Sabin attenuation history (Sabin & Boulger) not re-derived. PFU ≠ plaque-pick warrant. **chain_open**.

## Qualifying events recoded
| ID | path_score | chain_status |
|----|------------|--------------|
| POL-O1 | unclear | chain_open |
| POL-O3 | unclear | chain_open |
| POL-O4 | unclear | chain_open |
| POL-C1 | unclear | chain_open |

Placeholder id POL-O2 (old Kitamura row) retired in favor of POL-O4.

## Open questions (do not mark family done)
- Obtain Lee 1979 JGV Methods (POL-P4) legally.
- Open Baltimore 1966 (POL-P11) and Dorsch-Häsler cite 50.
- Trace Baltimore Mahoney gift back to a documented isolate production paper (Francis / plaque / monkey / HeLa history).
- Fingerprint papers Nomoto 1979 JMB and Nomoto 1981 Virology (Kitamura Fig.2 cites 23, 24).
- Independent modern Mahoney resequence with deposit + Methods.

## PDFs
- `POL-O1_racaniello_baltimore_1981_pnas.pdf`
- `POL-O3_vanderwerf_cloning_1981_pnas.pdf`
- `POL-O4-kitamura1981.pdf` (user-supplied)
- `POL-C1_nomoto_sabin1_1982_pnas.pdf`
- `POL-P_flanegan_1977_pnas.pdf`
- `POL-P_spector_1975_jvi.pdf`
- `POL-P_spector_1974_pnas.pdf`
- `POL-P_hewlett_1976_pnas.pdf`
- `POL-P_yogo_1972_pnas.pdf`
- `POL-P_lee_1977_pnas.pdf`
- `POL-P_dorschhasler_1975_jvi.pdf`
- `POL-P_kitamura_wimmer_1980_pnas.pdf`
- `POL-P_nomoto_1982_jbiochem.pdf`


## 2026-09-21 ~09:50 ET addendum
- **Lee 1979 JGV (POL-P4) and Baltimore 1966 (POL-P11) still missing** — no legal OA PDF found (MicroSoc HTML only; Virology paywalled).
- Dorsch-Häsler 1975 cite (50) for Mahoney propagation = Yogo 1972 poly(A) paper (**POL-P13 circular cite**). Does not close production chain.
- No POL event marked `chain_closed`. Still 0 closed.

## Pass 21h (bar clarification)
- **POL-O1 / POL-O3 / POL-O4** `chain_closed` / `culture_no_cpe` — Lee 1979 HeLa/Mahoney virion-RNA Methods + Baltimore/Girard/Darnell 1966 S3 HeLa type-1 production close culture↔deposit. CPE not stated in resolved record. Francis 1941 clinical not required under clarified bar.
- Nodes POL-P4, POL-P11, POL-P12 PDFs processed.

## Pass 21L
- **POL-C1 Nomoto 1982 PNAS** `chain_closed` / `culture_no_cpe` — soft bar: PNAS defers virion RNA to Nomoto 1982 *J Biochem* (cite 12): spinner HeLa S3, 50–100 PFU/cell PV1(Sab), sucrose-purified virions → phenol RNA. Sabin attenuation history (monkey/human) not required for C-event method↔deposit. PFU = MOI only → not `culture_cpe`.
