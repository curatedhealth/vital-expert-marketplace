# Output format: context card

The card is what other TRUSTED skills read before drafting or checking. It stays in the
conversation and is updated when an answer arrives. Every line says where it came from:
`stated`, `read`, `assumed`, `asked` or `unknown`. Plain words throughout, so it can be
shown to the person without translation (TR-H13).

## Card (for other skills)

```
TRUSTED context: <the deliverable, in a few words>

Reader          <who will read it>                                 (<source>)
Market          <country or region | not needed for this work>     (<source>)
Language        <language of the deliverable, and of the source if different | not needed>  (<source>)
Product status  <the person's own words, e.g. "launched, as you said" | approved here per your label | approved elsewhere only | investigational | device, class <x> as you said | not about a product | unknown>  (<source>)
Use             <internal only | scientific exchange | promotional | not about a product | unclear>  (<source>)
Deliverable     <format, rough length>                             (<source>)
Material        <one line per item supplied | none yet>
Not seen        <each item the work relies on that was not supplied, e.g. "label: not seen", "sources: not seen" | nothing the work relies on is missing>
Stakes          <internal and quick | leadership | leaving the company>
Next process    <kind of internal process in plain words | none apparent>
Inputs          <kinds: public, internal, confidential company, unpublished study data, client or partner, personal, patient or health | none described>
AI use policy   <person states it allows this | person states it does not | person not sure | no policy, as stated | not asked (no sensitive input)>
Tool decision   not made here; it belongs to the person and their AI policy owner

Assumed         <one line per assumption, as the person saw it>
Asked           <one line per open question>
```

Rules for the card:

- `Tool decision` is always the fixed line above. It never changes.
- A policy line only ever starts with "person states", "person not sure", "no policy, as
  stated" or "not asked". Never "approved" or "allowed".
- `Product status` cites its source: "per your label" when a label was supplied, "as you
  said" when stated. Never from memory. Echo the person's own status word (TR-H7):
  "launched, as you said" stays "launched", never "approved", and "launched" is not
  read as approved in any market.
- `Not seen` is always on the card. When the work makes product statements and no label
  was supplied, it reads "label: not seen", even when the person said the product is
  approved or launched.
- `Unknown` fields are left unknown. Other skills treat them with the careful defaults in
  `governance.md`.

## Person view (leadership stakes and above)

Shown once, at the top of the first reply after intake, only when something is missing,
assumed or not seen: one short line per field that matters for this work, each ending with where it came from in plain words ("as you
said", "from your <material>", "my assumption", "not given", "not seen"). Not shown for
internal and quick work, where one line of assumption is enough.

```
Working from:
- Reader: <reader> (<as you said | from your <material> | my assumption>)
- Market: <market, in the person's words | not given> (<as you said, not confirmed | not given>)
- Product status: <the person's own words, e.g. "launched"> (as you said; label not seen)
- Use: <use> (<as you said | my assumption>)
- Material: <what was supplied | nothing yet>
- Not seen: <label | sources | ...>
<If an internal process applies:> It goes through your <kind of process> before it's used.
```

Leave out a line that does not matter for this work (no product status line for an
update that makes no product claims). Never upgrade what the person said: "Austria or
Switzerland" stays both, "launched" stays "launched".

## One-line form (internal and quick, or nothing missing)

When the request gives every field that matters, the "Working from" line is this one
line, at any stakes, and no question is asked. Language follows the request unless the
person names another.

```
Working from: <reader>, <material>. <Not seen: <item>, if any.> <One assumption, if any.>
```
