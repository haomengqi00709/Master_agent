---
id: making-current-release
type: concept
tags: [concept, iec-56, circuit-breaker]
---

# Making-current release

A release which permits a [[circuit-breaker]] to open, without any intentional time delay, during a closing operation, if the making current exceeds a predetermined value, and which is rendered inoperative when the circuit-breaker is in the closed position ([[iec-56]] 3.104.18). It guards the closing stroke: should the breaker be closed onto a fault, the high making current trips the [[operating-mechanism]] at once so the contacts re-open. Because it is disabled once the breaker reaches the closed position, it does not duplicate the protective function of an [[over-current-release]] during normal service. Its time characteristic is effectively that of an [[instantaneous-release]], and it complements the trip-free behaviour required of the mechanism.
