# Motor PAS + CMS Prototype

Configurable motor insurance Policy Administration (PAS) and Claims Management (CMS) prototype.
Stack: Python 3.12, FastAPI, SQLModel on SQLite, Jinja2, HTMX, Bootstrap. Single codebase, one laptop.

## First run (Windows PowerShell)
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest                      # 22 tests should pass on a fresh checkout
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000 (page) and http://127.0.0.1:8000/docs (API test page).

## Day-1 chores (do once)
1. Download Bootstrap CSS (`bootstrap.min.css`) and HTMX (`htmx.min.js`) into `shared/static/vendor/` so the demo works offline.
2. Put the reference schema files (`motor_pas_lite_schema_sqlite.sql` etc.) into `db/`. They are a reference, not the source of truth. SQLModel classes are.
3. Fill in the status block at the bottom of `PROJECT_CONTEXT.md` every evening.

## Folder map
| Folder | Owner | What lives here |
|---|---|---|
| `app/` | Agus | FastAPI entry point, config, router wiring |
| `shared/` | Agus | models, form engine, schemas (JSON), templates, static files, money rules, **contracts.py** |
| `pas/` | Agus | policy, rating, underwriting, endorsement, renewal |
| `cms/` | Praveen | claim, claimant, assessment, reserve, settlement |
| `integrations/` | Agus | mocked adapters (vehicle lookup, KYC, payment, SMS) |
| `data/masters`, `data/rates` | Agus (claims parameters: Praveen) | CSV masters and rate tables |
| `tests/` | Owner of the module under test | pytest, golden cases from BRD A.10 |
| `docs/` | Both | decisions, demo script, UX audit sheet, Copilot prompt templates |

## Rules that never bend
- Money is `Decimal`, rounded half-up to 2 places per line, tax on the sum of lines (`shared/money.py`).
- CMS reads policies only through `shared/contracts.py`. Changing it needs both owners.
- A new product or vehicle class is a JSON schema + rate CSV, never a new `if` in code.
- No feature starts before its golden test exists (`tests/golden_cases.json`).
- Prototype footer stays on every page.
