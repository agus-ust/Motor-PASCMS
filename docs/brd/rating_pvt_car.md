<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 561,651. -->
## 16. Appendix A: Sample rating tables and test cases

All numbers here are made up for testing, in a generic currency unit; they are not actuarial advice and must be replaced with real rates before any real use. Each table is one CSV file in the build, and every vehicle class follows the same pattern: base rate times risk factors, less discounts, plus add-ons and third-party premium, then tax.

> **Band** = a range of values (for example, vehicle age 3 to 5 years) that share one rate. **Factor** = a multiplier, so 1.10 means 10% more. **Loading** = an increase added for extra risk. **Per mille (‰)** = per thousand, so 1.8‰ of 60,000,000 is 108,000. **Rounding rule** = round every premium line to 2 decimals (half up); calculate tax on the sum of the lines.

### A.1 Shared tables

**tax_by_region.csv**

| Region   | Tax rate | Exemption                         |
|----------|----------|-----------------------------------|
| Region A | 10%      | None                              |
| Region B | 8%       | Individual health policies exempt |
| Region C | 12%      | None                              |

**zone_map.csv** (used by Motor)

| City tier   | Zone |
|-------------|------|
| Metro       | A    |
| Second tier | B    |
| All others  | C    |

**Minimum premium:** 500 for own damage on cars, goods-carrying, passenger-carrying and miscellaneous vehicles; 200 for two-wheeler own damage. The zone table and the claim-free discount table in A.2 apply to every class unless a class says otherwise. Claim-free discount does not apply to fleets, which use an experience adjustment.

### A.2 Private car

**motor_od_base.csv**: own-damage base rate as a percentage of IDV

| Vehicle age   | Small engine (under 1,000 cc) | Medium (1,000 to 1,500 cc) | Large (over 1,500 cc) |
|---------------|-------------------------------|----------------------------|-----------------------|
| 0 to 2 years  | 2.80%                         | 3.10%                      | 3.40%                 |
| 3 to 5 years  | 2.90%                         | 3.20%                      | 3.50%                 |
| 6 to 10 years | 3.00%                         | 3.30%                      | 3.60%                 |
| Over 10 years | 3.10%                         | 3.40%                      | 3.70%                 |

**motor_factors.csv**

| Factor                                     | Value                                      |
|--------------------------------------------|--------------------------------------------|
| Zone A, B, C                               | 1.10, 1.00, 0.95                           |
| Fuel: petrol, diesel, CNG or LPG, electric | 1.00, 1.05, 1.03, 1.08                     |
| Voluntary deductible 0, 500, 1,000, 2,000  | 0%, 5%, 10%, 15% discount                  |
| Claim-free years 0, 1, 2, 3, 4, 5 or more  | 0%, 20%, 25%, 35%, 45%, 50% discount (NCB) |

**motor_addons_tp.csv**

| Item                                             | Rule                          |
|--------------------------------------------------|-------------------------------|
| Zero depreciation                                | 12% of own-damage net premium |
| Engine protect                                   | 4% of own-damage net premium  |
| Roadside assistance                              | Flat 350                      |
| Third-party premium: small, medium, large engine | 2,000, 3,400, 7,900           |
| Owner-driver personal accident                   | Flat 300                      |

**Formula.** Own-damage basic = IDV × base rate × zone × fuel. Net own damage = basic × (1 − deductible discount) × (1 − NCB). Add-ons are taken on net own damage. Total before tax = net own damage + add-ons + third-party + owner-driver accident. Tax = rate × total before tax.

**Test case M1: step by step**

Input: IDV 800,000; vehicle age 4 years; 1,200 cc petrol; Zone A; voluntary deductible 1,000; 2 claim-free years; zero depreciation and roadside assistance; Region A.

| Step                      | Working                       | Result        |
|---------------------------|-------------------------------|---------------|
| Basic own damage          | 800,000 × 3.20% × 1.10 × 1.00 | 28,160.00     |
| After deductible discount | 28,160 × 0.90                 | 25,344.00     |
| After NCB (25%)           | 25,344 × 0.75                 | 19,008.00     |
| Zero depreciation         | 12% × 19,008                  | 2,280.96      |
| Roadside assistance       | Flat                          | 350.00        |
| Third-party (medium)      | Table                         | 3,400.00      |
| Owner-driver accident     | Flat                          | 300.00        |
| Total before tax          | Sum of the lines              | 25,338.96     |
| Tax (10%)                 | 25,338.96 × 10%               | 2,533.90      |
| **Total premium**         |                               | **27,872.86** |

**Test case M2:** IDV 2,000,000; age 1 year; large diesel; Zone B; no deductible; no claim-free years; no add-ons; Region B. Basic own damage = 2,000,000 × 3.40% × 1.00 × 1.05 = 71,400; plus third-party 7,900 and accident cover 300 gives 79,600; tax at 8% is 6,368.00; **total 85,968.00**.

**idv_depreciation.csv**: IDV = manufacturer's listed price × (1 − depreciation), plus accessories at declared value

| Age of vehicle at policy start | Depreciation                        |
|--------------------------------|-------------------------------------|
| Up to 6 months                 | 5%                                  |
| 6 months to 1 year             | 15%                                 |
| 1 to 2 years                   | 20%                                 |
| 2 to 3 years                   | 30%                                 |
| 3 to 4 years                   | 40%                                 |
| 4 to 5 years                   | 50%                                 |
| Over 5 years                   | Agreed value, based on market value |

**Test case D1:** listed price 1,000,000, vehicle aged 2 years 6 months: depreciation 30%, so **IDV = 700,000**.


