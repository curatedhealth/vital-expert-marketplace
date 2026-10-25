# Decision Companion

One plugin, three connectors. Coaching is new. Scores and claim checks are not.

| Server | Key | Tools this plugin calls |
|---|---|---|
| `vital-decision-companion` | `vdec_` | `decision_*` session, worksheets, brief |
| `vital-ontology-navigator` | `vont_` optional | `decide_*`, `methods_*` (ODI, MCDA, scenario, tornado, capability gap) |
| `vital-verify` | `vvfy_` optional | `qualify_source`, `check_claim` |

`methods_mcda_rank` stays on Navigator. This pack does not ship a second MCDA.

Literature, trials, labels, and commercial reads stay on their own connectors (`medical-affairs`, `literature`, `commercial`, and the rest). `decision_status.leverage` names them. This plugin does not copy their clients.

## Skills

Sixteen method skills. Each one has a task, references, a teaching example, an output asset, and a routing eval. The file contract matches Verify. Scores stay on Ontology Navigator. Claim checks stay on Verify.

| Skill | Tool | Job |
|---|---|---|
| `where-to-start` | `decision_start`, `decision_status` | Open the session and walk the six stages |
| `facilitator` | `decision_run_stage` | One question, then stop |
| `classify` | `decision_classify` | Draft the type. Wait for a yes |
| `rigor` | `decision_rigor_guide` | Read the checklist for the confirmed level |
| `widen-options` | `decision_widen_options` | Store names the person said |
| `gather-intelligence` | `decision_attach_notes` | Knowns and unknowns. No invented facts |
| `tradeoff` | `decision_tradeoff_matrix` | Worksheet. Winner stays empty |
| `premortem` | `decision_premortem` | Failure hypotheses, not advice |
| `bias` | `decision_bias_check` | Read the card. Leave it a draft |
| `make-decision` | `decision_run_stage` | Store the option a named person chose |
| `daii` | `decision_daii_plan` | Decide, Advise, Inform, Implement |
| `learning-loop` | `decision_run_stage` | Review date and success signal |
| `brief` | `decision_build_brief` | Compile. Incomplete stages stay `[GAP]` |
| `usecase-library` | `decision_usecase_card` | UC01, UC02, UC05 |
| `handoff-navigator` | `decision_handoff_navigator` | Then Navigator `decide_*` or `methods_*` |
| `handoff-verify` | `decision_handoff_verify` | Then Verify `qualify_source` and `check_claim` |

`my_usage` stays a tool with no skill. Without a `vdec_` key the method still runs and the turn is labeled not tool-checked.

Shelf status: Opening next. Sessions in this build are process memory until `decision_companion_sessions` is applied.
