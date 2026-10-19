# C Field test and Gate 2

Framework task: 2.2 Outcome Prioritization, Part C.

## What this task delivers

A recorded answer to whether the room's scores are enough to decide on: the field-test rule read against the decision, and either a proportionate field test planned (top three to five outcomes, with the people they are for), or the owner's reason for proceeding without. Then the owner's attestation of the priorities, with dissent recorded: Gate 2.

Why it matters: scores given in a room are the room's view of other people's needs. When the decision is big and hard to undo, or the room is split, or the ranking wobbles, that view should be checked with the people the outcomes are for before money moves. The owner can still proceed, but on the record (method.md O14). Gate 2 makes the priorities the owner's, not the assistant's (method.md O15).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 2.2 Outcome Prioritization, Part C |
| Workflow | The steps below |
| Knowledge | `references/method.md` (O14, O15, O16) |
| Tools | `scripts/outcome_priority_check.py` (field-test reading); no connector function exists for Gate 2 |
| Prompt | This guide |
| Template | `assets/field-test-plan.md`; "Field test" and "Gate 2" sections of the report |
| Input | The result of Part B; the decision frame |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Read the rule

A field test of the top outcomes is required when **either**:

1. The decision is hard to reverse, **and** commits money or people beyond the client's own budget cycle or across more than one function, **and** the top outcomes were scored only in the room; **or**
2. Scorers strongly disagreed (spread of 4 or more on either criterion) on a top-five outcome, **or** the first-ranked outcome changes when any one scorer is left out, whatever the decision's size.

Thresholds are the owner's (18 October 2026). Changes lower in the ranking are reported, not triggers.

Take the first two facts from the frame (*Decision Framing* asks the owner). If they are not known, ask the owner in one question (session question 4). The script reports which conditions hold and what is still to ask.

### Step 2. If the rule applies, offer the choice

One question: "The field-test rule applies because [reason]. Field-test the top five (or fewer, if the list is shorter) with [the parties], or proceed without it, with your reason?"

- **Test:** draft the plan ([assets/field-test-plan.md](../assets/field-test-plan.md)): which outcomes, which party, how many people, what is asked (the same importance and satisfaction questions, in the party's words), by when, who runs it. Scores stay "scored in the room" until the test returns; then each tested outcome is "field-verified" with who was asked, how many and when. Where field and room disagree, record it as dissent.
- **Waive:** record "Proceeding without a field test: [owner's reason], [owner], [date]." Never supply the reason.

If the rule does not apply, say so in one line with why, and continue.

### Step 3. Gate 2: ask the owner to attest

The gate is well-formed only if it shows the evidence trail, names the person, offers dissent, and records the decision with responsibility. One question to the owner, with the priorities table and the dissent in front of them: "Do you attest these priorities, with the dissent recorded, as the basis for choosing options?"

Record: "Gate 2, priorities attested by [name, role], [date]. Evidence: [scorers, field test or waiver]. Dissent: [n entries]." If the owner declines or wants changes, record that and what happens next. Gate 2 is never attested by anyone other than the decision owner, and never by you.

### Step 4. Hand over

Carry forward to the Intelligence Core stage: the attested top outcomes, the restated solutions kept as options, and one open question per top outcome: what level of AI involvement fits it (assist, augment, automate, orchestrate, redesign) is set later, by the process owner, against the outcome (method.md O16).

## Boundaries

- The connector does not check the field-test rule or take Gate 2; the conversation does, and the report records it.
- No attestation by implication ("sounds good" is not an attestation; ask once more, plainly).
- A field test is proportionate: a short check, not a research program.

## When you are unsure

If the owner is not in the conversation, deliver the report with Gate 2 "pending attestation by [owner]" and the exact question to put to them.
