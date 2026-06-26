---
id: terminal-electrical-characteristics
type: concept
tags: [concept, iec-79-3, ex, intrinsic-safety]
---

# Terminal electrical characteristics

Residual-reactance limits that the [[spark-test-apparatus]] itself must meet **at
the terminals of the [[contact-mechanism]]** (standard's Figure 4) so that the
apparatus does not add energy storage that would falsify the test of the circuit
under test ([[iec-79-3]] §4.2, last paragraph):

- **Capacitance ≤ 30 pF** — measured with the contacts open and with the contacts
  closed;
- **Resistance ≤ 0,15 Ω** — at a current of 1 A d.c.;
- **Inductance ≤ 3 nH**.

The intent is that the apparatus contributes negligible stray C, R and L compared
with the intrinsically-safe circuit being assessed, so the spark energy delivered
at the electrodes reflects the **circuit under test**, not the fixture. These
parasitics matter because intrinsic safety turns on the energy available in the
circuit (see [[intrinsically-safe-circuit]]); an apparatus with significant stray
reactance could either mask or exaggerate ignitions. The limits are checked as
part of keeping the apparatus within specification (referenced in the sensitivity
trouble-shooting list, see [[spark-test-sensitivity-actions]]).

**Related:** [[contact-mechanism]] · [[spark-test-apparatus]] ·
[[spark-test-calibration]] · [[intrinsically-safe-circuit]]
