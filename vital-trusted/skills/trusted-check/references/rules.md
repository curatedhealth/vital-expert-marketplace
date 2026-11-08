# Rules behind this skill

`trusted-check` enforces no external regulation of its own. It runs the letter skills,
which carry their own sourced rules in their own `references/rules.md`, and it applies
the TRUSTED hard rules to the summary. This file says what it applies and where each
comes from (TR-H8).

Last reviewed: 20 October 2026.

## What it applies

| Id | Rule | Source | Status |
|---|---|---|---|
| C1 | Report counts and plain notes; never a verdict | TR-H3, `trusted-capability-map` | Owner decision, product concept v0.4, 20 October 2026 |
| C2 | A check that did not run is reported as not checked; no companion result is described unless the companion returned it | TR-H4 | Owner decision, 20 October 2026 |
| C3 | Work stays an uncleared draft unless the person names who cleared it | TR-H5 | Owner decision, 20 October 2026 |
| C4 | Depth follows the reader: light, short, full | TR-H12 | Owner decision, 20 October 2026 |
| C5 | Name the kind of internal process the work goes to next; never replace or name a company's SOP | TR-H11 | Owner decision, 20 October 2026 |
| C6 | Plain language for the person; codes and skill names only on request | TR-H13 | Owner decision, 20 October 2026 |
| C7 | Every summary ends with the closing statement, unchanged | TR-H10 | Owner decision, 20 October 2026 |
| C8 | Letters the person turned off are shown as "off by choice" and not run; hard rules still run | Concept §6.3, `trusted-capability-map/tasks/choose-letters.md` step 6 | Owner decision, 20 October 2026 |
| C9 | Prove skills run whenever VERIFY is connected, including when True is off | Concept §6.3 and §17 | Owner decision, 20 October 2026 |

## What it relies on from VERIFY

Read from the VERIFY connector's tool schemas and server instructions as exposed in a
session on 20 October 2026. No VERIFY tool was called. Behavior beyond the schema is
`[CHECK]` until the owner cross-checks against VERIFY.

| Id | What | Source | Status |
|---|---|---|---|
| V1 | A support status is word overlap with a supplied passage, not a verdict that the sentence is true in the world | VERIFY server instructions | Read 20 October 2026. `[CHECK]` against VERIFY documentation |
| V2 | Status names: supported, partial, unsupported, contradicted, unverifiable, out_of_scope | VERIFY server instructions | Read 20 October 2026. `[CHECK]`: the `check_claim` schema says only "returns a status" |
| V3 | Confidence (faithfulness) percent = (supported + 0.5 × partial) ÷ (supported + partial + unsupported + contradicted + unverifiable), whole percent, out_of_scope excluded | VERIFY server instructions | Read 20 October 2026. Computed by `confidence-scoring`, not here. `[CHECK]` |
| V4 | `build_record` refuses a record whose `cleared_by.name` is missing or is a tool or model name | `build_record` schema description | Read 20 October 2026 |
| V5 | `verify_text` is one counted call, at most 60 findings | `verify_text` schema description | Read 20 October 2026. Which other calls are counted: `[CHECK]` |
| V6 | `build_evidence_table` only when the person asks for the table | `build_evidence_table` schema description | Read 20 October 2026 |

## How to use these in output

None of these ids appears in what the person reads. They explain why the summary is
written the way it is, when someone asks.
