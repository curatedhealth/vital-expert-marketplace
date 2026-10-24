# Gap rules

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | Prep record id | Return id + status |
| field missing | No cleared_by.name | Refuse tool call |
| covered but absent | No conflicts | Still not approved for use |
| not covered | No vmlr_ record scope | not tool-checked; do not invent id |

The four class names are the pack standard (aligned with Verify / Decision Companion).

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.
