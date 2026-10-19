# B1 Change decision record

Framework task: DH-03.02.2.1, Part B, task B1. Replaces the earlier "Change record" section and its approver rule.

## What this task delivers

A change decision record, drafted by the model and decided by the person: the change, the frameworks applied, every question with its answer and source (from A2), the decision the owner states, the owner's rationale in their words, the evidence it rests on, the approver and the date, and what happens next (documentation only, submission, notified body notification, field action). It answers "write up what we decided about this change, so it stands up at inspection."

Why it matters: FDA's 2017 guidance asks manufacturers either to submit or to "document the basis for concluding that submission of a new 510(k) is not required" (QX14), and those records must be available to an investigator (QX20). MDCG 2020-3 asks for the justification to be documented and available to the competent authority (QX22). A record without its basis is the gap an inspector finds.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (`quality-assurance-manager-software`) |
| Skill | DH-03.02.2.1 Part B, Change decision record |
| Workflow | The steps below |
| Knowledge | A2's question sheet; `references/change-significance.md`; `references/document-and-record-control.md` (records, retention) |
| Tools | `verify.build_record` at clearance only |
| Prompt | This guide |
| Template | `assets/change-decision-record-output.md` |
| Input | A2 output; the owner's decision and rationale; the approver; evidence references (risk file, V&V reports) |
| Governance | `references/governance.md`; the decision and the approval are the person's |

## Read the request

- **Which change.** One change id; if the request bundles several, one record each, or one record that lists them and the aggregate view (QX12).
- **What exists.** An A2 sheet, a decision already taken, an approver already named. Take them from the conversation; ask only for what is missing.
- **Where it goes.** Into the person's QMS, a change board, or an inspection file. Anything leaving the conversation needs a named clearer.

## The rule that shapes this task: the owner decides

The model drafts every section except the decision line and the approval. Those are written from the person's own words. If the person has not stated a decision, the record stays a draft with "Decision: not yet stated by the owner". If no owner is named, write "owner not named" and ask; never suggest a job title.

## Workflow

### Step 1. Check A2 is complete enough

Use the A2 sheet from the conversation; if none exists, run A2 first in short mode. List the open questions. A record with open questions can still be drafted, but the open questions appear in it and the decision line says the owner decided with them open, if that is what the owner says.

### Step 2. Ask for the decision in the owner's words

Ask: what did you decide, who decided, on what date, and why. Offer the choices the sources name, without recommending: document the change only; submit a new 510(k) (or other FDA submission); implement under the authorized PCCP; inform the notified body of a planned change (Annex IX 4.10); treat as a correction or removal or FSCA. Record the answer verbatim.

### Step 3. Check the decision against the sheet

Do not judge the decision. Do point out, factually, where the decision and the sheet's answers sit apart, citing the row. Example: "Q4 was answered yes; the guidance says a new 510(k) is likely required on that answer (CH16). The record states 'document only'. The rationale should address Q4." The owner then adds rationale or changes the decision.

### Step 4. Draft the record

Fill `assets/change-decision-record-output.md`: identification, change, baseline, frameworks, question table (from A2), decision (owner's words), rationale (owner's words, with evidence ids), consequences checked (risk file update QS22, V&V reopen rule QX15, field action rules VG22 to VG24, retention per `document-and-record-control.md`), approval, and the AI-assisted draft label.

### Step 5. Stop for the owner

Present the draft. Say what the owner must do: confirm the decision line, sign through their own QMS, and, if the decision is a submission or notification, hand it to whoever prepares it. The model does not sign, does not fill the approver field with anything but the name the person gives, and does not date the approval.

### Step 6. Clear the record if it leaves the conversation

If the record goes into the QMS or to anyone else, ask who clears it and call `verify.build_record` with `cleared_by.name` set to that person, the record text, and the sources cited. The tool refuses a model or tool name. Without a name, label it "uncleared draft".

## Build the output

Follow `assets/change-decision-record-output.md`. Short mode for "write it up quickly": decision line, one-paragraph rationale, open questions, approver, record status. 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- The decision line and rationale are the owner's words, or the record says no decision was stated.
- Every point where the decision and the sheet sit apart is listed with its row.
- No approval, signature or date is filled in by the model.
- Submissions, notifications and field actions are marked as stops for the owner.
- The record is labeled AI-assisted draft; cleared by a named person or uncleared.

## Boundaries

- Records the decision; does not make it.
- Does not backdate, alter or reconstruct a past approval. A late record is dated today and says so.
- Does not write regulator-facing text; a draft for the owner, labeled so, at most.
