---
id: spark-test-apparatus-limitations
type: concept
tags: [concept, iec-79-3, ex, intrinsic-safety]
---

# Limitations of the spark-test apparatus

The boundaries of applicability of the [[spark-test-apparatus]] ([[iec-79-3]]
§4.4). It is suitable for testing [[intrinsically-safe-circuit|intrinsically-safe
circuits]] with:

- **rated current not exceeding 2 A**;
- **test voltage in resistive or capacitive circuits not exceeding 300 V**;
- **inductance in inductive circuits not exceeding 1 H**.

**Note 1 — heating limit.** If the **test current** — the rated current after
allowing for faults, **multiplied by the safety factor** (IEC 79-11 9.1.5, see
[[safety-factor-and-ignition-criterion]]) — exceeds some value in the range
**2,5 A to 3 A**, the temperature rise of the
[[tungsten-wire-electrode|tungsten wires]] may produce additional ignition effects
that invalidate the test results.

**Note 2 — time constants.** With capacitive and inductive circuits, take care
that **circuit time constants do not adversely affect the results**. Circuits with
large time constants may be tested, for example by **reducing the speed at which
the apparatus is driven** or — **for capacitive circuits only** — by **removing two
or three of the tungsten wires**. However, reducing the drive speed **may change
the apparatus's sensitivity**, so it is not a free remedy.

The 2 A scope ceiling matches IEC 79-3 §1; SC 31G work continued on testing
circuits with rated current above 2 A.

**Related:** [[spark-test-apparatus]] · [[safety-factor-and-ignition-criterion]] ·
[[tungsten-wire-electrode]] · [[contact-mechanism]]
