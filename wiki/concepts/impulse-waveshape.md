---
id: impulse-waveshape
type: concept
tags: [concept, iec-99-1, surge-arrester]
---

# Impulse and its waveshape designation

An **impulse** is a unidirectional wave of voltage or current which, without appreciable oscillations,
rises rapidly to a maximum value and falls, usually less rapidly, to zero ([[iec-99-1]] §16). A
voltage or current impulse is defined by its polarity, peak value, front time and time to half value
on the tail. IEC 99-1 §16–§33 build a precise vocabulary for the impulses used to specify and test
arresters:

- **Peak (crest) value** (§18) — the maximum value of voltage or current in the impulse.
- **Front / tail** (§19, §20) — the parts of the impulse before and after the peak.
- **Virtual origin** (§24) and **virtual front time T₁** (§25) — the front time is 1.67× the time to
  rise from 30 % to 90 % of peak (for voltage fronts ≤ 30 µs), or 1.25× the 10 %–90 % rise time for
  current impulses.
- **Virtual time to half value on the tail T₂** (§27) — origin to the instant of half-peak decay.
- **Waveshape designation T₁/T₂** (§28) — written as front-time / tail-time in microseconds, the "/"
  having no mathematical meaning.
- **Standard lightning voltage impulse** (§29) — waveshape **1.2/50**.
- **Switching voltage impulse** (§30) — a voltage impulse with virtual front time greater than 30 µs.
- **Full-wave / chopped voltage impulse** (§21, §22) and **prospective peak value** (§23).
- **Rectangular impulse** (§17, §31, §32) — rises rapidly, stays substantially constant, then falls;
  defined by virtual duration of the peak (>90 % of peak) and virtual total duration (>10 % of peak).

The two reference test waveshapes are the **1.2/50 standard lightning voltage impulse** (used for the
[[impulse-sparkover-voltage|impulse-sparkover]] tests, §61) and the **8/20 current impulse** (the
[[nominal-discharge-current|nominal discharge current]] waveshape, §35, used in the
[[residual-voltage-test]] §62 and the [[operating-duty-test]] §64). The high-current
[[current-impulse-withstand-test]] uses a 4/10 impulse; the long-duration test uses substantially
rectangular current impulses up to ~2 000 µs (§63).

**Related:** [[nominal-discharge-current]], [[impulse-sparkover-voltage]], [[discharge-current]],
[[voltage-impulse-sparkover-test]], [[residual-voltage-test]], [[current-impulse-withstand-test]].
