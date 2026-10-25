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

Twenty method skills (v0.3.6). Each one has tasks, references, a teaching example, an output asset, and evals: a routing harness, held-out requests, near misses, and behavioural cases. The file contract matches Verify. Scores stay on Ontology Navigator. Claim checks stay on Verify.

| Skill | Tool | Job |
|---|---|---|
| `where-to-start` | `decision_start`, `decision_status` | Open the session and walk the six stages |
| `facilitator` | `decision_run_stage` | One question, then stop |
| `frame-decision` | `decision_run_stage` | Statement, goal, decider, deadline; size on consequence × reversibility; rigor once or via change_rigor |
| `classify` | `decision_classify` | Draft the type. Confirm so session.decision_type is set |
| `rigor` | `decision_rigor_guide` | Read the checklist for the confirmed level |
| `widen-options` | `decision_widen_options`, `decision_run_stage` | Store names and widening answers; complete the stage |
| `gather-intelligence` | `decision_attach_notes`, `decision_run_stage` | Knowns, unknowns, disconfirming question; completes the stage |
| `tradeoff` | `decision_tradeoff_matrix` | Worksheet with value + rater. Winner stays empty |
| `premortem` | `decision_premortem` | Failure hypotheses, not advice |
| `bias` | `decision_bias_check` | Read the card. Ask on unknown type |
| `record-dissent` | `decision_attach_notes` | Invite dissent; notes always; merge fields when safe |
| `make-decision` | `decision_run_stage` | Store chosen_option with confidence_pct |
| `daii` | `decision_daii_plan` | Decide, Advise, Inform, Implement |
| `implement-plan` | `decision_run_stage` | Owner, milestone, review, if–then plans |
| `learning-loop` | `decision_run_stage`, `decision_attach_notes` | success_signal only; retro via merge fields |
| `decision-check` | `decision_status` | Readiness from required_stages_unmet / daii_valid / options cross-check |
| `brief` | `decision_build_brief` | Compile. None/null/{} → [GAP]. Keep SIMULATED |
| `usecase-library` | `decision_usecase_card` | UC01, UC02, UC05 |
| `handoff-navigator` | `decision_handoff_navigator` | Prefer mcda_rank_args[]; else cells + scale_note |
| `handoff-verify` | `decision_handoff_verify` | claims[]; qualify_source then check_claim |

`my_usage` stays a tool with no skill. Without a `vdec_` key the method still runs and the turn is labeled not tool-checked.

Shelf status: Opening next. Durable sessions use `decision_companion_sessions` when `DC_STORE=supabase`. Default local store is sqlite.

## Connector compatibility (v0.2 / v0.3)

| Skill | On connector v0.2 | On connector v0.3 |
|---|---|---|
| tradeoff | value + rater; scale → keep 1–5 if host lacks scale | value + rater; send scale when not 1–5 |
| frame-decision | statement, goal, decider, deadline; rigor once | same; change_rigor when rigor already set |
| make-decision | confidence_pct; handle stage_order / unknown_option | same |
| record-dissent | notes only (replace would wipe choice) | notes + dissent[] / no_dissent_attested_by without replace |
| learning-loop | success_signal only (no expected_outcome) | same + retro merge fields |
| widen-options | status cross-check; run_stage once if flag stale | widening answer fields on run_stage |
| classify | owner note if confirm unavailable; bias unfiltered | confirmed/confirmed_by or decision_type + type_confirmed_by |
| handoff-navigator | build from handoff.cells + scale_note | prefer handoff.mcda_rank_args[] |
| handoff-verify | claim strings | claims[] objects |
| decision-check | cross-check options vs widen flag | required_stages_unmet, daii_valid, brief marks |
| bias | ask on unknown_decision_type | prefer stages[] / contested from pack |

See each skill's `references/tools.md` Connector version block.
