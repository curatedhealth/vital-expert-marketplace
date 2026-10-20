# B1 Memo and decision record

Framework task: DH-DIL.4.1, Part B, task B1. Replaces the old "Investment memo" skill, which only said not to start the catalogue job `investment-memo`; the job stays unstarted, and this task records the person's own decision instead.

## What this task delivers

A memo draft under the person's headings (or proposed headings, labeled), filled from A1 and A2 and from the person's own material, followed by a decision record: the thesis in the person's words, the criteria and scores they set, any ranking of what they scored, the decision as they state it, the decider and date, dissent, conditions and open items with owners. Public-record facts and the person's non-public facts sit in separate sections. It answers "what did we decide, on what, and what stays open?"

Why it matters: a decision read later is only as good as the trace behind it. A record that mixes a data-room revenue figure with filed facts, or carries a model's recommendation as if it were the committee's, cannot be relied on.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (diligence suite); work as a diligence analyst who assembles and records |
| Skill | DH-DIL.4.1 Part B, Memo and decision record |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/memo-sources.md` section 7 (proposed headings); `references/governance.md` |
| Tools | `analytics.mcda` only on the person's own scores; `verify.build_record` once the named person clears it |
| Prompt | This guide |
| Template | `assets/decision-record-output.md` |
| Input | The request and its context: headings, thesis, criteria, weights, scores, the decision, decider, date, attendees, dissent, conditions, open items and owners as the person states them; A1 and A2 outputs; non-public material the person supplies |
| Governance | `references/governance.md`; the person decides; the model never recommends |
| Catalogue job | `investment-memo`: design partners only, never started |

## The rule that shapes this task: people decide

The person writes the thesis, the criteria and the decision. The model checks the facts against the person's criteria where a criterion names a fact, records what the person decided, and ranks only what the person scored. It never recommends investing or passing, never gives a valuation, price, multiple or return, and never names a decider, attendee or owner the person has not named. If asked to propose headings, criteria or conditions, it may, each labeled "proposed", and applies none until the person confirms.

## Workflow

### Step 1. Headings and thesis

Write the person's headings verbatim. If none, offer `memo-sources.md` section 7 as "proposed" and ask. Write the thesis back verbatim, numbered by claim. For each thesis claim that names a public fact (for example "two FDA clearances", "randomized evidence"), set the A1 fact beside it with its source; where A1 holds no such fact, write `[GAP]`. A thesis claim about evidence quality (randomized, validated, outcomes) is set beside the library's registered-study counts and routed to dh-diligence company-and-evidence-assessment for a named-framework reading. A thesis that assumes the company operates is set beside A1's company status line; if status is "[GAP]: not read", say so beside the claim. Never judge the thesis.

### Step 2. Fill the headings

Place A1 facts and A2 flags under the headings, each with source and retrieval date or row. Place non-public material under "From you (non-public)", each fact labeled; never merge it into a public-record sentence. Vendor or press figures the person brings are labeled "from you (vendor figure)" (DL-125).

### Step 3. Criteria and scores

Write the person's criteria, weights and scores verbatim. If several options are scored (for example two targets, or invest now against a later round), call `analytics.mcda {alternatives: [{id, scores}], criteria_weights}` with the person's numbers only. Phrase criteria so 4 is best; drop an option with a missing score and list it as not ranked (register C17). Show the weights and scores beside the rank, and say the rank is arithmetic on their scores, not a decision. If one option is scored, no ranking is needed. Never call it with proposed scores.

### Step 4. Record the decision as stated

Write the decision, decider, date and attendees exactly as the person gives them. If the decision goes ahead while a criterion is unmet or a fact is `[GAP]`, write both side by side with the person's stated reason; do not judge it. Write dissent in the dissenter's words as the person gives them. Conditions (for example "subject to the HSR view of the owner the person names for legal") are the person's, in their words.

### Step 5. Open items

For each A1 gap, each A2 conclusion for the owner the person names for legal or compliance, and each unmet condition: what it is, the owner the person names (or owner not named), what it blocks by dependency, and the date the person sets to read it again (or "reread date not given"; ask). The decider is not the default owner of an open item; an item the person gave no owner for is 'owner not named'. These items feed `thesis-and-memo-monitoring` (this pack).

### Step 6. Clear the record

If the record leaves the conversation, ask who clears it and call `verify.build_record` with that person in `cleared_by.name`. The model is never the clearer (`examples/live/verify_build_record_refusal.json`).

## Build the output

Follow `assets/decision-record-output.md`. Answer first: the decision as the person stated it, the decider and date, the criteria met, unmet or not measurable (counts), and the open item that blocks most. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/memo_facts.py words ANSWER.md` (counts the body above the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Headings, thesis, criteria, scores, decision, decider, dissent and owners are the person's, and the record says so.
- No recommendation, valuation, multiple, return or market size anywhere.
- Public-record and non-public facts are in separate sections.
- Any ranking shows the person's weights and scores beside it.
- The record is labeled "decision record draft for the owner".
- Every open item carries the owner the person named for that item, or owner not named.
- `python3 scripts/memo_facts.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Watching the thesis and the memo's facts after the decision: `thesis-and-memo-monitoring` (this pack).
- Any external wording (LPs, board, target, press): stops for the owner the person names.
- Deal conclusions (HSR, CFIUS, DOJ, EU, Swiss, HIPAA, GDPR): the owner the person names for legal or compliance, or owner not named.
