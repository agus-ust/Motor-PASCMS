# Demo script (rehearse twice, no help, before Gate 4)
Reset to known state first: `python -m shared.fixtures.seed_fixtures --reset`

## Example A - Private car own-damage claim (about 6 minutes)
1. Intermediary: type registration number -> vehicle details autofill -> live premium -> issue policy.
2. Claims officer: FNOL by registration number -> validation ticks -> reserve 140,000.
3. Assessment: show payable 116,500, flip zero-dep -> 139,000 ("explain this payout" view).
4. Approve inside authority -> cashless settlement -> claim closed.
5. Renewal quote: NCB reset visible in the premium breakup.

## Example B - Goods fleet + third-party injury (about 7 minutes)
1. Intermediary: upload 12-truck CSV -> premium 1,877,388.48 -> rule R5 refers to underwriter.
2. Underwriter: referral inbox -> approve with reason.
3. Endorse: add 13th truck mid-term -> 117,336.78.
4. Claims officer: third-party injury FNOL -> reserve 1,500,000 -> case stages -> award 750,000 (BRD A.8 CA4 limit) -> regional head approval.

## Wow moment (3 minutes): launch a product by configuration
Admin: clone private-car version -> create "Electric two-wheeler" product from JSON -> quote it. No code release.

## Proof page
Open /proof: all golden tests green on screen.
