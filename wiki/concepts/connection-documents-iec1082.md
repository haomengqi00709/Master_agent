---
id: connection-documents-iec1082
type: concept
standard: IEC 1082-3
aliases: [connection diagram, connection table, connection list, wiring documents]
tags: [concept, iec-1082, documentation]
---

# Connection documents (IEC 1082-3)

The class of documents that give the information needed to **physically wire**
equipment — the whole subject of [[iec-1082|IEC 1082-3 (1993)]]. Per §2.1,
**connection documents provide information on the physical connections among
components, devices, assemblies and installations, and are used when assembling,
installing or maintaining equipment.** They are the "how it's wired" complement to
the [[function-oriented-diagrams|function-oriented diagrams of Part 2]].

**What every connection document must carry (§2.1).** It shall identify the
**connection points of each connection** and the **conductors or cables** used. For
terminal-connection documents, only one end need be shown. Information considered
for inclusion: conductor/cable type (type designation, part number, material,
size, insulation colour, voltage rating, number of conductors); the conductor/cable
number or [[reference-designation-system|item designation]]; identification of the
connection points (item and/or terminal designation, remote-end designation);
laying/routing/termination/twisting/screening instructions; conductor length;
[[signal-and-location-references|signal designation]]; and special classification.
Conductors are coloured/numbered per **IEC 446**, colour-coded per **IEC 757**,
items designated per **[[iec-750|IEC 750]]**, and terminals per **IEC 445** (a
graphical/colour terminal mark may be replaced by an equivalent letter code, e.g.
`PE` for protective earth, `BU` for blue).

**Diagram vs table (§2.2–2.3).**
- A **connection diagram** uses **topographical layout** but need not be to scale
  (§2.2.1); devices are simple outlines (squares, rectangles, circles) or
  simplified pictorials, terminals clearly indicated. Conductors are shown either
  by **continuous lines** (groups/cables collapsible to a single line, §2.2.3a) or
  by **interrupted lines** with association of the broken ends (§2.2.3b). For dense
  wiring (e.g. a sub-rack of PCBs) a **matrix / grid form** is used (§2.2.4).
- A **connection table/list** comes in two forms (§2.3.1): **terminal-oriented**
  (each device and its terminals listed, showing the connection(s) at each) or
  **connection-oriented** (each wire/cable conductor listed, showing the terminals
  it joins). IEC 1082 draws **no distinction between *table* and *list*** (§1.1).

**The four document types** (one Part-3 section each):
[[unit-connection-diagram]] (Section 3 — *internal* connections of a single unit) ·
[[interconnection-diagram-iec1082]] (Section 4 — connections *between* units) ·
[[terminal-connection-diagram]] (Section 5 — *external* connections to a unit) ·
[[cable-diagram]] (Section 6 — cable laying and routing). Part 3 corresponds to the
superseded IEC 113-5 and IEC 113-6.
