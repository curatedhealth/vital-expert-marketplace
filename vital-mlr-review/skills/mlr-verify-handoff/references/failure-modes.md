# Failure modes — VERIFY handoff

# Gap rules

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | VERIFY returned status | Paste into notes |
| field missing | No passage | Do not call check_claim |
| covered but absent | No claims need VERIFY | Say so; continue compile |
| not covered | No vvfy_ | not tool-checked; never invent |

The four class names are the pack standard (aligned with Verify / Decision Companion).

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.


## Skill-specific

- FM-V1: VERIFY supported without vvfy_ key.

## Additional failure modes
- Claiming tool-checked VERIFY without vvfy_.
- Treating passage overlap as MLR approval.
- Omitting "versus placebo" style qualifiers when the passage has them and the claim does not.

## Cross-skill failure modes
- Borrowing another skill's good-draft paragraphs (clone detection fails the meter).
- Emitting forbidden clearance phrases in any card.
- Claiming tool-checked when keys are absent.
- Skipping the closing stamp line.
- Writing net-new ISI or label text as if sponsor-final.

### Skill-specific traps — mlr-verify-handoff
See Additional failure modes above; never collapse status to a clearance synonym.
