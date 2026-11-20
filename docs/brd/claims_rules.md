<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 298,341 750,770. -->
## 9. Claims management requirements

The claims journey is the same for every vehicle class; only the claim type, the data collected, the documents asked for and the people involved change, and all of them come from configuration. The 6-week build covers every claim type below, with third-party claims in a simpler form.

| ID    | Requirement                                                                                                                                                        | Tier   |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| CL-01 | First Notice of Loss (FNOL) through staff entry, with web form and call-centre entry as variants                                                                   | Build  |
| CL-02 | Automatic validation at FNOL: policy in force on the loss date, vehicle matches, driver licence valid for the class, use as declared, premium paid                 | Build  |
| CL-03 | Claim types: own damage (accident), theft, total loss, fire, natural calamity, third-party property damage, third-party injury, third-party death                  | Build  |
| CL-04 | Claim forms from claim schemas by type and vehicle class (accident details, theft details, third-party details)                                                    | Build  |
| CL-05 | Document checklist per claim type and class, with upload and status tracking                                                                                       | Build  |
| CL-06 | Cashless garage network: garage master, repair estimate upload, repair authorisation                                                                               | Simple |
| CL-07 | Surveyor assignment by region, survey report upload, re-inspection                                                                                                 | Simple |
| CL-08 | Reserve setting and revision with reason codes, and a full history of reserve movements                                                                            | Build  |
| CL-09 | Assessment: compulsory and voluntary deductible, depreciation on parts, zero-depreciation add-on, salvage, under-insurance                                         | Build  |
| CL-10 | Total loss: if the repair cost is above a set share of IDV, settle on a total-loss basis; theft settles on IDV                                                     | Build  |
| CL-11 | Approval workflow by authority matrix, with escalation and reasons                                                                                                 | Build  |
| CL-12 | Settlement and payment to garage or owner, with payment record                                                                                                     | Simple |
| CL-13 | Third-party claims: claimant records, injury or damage details, legal case status and stages, lawyer and hearing dates, award or settlement                        | Simple |
| CL-14 | Fraud indicators: rule flags such as a loss soon after the policy start, repeated claims, mismatched details, inflated estimates, with referral to an investigator | Simple |
| CL-15 | Subrogation and salvage recovery record                                                                                                                            | Simple |
| CL-16 | Repudiation (rejection) with reason, policy clause cited and a letter template                                                                                     | Build  |
| CL-17 | Claim reopening, supplementary and partial payments                                                                                                                | Later  |
| CL-18 | Turnaround timers and alerts for regulatory and internal timelines                                                                                                 | Simple |
| CL-19 | Catastrophe event tagging, so many claims from one flood or hailstorm are grouped and reported together                                                            | Simple |
| CL-20 | Claims dashboards: open, aged, reserve versus paid, frequency, severity and loss ratio by class and region                                                         | Build  |
| CL-21 | Grievance and complaint linking to claims                                                                                                                          | Later  |
| CL-22 | Salvage sale and auction handling                                                                                                                                  | Later  |

> **FNOL** = the first report of a loss to the insurer. **Repudiation** = the insurer's formal rejection of a claim, which must state reasons. **Subrogation** = the insurer, after paying, stepping into the policyholder's shoes to recover the loss from the party at fault. **Salvage** = the value recovered by selling what remains of a damaged vehicle. **Total loss** = a claim where the vehicle is destroyed or repair costs too much, so the insurer pays its value (IDV) less salvage. **Compulsory deductible** = the fixed amount of every own-damage claim that the owner always bears. **Depreciation on parts** = a deduction for wear on replaced parts, unless the zero-depreciation add-on applies. **Claimant** = a third party who claims for injury or damage the insured vehicle caused. **Tribunal** = the special court that decides compensation for road-accident injury and death claims. **Incurred** = paid amounts plus outstanding reserves for claims. **Catastrophe (CAT) event** = a single large event, such as a flood, that causes many losses at once.

**Timers.** Regulatory turnaround times (for example, surveyor appointment, survey report, decision after the last document) are held as configurable timers per vehicle class. The exact values are to be confirmed against the regulations that apply in the target market during analysis and kept in a versioned parameter table, not in code.

### Claim data captured by claim type 

| Claim type                  | Fields                                                                                                                                                                                                                                                               |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Own damage (accident)       | Loss date, time and place, cause, description, driver at the time and licence details, passengers, police report number if any, drivable flag, towing needed, damage photos, repair estimate, garage, third party involved flag                                      |
| Theft or total loss         | Last-seen date and place, police report number, keys available, anti-theft device, circumstances, recovery status, notice date, salvage details                                                                                                                      |
| Fire or natural calamity    | Event type (fire, flood, storm, hail, earthquake), date, location, event reference, damage description, where the vehicle was during the event                                                                                                                       |
| Third-party property damage | Claimant, owner of the damaged property, property type, damage description, assessed value, claimant's insurer if any, police report                                                                                                                                 |
| Third-party injury or death | Claimant (injured person or dependants), age, occupation and income, injuries or cause of death, medical bills, disability percentage, hospital, police report, legal representative, tribunal case number, hearing dates, award or settlement amount, appeal status |
| All claim types             | Cover check result, reserve history, surveyor, documents, approvals, payments, recoveries                                                                                                                                                                            |


### A.8 Claims parameters and tests

**claims_parameters.csv**

| Parameter                                                                             | Value                                                                                                                          |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Compulsory deductible                                                                 | Two-wheeler 100; car up to 1,500 cc 1,000; car over 1,500 cc 2,000; goods-carrying, passenger-carrying and miscellaneous 1,000 |
| Depreciation on parts by vehicle age in completed years (0, 1, 2, 3, 4, 5, 6 or more) | 0%, 10%, 15%, 20%, 25%, 30%, 35% (parts only, not labour or paint; none with zero depreciation)                                |
| Total-loss threshold                                                                  | Repair estimate above 75% of IDV                                                                                               |
| Total-loss payment                                                                    | IDV − salvage − compulsory deductible                                                                                          |
| Theft payment                                                                         | IDV − compulsory deductible                                                                                                    |
| Third-party property damage limit (sample)                                            | 750,000 per claim                                                                                                              |

**Test case CA1** (own damage): 4-year-old 1,200 cc car, IDV 800,000, estimate parts 90,000, labour 40,000, paint 10,000. Without zero depreciation: parts depreciation 25% × 90,000 = 22,500, so payable = 140,000 − 22,500 − 1,000 = **116,500**. With zero depreciation: 140,000 − 1,000 = **139,000**.

**Test case CA2** (total loss): IDV 800,000; repair estimate 700,000 (87.5% of IDV, above the threshold); salvage 120,000. Payable = 800,000 − 120,000 − 1,000 = **679,000**.

**Test case CA3** (theft): IDV 800,000. Payable = 800,000 − 1,000 = **799,000**.

**Test case CA4** (third-party property): assessed damage 900,000; limit 750,000. The insurer pays **750,000**; the owner bears the other 150,000.


