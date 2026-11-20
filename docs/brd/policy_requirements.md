<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 192,225. -->
## 7. Policy administration requirements

Each requirement has a build tier: **Build**, **Simple** or **Later**, as defined in Section 2.

| ID    | Requirement                                                                                                                                                          | Tier   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| PA-01 | Capture and validate owner and proposer details, with KYC status and duplicate-party detection                                                                       | Build  |
| PA-02 | Product catalogue by vehicle class with versioning, effective dates and region availability                                                                          | Simple |
| PA-03 | Dynamic quote and proposal forms drawn from the product schema for each vehicle class (Section 5)                                                                    | Build  |
| PA-04 | Vehicle details capture, with a mocked vehicle database that pre-fills make, model, year and specification from the registration number                              | Simple |
| PA-05 | IDV calculation: manufacturer's listed price less age-based depreciation, plus accessories, with an underwriter override within a set limit                          | Build  |
| PA-06 | Rating engine: base rates, zone, fuel, class factors, deductibles, claim-free discount, add-ons, third-party tariff, minimum premium, with a visible premium breakup | Build  |
| PA-07 | Underwriting rules: accept, refer, hold, decline, with reasons and a referral queue                                                                                  | Build  |
| PA-08 | Pre-inspection for break-in and older vehicles: request, photo upload, findings, approval                                                                            | Simple |
| PA-09 | Policy issuance with number generation per branch and class; schedule and certificate as printable pages                                                             | Build  |
| PA-10 | Endorsements: change IDV, accessories, address, financier, vehicle details, add-ons, with pro-rata premium and approval                                              | Build  |
| PA-11 | Cancellation with pro-rata or short-period refund; ownership transfer to a new owner                                                                                 | Simple |
| PA-12 | Renewal: notice, renewal quote using claim history and claim-free discount, lapse and break-in handling, rollover from another insurer                               | Build  |
| PA-13 | Fleet policies: many vehicles on one policy, CSV upload, add or remove vehicles mid-term with pro-rata premium, fleet discount and experience adjustment             | Simple |
| PA-14 | Claim-free discount tracking by owner, including transfer from the previous insurer or to a new vehicle                                                              | Build  |
| PA-15 | Previous insurer and claim history check through a mocked industry database                                                                                          | Simple |
| PA-16 | Tax handling: premium or sales tax by jurisdiction, with configurable rates and exemptions                                                                           | Simple |
| PA-17 | Commission and brokerage calculation per intermediary plan                                                                                                           | Later  |
| PA-18 | Document templates per product (schedule, certificate, renewal notice)                                                                                               | Build  |
| PA-19 | Full audit trail on every change, with before and after values                                                                                                       | Build  |
| PA-20 | Search by policy number, registration number, chassis number, owner name, mobile, tax or national ID, claim number                                                   | Build  |
| PA-21 | Customer communication triggers (issuance, renewal, endorsement) through mocked channels                                                                             | Later  |
| PA-22 | Multi-language labels (English only in the prototype)                                                                                                                | Later  |
| PA-23 | Instalment premium, payment failure and lapse handling                                                                                                               | Later  |
| PA-24 | Co-insurance (lead and follow shares) on large commercial fleets                                                                                                     | Later  |
| PA-25 | Usage-based discounts from telematics or driving-score data                                                                                                          | Later  |

> **Pro-rata** = premium charged or refunded in proportion to the time the cover is in force. **Short-period** = a refund scale that returns less than pro-rata when a policy is cancelled early, to cover acquisition costs. **Break-in** = a gap between the old policy expiry and the new one; the vehicle is usually inspected before cover restarts. **Rollover** = renewing with a different insurer. **Pre-inspection** = checking and photographing a vehicle before cover starts, to record existing damage. **Claim-free discount (NCB) transfer** = the discount follows the owner's claim history, so it moves with them when they change insurer or buy another vehicle. **Tax jurisdiction** = the region treated as where the cover is delivered, which decides which tax rules and rates apply. **Telematics** = data from a device or app that records how a vehicle is driven.


