---
id: arrester-section
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Section of an arrester

A section of an arrester is **a complete, suitably assembled part of an arrester
necessary to represent the behaviour of a complete arrester with respect to a
particular test** ([[iec-99-4]] §2.5). A section is *not necessarily* an
[[arrester-unit|arrester unit]] — the section is a test-and-modelling concept,
whereas a unit is a constructional, separately-housed building block.

Sections matter because high-voltage arresters cannot usually be tested whole: for
arresters rated above 12 kV the [[operating-duty-test]] is normally done on a
section because of test-facility limits (§7.5.1). The number of similar sections in
the full arrester is the integer **n**, and the power-frequency test voltages
applied to a section are the complete arrester's [[continuous-operating-voltage]]
and [[arrester-rated-voltage|rated voltage]] divided by n (U_c/n and U_r/n), before
being raised to the elevated values U_c* and U_r* by the
[[accelerated-ageing-procedure]] (§7.5.1, §7.5.2.2). The section must reproduce the
complete arrester's transient and steady-state heat-dissipation behaviour — its
thermal model is constrained by §7.5.3.2 and its equivalence verified per **Annex B**
(thermal equivalency test). For the [[line-discharge-class]] and operating-duty
tests, §6.3 requires sections whose resistor volume and [[reference-voltage]]
sit at the worst-case (lowest) end of the manufacturer's declared range.
