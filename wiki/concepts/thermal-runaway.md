---
id: thermal-runaway
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Thermal runaway of an arrester (§2.40)

Thermal runaway describes **a situation when the sustained power loss of an arrester
exceeds the thermal dissipation capability of the housing and connections, leading
to a cumulative increase in the temperature of the resistor elements culminating in
failure** ([[iec-99-4]] §2.40). It is the characteristic failure mode of a gapless
[[metal-oxide-surge-arrester]]: because the [[metal-oxide-resistor|metal-oxide
resistors]] are energized continuously at [[continuous-operating-voltage]], any
positive feedback between resistor temperature and resistive
[[continuous-current|leakage current]] can spiral until the resistors fail. It is
the inverse condition of [[thermal-stability]].

Preventing thermal runaway is the central objective of the [[operating-duty-test]]
(§5.9, §7.5): after the impulse stresses, elevated rated and continuous voltages
(Uᵣ\*, U_c\*) are applied for 10 s and 30 min to prove the arrester cools down
rather than runs away. The whole point of the [[accelerated-ageing-procedure]]
(§7.5.2) is to set those elevated test voltages so the duty test is run on new
resistors at the same power loss as aged ones — the worst case for runaway. The
[[power-frequency-withstand-voltage-vs-time]] characteristic (§2.37, §5.10) bounds
the voltage/time combinations that may be applied without runaway, and runaway is
the failure judged in the [[thermal-stability-evaluation]] (§7.5.6).
