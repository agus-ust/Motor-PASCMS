# Decision log (one line per decision, link to an ADR when it needs more than a line)
| # | Date | Decision | Owner | ADR |
|---|---|---|---|---|
| 1 | | Party tables owned by Agus; Praveen reads through the read interface | Agus, Praveen | |
| 2 | | Co-insurance deferred; fleet simplified (CSV, per-vehicle rating, R6) | Agus | |
| 3 | | Claims parameters (deductible, depreciation, total-loss %) follow BRD A.8 unless Shryans changes them | Praveen | |
| 4 | 2026-11-20 | BRD is the source for the four claims rules: two-wheeler deductible 100; parts depreciation by age (A.8); total loss = IDV - salvage - deductible; theft = IDV - deductible. Build Checklist values are superseded. | Praveen | |
| 5 | 2026-11-20 | CA4 third-party property payable = 750,000 (BRD A.8 and golden file). The 1,250,000 in demo_script.md is wrong and is corrected. | Praveen | |
| 6 | 2026-11-20 | itsdangerous added to requirements.txt for session login (approved). Build runs from one account (Praveen); pas/ work is reviewed in-repo, not built by Agus. | Praveen | |
