---
id: ip-supplementary-letter
type: concept
tags: [concept, iec-529, ip-code]
---

# IP supplementary letter (H, M, S, W)

An **optional** letter placed last in the [[ip-code-structure|IP Code]], giving
**supplementary information** specific to a type of apparatus or to the test
conditions ([[iec-529]] 2nd ed. clause 4, clause 8). Where more than one is used
the alphabetic sequence applies. The four standardised letters are:

| Letter | Meaning |
|--------|---------|
| **H** | High-voltage apparatus |
| **M** | Tested for water protection with the equipment's moving parts **in motion** (e.g. machine running) |
| **S** | Tested for water protection with the equipment's moving parts **stationary** (not in operation) |
| **W** | Suitable for use under specified **weather** conditions, with additional protective features/processes |

The **S/M pair** matters because the water tightness of a rotating machine can
differ between running and stopped states; `IP23S` declares the spray test was
done stationary, `IP21CM` (using both an [[ip-additional-letter|additional]] and
a supplementary letter) declares it running. **The absence of S and M implies the
degree of protection does not depend on whether parts are in motion** — which may
require the water test to be done under **both** conditions, though one is
generally sufficient if the other would obviously pass ([[iec-529]] 2nd ed.
clause 8). Other letters may be used in product standards, but to avoid duplicate
use the Secretariat of TC 70 should be consulted before any new supplementary
letter is introduced (§9.2 footnote).

In the **1st edition (1976)** (clause 2.2) the letters **S, M, W** already
existed (carried over from rotating-machine practice): S = tested against water
ingress when **not** in operation; M = tested when **in mechanical operation**;
W (placed immediately after "IP") = suitable for agreed weather conditions with
extra protective features. The 1989 edition added **H** and tightened the
definitions. Note the 1st-edition S/M sense for "not in operation"/"in operation"
is the inverse mnemonic of the 2nd-edition Stationary/Motion wording, but the
underlying intent (which state the water test used) is the same.

**See:** [[ip-code-structure]] · [[ip-additional-letter]] · [[ip-second-numeral-tests]]
