# Gap rules

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | Ruleset medical item fails | Write finding with source_ref |
| field missing | No authorized-use text | [GAP]; do not invent PI/SmPC/FI |
| covered but absent | No medical issue | decision approve means not blocking handoff |
| not covered | No vmlr_ | Chair by hand; not tool-checked |

The four class names are the pack standard (aligned with Verify / Decision Companion).

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.
