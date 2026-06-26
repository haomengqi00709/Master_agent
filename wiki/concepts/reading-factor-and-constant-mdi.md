---
id: reading-factor-and-constant-mdi
type: concept
tags: [concept, iec-387, demand]
---

# Reading factor C and constant K of a maximum demand indicator

IEC 387 defines two scaling coefficients for a [[maximum-demand-indicator]]
(§3.20–3.21). The **reading factor C** (§3.20) is *the factor by which it is
necessary to multiply the reading in units of power (active or reactive) in order
to obtain the value of the corresponding power expressed in the same units.* The
**constant K** (§3.21) is *the coefficient by which the reading must be
multiplied to obtain the value of the corresponding power (active or reactive).*

Both convert a raw indicator reading into a true power value; they parallel the
energy-meter [[meter-constant]] (§3.19) which relates registered energy to test
output. C and K matter when the indicator scale is graduated in divisions rather
than direct power units — for example the drum-type MDI in Table 6 with a
multiplier of 0,2 kW/div ([[tariff-device-symbols]], §9 c). They also interact
with transformer ratios: where a meter is fed via instrument transformers
([[transformer-operated-meter-marking]], §8) the demand reading must additionally
be scaled by the transformer multiplying factor.

See also: [[maximum-demand-indicator]] · [[maximum-demand-meter]] ·
[[meter-constant]] · [[iec-387]] §3.20–3.21.
