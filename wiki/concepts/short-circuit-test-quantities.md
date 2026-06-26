---
id: short-circuit-test-quantities
type: concept
tags: [concept, iec-56, circuit-breaker]
---

# Short-circuit test quantities

Sub-clause 6.104 of [[iec-56]] fixes the electrical quantities for each [[short-circuit-test]]. Unless a tolerance is given, tests must be no less severe than the specified values. Applied voltage before making tests is U/sqrt(3) (phase-to-earth) for single-phase, averaging U/sqrt(3) for three-phase, not exceeding +10% (6.104.1). The short-circuit breaking current is stated as the average r.m.s. a.c. component in all phases plus the percentage maximum d.c. component, measured at contact separation per Figure 8, with the a.c. component not below 90% at final arc extinction (6.104.3-6.104.4). The prospective [[transient-recovery-voltage]] is specified by reference, delay and ITRV lines via two- or four-parameter envelopes, with standard values tabulated per duty and rated voltage (6.104.5, Tables II/XIV-XVII). Power-frequency recovery voltage equals U/sqrt(3) (or x first-pole-to-clear factor), held at least 0.1 s at 95% or more (6.104.7). See [[test-duty]], [[short-circuit-test-procedure]].

**Amended (1992, Amd. 1):** [[iec-56-amendment-1]] replaces 6.104.2 (peak making current — proven in test-duty No. 4, two extreme pre-strike cases per Figure 1, with new three-phase and single-phase procedures; see [[rated-short-circuit-making-current]]), deletes the last paragraph of 6.104.3 (breaking current) and the third paragraph of 6.104.7 (power-frequency recovery voltage).
