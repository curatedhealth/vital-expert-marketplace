# Failure modes — Compile

# Gap rules

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | Validation errors | Quote tool errors |
| field missing | Missing chair packet | Stop; name which chair |
| covered but absent | No conflicts | Say so; still no approval |
| not covered | No vmlr_ | Structural merge only; not tool-checked |

The four class names are the pack standard (aligned with Verify / Decision Companion).

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.


## Skill-specific

- FM-CO1: Single 'all chairs approve' row.

## Additional failure modes
- Dropping open checklist items to reach prep_complete.
- Merging M/L/R into a single approve score.
- Hiding stub-ruleset warnings (catalogue status `stub`) from the board packet.

## Cross-skill failure modes
- Borrowing another skill's good-draft paragraphs (clone detection fails the meter).
- Emitting forbidden clearance phrases in any card.
- Claiming tool-checked when keys are absent.
- Skipping the closing stamp line.
- Writing net-new ISI or label text as if sponsor-final.

### Skill-specific traps — mlr-compile
See Additional failure modes above; never collapse status to a clearance synonym.
