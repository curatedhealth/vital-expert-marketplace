Input:    judged rows, failure-mode screen
Atom:     compose-draft (structure = templates/evidence-register.md)
Tool:     python3 scripts/validate_register.py register.json --pretty
Template: templates/evidence-register.md
Output:   evidence register (markdown + register.json), one-page summary leading with the three most consequential gaps
Check:    script exit 0; zero unresolved triggered modes; reviewer named. Rule: the script output is attached unmodified; a failing run is fixed in the input, never by editing the output
Human:    the named clinical development reviewer signs the register
