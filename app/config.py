import os

POLICY_SOURCE = os.getenv("POLICY_SOURCE", "fixture")   # fixture until Gate 3, then "live"
ROLES = ("INTERMEDIARY", "UNDERWRITER", "CLAIMS_OFFICER", "ADMIN")
