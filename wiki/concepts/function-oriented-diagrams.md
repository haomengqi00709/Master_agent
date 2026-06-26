---
id: function-oriented-diagrams
type: concept
standard: IEC 1082-2
aliases: [overview diagram, function diagram, logic-function diagram, terminal-function diagram, equivalent circuit diagram]
tags: [concept, iec-1082, documentation]
---

# Function-oriented diagrams (IEC 1082-2)

The family of diagrams **showing how a system functions**, independent of its
physical construction — the whole subject of [[iec-1082|IEC 1082-2 (1993)]]. They
follow the [[function-oriented-vs-location-oriented-structure|function-oriented
structure]] and are built from [[60617-3|IEC 617]] symbols chosen, per §2.4, to
**depict the function actually performed** by the device (the same physical device
may be drawn as an AND- or OR-element, a multiplier or a squarer, depending on its
role in the system). Part 2 standardises these document types:

- **Overview diagram (§3.4, figs. 44–54)** — the top-level functional picture of a
  system, showing its sub-systems/functions and the energy/signal flow between
  them, with rectangles (often text-inscribed) for the blocks. Examples: a
  steelworks `=…`, a radio receiver, an electronic telephone exchange (with SPEECH
  / SIGNALLING data buses), a thyristor-converter pumping system, a HV switchgear
  assembly with location information. Items carry [[reference-designation-system|IEC
  750 designations]] (`=E1`, `=W11`, `-A31`, …).
- **Function diagram = equivalent-circuit diagram (figs. 55–56)** — represents a
  device by an idealised equivalent circuit (e.g. a transformer and its load, a
  constant-level generator) for analysis rather than for building.
- **Circuit diagram (figs. 21–22, 71)** — the detailed functional diagram showing
  all the electrical connections and operating links; Part 2 covers the
  **positive-logic convention** and **direct logic-polarity indication** variants.
  (For the general definition see the [[circuit-diagram]] of [[iec-113-1]]; IEC 1082
  governs how it is drawn for function.)
- **Logic-function diagram (fig. 57)** — a diagram of a logic system (e.g. a
  timing-pulse generator) built from binary-logic symbols per IEC 617-12.
- **Terminal-function diagram (§ figs. 40–41)** — describes a unit purely by the
  **function at each of its terminals**, optionally using a **function chart** and
  supplementary application information; it treats the unit as a black box with
  defined terminal behaviour.

Supporting rules cover **fundamental circuits** (an RS-latch, figs. 31–32), **two-
and four-terminal passive networks** (figs. 26–27), **amplifying stages** (fig. 29),
the use of a **block symbol** in a circuit diagram (fig. 42), and
[[simplified-representation-many-terminals|simplifying symbols with many terminals]].
Worked sheets (figs. 63–67) show the *same* co-ordinating logic unit `-A31`
implemented alternately by a function chart, by relays, by binary-logic elements,
and by a computer — illustrating that a function-oriented diagram is independent of
the technology realising the function.
