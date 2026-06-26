---
id: operating-duty-test
type: concept
tags: [concept, iec-99-1, iec-99-4, surge-arrester]
---

# Operating-duty test (Type test, §64)

The **operating-duty test** of [[iec-99-1]] §64 simulates service conditions by applying a stipulated
number of specified impulses to the arrester **while it is energized** by a power supply of specified
frequency, voltage and impedance. It is the test that proves the
[[non-linear-resistor-type-arrester|valve-type arrester]] can repeatedly discharge a surge and then
**interrupt the resulting [[follow-current]]** — the defining duty of the device. It is made (per §55,
§56, §59) on **three new samples** of complete arresters or sections (rating ≥ 3 kV, need not exceed
12 kV); a typical test circuit is in Appendix A. For arresters above 12 kV the test is usually made on
a section, with the section test voltage derived from the whole-arrester rated voltage and the
voltage-distribution rules of §64.

The arrester is connected across a 48–62 Hz supply whose impedance is set so that, during follow
current, the peak power-frequency voltage at the terminals does **not fall below the peak
[[rated-voltage-arrester|rated voltage]]**, and after interruption does not exceed it by more than
10 %. An impulse generator applies an **8/20 current impulse of peak equal to the
[[nominal-discharge-current]]**, the first impulse timed ~60 electrical degrees before the voltage
peak (retarded in ~10° steps if follow current is not consistently established). **Twenty impulses are
applied in four groups of five** (50–60 s between impulses, 25–30 min between groups). **Follow current
must be established by each impulse and the arrester must interrupt it every time.** Voltage and follow
current are recorded oscillographically for at least one discharge per group. Before and after the
test the average dry [[power-frequency-sparkover-voltage|power-frequency sparkover]] and the
[[residual-voltage]] at nominal current are measured and **must not have changed by more than 10 %**.

## In the gapless metal-oxide standard [[iec-99-4]] (§7.5)
For the gapless [[metal-oxide-surge-arrester]] there is no [[follow-current]] to interrupt — the
operating-duty test instead proves the arrester is **[[thermal-stability|thermally stable]]** (does
not run into [[thermal-runaway]]) after impulse stress while continuously energized ([[iec-99-4]]
§5.9, §7.5). Made on three samples (complete arresters or [[arrester-section|sections]]) at 20 °C
±15 °C. The critical parameter is resistor power loss, so the test runs on **new** resistors at
**elevated** voltages U_c\* and Uᵣ\* that give the same power loss as aged resistors — these are set
by the **[[accelerated-ageing-procedure]]** (§7.5.2). Per-section voltages are U_c/n and Uᵣ/n raised to
U_c\*, Uᵣ\*. Two variants by class:
- **§7.5.4 High current impulse operating duty test** — for 1 500 A, 2 500 A, 5 000 A, 10 000 A
  [[line-discharge-class|class 1]] and [[high-lightning-duty-arrester|HLD]] arresters. Conditioning:
  twenty 8/20 [[lightning-current-impulse|impulses]] at Iₙ in four groups of five, on 1,2 × U_c
  (§7.5.4.1). Then two [[high-current-impulse|4/10 high current impulses]] (Table 6 peaks; second after
  preheat to 60 °C ±3 °C). Within 100 ms, Uᵣ\* for 10 s then U_c\* for 30 min (§7.5.4.2).
- **§7.5.5 Switching surge operating duty test** — for 10 000 A classes 2 & 3 and 20 000 A classes 4 &
  5. Conditioning adds two 100 kA 4/10 impulses; then two [[long-duration-current-impulse]]s per Table 4
  (preheat 60 °C), followed by Uᵣ\* 10 s / U_c\* 30 min.

Pass criteria (§7.5.6, [[thermal-stability-evaluation]]): thermal stability achieved; [[residual-voltage]]
unchanged by more than **5 %**; no puncture, [[impulse-waveshape-terminology|flashover]] or cracking of
the [[metal-oxide-resistor|resistors]]. Figures 1, 2, C.1 illustrate the sequences.

**Related:** [[follow-current]], [[nominal-discharge-current]], [[rated-voltage-arrester]],
[[arrester-rated-voltage]], [[continuous-operating-voltage]], [[accelerated-ageing-procedure]],
[[thermal-stability]], [[thermal-runaway]], [[high-current-impulse]],
[[long-duration-current-impulse]], [[residual-voltage]], [[impulse-waveshape]], [[arrester-type-test]],
[[type-test]].
