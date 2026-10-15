# P4 pilot - kit-insert census (8 rows)

**Date:** 2026-10-15. Coding sheet: `../P4_coding_sheet.md` (frozen 2026-10-15).
Rows: `../p4_antigen_provenance.csv`, `P4-001` to `P4-008`.

Purpose of this pilot was not to measure anything. It was to find out whether the 20
columns can actually be filled from real documents, and where they break.

## Sources and provenance reasoning

**P4-001 - ZEUS IFA CMV IgG (human, IFA).** The reference material *is* the culture: the
slide wells hold "human fibroblasts infected with CMV (strain AD169). Approximately
10 - 15% of the cells are infected"
([insert](https://www.zeusscientific.com/content/resources/ifa-psd-00014-package-insert-english-fa9001g.pdf)).
Positivity is defined morphologically, by apple-green intra-nuclear inclusions against
red counterstained cells. The remaining 85-90% uninfected cells are a within-well
reference for staining, not a matched mock antigen, so `matched_mock_run = no` rather
than `not_stated`: the insert does address uninfected cells and still does not run them
as an independent antigen. Nothing is said about how AD169 was established, nor about
medium or serum. Full insert read directly.

**P4-002 - EUROIMMUN Anti-Measles Virus ELISA IgG (human, ELISA).** The cleanest row in
the pilot: "The antigen source is provided by inactivated cell lysates of Vero cells
infected with the 'Edmonston' strain of measles viruses"
([IFU](https://www.intimakmur.co.id/uploads/files/produk/ifu/20210715092447-ifu-anti-measles-virus-elisa-igg.pdf);
same sentence in a second copy of the IFU). Substrate line and strain both named, no
uninfected-Vero lysate control specified, and specificity argued from cross-reactivity
panels against other infections rather than from a matched mock.

**P4-003 - SERION ELISA classic Measles Virus IgG/IgM (human, ELISA).** Same analyte and
format as P4-002, but the document states only that "the coating material is inactivated"
([insert](https://www.leinco.com/wp-content/uploads/2025/01/Measles-V11-E-_US_.pdf)).
No substrate, no strain. Coded `not_stated`, not `unclear`. The pair P4-002 / P4-003 is
the pilot's most useful finding: two kits measuring the same claimed analyte differ
completely in whether their provenance is disclosable at all.

**P4-004 - ID Screen Bluetongue Competition (veterinary, ELISA).** "Coated antigen:
Recombinant VP7"
([product page](https://www.innovative-diagnostics.com/produit/id-screen-bluetongue-competition/));
the 2011 catalogue says "Recombinant purified VP7". No expression host, no ORF origin,
so this is `recombinant_source_unclear` rather than either independence or inheritance.

**P4-005 - ID Screen Infectious Bronchitis Competition (veterinary, ELISA).** "Coated
antigen IBV purified antigen"
([catalogue](https://diagnostics.lillidale.co.uk/wp-content/uploads/2016/04/ID-Vet2011.pdf)).
Purity claimed with no method and no substrate named; IBV is conventionally
egg-propagated, which the document does not say either.

**P4-006 - ID Screen Infectious Bronchitis Indirect 2.0 (veterinary, ELISA).** The
successor product replaces that with "Purified IBV recombinant protein"
([product page](https://www.innovative-diagnostics.com/produit/id-screen-infectious-bronchitis-indirect-2-0/)).
A culture-antigen to recombinant transition inside one manufacturer's line, which is
exactly the ambiguous case the prediction anticipated: the complexity of culture
supernatant is gone, but the reference ORF origin is still unprinted.

**P4-007 - VMRD Bluetongue cELISA v2 (veterinary, ELISA).** Distributor catalogue only
([catalogue](https://www.indical.com/wp-content/uploads/2025/01/Veterinary-Diagnostic_Catalog_web.pdf));
the antigen-coated plate is never characterised. Kept deliberately as a negative control
on source type: catalogue-level sources cannot fill the stack and must be upgraded to the
manufacturer insert before they count.

**P4-008 - IBT Bioservices anti-SUDV GP mAb 16F6 (research reagent datasheet).** One
product, two different provenances: the immunogen was alphavirus replicons encoding the
glycoprotein together with gamma-irradiated culture virus, while the ELISA coating
antigens are virus-like particles and recombinant glycoprotein
([datasheet](https://www.ibtbioservices.com/wp-content/uploads/2015/11/2003004.pdf)).

## Which columns held, which did not

| Column | Verdict |
|--------|---------|
| `analyte_claimed`, `assay_format`, `domain` | Fill cleanly every time |
| `immunogen_or_reference_source` | Fills, but see the amendment below: one product can have two |
| `isolate_justification` | Almost always `unspecified`; inserts never narrate how the Isolate was established. Low information as written, but the uniformity is the point |
| `matched_mock_run` | Needs the P4-001 distinction between a refused mock and an unmentioned one |
| `serum_or_maintenance_language` | `not_stated` in 8 of 8. Inserts do not discuss production medium; this column will only earn its keep on the Isolation-paper rows |
| `particle_separation_claim` | Only fires on "purified" language (P4-005) |
| `sequence_path` | `unclear` in 8 of 8; no insert printed an accession |
| `inheritance_score` | Workable, but `undetermined` is doing heavy lifting for non-disclosure |

## Amendment needed

P4-008 showed that **immunogen** (what raised the antibody) and **reference antigen**
(what is on the plate) can differ within one product, and the single column
`immunogen_or_reference_source` forces a choice between them. Recommend splitting it into
`immunogen_source` and `reference_antigen_source` with the same value set, before the
corpus grows. Not applied yet: the sheet is frozen and this is Albert's call.

## Distribution (n=8)

- Immunogen / reference source: `culture_isolate_lysate` 2, `recombinant_source_unclear` 2,
  `not_stated` 2, `purified_culture_particles` 1, `inactivated_culture_virus` 1.
- Matched mock: `no` 1, `not_stated` 7. None reported running a matched uninfected culture antigen.
- Inheritance: `inherits` 3, `partial` 3, `undetermined` 2.
- Domain: human 4, veterinary 4.

## Next steps

1. Decide the immunogen / reference-antigen split above, then log it as amendment 2.
2. Upgrade P4-007 from catalogue to manufacturer insert, and find manufacturer inserts for
   the veterinary rows rather than product pages.
3. Add the two missing formats: a lateral-flow antigen test and a licensed immunoblot
   (immunoblots are the one format that routinely runs an uninfected-lysate lane, so they
   are the best chance of a real `matched_mock_run = yes` row).
4. Then move to R1 dual-serum Isolation papers, where `serum_or_maintenance_language`
   should finally become informative.
5. Consider a `disclosure_level` column, since the strongest pilot signal was not culture
   provenance but the refusal of several kits to state any provenance at all.
