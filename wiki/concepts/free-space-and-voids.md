---
id: free-space-and-voids
type: concept
tags: [concept, iec-79-18, ex, encapsulation]
---

# Free space and voids (encapsulation "m")

A core constructional rule of [[type-of-protection-m|encapsulation "m"]]: the
encapsulation **shall be made without voids** (IEC 79-18 §5.1.2). A void filled with
explosive atmosphere defeats the protection, so empty space inside the compound is
tightly limited.

The standard permits **only** the unavoidable internal free volume of encapsulated
components (relays, transistors, etc.), each with an **internal free volume of up to
100 cm³**. Around such components the [[thickness-of-compound|compound thickness]]
between components shall be **at least 3 mm**; where the void is less than 1 cm³ the
compound thickness between them may be reduced to **1 mm**. Two further rules close
loopholes: **switching contacts shall have an additional housing before
encapsulation**, and if the rated contact current exceeds **6 A** that additional
housing **shall be inorganic**; and **loose filling materials shall not be used** to
reduce the free volume inside a void down to the permitted upper limit (i.e. you may
not "pad out" an oversized cavity).

Note that the distances between live parts of encapsulated electronic assemblies
(e.g. printed-circuit boards) are **not** treated as
[[distances-through-compound|distances through the compound]] (§5.3), and after the
[[thermal-tests]] no visible separation of partially-embedded parts is allowed
([[adhesion]], §5.7).

**Related:** [[type-of-protection-m]] · [[encapsulation-compound]] · [[thickness-of-compound]] · [[distances-through-compound]] · [[adhesion]]
