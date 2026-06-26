---
id: nominal-discharge-current
type: concept
tags: [concept, iec-99-1, iec-99-4, surge-arrester]
---

# Nominal discharge current of an arrester

The **nominal discharge current of an arrester** is the peak value of [[discharge-current]], having
an **8/20 waveshape** ([[impulse-waveshape]]), which is used to classify an arrester; it is also the
discharge current used to initiate follow current in the [[operating-duty-test]] ([[iec-99-1]] §35).
It is the single most important classifying rating: arresters are classified by their standard
nominal discharge currents and must meet at least the test requirements and performance
characteristics of Table I for their class (§54). The nominal current must appear on the
[[arrester-identification|rating plate]] (§50), specifying for the 5 000 A arrester whether Series A
or B, and for the 10 000 A arrester whether light- or heavy-duty.

**Standard nominal discharge currents** are **10 000 A, 5 000 A, 2 500 A and 1 500 A**, all with an
8/20 waveshape (§53). The classes subdivide further (Table I, §54):

| Class | Sub-type | Voltage-rating coverage |
|-------|----------|-------------------------|
| 10 000 A | light-duty / heavy-duty | 3 kV or more |
| 5 000 A | Series A | 3 kV through 138 kV |
| 5 000 A | Series B | 3 kV through 39 kV |
| 2 500 A | — | up to 36 kV |
| 1 500 A | — | up to 0.660 kV |

Series A characteristics reflect practice in all countries; Series B reflects practice in Canada,
USA and other countries. The 10 000 A light/heavy distinction is by the long-duration impulse
current the arrester withstands (§63.3). The nominal current sets the reference point for the
[[residual-voltage-test]] (residual voltage measured at 0.5×, 1× and 2× nominal current, §62) and is
the impulse peak in the [[operating-duty-test]] (§64). Higher-class arresters (10 000 A) give the
best [[protective-characteristics-arrester|protective levels]].

## In the gapless metal-oxide standard [[iec-99-4]]
[[iec-99-4]] §2.30 keeps the same definition — the peak value of [[lightning-current-impulse]]
(8/20) used to **classify** the arrester (§3.2). The **standard nominal 8/20 discharge currents add
the 20 000 A class**: they are **20 000 A, 10 000 A, 5 000 A, 2 500 A and 1 500 A** (§4.3). Per
[[arrester-classification]] Table 1 each maps to a rated-voltage range (e.g. 20 000 A for
360 < Uᵣ ≤ 756 kV; 10 000 A for 3 ≤ Uᵣ ≤ 360 kV; 5 000 A for Uᵣ ≤ 132 kV; 2 500 A for Uᵣ ≤ 36 kV).
For the 10 000 A and 20 000 A arresters there are five [[line-discharge-class|line-discharge
classes]] differentiated by long-duration energy capability. In 99-4 the nominal current is also the
reference peak for the [[residual-voltage-test]] (measured at ≈0,5×, 1×, 2× Iₙ, §7.3.2; the residual
voltage at Iₙ is the lightning-impulse [[protective-characteristics|protection level]]) and the
conditioning impulse peak in the [[operating-duty-test]] (§7.5.4.1). It must appear on the nameplate
([[arrester-identification]] §3.1).

**Related:** [[surge-arrester]], [[discharge-current]], [[lightning-current-impulse]],
[[residual-voltage]], [[operating-duty-test]], [[line-discharge-class]], [[arrester-classification]],
[[arrester-identification]], [[arrester-application-guide]].
