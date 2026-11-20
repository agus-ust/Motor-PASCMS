"""THE interface between PAS (Agus) and CMS (Praveen).

CMS only ever reads policies through a PolicyReader. In Weeks 1-3 CMS uses FixturePolicyReader;
at Gate 3 the app switches to DbPolicyReader (Agus) with ONE config change (POLICY_SOURCE=live).
Change this file only with both owners' sign-off (Gate 1 freezes it).
"""
from __future__ import annotations
import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional, Protocol

FIXTURE_FILE = Path(__file__).parent / "fixtures" / "policies.json"


@dataclass(frozen=True)
class RiskSnapshot:
    risk_no: int
    vehicle_class: str            # PVT_CAR | TWO_WHEELER | GOODS | PASSENGER | MISC  (codes agreed at mid-week-3 sync)
    registration_no: str
    chassis_no: str
    engine_no: str
    make: str
    model: str
    variant: str
    manufacture_year: int
    engine_cc: Optional[int]
    idv: float
    coverages: tuple = ()         # e.g. ("OD", "TP", "ZERO_DEP")
    ncb_pct: float = 0.0


@dataclass(frozen=True)
class PolicySnapshot:
    policy_no: str
    product_code: str
    status: str                   # ISSUED | CANCELLED | LAPSED | QUOTE
    inception: date
    expiry: date
    insured_party_id: int
    premium_paid: bool
    risks: tuple = field(default_factory=tuple)

    def in_force_on(self, loss_date: date) -> bool:
        """CL-02 first check: policy in force on the loss date and premium paid."""
        return self.status == "ISSUED" and self.premium_paid and self.inception <= loss_date <= self.expiry

    def risk_by_registration(self, registration_no: str) -> Optional[RiskSnapshot]:
        for r in self.risks:
            if r.registration_no.replace(" ", "").upper() == registration_no.replace(" ", "").upper():
                return r
        return None


class PolicyReader(Protocol):
    def get_by_policy_no(self, policy_no: str) -> Optional[PolicySnapshot]: ...
    def find_by_registration(self, registration_no: str) -> list[PolicySnapshot]: ...


def _from_dict(d: dict) -> PolicySnapshot:
    risks = tuple(RiskSnapshot(**{**r, "coverages": tuple(r.get("coverages", []))}) for r in d["risks"])
    return PolicySnapshot(
        policy_no=d["policy_no"], product_code=d["product_code"], status=d["status"],
        inception=date.fromisoformat(d["inception"]), expiry=date.fromisoformat(d["expiry"]),
        insured_party_id=d["insured_party_id"], premium_paid=d["premium_paid"], risks=risks)


class FixturePolicyReader:
    """Reads shared/fixtures/policies.json. Regenerate that file by script whenever the schema version changes."""

    def __init__(self, path: Path = FIXTURE_FILE):
        self._policies = [_from_dict(p) for p in json.loads(Path(path).read_text(encoding="utf-8"))]

    def get_by_policy_no(self, policy_no):
        return next((p for p in self._policies if p.policy_no == policy_no), None)

    def find_by_registration(self, registration_no):
        return [p for p in self._policies if p.risk_by_registration(registration_no)]


def get_reader(source: str = "fixture") -> PolicyReader:
    if source == "fixture":
        return FixturePolicyReader()
    if source == "live":
        from pas.reader import DbPolicyReader   # Agus creates this in Week 4 (Gate 3)
        return DbPolicyReader()
    raise ValueError(f"POLICY_SOURCE must be 'fixture' or 'live', got {source!r}")
