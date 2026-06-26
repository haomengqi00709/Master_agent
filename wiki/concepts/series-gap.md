---
id: series-gap
type: concept
tags: [concept, iec-99-1, surge-arrester]
---

# Series gap of an arrester

The **series gap of an arrester** is an intentional gap or gaps between spaced electrodes in series
with the non-linear series resistor or resistors of the arrester ([[iec-99-1]] §5). It is the element
that holds off normal power-frequency voltage so that the [[non-linear-series-resistor]] carries no
continuous current, and that **sparks over** ([[power-frequency-sparkover-voltage|sparkover]],
§15: a disruptive discharge between the electrodes of the gaps) when an overvoltage arrives,
connecting the resistor across the line to pass the [[discharge-current]]. The gap arrangement also
governs interruption: after the surge, the gap must reseal and extinguish the
[[follow-current]] at a current zero. The definition of [[surge-arrester]] (§3) explicitly includes
any *external* series gap essential to proper functioning, whether or not supplied as an integral
part of the device.

Series gaps may be plain or **current-limiting (high arc-voltage)** gaps; the latter do not permit
the full rectangular long-duration current impulse to be maintained, which is why the
[[current-impulse-withstand-test]] for heavy-duty 10 000 A arresters (§63.3.2) and the
[[operating-duty-test]] (§64) include special provisions for such gaps. Sparkover behaviour is
quantified by the [[power-frequency-sparkover-voltage]] (§38) and the various
[[impulse-sparkover-voltage]] characteristics (§39–§43), and verified by the
[[power-frequency-sparkover-test]] and [[voltage-impulse-sparkover-test]]. The graphical symbol for
a gap is [[07-22-01]] (a double spark gap is [[07-22-02]]).

**Related:** [[surge-arrester]], [[non-linear-series-resistor]], [[power-frequency-sparkover-voltage]],
[[follow-current]].
