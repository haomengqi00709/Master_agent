---
id: follow-current
type: concept
tags: [concept, iec-99-1, surge-arrester]
---

# Follow current of an arrester

The **follow current of an arrester** is the current from the connected power source which flows
through an arrester following the passage of [[discharge-current]] ([[iec-99-1]] §36). Once a surge
has caused the [[series-gap|series gaps]] to spark over and the [[discharge-current]] has been
diverted, the power system continues to drive current through the now-conducting path at power
frequency. The defining function of a [[non-linear-resistor-type-arrester|valve-type arrester]] is to
**interrupt this follow current**: the [[non-linear-series-resistor]] presents a high resistance at
normal power-frequency voltage, limiting the follow-current magnitude, and the series gaps then
reseal and extinguish it at a current zero, restoring the arrester to its non-conducting state. The
scope (§1) states the arrester is designed both to limit voltage surges and to **interrupt power
follow current**, and §3 notes the arrester limits the duration and frequently the amplitude of
follow current.

Successful follow-current interruption is what the [[operating-duty-test]] (§64) demonstrates: the
energized arrester is struck with twenty [[nominal-discharge-current|nominal-current]] impulses; each
must **establish** follow current and the arrester must **interrupt** it every time. The source
impedance is set so the power-frequency voltage at the terminals does not fall below the peak
[[rated-voltage-arrester|rated voltage]] during follow current, nor exceed it by more than 10 % after
interruption. The ability to reseal against the rated voltage is also why the rating must be chosen at
least equal to the highest phase-to-earth voltage (see [[arrester-application-guide]]); prolonged
overvoltage that prevents resealing is a recognised cause of arrester failure under certain switching
surges.

**Related:** [[surge-arrester]], [[discharge-current]], [[series-gap]],
[[non-linear-series-resistor]], [[operating-duty-test]], [[rated-voltage-arrester]].
