# Output format: joint decision record (draft for the person)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the decision in the person's words (or "no decision"), the functions and each position, who carries it out, what it unblocks.
2. **Positions:** table Function · Agreed, disagreed or not recorded · In the person's words.
3. **Rested on:** the evidence the person named; any [PAPER] passage checked (row, DOI, passage locator).
3a. **Structure:** one line: "Modeled on the evidence-to-decision conclusions (TM112, [PAPER] DOI 10.1186/s12961-018-0320-2); a pattern, not an obligation."
4. **Implementation and look-again:** carrier (named, or "owner not named"), any follow-up another function carries (dosing instructions, labeling, a clinical claim: named, or "owner not named"), A2 items unblocked or created, change record routed to `dh-regulatory-and-quality` document-and-change-control, the date the person set to look again (or "not given").
5. **Record:** "Joint decision record draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
6. **Calls made** (after the record line): list.

## Full mode

Structured on the evidence-to-decision conclusions pattern (TM112, [PAPER] DOI 10.1186/s12961-018-0320-2); a pattern, not an obligation.

### Answer
### Decision (person's words) and date
### Functions that had to agree, and why (PL1, PL4 where it was a design review)
### Positions, including dissent
| Function | Position | In the person's words | Reported by |
|---|---|---|---|
### Independent review (who, why, or "not used"; PL2, PL66, PL67)
### What was weighed: evidence and the person's assumptions (TM113)
### Options considered
### Justification
### Conditions, core components and adaptable aspects (TM117, if relevant)
### Implementation: carrier, items unblocked, items created
### Monitoring: what is looked at again, when, by whom
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
