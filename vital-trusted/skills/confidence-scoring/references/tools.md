# Tools and companion slot

## Companion slot

| Task | What VERIFY adds | What this skill reads | Without VERIFY |
|---|---|---|---|
| Faithfulness and source scores | A status per statement, decided against a quoted passage, and a source score per page | Statuses from `check_claim` or `verify_text` (through `claim-assessment`); `source_score` from `qualify_source` and currency from `check_currency` (through `source-assessment`) | No confidence figure. Counts from reading, labeled "not tool-checked". `[GAP: not checkable here — confidence figure — connect VERIFY]` |
| The Verify card | The open items, each tied to the passage that decided it | The same findings | No Verify card. A reading summary titled "Read, not tool-checked", no percent |

This skill never calls a VERIFY tool. Calls live in `claim-assessment`,
`source-assessment` and `citation-and-record`, so the tool contract is kept in one
place. Never simulate a result (TR-H4).

## What the schemas say (read 20 October 2026, not called)

Recorded from the VERIFY connector tool schemas. Anything beyond them is `[CHECK]`.

| Tool | Schema says | Relevant here | Beyond the schema |
|---|---|---|---|
| `check_claim` | Arguments `claim` (object, required), `passage` (object: text and locator, quoted not paraphrased), `source` (object). "Returns a status and the deciding passage." "Never judges whether the claim is true." | The status counted here | `[CHECK]` the field name holding the status and its exact values |
| `verify_text` | Arguments `text` (required), `sources`, `document_ids`. "One counted call. At most 60 findings." | Findings counted here; a text over 60 findings is split upstream, and counts from the parts are added | `[CHECK]` finding shape and status field |
| `extract_claims` | Splits text of at most 20,000 characters into claims with offsets; "never decides whether a claim is supported". | Not used | — |
| `qualify_source` | Returns "a source with a tier and a source_score"; `question` is passed "so relevance is scored". | The score total and its axes, printed under each reference | `[CHECK]` axis names and null behavior (`references/rules.md` C7) |
| `check_currency` | Reports retracted, corrected, superseded or withdrawn; "a URL alone returns notices ["not checked"]". | Whether the currency axis was filled | `[CHECK]` how the result enters `source_score` |
| `build_citation` | Returns one formatted citation line. | The reference line the score sits under | — |
| `build_record`, `build_evidence_table` | Record needs a named clearer; table only on request. | Not used here | — |

Known limit from the connector instruction: a status is word overlap with the passage,
not truth (`references/rules.md` C5).

## Script

### `scripts/faithfulness.py`

Computes the faithfulness percent and the card counts. Prints no grade, pass mark or
label. `--source` is required, so every run states where the statuses came from.

```
python scripts/faithfulness.py --source verify --supported 6 --partial 2 --unsupported 1 --unverifiable 1 --out-of-scope 3
python scripts/faithfulness.py --source verify --json-file findings.json
echo '["supported","partial","out_of_scope"]' | python scripts/faithfulness.py --source verify --json-file -
python scripts/faithfulness.py --source method --supported 4 --unsupported 1
python scripts/faithfulness.py --source verify --supported 3 --unverifiable 1 --json
```

Input: status counts, or JSON that is a list of status strings, a list of objects with a
`status` key, or an object with a `findings` list. Unknown statuses are rejected.

Output: the confidence line with the arithmetic, the six counts in plain words, the
number of open items and one default recommendation. With `--source method`, or when
the denominator is zero, it prints "No confidence figure" and the reason.

Rounding: half up (`references/rules.md` C2, `[CHECK]`).

Tests: `python3 scripts/test_faithfulness.py` (16 cases: out-of-scope exclusion,
half-up rounding, zero denominator, method-only, JSON shapes, rejected input,
recommendation order, no verdict words in output).

Pitfalls:

- Count each statement once. If `verify_text` and `check_claim` both ran on the same
  statement, use the status `claim-assessment` settled on.
- When a long text was split across several `verify_text` calls, add the counts; do not
  average the percents.
- Where the host cannot run code, do the arithmetic by hand and show it.
