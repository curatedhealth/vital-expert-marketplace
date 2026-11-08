# Rendered example: HQ "how was this made?" record (sourced draft)

Invented teaching case. Defensible letter: who, what, when, open items, status line,
check-line stamp. Uncleared draft; no invented reviewer.

## Deliverable returned

Short payer summary deck (five slides), still draft.

## Record note (`templates/record-note.md`, full)

How this work was made (draft, not yet reviewed)

Who asked: Market access lead (name as person gave it: [not supplied in example]).

Built from (as supplied in this conversation)
1. ORION-4 registry tables PDF, data cut-off 30 June 2026 (person uploaded).
2. Internal forecast memo, 2 September 2026 (person pasted excerpt).

Tools
1. VITAL TRUSTED assistant in this thread (no other tools named by person).
2. VERIFY not connected — no automated claim check ran.

What the AI did
1. Drafted slide bullets from the registry PDF excerpt.
2. Summarized the forecast memo excerpt into one slide.
3. Did not validate figures against a database; person should reconcile numbers.

Assumed (person stated or visible in thread)
1. Germany payer audience.
2. Registry PDF is the version the team intends to use externally — not verified here.

Open
1. Cost model for savings slide — person said "coming next week" — owner: market access.
2. Medical review — not yet done — owner: medical affairs (per person: "not scheduled").

Checks that ran
1. `sourced-claims` method pass in conversation — not tool-checked.
2. No VERIFY `verify_text` — listed as not run.

What this record is not
1. Not approval, not final, not a substitute for document control.

## Status line (`templates/status-line.md`)

```text
Status: Uncleared draft — AI-assisted summary from supplied registry PDF and forecast excerpt; no named medical or market access reviewer recorded (8 November 2026).
```

## Open items (`../../templates/gap-list.md`)

```text
Open items
1. Savings slide — cost model due next week — owner: Market access
2. Medical review — not scheduled — owner: Medical affairs

Not yet checked
- Document control reference number (company SOP)
- VERIFY formal record if person later names who cleared the work
```

## Check-line stamp (`../../templates/check-line-stamp.md`)

```text
TRUSTED / work-record: not tool-checked (offline tools) · record: full note; status: uncleared draft; open: 2 items; verify: not run
```

## Letter lines (`templates/check-line.md`, trusted-check only)

```text
Defensible · record of making: 2 sources listed, AI verbs only, VERIFY not run (not tool-checked)
Defensible · assumptions and open items: 2 open with owners (not tool-checked)
Defensible · honest status: uncleared draft, no false approval (not tool-checked)
```
