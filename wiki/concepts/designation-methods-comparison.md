---
id: designation-methods-comparison
type: concept
tags: [concept, iec-750, item-designation]
---

# Comparison of the higher-level and location designation methods (§8)

IEC 750 §8 is a short clause that **compares the methods described in §6.2 and
§7.2** — that is, the numbering method for the
[[higher-level-designation|higher-level (function) designation]] (Block 1, prefix
`=`) against the numbering method for the [[location-designation]] (Block 2, prefix
`+`) ([[iec-750]] §8). The two methods are deliberately *parallel in form* — both
build a hierarchical code by descending through levels — but they answer different
questions and therefore must be kept distinct.

The comparison matters because the function hierarchy and the location hierarchy
**need not coincide**: items belonging to one function group (`=S5P2`) can be
scattered across several physical locations (`+A`, `+C`, …), and one cubicle (`+A`)
can house items from several functions. §8 clarifies that, although §6.2 and §7.2
use a similar numbering technique, each is applied independently to its own
hierarchy, and the prefix sign (`=` versus `+`) is what keeps a given code attached
to the right [[item-designation-aspects|aspect]]. IEC 750 Figure 11 demonstrates the
two living together: the pump-equipment subassemblies first designated by function
in Figure 4 are *supplemented with location designations*, producing combined
references where a `=` block and a `+` block sit side by side on the same item.

In other words, §8 is the standard's caution against conflating the *function
aspect* and the *location aspect* just because their codes look alike — the
distinction that later standards (IEC 61346 / 81346) formalise as separate
function-, location- and product-structures.

**See:** [[iec-750]] · [[higher-level-designation]] · [[location-designation]] ·
[[item-designation-aspects]] · [[designation-block]]
