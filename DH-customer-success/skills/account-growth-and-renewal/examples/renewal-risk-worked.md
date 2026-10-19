# Worked example: A1 renewal horizon, then B1 risk note and plan

Run on 19 October 2026. The account file and the definitions are illustrative, written for this example and labeled so (`sample-data/accounts_illustrative.csv`, `sample-data/definitions_illustrative.json`). The library calls are real (`live/`). The action scores are illustrative scores typed for the measurement and presented here as the example person's.

**Request:** "As of today, which renewals fall in the next 120 days, and which are at risk? Our rule: not ready, and at risk, if go-live is not done or any implementation item is open. For ACC-11 we are weighing three actions; scores attached. I own the plan (Dana Ortiz). The product is our substance use disorder therapy app, De Novo DEN160018; the customer's clinicians bill DMHT codes."

**Calls and runs**

1. `scripts/renewal_metrics.py horizon sample-data/accounts_illustrative.csv sample-data/definitions_illustrative.json` (output saved in `sample-data/horizon_run_2026-10-19.txt`).
2. `analytics.mcda` with the person's three actions, criteria risk_reason_addressed, effort_avoided, customer_time_avoided, weights 0.5, 0.25, 0.25 (`live/mcda_renewal_actions.json`).
3. `commercial-dh.map_money_flow {reference: "DEN160018", user, buyer, payer as stated}` (`live/map_money_flow_reset.json`), to record the roles only.

## Answer (short mode)

**Three renewals fall between 19 October 2026 and 16 February 2027. On your rule, one is ready (ACC-10, 30 November 2026) and two are at risk: ACC-11 (15 December 2026: go-live not done, 4 open implementation items) and ACC-12 (31 January 2027: 1 open item).** The first action in the chain is closing ACC-11's open items, because your rule keeps it at risk until then.

| Account | Contract | Renewal | Days | Your rule | Reason from the record |
|---|---|---|---|---|---|
| ACC-10 | CT-1010 | 30 November 2026 | 42 | ready | none hit |
| ACC-11 | CT-1011 | 15 December 2026 | 57 | at risk | go_live = no; open_impl_items = 4 |
| ACC-12 | CT-1012 | 31 January 2027 | 104 | at risk | open_impl_items = 1 |

**Check the record:** ACC-08's renewal date passed on 31 August 2026 and the file still says open.

**Your scored actions for ACC-11:** bridge term until go-live 75; close open implementation items 68.75; sponsor review of agreed outcomes 68.75. The last two tie. The ranking is your scores and weights, not a recommendation; at 0.5 weight on "risk reason addressed", closing the items scores highest on that criterion (50 of its 68.75).

**Stops:** the bridge term is a contract term (legal owner, not named). Any credit or free service offered to keep ACC-11 is an offer element: a free item to win a renewal is outside the discount definition unless narrow conditions hold (FA10), and a free device would remove the customer's G0552 billing basis (CP-US-59). Those stop for your compliance owner (not named). Whether a Federal program pays is theirs to determine.

**What it means for you:** "value unseen" at ACC-11 cannot be separated from the open implementation yet, since implementation outcomes come before service outcomes (CS32). If ACC-11 does not renew, the BAA's return or destroy step applies (CS100).

**Owners:** plan, Dana Ortiz; each action: owner not named. Who owns each?

**Record:** Risk note draft on your data. Uncleared. AI-assisted.

The full version adds the readiness facts per account, hypotheses with what would confirm them, and the contract and data points table.

## What this example shows

- The readiness and risk verdicts come from one rule the person stated; no account is called healthy.
- The connector ranked only the person's scores; the tie it did not report is stated.
- The highest-ranked action is a contract term, so it stops for an owner; the ranking does not decide.
- The money-flow call recorded roles only; it did not decide whether a Federal program pays (its payer listings were empty because DMHT rows are code-level).
