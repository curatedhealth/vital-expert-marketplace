# Failure modes - classify

## Legacy gap rules (migrated)

# Gap rules

A missing value is left out of the stored payload (never store `[GAP]` as a value); the connector reports it as a gap and the brief shows it as "not given yet". In replies to the person, say "not given yet" (or name what is missing).

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | A keyword matched and the tool returned a type | Read it back as a draft |
| field missing | statement is empty | Ask for the statement |
| covered but absent | The tool returned no matching type | Say the pack has no row |
| not covered | No vdec_ key | Offer the eight type names by hand and label not tool-checked |

Do not write "false" from an empty field. The four class names are the pack standard, aligned with Verify on 19 October 2026 and used here for a coaching session.

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.

## Library

| ID | Mode | Detection question |
|---|---|---|
| FM-classify-01 | Invented certainty | Did any field appear that the person did not supply? |
| FM-classify-02 | Winner language | Did the skill recommend or rank as advice? |
| FM-classify-03 | type without confirm | Is the anti-pattern 'type without confirm' present? |
| FM-classify-04 | MCP assumed | Did the skill require a key for ordinary coaching? |

Screen every package against every mode before closing the turn.
