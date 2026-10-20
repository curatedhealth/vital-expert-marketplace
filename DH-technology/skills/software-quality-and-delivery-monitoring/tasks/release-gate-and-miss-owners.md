# B1 Release gate and miss owners

Framework task: DH-04.03.4.2 with DH-04.03.2.2, DH-04.03.3.2 and DH-01.06.4.2, Part B, task B1. Carries the old tasks "DH-04.03.4.2.3 Release gate for the class", "DH-04.03.2.2.3 Open validation miss", "DH-04.03.3.2.3 Pipeline change owner", "DH-01.06.4.2.2 DTx architecture pass rule" and "DH-01.06.4.2.3 DTx architecture miss owner" as steps.

## What this task delivers

For a release candidate or a review period: the person's pass rules written back verbatim, each unit read against its rule from A1 and A2, every failed element with whether it blocks release, the owner the person names, the recheck date they set or "stopped", and the gate record with the build id and the named acceptor. Then the decisions the review surfaces, all left to the person. It answers "by our own rules, what failed, who owns each miss, and what must we decide before this build ships?"

Why it matters: the old tasks were explicit that a unit is not scored before its rule exists, that a miss is never closed by editing the expected result after the run, that a release is not shipped on an informal chat approval, and that a failed element is not closed because an earlier assessment described it. A review that assigns owners the team never named, or calls a release go, says more than the data does.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-04.03.4.2.3, DH-04.03.2.2.3); `digital-health-product-manager` (old DH-04.03.3.2.3); `ai-ml-governance-director` (old DH-01.06.4.2.2, DH-01.06.4.2.3). Work as a release quality analyst who checks against the person's rules |
| Skill | DH-04.03.4.2 Part B, Release gate and miss owners |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/monitoring-rules.md` section 6; `references/governance.md` |
| Tools | None beyond A1 and A2. `scripts/delivery_check.py misses`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/release-gate-and-miss-owners-output.md` |
| Input | The request and its context: A1 and A2 outputs or the person's files, the miss log (CSV columns in `scripts/delivery_check.py`), the pass rules, owners, recheck dates, the candidate build id and read date |
| Governance | `references/governance.md`; the person judges and decides |
| Catalogue job | none known (needs a live check) |

## Read the request

- **Candidate and read date.** Both needed. If either is missing, ask; write "not given" and never use today's date.
- **Rules.** The person's pass rules, verbatim. Without them, report facts and mark nothing pass or fail.
- **"Can it pass our gate?"** Answered with counts against the person's rules and the decisions open, never with go or no-go.
- **Short or full.** A direct question is short mode. "Full gate review" is full mode.

## The rule that shapes this task: people judge

The person writes the rules, names the owners, sets the recheck dates and decides go or no-go. The model reads the data against the rules and writes down the result. It never gives an overall verdict, never calls a release go, never names an owner the person has not named, never sets a threshold and never closes a failed element. Where a rule's words allow two readings on the data, it shows both and writes "your call".

## Workflow

### Step 1. Confirm the pass rules (old "DTx architecture pass rule")

Write each rule back verbatim, numbered: the elements that count (for architecture: component, interface, failure mode), pass or fail per element, and the element that blocks release if it fails. A unit without a rule: "pass rule not given `[GAP]`" (G1); report its facts but mark nothing pass or fail (old rule: do not score a unit before its rule exists).

### Step 2. Read each unit against its rule

Run `python3 scripts/delivery_check.py misses --file M.csv --as-of DATE`, or carry the A1 and A2 flags into the person's rules. Check that the evidence measures what the rule says: a case on another build is "not the candidate build" (T3), a quota is "not a load test" (K1); say so.

### Step 3. Open validation misses (old 2.2.3)

For each failed validation element: does it block release (the person's statement; G6 when not given); if not, who accepted it and what the user is told; if it does, the owner of the fix. Old rule: never close a miss by editing the expected result after the run.

### Step 4. Pipeline stage owners (old 3.2.3)

For a stage that fails or is skipped: the owner the person names (old rule: not "the whole platform team"), the change they set (restore a test, stop an unrecorded skip), and the next release that should show it.

### Step 5. Owners and recheck dates for each failed element (old "DTx architecture miss owner")

For each failed element: the owner the person named (or "owner not named", G2; ask), the recheck date they set (or "not given", G3; ask), or "stopped". A recheck date earlier than the read date is stated as a fact (G5), never as urgency. A closed element without evidence is flagged (G4). A failed element stays open until the person closes it with evidence.

### Step 6. The gate record (old 4.2.3) and the decisions

The gate record holds: build id (G7 when missing), each blocking element and its state, the named acceptor for any documentation gap the person accepts, and the decision. The old task's rules are written as the person's choices to confirm, not applied by the model: block when a required plan is missing or a hazardous problem is open; allow only with a named acceptor when the gap is documentation rather than an open hazard; record against the build id; no informal chat approval. List the decisions the review surfaces, each with its facts: go or no-go, accept or fix each non-blocking miss, reset a rule (with the date the new rule is written), stop a unit. Propose nothing unless asked; label any proposal "proposed".

## Build the output

Follow `assets/release-gate-and-miss-owners-output.md`. Answer first: counts of units whose rule is passed, failed and not readable, the blocking failures by name, how many failures have an owner and a recheck date, and the flag that most limits the review. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/delivery_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Rules, owners, recheck dates, acceptors and the decision are the person's, and the record says so.
- No overall verdict; no go or no-go; no failed element closed by the model.
- Units without a rule are not marked pass or fail.
- The review is labeled "release gate review draft for the owner".
- `python3 scripts/delivery_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- What a change re-opens and the regulatory questions: `medical-software-lifecycle-and-delivery` (this pack), task B1.
- CAPA for repeated misses: `dh-regulatory-and-quality` audit-capa-and-complaints.
- Any wording for FDA, a notified body or customers: stops for the owner the person names.
