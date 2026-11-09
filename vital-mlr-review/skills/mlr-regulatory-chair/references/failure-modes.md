# Failure modes — Regulatory chair

# Gap rules

Classify every miss before you write it. Never turn an absent field into a fact.

| Class | Meaning here | How to word it |
|---|---|---|
| found | Format/process fail | Finding with source_ref |
| field missing | Channel unknown | Ask; format depends on channel |
| covered but absent | No regulatory issue | approve = not blocking handoff |
| not covered | No vmlr_ | Not tool-checked |

The four class names are the pack standard (aligned with Verify / Decision Companion).

- found: quote the tool field.
- field missing: name the field and leave it empty.
- covered but absent: the tool ran and the value is intentionally empty. Say so.
- not covered: the connector or the key is missing. Label the turn not tool-checked.


## Skill-specific

- FM-R1: Regulatory chair signing clinical efficacy.

## Additional failure modes
- Soft-pedaling pre-approval trade-name efficacy charts.
- Simulating Form 2253 submission while deferred.
- Writing Form 2253 as a finding or rule row, or minting a rule id that is not in a loaded ruleset (TEH-RDY-025).
- Composing a claim span that is not a verbatim quote of person-supplied text (TEH-RDY-026).
- Gating a correctable wording or format finding only because its rule row is fail-close (TEH-RDY-027).
- Treating compile schema-OK as regulatory clearance.

## Cross-skill failure modes
- Borrowing another skill's good-draft paragraphs (clone detection fails the meter).
- Emitting forbidden clearance phrases in any card.
- Claiming tool-checked when keys are absent.
- Skipping the closing stamp line.
- Writing net-new ISI or label text as if sponsor-final.

### Skill-specific traps — mlr-regulatory-chair
See Additional failure modes above; never collapse status to a clearance synonym.
