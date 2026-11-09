# Citing and recording by hand

This is the only path. No tool builds a citation or files a clearance. You write the lines
from details the person supplied, and every output is labeled "not tool-checked".

## Steps

1. **Collect the details the person gave** for each source: authors, title, journal or
   publisher, year, volume, pages, identifier, address. A detail that was not given stays
   out and is listed as missing. Do not fill it, correct it or look it up.
2. **Build the reference lines.** Use the style the person names. With none named, use
   plain lines in one consistent order. Where code can run, `../scripts/plain_reference.py`
   copies the supplied details into plain lines and lists what is missing. It applies no
   named style, so a named style is written by hand.
3. **Do not add an access date** the person did not give.
4. **Pair each claim with its source.** Keep only sentences whose result is "Found in your
   passage", and rewrites that were checked again. Anything else is an open item
   (`escalation-packet.md`).
5. **Write the record** from `../templates/record-note.md`, with the counts from
   `confidence-scoring` in the six hand-check words, each labeled "not tool-checked".
6. **Name the clearer only if the person did.** A record with no named person who reviewed
   it is an "Uncleared draft", even when every sentence was found in its passage. Finding
   a passage is not clearance. You never clear.
7. **Build an evidence table only when asked** (`exports.md`).

## What stays out

- No citation for a source nobody supplied.
- No "approved", "validated", "verified", "compliant", "ready to send", "ready to go",
  "good to go", "all set" or "fine to send".
- No tool, model or assistant named as the clearer.
- No count written without the manual result behind it.

## Handing on

The record goes with the work into the internal review your process names
(`../governance.md`). It does not replace that review.
