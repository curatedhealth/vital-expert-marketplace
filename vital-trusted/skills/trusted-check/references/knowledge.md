# Knowledge: trusted-check

## Migrated rules

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

## Migrated patterns

# How a final check goes wrong

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
Examples are invented for teaching; no real product or person. Pattern ids stay in this
file (TR-H13).

## Contents

- Verdicts P1–P3
- Honesty about what ran P4–P7
- Plain language P8–P9
- Scope and depth P10–P13
- Process and people P14–P16

## Verdicts

**P1 The verdict leak.** Words that read as a grade: pass, passed, compliant, approved,
validated, safe (as a judgment), accurate, correct, ethical, true (as a judgment), fine,
looks good, good to go, ready to send, ready for approval, all clear, green, no issues.
Why: the reader stops reading and skips the review the word cannot replace.
Before: "Safe: no issues, good to go." After: "Safe: nothing flagged in the 3 safety
statements looked at." (TR-H3)

**P2 Yes or no to "is it OK to send".**
Why: either answer is a verdict, and "no" hides what to fix.
Before: "Not yet, almost there." After: "Before it goes, fix these 4 things. Your
promotional review process decides whether it can be used." (TR-H3, TR-H5, TR-H11)

**P3 The score.** A percentage, a grade or a traffic light for the whole draft.
Why: a score for the draft is a verdict with a number on it. The only percentage allowed
is VERIFY's confidence line, with its meaning stated.
Before: "TRUSTED score: 86/100." After: counts per letter. (TR-H3)

## Honesty about what ran

**P4 Zero for not checked.** A letter that could not run shown as "0 flags".
Why: the reviewer reads it as looked at and clear.
Before: "Safe: 0." (No label supplied.) After: "Safe: not checked, no label supplied
for the 2 dosing statements." (TR-H4)

**P5 The simulated VERIFY.** Supported counts or a confidence figure when VERIFY is not
connected, or when it did not return them.
Why: a fabricated record of a check.
Before: "Checked with VERIFY: 3 supported." After: "Could not be checked: VERIFY is not
connected; it would test the 3 figures against your sources." (TR-H4, TR-H1)

**P6 Confidence as truth.** "75% accurate", "75% of the claims are true".
After: "75% of the checked claims are supported by the passages you supplied. This is
support from your sources, not proof the statements are true." (TR-H3)

**P7 The silent off.** A letter turned off simply missing from the summary.
Why: a reviewer cannot tell "not checked" from "forgot".
After: "Ethical: off by choice." (TR-H4)

## Plain language

**P8 Codes and skill names.** "R · claims-and-label: 1", "TR-H6", "pattern B1",
"[GAP: not supplied — …]" in what the person reads.
After: "Rule-compliant: 1 to fix. 'Most effective' compares with other treatments, and
nothing you supplied compares them directly." (TR-H13)

**P9 The lecture.** Paragraphs explaining each rule.
Why: daily users stop running the check.
After: one note per problem, where and what. Detail only when asked. (TR-H12, TR-H13)

## Scope and depth

**P10 Full audit on a team email.** A seven-row table for a reminder to colleagues.
After: two lines and the closing statement. (TR-H12)

**P11 Light pass on external work.** A two-line summary for copy going to an agency or a
doctor because the person said "quick look".
After: full depth, with the top items first. (TR-H12)

**P12 Fixing inside the check.** The summary rewrites the draft or edits it silently.
Why: the person cannot see what changed, and the check now covers text nobody reviewed.
After: report; offer the repair as a separate step. (TR-H5)

**P13 Arguing the off letters.** "You turned off Safe, but I strongly recommend…"
Why: the person set the scope. Repeating it erodes trust.
After: "Safe: off by choice." Hard-rule items still surface as open items, once, without
argument. (Concept §11)

## Process and people

**P14 The invented SOP.** "Send it through SOP-PRM-004" or "your MLR committee meets on
…".
After: "your promotional review process". (TR-H11, TR-H1)

**P15 The invented clearer.** A reviewer's name added to the status line or the record.
After: "Draft, not yet reviewed." (TR-H5)

**P16 The reportability call.** "This side effect is mild and not reportable."
After: "The draft mentions a possible side effect (dizziness after the first dose). Pass
it to your safety reporting procedure." (TR-H6)
