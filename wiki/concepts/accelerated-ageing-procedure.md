---
id: accelerated-ageing-procedure
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Accelerated ageing procedure (§7.5.2)

The accelerated ageing procedure determines the **elevated voltages U_c\* and Uᵣ\***
used in the [[operating-duty-test]] so those tests can be carried out on **new**
resistors yet reproduce the power loss of aged ones ([[iec-99-4]] §7.5.2). It exists
because a gapless [[metal-oxide-surge-arrester]] energizes its
[[metal-oxide-resistor|metal-oxide resistors]] at
[[continuous-operating-voltage|continuous operating voltage]] for its whole life, so
the duty test must anticipate long-term ageing. (The clause is provisional — ageing
of metal-oxide resistors was still under study.)

**Procedure (§7.5.2.1):** three resistor samples are stressed at the **corrected
maximum continuous operating voltage** for **1 000 h** while held at a surface
temperature of **115 °C ±4 °C**, in the medium used in the arrester (closed chamber
≥2× resistor volume). The corrected voltage is
**U_ct = √2·U_c·(1 + 0,05 L)**, where L is the total arrester length in metres,
accounting for voltage unbalance along the column (lower values must be proven by
voltage-distribution measurement/calculation; for multi-unit arresters apply to the
maximum-stressed [[arrester-unit|unit]]).

**Determining the elevated voltages (§7.5.2.2):** resistor power losses P (per-loss)
are measured at U_c/n before ageing and after 1 000 h at the same temperature. If
post-ageing loss ≤ pre-ageing, U_c/n and Uᵣ/n are used unchanged. Otherwise the
worst ratio K of the three samples is found, and on three new resistors the voltages
are increased so the power losses satisfy that ratio — giving the highest values
U_c\* and Uᵣ\*. These elevated voltages then drive the 10 s / 30 min power-frequency
application in the operating-duty test (figures 1, 2, C.1) and the
[[power-frequency-withstand-voltage-vs-time]] verification (Annex D).
