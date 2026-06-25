---
id: rated-back-to-back-capacitor-bank-breaking-current
type: concept
tags: [concept, iec-56, circuit-breaker]
---

# Rated back-to-back capacitor bank breaking current

Clause 4.110 of [[iec-56]] defines the rated back-to-back capacitor bank breaking current as the maximum capacitor current the circuit-breaker shall be capable of breaking at its rated voltage under the prescribed conditions, without exceeding the maximum permissible switching overvoltages specified by the manufacturer (suggested values in Table IX, columns B). It refers to switching a shunt capacitor bank where one or several other shunt banks are connected to the source side, so the breaker sees a multiple (parallel) / back-to-back bank (3.101.12): on closing, the already-energised parallel banks discharge into the bank being switched, giving a high-frequency inrush equal to the [[rated-capacitor-bank-inrush-making-current]]. This distinguishes it from the [[rated-single-capacitor-bank-breaking-current]], where no source-side banks exist. Specification is not mandatory; values come from the R 10 series, and a note adds that similar conditions can apply to switching cables. [[restrike]] on interruption is the key risk; see [[capacitive-current-switching-test]] ([[iec-56]] 4.110).
