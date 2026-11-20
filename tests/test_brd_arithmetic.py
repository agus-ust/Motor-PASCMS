"""Independent hand-calculation of every BRD Appendix A.10 case, written straight from the BRD tables.
Purpose: prove the BRD's own numbers are consistent BEFORE the rating engine exists.
When the real engine is built, tests/test_rating_golden.py must reproduce the same totals."""
import json
from decimal import Decimal as Dc
from pathlib import Path
from shared.money import money, pro_rata, tax_on_sum

GOLD = {c["id"]: c for c in json.loads((Path(__file__).parent / "golden_cases.json").read_text())["cases"]}


def total(lines, tax_pct):
    s = sum((money(x) for x in lines), Dc(0))
    return s + tax_on_sum(lines, tax_pct)


def test_D1_idv():
    assert money(Dc(1_000_000) * (1 - Dc("0.30"))) == Dc(GOLD["D1"]["expected_idv"])


def test_M1():
    od = money(Dc(800000) * Dc("0.032") * Dc("1.10") * Dc("1.00") * Dc("0.90") * Dc("0.75"))
    lines = [od, money(od * Dc("0.12")), 350, 3400, 300]
    assert od == Dc("19008.00")
    assert total(lines, 10) == Dc(GOLD["M1"]["expected_total"])


def test_M2():
    od = money(Dc(2_000_000) * Dc("0.034") * Dc("1.00") * Dc("1.05"))
    assert total([od, 7900, 300], 8) == Dc(GOLD["M2"]["expected_total"])


def test_N1():
    od = money(Dc(700000) * Dc("0.032") * Dc("1.10") * Dc("0.90") * Dc("0.65"))
    assert total([od, money(od * Dc("0.12")), 350, 3400, 300], 10) == Dc(GOLD["N1"]["expected_total"])


def test_K1():
    prem = Dc("25338.96")
    refund = pro_rata(prem, 9)
    tax_refund = money(refund * Dc("0.10"))
    assert refund + tax_refund == Dc(GOLD["K1"]["expected_total"])


def test_T1():
    od = money(Dc(90000) * Dc("0.018") * Dc("1.00") * Dc("1.00") * Dc("0.80"))
    assert total([od, money(od * Dc("0.10")), 750, 300], 12) == Dc(GOLD["T1"]["expected_total"])


def test_G1():
    od = money(Dc(2_400_000) * Dc("0.034"))
    assert total([od, 27500, 160], 10) == Dc(GOLD["G1"]["expected_total"])


def test_G2_and_G3():
    od = money(Dc(2_400_000) * Dc("0.034") * Dc("1.20") * Dc("1.30") * Dc("0.90"))
    per_truck = od + 27500 + 160
    assert per_truck == Dc("142226.40")
    assert total([per_truck * 12], 10) == Dc(GOLD["G2"]["expected_total"])
    g3 = pro_rata(per_truck, 9)
    assert total([g3], 10) == Dc(GOLD["G3"]["expected_total"])


def test_PC1():
    od = money(Dc(700000) * Dc("0.033") * Dc("0.90") * Dc("1.10"))
    assert total([od, 9000 + 4 * 150, 80], 8) == Dc(GOLD["PC1"]["expected_total"])


def test_PC2():
    od = money(Dc(3_500_000) * Dc("0.033") * Dc("1.15"))
    assert total([od, 28000 + 30 * 150, 160], 10) == Dc(GOLD["PC2"]["expected_total"])


def test_X1():
    od = money(Dc(5_000_000) * Dc("0.026") * Dc("1.10") * Dc("0.70"))
    assert total([od, money(Dc(6500) * Dc("0.5")), 80], 12) == Dc(GOLD["X1"]["expected_total"])


def test_X2():
    od = money(Dc(900000) * Dc("0.018") * Dc("0.95") * Dc("0.80"))
    assert total([od, 3500, 300], 10) == Dc(GOLD["X2"]["expected_total"])


def test_claims_CA1_to_CA4():
    est = Dc(140000); parts = Dc(90000); ded = Dc(1000)
    assert est - money(parts * Dc("0.25")) - ded == Dc(GOLD["CA1"]["expected_payable"])
    assert est - ded == Dc(GOLD["CA1"]["expected_payable_zero_dep"])
    assert Dc(700000) / Dc(800000) > Dc("0.75")                       # total-loss trigger
    assert Dc(800000) - Dc(120000) - ded == Dc(GOLD["CA2"]["expected_payable"])
    assert Dc(800000) - ded == Dc(GOLD["CA3"]["expected_payable"])
    assert min(Dc(900000), Dc(750000)) == Dc(GOLD["CA4"]["expected_payable"])
