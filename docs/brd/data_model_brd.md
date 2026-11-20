<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 117,175. -->
## 5. Data model and the product configuration engine

**Every policy has a common core plus a line-specific block described by a product schema.** This is how one system serves two-wheelers, cars, trucks, buses and special vehicles without a table per vehicle class.

**Core entities (shared by all lines)**

| Entity                       | Purpose                                                   | Key fields                                                                                                                                              |
|------------------------------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Party                        | Any person or organisation                                | Party ID, type (owner, driver, claimant, intermediary, garage, surveyor), name, national ID, tax number, KYC status, addresses, contacts                |
| Product                      | A sellable cover                                          | Code, vehicle class, version, effective dates, status, linked schema, rate tables, rules                                                                |
| Policy                       | Issued contract (a quote is a policy with status Quote)   | Policy number, product, cover type, insured, period, total IDV, premium, tax, branch, channel, status, claim-free percentage, previous policy reference |
| Risk Item (vehicle)          | Each insured vehicle on a policy                          | Risk ID, policy, registration number, vehicle class, vehicle data (JSON), IDV, accessories, financier                                                   |
| Driver                       | People who drive the vehicle                              | Licence number and class, validity, date of birth, experience, link to policy or vehicle                                                                |
| Coverage                     | Covers and add-ons on a vehicle                           | Coverage code, limit, deductible, premium, add-on flag                                                                                                  |
| Endorsement                  | Mid-term change                                           | Type, effective date, premium difference, reason, approval trail                                                                                        |
| Inspection                   | Check of a vehicle before cover or after a loss           | Request, mode, photos, findings, status                                                                                                                 |
| Claim                        | A reported loss                                           | Claim number, policy, vehicle, loss date and place, type, cause, status, reserves, paid                                                                 |
| Claimant                     | Injured person or owner of damaged property (third party) | Claimant, type, injuries, damage, representative, case status                                                                                           |
| Claim Transaction            | Money and reserve movements                               | Reserve, payment, recovery, salvage, with date and approver                                                                                             |
| Garage                       | Repair network                                            | Garage ID, name, region, cashless flag, agreed rates                                                                                                    |
| Intermediary                 | Seller                                                    | Licence, type, commission plan, region                                                                                                                  |
| Org Unit                     | Region hierarchy                                          | Zone, state or province, region, branch, with parent links                                                                                              |
| Reinsurance and Co-insurance | Shared risk                                               | Share percentage per policy, treaty reference                                                                                                           |
| Document                     | Files and letters                                         | Type, linked entity, version, generated or uploaded                                                                                                     |
| Audit Log                    | Who changed what                                          | User, time, entity, before and after                                                                                                                    |

> **Sum insured** = the maximum amount the insurer will pay for a loss under the policy. **Deductible (excess)** = the part of each loss the policyholder bears. **Endorsement** = a recorded change to a policy during its term, such as adding a vehicle. **Reserve** = the amount the insurer sets aside for a reported claim that is not yet paid.

**The product configuration engine: how fields are structured**

Each product points to a versioned schema that lists its fields. The back end validates against it, and the web form renders from it. Fields are grouped into sections, support conditions (show this only if that is true), and can be used in rating and rules.

{  
"schema_code": "MOTOR_PVT_CAR",  
"version": 3,  
"sections": \[  
{  
"key": "vehicle",  
"title": "Vehicle details",  
"fields": \[  
{"key": "registration_no", "type": "string", "required": true,  
"validation": {"regex": "^\[A-Z0-9-\]{4,12}\$"}},  
{"key": "fuel_type", "type": "enum", "options": "MASTER:FUEL_TYPE", "required": true},  
{"key": "idv", "type": "money", "required": true, "used_in": \["rating"\]},  
{"key": "cng_kit_value", "type": "money",  
"visible_if": "fuel_type in \['CNG','LPG'\]"}  
\]  
}  
\]  
}

**Field types supported:** string, number, money, date, boolean, enum (from master data), multi-select, address, file upload, repeating group (for example, a list of locations or drivers), and calculated field.

**Storage approach:** core fields are normal table columns; the line-specific block is one JSON column (JSONB in PostgreSQL later) with the schema version stored on the record. The few fields needed for search, rating or reports are also copied into normal columns. This keeps products fast to add and still reportable.

> **IDV (Insured Declared Value)** = the agreed market value of a vehicle used as the sum insured in motor policies.

**Tables to build in the 6-week build:** Party, Product, Policy, Risk Item (the vehicle), Driver, Endorsement, Inspection, Claim, Claimant, Claim Transaction, Garage, Document (file name only), Audit Log and Org Unit. Coverage lives as a JSON list inside the risk item, intermediary is a flag on Party, and co-insurance and reinsurance are fields on the policy.


