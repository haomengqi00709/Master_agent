---
id: lightning-current-impulse
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Lightning current impulse (§2.17)

A lightning current impulse is **an 8/20 current impulse**, with equipment-adjustment
limits such that the measured values are **7 µs to 9 µs for the virtual front time
and 18 µs to 22 µs for the time to half value on the tail** ([[iec-99-4]] §2.17).
During the [[residual-voltage-test]] the tail (half-value) time is not critical and
may have any tolerance (note). It is the canonical lightning-surge test wave (see
[[impulse-waveshape-terminology]] for 8/20 designation).

The 8/20 lightning current impulse is the wave whose **peak value is the
[[nominal-discharge-current]]** (Iₙ) that classifies the arrester (§2.30, §4.3). It
drives the **lightning impulse residual voltage test** (§7.3.2): one impulse at
each of ≈0,5×, 1× and 2× Iₙ is applied to three samples, and the maximum
[[residual-voltage|residual voltages]] are plotted as a residual-voltage-versus-
discharge-current curve; the value read at Iₙ is the **lightning impulse protection
level** (element (b) of [[protective-characteristics]], §2.39b). The same 8/20
impulse is the conditioning wave of the [[operating-duty-test]] (twenty impulses at
Iₙ, §7.5.4.1) and the impulse used in the [[arrester-routine-test]] /
[[arrester-acceptance-test]] residual-voltage checks (§8.1b, §8.2.1b).
