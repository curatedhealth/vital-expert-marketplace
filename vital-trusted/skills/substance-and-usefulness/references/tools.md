# Tools and companion slot

## Companion slot

No companion exists for this skill and none is planned (product concept v0.4, §10.2:
Tangible stays method only). Usefulness is judged by reading against the reader's job;
there is nothing for a tool to verify. Do not imitate one (TR-H4).

| Task | What a companion would do, if one were ever built | Tool | Without it |
|---|---|---|---|
| Specificity | Fetch the person's own figures, owners and dates from systems they name (plan, CRM, project tracker), so a specific comes from a source rather than a question | None | Ask the person; leave gaps; check line says "not tool-checked" |
| No fluff | Nothing beyond the script below | None | Method and script run |
| So what | Read the person's plan or objectives document to know the reader's job | None | Read the context card; ask once |
| Actionability | Read the action log or tracker to find owners and dates already agreed | None | Ask; leave `needs a decision` gaps |
| Structure integrity | Read the company's standard templates, so a mandated structure is not flagged | None | Ask whether a template applies |

VERIFY does not fill these slots. It checks sentences against supplied passages; when a
new specific or "so what" is added and VERIFY is connected, it goes to
`claim-assessment` like any other sentence, through `trusted-check`.

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `scan_fluff`

Scan a draft for filler, buzzwords, throat-clearing openings, vague words,
stacked hedges and near-duplicate sentences.

Data: `check-rules.json` → `checks.scan_fluff.data`.

## Procedure: fluff scan

1. Split into sentences (line breaks; also split on `.?!` followed by space and a capital/digit/quote).
2. Buzzword / vague: match each term in `buzzwords` / `vague` as a whole phrase (case-insensitive; hyphen≈space).
3. Openers: if a sentence starts with any `openers` regex (optional leading bullet), record a throat-clearing hit.
4. Stacked hedges: if a sentence has **two or more** matches from `hedges`, record one stacked-hedges hit listing them.
5. Near-duplicates: content words = tokens `[a-z0-9]+` length>2 not in `stop_words`. For each sentence pair with ≥4 content words each, overlap = |A∩B|/|A∪B|. If overlap ≥ `near_duplicate_threshold` (default 0.6), record the pair.
6. Drop a hit whose character span sits inside a longer hit on the same sentence.
7. Output counts + hits with line numbers. Note: hits are prompts to read, not findings.


