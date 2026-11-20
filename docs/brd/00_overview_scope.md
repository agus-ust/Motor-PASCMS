<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 1,91 420,457. -->
# Motor Insurance Policy Admin and Claims System: Prototype Brief and BRD

Nov 5, 2026 · @Shryans Baid

## 1. Project brief

**This is a prototype.** We are building a working, demonstrable Policy Administration System (PAS) and Claims Management System (CMS) for the motor line of a general (non-life) insurer, covering every vehicle type. It proves the design and the product-configuration approach before a production build; it is not a production system and will not carry live policyholder data.

**Build constraint.** One non-technical fresher must be able to build this in 6 weeks, with an AI coding assistant, a mentor for a weekly review and a laptop only. Every choice here is made for that: one language, one database file, no separate front-end project, and scope tiers (Section 2) that separate what is built, what is shown by configuration, and what is only described.

> **PAS** = the system of record that issues and maintains policies from quote to renewal. **CMS** = the system that handles a loss from first notice to settlement and recovery. **General (non-life) insurance** = short-term covers (usually one year) for motor, property, health and similar risks, as opposed to life insurance. Line of business (LOB) = a class of insurance such as motor or property; this document covers motor only. Motor insurance = cover for loss of or damage to a vehicle and for the owner's legal liability to others arising from its use.

| Item                          | Statement                                                                                                                                                                                                |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Problem                       | General insurers often run motor products on rigid systems, so launching a new vehicle class, product variant or region takes months, and fleet and third-party claims are often handled by hand.        |
| Proposed answer               | One configurable platform where a new vehicle class or product is defined as data (fields, rules, rates), not new code.                                                                                  |
| Prototype goal                | Quote-to-claim in depth for all vehicle classes (two-wheeler, private car, goods-carrying, passenger-carrying and miscellaneous), including servicing, fleets, own-damage, theft and third-party claims. |
| Back end                      | Python (FastAPI) with a SQLite database file, running on a laptop; PostgreSQL is the production path.                                                                                                    |
| Front end                     | Plain HTML pages from Jinja2 templates with HTMX, drawn by one schema-driven form renderer; React is a production-stage option.                                                                          |
| Primary audience for the demo | Insurer leadership, product, underwriting, claims and IT stakeholders.                                                                                                                                   |
| Out of scope                  | Live payments, real regulator filings, production data migration. All integrations are mocked.                                                                                                           |

**Success measures for the prototype**

- A new product (for example, an electric two-wheeler product) can be added through configuration alone, with no code release.

- One policy can be taken from quote to issuance to endorsement to claim to settlement in a single guided demo.

- Every vehicle class's field set in Section 8 renders, validates and saves from the same form engine.

- Stakeholders can see regional hierarchy, tax and rating differences work across at least 3 regions.

## 2. Prototype scope

The 6-week build covers the whole motor journey in depth (quote, issue, endorse, renew, claim, settle) for every vehicle class; anything needing a live external party is mocked or only described. In the tables of Sections 7, 9 and 10, Build means built in full, Simple means built in a simplified form, and Later means described but not built.

| Capability                                                                                                              | 6-week treatment                                           |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| Login with 4 roles (Intermediary, Underwriter, Claims officer, Admin)                                                   | Build, simple session login with seeded users              |
| Party master (owners, drivers, intermediaries)                                                                          | Build                                                      |
| Product configuration: one schema file and rate CSVs per vehicle class, with an admin page that lists and previews them | Build                                                      |
| Schema-driven forms for all five vehicle classes                                                                        | Build                                                      |
| IDV calculation (listed price less age-based depreciation)                                                              | Build                                                      |
| Rating: rate tables, factors, claim-free discount, add-ons, third-party tariff                                          | Build                                                      |
| Underwriting rules and referral queue                                                                                   | Build                                                      |
| Policy issue, endorsement, renewal with claim-free discount                                                             | Build                                                      |
| Fleet policies uploaded from a CSV file, with vehicles added or removed mid-term                                        | Simple                                                     |
| Cancellation and ownership transfer                                                                                     | Simple                                                     |
| Pre-inspection with photo upload and approval                                                                           | Simple                                                     |
| Claims: own damage, theft, total loss, assessment, approval, settlement                                                 | Build                                                      |
| Third-party property and injury claims with case status                                                                 | Simple                                                     |
| Fraud flags (rules table), salvage and recovery record                                                                  | Simple                                                     |
| Policy and claim documents                                                                                              | Build, as printable HTML pages (browser Print to PDF)      |
| Dashboards: frequency, severity and loss ratio by vehicle class and region                                              | Build                                                      |
| Audit log                                                                                                               | Build, one helper that records every change                |
| Co-insurance and reinsurance                                                                                            | Simple: share percentage fields and a CSV extract          |
| Finance and tax                                                                                                         | Simple: a receipt record and one tax calculation by region |
| KYC, vehicle database, previous-insurer check, payment, SMS and email                                                   | Mock: a button returns sample data                         |
| Regulatory reports, data protection controls, tax e-invoicing, telematics discounts                                     | Described only                                             |
| Mobile apps, portals, extra languages                                                                                   | Out of scope                                               |

> **Bordereau** = a periodic listing of policies or claims sent to a reinsurer or co-insurer so they can track what they share in. **Reinsurance** = insurance bought by the insurer to pass on part of its risk.

