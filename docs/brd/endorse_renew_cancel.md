<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 733,749. -->
### A.7 Renewal and cancellation tests

**Test case N1** (renewal of M1 with no claims): IDV 700,000 (from D1); age 5; 1,200 cc petrol; Zone A; deductible 1,000; 3 claim-free years (35%); zero depreciation and roadside assistance; Region A.

| Step                                             | Working                | Result        |
|--------------------------------------------------|------------------------|---------------|
| Basic own damage                                 | 700,000 × 3.20% × 1.10 | 24,640.00     |
| After deductible discount                        | × 0.90                 | 22,176.00     |
| After claim-free discount                        | × 0.65                 | 14,414.40     |
| Zero depreciation                                | 12% × 14,414.40        | 1,729.73      |
| Roadside assistance, third-party, accident cover | 350 + 3,400 + 300      | 4,050.00      |
| Total before tax                                 | Sum                    | 20,194.13     |
| Tax (10%)                                        |                        | 2,019.41      |
| **Total premium**                                |                        | **22,213.54** |

**Test case K1** (cancellation): the M1 policy is cancelled after 3 months, so 9 months remain. Premium refund = 25,338.96 × 9/12 = 19,004.22; tax refund 1,900.42; **total refund 20,904.64**. Refunds are pro-rata by whole months remaining.


