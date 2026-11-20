# Motor PAS + CMS prototype (read first, keep short)

Prototype of a motor insurance Policy Admin (PAS) and Claims (CMS) system. Five vehicle classes: PVT_CAR, TWO_WHEELER, GOODS, PASSENGER, MISC. Four logins: INTERMEDIARY, UNDERWRITER, CLAIMS_OFFICER, ADMIN.

## Stack and layout
Python 3.12, FastAPI, SQLModel on SQLite, Jinja2, HTMX, Bootstrap (vendored in shared/static/vendor). No other libraries without asking.

app/ entry point | shared/ models, db, form engine, templates, money.py, contracts.py | pas/ policy side (Agus) | cms/ claims side (Praveen) | integrations/ mocked adapters | data/ CSV and JSON config | tests/ | docs/

## Ownership
pas/ is Agus. cms/ is Praveen. Do not edit the other owner's folder, and never edit shared/contracts.py, unless the prompt says so. CMS reads policies only through shared/contracts.py (get_reader). pas never imports cms and cms never imports pas.

## Rules
1. Money is Decimal through shared/money.py. Round every line half-up to 2 places. Tax is on the sum of lines. Never float.
2. Rates, factors, rules, field lists and claim parameters live in data/ files (CSV or JSON), never in code. A new product or vehicle class must be addable by files only.
3. Tests first. Write the failing test, then the code. Expected values are in tests/golden_cases.json. Never change a golden value. Never delete or weaken a test to make it pass.
4. If a number, rate or rule is not in the docs/ files, say "not in BRD" and ask. Do not invent it.
5. Nothing is hard-deleted. Retire with is_active or status. Corrections add rows (endorsement, ledger transaction).
6. Small files, about 150 lines. One feature per task. Do not refactor unrelated code. Do not read files the prompt does not name.
7. Run tests with: python -m pytest -q. Report only failing test names and a one-line reason.
8. Prototype: all integrations mocked, sample data marked illustrative, prototype footer on every page.
9. Finish every task with three short lines: files changed, how to run it, assumptions made.

## Docs map (read only what the prompt names)
docs/DATA_MODEL.md tables and columns | docs/brd/*.md BRD excerpts (cut from the full BRD; the .docx is never read directly) | docs/decisions/decision_log.md decisions | tests/golden_cases.json expected values
