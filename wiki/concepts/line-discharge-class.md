---
id: line-discharge-class
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Line discharge class (§7.4.2, Annex E)

The line discharge class is the **energy-capability grading** of 10 000 A and
20 000 A [[metal-oxide-surge-arrester|metal-oxide arresters]], expressing how much
energy from a discharging transmission line the arrester can absorb. There are
**five classes (1–5) of increasing discharge requirement** ([[iec-99-4]] §7.4.2,
note to Table 4; §3.2 note). Each class fixes the parameters of the
[[long-duration-current-impulse-withstand-test|line discharge test]] (Table 4),
expressed relative to the test sample's [[arrester-rated-voltage|rated voltage]]
U_n:

| Class | Arrester | Line surge impedance Z | Virtual peak duration T (µs) | Charging voltage U_L |
|-------|----------|------------------------|------------------------------|----------------------|
| 1 | 10 000 A | 4,9·U_n | 2 000 | 3,2·U_n |
| 2 | 10 000 A | 2,4·U_n | 2 000 | 3,2·U_n |
| 3 | 10 000 A | 1,3·U_n | 2 400 | 2,8·U_n |
| 4 | 20 000 A | 0,8·U_n | 2 800 | 2,6·U_n |
| 5 | 20 000 A | 0,5·U_n | 3 200 | 2,4·U_n |

(U_n = rated voltage of the test sample, kV r.m.s.) Class determines which
[[operating-duty-test]] applies: class 1 takes the high-current duty test (§7.5.4),
classes 2–5 the switching-surge duty test (§7.5.5). The injected energy
W ≈ (U_L − U_res)·(U_res/Z)·T depends strongly on the actual
[[switching-current-impulse|switching impulse]] [[residual-voltage]].

**Selection (Annex E, informative):** determine the energy generated in service
(lightning and/or switching), divide by the r.m.s. rated voltage to get the
*specific energy* (kJ per kV rating), compare with the specific energy of the test
(formula 1 / figure E.1, parametrised by class against the ratio of switching
residual voltage to rated voltage), and select the **next higher** class. The line
discharge class (or [[high-lightning-duty-arrester|HLD]] type) may be marked on the
nameplate ([[arrester-identification]]).
