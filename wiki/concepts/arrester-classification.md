---
id: arrester-classification
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Arrester classification (§3.2, Table 1)

Surge arresters are **classified by their standard
[[nominal-discharge-current|nominal discharge currents]]**, and each class must meet
at least the test requirements and performance characteristics of **Table 1**
([[iec-99-4]] §3.2). The five standard classes and their
[[arrester-rated-voltage|rated-voltage]] (Uᵣ) ranges are:

| Nominal discharge current | Rated-voltage range Uᵣ (kV) |
|---------------------------|------------------------------|
| 20 000 A | 360 < Uᵣ ≤ 756 |
| 10 000 A | 3 ≤ Uᵣ ≤ 360 |
| 5 000 A | Uᵣ ≤ 132 |
| 2 500 A | Uᵣ ≤ 36 |
| 1 500 A | low-voltage range, under consideration |

For 10 000 A and 20 000 A arresters there are **five [[line-discharge-class|line
discharge classes]]** (1–5) differentiated by the amplitude and duration of the
long-duration current they withstand (Table 4, §7.4.2). Table 1 maps each class to
its required tests: [[insulation-withstand-test|insulation withstand]] (§7.2.x),
[[residual-voltage-test|residual voltage]] (steep §7.3.1 / lightning §7.3.2 /
switching §7.3.3 — switching only for 10 000/20 000 A),
[[long-duration-current-impulse-withstand-test|long-duration]] (§7.4.2 line-discharge
for 10/20 kA, §7.4.3 for 5 000/2 500 A, not required for 1 500 A),
[[operating-duty-test|operating duty]] (high-current §7.5.4 or switching-surge
§7.5.5), [[power-frequency-withstand-voltage-vs-time|power-frequency V-t]] (§5.10),
[[pressure-relief]] (§5.11, when fitted), [[arrester-disconnector]] (§5.12, when
fitted), and the polluted-housing test (Annex F).

Some countries informally call 10 000 A arresters **station**, 5 000 A
**intermediate/distribution**, and 1 500 A **secondary** (note 2 to Table 1).
Annex C adds a [[high-lightning-duty-arrester|High Lightning Duty]] 20 000 A class
for 1 kV–52 kV. Identification quantities appear on the nameplate per
[[arrester-identification]].
