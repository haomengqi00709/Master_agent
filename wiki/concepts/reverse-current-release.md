---
id: reverse-current-release
type: concept
tags: [concept, iec-56, circuit-breaker]
---

# Reverse-current release

A release, applicable to d.c. only, which causes a [[circuit-breaker]] to open when the current passes in the reverse direction and exceeds a predetermined value ([[iec-56]] 3.104.26, IEV 441-16-43). It senses the direction as well as the magnitude of current, and on a sufficiently large reversal it actuates the [[operating-mechanism]] to trip the breaker, protecting sources such as batteries or rectifiers against back-feeding. It is one of the current-operated releases alongside the [[over-current-release]] and may act with or without intentional delay, the no-delay case being an [[instantaneous-release]]. Being a d.c. phenomenon, it sits apart from the a.c. duties that are the main subject of [[iec-56]].
