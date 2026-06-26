---
id: designation-block
type: concept
tags: [concept, iec-750, item-designation]
---

# Designation block (and prefix signs)

IEC 750 builds every [[item-designation]] from up to four **designation blocks**,
each conveying a different *aspect* of the item and each introduced by a unique
**prefix sign** ([[iec-750]] §3). Because each block carries its own marker, blocks
can be freely combined, re-ordered for emphasis, or omitted without ambiguity — the
prefix sign tells the reader which aspect the following characters describe.

| Block | Aspect | Prefix sign | Concept page |
|-------|--------|-------------|--------------|
| **Block 1** | Higher-level / function designation | **`=`** (equals) | [[higher-level-designation]] |
| **Block 2** | Location of item | **`+`** (plus) | [[location-designation]] |
| **Block 3** | Identification of item (kind + serial number) | **`-`** (hyphen / minus) | [[item-identification-block]] |
| **Block 4** | Terminal designation | **`:`** (colon) | [[terminal-designation]] |

When a complete designation is written, the blocks appear in the canonical order
`= + - :`, e.g. `=S5P2+A-K1:13`. Any block may be left out: most working
designations on a diagram are just Block 3 (`-K1`), with Blocks 1 and 2 stated once
in a note (as a "higher-level designation applying to all items on the diagram",
e.g. the note `(=S5P2)` in IEC 750 Figures 4 and 11) and inherited by every item.

The prefix sign is **part of the designation**, not punctuation between fields: it
both identifies the aspect and separates one block from the next. Within a block,
the characters may themselves be hierarchical (e.g. `=A1A3` for a function group
nested in a larger function), and where the same prefix would repeat down a level
the [[simplified-designation|simplified form]] allows it to be dropped
(`-A2-A1-C1` → `-A2A1C1`).

**See:** [[iec-750]] · [[item-designation]] · [[item-designation-aspects]] ·
[[item-identification-block]] · [[higher-level-designation]] ·
[[location-designation]] · [[terminal-designation]]
