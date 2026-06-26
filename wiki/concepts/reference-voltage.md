---
id: reference-voltage
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Reference voltage of an arrester (U_ref)

The reference voltage of an arrester is **the peak value of power-frequency voltage
divided by √2 which shall be applied to the arrester to obtain the
[[reference-current]]** ([[iec-99-4]] §2.35). For a multi-unit arrester it is the
**sum** of the reference voltages of the individual [[arrester-unit|units]].
Measuring it (at the reference current, §6.2) is necessary for selecting a correct
test sample in the [[operating-duty-test]] (note to §2.35).

Reference voltage is the arrester's basic power-frequency operating-point marker.
The corresponding requirement (§5.2) is that each arrester's reference voltage be
measured by the manufacturer at the chosen reference current, and the **minimum**
reference voltage at the routine-test reference current be specified and published.
It governs test-sample selection: the line-discharge and operating-duty test
samples must have a reference voltage at the **lowest end** of the manufacturer's
declared range (§6.3), and the test-section reference voltage should equal
k·Uᵣ/n, where k is the ratio of minimum reference voltage to
[[arrester-rated-voltage|rated voltage]] and n the section count (§6.3b). For
arresters rated **below 36 kV**, the manufacturer may check only the reference
voltage (not the residual voltage) in routine tests, deriving residual voltages by
the reference-voltage scale factor (§5.3 note, §7.3, §8.1b). Measurement of
reference voltage (or power-frequency voltage at reference current) is the first
[[arrester-routine-test]] (§8.1a) and a standard [[arrester-acceptance-test]]
(§8.2.1a).
