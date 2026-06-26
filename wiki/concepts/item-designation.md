---
id: item-designation
type: concept
tags: [concept, iec-750, item-designation]
---

# Item designation

An **item designation** is the alphanumeric reference that identifies one
particular *item* of equipment on a diagram and in the associated documents
([[iec-750]] §4). In IEC 750 an **"item"** is anything that can be treated as a
discrete entity for the purposes of the diagram — a single component (a resistor,
a relay), a complete piece of apparatus, or a whole subassembly or unit. The
designation answers, for that item, up to four questions: *what function it
performs* (Block 1), *where it is located* (Block 2), *what kind of item it is and
which one* (Block 3), and *which terminal* (Block 4).

The designation is built by stringing together the relevant
**[[designation-block|blocks]]**, each marked by its **prefix sign**, in the fixed
order `= + - :`. Block 3 — the [[item-identification-block]] — is the most common
and is the one written `-K1`, `-R2`, `-Q1`; the other blocks are added only when
the function, location or terminal must also be stated. So a relay K1 that belongs
to function group S5P2, located in cubicle A, with its terminal 13, can be written
`=S5P2+A-K1:13`. Any block may be omitted; a bare `-K1` is a complete (if minimal)
item designation.

A central principle is that the designation is **independent of the graphical
symbol**: the symbol shows graphically *what type* of thing the item is, while the
item designation says *which individual one* it is and *where it sits* in the
plant. The **[[kind-of-item-letter-codes|kind-of-item letter]]** inside Block 3
(the `K` in `-K1`) is the only part that overlaps with the symbol's meaning, and
it is drawn from Table I.

**See:** [[iec-750]] · [[designation-block]] · [[item-identification-block]] ·
[[item-designation-aspects]] · [[simplified-designation]]
