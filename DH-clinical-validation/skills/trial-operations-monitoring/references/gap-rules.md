# Gap rules

A gap is information. The person needs to know why something is missing, because each reason leads to a different next step.

## The person's data

| Situation | How to word it | Next step |
|---|---|---|
| A column is missing from the export (no important-deviation flag, no arm, no expected assessments) | "Not in your export `[GAP]`: important deviations cannot be separated." | Name the system that holds it (EDC, CTMS, deviation log). |
| No target or activation date for a site | "Target not given `[GAP]`; enrolled count shown without a share." | The person gives it or leaves it. |
| A status outside active, completed, withdrawn, lost to follow-up | Counted as enrolled, not retained; the script prints the count. | Ask what the status means. |
| Numbers that cannot both be true (received larger than expected; completed after the as-of date) | Quote both and ask. Do not correct them. | The person checks the export. |

## Rules

| Situation | How to word it |
|---|---|
| No rule for a metric | "No rule set; no verdict." Show the number only. |
| The person asks for a benchmark | "No sourced benchmark in this skill `[GAP]`; the acceptable range is yours (CVB3)." |
| A disclosure rule applies to a different product type (EU CTR for a device) | "The EU CTR is the regulation on clinical trials on medicinal products (CVB7); device investigation rules are not sourced `[GAP]`." |

## Connector results

| Situation | How to word it |
|---|---|
| `find_trial` returns no dates | "The library returns status and phase but no registration or completion dates `[GAP]`; the dates used are yours." |
| `find_trial` finds no registration from a paper | "No registration linked from this paper in the library's sources." Never "unregistered". |
| No linked publication | "No publication linked to NCT... in the library's sources (DATE)." Never "unpublished". |

## Never

- Never turn a gap into "missed", "non-compliant", "failing site" or "on track".
- Never mark a field `[GAP]` from an abstract when the source is open access: read the full text first.
- Never fill a gap from memory or from a passage without a source URL.
