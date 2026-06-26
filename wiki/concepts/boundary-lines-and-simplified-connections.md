---
id: boundary-lines-and-simplified-connections
type: concept
standard: IEC 1082-1
aliases: [boundary frame, boundary line, enclosure frame, simplified representation of connections]
tags: [concept, iec-1082, documentation]
---

# Boundary lines, frames & simplified connections (IEC 1082-1 §4)

Two related drawing devices from IEC 1082-1 clause 4 that let a diagram show
**grouping and reduce clutter** without losing meaning.

**Boundary lines / frames (§4.5, figs. 74–75).** A **boundary frame** (a closed
dashed/chain outline) is drawn around a set of symbols to indicate that they form
one **functional unit**, e.g. enclosing the parts of unit `-A1` (fig. 74). A
**nested ("window") boundary frame** does the opposite: it marks items that are
**not** part of the surrounding unit — fig. 75 uses a window frame to show that
`-S1` and `-S2` are *external to* unit `-Q1`. Boundary frames thus make the
[[function-oriented-vs-location-oriented-structure|function/location grouping]]
visible on the drawing itself, complementing the
[[reference-designation-system|item-designation prefixes]].

**Simplified representation of connections (figs. 76–83).** Rules for cutting the
number of drawn connection lines to a component:
- an AND-gate (or any component) may be drawn **without terminal designations
  (a)**, **with terminal designations (b)**, or **with terminal designations in
  consecutive order (c)** (figs. 76–77);
- **single-line representation** collapses several identical connections into one
  line annotated with a count (fig. 83 — e.g. a three-pole switch as one line ≡
  three single-pole switches; six identical D-latches with common control as `6×`);
- terminal-symbol **location rules** (figs. 78–82) fix where the male/female
  connector halves, frame/chassis, conductive-enclosure and screen connections are
  drawn, including which connector half belongs to the unit `-A1` and which to the
  cable `-W1`.

Technical data and waveforms attached to a symbol have their own placement rules
(figs. 88–91: rating data beside the symbol, signal waveforms and explanatory
texts in a circuit diagram). These simplifications interact with
[[single-line-representation]] and the
[[simplified-representation-many-terminals|many-terminal simplifications of Part 2]].
