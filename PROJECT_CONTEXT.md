# PROJECT CONTEXT - paste this at the top of every Copilot chat

## What we are building
A prototype Motor Insurance PAS (policy admin) and CMS (claims) for five vehicle classes: two-wheeler, private car,
goods-carrying, passenger-carrying, miscellaneous. New products are DATA (JSON schema + rate CSV), not code.
Prototype only: all integrations mocked, illustrative rates, no real data.

## Team and ownership
- Agus owns: party, product, policy, underwriting, rating, shared components, merge.
- Praveen owns: claim, claimant, reserve, assessment, settlement, claims masters and seed data.
- Four logins only: INTERMEDIARY, UNDERWRITER, CLAIMS_OFFICER, ADMIN.

## Stack and layout
Python 3.12, FastAPI, SQLModel + SQLite, Jinja2, HTMX, Bootstrap (vendored). Folders: app/, shared/, pas/, cms/,
integrations/, data/, tests/, docs/. Interface between PAS and CMS: shared/contracts.py (PolicyReader).

## Non-negotiable coding rules
1. Money: Decimal only. Round each line half-up to 2 places. Tax is on the sum of lines. Use shared/money.py.
2. No new library without asking me first.
3. One feature per file. Give me COMPLETE files, not fragments. Max ~150 lines per file.
4. Every function you write gets a pytest test. If the BRD has a golden case (tests/golden_cases.json) use it.
5. Explain each file in two plain sentences so I can defend it to the mentor.
6. Rates, factors, rules and field lists come from CSV/JSON, never hard-coded.
7. If something is not in the BRD, say "not in BRD" and ask. Do not invent numbers.

## Business rules in one breath
OD basic = IDV x base rate x zone x fuel (class factors differ). Net OD = basic x (1 - deductible disc) x (1 - NCB).
Add-ons are a % of net OD. Total before tax = net OD + add-ons + TP + PA. Tax = rate x total. Pro-rata by whole months.
Claims: payable = estimate - parts depreciation - compulsory deductible; total loss if estimate > 75% of IDV
(payable = IDV - salvage - deductible); theft = IDV - deductible; zero-dep waives parts depreciation.

## Status block (update every evening)
- Date:
- Gate reached:
- Done today:
- Broken / stuck:
- Next 3 tasks:
- Files changed today:
