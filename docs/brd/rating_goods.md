<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 667,698. -->
### A.4 Goods-carrying vehicles

**goods_od_base.csv**: own-damage base rate as a percentage of IDV

| Vehicle age   | Rate  |
|---------------|-------|
| 0 to 2 years  | 3.20% |
| 3 to 5 years  | 3.40% |
| 6 to 10 years | 3.70% |
| Over 10 years | 4.20% |

**goods_factors.csv**

| Factor                                                                                                                   | Value                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Permit area local, state, national                                                                                       | 0.90, 1.00, 1.20                                                                                                    |
| Type of goods general, perishable, high value, hazardous                                                                 | 1.00, 1.10, 1.25, 1.30                                                                                              |
| Fleet discount on own-damage net: 1 to 4, 5 to 9, 10 to 24, 25 or more vehicles                                          | 0%, 5%, 10%, 15%                                                                                                    |
| Experience adjustment on own-damage net by fleet loss ratio over 3 years: up to 50%, 50% to 80%, 80% to 110%, above 110% | 10% discount, none, 15% loading, refer (rule R6)                                                                    |
| Third-party premium by GVW: up to 3,500 kg; 3,501 to 7,500; 7,501 to 12,000; 12,001 to 20,000; over 20,000               | 6,500; 12,000; 19,000; 27,500; 36,000                                                                               |
| Legal liability to paid driver or cleaner                                                                                | 80 each                                                                                                             |
| Owner-driver personal accident (only if the owner drives)                                                                | 300                                                                                                                 |
| Trailer                                                                                                                  | Own damage on the trailer's IDV with the same table; third-party is 25% of the towing vehicle's third-party premium |

**Formula.** Own-damage basic = IDV × rate × permit area × goods type × zone. Net = basic × (1 − fleet discount) × (1 ± experience adjustment), or × (1 − claim-free discount) for a single vehicle. Total before tax = net + third-party + liability to paid staff + owner-driver cover. Tax is then added.

**Test case G1** (single truck): IDV 2,400,000; age 3; GVW 16,000 kg; state permit; general goods; Zone B; no claim-free years; driver and cleaner; Region A. Basic own damage = 2,400,000 × 3.40% = 81,600; third-party 27,500; staff liability 160; total before tax 109,260; tax at 10% is 10,926; **total 120,186.00**.

**Test case G2** (fleet of 12 such trucks carrying hazardous goods on national permits; fleet loss ratio 60%): per truck own damage = 81,600 × 1.20 × 1.30 = 127,296; fleet discount 10% gives 114,566.40; adding third-party 27,500 and staff liability 160 gives 142,226.40; for 12 trucks 1,706,716.80; tax at 10% is 170,671.68; **total 1,877,388.48**; the case is referred by rule R5.

**Test case G3:** a 13th identical truck is added after 3 months, so 9 months remain. Premium before tax = 142,226.40 × 9/12 = 106,669.80; tax 10,666.98; **total 117,336.78**.


