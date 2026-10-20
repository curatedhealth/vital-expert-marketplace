# Launch measures: what is sourced and what is the person's

The research files hold no launch benchmarks, no "good" launch-week numbers and no rule for how many accounts a rep should reach. Every threshold, target and pass rule in this skill is the person's. National or peer figures are context, never targets. This file says how to define and compute measures honestly, and where a measure touches a sourced rule.

## Measure sheet (the person defines it)

Each measure the person keeps has: an id, a plain label, the record it is counted from (system of record), the period, the comparison (at least, at most), the threshold, and the owner. Old task rules carried forward:

- Name the counts that matter (accounts reached, claims used, meetings held, briefings delivered) and leave out counts nobody will act on.
- Do not use revenue as the only launch-week measure when the contract cycle is longer.
- Pull counts from the system of record; never fill a missing count with an estimate.
- Separate a missed briefing from a missed customer meeting.
- Do not close a miss because the week ended.

## Metrics computed by `scripts/launch_measures.py`

| Metric | Counted as | Note |
|---|---|---|
| meetings_held | Activity rows "meeting" with outcome "held" in the period | |
| meetings_cancelled | "meeting" rows with outcome cancelled or no-show | |
| accounts_reached | Distinct accounts with a held meeting | |
| leave_behinds | "leave_behind" rows | |
| briefings_delivered | "briefing" rows held or delivered in the period | |
| roster_briefed_share | Roster people briefed by the as-of date, divided by roster size | Denominator is the person's roster |
| roster_overdue | Roster people not briefed and past the person's due date | |
| claim_uses | Claim ids recorded on activity rows | Only as good as the logging |
| unapproved_claim_uses | Claim ids used that are not on the approved list | Ties to the rules below |

State the basis of every number: which records, which period, which denominator, which as-of date.

## Where a measure touches a sourced rule

| Measure | Why it matters | Rows |
|---|---|---|
| Unapproved claim used in the field | Oral statements by representatives show intended use in the US; promotional statements are part of intended purpose in the EU; testimonials repeated by the maker count as its claims in Great Britain | PC-US-17, PC-EU-03, PC-UK-03 |
| A claim used to an audience it was not approved for | Health care economic information is for payors, not prescribers or consumers | PC-US-35 |
| Free items, codes or devices handed out, counted as an activity | Potential inducement; stops for compliance | CP-US-01, CP-US-34, CP-US-25 to CP-US-28 |
| Prescriptions or activations steered by a partner or physician deal (Germany) | Barred for DiGA prescriptions | CP-DE-06 |
| DiGA route mix (prescription or fund approval) | Two routes exist; fund approval needs proof of indication | CP-DE-01, CP-DE-02 |
| US DMHT billing by customers | Payable only where the practitioner bears the device cost and use matches the FDA classification; the seller's sales are not the customer's billed services | CP-US-59, CP-US-64 |

## Never

- Treat uptake, activations or prescriptions as clinical evidence or as proof the product works.
- Present coverage or a price as secured because sales occurred.
- Infer why a measure missed. Offer hypotheses, labeled, each with what would confirm it.
- Average measures into one score.
