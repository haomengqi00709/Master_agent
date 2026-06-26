---
id: repeatability-reproducibility
type: concept
tags: [concept, iec-79-4, ex, ignition-temperature]
---

# Repeatability and reproducibility (ignition-temperature precision)

The two precision statistics that gate an [[ignition-temperature]] result in
[[iec-79-4]] §7. They distinguish **within-operator** scatter from
**between-laboratory** scatter:

- **Repeatability (§7.1)** — duplicate results by the **same operator** are
  **suspect if they differ by more than 2 %**. This bounds short-term, same-rig
  variation (sample dosing, observation, flask cleanliness).
- **Reproducibility (§7.2)** — averages of duplicate results from **different
  laboratories** are **suspect if they differ by more than 5 %**. This bounds the
  larger between-lab variation (different furnaces, thermocouples, operators).

Reproducibility (5 %) is deliberately looser than repeatability (2 %) — the
classic pattern, since cross-lab differences add furnace/operator variance on top
of within-lab scatter. A §7 **Note** flags both tolerances as **tentative,
pending more information**.

These figures explain method choices elsewhere: the final test refines in **2 °C
steps** and runs **five confirmatory** repeats ([[ignition-test-procedure|§5.4–5.5]])
to keep within the 2 % repeatability band; the §4.2 furnace is accepted only if
it reproduces the Table I reference substances within these same tolerances; and
the reference table in [[iec-79-4a|amendment 79-4A]] admits only values agreed by
≥2 countries to within the 5 % of §7.2.

**Related:** [[ignition-test-validity]] · [[ignition-temperature]] · [[ignition-test-procedure]] · [[ignition-temperature-data-list]] · [[iec-79-4]]
