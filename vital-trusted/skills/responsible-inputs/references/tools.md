# Tools and companion slot

## Companion slot

No companion exists for this skill yet. Do not imitate one (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Input confidentiality | An AI-policy companion would read the company's AI use policy and approved-tool list and return, for this kind of material and this tool, the covering section, the approved alternative if any, and the policy owner | None yet | Ask the person the policy question; check line says "asked, not checked" |
| Intellectual property | The same companion, extended with the company's license register, could say whether a subscription or license covers this use and this tool | None yet | Ask the person or point to the licensing process; "asked, not checked" |

When a person quotes their policy or approved-tool list in the conversation, use their
words as supplied, with their date, and do not extend them. That is the person's input,
not a companion result.

VERIFY does not fill these slots. It checks sentences against supplied passages; it does
not read policies or licenses.

## Script

### `scripts/scan_inputs.py`

A pattern scan of a text the person wants to use, run where the host can execute code.
It looks for:

- identifier formats: email addresses, phone numbers, dates, ages over 89, URLs, IP
  addresses, long ID-like numbers and subject codes, titles followed by a name;
- confidentiality markers: "confidential", "unpublished", "draft", "internal use only",
  "not for distribution", "embargo", "topline", "clinical study report";
- copyright and license markers: copyright lines, "all rights reserved", "licensed to",
  DOIs, "reprinted with permission".

```
python scripts/scan_inputs.py extract.txt
python scripts/scan_inputs.py extract.txt --json
cat extract.txt | python scripts/scan_inputs.py -
```

Output: counts by category and, for each hit, the line number and a masked snippet. The
script never prints a full identifier.

Pitfalls:

- It finds formats, not meaning. Names without a title, rare diagnoses, a patient's
  story or a small town are not found. A clean scan does not mean the text is anonymous
  or safe to share; say so when reporting it.
- Run it on the extract the person plans to use, ideally before it goes into a cloud
  tool. Where it runs inside the assistant, the text is already in the conversation;
  the scan then only helps keep identifiers out of the output.
- It also over-finds: a press release date or a spaced number can show as a date or
  phone number. A date is an identifier only when it is linked to a person. Read the
  hits; do not report raw counts as findings.
- Markers are signals for a question, not findings. "Draft" in a public document is not
  a confidentiality finding.
