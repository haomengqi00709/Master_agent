---
id: transient-recovery-voltage
type: concept
tags: [concept, circuit-breaker, trv]
---

# Transient recovery voltage (TRV)

The rated transient recovery voltage (TRV) for terminal faults is the reference voltage that constitutes the limit of the prospective TRV of circuits the circuit-breaker can break on a fault at its terminals, relating to the [[rated-short-circuit-breaking-current]] (4.101). It is represented by a two-parameter envelope (uc, t3) for [[rated-voltage]] below 100 kV, or a four-parameter envelope (u1, t1, uc, t2) for 100 kV and above, plus a delay line (td) and, for the busbar-driven initial TRV (ITRV), a further line ([[iec-56]] 4.102). Standard values (prospective, for 50/60 Hz systems) include, from Table IIA (first-pole-to-clear factor 1.5):
- 12 kV: uc = 20.6 kV, t3 = 60 us, RRRV 0.34 kV/us
- 72.5 kV: uc = 124 kV, t3 = 166 us, RRRV 0.75 kV/us
For 100-170 kV (Table IIC, factor 1.3) e.g. 145 kV gives u1 = 154 kV, uc = 215 kV, RRRV 2.0 kV/us. ITRV may be neglected below 25 kA. Also governs [[short-line-fault]] supply-side TRV.
