---
id: simplified-designation
type: concept
tags: [concept, iec-750, item-designation]
---

# Simplified item designation

IEC 750 allows an item designation to be written in a **simplified form** in which
a repeated prefix sign is dropped where doing so causes no ambiguity ([[iec-750]]
§5). This matters most for **hierarchical Block-3** designations (see
[[item-identification-block]]), where an item is nested inside one or more
subassemblies and the full form would repeat the `-` prefix at every level.

IEC 750 Figures 4 and 5 give the canonical examples, each shown in full form and
in simplified form:

| Meaning | Full form | Simplified form |
|---------|-----------|-----------------|
| Subassembly A1 with pushbutton S1 | `-A1-S1` | `-A1S1` |
| Subassembly A2 with pushbutton S1 | `-A2-S1` | `-A2S1` |
| Circuit-breaker Q2 with main-contact assembly Q1 | `-Q2-Q1` | `-Q2Q1` |
| Subassembly A1 with resistor R2 | `-A1-R2` | `-A1R2` |
| Subassembly A2 with subassembly A1 | `-A2-A1` | `-A2A1` |
| Subassembly A2 → subassembly A1 → capacitor C1 | `-A2-A1-C1` | `-A2A1C1` |

The simplification is legitimate only when the reader can still parse the
kind-letters and numbers unambiguously; the prefix sign for the *block* is kept
(one leading `-`), only the *internal repetitions* between levels are removed. A
related, document-level simplification (IEC 750 Figure 5) lets a **note** declare
that *all designations on the diagram belong to Block 3*, after which the leading
`-` itself may be omitted and items are written `A1S1`, `R2`, etc.

The same economy applies in principle to the hierarchical
[[higher-level-designation|function]] and [[location-designation|location]] blocks,
whose nested levels can likewise collapse a repeated `=` or `+`.

**See:** [[iec-750]] · [[item-identification-block]] · [[item-designation]] ·
[[designation-block]]
