# Record method examples

## Refused

The user says "save the record" and has not given a name.
Do not call `build_record`. Reply that the memo is a draft until they give the name of the person who decided.

## Cleared

The user gives the signer's name and role, and says the 62 percent claim is removed.
Call `build_record` with decision `removed`, that name in `cleared_by.name`, the role, the time, and a note that the passage did not state 62 percent.
The memo's first line is not "Draft." The evidence table is still omitted unless they asked for it.
