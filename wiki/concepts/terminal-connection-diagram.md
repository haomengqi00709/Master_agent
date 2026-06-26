---
id: terminal-connection-diagram
type: concept
standard: IEC 1082-3
aliases: [terminal connection table]
tags: [concept, iec-1082, documentation]
---

# Terminal connection diagram and table (IEC 1082-3 §5)

The [[connection-documents-iec1082|connection document]] that provides the
information needed to make the **external connections to a single constructional
unit or equipment** (IEC 1082-3 Section 5, §5.1). It is essentially an
[[interconnection-diagram-iec1082]] seen from one unit's terminal strip: §5.1 states that a
*set* of terminal connection diagrams/tables for a set of units carries **the same
information in the same form** as an interconnection diagram for the connections
among those units — i.e. the same rules apply. Per §2.1 only **one end** of each
connection need be shown on a terminal-connection document.

**Worked examples (§5.2).**
- **fig. 13** — two terminal connection diagrams, one for unit `+A4` and one for
  `+B5`. Each cable end is labelled by its [[reference-designation-system|item
  designation]] and each core by its **core number**; spare terminals (connected or
  not) are marked **`RES` (reserved)**.
- **fig. 14** — the same two diagrams supplemented with the **terminal designations
  of the remote end**.
- **fig. 15** — two **connection-oriented terminal connection tables** with
  remote-end terminal designations, based on fig. 14; a **dash `-`** means *no
  connection*, and spare cores are denoted `RES`.
- **fig. 16** — a **terminal-oriented terminal connection table** based on the
  `+A4` diagram (each terminal listed with the core/cable attached).
- **fig. 17** — a **terminal connection table of grid type** with remote-end
  designations, recording the number of cores of each cable and the spare cores in
  the last column.

Terminals are identified by the designations marked on the device (or assigned by
the manufacturer/convention, or arbitrarily and explained), and the **same terminal
designation is used for the same terminal in all documents** (§2.3.2). A graphical
or colour terminal mark may be replaced by an equivalent letter code (`PE`, `BU`)
per IEC 445 / IEC 757.
