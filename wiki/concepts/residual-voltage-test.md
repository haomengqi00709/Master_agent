---
id: residual-voltage-test
type: concept
tags: [concept, iec-99-1, iec-99-4, surge-arrester]
---

# Residual voltage test (Type test, §62)

The **residual voltage test** of [[iec-99-1]] §62 measures the
[[residual-voltage|residual (discharge) voltage]] of the arrester as a function of
[[discharge-current]]. It is made (per §55, §59) on **three samples** of complete arresters or
[[surge-arrester|arrester sections]] — which may be the same samples as used for the §60 and §61
sparkover tests. The test-sample voltage rating must be at least 3 kV (if the arrester's rated voltage
is that high) and need not exceed 12 kV.

An **8/20 current impulse** ([[impulse-waveshape]]) is used, with equipment tolerances of 7–9 µs front
and 18–22 µs tail. **Three current impulses are applied to each sample at peak values of approximately
0.5, 1 and 2 times the [[nominal-discharge-current]]**, the sample being allowed to return to ambient
temperature between discharges. The maximum envelope of the test points is drawn as the
**residual-voltage / discharge-current curve**. The pass criterion: **the residual voltage read on
that curve at the nominal discharge current shall not exceed the maximum residual voltage** tabulated
against [[rated-voltage-arrester|rated voltage]] and class in **Table VII** (§62). When the test is
made on a section, the whole-arrester residual voltage is the measured value scaled by the ratio of
the rated voltages of the whole arrester to the section.

The residual-voltage / discharge-current curve is component (b) of the
[[protective-characteristics-arrester|protective characteristics]] (§48), and the residual voltage at
nominal current is a reference checked before and after the [[operating-duty-test]] and the
long-duration [[current-impulse-withstand-test]] (must not change by more than 10 %). It is also,
only when specifically agreed, a [[routine-and-acceptance-tests|standard acceptance test]] (§68).

## In the gapless metal-oxide standard [[iec-99-4]] (§7.3)
For the gapless [[metal-oxide-surge-arrester]], [[iec-99-4]] §7.3 obtains the data to derive the
**maximum [[residual-voltage]]** for all currents/waveshapes. Made on the **same three samples**
(complete arresters or [[arrester-section|sections]]), with enough time between discharges to return to
ambient. It comprises three sub-tests forming the [[protective-characteristics]] (§2.39):
- **§7.3.1 Steep current impulse residual voltage test** — one
  [[steep-current-impulse|1 µs steep impulse]] at peak = [[nominal-discharge-current]] ±5 %; highest of
  three peaks is the steep-current residual voltage. Voltage-measuring-circuit response time ≤20 ns.
- **§7.3.2 Lightning impulse residual voltage test** — one
  [[lightning-current-impulse|8/20 impulse]] at each of ≈0,5×, 1×, 2× Iₙ; maxima plotted as a
  residual-voltage-versus-discharge-current curve; the value at Iₙ is the **lightning impulse
  protection level**.
- **§7.3.3 Switching impulse residual voltage test** — one
  [[switching-current-impulse|switching impulse]] at each Table 3 value (±5 %); highest is the
  switching residual voltage; the maximum is the **switching impulse protection level** (10 000 /
  20 000 A only).

The **maximum residual voltage** for any current/waveshape = measured section residual voltage ×
scale factor (declared max ÷ measured at the routine-test current) (§5.3, §7.3). For arresters below
36 kV the manufacturer may instead scale by the [[reference-voltage]]. The result must not change by
more than **5 %** across the [[long-duration-current-impulse-withstand-test]] / [[operating-duty-test]]
(vs 99-1's 10 %). It is also the lightning-impulse residual-voltage check in the
[[arrester-routine-test]] (§8.1b) and [[arrester-acceptance-test]] (§8.2.1b). Typical maxima: Annex K.

**Related:** [[residual-voltage]], [[nominal-discharge-current]], [[discharge-current]],
[[steep-current-impulse]], [[lightning-current-impulse]], [[switching-current-impulse]],
[[impulse-waveshape]], [[protective-characteristics-arrester]], [[protective-characteristics]],
[[arrester-type-test]], [[type-test]].
