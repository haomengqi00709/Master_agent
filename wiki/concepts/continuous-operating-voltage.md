---
id: continuous-operating-voltage
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Continuous operating voltage of an arrester (U_c)

The continuous operating voltage (U_c, often written MCOV) is **the designated
permissible r.m.s. value of power-frequency voltage that may be applied
continuously between the arrester terminals**, in accordance with the
[[operating-duty-test]] (§7.5) ([[iec-99-4]] §2.9). Because a
[[metal-oxide-surge-arrester]] has no series spark gap, its
[[metal-oxide-resistor|metal-oxide resistors]] are energized at U_c continuously
for the whole service life — they must withstand this without thermal runaway.
U_c is therefore the voltage that the [[accelerated-ageing-procedure]] (§7.5.2)
simulates the long-term effect of: ageing is done at the **corrected maximum
continuous operating voltage** U_ct = √2·U_c·(1 + 0,05 L), where L is the arrester
length in metres, to account for voltage unbalance along the column (§7.5.2.1).

U_c is the heading nameplate quantity ([[arrester-identification]] §3.1) and the
voltage at which the [[continuous-current]] is defined (§2.33). In the
operating-duty test, U_c is divided by n to U_c/n per section, raised to the
**elevated continuous operating voltage U_c\*** (§7.5.2.2) and applied for 30 min
to prove [[thermal-stability]] / detect [[thermal-runaway]]. The conditioning
impulses are applied superimposed on 1,2 × U_c (§7.5.4.1), and the
[[partial-discharge-test]] is performed at 1,05 × U_c (§5.4). Normal service
requires the applied power-frequency voltage **not to exceed U_c** (§4.4.1e).
Contrast with [[arrester-rated-voltage]] (Uᵣ), the *temporary-overvoltage* rating.
