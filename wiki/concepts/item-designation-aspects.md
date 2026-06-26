---
id: item-designation-aspects
type: concept
tags: [concept, iec-750, item-designation]
---

# Aspects of item designation (function / location / product)

IEC 750 recognises that the same physical item can be referred to from several
**aspects**, and provides a parallel designation for each ([[iec-750]] §3–§7). The
three aspects, each with its own [[designation-block|block and prefix sign]], are:

- **Function aspect** — *what the item does* in the system, expressed by the
  **[[higher-level-designation|higher-level (function) designation]]**, prefix
  `=`. This places the item in a functional hierarchy of units / function groups
  (e.g. `=S5P2`) rather than a physical one.
- **Location aspect** — *where the item physically is*, expressed by the
  **[[location-designation]]**, prefix `+`. This places the item in a spatial
  hierarchy of rooms, cubicles and mounting positions (e.g. `+A`, `+C`,
  `+16+A2B31`).
- **Product / kind aspect** — *what the item itself is*, expressed by the
  **[[item-identification-block|identification of item]]** (Block 3), prefix `-`.
  This names the item by its [[kind-of-item-letter-codes|kind-of-item letter]]
  and serial number (e.g. `-K1`, `-R2`).

The point of separating the aspects is that a circuit is conceived functionally
but realised physically: a relay may be *function* "supervision of pump 2", be
*located* in cubicle A, and *be* the third relay `-K3`. Each aspect can be
numbered independently, which is why IEC 750 needs three parallel systems rather
than one. §8 (see [[designation-methods-comparison]]) explicitly compares the
numbering methods of the function aspect (§6.2) and the location aspect (§7.2),
which look superficially similar but answer different questions.

In practice a diagram chooses a *leading* aspect (often the function aspect, fixed
once in a note such as `(=S5P2)`) and labels individual symbols with only the
product aspect `-K1`; the other aspects are added where disambiguation requires it.
The same separation of *function vs location vs product* aspects is the structuring
idea later formalised in IEC 61346 / 81346.

**See:** [[iec-750]] · [[item-designation]] · [[higher-level-designation]] ·
[[location-designation]] · [[item-identification-block]] ·
[[designation-methods-comparison]]
