# Failure modes - gut-check

## Legacy gap rules (migrated)

# Gap rules

A missing value is left out of the stored payload (never store `[GAP]` as a value); the connector reports it as a gap and the brief shows it as "not given yet". In replies to the person, say "not given yet" (or name what is missing).

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | Reaction or lean given | Quote the person's words |
| field missing | Grid incomplete | Ask for the missing weight or rating |
| covered but absent | The person did not say how it sits with them | Say "not given yet" |
| not covered | No vdec_ key | Ask the hand version and label not tool-checked |

Do not write "false" from an empty field. The four class names are the pack standard, aligned with Verify on 19 October 2026 and used here for a coaching session.

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.

## Library

| ID | Mode | Detection question |
|---|---|---|
| FM-gutcheck-01 | Invented certainty | Did any field appear that the person did not supply? |
| FM-gutcheck-02 | Winner language | Did the skill recommend or rank as advice? |
| FM-gutcheck-03 | skip gut into choice | Is the anti-pattern 'skip gut into choice' present? |
| FM-gutcheck-04 | MCP assumed | Did the skill require a key for ordinary coaching? |

Screen every package against every mode before closing the turn.
