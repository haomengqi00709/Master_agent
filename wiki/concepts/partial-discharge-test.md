---
id: partial-discharge-test
type: concept
tags: [concept, iec-56, iec-99-4, circuit-breaker, surge-arrester]
---

# Partial discharge test

The partial-discharge test detects internal discharges in insulation that would otherwise degrade it over time. Per [[iec-56]] 6.1.9 (with IEC 694 6.1.9), no partial-discharge test is required on the complete circuit-breaker. However, where the breaker uses components for which a relevant IEC publication prescribes partial-discharge measurement — for example bushings to IEC 137 (Bushings for Alternating Voltages above 1000 V) — the manufacturer must produce evidence that those components have passed the partial-discharge tests laid down in the applicable component standard ([[iec-56]] 6.1.9). It is grouped under the dielectric [[type-test]]s alongside the [[dielectric-test]] and [[radio-interference-voltage-test]], supporting the [[rated-insulation-level]].

**For metal-oxide surge arresters ([[iec-99-4]]):** by contrast, a partial-discharge test *is*
required. Per [[iec-99-4]] §5.4 the internal partial discharges in the arrester energized at
**1,05 × [[continuous-operating-voltage]]** shall **not exceed 50 pC** (measured per IEC 270). It is a
[[arrester-routine-test|routine-test]] check (absence of PD and contact noise on each unit, §8.1c) and
a standard [[arrester-acceptance-test|acceptance test]] (§8.2.1c, voltage raised to rated then dropped
to 1,05·U_c within 10 s), as well as type-test item 8 of the [[arrester-type-test]] programme.
