---
id: long-duration-current-impulse-withstand-test
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Long duration current impulse withstand test (§5.8, §7.4)

This test demonstrates the ability of the [[metal-oxide-resistor|metal-oxide
resistor]] elements to **withstand the dielectric and energy stresses of a
long-duration discharge without puncture or [[impulse-waveshape-terminology|flashover]]**
([[iec-99-4]] §5.8, §7.4). It uses the rectangular
[[long-duration-current-impulse]] (§2.18) representing the discharge of a charged
line. Made on **three new samples** (§7.4.1) which must have rated voltage ≥3 kV
(need not exceed 6 kV); the lightning-impulse [[residual-voltage]] at
[[nominal-discharge-current]] is measured before and after. Each test consists of
**18 discharge operations in six groups of three** (50–60 s between operations,
cooling to ambient between groups).

Two forms by class:
- **§7.4.2 Line discharge test** (10 000 A & 20 000 A) — applies impulses simulating
  discharge of a precharged line per the **[[line-discharge-class]]** parameters
  (Table 4: surge impedance, peak duration, charging voltage by class 1–5). Energy
  W is computed from the table parameters and the lowest measured switching residual
  voltage. Generator tolerances: peak duration 100–120 % of table, total duration
  ≤150 % of peak, oscillations/overshoot ≤10 %, per-impulse energy within 90–110 %
  (first) / 100–110 % (subsequent). Example circuit: Annex J.
- **§7.4.3 Long-duration impulse test** (5 000 A & 2 500 A) — Table 5: peak current
  **75 A over 1 000 µs** (5 000 A), **50 A over 500 µs** (2 500 A). *Not required*
  for 1 500 A.

Pass: after the test, the [[residual-voltage]] must not have changed by more than
**5 %**, and visual examination must reveal no puncture, flashover, cracking or
other significant damage of the resistors (§5.8). Type-test item 3 of the
[[arrester-type-test]] programme; row 4 of [[arrester-classification]] Table 1.
