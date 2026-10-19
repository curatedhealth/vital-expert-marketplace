# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Requirement facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A row states it. | The fact plus the row id ("pointer targets at least 24 by 24 CSS pixels, UX-STD-11"). | None. |
| Criterion not in the rows | A WCAG criterion the component needs is not quoted in the rows (for example a text-alternative criterion for an icon). | "Criterion not in this skill's sources `[GAP]`; read it in the WCAG 2.2 text." | Read the W3C text before relying on it. |
| Another system's practice | The only source is GOV.UK, NHS or USWDS practice (a status, a cadence, a version rule). | "GOV.UK practice (DSX-16), an option for you, not a requirement." | The person adopts it or not. |
| Non-normative | The only source is a W3C Understanding document. | "W3C advice, not part of the criterion (DSX-12)." | None. |
| Standard text paywalled | The point sits in IEC 62366-1 or ISO 13485 clause text. | "Clause text not in the sources `[GAP]`; only the public abstract or FDA's restatement is." | The person's licensed copy or their quality owner. |
| Moved or proposed rule | A date was moved by an interim final rule, or a rule is only proposed (HTI-5). | State the instrument and that it is interim or proposed (UX-US-11, UX-US-18, UX-US-24). | Check before relying on it outside the conversation. |
| Not checked | Whether EN 301 549 V4.1.1 is cited in the Official Journal. | "Citation status not checked `[GAP]`." | The person's regulatory or legal owner. |

## The person's facts

| Situation | How to word it |
|---|---|
| No accessibility target chosen | Lay out what each market cites (`component-requirements.md` section 1) and ask; do not pick one. |
| Device status not stated | "Device status not stated `[GAP]`." Apply section 5 of `component-requirements.md` only if the person's regulatory owner says the product is a device. |
| No current version declared | "Current version not declared"; the script uses the highest version in the inventory and says so. |
| No owner named | Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. |
| No date, version or reason for a fix | Leave it blank and ask; never pick one. |
| States not listed | Ask for the states the component supports; offer the ones the person's own screens show; never assume a state exists. |
| No scores for ranking | No ranking. Lay out facts per option and ask the person to score. |
| No rule for an indicator | Report the number; no verdict. Ask for the rule. |
| Inventory column missing | Name the column (`scripts/ds_adoption.py` header) and what cannot be counted without it. |
| Surface not shown | "Not seen"; a description is "described, not seen". Never pass a criterion on a description. |
| Test evidence described but not shown | "Described, not seen." |

## Library facts

| Situation | How to word it |
|---|---|
| No safety events returned | "No events in the library for this query; absence is not evidence of no events." |
| Guidance passage without a source URL | Do not use it. |

## Never

- Never fill a criterion, a status, a version, an owner or a date from memory.
- Never treat a missing row as "not required".
- Never treat a component's test results as evidence that a product conforms.
