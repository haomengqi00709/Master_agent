---
id: signal-flow-and-line-bundling
type: concept
standard: IEC 1082-1
aliases: [signal flow direction, line bundling, grouping of lines, connecting lines]
tags: [concept, iec-1082, documentation]
---

# Connecting lines: signal flow & bundling (IEC 1082-1 §4)

The general drawing rules in IEC 1082-1 clause 4 for **drawing and tidying the
connecting lines** of a diagram. They govern direction of reading, how lines join,
and how many lines may be collapsed.

**Preferred signal-flow direction.** The recommended sense of signal flow is **left
to right and top to bottom** (Part 1 fig. 42). Symbols are normally drawn for this
flow; using the non-preferred directions (right-to-left, bottom-to-top) requires
symbols specifically designed for it. For binary-logic and block symbols Part 1
tabulates the symbol adaptations for all four signal directions (figs. 51, 52),
keyed to the general qualifying symbol placed preferably at the top per IEC 617-12.
The **preferred main signal path** and **power circuits** may be emphasised with
**thicker lines** (figs. 60, 61; the thick-to-thin ratio is set in Annex A as ≥ 2:1).

**Junctions.** A connection (junction) between lines is shown as a **T-junction**;
a **double junction** is exceptional and then the **dot is mandatory**, whereas on
a simple branch the dot is optional (figs. 58–59). Leader lines to connecting lines
terminate per Annex A (dot inside an object, arrowhead on an outline).

**Bundling and grouping of lines.** Where many parallel lines run together they may
be **grouped** (drawn close, fig. 66) or **bundled** into a single drawn line:
- *method a)* — the bundle is one line with the individual lines indicated, a dot
  marking the first connecting line (figs. 67–69);
- *method b)* — the bundle's individual lines are identified by **signal
  designations** (figs. 70–71), tying each entry to its exit by name.

This is closely related to [[single-line-representation]]: a group of conductors
can be drawn as one line with the **number of conductors indicated** by a stroke +
figure (figs. 72–73, e.g. an 8-conductor information bus). Crossing references for
lines that are interrupted rather than bundled are handled by
[[signal-and-location-references]]. The fluid-flow direction of pipes (gas, liquid)
is indicated by arrows (fig. 40), and leader lines may be added to connecting lines
(fig. 41).
