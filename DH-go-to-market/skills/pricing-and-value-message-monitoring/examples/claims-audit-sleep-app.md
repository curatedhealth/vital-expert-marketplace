# Worked example: A2 claims audit (live connector calls, 19 October 2026)

**Request (illustrative person):** "Is this Instagram ad OK for Germany? It goes to consumers. Our intended purpose, from our instructions for use: digital cognitive behavioral therapy for adults with non-organic insomnia. Our regulatory owner is Jana Weber." The ad text is `evals/files/sleepwell_ad_illustrative.txt`. SleepWell Pro is a fictional product written for this test; its intended purpose is the illustrative person's statement.

## Calls made

1. `verify.extract_claims` on the first five claim sentences of the ad (the live call text; the self-test and disclaimer lines were added to the test file afterwards and split by hand): c1 to c5, one per sentence, all `checkable: true` (`examples/live/verify_calls.json`). "Doctor-recommended and CE-certified." came back as one claim; split by hand into two.
2. `scripts/claim_screen.py --market DE --audience consumer` on the ad: 10 candidate matches in 7 claim sentences (`examples/live/claim_screen_sleepwell_DE.md`).
3. `commercial-dh.audit_claims` not called: SleepWell Pro is fictional and has no record. On real records the tool's labels carry no information while the intended purpose is not stored (`examples/live/audit_claims_summary.json`); only the authorization record it finds is used.
4. No evidence passage was supplied for "6 weeks" or "45 minutes", so no `check_claim` call; both are `[GAP]`.

## Answer (short mode)

**Answer.** Nine claims; three Stop, six Review. The claim that matters most is "cures insomnia in 6 weeks": a cure claim to German consumers can engage the HWG ban on misleading efficacy (PC-DE-03) and, if false, the EU blacklist (PC-EU-10). This audit flags; it does not clear.

| # | Claim | Level | Rows (kind) | Safer draft for the owner |
|---|---|---|---|---|
| 1 | Clinically proven, cures insomnia in 6 weeks | Stop | PC-DE-03, PC-EU-10, PC-DE-05 (law) | "Digital cognitive behavioral therapy for adults with non-organic insomnia." Add a result only with its study, author, date and source |
| 2 | Doctor-recommended | Review | PC-DE-11 (law, public advertising) | Drop, or state who recommends it and on what basis, as the owner decides |
| 3 | CE-certified | Review | PC-EU-11 (law) | State the CE marking and class exactly as the authorization holds them; `[GAP]` until supplied |
| 4 | No side effects | Stop | PC-DE-04 (law) | Drop; give safety information only as the instructions for use state it |
| 5 | Unlike sleeping pills | Review | PC-EU-02, PC-DE-03 (law) | Drop unless a study in this population compared them; then report it as the passage reads |
| 6 | Covered by your health insurance, on prescription | Review | PC-EU-07, PC-EU-08 (law); CP-DE-01 | No listing is stated for this product `[GAP]`; if listed, state the routes (prescription or fund approval) and who they apply to |
| 7 | Sleep 45 minutes longer on average | Review | PC-DE-05, PC-EU-07 | No passage `[GAP]`; keep only a figure read in a source, with comparator and time point |
| 8 | Take the test to find out if you have chronic insomnia | Stop | PC-EU-02 (law: use outside the intended purpose) | Remove: diagnosis is not in the stated intended purpose |
| 9 | Not a medical device; for information only | Review | PC-EU-07 (law: overall presentation) | Remove: it contradicts the product's own intended purpose and does not fix any claim |

**Public-advertising rule.** Outside professional circles, device advertising may not suggest health improves with use (PC-DE-10, PC-DE-09). Claims 1, 4 and 5 sit close to that line; the owner decides.

**Evidence.** "6 weeks" and "45 minutes": no passage `[GAP]`. When supplied: `qualify_source`, then `check_claim`, read in the same direction (register N3).

**Authorization on file.** Not checked: fictional product. Intended purpose: the person's words, from the instructions for use.

**Record.** Draft for the owner: Jana Weber. Claims not cleared. AI-assisted.

Word count of the answer above, excluding the calls list and the table's Rows column: 335 (counted by script).
