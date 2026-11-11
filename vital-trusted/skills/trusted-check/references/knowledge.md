# Knowledge: trusted-check

This file is the single home for this skill's sourced rules, failure patterns, gap
wording and failure modes. Where the same rule or pattern appeared in more than one
earlier file, one copy is kept.

## Contents

- Part 1: Rules (sourced, with scope and confirmation status)
- Part 2: Failure patterns (before and after)
- Part 3: Gap rules (shared wording, with this skill's cases)
- Part 4: Failure modes (detection questions)

## Part 1: Rules

`trusted-check` enforces no external regulation of its own. It runs the letter skills,
which carry their own sourced rules in their own `references/rules.md`, and it applies
the TRUSTED hard rules to the summary. This file says what it applies and where each
comes from (TR-H8).

Last reviewed: 20 October 2026.

### What it applies

| Id | Rule | Source | Status |
|---|---|---|---|
| C1 | Report counts and plain notes; never a verdict | TR-H3, `trusted-capability-map` | Owner decision, 20 October 2026 |
| C2 | A check that did not run is reported as not checked; no companion result is described unless the companion returned it | TR-H4 | Owner decision, 20 October 2026 |
| C3 | Work stays an uncleared draft unless the person names who cleared it | TR-H5 | Owner decision, 20 October 2026 |
| C4 | Depth follows the reader: light, short, full | TR-H12 | Owner decision, 20 October 2026 |
| C5 | Name the kind of internal process the work goes to next; never replace or name a company's SOP | TR-H11 | Owner decision, 20 October 2026 |
| C6 | Plain language for the person; codes and skill names only on request | TR-H13 | Owner decision, 20 October 2026 |
| C7 | Every summary ends with the closing statement, unchanged | TR-H10 | Owner decision, 20 October 2026 |
| C8 | Letters the person turned off are shown as "off by choice" and not run; hard rules still run | The TRUSTED standard, `trusted-capability-map/tasks/choose-letters.md` step 6 | Owner decision, 20 October 2026 |
| C9 | Prove skills run by hand at short or full depth when the person supplied sources and True is on. When True is off they do not run, unless the person asks directly; see `trusted-capability-map/SKILL.md`, "Letters that are off" | The TRUSTED standard | Owner decision, 20 October 2026; by-hand only, owner decision of 9 November 2026 |

### What the hand-check results mean

Owner decision of 9 November 2026: no live tools. Every Prove result is read by hand.

| Id | What | Source | Status |
|---|---|---|---|
| V1 | A hand-check result says how a supplied passage compares with a sentence. It is not a verdict that the sentence is true in the world | `claim-assessment/references/statuses.md` | Owner decision, 9 November 2026 |
| V2 | The six results, in these exact words: "Found in your passage"; "Partly found: <missing part> not in your passage"; "Not found in your passage"; "Your passage says something different"; "No passage to compare with"; "Opinion, recommendation or definition" | `claim-assessment/references/statuses.md` | Owner decision, 9 November 2026 |
| V3 | No percentage, ratio, score, tier or grade is given. The fixed line is "No confidence figure: these results were not tool-checked." | `confidence-scoring/SKILL.md` | Owner decision, 9 November 2026 |
| V4 | A record names a clearer only when the person named who reviewed it, with role and date. Otherwise it is an uncleared draft | `citation-and-record/governance.md` | Owner decision, 9 November 2026 |
| V5 | An evidence table is built by hand, only when the person asks | `citation-and-record/references/exports.md` | Owner decision, 9 November 2026 |

### How to use these in output

None of these ids appears in what the person reads. They explain why the summary is
written the way it is, when someone asks.

## Part 2: Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
Examples are invented for teaching; no real product or person. Pattern ids stay in this
file (TR-H13).

### Contents

- Verdicts P1–P3
- Honesty about what ran P4–P7
- Plain language P8–P9
- Scope and depth P10–P13
- Process and people P14–P16

### Verdicts

**P1 The verdict leak.** Words that read as a grade: pass, passed, compliant, approved,
validated, safe (as a judgment), accurate, correct, ethical, true (as a judgment), fine,
looks good, ready to go, good to go, ready to send, all set, fine to send, ready for
approval, all clear, green, no issues.
Why: the reader stops reading and skips the review the word cannot replace.
Before: "Safe: no issues, good to go." After: "Safe: nothing flagged in the 3 safety
statements looked at." (TR-H3)

**P2 Yes or no to "is it OK to send".**
Why: either answer is a verdict, and "no" hides what to fix.
Before: "Not yet, almost there." After: "Before it goes, fix these 4 things. Your
promotional review process decides whether it can be used." (TR-H3, TR-H5, TR-H11)

**P3 The score.** A percentage, a grade or a traffic light for the whole draft.
Why: a score for the draft is a verdict with a number on it. No percentage, ratio, score or grade appears anywhere.
Before: "TRUSTED score: 86/100." After: counts per letter. (TR-H3)

### Honesty about what ran

**P4 Zero for not checked.** A letter that could not run shown as "0 flags".
Why: the reviewer reads it as looked at and clear.
Before: "Safe: 0." (No label supplied.) After: "Safe: not checked, no label supplied
for the 2 dosing statements." (TR-H4)

**P5 The simulated tool.** Counts or a figure presented as if a tool produced them.
Why: a fabricated record of a check.
Before: "Checked with a verification tool: 3 supported." After: "Compared by hand with your
passages (not tool-checked): 3 found in your passage." Or, with no sources: "Could not be
checked: no sources were supplied; a hand check would compare the 3 figures with them."
(TR-H4, TR-H1)

**P6 Confidence as truth.** "75% accurate", "75% of the claims are true", or any
figure for how much of the draft holds up.
After: counts by hand-check result and the line "No confidence figure: these results were not tool-checked." A count of sentences found in
your passages is not proof the statements are true. (TR-H3)

**P7 The silent off.** A letter turned off simply missing from the summary.
Why: a reviewer cannot tell "not checked" from "forgot".
After: "Ethical: off by choice." (TR-H4)

### Plain language

**P8 Codes and skill names.** "R · claims-and-label: 1", "TR-H6", "pattern B1",
"[GAP: not supplied; …]" in what the person reads.
After: "Rule-compliant: 1 to fix. 'Most effective' compares with other treatments, and
nothing you supplied compares them directly." (TR-H13)

**P9 The lecture.** Paragraphs explaining each rule.
Why: daily users stop running the check.
After: one note per problem, where and what. Detail only when asked. (TR-H12, TR-H13)

### Scope and depth

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
argument. (The TRUSTED standard)

### Process and people

**P14 The invented SOP.** "Send it through SOP-PRM-004" or "your MLR committee meets on
…".
After: "your promotional review process". (TR-H11, TR-H1)

**P15 The invented clearer.** A reviewer's name added to the status line or the record.
After: "Uncleared draft." (TR-H5)

**P16 The reportability call.** "This side effect is mild and not reportable."
After: patient-safety's flag, first, in its template wording: "Before anything else:
something to pass to your safety reporting procedure ... I have not judged whether it is
related to <product>, how serious it is, or whether it needs reporting." (TR-H6, TR-H14)

## Part 3: Gap rules

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/gap-rules.md`.

Same classes as every TRUSTED skill: `[GAP: <class>; <what is missing>; <what would
close it>]`. The letter skills write gaps in this syntax inside drafts. `trusted-check`
does not edit the draft, so in the summary each gap is translated into plain words
(TR-H13). The syntax appears only in the "Detail for reviewers" view, when asked.

| Class | Where it lands in the summary | Plain wording |
|---|---|---|
| `not supplied` | The letter's row, and "Open for a person" when the person can supply it | "'9 out of 10' has no source in what you gave me. Share the study to keep it." |
| `not checkable here` | "Could not be checked" | "Whether the claims match your sources: no sources were supplied." / "Whether the safety statements match the approved label: no label was supplied." |
| `conflicting` | The letter's row, and "Open for a person" | "Your notes give 412 patients; the paper gives 408. Which is final?" |
| `needs a decision` | "Open for a person", with who decides | "Whether this tool can take unpublished data: your AI policy owner decides." |
| `out of date or unclear date` | The True row | "'Latest guidance' names no document or date." |

Wording rules:

- Name the exact item and where it is in the draft.
- Never hint at a value ("probably around 400").
- A gap is never counted as zero and never as a problem with the person.
- Each item appears once. If it is open for a person, the letter row carries the count
  and "Open for a person" carries the action.

## Part 4: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-TC-01 | Invented letter PASS | Were letters marked pass without running? | Summary | TR-H3 / TR-H4 | VERIFIED practice |
| FM-TC-02 | Wrong depth | Was Full clearance language used for a light colleague email? | Depth | TR-H12 | VERIFIED practice |
| FM-TC-03 | Hand-check results invented | Were Prove results shown when no sources were supplied, or labeled as tool-checked? | Handoff | TR-H4 | VERIFIED practice |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
