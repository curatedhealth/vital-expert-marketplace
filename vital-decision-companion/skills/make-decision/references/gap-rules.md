# Gap rules

`[GAP]` is the marker stored in payloads and briefs. In replies to the person, say "not given yet" (or name what is missing) instead of `[GAP]`.

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | The person named an option and themselves | Store both |
| field missing | No option or no name | Ask |
| covered but absent | The tool refused an AI author | Say the choice was not stored |
| not covered | No vdec_ key | Write the sentence by hand, label not tool-checked, and do not invent a stored choice |

Do not write "false" from an empty field. The four class names are the pack standard, aligned with Verify on 19 October 2026 and used here for a coaching session.

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.
