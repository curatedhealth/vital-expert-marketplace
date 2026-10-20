# Output format: intervention specification (draft for the person and the owners they name)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** what the specification covers; TIDieR items filled (from what the person described first, task Step 2), N/A and open (of 10 for a specification, TM34); decision rules complete, open or blocked; the development framework (the person's, or "not given" and ask); the decisions waiting for the person.
2. **Program theory (hypothesis until tested, TM7):** components, mechanisms, context, proximal and distal outcomes, each with its source claim or [GAP] (TM6, DOI 10.1136/bmj.n2061).
3. **Decision rules:** table Rule · Decision point · Options · Tailoring variables (and the measurement evidence held) · Rule · Missing-data behavior · Claim ids · Status (complete, open, blocked) · Rows (TM77 to TM89, DOI 10.1007/s12160-016-9830-8).
4. **Dose:** tested in the source versus planned, with the difference flagged for B1.
5. **Core and adaptable (proposed):** one line each (TM11, DOI 10.1136/bmj.n2061; TM117, DOI 10.1136/bmj.i6795).
6. **Routes:** design inputs and risk to `dh-regulatory-and-quality` design-controls-and-risk-management; the rule engine to `dh-digital-therapeutic-design` (old pack, heading DH-01.06.1 Personalization Engine); any trial of the app to `dh-clinical-development` study-protocol-and-endpoint-design; device status to `dh-regulatory-and-quality` regulatory-pathway-and-classification. One line.
7. **Record:** "Intervention specification draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
8. **Calls made and script run:** list, with the spec_check counts. Follows the record line.

## Full mode

### Answer
### What is being translated, and in which development framework (the person's choice)
### Program theory
| Part | Content | Source claim or [GAP] | Rows |
|---|---|---|---|
### TIDieR description
| Item | Content | Status (filled, N/A, open) | Rows |
|---|---|---|---|
### Behavior change functions
| Component | COM-B source targeted | Intervention function | Technique named by the person (BCTTv1 abstract only) | Rows |
|---|---|---|---|---|
### Dose and regimen
### Decision rules
| Rule | Decision point | Options | Tailoring variables | Measurement evidence | Rule | Missing data | Proximal outcome | Claim ids | Status | Rows |
|---|---|---|---|---|---|---|---|---|---|---|
### User-facing text per rule (draft for the owner)
### Core components and permitted variation (proposed)
### spec_check output
### Gaps
### Decisions for the person and the owners they name
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
