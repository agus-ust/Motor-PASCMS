# Ownership and handoffs
| Area | Owner | Reviewer |
|---|---|---|
| shared/models.py (PAS tables) | Agus | Praveen reads |
| cms/models.py (CMS tables) | Praveen | Agus reads |
| shared/contracts.py | BOTH (frozen at Gate 1) | each other |
| shared/form_engine.py, schemas/*.json | Agus | Praveen (claim schemas) |
| pas/rating.py, pas/underwriting.py | Agus | Praveen runs the golden tests |
| cms/assessment.py | Praveen | Agus runs CA1-CA4 |
| Merge (Week 5) | Agus | Praveen fixes claims-side defects |

Rule: never edit a file you do not own without a message first. Branches: `pas/<feature>`, `cms/<feature>`, merged to `main` by PR after the other person has run `pytest`.
Tags: `gate-week1` ... `gate-week5` on main when the Friday gate passes.
