# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13). Never
include a personal detail. Shape as in `trusted-check/references/letter-lines.md`.

```
Rule-compliant · market: <market as stated | market not stated>, <n> statements that may not be allowed there (not tool-checked)
Rule-compliant · required statements: <n> missing for this kind of material, as the person's market and process define them (not tool-checked)
Rule-compliant · personal data in the output: <n> items that could identify a patient or person (not tool-checked)
```

Each line may carry up to three short plain notes, for the summary:

```
  - <where and what, e.g. "slide 2 says FDA-approved in a deck for Germany">
  - <e.g. "job code and date of preparation left for your approval system">
  - <e.g. "patient's name, age and village left out of the email">
```

"Statements that may not be allowed there" counts wording, approvals or reporting routes
from another market and content that could reach a reader it was not meant for. It does
not count claims beyond the label; those are on the label line of `claims-and-label`.

"Missing" counts elements on the list for that market (or the person's own template)
that the draft does not carry. Placeholders left for the person count as missing until
filled.

"Items" counts details in the output after repair. When all were left out, write 0 and a
note: "  - 3 details from the notes kept out of the draft".

When the market is unknown and the work leaves the company:

```
Rule-compliant · market: not checkable — market not stated (<n> product statements affected)
Rule-compliant · required statements: not checkable — market not stated
```
