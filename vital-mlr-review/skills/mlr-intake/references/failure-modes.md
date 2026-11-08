# Failure modes — Intake

# Gap rules

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | Tool returned missing_fields | Quote them |
| field missing | No jurisdictions | Ask; do not default |
| covered but absent | Stub market | Name stub; do not substitute full pack |
| not covered | No vmlr_ | Ask by hand; label not tool-checked |

The four class names are the pack standard (aligned with Verify / Decision Companion).

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.


## Skill-specific

- FM-IN1: Silent US insertion when user said 'Europe'.

## Additional failure modes
- Silent US market inject when person listed only EU/CH markets.
- Treating CH stub ruleset as full automation coverage.
- Pasting competitor label text as if it were the product FI.
- Closing intake with status prep_complete (wrong skill).

## Cross-skill failure modes
- Borrowing another skill's good-draft paragraphs (clone detection fails the meter).
- Emitting forbidden clearance phrases in any card.
- Claiming tool-checked when keys are absent.
- Skipping the closing stamp line.
- Writing net-new ISI or label text as if sponsor-final.

### Skill-specific traps — mlr-intake
See Additional failure modes above; never collapse status to a clearance synonym.