## 3. Users and roles

Access is role-based and scoped by region, so a branch user sees only their own branch and below.

In the 6-week build only four logins exist: Intermediary, Underwriter, Claims officer and Admin. The other roles are described but not coded, and region scoping is a filter, not a security layer.

| Role                                        | Main job                            | Key permissions                                                       |
|---------------------------------------------|-------------------------------------|-----------------------------------------------------------------------|
| Intermediary (agent, broker, online seller) | Sells and services policies         | Create quotes, issue within authority, view own book                  |
| Underwriter                                 | Accepts, prices and declines risk   | Review referrals, override rates within a limit, approve endorsements |
| Policy servicing officer                    | Handles changes and renewals        | Process endorsements, cancellations, renewals                         |
| Claims intake officer                       | Registers a loss                    | Register claim, upload documents, assign surveyor                     |
| Claims assessor or adjuster                 | Decides the claim                   | Set reserve, approve within authority, request documents              |
| Surveyor (external)                         | Inspects and assesses loss          | View assigned claims, upload survey report                            |
| Finance officer                             | Premium, commission, claim payments | Receipts, ledger, payment approvals                                   |
| Reinsurance officer                         | Manages ceded risk                  | Treaty set-up, cession reports                                        |
| Product manager                             | Configures products                 | Create products, fields, rates, rules, document templates             |
| Compliance and audit                        | Oversight                           | Read-only access, audit trail, regulatory extracts                    |
| System administrator                        | Platform control                    | Users, roles, regions, master data                                    |

> **Intermediary** = a person or firm licensed to sell and service policies, such as an agent or a broker. **Surveyor** = an independent licensed professional who inspects a loss and reports to the insurer on cause and amount. **Underwriter** = the person who decides whether to accept a risk and at what price. **Authority limit** = the maximum amount or risk size a person may approve without escalating.

**Authority matrix (prototype defaults, configurable)**

- Claims: up to a set amount by assessor, higher by regional head, highest by head office.

- Underwriting: standard risks auto-approved; risks above a sum insured threshold or flagged by rules go to referral.


## 13. Worked examples for the demo

Both examples use illustrative figures in a generic currency unit, not real rates, and double as the scripted demo journeys.

In the 6-week build, co-insurance and reinsurance appear only as share-percentage fields and a CSV export.

### Example A: Private car own-damage claim

A private car with an IDV of 800,000 and a zero-depreciation add-on is hit from behind. The repair estimate is 140,000 (parts 90,000, labour 40,000, paint 10,000), and the compulsory deductible is 1,000.

| Step               | What the system does                                                                                                                                 |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1\. FNOL           | Intake officer searches by registration number; the system confirms the policy was in force and shows the motor claim form                           |
| 2\. Validation     | Loss date within period, own-damage cover present, vehicle matches the risk item, no open duplicate                                                  |
| 3\. Survey         | Surveyor assigned from the regional panel; estimate and photos uploaded; document checklist ticks off                                                |
| 4\. Reserve        | Reserve set at 140,000, with the history recorded                                                                                                    |
| 5\. Assessment     | Payable = estimate − deductible = 139,000 with zero depreciation. Without the add-on, assuming 25% depreciation on parts (22,500), payable = 116,500 |
| 6\. Approval       | Within the assessor's authority, so approved directly                                                                                                |
| 7\. Payment        | Cashless settlement to the garage; claim closed and the customer notified through the mock channel                                                   |
| 8\. Renewal effect | The claim is recorded; the no-claim bonus resets at renewal and the renewal quote reflects it                                                        |

### Example B: Goods fleet policy and a third-party injury claim

A transport company insures 12 heavy trucks (GVW 16,000 kg) that carry hazardous goods on national permits.

| Stage        | What the system shows                                                                                                                                                                                                                        |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quote        | A fleet CSV with 12 vehicles is uploaded; permit, goods type and driver details are validated; premium follows test G2 in Appendix A                                                                                                         |
| Underwriting | Hazardous goods triggers rule R5, so the case goes to an underwriter for referral and approval; the fleet's 3-year claims experience (loss ratio 60%) sets the experience adjustment                                                         |
| Issuance     | One fleet policy with 12 vehicle certificates; premium before tax 1,706,716.80; total with 10% tax 1,877,388.48                                                                                                                              |
| Endorsement  | After 3 months a 13th truck is added with pro-rata premium for 9 months (total 117,336.78); a sold truck is removed with a pro-rata refund                                                                                                   |
| Claim        | A truck hits a motorcyclist, who is seriously injured. First notice records the police report, driver licence (valid for the class), claimant details and injuries; the claim type is third-party injury and the reserve is set at 1,500,000 |
| Case stages  | The claim moves through notice, tribunal case opened, hearings, and award or settlement, with dates and lawyer details                                                                                                                       |
| Settlement   | The award is agreed at 1,250,000; the amount is above the assessor's authority, so the regional head approves; payment is recorded and the reserve closed                                                                                    |
| Reporting    | Fleet loss ratio, frequency and severity update; the claim appears in the claims register and the CSV extract for reinsurers                                                                                                                 |

> **Hazardous goods** = loads such as fuel, chemicals or gas that can cause fire, explosion or pollution, which raises the cost of third-party claims. **Experience adjustment** = an increase or decrease in a fleet's premium based on its past loss ratio.


