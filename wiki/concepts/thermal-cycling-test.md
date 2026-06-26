---
id: thermal-cycling-test
type: concept
tags: [concept, iec-79-18, ex, encapsulation]
---

# Thermal cycling test (encapsulation "m")

The §8.2.1.2 type test that stresses the [[encapsulation-compound|compound]] by
repeatedly driving the sample between its hot and cold service extremes, checking that
[[type-of-protection-m|encapsulation "m"]] survives differential expansion without
cracking or separating (IEC 79-18; the procedure is also drawn diagrammatically in
**annex A**).

The sample is fitted with one or more **temperature sensors in the compound at the
hottest points** judged by the authority (for windings, temperature may be inferred from
resistance change). The cycle:

1. De-energized, stabilized at room temperature **21 °C ± 2 K** (stability = inside/outside
   difference < 2 K).
2. Brought to **(T_amax + 10) °C ± 2 K** (T_amax = specified max service ambient); once
   stable, **energized at 90–110 % of rated voltage** at the most unfavourable condition.
   Where internal thermal protective devices exist, energize only to the level that just
   does not operate the non-self-resetting device (such devices may be bridged for test).
   The **internal temperature shall not exceed the
   [[continuous-operating-temperature|continuous operating temperature]] of the compound**
   (§3.4, §5.4). Energize until the internal gradient is **< 2 K/h**, minimum **1 h**.
3. De-energized, cooled to room temperature, then brought to **(T_amin − 5) °C ± 2 K**
   (T_amin = specified min service ambient); re-energized at 90–110 % rated voltage,
   most unfavourable condition, until gradient < 2 K/h, minimum **0.5 h**; then cooled to
   (T_amin − 5) °C, minimum **0.5 h**.
4. The energize/de-energize cycle is repeated — **three complete cycles** in all — before
   the sample is removed and reheated to room temperature.

Acceptance is by the §8.2.1.3 criteria (see [[thermal-tests]]): no cracks, flaking,
exposure, shrinkage, swelling, decomposition, softening or overheating.

**Related:** [[type-of-protection-m]] · [[thermal-tests]] · [[temperature-limitation]] · [[continuous-operating-temperature]] · [[temperature-range-of-the-compound]]
