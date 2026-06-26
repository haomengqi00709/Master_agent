---
id: steep-current-impulse
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Steep current impulse (§2.16)

A steep current impulse is **a current impulse with a virtual front time of 1 µs,
with equipment-adjustment limits such that the measured values are from 0,9 µs to
1,1 µs** ([[iec-99-4]] §2.16). The virtual time to half value on the tail shall be
**not longer than 20 µs**, and — per the note — during the
[[residual-voltage-test]] the tail time is not critical and may have any tolerance.
It is the fastest-fronted of the standard's test waves (see
[[impulse-waveshape-terminology]]).

The steep current impulse drives the **steep current impulse residual voltage
test** (§7.3.1): one steep impulse with peak equal to the
[[nominal-discharge-current]] (±5 %) is applied to each of three samples, the three
voltage peaks recorded, and the highest taken as the steep-current
[[residual-voltage]]. Because the front is so fast, the voltage measuring circuit
must have response times not exceeding 20 ns (per IEC 60-3). The resulting
residual voltage for a steep impulse is element (a) of the arrester's
[[protective-characteristics]] (§2.39a) and a characteristic quoted in tenders
(Annex G).
