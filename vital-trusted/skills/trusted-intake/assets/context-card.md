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
Product status  <approved here per your label | approved elsewhere only | investigational | device, class <x> as you said | not about a product | unknown>  (<source>)
Use             <internal only | scientific exchange | promotional | not about a product | unclear>  (<source>)
Deliverable     <format, rough length>                             (<source>)
Material        <one line per item supplied | none yet>
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
  said" when stated. Never from memory.
- `Unknown` fields are left unknown. Other skills treat them with the careful defaults in
  `references/governance.md`.

## Person view (leadership stakes and above)

Shown once, at the top of the first reply after intake, in three to five lines. Not shown
for internal and quick work, where one line of assumption is enough.

```
Working from: <reader>, <market if relevant>, <use if relevant>, from <material>.
<If assumed:> I've assumed <assumption>; tell me if that's wrong.
<If an internal process applies:> It goes through your <kind of process> before it's used.
```

## One-line form (internal and quick, or nothing missing)

```
Working from: <reader>, <material>. <One assumption, if any.>
```
