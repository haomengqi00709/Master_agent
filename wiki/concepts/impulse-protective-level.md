---
id: impulse-protective-level
type: concept
tags: [concept, iec-99-1, surge-arrester]
---

# Impulse protective level and protective ratio

These are the application-side characterisations of an arrester's protection, introduced by
**Publication 99-1A (1962)** and carried into Appendix C of the 1970 second edition of [[iec-99-1]]
(§6 of 99-1A, "New definitions"):

- **Impulse protective level of an arrester** (99-1A §6.1) — the highest peak value of impulse voltage
  that may occur across the terminals of an arrester under the prescribed conditions. It is given
  numerically by the **maximum** of three quantities:
  - the front-of-wave [[impulse-sparkover-voltage]] **divided by 1.15**,
  - the **1.2/50** ([[impulse-waveshape]]) sparkover voltage, and
  - the [[residual-voltage|residual (discharge) voltage]] at a given [[discharge-current]].
- **Rated impulse protective level of an arrester** (99-1A §6.2) — the impulse protective level with
  the residual voltage referred to the [[nominal-discharge-current]].
- **Protective ratio** (99-1A §6.3) — the ratio of the insulation withstand characteristic of the
  protected equipment to the arrester protective level.

The protective level condenses the arrester's [[protective-characteristics-arrester|protective
characteristics]] (§48) into a single voltage to compare against insulation withstand strength. The
[[arrester-application-guide]] requires a minimum **protective ratio of 1.2** between the impulse
withstand strength of the equipment and the impulse protective level achieved at it. (99-1A §6 footnote
notes IEC Publication 60 gives the standard wave as 1.2/50, replacing the older 1/50 of the 1958
edition of 99-1.) **Amended:** the entire protective-level / protective-ratio framework is the
substantive addition of the 99-1A amendment.

**Related:** [[arrester-application-guide]], [[protective-characteristics-arrester]],
[[impulse-sparkover-voltage]], [[residual-voltage]], [[nominal-discharge-current]],
[[impulse-waveshape]].
