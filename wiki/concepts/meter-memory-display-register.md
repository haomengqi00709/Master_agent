---
id: meter-memory-display-register
type: concept
tags: [concept, iec-387, register]
---

# Memory, display and register

IEC 387 defines the digital-information chain of an electronic meter in three
linked terms (§3.11–3.13):

- **Memory** (§3.11): *element which stores digital information.*
- **Display** (§3.12): *device which displays the content(s) of (a) memory(ies).*
- **Register** (§3.13): *electromechanical or electronic device comprising both
  memory and display which stores and displays information.*

A key architectural note follows §3.13: **a single display may be used with
multiple electronic memories to form multiple registers.** This is what lets a
[[static-energy-meter|static meter]] present several tariff registers
([[multi-rate-meter]]) or import/export registers
([[bidirectional-meter]]) on one display.

The register is the totalising heart of the meter and the reference point for
several other definitions: the [[meter-constant]] (§3.19) relates the energy
*registered* to the test output, and the
[[primary-half-primary-secondary-register|primary / half-primary / secondary
registers]] (§3.14–3.16) classify how a transformer-operated meter's register
accounts for instrument-transformer ratios. The static maximum-demand display
symbols 9.6–9.10 ([[tariff-device-symbols]]) act on register/display content.

See also: [[primary-half-primary-secondary-register]] · [[meter-constant]] ·
[[iec-387]] §3.11–3.13.
