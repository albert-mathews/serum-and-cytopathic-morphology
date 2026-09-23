# Summary — batch 1 expansion

## Counts
- **Total new rows:** 70
- **OA fully coded** (access=oa, both FBS% + quotes): 45
- **Abstract-only:** 0
- **Paywall wishlist** (access=paywall_needed): 25
- **ID range:** VI50–VI121 (VI48–VI49 left unused for notes)
- **Duplicates vs existing corpus:** none (DOI/PMID/PMC checked)

## OA virus / system diversity
African swine fever virus, BVDV, BVDV-1c, CPV-2c, DENV, DENV-2, Duck Tembusu virus, FAdV, FAdV-4, FHV-1, H3NX avian influenza, HAdV, HAdV-55, HSV-1, HSV-2, Japanese encephalitis virus, Orthobunyavirus, PDCoV, PDCoV-related viruses, PIV5, PRRSV-1 and PRRSV-2, RSV, SARS-CoV-2, bat Jeilongvirus, bovine enterovirus, bovine enterovirus genotype F, camelpox virus, covert mortality nodavirus, enteroviruses, feline astrovirus, fowl adenovirus, herpes B virus, human adenovirus, insect-specific flavivirus, mosquito-borne alphaviruses, mumps virus, nervous necrosis virus, novel duck orbivirus, poliovirus, porcine teschovirus 2, sarbecoviruses, vaccine-like recombinant virus

## Protocol patterns of interest
- Classic **10% growth → 2% maintenance** is the dominant pattern (~35 OA rows).
- **Serum-free / 0% post-inoculation:** HSV-1 (VI73, serum-free DMEM for replication); H3NX influenza (VI80, serum-free DMEM + TPCK-trypsin).
- **Non-classic maintenance FBS:** 5% (BVDV-1c VI59); 1% (DTMUV VI86, duck orbivirus VI87); 3% (VI88); 4% plaque-agar serum (FHV-1 VI89); 8%→2% on HEL for HSV-2 (VI90).
- **Insect cells (C6/36):** L-15/M199 with 2% FBS post-inoculation common for arbovirus/flavivirus work.
- **BSA** (e.g. 0.5%) appears in specimen transport media for some bat virus isolations — recorded in notes, not as FBS%.
- Antibiotics frequently stated as “1% pen/strep” stock rather than IU/mg/ml; blanks left when conversion would be guesswork.

## Quality caveats
- Every OA row has a real PMC link and verbatim quote_pre / quote_post supporting the FBS values.
- A minority of OA rows are strong secondary (explicit dual media in propagation/antiviral Methods) rather than primary clinical isolation — flagged in notes where relevant.
- Paywall rows are isolation/CPE-titled candidates; abstracts rarely state both FBS%, so FBS columns are usually blank pending PDF.

## Outputs
- `new_isolation_refs_batch1.csv` — 70 rows
- `paywall_wishlist_batch1.md` — 25 download targets
- `search_log_batch1.md` — Europe PMC queries + hit counts
- `summary_batch1.md` — this file
