---
id: impulse-sparkover-voltage
type: concept
tags: [concept, iec-99-1, surge-arrester]
---

# Impulse sparkover voltage of an arrester

The **impulse sparkover voltage of an arrester** is the highest value of voltage attained before
sparkover during an impulse of given waveshape and polarity applied between the terminals of the
arrester ([[iec-99-1]] §39). It is the impulse counterpart of the
[[power-frequency-sparkover-voltage]], and together with the [[residual-voltage]] it defines the
[[protective-characteristics-arrester|protective level]] of the arrester. IEC 99-1 defines several
related forms:

- **Front-of-wave impulse sparkover voltage** (§40) — obtained on the wavefront whose voltage
  increases linearly with time (a steep front); the most onerous, fast-front condition.
- **Standard lightning impulse sparkover voltage** (§41) — the lowest prospective peak value of a
  standard 1.2/50 lightning voltage impulse ([[impulse-waveshape]]) which causes sparkover on every
  application.
- **Time to sparkover** (§42) — the interval between virtual origin and the instant of sparkover,
  in microseconds.
- **Impulse sparkover-voltage / time curve** (§43) — the curve relating impulse sparkover voltage to
  time to sparkover.

These quantities are verified by the [[voltage-impulse-sparkover-test]] (§61): the standard lightning
test (§61.2), the sparkover-voltage/time curve (§61.3) and front-of-wave test (§61.3.1), and the
switching-impulse curve (§61.4, only for 10 000 A arresters above 100 kV). The **maximum permissible
standard-lightning and front-of-wave sparkover voltages** are tabulated against
[[rated-voltage-arrester|rated voltage]] and front steepness in [[iec-99-1]] **Table VI** (e.g. for a
12 kV arrester at 100 kV/µs front steepness: 43 kV peak standard, 50 kV peak front-of-wave). No limits
are yet specified for switching-impulse sparkover.

**Related:** [[surge-arrester]], [[power-frequency-sparkover-voltage]], [[residual-voltage]],
[[impulse-waveshape]], [[voltage-impulse-sparkover-test]], [[protective-characteristics-arrester]],
[[impulse-protective-level]].
