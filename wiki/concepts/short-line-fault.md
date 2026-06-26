---
id: short-line-fault
type: concept
tags: [concept, circuit-breaker, fault]
---

# Short-line fault (SLF)

Rated characteristics for short-line faults are required for three-pole circuit-breakers designed for direct connection to overhead transmission lines, with [[rated-voltage]] of 52 kV and above and a [[rated-short-circuit-breaking-current]] exceeding 12.5 kA. They relate to breaking a single-phase earth fault in an earthed-neutral system ([[iec-56]] 4.105). The circuit comprises a source-side supply circuit and a load-side short line (Figure 13). The supply circuit has voltage U/sqrt(3), terminal-fault current equal to the rated short-circuit breaking current, prospective [[transient-recovery-voltage]] per Tables IVA/IVB/IVC, and ITRV from Table III. The line side is defined by standard rated surge impedance Z, peak factor k and time delay td (Table V), with the RRRV factor s = 0.200 kV/(us-kA) at 50 Hz and 0.240 at 60 Hz. TRV is calculated per Appendix AA; the initial portion is closely related to the ITRV described under 4.102.

In the earlier Part 2 ([[iec-56]] / IEC 56-2 §8, Table VII) the line characteristics were tabulated by number of conductors per phase: Z = 480 Ω (k = 1.7) for 1 conductor (52 ≤ U < 245 kV), 375 Ω (k = 1.6) for 2 conductors, and 330 Ω (k = 1.5) for 3-4 conductors (525-765 kV), with RRRV factor s = Z/(2·√2·π·f). Amendment 1 (1971) to 56-2 later replaced the whole table with a single row Z = 450 Ω, k = 1.6 (s = 0.200 kV/µs·kA at 50 Hz, 0.240 at 60 Hz), permitting lower Z and k by agreement when the short-circuit current is below 20 kA or U exceeds 420 kV. Appendix A of 56-2 derives the SLF-TRV (initial voltage to earth u/U = 1 − i_L/i, line-side excursion u* = k·u, peak source-side u_m = (1 + 0.4·i_L/i)·U_m) — the basis of the consolidated method. See [[iec-56-2-rated-characteristics]].
