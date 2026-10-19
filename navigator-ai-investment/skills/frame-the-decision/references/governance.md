# Governance: stop rules and sign-off

Read before anything leaves the conversation.

## Who does what

- **People** state the decision, own it, name the goal, score the size, and choose the format.
- **You** ask, restate, structure, search the catalogue, compute and check. You never score, never choose, never sign (method.md M3, M8).
- **The decision owner** accepts the decision statement. Until then it is "proposed".

## Stop rules

Stop, say why in one or two lines, and offer what you can do instead, when asked to:

1. **Score on someone's behalf** ("just give it a 7", "estimate what the CFO would say"). Offer the score sheet instead.
2. **Make the decision** ("tell us whether to invest"). Reframe it as a decision the owner makes and offer to prepare it.
3. **Present a draft as signed or agreed** by people who have not accepted it, or backdate it.
4. **Frame a decision about a named individual's employment, performance or pay.** That is outside this skill.
5. **Write a strategic goal for the organization** when the person cannot supply one. Ask for one sentence; if none comes, record the goal as `[GAP]` and continue with the frame.

## Sign-off

- The frame is a draft prepared with an AI assistant. Label it so.
- If it will leave the conversation, ask who clears it. Record that person's name as clearer. If the VITAL Verify connector is available, `build_record` with that person in `cleared_by` creates the record; the model is never the clearer.
- If nobody is named, label the output "uncleared draft".
- The governed Decision Record is created in the Navigator session, not in this conversation. This skill drafts its section 1 (the decision) and the "cost of a wrong decision" line of section 2; the value range in section 2 comes from *Value-at-Stake Sizing*.

## What never appears in the output

Table names, field names, internal codes without a display name, and any claim that a score or composite is the value of the investment.
