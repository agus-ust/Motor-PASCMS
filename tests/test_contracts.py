from datetime import date
from shared.contracts import FixturePolicyReader, get_reader


def test_fixture_reader_loads():
    r = FixturePolicyReader()
    p = r.get_by_policy_no("FIX-PC-0001")
    assert p and p.risks[0].idv == 800000


def test_in_force_check_cl02():
    r = FixturePolicyReader()
    assert r.get_by_policy_no("FIX-PC-0001").in_force_on(date(2026, 8, 15))
    assert not r.get_by_policy_no("FIX-PC-0001").in_force_on(date(2027, 6, 1))     # after expiry
    assert not r.get_by_policy_no("FIX-PC-LAPSED").in_force_on(date(2025, 6, 1))   # lapsed status


def test_find_by_registration_ignores_spaces_and_case():
    r = FixturePolicyReader()
    assert r.find_by_registration("kl 01 ab 1234")[0].policy_no == "FIX-PC-0001"


def test_unknown_source_rejected():
    import pytest
    with pytest.raises(ValueError):
        get_reader("banana")
