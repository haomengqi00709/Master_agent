---
id: fault-not-considered-components
type: concept
tags: [concept, iec-79-18, ex, encapsulation]
---

# Faults and components not considered (encapsulation "m")

[[type-of-protection-m|Encapsulation "m"]] **shall be maintained even in the case of
recognized overloads and of any single internal electrical fault** that could cause
an overvoltage or overcurrent — for example a short circuit or other component
failure, a change in a component's characteristics, or a fault in printed circuitry
(IEC 79-18 §5.1.4). If a fault can lead to subsequent faults (e.g. overrating another
component), the primary and subsequent faults count as a **single fault**. Acceptance
is judged by [[thermal-tests]] §8.2.1.3.

Against that fault model, §5.1.5 lists components that, when encapsulated to this
standard, are **not considered subject to fault** (so they need not be assumed
failed):

- **(a) Not subject to short-circuit / lower-than-rated resistance** — film-type
  resistors; single-layer helical wire resistors; single-layer helical coils — when
  used at **no more than two-thirds of rated voltage or power**.
- **(b) Not subject to short-circuit, lower resistance or higher capacitance** —
  plastic-foil, paper and ceramic capacitors — when used at **no more than two-thirds
  of rated voltage**.
- **(c) Optocouplers and relays segregating circuits** — not subject to breakdown
  between the segregated circuits when the sum *U* of the r.m.s. circuit voltages is
  **≤ 1 000 V** and the electric strength tested per 8.2.3 is **≥ 1.5 U**.
- **(d) Transformers, coils and motor windings** — not subject to inter-turn shorts
  (and transformers not subject to inter-winding breakdown) when they comply with
  **IEC 79-7** (including wire < 0.25 mm) **and** are protected against inadmissible
  internal temperatures.
- **(e) Transformers** — not subject to inter-turn shorts/inter-winding breakdown when
  they comply with **8.1 of IEC 79-11**, except type 2(a) of that clause.

Together with the [[distances-through-compound|distances of §5.3]] (which need no
fault to be assumed), these "not considered" components define the boundary of the
single-fault analysis.

**Related:** [[type-of-protection-m]] · [[distances-through-compound]] · [[thermal-tests]] · [[apparatus-electric-strength-test]] · [[temperature-limitation]]
