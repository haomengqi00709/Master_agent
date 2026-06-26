---
id: arrester-disconnector
type: concept
tags: [concept, iec-99-1, iec-99-4, surge-arrester]
---

# Arrester disconnector

An **arrester disconnector** is a device for disconnecting an arrester from the system in the event of
arrester failure, to prevent a persistent fault on the system and to give visible indication of the
failed arrester ([[iec-99-1]] §49). Clearing of the fault current through the arrester during
disconnection is generally *not* a function of the device, and it may not prevent explosive shattering
of the housing following internal flashover on high fault currents — that is the role of the
[[pressure-relief-device]] (§9). The disconnector is therefore a fault-isolation and indication
device, not a current-interrupter or pressure-relief means.

The disconnector is verified by the [[arrester-disconnector-test|tests of arrester disconnectors]]
(§66). The device must **withstand without operating** the high-current impulse test (per §63.2), the
long-duration current impulse test (per §63.3) and the [[operating-duty-test]] (§64) corresponding to
the highest arrester class it is rated for (§66.2). A **time/current characteristic** is then
established (§66.3) at three symmetrically initiated current levels — 20 A, 200 A and 800 A r.m.s. —
to define how quickly it disconnects under fault. Effective and permanent disconnection must be
demonstrated; if in doubt, a power-frequency voltage of 1.2 times the rated voltage of the highest-
rated associated arrester is applied for one minute, during which current must not exceed 1 mA r.m.s.
(§66.3.1). When an arrester has a built-in disconnector, the §63 and §64 type tests are made with the
disconnector in operable condition.

**In the gapless metal-oxide standard [[iec-99-4]]:** the definition is identical (§2.42). The
requirement is **§5.12** and the tests are **§7.6**: the disconnector must withstand *without
operating* the [[long-duration-current-impulse-withstand-test]] (§7.6.2.1) and the
[[operating-duty-test]] (§7.6.2.2), and a time-versus-current curve is taken at the same three r.m.s.
levels — **20 A, 200 A, 800 A** (±10 %), ≥5 samples each (§7.6.3). The 1,2 × rated-voltage / 1 mA
confirmation (§7.6.3.2) matches 99-1. It applies to all classes of [[arrester-classification]] Table 1
when fitted.

**Related:** [[surge-arrester]], [[arrester-disconnector-test]], [[pressure-relief-device]],
[[operating-duty-test]], [[long-duration-current-impulse-withstand-test]], [[current-impulse-withstand-test]].
