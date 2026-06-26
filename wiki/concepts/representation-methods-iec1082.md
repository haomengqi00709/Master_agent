---
id: representation-methods-iec1082
type: concept
standard: IEC 1082-1
aliases: [attached representation, detached representation, grouped representation, dispersed representation, repeated representation]
tags: [concept, iec-1082, documentation]
---

# Methods of representing components (IEC 1082-1)

IEC 1082-1 defines several **methods for placing the parts of a multi-element
device** (e.g. a relay's coil and its contacts) on a diagram. They trade
compactness against ease of following the circuit, and are illustrated by Part 1's
figures 2–11 using a common worked example (a relay, pushbutton, circuit-breaker,
three-winding transformer, optical coupler and multiplexer). The methods are:

- **Attached representation (fig. 2)** — all parts of a component are drawn
  **together as one symbol group**, mechanically/functionally adjacent.
- **Semi-attached representation (fig. 3)** — the parts are drawn apart but joined
  by a **thin dashed mechanical-link line** showing they belong together.
- **Detached representation (fig. 6)** — the parts are **drawn separately** wherever
  the circuit needs them, related only by their common item designation (e.g. the
  relay coil `-K1` and its contacts placed in different circuit branches).
- **Grouped representation (figs. 9, 10)** — several like components forming one
  package (e.g. a package of two relays, or four AND-elements with negated output)
  shown as a single grouped block.
- **Dispersed representation (fig. 11)** — the elements of a grouped/packaged
  device shown scattered (dispersed) across the diagram.
- **Repeated representation (figs. 8, 8A)** — a regularly repeating structure
  (e.g. a multiplexer) drawn once and marked as repeated rather than fully redrawn.

These methods concern the **arrangement of symbols**; they are orthogonal to the
**conductor-count** methods, [[single-line-representation]] (one line for a group
of conductors/poles) and [[multi-line-representation]] (every conductor drawn).
The detached and semi-attached methods rely on the [[reference-designation-system|item
designation]] (`-K1`, etc.) to tie scattered parts back together. (Compare the
older [[iec-113-1]] terms *assembled / semi-assembled / detached representation*.)
