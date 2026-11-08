# Tools and companion slot

## Sources for this file

- **Schema:** the VERIFY connector tool schemas as listed in a build session on
  20 October 2026 (names `build_citation`, `build_record`, `build_evidence_table`, shown
  to the host with a connector prefix). Read, not called.
- **Connector instruction:** the VERIFY connector's own usage instruction as exposed in
  the same session.
- **Earlier method:** the vital-verify `record-method` and `escalation` skills (version
  2026-10-19.2). These are a document's assertions, not a measured contract.

Anything below that goes beyond the schema text is marked `[CHECK]`. The owner will
cross-check against VERIFY before release. No tool was called while writing this skill.

## Companion slot

| Task | What VERIFY does | Tool | Without it |
|---|---|---|---|
| Build citations | Returns one formatted reference line per source | `build_citation` | Plain lines from supplied details, `scripts/plain_reference.py`; "not tool-built" |
| Build the record | Writes the record and its exports from claims, findings, sources and clearances | `build_record` | Plain record note in the `work-record` shape; "not tool-built" |
| Evidence table, on request | Renders findings as a Markdown table | `build_evidence_table` | Only if asked: a plain list of findings the tools returned; never invented statuses |

## `build_citation`

**Schema says:** "Return one citation line in formatted. Paste that line as the
reference and add no caption. style is chicago or harvard. Omit style to use the key
preference, which defaults to chicago. Free. It does not check the claim."

| Argument | Type (schema) | Required | Use |
|---|---|---|---|
| `source` | object | no | The source to cite. Pass the source object `qualify_source` returned when `source-assessment` ran. [CHECK: required fields when built from the person's own details, without `qualify_source`] |
| `record` | object | no | "A literature record, when the source is a paper." [CHECK: shape; presumably the record VERIFY returns for a DOI or PMID] |
| `passage` | string | no | The quoted passage the citation supports. [CHECK: whether it changes the line, for example a page locator] |
| `style` | `"chicago"` or `"harvard"` | no | Only when the person names one of these. Otherwise omit |

Returns: one line in a field named `formatted`. Paste it as the reference, exactly.

Connector instruction: "Call build_citation once per source and paste the formatted
line as the reference. Add no caption before it. If the user does not name a style,
omit style so the key preference applies."

Example call shape (fictional source, details as the person supplied them):

```
build_citation({
  "source": { ...the source object for source 1, as returned or supplied... }
})
```

With a named style:

```
build_citation({ "source": { ... }, "style": "harvard" })
```

Pitfalls:

- One call per source. Never one call for the whole list.
- Do not pass `style` because a style seems usual. Leaving it out is the instruction.
- No caption: not "Reference:", not "As returned by VERIFY:".
- Do not edit the returned line or add a missing year to it. A missing detail is named
  after the list. [CHECK: how VERIFY renders a missing field, for example omitted or
  marked]
- It does not check the claim. A built citation is not a supported claim.
- The connector instruction also asks for the source score total and numeric axes under
  each reference. Those values come from `qualify_source` (`source-assessment`) and are
  presented by `confidence-scoring`. This skill prints them only when that result is in
  hand, never computed or estimated. [CHECK: which skill prints them, to be settled]
- Vancouver, AMA, APA and other styles are not in the schema. Offer Chicago or Harvard
  through VERIFY, or plain lines marked "not tool-built".
- If `source-assessment` found the source inadmissible (for example the fetch failed),
  say so and do not invent the missing details. [CHECK: whether `build_citation`
  accepts a source that was not admitted]

## `build_record`

**Schema says:** "Write the record and its exports from claims, findings, and
clearances. Requires verify:write. Refuses a record whose cleared_by.name is missing or
is a tool or model name."

| Argument | Type (schema) | Required | Use |
|---|---|---|---|
| `clearances` | array of objects | yes | One per decision. Each carries `cleared_by.name` (a person's name the owner gave). [CHECK: other fields. The earlier record method lists a decision (cleared, revised, removed or escalated), the name, a role, a time and a note] |
| `claims` | array of objects | no | The claims as `claim-assessment` split them. [CHECK: shape] |
| `findings` | array of objects | no | The results `check_claim` or `verify_text` returned, unchanged. [CHECK: shape] |
| `sources` | array of objects | no | The sources as `qualify_source` returned them, including any found inadmissible. [CHECK: shape] |
| `text` | string | no | The finished text the record covers |

Example call shape (fictional; fields beyond `cleared_by.name` are `[CHECK]`):

```
build_record({
  "text": "<the finished text>",
  "claims": [ ...as returned by claim-assessment... ],
  "findings": [ ...as returned by check_claim or verify_text... ],
  "sources": [ ...as returned by qualify_source... ],
  "clearances": [
    {
      "decision": "revised",
      "cleared_by": { "name": "Priya Shah", "role": "Medical Lead" },
      "time": "<date and time the person gave>",
      "note": "Visit figure restored to the passage: 4.1 to 3.2 per patient-year."
    }
  ]
})
```

Pitfalls:

- Do not call it without a person's name in `cleared_by.name`. It refuses, and the
  attempt adds nothing. Write the uncleared draft instead.
- Never pass a tool, model, connector, assistant or team name. It refuses those, and a
  hand-made note must not carry them either.
- Do not call it while an open item has no decision. [CHECK: whether VERIFY accepts a
  record with undecided items and labels it a draft itself]
- Needs a key with write access (`verify:write`). If it is refused for access, say the
  key cannot write records and give the plain record note instead, marked "not
  tool-built".
- Pass findings exactly as the tools returned them. Never change a status to get a
  record through.
- Never invent the time. Use the date and time the person gives. [CHECK: whether VERIFY
  stamps its own time]
- What comes back is the record and its exports. [CHECK: return fields; the earlier
  method lists a clearance memo, a source register, finding cards and, on request, an
  evidence table]. Report what came back; do not describe exports that were not
  returned.

## `build_evidence_table`

**Schema says:** "Render findings as a Markdown table. Call it only when the user asks
to see the evidence table. Otherwise do not call it and do not print a table."

| Argument | Type (schema) | Required | Use |
|---|---|---|---|
| `findings` | array of objects | yes | The findings the tools returned, unchanged |

```
build_evidence_table({ "findings": [ ...as returned by check_claim or verify_text... ] })
```

Pitfalls:

- Only when the person asks to see the table. "Build the record" is not a request for
  the table.
- Do not build the same table by hand when VERIFY is connected.
- It does not change any status.

## Scripts

### `scripts/plain_reference.py`

Builds plain reference lines from the details the person supplied, for use without
VERIFY. It never fills a missing field: it leaves it out of the line and lists it.
It follows no named style and labels every line "not tool-built".

```
python scripts/plain_reference.py sources.json
python scripts/plain_reference.py sources.json --json
cat sources.json | python scripts/plain_reference.py -
```

Input: a JSON list of sources. Recognized fields: `authors` (list or string), `title`,
`container` (journal, book, website or congress), `publisher`, `year`, `volume`,
`issue`, `pages`, `doi`, `pmid`, `url`, `type`. Unknown fields are ignored and listed.

Output: one line per source, then a list of missing details per source (year, title,
authors, and container are expected for every source; volume and pages for journal
articles; a DOI, PMID or URL for every source), then the line "Reference lines built from
the details you gave; not tool-built."

Tested on 20 October 2026 on the fictional sources in
`examples/advisory-board-pre-read.md`, including a source with no year, a source with
no authors and an empty input.
