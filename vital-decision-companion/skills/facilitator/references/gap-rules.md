# Gap rules

`[GAP]` is the marker stored in payloads and briefs. In replies to the person, say "not given yet" (or name what is missing) instead of `[GAP]`.

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | The person stated a choice and a name | Store both |
| field missing | The choice has no human name | Ask who decides |
| covered but absent | The tool refused an AI author | Say the choice was not stored |
| not covered | No vdec_ key | Coach by hand and label not tool-checked |

Do not write "false" from an empty field. The four class names are the pack standard, aligned with Verify on 19 October 2026 and used here for a coaching session.

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.
