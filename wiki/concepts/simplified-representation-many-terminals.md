---
id: simplified-representation-many-terminals
type: concept
standard: IEC 1082-2
aliases: [simplifying symbols with many terminals, breaking the outline]
tags: [concept, iec-1082, documentation]
---

# Simplifying symbols with many terminals (IEC 1082-2)

A drawing technique in [[iec-1082|IEC 1082-2]] for components — typically large
integrated circuits, connectors or sub-racks — that have **too many terminals to
draw cleanly** in full. Part 2 gives two complementary devices (figs. 58–59):

- **Simplifying a many-terminal symbol (fig. 58)** — reducing the drawn detail of a
  symbol with a large number of terminals, e.g. by listing terminals in compact
  groups rather than spacing every pin around the outline.
- **Breaking the outline (fig. 59)** — the symbol's rectangle outline may be
  **interrupted (broken)** so that the terminal rows can be laid out compactly,
  the break indicating that the outline continues and the terminals still belong to
  one device.

When the same terminal designation must be repeated (e.g. for a repeated structure),
**parentheses may be added around the repeated terminal designations** per §2.11.2
and §2.4.4.4 (a note attached to several Part-2 figures). The technique is paired
on connection drawings with the **matrix / grid layout** of
[[connection-documents-iec1082|IEC 1082-3 §2.2.4]], where a many-terminal device's
pins are placed in a grid to suit the diagram rather than the physical pin order.

This is the function-oriented counterpart of the general
[[boundary-lines-and-simplified-connections|simplified-connection rules]] of Part 1
and relies on the [[reference-designation-system|terminal designations]] (`:`)
remaining consistent across all documents in which the device appears.
