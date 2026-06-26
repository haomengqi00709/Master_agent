---
id: discharge-current
type: concept
tags: [concept, iec-99-1, iec-99-4, surge-arrester]
---

# Discharge current of an arrester

The **discharge current of an arrester** is the surge or impulse current which flows through the
arrester after a sparkover of the [[series-gap|series gaps]] ([[iec-99-1]] §34). It is the current the
[[non-linear-series-resistor]] diverts to earth when a surge causes the gaps to spark over, and during
its passage the [[residual-voltage]] (§37) appears across the arrester terminals. It is distinct from
the [[follow-current]] (§36), which is the power-frequency current drawn from the connected source
*after* the discharge current, and which the arrester must interrupt.

The characterising value is the [[nominal-discharge-current]] (§35) — the peak value of an 8/20
([[impulse-waveshape]]) discharge current used to classify the arrester. Discharge-current magnitudes
appear throughout the test programme: the [[residual-voltage-test]] applies 0.5×, 1× and 2× nominal
current (§62); the high-current [[current-impulse-withstand-test]] applies a 4/10 impulse of up to
100 kA (§63.2); and the long-duration test applies substantially rectangular impulses of up to ~2 000
µs (§63.3). In service the actual discharge current depends on the lightning or switching surge and
the system; the [[arrester-application-guide]] (Appendix C / IEC 99-1A) discusses estimating it for
effectively- and non-effectively-shielded installations (typically 5 000–20 000 A, 8/20).

## In the gapless metal-oxide standard [[iec-99-4]]
In the gapless [[metal-oxide-surge-arrester]] of [[iec-99-4]] there are **no series
[[series-gap|gaps]]** and hence no sparkover and no [[follow-current]]: §2.29 defines the discharge
current simply as "the impulse current which flows through the arrester." Its named forms there are
the [[nominal-discharge-current]] (8/20 [[lightning-current-impulse]], §2.30 — the classifier), the
[[high-current-impulse]] (4/10, §2.31) and the [[switching-current-impulse]] (§2.32). The
residual-voltage-versus-discharge-current curve obtained at ≈0,5×, 1×, 2× Iₙ in the
[[residual-voltage-test]] (§7.3.2) characterises the arrester across the discharge-current range.

**Related:** [[surge-arrester]], [[nominal-discharge-current]], [[residual-voltage]],
[[follow-current]], [[high-current-impulse]], [[switching-current-impulse]], [[impulse-waveshape]],
[[current-impulse-withstand-test]].
