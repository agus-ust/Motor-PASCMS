from decimal import Decimal
from shared.money import money, pro_rata, tax_on_sum


def test_half_up_not_bankers():
    assert money("2533.896") == Decimal("2533.90")
    assert money("0.125") == Decimal("0.13")      # Python round() would give 0.12


def test_pro_rata_k1_and_g3():
    assert pro_rata("25338.96", 9) == Decimal("19004.22")      # K1 premium refund
    assert pro_rata("142226.40", 9) == Decimal("106669.80")    # G3 premium


def test_tax_on_sum_m1():
    lines = ["19008.00", "2280.96", "350", "3400", "300"]
    assert tax_on_sum(lines, 10) == Decimal("2533.90")
