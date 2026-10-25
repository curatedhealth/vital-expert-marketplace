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

Twenty method skills (v0.3.0). Each one has tasks, references, a teaching example, an output asset, and evals: a routing harness, held-out requests, near misses, and behavioural cases. The file contract matches Verify. Scores stay on Ontology Navigator. Claim checks stay on Verify.

| Skill | Tool | Job |
|---|---|---|
| `where-to-start` | `decision_start`, `decision_status` | Open the session and walk the six stages |
| `facilitator` | `decision_run_stage` | One question, then stop |
| `frame-decision` | `decision_run_stage` | Statement, goal, decider, deadline, criteria; size on consequence × reversibility; the person sets rigor |
| `classify` | `decision_classify` | Draft the type. Wait for a yes |
| `rigor` | `decision_rigor_guide` | Read the checklist for the confirmed level |
| `widen-options` | `decision_widen_options` | Store names the person said |
| `gather-intelligence` | `decision_attach_notes`, `decision_run_stage` | Six intelligence questions, base rate, disconfirming question; completes the stage |
| `tradeoff` | `decision_tradeoff_matrix` | Worksheet. Winner stays empty |
| `premortem` | `decision_premortem` | Failure hypotheses, not advice |
| `bias` | `decision_bias_check` | Read the card. Leave it a draft |
| `record-dissent` | `decision_attach_notes` | Invite dissent; store it in the holder's words, or a named no-dissent attestation |
| `make-decision` | `decision_run_stage` | Final check, then store the option a named person chose, with reason, saying-no-to, and confidence |
| `daii` | `decision_daii_plan` | Decide, Advise, Inform, Implement |
| `implement-plan` | `decision_run_stage` | Owner, 48-hour milestone, review trigger, communication, if–then plans |
| `learning-loop` | `decision_run_stage`, `decision_attach_notes` | Expectations up front; later a retrospective with the process/outcome 2x2 |
| `decision-check` | `decision_status` | Readiness checklist by section and the weakest quality element. Never one score |
| `brief` | `decision_build_brief` | Compile. Incomplete stages stay `[GAP]` |
| `usecase-library` | `decision_usecase_card` | UC01, UC02, UC05 |
| `handoff-navigator` | `decision_handoff_navigator` | Then Navigator `decide_*` or `methods_*` |
| `handoff-verify` | `decision_handoff_verify` | Then Verify `qualify_source` and `check_claim` |

`my_usage` stays a tool with no skill. Without a `vdec_` key the method still runs and the turn is labeled not tool-checked.

Shelf status: Opening next. Durable sessions use `decision_companion_sessions` when `DC_STORE=supabase` (table applied 25 October 2026). Default local store is sqlite.

## Known connector gaps the skills compensate for (v0.1 connector)

The skills guard these until the connector fix lands: unauthored matrix ratings, AI or role-only names spelled differently from `ai`/`model`/`assistant`, stage order not enforced, `run_stage` skipping option warnings, the brief ignoring matrix, DAI-I and notes and printing raw JSON, and SIMULATED missing from the brief text. Each has a behavioural eval. See `CHANGELOG.md`.
