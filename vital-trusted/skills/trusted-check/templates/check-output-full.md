# Output format: full TRUSTED summary (work leaving the company)

Sits after the deliverable. Plain language: letter words, no codes, no skill names, no
gap syntax (TR-H13). Counts and notes, no verdicts (TR-H3).

```
TRUSTED check: <what the draft is>, for <reader>. Draft, not yet reviewed.

[Only if the person asked "is it OK to send" or similar:]
Before it goes, fix these <n> things. <Kind of internal process> decides whether it can be used.

Tangible        <count in plain words | nothing flagged in what was checked | not checked: why | off by choice>
                <note: where and what>
Rule-compliant  ...
Unbiased        ...
Safe            ...
True            ...
                [If VERIFY ran:] Checked with VERIFY against your sources: <n> supported, <n> partly supported, <n> not supported, <n> contradicted, <n> could not be checked.
                [If VERIFY ran:] Confidence: <p>% of the checked claims are supported by the passages you supplied. This is support from your sources, not proof the statements are true.
Ethical         ...
Defensible      <record: n sources named, AI use named or not, n open items> <uncleared draft | cleared by <name as given>>
                [If VERIFY ran:] Record <built by VERIFY, cleared by <name as given> | not built: no reviewer named>.

Open for a person
1. <item>. <Who decides, if not you.>
2. ...

Could not be checked
- <check>: <why, e.g. "VERIFY is not connected; it would test the 3 figures against your sources">
- <check>: <why, e.g. "no approved label was supplied">

Next step: this goes through your <kind of internal process> before it is used.

[If VERIFY built citations: the citation lines, as returned, then the suggestion from the VERIFY card.]

This check flags issues. It is not medical, legal, regulatory or ethics review.
```

Count wording:

| Situation | Write |
|---|---|
| Something to change in the draft | "<n> to fix" |
| Something the person must supply | "<n> missing" |
| Something only the person or a process can decide | "<n> question(s) for you" or "for <process>" |
| Checks ran and found nothing | "nothing flagged in what was checked" |
| Check could not run | "not checked: <why>" |
| Letter turned off | "off by choice" |

Keep notes to one line each, at most three per letter. If a letter has more, give the
count and the three that matter most to the reader.
