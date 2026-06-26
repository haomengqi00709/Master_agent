---
id: location-designation
type: concept
tags: [concept, iec-750, item-designation]
---

# Block 2 — location of item (prefix `+`)

**Block 2** gives the **location designation** — *where the item is physically
situated* — and is introduced by the prefix sign **`+`** (plus) ([[iec-750]] §7).
It answers "*in which room / cubicle / mounting position is this item?*", which is
deliberately separate from *what the item is* (Block 3) and *what function it
serves* (Block 1). Location codes are things like `+A`, `+C`, `+106` (room 106),
or hierarchical positions such as `+16+A2B31`.

The location aspect (see [[item-designation-aspects]]) is needed because the same
function may be realised by hardware spread across the plant, and maintenance staff
must be able to *find* the item. IEC 750 Figure 7 shows a switchgear-and-controlgear
room laid out as assemblies `+A`, `+B`, `+C` and `+D`; Figure 8 then designates
*subassembly 4 of assembly A* and shows location designations nesting
(`+A`, then positions within it). A note may also fix the location for a whole
sheet, e.g. *"location: room 106"* written `(+106…)`.

Block 2 is **hierarchical** in the same way as Block 1: successive `+` levels
descend from coarse to fine position (room → cubicle → rack → slot), and the
repeated prefix can be simplified where unambiguous (see
[[simplified-designation]]). IEC 750 §7.2 defines the numbering method for these
location levels; §8 then **compares** the location method (§7.2) with the
[[higher-level-designation|higher-level/function method]] of §6.2 — they share a
form but track different hierarchies (see [[designation-methods-comparison]]). A
full designation may carry both, as in IEC 750 Figure 11 where the pump-equipment
subassemblies of Figure 4 are *"supplemented with location designations"*, giving
combined references such as `+16+A2B31` and `=S5P2+A-K1`.

**See:** [[iec-750]] · [[designation-block]] · [[item-designation-aspects]] ·
[[higher-level-designation]] · [[designation-methods-comparison]] ·
[[item-identification-block]]
