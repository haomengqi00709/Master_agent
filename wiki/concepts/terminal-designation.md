---
id: terminal-designation
type: concept
tags: [concept, iec-750, item-designation]
---

# Block 4 — terminal designation (prefix `:`)

**Block 4** designates a **terminal** (connection point) of an item and is
introduced by the prefix sign **`:`** (colon) ([[iec-750]] §9). It is the most
detailed block: where Block 3 identifies the *item*, Block 4 picks out *one of its
terminals* so a wire or connection can be referenced precisely. It is written by
appending the terminal's identifier after the item's Block 3, e.g. `-K1:13`,
`-X1:4`, `-Q1:2`.

The terminal identifier itself follows the marking carried on the apparatus — the
terminal numbers/letters defined for that kind of equipment (for example the
contact-terminal numbering of relays and contactors, or the terminal markings of a
terminal board `-X`). IEC 750 thus *uses* the apparatus terminal markings (the same
identification scheme standardised in **IEC 445**, apparatus terminal marking)
rather than inventing new ones: the colon block says "terminal *so-numbered* of
this item".

Because the terminal designation always hangs off an item, a complete reference
combines the relevant blocks in order, e.g. `=S5P2+A-K1:13` = terminal 13 of relay
K1, which is in function group S5P2 and located in cubicle A. On a diagram the
higher blocks are usually inherited from a note and only `-K1:13` (or even `K1:13`
where Block-3 prefixes are omitted by note) is written at the connection.

Terminal designation is what lets a wiring diagram or connection table state both
ends of every conductor — item-and-terminal to item-and-terminal — which is the
level of detail the documents governed by [[iec-1082]] require.

**See:** [[iec-750]] · [[designation-block]] · [[item-identification-block]] ·
[[item-designation]]
