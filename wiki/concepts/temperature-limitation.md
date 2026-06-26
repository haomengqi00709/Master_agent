---
id: temperature-limitation
type: concept
tags: [concept, iec-79-18, ex, encapsulation]
---

# Temperature limitation (encapsulation "m")

The thermal-safety requirement of [[type-of-protection-m|encapsulation "m"]]
(IEC 79-18 §5.4). In normal service, **none** of the following may be exceeded: the
marked **maximum surface temperature**, the **temperature class**, or the
[[continuous-operating-temperature|continuous operating temperature of the compound]].
Exceeding any of these would risk igniting the atmosphere by heating or degrading the
[[encapsulation-compound|compound]] that provides the protection.

Beyond normal service, the apparatus, parts or [[ex-component-encapsulation|Ex
components]] **shall be protected** so that under the electrical-fault conditions of
§5.1.3 (prospective short-circuit current, default 4 000 A) and the single-fault
conditions of §5.1.4 the type of protection "m" is not affected. This may be achieved
by a **non self-resetting** internal or external, electrical or thermal protecting
device; a self-resetting device may be added *in addition* but cannot be the sole
means.

Compliance is demonstrated by the [[thermal-tests]] of §8.2.1 — the maximum-temperature
test (8.2.1.1) confirms the §5.4 limits hold in normal service and that the maximum
surface temperature is not exceeded under §5.1.4 faults, and the
[[thermal-cycling-test]] (8.2.1.2) confirms the internal temperature stays within the
continuous operating temperature. The [[encapsulated-fuses|fuse exception]] (§6.2)
allows transient over-temperature on rupture only if the protection and marked surface
temperature are preserved.

**Related:** [[type-of-protection-m]] · [[continuous-operating-temperature]] · [[temperature-range-of-the-compound]] · [[thermal-tests]] · [[thermal-cycling-test]] · [[fault-not-considered-components]]
