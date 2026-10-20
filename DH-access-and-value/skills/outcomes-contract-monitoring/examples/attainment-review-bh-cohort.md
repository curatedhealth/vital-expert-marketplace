# Worked example: attainment, completeness and review on a behavioral health cohort

Run on 19 October 2026. **The patient data is illustrative** (`bh_cohort_illustrative.csv`, 20 de-identified rows built for this test); no buyer data was available. The rules follow the ACCESS behavioral health rules in `references/attainment-rules.md`. The request sets its own rule for baselines under 10, which differs from ACCESS; both are computed. The library calls below were live. Re-run on 19 October 2026 after the review pass added the CMS Table 5 control target, PGIC and the denominator exclusions.

**Request:** "We're an ACCESS participant on the behavioral health track. Here are our first 20 aligned patients at end of period. Where do we stand, what will the withhold reconciliation pay, and is missing data hurting us? Our rule for the review: stay at least two patients above the 50 percent threshold, owner is our Clinical Operations lead. Below baseline 10 we treat the measure as not required."

**Calls made**

1. `market-access-dh.retrieve_guidance {query: "erfolgsabhängige Preisbestandteile DiGA outcome-based price component", limit: 5}` and `{query: "outcomes-based contract risk-sharing agreement digital health", limit: 5}`: no passage. The library holds no outcome-contract guidance.
2. `market-access-dh.list_schemes`: no scheme carries outcome or attainment data. Monitoring runs on the person's data.
3. `python3 scripts/attainment.py examples/bh_cohort_illustrative.csv examples/bh_rules_access_style.json`: ACCESS rules including the below-10 control target, output saved as `bh_attainment_access_style.md`.
4. `python3 scripts/attainment.py examples/bh_cohort_illustrative.csv examples/bh_rules_person_below10_dropped.json`: the requester's below-10 rule, output saved as `bh_attainment_person_rule.md`.
5. `python3 scripts/attainment.py examples/bh_cohort_illustrative.csv examples/bh_rules_population.json`: the same cohort under an illustrative population-average rule, saved as `bh_attainment_population.md`.

## A1 answer (short mode)

**Attainment.** 10 of 20 aligned patients met every required target: 50.0 percent, exactly at the 50 percent threshold. Under the ACCESS rules that gives full payment of the withheld half: payment factor 100 percent: the full Medicare portion of $144 per patient on the BH initial amount ($180 allowed, 80 percent Medicare), so the $72 withheld per patient is released in full, before the substitute-spend adjustment (not computed: no substitute-service data given) and before sequestration. **Distance to the threshold: zero patients.** One more failure puts the rate at 45 percent (9 of 20) and the factor at 90 percent ($129.60 of $144 per patient; $57.60 of the $72 withhold released).

**By measure.** PHQ-9: 10 met, 4 not met, 6 missing (5 no final value, 1 out of window). GAD-7: 13 met, 2 not met, 5 missing (4 no final value, 1 out of window).

**Your below-10 rule differs from ACCESS.** CMS sets a control target when baseline is under 10: final GAD-7 under 10 (OC "ACCESS: BH targets by baseline, Table 5"). P03, P08 and P15 meet it, so the result is 10 of 20 under either rule.

**Open items that can move the rate.** (1) PGIC: ACCESS BH counts success as submission of the end-of-period PGIC, and the file has no PGIC column; at zero margin, every success depends on it (OC "ACCESS: PGIC, submission-only measure, Table 5"). (2) P13's unalignment reason: relocation or ineligibility removes P13 from the denominator, giving 10 of 19 = 52.6 percent; self-initiated unalignment keeps P13 in (OC "ACCESS: denominator exclusions").

## A2 answer (short mode)

**Six of the ten failures are missing data, not missed targets.** Three patients were lost to follow-up, one unaligned, one had no PHQ-9 final value, and one had final values on day 430, after the day-425 window. Under the contract's rule (missing counts as failure, dropouts stay in) the rate is 50.0 percent; if missing data were excluded it would be 71.4 percent (10 of 14). That 21-point gap is what completeness is worth under this contract.

**Where data is lost.** Every patient had a baseline. Loss is between baseline and final: 4 patients left the program, 2 had incomplete or late finals. No self-report flag was supplied, so the self-report check could not run `[GAP]`.

## B1 answer (short mode)

**Verdict: missed against your review rule.** Your rule: stay at least two patients above the threshold (owner: Clinical Operations lead). Number: zero patients above (still under two if P13 leaves the denominator: 10 of 19, and one more failure gives 47.4 percent). The contract payment itself is at full on this data, subject to the PGIC submissions being confirmed.

**Stall point:** data, not outcome. Of the patients with complete data, 10 of 14 met all targets.

**Hypotheses to test first** (labeled; none is a finding):
1. Patients drop out before the end-of-period visit is scheduled. Confirm: days from last contact to loss for the four.
2. End-of-period scheduling runs late. Confirm: the distribution of final-value days against day 425.
3. PHQ-9 is skipped when GAD-7 is collected. Confirm: the one patient with GAD-7 but no PHQ-9.

**Check first:** end-of-period PGIC submissions for the ten successes, and P13's unalignment reason.

**Where the response sits:** data operations and patient follow-up, owner Clinical Operations lead. If the window or the dropout rule proves unworkable, route back to contract design (DH-03.01.1.1); for ACCESS those are CMS rules, not terms open to negotiation.

**Record:** Review draft on illustrative data. Rules and owner are the requester's. Attainment is not clinical evidence. Uncleared. AI-assisted draft.

## What this example shows

- Exactly at threshold looks like success on the payment and is a miss on a margin rule the person set.
- Under an all-or-nothing rule, completeness decides more of the result than outcomes do.
- The population-average run on the same cohort (`bh_attainment_population.md`) meets both illustrative targets because missing values drop out of the averages: PHQ-9 mean reduction 5.79 on 14 patients, GAD-7 4.07 on 15. The same data reads differently under a different rule family.
