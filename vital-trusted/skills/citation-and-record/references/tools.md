# Tools

No verification tool or connector is used by this skill; the one helper script only lays
out a plain reference line. References and the record are written by hand and labeled
"not tool-checked".

| Task | Tool | Method |
|---|---|---|
| Build citations | None | Plain lines from the supplied details (`../scripts/plain_reference.py` where code can run, or by hand) |
| Build the record | None | The record note from `../templates/record-note.md`, written by hand |
| Evidence table, on request | None | Built by hand from `../../../templates/evidence-table.md` in the six hand-check words |

## `scripts/plain_reference.py`

Copies the details the person supplied into plain reference lines. It never fills a
missing field: it leaves it out of the line and lists it. It follows no named style and
adds no access date. Every set of lines ends with "Reference lines built from the details
you gave; not tool-checked."

```
python scripts/plain_reference.py sources.json
python scripts/plain_reference.py sources.json --json
cat sources.json | python scripts/plain_reference.py -
```

Input: a JSON list of sources. Recognized fields: `authors` (list or string), `title`,
`container` (journal, book, website or congress), `publisher`, `year`, `date` (a full
date as given, used where no year was given), `volume`, `issue`, `pages`, `version` or
`revision` (a label's revision or a document's version, as given), `published_online`
(the online publication date, as given; the line reads "Published online <date>."),
`doi`, `pmid`, `url`, `type`, `presenter` or `presented_by` (shown as "Presented by
<name>.", never as the author). Unknown fields are ignored and listed. A year supplied in
any of these forms is never listed as missing.

Output: one line per source, then a list of missing details per source (year, title,
authors and container are expected for every source, except that a label, fact sheet,
press release or similar company document is not asked for authors, since it has a
corporate author or none; a guideline, position or consensus statement whose issuing
society or agency is given as author, and a label or SmPC, are not asked for a journal,
publisher or website; volume and pages for journal articles; a DOI, PMID or URL for every
source except a label, SmPC, prescribing information or leaflet, which carry none), then
the fixed label line. A presenter is not an author, so a poster with only a presenter
still lists authors as missing. Read the missing list before passing it on: leave out a
note that does not apply to the source as the person described it. The source kind from `type` stays in the line
("Poster", "Fact sheet", "Label", "Press release") unless it is a journal article, web
page or book, or the venue or title already names it.
