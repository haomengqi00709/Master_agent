---
id: unit-connection-diagram
type: concept
standard: IEC 1082-3
aliases: [unit wiring diagram, unit connection table]
tags: [concept, iec-1082, documentation]
---

# Unit connection diagram and table (IEC 1082-3 §3)

The [[connection-documents-iec1082|connection document]] that provides **all the
information about the *internal* connections within a single constructional unit or
assembly of units** (IEC 1082-3 Section 3, §3.1). Information about *external*
connections among units need not be included, but a reference to the relevant
[[interconnection-diagram-iec1082]] may be given. It is the IEC 1082 successor of the
*unit wiring diagram* of the superseded IEC 113-6.

**Layout (§3.2).** Device symbols should be arranged to **correspond with the view
of the equipment as seen when making the connections**; more than one view may be
needed if the unit is wired from several directions. Terminals need not be drawn in
their physical arrangement, and devices stacked at several levels may be shown
flipped/turned/moved so the user can see them — the method used being indicated
(e.g. a note that the movable part right of a boundary line is wired from the front
of the bay).

**Conductor representation (worked examples, §3.3).**
- **fig. 1** — continuous lines, conductors identified by **conductor numbers**.
- **fig. 2** — the same unit with **interrupted lines** and terminal symbols left
  out.
- **fig. 3** — conductors grouped into two **cable bundles `-W1`, `-W2`**, the
  entering/leaving wires drawn so they stay identifiable.
- **fig. 5** — a **connection-oriented unit connection table** for fig. 1: the
  instruction `TWIST 1` marks a twisted pair (conductors 44/45; 46/47 another); a
  **short dash** in the conductor-designation column means the terminals are
  *directly* connected with no separate conductor; `LINK` means a physical link or
  short unnumbered wire.
- **figs. 6–7** — **matrix / grid form** for a sub-rack of printed-circuit boards:
  each board's terminal symbols are placed to suit the diagram (not the physical
  pin order), so exact point-to-point connections need not be shown.

Devices are identified by their [[reference-designation-system|item designations]]
(`-K14`, `-V1`, …) and terminals by the manufacturer's terminal designations (or
arbitrarily assigned ones, explained in the table), used consistently across all
documents (§2.3.2).
