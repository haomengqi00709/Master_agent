---
id: switching-current-impulse
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Switching current impulse of an arrester (§2.32)

A switching current impulse is **the peak value of [[discharge-current]] having a
virtual front time greater than 30 µs but less than 100 µs and a virtual time to
half value on the tail of roughly twice the virtual front time** ([[iec-99-4]]
§2.32). It is a slower, broader surge than the [[lightning-current-impulse]],
representing switching overvoltages on the system (see
[[impulse-waveshape-terminology]]).

The switching current impulse drives the **switching impulse residual voltage
test** (§7.3.3): one switching impulse of each specified value in Table 3 (±5 %) is
applied to each of three samples, and the highest of the three voltages is the
switching-impulse [[residual-voltage]] at that current. The
**switching-impulse protection level** ([[protective-characteristics]] §2.39c) is
the highest voltage measured at the Table 3 currents:

| Arrester classification | Switching peak currents (A) |
|-------------------------|------------------------------|
| 20 000 A, line discharge classes 4 & 5 | 500 and 2 000 |
| 10 000 A, line discharge class 3 | 250 and 1 000 |
| 10 000 A, line discharge classes 1 & 2 | 125 and 500 |

This test is required only for the larger 10 000 A and 20 000 A arresters; it is
*not required* for 5 000 A, 2 500 A and 1 500 A arresters per
[[arrester-classification]] Table 1. The lowest switching-impulse residual voltage
measured feeds the line-discharge-test energy formula (§7.4.2).
