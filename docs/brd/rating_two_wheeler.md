<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 652,666. -->
### A.3 Two-wheeler

**twowheeler_od_base.csv**: own-damage base rate as a percentage of IDV

| Vehicle age   | Small (up to 150 cc) | Medium (151 to 350 cc) | Large (over 350 cc) |
|---------------|----------------------|------------------------|---------------------|
| 0 to 2 years  | 1.80%                | 2.00%                  | 2.30%               |
| 3 to 5 years  | 1.90%                | 2.10%                  | 2.40%               |
| 6 to 10 years | 2.00%                | 2.20%                  | 2.50%               |
| Over 10 years | 2.10%                | 2.30%                  | 2.60%               |

Other rules: zone, fuel and claim-free discount as in A.2; voluntary deductible 0, 100, 250, 500 gives 0%, 5%, 10%, 15% discount; zero depreciation is 10% of own-damage net; roadside assistance flat 150; third-party premium small, medium, large is 750, 1,200, 2,800; owner-driver personal accident flat 300.

**Test case T1:** IDV 90,000; age 2 years; 125 cc petrol; Zone B; no deductible; 1 claim-free year; zero depreciation; Region C. Basic own damage = 90,000 × 1.80% = 1,620; after 20% claim-free discount 1,296.00; zero depreciation 129.60; third-party 750; accident cover 300; total before tax 2,475.60; tax at 12% is 297.07; **total 2,772.67**.


