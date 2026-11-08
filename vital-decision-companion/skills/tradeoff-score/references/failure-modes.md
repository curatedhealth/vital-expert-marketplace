# Failure modes - tradeoff

## Legacy gap rules (migrated)

# Gap rules

A missing value is left out of the stored payload (never store `[GAP]` as a value); the connector reports it as a gap and the brief shows it as "not given yet". In replies to the person, say "not given yet" (or name what is missing).

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | The tool stored ratings and returned winner null | Say so |
| field missing | Criteria or ratings are missing | Ask |
| covered but absent | No cell supports a rank | Leave winner null |
| not covered | No `vdec_` key, so `decision_score` is unavailable | Say nothing has been added up; the person weighs the grid |

Do not write "false" from an empty field. The four class names are the pack standard, aligned with Verify on 19 October 2026 and used here for a coaching session.

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.

## Library

| ID | Mode | Detection question |
|---|---|---|
| FM-tradeoff-01 | Invented certainty | Did any field appear that the person did not supply? |
| FM-tradeoff-02 | Winner language | Did the skill recommend or rank as advice? |
| FM-tradeoff-03 | invented winner | Is the anti-pattern 'invented winner' present? |
| FM-tradeoff-04 | MCP assumed | Did the skill require a key for ordinary coaching? |

Screen every package against every mode before closing the turn.
