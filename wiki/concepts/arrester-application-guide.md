---
id: arrester-application-guide
type: concept
tags: [concept, iec-99-1, surge-arrester]
---

# Arrester application guide (insulation co-ordination, Appendix C)

The **application guide** is Appendix C of [[iec-99-1]] — "Guide to the application of non-linear
resistor type lightning arresters for a.c. systems." It covers applying [[surge-arrester|arresters]]
to safeguard apparatus against overvoltages by proper **co-ordination of protective devices with
insulation strength**, and is the source of the [[impulse-protective-level]] / protective-ratio
definitions. **Amended:** this guide was first issued as the separate supplement **Publication 99-1A
(1962)** to the 1958 first edition, and was incorporated as Appendix C in the 1970 second edition
(it cross-references IEC Publication 71/71A for insulation co-ordination).

The selection-and-location procedure (99-1A §2–§3) is a sequence of steps:
1. **Determine the maximum phase-to-earth power-frequency voltage** at the arrester location — the
   highest system voltage Uₘ multiplied by the **coefficient of earthing**, classified as ≤ 80 %
   (effectively earthed: X₀/X₁ between 0 and +3, R₀/X₁ between 0 and +1) or > 80 % (non-effectively
   earthed, resonant-earthed or isolated neutral). This connects to [[earth-fault-factor]],
   [[earthed-neutral-system]], [[isolated-neutral-system]] and [[resonant-earthed-system]].
2. **Estimate the magnitude and waveshape of the [[discharge-current]]**, governed largely by
   shielding — effectively shielded installations see ~4 000 A at 110 kV up to ~10 000 A at 400 kV
   (8/20); non-effectively-shielded installations may need co-ordination at **5 000–20 000 A**.
3. **Determine the insulation withstand strength** to be protected (full-wave impulse test voltage per
   IEC Publication 71; oil/paper transformer insulation withstands ~15 % above full-wave for peaks
   shorter than 3 µs).
4. **Tentatively select the arrester class and [[rated-voltage-arrester|voltage rating]]** — the
   10 000 A class gives the best [[protective-characteristics-arrester|protective levels]], then
   5 000 A Series A. The rating must be at least the highest phase-to-earth voltage to assure
   [[follow-current]] extinction; too low a rating risks arrester failure.
5. **Determine the [[impulse-protective-level]]** of the selected arrester and **co-ordinate** it with
   the insulation: the recommended **minimum protective ratio is 1.2**.

The guide also treats protection of series windings, dry-type transformers and rotating machines (§4),
switching surges liable to operate the arrester (§5, classified by surge energy and follow-current
duration), and protection of transformer unearthed neutrals (§3.6.5, rating ≥ 0.7 Uₘ for fully
insulated transformers). Abnormal frequency (<48 or >62 Hz) requires special consideration.

**Related:** [[impulse-protective-level]], [[protective-characteristics-arrester]],
[[rated-voltage-arrester]], [[nominal-discharge-current]], [[discharge-current]], [[follow-current]],
[[earth-fault-factor]], [[isolated-neutral-system]], [[resonant-earthed-system]],
[[earthed-neutral-system]].
