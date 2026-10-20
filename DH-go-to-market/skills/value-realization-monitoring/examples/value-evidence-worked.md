# Worked run: A1 threshold review and A2 value evidence check (illustrative data)

Illustrative. The account file, the two target versions and the five notes in `examples/sample-data/` were written for this example; they describe no real customer or person. Run on 19 October 2026.

## Request

"Before our board review: did our July target change flatter the numbers, and were the October notes to customers right?"

## Calls and runs

- `python3 scripts/account_health.py thresholds examples/sample-data/accounts_illustrative.csv --targets examples/sample-data/targets_illustrative_v2.json --previous examples/sample-data/targets_illustrative_v1.json` (output: `examples/runs/thresholds.md`)
- `python3 scripts/account_health.py notes examples/sample-data/accounts_illustrative.csv --notes examples/sample-data/notes_illustrative.csv --tol 0.005` (output: `examples/runs/notes.md`)
- `verify.extract_claims` on the text of a note like VN-01, VN-02 and VN-04 combined (live, `examples/live/verify.json`): three claims; the third joins "clinically proven" with "will cut your behavioral health costs" and is marked checkable.

## Answer (short mode, as the skill would hand it over)

**Answer.** Two targets were eased in v2 (set 15 July 2026, after the Q2 period closed) and each turned two accounts to met at 30 September 2026: activation 0.5 to 0.4 (Lakeside, Northfield; Lakeside also gained its own 0.35 target) and the PHQ-9 5-point share 0.6 to 0.5 (Lakeside, Northfield). Under v1, neither account would meet activation. Whether the changes stand is your decision; no reason is recorded in the files. Of five October notes, two are supported by their rows, one differs and two are unsupported.

| Note | Account | Sent | Row | Status |
|---|---|---|---|---|
| VN-01 | Northfield | 62% activated | 455 of 1,000 (45.5%) | value differs |
| VN-02 | Northfield | PHQ-9 mean drop of 6 | no such measure tracked | unsupported |
| VN-03 | Lakeside | 41.6% active, 90 days | 0.416 | supported |
| VN-04 | Riverbend | "clinically proven to reduce depression" | no measure named | unsupported |
| VN-05 | Northfield | 55% with a 5-point drop | 11 of 20 starters | supported |

**Wording no row can carry.** VN-04 states clinical effect; uptake and customer-reported outcomes are not clinical evidence (CS32). It stops for your regulatory or legal owner. VN-05 says "moderate or worse symptoms": acceptable only as the PHQ-9 band at 10 or more (CS92).

**Other flags.** Harbor sent no PHQ-9 data for Q3. Riverbend's activation is computed on enrolled members, so it is not reach (CS27) and was left out of met and missed.

**Open questions.** Is a reason recorded for the July changes? Who owns the VN-01 and VN-04 corrections: owner not named. What tolerance do you accept (0.005 used here as stated in the run)?

**Record.** Review on data you supplied. Uncleared.
