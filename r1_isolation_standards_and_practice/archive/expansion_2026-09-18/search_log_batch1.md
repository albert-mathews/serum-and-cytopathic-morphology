# Search log — batch 1

Date: 2026-09-14 (America/Toronto)

## Method
Europe PMC REST API via curl/urllib (`resultType=core`, `pageSize` 50–100). OA full text via `/fullTextXML`. Existing corpus links/IDs excluded (VI2–VI47/SPT10).

## Query set A (initial dual-serum isolation sweeps)
```
q2_maint: hitCount=1507, saved=200
q3_cpe: hitCount=3544, saved=200
q4_inoc: hitCount=6093, saved=200
q5_entero: hitCount=1169, saved=200
q6_adeno: hitCount=2772, saved=200
q7_hsv: hitCount=4026, saved=200
q8_measles: hitCount=1127, saved=200
q9_dengue: hitCount=2882, saved=200
q10_flu: hitCount=3390, saved=200
q11_prrsv: hitCount=3590, saved=200
```

## Query set B (virus-specific sweeps)
```
q12_classic: hitCount=366, returned=50
  new unique kept: 20
q13_hsv_iso: hitCount=2035, returned=50
  new unique kept: 8
q14_cmv: hitCount=3924, returned=50
  new unique kept: 15
q15_measles_iso: hitCount=755, returned=50
  new unique kept: 15
q16_dengue_iso: hitCount=1570, returned=50
  new unique kept: 26
q17_rsv: hitCount=761, returned=50
  new unique kept: 19
q18_rota: hitCount=1059, returned=50
  new unique kept: 44
q19_fmdv: hitCount=664, returned=50
  new unique kept: 23
q20_ndv: hitCount=365, returned=50
  new unique kept: 26
q21_wnv: hitCount=878, returned=50
  new unique kept: 26
q22_yfv: hitCount=1568, returned=50
  new unique kept: 18
q23_ibdv: hitCount=204, returned=50
  new unique kept: 22
q24_asfv: hitCount=317, returned=50
  new unique kept: 22
q25_nipah: hitCount=1054, returned=50
  new unique kept: 27
```

## Query set C (paywalled / NOT OPEN_ACCESS:Y)
```
pay_q1: hitCount=118, returned=100
pay_q2: hitCount=500, returned=100
pay_q3: hitCount=985, returned=100
unique_paywalled=31

```

## Notes
- First broad query (`2% FBS` + isolation + `10% FBS`) returned very large hitCounts with many non-virology false positives; subsequent queries added CPE/maintenance/virus filters.
- OA full-text XML scanned for Methods FBS/serum contexts; rows only kept when both growth and infection/maintenance (or serum-free/trypsin) could be supported by verbatim snippets.
- Existing PMIDs/PMCs/DOIs from `/workspace/r1/existing_links.txt` and clean CSV were skipped.
- IDs start at VI50 (VI48–VI49 left unused).