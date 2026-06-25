---
id: rated-operating-sequence
type: concept
tags: [concept, rating, circuit-breaker]
---

# Rated operating sequence

The rated operating sequence prescribes the standard succession of opening (O) and close-open (CO) operations the circuit-breaker must perform with specified time intervals. Two alternative sequences are defined ([[iec-56]] 4.104):
- a) O - t - CO - t' - CO, where t = 3 min for circuit-breakers not intended for rapid auto-reclosing, or t = 0.3 s (dead time) for those intended for rapid auto-reclosing, with t' = 3 min;
- b) CO - t'' - CO, with t'' = 15 s for circuit-breakers not intended for rapid auto-reclosing.
CO is a closing operation immediately followed by opening, with no intentional delay. For rapid auto-reclosing, alternative t' = 15 s (for [[rated-voltage]] up to 52 kV) and t' = 1 min are also used. If the dead time is adjustable, its limits shall be specified. This sequence governs short-circuit making and breaking test duties and applies to the [[rated-short-circuit-breaking-current]] (4.101) and [[rated-duration-of-short-circuit]] (4.7).
