---
id: encapsulated-cells-and-batteries
type: concept
tags: [concept, iec-79-18, ex, encapsulation]
---

# Encapsulated cells, batteries and accumulators (encapsulation "m")

Supplementary constructional and test requirements for primary and secondary cells,
batteries and accumulators encapsulated to [[type-of-protection-m|"m"]] (IEC 79-18
§6.1, with tests in §8.2.4). These supplement the general clause 5 requirements.

**Construction (§6.1).** Only cells/batteries/accumulators that, in normal use under
the manufacturer's specified conditions, are **not expected to release gas, do not
release electrolyte, or produce excessive temperature rise** may be encapsulated. The
construction shall allow **venting to the outside atmosphere** of any gas that may be
generated, unless precautions acceptable to the authority avoid gas release or cell
deformation affecting the protection. Expansion tolerances must be considered — e.g. a
**flexible elastomer around the cell** so no undue pressure is applied to the
[[encapsulation-compound|compound]]. Where the charging device is not in the same
enclosure, the certificate shall state the required charging conditions and the
apparatus is marked **"X"** (per 25.2.9 of IEC 79-0). The tests of §8.2.4 must be
passed.

**Tests (§8.2.4).** With internal temperature sensors fitted (as in
[[thermal-tests|§8.2.1]]):
- **Discharge test (8.2.4.1):** at T_amax °C ± 2 K, the fully-charged unit is completely
  discharged through an appropriate external load — **1 mΩ** if a current-limiting
  resistor/electronic device is present; a value giving **1.7 × the rated current** of
  any encapsulated fuse; or a value that just does not operate any encapsulated thermal
  protection. An encapsulated/fixed load is treated as short-circuited unless it is
  [[fault-not-considered-components|not subject to fault]]. Maximum cell and compound
  surface temperatures must satisfy [[temperature-limitation|§5.4]]; acceptance per
  §8.2.1.3.
- **Electric strength test (8.2.4.2):** the [[apparatus-electric-strength-test|§8.2.3 test]]
  is applied only if the cells are used **not as a sole power source** but together with
  other sources and galvanically connected to them.

**Related:** [[type-of-protection-m]] · [[batteries]] · [[temperature-limitation]] · [[thermal-tests]] · [[apparatus-electric-strength-test]] · [[encapsulated-fuses]]
