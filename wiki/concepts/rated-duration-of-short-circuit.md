---
id: rated-duration-of-short-circuit
type: concept
tags: [concept, rating, circuit-breaker]
---

# Rated duration of short-circuit

The rated duration of short-circuit is the time interval for which the circuit-breaker can carry, in the closed position, a current equal to its [[rated-short-time-withstand-current]] (4.5). Sub-clause 4.7 of IEC Publication 694 applies, with an addition in [[iec-56]] 4.7. The **standard value is 1 s**; if a value greater than 1 s is necessary, 3 s is recommended ([[iec-56]] / IEC 56-2 §10; see [[iec-56-2-rated-characteristics]]). A rated duration need not be assigned to a circuit-breaker fitted with a direct over-current release, provided that, in a circuit whose prospective breaking current equals its [[rated-short-circuit-breaking-current]], the circuit-breaker can carry the resulting current for the break-time required, with the over-current release set for its maximum time lag, while operating in accordance with its [[rated-operating-sequence]] (4.104). It thus links the thermal withstand rating to actual tripping behaviour and defines the duration associated with the [[rated-peak-withstand-current]].
