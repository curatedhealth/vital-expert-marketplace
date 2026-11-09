# Post-clearance human ops — deferred from READY

Date locked: **8 November 2026**  
Decision: taxonomy challenge § Owner decision (A) — no Form 2253 skill in Pilot.

## How to name it (TEH-RDY-025, TEH-RDY-031)

- Name Form 2253 only when US is a market the person supplied, or the person asks about it. Then write exactly one line: `[DEFERRED] Form 2253 — out of READY scope`. It is never a finding, a rule row, a rule id or a severity.
- In every other case write "regulator submission filings are deferred" and name no form.
- A tool note that mentions Form 2253 (for example the post-clearance note) is relayed only under the same condition.

## What READY does

Prepare the board packet offline (or with optional `vmlr_` / `vvfy_`). Stamp prep statuses only. Require a named human on the prep record. Keep `mlr_reviewed: false`.

## What READY does not do

- File or draft a regulator submission filing (when US is supplied or asked about: Form 2253)
- Invent submission ids, receipt numbers, or “filed with OPDP”
- Archive the company-approved final as a regulated record system of record
- Replace company SOP countersign

## Reminder language (allowed)

> If this is US promotional material and your SOP requires Form 2253 after human MLR clearance, a named human owns that filing. READY only prepared the packet.

## When to revisit

After Pilot Cowork retest + marketplace tip, owner may authorize a **checklist-only** skill that lists filing fields without submitting. Until then: reminder rows on board cover + submission checklist only.
