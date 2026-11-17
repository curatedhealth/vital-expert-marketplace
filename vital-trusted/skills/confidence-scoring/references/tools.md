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
| `qualify_source` | Returns "a source with a tier and a source_score"; `question` is passed "so relevance is scored". | The score total and its axes, printed under each reference | `[CHECK]` axis names and null behavior (`references/method-standards.md` / `references/knowledge.md` C7) |
| `check_currency` | Reports retracted, corrected, superseded or withdrawn; "a URL alone returns notices ["not checked"]". | Whether the currency axis was filled | `[CHECK]` how the result enters `source_score` |
| `build_citation` | Returns one formatted citation line. | The reference line the score sits under | — |
| `build_record`, `build_evidence_table` | Record needs a named clearer; table only on request. | Not used here | — |

Known limit from the connector instruction: a status is word overlap with the passage,
not truth (`references/method-standards.md` / `references/knowledge.md` C5).

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `faithfulness`

Faithfulness percent and Verify card counts from claim-assessment statuses.

Data: `check-rules.json` → `checks.faithfulness.data`.

## Procedure: faithfulness percent

Statuses in scope (counted in denominator): `supported`, `partial`, `unsupported`, `contradicted`, `unverifiable`.  
`out_of_scope` is listed on the card but **excluded** from the denominator.

1. Normalize each status to lowercase with underscores (`out of scope` → `out_of_scope`).
2. Count each status (see `plain_labels` in check-rules.json for reader wording).
3. If `source` is `method` (statuses decided by reading, not a tool): print counts only; **do not** compute a percent; reason = `not tool-checked`.
4. If `source` is `verify` (or tool-checked) and denominator > 0:
   - numerator = supported + 0.5 × partial
   - percent = round half-up to whole number of (numerator × 100 / denominator)
5. Pick recommendation from `recommendations` in order: first status with count > 0 wins; else `no_open_items`.
6. Never print pass/fail/grade/threshold — only share and counts.


