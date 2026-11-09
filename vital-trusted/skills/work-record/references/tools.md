# Tools

No verification tool or connector is used; the helper script only scans for status words.

| Task | Method | Tool |
|---|---|---|
| Record of making | The plain record note, from `templates/record-note.md`, written by hand. The formal record at the end is `citation-and-record` | None |
| Assumptions and open items | Listed in the record note | None |
| Honest status | Status line from `templates/status-line.md`; "Uncleared draft" when no name is given | `scripts/status_words.py` where code can run |

A future review-preparation companion may fill these slots; none exists. These slots run
as method only.

## Handing over for the formal record

When the person wants the formal record, hand over to `citation-and-record`. Pass on:

- the deliverable text,
- the materials list from the record note,
- the open items,
- the named clearer, with role and date, exactly as the person gave them.

If no named clearer has been given, do not hand over for a formal record. Say plainly
that the formal record needs the name of the person who reviewed and cleared the work,
and keep the plain record note.

## Script

### `scripts/status_words.py`

Lists every status or clearance word in a text (approved, final, validated, verified,
reviewed, signed off, cleared, certified, compliant, ready to send, ready to go, good to
go, all set, fine to send, for distribution)
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
