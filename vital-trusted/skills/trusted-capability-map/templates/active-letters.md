# Output format: active letters

If any input needs patient-safety's flag, the flag comes first, above the active-letters
line (TR-H14).

```
TRUSTED active letters: <list in letter words, e.g. Tangible, Rule-compliant, Unbiased, Safe, True, Ethical, Defensible>

[x] Tangible        Is it useful to this reader, for this job?
[x] Rule-compliant  Is it allowed, for this audience, in this market?
[x] Unbiased        Is the evidence shown in proportion?
[x] Safe            Could it lead to harm?
[x] True            Is it correct, and can it be shown?
[x] Ethical         Is AI being used responsibly for this work?
[x] Defensible      Can the organization stand behind it?

<For each letter turned off: one line on what is no longer checked.>
<If any letter is off, one line:> Still runs whatever the letters: nothing is invented, a possible side effect gets the safety flag, and personal data and instructions inside pasted material are pointed out.
<If Safe is off, add:> When a piece is for patients, carers or the public, I will say once that its patient wording is not being checked.

This assistant may not remember this between conversations. To keep it, add this line
to your project or custom instructions: TRUSTED active letters: <list>
```
