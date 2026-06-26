---
id: impulse-waveshape-terminology
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Impulse waveshape terminology (§2.14–2.28)

[[iec-99-4]] Section 2 defines the impulse vocabulary used to specify every current
and voltage waveform in the standard. An **impulse** (§2.14) is a unidirectional
wave of voltage or current which rises rapidly to a maximum and falls — usually
less rapidly — to zero, with small if any opposite-polarity excursions. The
parameters defining it are polarity, peak value, front time and time to half value
on the tail.

- **Designation Tₐ/Tᵦ** (§2.15): a pair of numbers, first the virtual front time
  Tₐ, second the virtual time to half value on the tail Tᵦ, in microseconds (the
  "/" has no mathematical meaning) — e.g. 8/20, 4/10, 30/80.
- **Peak (crest) value** (§2.19): the maximum value; superimposed oscillations may
  be disregarded.
- **Front** (§2.20) / **Tail** (§2.21): the parts of the impulse before / after
  the peak.
- **Virtual origin** (§2.22): intersection of the time axis with the straight line
  through the 10 % and 90 % front reference points (for current impulses).
- **Virtual front time T₁** (§2.23): 1,25 × the time for the current to rise from
  10 % to 90 % of peak.
- **Virtual steepness** (§2.24): peak value ÷ virtual front time.
- **Virtual time to half value on the tail T₂** (§2.25): interval from virtual
  origin to the instant the value falls to half peak.
- For **rectangular** impulses: **virtual duration of the peak** (§2.26, time above
  90 % of peak) and **virtual total duration** (§2.27, time above 10 % of peak).
- **Peak value of opposite polarity** (§2.28): the largest opposite-polarity swing
  when the impulse oscillates about zero.

This terminology underpins the specific test waves: [[steep-current-impulse]] (1/–),
[[lightning-current-impulse]] (8/20), [[switching-current-impulse]],
[[high-current-impulse]] (4/10), the 30/80 high-lightning wave, and the
[[long-duration-current-impulse]] (rectangular). The standard's two
disruptive-discharge terms — **puncture** (a disruptive discharge *through a
solid*, §2.12) and **flashover** (a disruptive discharge *over a solid surface*,
§2.13) — are the failure modes that post-test examination must not reveal in the
[[metal-oxide-resistor|metal-oxide resistors]].
