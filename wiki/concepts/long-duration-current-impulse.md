---
id: long-duration-current-impulse
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Long duration current impulse (§2.18)

A long-duration current impulse is **a rectangular impulse which rises rapidly to
its maximum value, remains substantially constant for a specified period, and then
falls rapidly to zero** ([[iec-99-4]] §2.18). The parameters defining such a
rectangular impulse are polarity, peak value, **virtual duration of the peak**
(time above 90 % of peak) and **virtual total duration** (time above 10 % of peak)
— see [[impulse-waveshape-terminology]] §2.26–2.27. It represents the discharge of
a charged transmission line (a long, flat-topped energy pulse) rather than a fast
lightning stroke.

This wave is the basis of the [[long-duration-current-impulse-withstand-test]]
(§7.4). For the larger 10 000 A / 20 000 A arresters it is produced by the
**[[line-discharge-class]]** test (§7.4.2, Table 4), simulating discharge of a
precharged line of defined surge impedance, peak duration and charging voltage. For
5 000 A / 2 500 A arresters it is the **long-duration impulse test** of §7.4.3
(Table 5): peak current 75 A over 1 000 µs for 5 000 A, and 50 A over 500 µs for
2 500 A, with the virtual peak duration 100–120 % of table value and total duration
≤150 % of peak duration. It also forms the impulse pair in the **switching-surge**
[[operating-duty-test|operating duty test]] (§7.5.5).
