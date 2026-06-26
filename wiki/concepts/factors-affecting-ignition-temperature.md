---
id: factors-affecting-ignition-temperature
type: concept
tags: [concept, iec-79-4, ex, ignition-temperature]
---

# Factors affecting the ignition-temperature result

The [[ignition-temperature]] is **not an absolute physical constant** but a
property tied to this test geometry; [[iec-79-4]] controls every variable that can
move the result, and amendment [[iec-79-4a|79-4A]] adds an explicit caution about
purity. The main factors:

- **Sample volume** — one axis of the test matrix; the test is repeated across
  volumes (§5.4) because the minimum igniting temperature varies with charge.
  Suitable starting volumes are 0.07 ml (liquid) / 20 ml (gaseous) (§5.2.3).
- **Flask material and cleanliness** — a 200 ml borosilicate [[erlenmeyer-test-flask|Erlenmeyer flask]];
  a **chemically clean** flask is required (§4.1), and any quartz/metal
  substitute must be **declared in the report** because the wall surface affects
  ignition.
- **Heating uniformity / temperature measurement** — the
  [[ignition-test-furnace|furnace]] must heat "adequately uniformly" and is only
  accepted if it reproduces the Table I reference values (§4.2); thermocouples
  must be calibrated and in intimate contact (§4.3).
- **Wetting the walls / injection technique** — liquids must be injected as
  central droplets, completed in 2 s, **without wetting the walls** (§5.2.1);
  gases at ~25 ml/s (§5.2.2).
- **Atmospheric pressure** — the result is defined "in air at **atmospheric
  pressure**" (§1) and barometric pressure is recorded with the result (§6, §8).
- **Sample purity** — calibration substances require ≥ 99.9 % purity (§4.2).
  **Amended (Amd.):** [[iec-79-4a|79-4A]] Note 2 warns that *a small amount of
  impurity may appreciably alter the ignition temperature*: e.g. **trichlorosilane
  gives 230 °C with a freshly prepared sample, but after ageing and possible
  moisture contamination the value falls to 185 °C** — a 45 °C drop that could
  push the substance into a lower (more onerous) [[temperature-classes-t1-t6|temperature class]].
- **Temperature-step resolution** — the final search uses **2 °C steps** (§5.4),
  setting the resolution of the reported value.

Because of these sensitivities the method fixes the apparatus and procedure
tightly and reports precision only within the
[[repeatability-reproducibility|2 %/5 % tolerances]] of §7.

**Related:** [[ignition-temperature]] · [[iec-79-4a]] · [[repeatability-reproducibility]] · [[temperature-classes-t1-t6]] · [[iec-79-4]]
