<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 787,811. -->
### A.10 Test case checklist

Write these as automated tests (pytest) for the rating and claims engine; each must match to the cent.

| ID  | Class                       | Key input                                    | Expected result                                  |
|-----|-----------------------------|----------------------------------------------|--------------------------------------------------|
| M1  | Private car                 | See A.2                                      | Total 27,872.86                                  |
| M2  | Private car                 | See A.2                                      | Total 85,968.00                                  |
| M3  | Private car                 | IDV 3,000,000, anything else                 | Referred by R1                                   |
| D1  | Private car                 | Listed price 1,000,000, age 2 years 6 months | IDV 700,000                                      |
| N1  | Private car                 | Renewal, see A.7                             | Total 22,213.54                                  |
| K1  | Private car                 | Cancellation, see A.7                        | Total refund 20,904.64                           |
| T1  | Two-wheeler                 | See A.3                                      | Total 2,772.67                                   |
| G1  | Goods-carrying              | See A.4                                      | Total 120,186.00                                 |
| G2  | Goods-carrying fleet        | See A.4                                      | Total 1,877,388.48, referred by R5               |
| G3  | Goods-carrying fleet        | 13th truck after 3 months                    | Total 117,336.78                                 |
| PC1 | Passenger-carrying          | Taxi, see A.5                                | Total 35,152.92                                  |
| PC2 | Passenger-carrying          | School bus, see A.5                          | Total 182,033.50, referred by R7                 |
| X1  | Miscellaneous               | Excavator, see A.6                           | Total 115,841.60, referred by R8                 |
| X2  | Miscellaneous               | Tractor, see A.6                             | Total 17,723.20                                  |
| CA1 | Claim: own damage           | See A.8                                      | Payable 116,500 (139,000 with zero depreciation) |
| CA2 | Claim: total loss           | See A.8                                      | Payable 679,000                                  |
| CA3 | Claim: theft                | See A.8                                      | Payable 799,000                                  |
| CA4 | Claim: third-party property | See A.8                                      | Insurer pays 750,000                             |


