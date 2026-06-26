---
id: safety-factor-and-ignition-criterion
type: concept
tags: [concept, iec-79-3, ex, intrinsic-safety]
---

# Safety factor and ignition criterion

Two linked ideas that turn a spark test into a pass/fail judgement of intrinsic
safety. Under the test principle ([[iec-79-3]] §4.1), **the parameters of the
circuit are adjusted to achieve a prescribed safety factor** (defined in **IEC
79-11, sub-clause 9.1.5**) before the test is run — i.e. the circuit's voltage,
current or stored energy is deliberately raised above its rated/fault condition by
that factor, so the test probes a margin rather than the nominal case.

The **ignition criterion** is then: with the circuit at this elevated condition,
the [[spark-test-apparatus]] is operated and one observes **whether or not
ignition of the [[explosive-test-mixture|explosive test mixture]] takes place
within a defined number of operations** of the [[contact-mechanism]] (counted as
revolutions of the wire holder). No ignition within that count ⇒ the circuit meets
[[intrinsically-safe-circuit|intrinsic safety]] for that gas group; an ignition ⇒
it fails. The "test current" used in the safety check is the rated current after
allowing for faults, **multiplied by the safety factor**; the standard warns that
if this exceeds roughly **2,5 A to 3 A** the tungsten wires heat enough to add
spurious ignition effects that invalidate the result (see
[[spark-test-apparatus-limitations]]). The Annex A conditioning procedure embodies
a related "lowest ignition voltage" criterion used to verify apparatus sensitivity
(see [[cadmium-disc-conditioning]]).

**Related:** [[spark-ignition-test-principle]] · [[spark-test-apparatus]] ·
[[explosive-test-mixture]] · [[spark-test-apparatus-limitations]]
