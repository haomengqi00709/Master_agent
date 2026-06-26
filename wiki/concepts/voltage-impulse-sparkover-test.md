---
id: voltage-impulse-sparkover-test
type: concept
tags: [concept, iec-99-1, surge-arrester]
---

# Voltage impulse sparkover tests (Type test, §61)

The **voltage impulse sparkover tests** of [[iec-99-1]] §61 establish the
[[impulse-sparkover-voltage|impulse sparkover]] performance of the arrester. They are made (per §55,
§59) on the **same complete-arrester samples** used for the [[power-frequency-sparkover-test]] (§60);
results for other ratings within ±25 % (or 6 kV) of a tested rating may be scaled. The clause has four
parts:

- **§61.2 Standard lightning-voltage impulse sparkover test.** The generator is set to a **1.2/50**
  ([[impulse-waveshape]]) wave at the prospective peak in Table VI. Five positive and five negative
  impulses are applied and **the gaps must spark over on every impulse**; if they fail once, ten more
  of that polarity are applied and must all spark over. Tolerances: 97–100 % of specified peak,
  0.85–1.6 µs front, 40–60 µs tail.
- **§61.3 Lightning-voltage impulse sparkover-voltage / time curve test.** Using the polarity giving
  the higher sparkover, 1.2/50 waves of increasing amplitude (and varied front times of 30–60, 150–300
  and 1 000–2 000 µs) plot the sparkover-voltage / time curve, the highest voltage before sparkover
  against time to sparkover. A U₅₀% sparkover is found by 5 % steps, then ten impulses at 1.4×U₅₀%.
- **§61.3.1 Front-of-wave voltage impulse sparkover test.** Using a wave of the virtual front
  steepness in Table VI column 2, five positive and five negative impulses are applied; **the sparkover
  voltage shall not exceed the value in the appropriate column of Table VI** (Fig. 1). The §61.3 curve
  may be used to determine the front-of-wave value if ≥5 points of each polarity lie within ±0.1 µs of
  the steepness line.
- **§61.4 Switching-voltage impulse sparkover-voltage / time curve test.** Applicable only to 10 000 A
  light- and heavy-duty arresters rated above 100 kV. It demonstrates switching-surge sparkover; no
  maximum limit is yet specified.

Maximum permissible standard-lightning and front-of-wave sparkover voltages are tabulated against
[[rated-voltage-arrester|rated voltage]] and front steepness in **Table VI**. The §61.2 test is also a
[[routine-and-acceptance-tests|standard acceptance test]] (§68).

**Related:** [[impulse-sparkover-voltage]], [[impulse-waveshape]], [[power-frequency-sparkover-test]],
[[protective-characteristics-arrester]], [[type-test]], [[residual-voltage-test]].
