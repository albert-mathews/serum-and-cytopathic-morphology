# IR1 vs IR2 — Pass 1 open-ended morphology (lexical descriptor incidence)

**Scope:** Blinded Pass-1 free-text descriptions of the same 100 CultureA/CultureB phase-contrast images.
**Labels:** IR1 and IR2 only (independent researchers).
**Method:** Lexical/synonym hits against shared CRO Healthy and CPE descriptor regex sets. Pass 1 was **not** a checklist — incidences are approximate.
**Arms (analysis only):** CultureA = path1 (10% FBS), CultureB = path2 (2% FBS).
**Rule:** Confluence/coverage is **not** healthy vs stressed.

**Companion CSV:** `IR1_IR2_pass1_descriptor_comparison.csv`

---

## Coverage

| | IR1 | IR2 |
|--|------:|------:|
| Images scored | 100 | 100 |
| Shared image IDs (`CultureX_dayY_ZZ`) | 100 | (same scheme) |
| CultureA / CultureB | 50 / 50 | 50 / 50 |

Image ID schemes match after normalizing IR2 Filename stems (`CultureA_day1_01.tif` → `CultureA_day1_01`). No blinded-mapping remapping required for this Pass-1 collation.

---

## Qualitative compare / contrast

| Theme | IR1 | IR2 |
|-------|-----|-----|
| Writing style | Long template-like paragraphs; heavy reuse of healthy-shape language (elongated/polygonal/adherent/phase-bright). | Shorter observational notes; more optical-artifact callouts; less checklist-echo phrasing. |
| Healthy-term density | Very high / near-saturated on several CRO Healthy terms. | Sparse — rarely says healthy/well-spread/adherent. |
| Classic CPE lexicon (V, G, Dy, Sy, ND) | Essentially **absent** in free text (0 lexical hits). | **Rare but non-zero** vacuolization / granularity; still no cell-death / syncytia / ND. |
| Main B−A morphology signal | **Detachment / non-adherent** (A 0.58 → B 1.00). | **Refractile** (A 0.26 → B 0.50); Detachment near-floor both arms. |
| Saturation risk | Rounded + Refractile hit **100% both arms** → not discriminative. | Rounded uncommon; Refractile moderate and arm-skewed — less saturated, still template-prone. |
| Blinding | No virus/CPE/FBS language. | No virus/CPE/FBS language; Notes state no A↔B comparisons. |

### Agreement / disagreement on which descriptors discriminate B−A

**Agree (both show little/no B>A for these under Pass-1 lexical scoring):** Cell death, Ballooned/Enlarged, Syncytia, Cytoplasmic strands, Nonspecific degeneration, Cytoplasmic extensions (healthy) — all near zero or flat.

**Disagree on the primary B>A discriminator:**
- IR1: **Detachment** is the clear CPE-set arm contrast (+0.42).
- IR2: **Detachment** is not discriminative (−0.02); **Refractile** is the largest positive B−A (+0.24).

**Disagree on saturation:** IR1 saturates Rounded/Refractile at 1.0 both arms; IR2 does not — so IR2’s Refractile B−A is interpretable as a wording-frequency difference, but still not equivalent to CRO classic CPE narrative.

**Healthy set:** IR1 near-ceiling on Mitotic/Adherent/Elongated/Polygonal; IR2 much lower absolute incidence, with Polygonal lower in B (−0.16) — likely colony-architecture wording differences, not a stress metric.

---

## Descriptor incidence tables

Incidence = fraction of images (n=50 per arm) with ≥1 lexical match.

### Aggregate

| Metric | IR1 A | IR1 B | IR1 B−A | IR2 A | IR2 B | IR2 B−A |
|--------|------:|------:|--------:|------:|------:|--------:|
| Mean healthy-term hits / image | 4.9 | 4.86 | -0.04 | 0.68 | 0.44 | -0.24 |
| Mean CPE-term hits / image | 2.58 | 3.0 | 0.42 | 0.5 | 0.6 | 0.1 |
| Any healthy-term hit | 1.0 | 1.0 | 0.0 | 0.44 | 0.3 | -0.14 |
| Any CPE-term hit | 1.0 | 1.0 | 0.0 | 0.38 | 0.52 | 0.14 |

### CRO Healthy set

| Descriptor | IR1 A | IR1 B | IR1 B−A | IR2 A | IR2 B | IR2 B−A |
|------------|------:|------:|--------:|------:|------:|--------:|
| H_Look_Healthy | 0.92 | 0.86 | -0.06 | 0.04 | 0.06 | 0.02 |
| H_Mitotic_Bright | 1.0 | 1.0 | 0.0 | 0.08 | 0.02 | -0.06 |
| H_Adherent | 1.0 | 1.0 | 0.0 | 0.04 | 0.06 | 0.02 |
| H_Elongated | 1.0 | 1.0 | 0.0 | 0.28 | 0.24 | -0.04 |
| H_Polygonal | 0.98 | 1.0 | 0.02 | 0.22 | 0.06 | -0.16 |
| H_Cytoplasmic_extensions | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| H_well_defined_nuclei | 0.0 | 0.0 | 0.0 | 0.02 | 0.0 | -0.02 |

### CPE set

| Descriptor | IR1 A | IR1 B | IR1 B−A | IR2 A | IR2 B | IR2 B−A |
|------------|------:|------:|--------:|------:|------:|--------:|
| CPE_Cell_death_Dy | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| CPE_Rounded_Ro | 1.0 | 1.0 | 0.0 | 0.1 | 0.02 | -0.08 |
| CPE_Ballooned_Enlarged_BE | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| CPE_Syncytia_Sy | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| CPE_Vacuolation_V | 0.0 | 0.0 | 0.0 | 0.04 | 0.02 | -0.02 |
| CPE_Detachment_D | 0.58 | 1.0 | 0.42 | 0.04 | 0.02 | -0.02 |
| CPE_Granularity_G | 0.0 | 0.0 | 0.0 | 0.06 | 0.04 | -0.02 |
| CPE_Refractile_Re | 1.0 | 1.0 | 0.0 | 0.26 | 0.5 | 0.24 |
| CPE_Cytoplasmic_strands_CS | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| CPE_Nonspecific_degeneration_ND | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

---

## Saturation and interpretation notes

1. **IR1 Rounded + Refractile = 1.00 both arms** — lexical CPE incidence is inflated by routine sparse-culture “rounded phase-bright” language; do not treat as arm discrimination.
2. **IR1 Detachment** is the only clear Pass-1 CPE-set B>A signal; still milder than a full classic CPE write-up.
3. **IR2 Refractile B>A** should be read cautiously: “refractile/bright round bodies” may be settling cells or debris language, not etiologic CPE.
4. **IR2 non-zero Vacuolation/Granularity** is a qualitative plus vs IR1 zeros, but counts are too small for arm claims.
5. **Neither IR** spontaneously builds CRO-like Path2 narratives of dying cells / nonspecific degeneration on Pass 1.
6. Prefer Pass-2 checklist (or human dual-read subset) for features that Pass-1 free text under-reports.

---

## Bottom line for paper drafting

Pass-1 open-ended text from two independent researchers **does not converge on the same primary B−A morphology discriminator**. IR1 points to detachment/non-adherent language; IR2’s strongest lexical B−A is refractile wording, while detachment is near absent. Shared absences (cell death, syncytia, ballooning, strands, ND) are themselves informative about unprimed free-text conservatism. Confluence/coverage differences must not be used for healthy vs stressed claims.

