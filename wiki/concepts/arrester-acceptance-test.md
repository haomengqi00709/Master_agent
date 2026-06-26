---
id: arrester-acceptance-test
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Acceptance tests of an arrester (§2.45, §8.2)

Acceptance tests are **tests made when it has been agreed between the manufacturer
and the purchaser that the arresters, or representative samples of an order, are to
be tested** ([[iec-99-4]] §2.45). They sit between the once-per-design
[[arrester-type-test|type tests]] and the per-unit [[arrester-routine-test|routine
tests]]: they verify a delivered batch on a sample basis.

**Standard acceptance tests (§8.2.1)** — when the purchaser specifies them, made on
the **nearest lower whole number to the cube root of the number of arresters
supplied**:
- a) **Power-frequency voltage at the [[reference-current]]** measured on the
  complete arrester (at the bottom), within the manufacturer's specified range;
  for multi-unit arresters the value may deviate from the arrester
  [[reference-voltage]].
- b) **[[lightning-current-impulse|Lightning impulse]] [[residual-voltage]]** on the
  complete arrester or unit (per §7.3), at [[nominal-discharge-current]] if possible
  (tail time need not be complied with); the complete-arrester value (sum of unit
  values) must not exceed the specified value.
- c) **[[partial-discharge-test|Partial discharge test]]**: voltage raised to rated
  voltage, then within 10 s decreased to **1,05 × [[continuous-operating-voltage]]**,
  at which the partial-discharge level (per IEC 270) must **not exceed 50 pC**.

Any change in sample number or test type is negotiated between manufacturer and
purchaser. The **special thermal stability test** (§8.2.2, by additional agreement,
see §5.7) runs part of the operating-duty sequence on three different sections from
routine production to confirm [[thermal-stability]].
