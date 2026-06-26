---
id: arrester-routine-test
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Routine tests of an arrester (§2.44, §8.1)

Routine tests are **tests made on each arrester, or on parts and materials as
required, to ensure that the product meets the design specifications** ([[iec-99-4]]
§2.44) — performed on every unit, unlike the once-per-design
[[arrester-type-test|type tests]]. The minimum routine-test programme (§8.1) is:

- a) **Measurement of [[reference-voltage]]** (U_ref, §2.35, §5.2) — measured values
  within the manufacturer-specified range.
- b) **Residual voltage test** — compulsory for arresters with rated voltage above
  1 kV; performed on complete arresters, units, or a sample of one/several resistor
  elements, at a manufacturer-chosen [[lightning-current-impulse|lightning impulse]]
  current in the range **0,01 to 2 × [[nominal-discharge-current|nominal current]]**.
  The complete-arrester [[residual-voltage]] (sum of element/unit values if not
  directly measured) must not exceed the specified value. *Note:* for 5 000 A and
  2 500 A arresters below 36 kV supplied in volume, this may be omitted by agreement.
- c) **Absence of [[partial-discharge-test|partial discharges]] and contact noise**
  checked on each unit by any sensitive method (per IEC 270).
- d) **[[seal-leakage|Leakage check]]** on each sealed-housing unit.
- e) **[[current-distribution-multi-column|Current distribution test]]** on all
  groups of parallel resistors in multi-column arresters, at a chosen impulse
  current 0,01–1 × nominal (front time ≥7 µs).

For arresters below 36 kV the manufacturer may routine-check only the reference
voltage rather than the residual voltage (§7.3, §8.1b), deriving residual voltages
by the reference-voltage scale factor.
