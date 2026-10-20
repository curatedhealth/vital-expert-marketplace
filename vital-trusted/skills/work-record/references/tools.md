# Tools and companion slot

## Companion slot

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Record of making | Write a formal record of the text, its sources, claims and findings, cleared by a named person, with exports | VERIFY `build_record`, through `citation-and-record` | The plain record note runs fully; it says "not a formal record" only if the person asked for one |
| Assumptions and open items | Carry open findings into the formal record | VERIFY `build_record` (`findings`), through `citation-and-record` | Open items listed in the record note |
| Honest status | Refuse a record with no human clearer | VERIFY `build_record` (`clearances`) | Status line from `assets/status-line.md`; "uncleared draft" when no name is given |

A future MLR preparation companion (concept candidate, not a commitment) could fill the
record and status slots by preparing material for the company's own review. No such
companion exists. Until it does, these slots run as method only.

## How this skill uses VERIFY

This skill never calls VERIFY. When VERIFY is connected and the person wants a formal
record, hand over to `citation-and-record`, which owns the call and its interpretation.
Pass on:

- the deliverable text,
- the materials list from the record note,
- the open items, as findings,
- the named clearer, exactly as the person gave it.

If no named clearer has been given, do not hand over for a formal record. Say plainly
that the formal record needs the name of the person who clears the work, and keep the
plain record note.

## What the schema says (read, not called)

Read from the VERIFY connector schema in this session on 20 October 2026, tool
`build_record` on the VITAL Verify connector:

- Purpose as described: "Write the record and its exports from claims, findings, and
  clearances."
- Arguments: `clearances` (array of objects, required); `claims`, `findings`, `sources`
  (arrays of objects, optional); `text` (string, optional).
- Stated behavior: requires the `verify:write` permission; refuses a record whose
  `cleared_by.name` is missing or is a tool or model name.
- Connector instructions in this session: "build_record needs a human name in
  cleared_by."

`[CHECK]` items, to be confirmed against VERIFY by the owner:

- The exact shape of a `clearances` object beyond `cleared_by.name` (role, date,
  meaning of the clearance).
- The shape of `claims`, `findings` and `sources` objects.
- What the record and its exports contain, and where they are stored.
- Whether `verify:write` is included in a standard VERIFY key.
- Whether the Digital Health Library connector's `verify_build_record` is the same tool
  with the same contract.

## Script

### `scripts/status_words.py`

Lists every status or clearance word in a text (approved, final, validated, verified,
reviewed, signed off, cleared, certified, compliant, ready to send, for distribution)
and every draft marking, with line, context and whether a capitalized name or "by" phrase
sits in the same sentence. It does not judge whether a status is true; it shows where to
ask "who, which event, when".

```
python scripts/status_words.py draft.txt
python scripts/status_words.py draft.txt --json
cat draft.txt | python scripts/status_words.py -
```

Pitfalls:

- "Approved" about a product ("approved in the EU in 2025") is a product fact, not a
  document status. The script lists it; the person reading the output decides.
- A name found near a status word is a hint, not proof that the person cleared the
  work.
- Where code cannot run, read the draft for the same words by hand.
