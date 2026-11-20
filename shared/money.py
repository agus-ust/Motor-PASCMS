"""Money rules from BRD Appendix A: Decimal only, round every line half-up to 2 places,
calculate tax on the SUM of the lines. Never use float for money."""
from decimal import Decimal, ROUND_HALF_UP

TWO = Decimal("0.01")


def D(x) -> Decimal:
    return x if isinstance(x, Decimal) else Decimal(str(x))


def money(x) -> Decimal:
    return D(x).quantize(TWO, rounding=ROUND_HALF_UP)


def pro_rata(amount, months_remaining: int, term_months: int = 12) -> Decimal:
    """Pro-rata by whole months remaining (BRD A.7: K1, G3)."""
    return money(D(amount) * D(months_remaining) / D(term_months))


def tax_on_sum(lines, rate_pct) -> Decimal:
    total = sum((money(l) for l in lines), Decimal("0"))
    return money(total * D(rate_pct) / D(100))
