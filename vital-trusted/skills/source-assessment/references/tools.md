# Tools

No connector, no key and no live tool. A source is described by hand from what the person
supplied, and every note is labeled "not tool-checked". The steps are in `by-hand.md`.

## What no tool does here

| Job | Who does it |
|---|---|
| Open a link, fetch a page or read a PDF the person did not supply | Nobody. The person pastes or attaches the source |
| Say whether a paper is retracted, corrected or replaced | The person, using the pages named in `by-hand.md` step 6 |
| Give a tier, score or grade | Nobody. There is none |
| Say whether a sentence matches the source | `claim-assessment`, by hand |

## Script

`scripts/identify_source_id.py` says what kind of identifier a string holds (DOI, PMID,
PMCID or link) so you know what the person can look up. It reads text only and looks
nothing up. Output is labeled "manual, not tool-checked".

```
python scripts/identify_source_id.py "<text>"
```

Pitfalls: never build an identifier from a title, and never complete a partial DOI from
memory. A link alone gives no identifier to check against a retraction database.
