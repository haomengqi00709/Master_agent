---
id: residual-voltage
type: concept
tags: [concept, iec-99-1, iec-99-4, surge-arrester]
---

# Residual voltage (discharge voltage) of an arrester

The **residual voltage (discharge voltage) of an arrester** is the voltage that appears between the
terminals of an arrester during the passage of [[discharge-current]] ([[iec-99-1]] §37). After the
[[series-gap|series gaps]] spark over, the [[non-linear-series-resistor]] carries the surge current;
the residual voltage is the voltage the resistor lets through at that current, and it is the voltage
actually impressed on the protected apparatus during a discharge. With the
[[impulse-sparkover-voltage]] it constitutes the [[protective-characteristics-arrester|protective
level]] — the lower the residual voltage, the better the protection. It is therefore the quantity that
insulation co-ordination compares against the withstand strength of the protected insulation (see
[[arrester-application-guide]], [[impulse-protective-level]]).

Residual voltage is characterised by the **residual-voltage / discharge-current curve**, measured in
the [[residual-voltage-test]] (§62). An 8/20 current impulse is applied at peak values of approximately
0.5, 1 and 2 times the [[nominal-discharge-current]], and the maximum envelope of the test points is
drawn as the curve. **The residual voltage read at the nominal discharge current shall not exceed the
maximum residual voltage** tabulated against [[rated-voltage-arrester|rated voltage]] and class in
[[iec-99-1]] **Table VII** (e.g. a 12 kV 10 kA / 5 kA Series A arrester: 43 kV peak). When the test is
made on a [[surge-arrester|section]] rather than a complete arrester, the whole-arrester residual
voltage is the measured value scaled by the ratio of the rated voltages (§62). The residual voltage at
nominal current is also a reference checked before/after the [[operating-duty-test]] and the
long-duration [[current-impulse-withstand-test]] (it must not change by more than 10 %).

## In the gapless metal-oxide standard [[iec-99-4]]
[[iec-99-4]] §2.36 keeps the same definition — *the peak value of voltage that appears between the
terminals of an arrester during the passage of [[discharge-current]]* (the term "discharge voltage"
is used in some countries). Because the [[metal-oxide-surge-arrester]] is gapless, the residual
voltage is governed entirely by the non-linear V–I characteristic of the [[metal-oxide-resistor]],
with no sparkover component. It is obtained per the [[residual-voltage-test]] (§7.3) in three forms —
[[steep-current-impulse|steep]], [[lightning-current-impulse|lightning (8/20)]] and
[[switching-current-impulse|switching]] — that together form the [[protective-characteristics]]
(§2.39). The **maximum residual voltage** for any current/waveshape is derived from the measured
section residual voltage multiplied by a **scale factor** = (declared max residual voltage checked in
routine test) ÷ (measured section residual voltage at the same current) (§5.3, §7.3). Before/after the
[[long-duration-current-impulse-withstand-test]] and [[operating-duty-test]] it must not change by
more than **5 %** (note: 99-4's tolerance is 5 %, vs 99-1's 10 %). Typical maximum residual voltages
are tabulated in Annex K.

**Related:** [[surge-arrester]], [[non-linear-series-resistor]], [[metal-oxide-resistor]],
[[discharge-current]], [[nominal-discharge-current]], [[residual-voltage-test]],
[[impulse-sparkover-voltage]], [[protective-characteristics-arrester]], [[protective-characteristics]],
[[impulse-protective-level]].
