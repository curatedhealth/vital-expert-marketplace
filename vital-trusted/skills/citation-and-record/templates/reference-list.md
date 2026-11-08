# Output format: reference list

What the person sees. No caption before any line, no tool names, no codes (TR-H13).

## With VERIFY

```
1. <formatted line returned by build_citation for source 1, pasted exactly>
2. <formatted line returned by build_citation for source 2, pasted exactly>
3. <formatted line returned by build_citation for source 3, pasted exactly>
```

Only if needed, after the list, one plain line each:

```
<Source n> has no <year | pages | identifier> in what you gave me; I left it out. Add it from <where it would come from> if you have it.
You asked for <style>. These lines are in <Chicago | Harvard>; I can give plain lines in <style> instead, built by hand and not tool-built.
```

## Without VERIFY

```
1. <plain line from the supplied details>
2. <plain line from the supplied details>
3. <plain line from the supplied details>

<missing-detail lines, as above>

Reference lines built from the details you gave; not tool-built.
```

## Never

- A caption such as "Reference:" or "As returned by VERIFY:" before a line.
- A sentence saying the references show the claims are supported.
- A table, unless the person asked for the evidence table.
