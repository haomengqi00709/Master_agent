---
id: item-identification-block
type: concept
tags: [concept, iec-750, item-designation]
---

# Block 3 — identification of item (prefix `-`)

**Block 3** is the core of an [[item-designation]]: it identifies *the item
itself* and is introduced by the prefix sign **`-`** (hyphen / minus)
([[iec-750]] §5). It is the block actually written beside almost every symbol on
a circuit diagram. Its structure is a **[[kind-of-item-letter-codes|kind-of-item
letter]]** drawn from Table I, followed by a **serial number** distinguishing the
several items of that kind:

```
-  K  1
│  │  └─ serial number (this is the first relay)
│  └──── kind-of-item letter (K = relay/contactor), from Table I
└─────── prefix sign for Block 3 (identification of item)
```

So `-R2` is "the resistor numbered 2", `-Q1` "power switch 1", `-S1` "switch /
control device 1". Items of the **same kind** are numbered in a single sequence
(`-R1`, `-R2`, `-R3`…). Where useful, a *function* or *position* letter can extend
the code, but the minimal valid Block 3 is one kind-letter plus a number.

Block 3 is also **hierarchical**: a component inside a subassembly is designated
by chaining the subassembly's Block 3 with the component's. IEC 750 Figure 4/5
examples show subassembly `-A1` containing pushbutton `-S1` written `-A1-S1`, and
the nested case `-A2-A1-C1` (capacitor C1, in subassembly A1, in subassembly A2).
Where the repeated `-` is unambiguous it may be dropped — see
[[simplified-designation]] (`-A1-S1` → `-A1S1`, `-A2-A1-C1` → `-A2A1C1`). On a
diagram where all designations belong to Block 3, a note may state this so the
prefix `-` can be omitted entirely (IEC 750 Figure 5 note: "all item designations
without a prefix sign belong to Block 3").

**See:** [[iec-750]] · [[kind-of-item-letter-codes]] · [[item-designation]] ·
[[designation-block]] · [[simplified-designation]]
