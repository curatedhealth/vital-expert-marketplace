# Tools and companion slot

## Companion slot

No companion exists for this skill yet. Do not imitate one (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Human oversight | An AI-policy or MLR-preparation companion would read the company's review procedures and say which process this work goes through and who the reviewer role is | None yet | Ask who will read it before use; name the kind of process in plain words; check line says "asked, not checked" |
| AI use disclosure | An AI-policy companion would read the company's AI use policy and return whether and how it expects disclosure for this kind of work and audience, with the section | None yet | Ask what the policy says; offer wording for the person to approve; "asked, not checked" |
| Authorship integrity | A publications companion would read the company's publication policy and the target journal's instructions and list the authorship and acknowledgment steps | None yet | Ask for the venue and point to the publications process; "asked, not checked" |
| Equity and inclusion | A language companion would check wording against the community guides the company has adopted | None yet | `scripts/scan_language.py` where code can run, plus reading by hand; "not tool-checked" |

When the person quotes their policy, the venue's instructions or a community guide in
the conversation, use their words as supplied, with their date, and do not extend them.
That is the person's input, not a companion result.

VERIFY does not fill these slots. It checks sentences against supplied passages; it
does not read policies, venue rules or language guides. When a disclosure statement or
evidence-gap sentence states a fact from a source ("the trial included 9% of people over
75"), that sentence can go to `claim-assessment` like any other claim.

## Script

### `scripts/scan_language.py`

Lists phrases that may stigmatize, blame or define people by a condition, with the line,
context, a suggestion and the rule id the term comes from in `references/rules.md`.
Terms tagged CHECK are good practice not yet confirmed against a primary document.

```
python scripts/scan_language.py draft.txt
python scripts/scan_language.py draft.txt --json
cat draft.txt | python scripts/scan_language.py -
```

Tested with `scripts/test_scan_language.py` (seven cases: campaign copy, no double count
for "substance abuser", "suffering from", quotes marked, clean text, identity-first form
not flagged, "the disabled" flagged).

Pitfalls:

- It finds wording, not meaning. Stereotyped images, a missing group, an assumption
  about a population ("older patients struggle with apps") and an unstated evidence gap
  are not found. A clean scan does not mean the text is free of stigma; say so.
- It over-finds. Quotations, a community's own preferred terms, organization names and
  clinical terms can match. Hits inside quotation marks are marked; keep quotes exact.
- It is English only.
- Hits are phrases to look at. Report what was changed, not the raw count.
