# Worked example: B1 support check (live connector calls, 19 October 2026)

Request (illustrative person): "We sell a cleared insomnia therapy app in the US. Some patients have no compatible phone. We are choosing between three options and have scored them: lend a tablet to patients who are need-tested, for up to 12 weeks; give every enrollee a free data plan; or give no device support and point to a list of clinics that lend devices. Our compliance lead is Dana. Rank our scores and tell us what Dana will look at."

The scores, weights and owner are the example person's. The scores were typed for the measurement call and are presented here as theirs.

## Calls made

1. `analytics.mcda` with the three options and weights patient access gained 0.5, inducement exposure avoided 0.3, operating effort avoided 0.2 (saved: `live/mcda_support_options.json`).
2. `scripts/mcda_swap.py live/mcda_support_options.json` (local; output `live/mcda_swap_output.md`).
3. `verify.build_record` was not called: no clearer named for an output leaving the conversation. The refusal test is in `live/build_record_refusal.json`.

## Answer (short mode)

**Answer.** All three options stop for Dana before launch: a tablet and a data plan are things of value to patients (OIG treated even a limited loaner phone as remuneration, CP-US-40). The free data plan is in tension with two sourced elements; the need-tested loan follows the pattern OIG weighed in AO 19-02, which binds only its requestor (CP-US-43). By your scores, the free data plan ranks first (72.5), the loan second (70.0), no device support third (62.5). The order of the top two is fragile: at a weight of 0.44 on patient access gained (yours is 0.50), or 0.33 on inducement exposure avoided (yours is 0.30), they swap.

**Elements Dana will weigh (as you state them).**

| Item | Element | As you state it | Row |
|---|---|---|---|
| Free data plan, all enrollees | No cash or cash equivalent (hh-3) | Not stated whether a data plan counts; for Dana | CP-US-26 |
| Free data plan, all enrollees | Recommended by the patient's licensed professional (hh-4) | Not stated `[GAP]` | CP-US-26 |
| Free data plan, all enrollees | Relieves a patient of a phone contract cost | In tension with the safeguard OIG named | CP-US-41 |
| Tablet loan, need-tested | Need test, limited function, two 12-week periods at most in AO 19-02 | Need test and 12 weeks as you state; function limits not stated `[GAP]` | CP-US-39, CP-US-41 |
| Both | Annual value per patient within the 2026 figure of $623 (hh-5) | Value not stated `[GAP]` | CP-US-27 |
| Both | Not used for recruitment or marketing; not by insurance type (hh-6, hh-7) | Not stated `[GAP]` | CP-US-28 |
| Both | Company is a VBE participant; device maker only if the tool is digital health technology and no Open Payments ownership report (hh-1, hh-2) | For Dana `[GAP]` | CP-US-25, CP-US-28 |

**Stop.** Support to patients stops for Dana. This draft does not say any option is protected; a value under the cap is one element, never protection on its own.

**Record.** Support check draft. Scores, weights and the decision are yours. Uncleared.

Full version available on request (launch rules, beneficiary CMP exceptions CP-US-36 to CP-US-38, and the full swap table).

## What the run showed about the connector

- `analytics.mcda` returned values that the script reproduced exactly ("values match analytics.mcda").
- No robustness view came back (register C17); the swap weights above come from the script.
- `negative_criteria` was empty and cannot be set; criteria were named so that higher is better.
