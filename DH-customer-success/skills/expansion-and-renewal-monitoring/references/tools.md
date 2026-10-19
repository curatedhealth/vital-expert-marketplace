# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance.

This competency runs on the person's own account file. The computation is local (`scripts/renewal_metrics.py`) and needs no connector. The library adds a ranking calculator for repairs the person scored and the record. The person's account data never goes into a library call. Behavior below was observed in live calls on 19 October 2026 during the sibling build (DH-02.02.2.1), whose trimmed outputs are copied into `examples/live/`.

## analytics.mcda (counted)

- Arguments: `alternatives` (each `id` plus `scores`, a map of criterion to number) and `criteria_weights` (the person's weights, summing to 1).
- Method returned: "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)". Each `value_estimate` is the weighted sum of score over 4, times 100, with `contributions` by criterion.
- Observed (`live/mcda_renewal_actions.json`): three actions, weights 0.5, 0.25, 0.25, values 75, 68.75 and 68.75. The tie is not reported. Every criterion is treated as higher-is-better (`negative_criteria` empty; no argument to set it). No robustness view.
- Use in B1 Step 6, only on the person's scores. Name criteria so higher is better. State ties in plain words. Never fill a missing score.

## analytics.rice (counted, not measured)

- Ranks initiatives with reach, impact (0.25, 0.5, 1, 2 or 3), confidence and effort, all supplied by the person. An alternative in B1 if the person already scores that way. Read the method it returns before relying on it.

## verify.build_record (counted)

- Needs a human `cleared_by.name`; with "Claude" it refused ("build_record refuses a record without a human cleared_by.name"), `live/build_record_refusal.json`.
- Call it only when an output leaves the conversation and the person names who clears it.

## agent-pack.download_agent

- `{expert: "digital-partnerships-director"}` returned the worker, version 16 October 2026, whose bound skills include this competency's old tasks (Renewal rate definition, Cohort score, Expansion result) (`live/agent_pack.json`). Its stop rules are a source of `governance.md`. No customer success expert exists in the catalogue (`live/agent_search.json`).

## Not used here

- `commercial-dh.audit_claims` and `commercial-dh.map_money_flow`: measured in the sibling build (`live/audit_claims_*.json`, `live/map_money_flow_reset.json`); not needed to compute or review renewal figures.
- `find_job`: no renewal or customer success job exists (`{query: "renewal expansion customer success"}` returned none).
- `watch_*` tools.

## Local helper

`scripts/renewal_metrics.py` (no connector):

- `cohort ACCOUNTS.csv DEFINITIONS.json`: account renewal rate, starting value, value lost, contraction, expansion, value retained with and without expansion, losses by recorded reason, open and renewed accounts with contract ids.
- `expansion ACCOUNTS.csv DEFINITIONS.json`: offers made, signed, refused, open, acceptance, refusals with reasons, outcomes outside the person's lists.
- `horizon` is used by the sibling skill.
- Every figure prints with its formula. The script refuses to run when a definition it needs is missing and names it. Tested on 19 October 2026 on `examples/sample-data/` (runs saved beside the data).

Definitions file keys: `period_start`, `period_end`, `status_field`, `renewed_values`, `lost_values`, `open_values`, `open_in_denominator`, optional `exclude` (field to list of values), `value_before_field`, `value_after_field`, `loss_reason_field`, `currency`, `definitions_owner`; for offers `offer_field`, `offer_made_values` (default ["yes"]), `offer_outcome_field`, `signed_values`, `refused_values`, `offer_open_values`, `offer_open_in_denominator`, optional `refusal_reason_field`, `offer_period_start`, `offer_period_end`, `offer_date_field`.
