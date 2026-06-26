---
id: primary-half-primary-secondary-register
type: concept
tags: [concept, iec-387, register]
---

# Primary, half-primary and secondary registers

For a meter fed through instrument transformers, IEC 387 classifies the
[[meter-memory-display-register|register]] by how much of the transformer ratio
it builds in (§3.14–3.16):

- **Primary register** (§3.14): register which **takes into account the ratios of
  all the transformers** (voltage and current) to which the meter is connected.
  The primary-side energy is read **directly** from the register (NOTE to §3.14).
- **Half-primary register** (§3.15): register which takes into account **either**
  the current-transformer ratio(s) **or** the voltage-transformer ratio(s), **but
  not both**. The primary-side value is the reading **multiplied by an appropriate
  factor**.
- **Secondary register** (§3.16): register which **takes no account** of the
  transformer ratio(s). Again the primary value is the reading times an
  appropriate factor.

This classification drives the §8 marking scheme
([[transformer-operated-meter-marking]]): ratios *accounted for* by the register
are marked on the name-plate/dial; ratios *not accounted for* go on a
supplementary plate on the cover (for half-primary and secondary registers),
together with the multiplying factor. Table 5 gives worked examples for each
register type (e.g. secondary: 50/5 A, 10 000/100 V on the supplementary plate,
multiplying factor = 1 000).

See also: [[meter-memory-display-register]] ·
[[transformer-operated-meter-marking]] · [[iec-387]] §3.14–3.16, §8.
