---
id: intrinsically-safe-circuit
type: concept
tags: [concept, iec-79-3, ex, intrinsic-safety]
---

# Intrinsically-safe circuit

A circuit in which **no spark and no thermal effect** produced under the test
conditions prescribed in **IEC 79-11** — which include normal operation and
specified fault conditions — is capable of causing **ignition of a given
explosive gas atmosphere** ([[iec-79-3]] §3.1). This is the core object that
IEC 79-3's apparatus exists to test: a circuit qualifies as intrinsically safe
only if, with its parameters set to the prescribed safety factor, the
[[spark-test-apparatus]] produces no ignition within the defined number of
operations (see [[safety-factor-and-ignition-criterion]]).

Unlike enclosure-based protection (flameproof "d", pressurization "p"), intrinsic
safety limits the **energy available in the circuit itself** so that even sparks
and hot spots arising in normal use or under fault cannot ignite the surrounding
gas. It is the defining concept of [[type-of-protection-i|type of protection "i"]]
and the reason the spark test must reproduce worst-case make- and break-sparks in
the [[explosive-test-mixture|explosive test mixture]]. The scope of IEC 79-3 is
limited to circuits whose **rated current does not exceed 2 A** (see
[[spark-test-apparatus-limitations]]).

**Related:** [[intrinsically-safe-system]] · [[explosive-gas-atmosphere]] ·
[[spark-ignition-test-principle]] · [[type-of-protection-i]]
