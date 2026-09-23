# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "P1_quotes.md"
text = p.read_text(encoding="utf-8")
if "Round 10" in text:
    print("Round 10 already present")
    raise SystemExit(0)

block = r'''

---

## Round 10 — Priority-A user PDFs (medium vs inoculation)

### P1-051 — Weller & Enders 1948 (pre-polio ultrafiltrate; single fluid)

> "The nutrient medium consisted routinely of 3 parts of a balanced salt solution made up according to the formula of Hanks and 1 part of Simms ox-blood serum ultrafiltrate. This mixture will hereafter be referred to as 'HS'."

> Fluid replaced at intervals with fresh HS; uninoculated cultures kept as controls.

**Role:** Documents **constrained enrichment** (ultrafiltrate, not whole serum) **before** Enders 1949 polio paper. **No** growth→maintenance percent switch at inoculation.

---

### P1-046 — Youngner 1954 (Medium D 2% horse serum → serum-free 199 at virus assay)

> "Medium D, used for washing and suspending dispersed cells, contained the following ingredients per 100 ml of medium: synthetic mixture 199, 2.8% NaHCO3, horse serum, 95, 3 and 2 ml, respectively."

> "For virus or antibody titrations medium D, containing horse serum, is not used. Instead, the medium employed is made up of 97.5 ml of mixture 199 to which is added 2.5 ml of 5% NaHCO3."

**Role:** By **1954**, standardized trypsinized MK monolayers already separate **cell-growth medium (2% horse serum in 199)** from **virus-assay medium (serum-free 199)**. Early quantitative dual-medium practice—not modern FBS brand, but same structural split at the inoculation/assay step.

---

### P1-047 — Scherer, Syverton & Gey 1953 (HeLa; high human serum → MS-100 after antibody dilution)

**Growth**

> Nutritive medium of human placental/adult serum or ascitic fluid **50%**, chick embryo extract **2 or 5%**, Hanks BSS **45–48%** (e.g. HPS-50, EE-2, H-48).

**At virus inoculation**

> "The liquid medium was assumed to contain antibodies against poliomyelitis virus, since human serum or ascitic fluid was employed for the growth of cells. Therefore, this liquid was removed and replaced by an equal amount of MS-100. … a second replacement … final dilution of from 1 to 400 to 1 to 800."

**Morphology note (post-study)**

> "a mixture of 10 per cent chicken serum and 90 per cent MS was superior to MS-100 for the maintenance of normal cellular structure. Titration end-points of poliomyelitis virus, Type 3, Saukett strain were identical in MS-100 and CHS-10, MS-90. However, the end-point in CHS-10, MS-90, was more easily determined microscopically, since non-specific degenerative changes did not occur within the 5 day period."

**Role:** Continuous-line era: **very rich human serum for growth**, then **synthetic MS-100** after deliberate **antibody washout** before virus. Explicit link: growth serum is treated as **confounder** of virus readout (antibody), not only as "nutrition."

---

### P1-048 — Baron & Low 1958 (*Science*; named maintenance medium; serum inhibits polio)

> "Although animal serum has been a necessary constituent of most media for continuous cell cultures, many sera contain 'inhibitors' to a wide range of viruses. It would be desirable to replace serum with another substance which does not contain nonspecific inhibitors or antibody and which would sustain cells in a condition sensitive to viral effects during the necessary observation periods."

> "Final concentration of 20 percent of skim milk in medium 199 was selected for further experimental use."

> "In comparative titrations, 4- to 100-fold serum-inhibition of poliovirus was observed when calf-serum-containing maintenance medium was compared with serum-free medium on monkey kidney cells."

> "Skim milk maintenance medium appears applicable as a standard medium for … (iii) isolation of viral agents which were not previously cultured, due to neutralization by serum-containing maintenance media"

**Role:** Names **maintenance medium** as the problem space; quantifies **serum inhibition of polio sensitivity**; proposes non-serum protein (skim milk) for post-growth virus observation. Direct ancestor of "drop serum at infection" rationales (inhibitors / attachment / neutralization).

---

### P1-013 — Leland & Ginocchio 2007 (secondary; little medium recipe)

Review of diagnostic cell-culture formats (traditional tubes, shell vial, coculture, transgenic lines) vs molecular methods. **No** quantitative growth/maintenance FBS tables. Useful only as **secondary timeline** of Isolation practice after institutional lock-in—not primary medium evolution evidence.

'''

# replace end marker if present
if text.rstrip().endswith("*End quotes archive (through Round 9).*"):
    text = text.rstrip()[: -len("*End quotes archive (through Round 9).*")].rstrip()

p.write_text(text + "\n" + block + "\n*End quotes archive (through Round 10).*\n", encoding="utf-8")
print("quotes appended OK")
