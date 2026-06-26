---
id: reference-current
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Reference current of an arrester (§2.34)

The reference current is **the peak value (the higher peak value of the two
polarities if the current is asymmetrical) of the resistive component of a
power-frequency current used to determine the [[reference-voltage]] of the
arrester** ([[iec-99-4]] §2.34). It is chosen high enough that the effects of stray
capacitance on the measured reference voltage of the arrester units (with their
[[internal-grading-system|designed grading system]]) become negligible, and is
**specified by the manufacturer**.

The reference current pins down the operating point at which the
[[reference-voltage]] is measured — and reference voltage is what selects a correct
test sample for the [[operating-duty-test]] (§7.5) and the
[[line-discharge-class|line discharge test]] (§7.4.2). Per the note to §2.34, the
reference current is typically in the range **0,05 mA to 1,0 mA per square
centimetre of disc area** for single-column arresters, depending on the
[[nominal-discharge-current]] and/or [[line-discharge-class]]. It is measured at an
ambient temperature of 20 °C ±15 °C (§6.2), with the resistive peak approximated by
the momentary current value at the instant of voltage peak.
