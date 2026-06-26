---
id: distances-through-compound
type: concept
tags: [concept, iec-79-18, ex, encapsulation]
---

# Distances through the compound (encapsulation "m")

A path-length rule that lets the designer avoid assuming the
[[fault-not-considered-components|§5.1.4 single fault]] between bare live parts.
Under IEC 79-18 §5.3, it is **not necessary to consider the possibility of a fault**
between bare live parts that are mechanically fixed relative to each other **before
encapsulating** — provided the distances between them, measured through the
[[encapsulation-compound|compound]], are at least the values of **Table 1**. The rule
covers three pairings: parts of the **same circuit**, a circuit and **earthed
metallic parts**, and **two separate circuits**.

**Table 1 — minimum distance through the compound** (rated insulation voltage,
r.m.s.):

| Rated voltage (V) | Min. distance (mm) |
|------|------|
| 380 | 1 |
| 500 | 1.5 |
| 660 | 2 |
| 1 000 | 2.5 |
| 1 500 | 4 |
| 3 000 | 7 |
| 6 000 | 12 |
| 10 000 | 20 |

The rated voltage may exceed the tabulated value by **10 %** (Table 1 note). Two
limits apply: distances between live parts of encapsulated **electronic assemblies**
(e.g. PCBs) are **not** counted as distances through the compound; and this is
separate from the [[thickness-of-compound|compound thickness over live parts]] (§5.2).

**Related:** [[type-of-protection-m]] · [[fault-not-considered-components]] · [[thickness-of-compound]] · [[free-space-and-voids]]
