<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 716,732. -->
### A.6 Miscellaneous and special vehicles

**misc_od_base.csv**: own-damage base rate as a percentage of IDV

| Type                                      | Rate  |
|-------------------------------------------|-------|
| Agricultural tractor                      | 1.80% |
| Tractor with trailer                      | 2.00% |
| Construction equipment (crane, excavator) | 2.60% |
| Ambulance and special-purpose             | 2.40% |

Other rules: age factor 0 to 5 years 1.00, 6 to 10 years 1.10, over 10 years 1.25; place of use public road 1.00, private site only 0.70 (third-party premium is halved for site-only use); zone and claim-free discount as in A.2; third-party premium for tractor, tractor with trailer, construction equipment, ambulance is 3,500, 4,500, 6,500, 8,000; legal liability to paid operator 80; owner-driver personal accident 300.

**Test case X1:** excavator; IDV 5,000,000; age 6; private site only; Zone B; one paid operator; Region C. Own damage = 5,000,000 × 2.60% × 1.10 × 0.70 = 100,100; third-party 6,500 × 0.50 = 3,250; operator liability 80; total before tax 103,430; tax at 12% is 12,411.60; **total 115,841.60**; referred by rule R8.

**Test case X2:** tractor; IDV 900,000; age 3; public road; Zone C; 1 claim-free year; owner drives; Region A. Own damage = 900,000 × 1.80% × 0.95 = 15,390; after 20% claim-free discount 12,312; third-party 3,500; accident cover 300; total before tax 16,112; tax at 10% is 1,611.20; **total 17,723.20**.


