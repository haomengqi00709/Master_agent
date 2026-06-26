---
id: ignition-test-thermocouples
type: concept
tags: [concept, iec-79-4, ex, ignition-temperature, apparatus]
---

# Thermocouples (flask-temperature measurement)

The temperature sensors that measure the **flask temperature** — the quantity
whose minimum igniting value is the [[ignition-temperature]] ([[iec-79-4]] §4.3).
**One or more calibrated thermocouples of 0.8 mm (0.032 in) maximum diameter**
shall be used. They **shall be positioned at selected points on the flask** (the
points chosen per §4.2 to verify uniform heating) and in **intimate contact with
its external surface** — the flask wall temperature, not the air or furnace
temperature, is what is reported.

The small 0.8 mm diameter limit keeps thermal mass and response lag low so the
reading tracks the flask wall closely. Calibration is essential because the
final result is refined in **2 °C steps** (§5.4) and repeatability is suspect
beyond **2 %** (§7.1) — errors of that order are well within an uncalibrated
thermocouple's drift.

The number and placement of thermocouples is tied to the
[[ignition-test-furnace|furnace]] design and its §4.2 uniformity check:

- **Furnace A1** uses **three** thermocouples — 25 mm and 50 mm below the bottom
  of the neck heater, and under the flask base near its centre — each adjustable
  to within ±1 °C via independent heater controls.
- **Furnace A2** positions measurement thermocouples on the flask wall **25 ± 2 mm
  from the base** and at the **centre of the under-surface of the base**.

A furnace/thermocouple arrangement is only accepted if, so positioned, it
reproduces the Table I reference ignition temperatures within the §7 tolerances.

**Related:** [[ignition-test-furnace]] · [[erlenmeyer-test-flask]] · [[ignition-test-validity]] · [[iec-79-4]]
