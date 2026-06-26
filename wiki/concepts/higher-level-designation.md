---
id: higher-level-designation
type: concept
tags: [concept, iec-750, item-designation]
---

# Block 1 — higher-level (function) designation (prefix `=`)

**Block 1** gives the **higher-level designation** of an item — the *function* or
*unit* to which it belongs — and is introduced by the prefix sign **`=`** (equals)
([[iec-750]] §6). It answers "*which functional part of the plant is this item a
member of?*" rather than "what is the item?". Typical Block-1 codes name a unit, a
function group, or a sub-function: `=S5P2`, `=1`, `=A1A3`.

A higher-level designation is the **[[item-designation-aspects|function aspect]]**
of the designation and is usually *common to many items*. On a circuit diagram the
function of the whole sheet is therefore often stated **once**, in a note, and
inherited by every symbol on it. IEC 750 Figures 4 and 11 do exactly this with the
note *"higher-level designation applying to all items on the diagram: `(=S5P2)`"* —
the parentheses mark a designation that applies collectively, so each symbol need
only carry its own Block 3 (`-K1`, `-S1`, …) and is understood to mean
`=S5P2-K1`, `=S5P2-S1`, etc.

Block 1 is **hierarchical**: a sub-function is appended to its parent (e.g.
`=A1A3` = function group A3 within unit/function A1). IEC 750 §6.2 sets out a
numbering method for these function levels; §8 (see
[[designation-methods-comparison]]) compares it with the parallel method used for
the [[location-designation|location aspect]] (§7.2). Figure 6 illustrates
combining Block 1 with Block 3 — higher-level *numbers* for units (`=1`, `=2`,
`=3`) plus item *letters-and-numbers* (`-Q1`) — to give designations such as
`=1-Q1`.

**See:** [[iec-750]] · [[designation-block]] · [[item-designation-aspects]] ·
[[location-designation]] · [[designation-methods-comparison]] ·
[[item-identification-block]]
