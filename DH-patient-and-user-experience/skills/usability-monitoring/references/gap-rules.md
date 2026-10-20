# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Requirement facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it. | The fact plus the row id ("FDA treats professionals and lay users as distinct populations, UX-US-36"). | None. |
| Guidance, not law | The row is FDA or MHRA guidance. | Add "recommended, not required" where it matters (UX-US-26, UX-UK-14). | None. |
| Proposed, not final | HTI-5 proposals (UX-US-24, UX-US-60, UX-US-63). | "In force on 19 October 2026; proposed for removal, not final." | Check the Federal Register before relying on it outside the conversation. |
| Paywalled text | IEC 62366-1, ISO 14971 clause text. | "Clause text not in the sources `[GAP]`." | The person's licensed copy. |
| Summarizer read | A row marked [WF] (DCB0160, DTAC). | "Read through a summarizer [WF]; check the page before quoting." | Check the source page. |
| Not researched | Pass thresholds, SUS adjective bands, SAFER Guide practice text, DCB0160 clauses. | "Not in this skill's sources `[GAP]`." | Ask the person or the regulatory pack. |
| Restated, not read | Faulkner 2003 and Sauro and Lewis, known only as FDA or Hyzy restate them (UX-M-01, UX-M-08). | "As restated by FDA (or Hyzy et al. 2022); original not read." | None. |

## The person's facts

| Situation | How to word it |
|---|---|
| Test kind not stated | Ask formative or validation. Without it, validation conditions are listed as questions, not checked. |
| Severity not assigned in the log | "Severity not assigned `[GAP]`" per row (the script flags them); no row is treated as minor. |
| No rule for a task | Factual summary, no verdict. |
| Build version not named | "Build not named `[GAP]`"; no control is marked present. |
| Control evidence described, not seen | "Described, not seen." |
| No owner named | Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. |
| No scores for B1 | No ranking. Lay out repair options and ask the person to score. |

## Library facts

| Situation | How to word it |
|---|---|
| No safety events returned | "No events in the library for this query; absence is not evidence of no events." |
| Event without a record link (US) | "openFDA enforcement report, record not linked." |
| Jurisdiction not loaded (EU, CH) | "The library holds no field events for this market." |
| Guidance passage without a source URL | Do not use it. |

## Never

- Never fill a definition, a severity, a threshold, a class or a score from memory.
- Never treat a missing row as "not required".
