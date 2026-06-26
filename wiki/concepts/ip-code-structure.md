---
id: ip-code-structure
type: concept
tags: [concept, iec-529, ip-code]
---

# IP Code — arrangement of the designation

The degree of protection provided by an enclosure is indicated by the **IP Code**
([[iec-529]] 2nd ed. clause 4). The designation is the code letters **IP**
(International Protection) followed, in fixed order, by: a **first characteristic
numeral** (0–6), a **second characteristic numeral** (0–8), an optional
**[[ip-additional-letter|additional letter]]** (A, B, C, D) and an optional
**[[ip-supplementary-letter|supplementary letter]]** (H, M, S, W) (§4.1):

```
IP  2  3  C  S
└┬┘ │  │  │  └─ supplementary letter (optional)
 │  │  │  └──── additional letter (optional)
 │  │  └─────── second characteristic numeral (water): 0–8 or X
 │  └────────── first characteristic numeral (access/objects): 0–6 or X
 └───────────── code letters (International Protection)
```

**Placeholder "X" rule (§4.1):** where a characteristic numeral is not required
to be specified, it is replaced by the letter **X** ("XX" if both are omitted).
Additional and supplementary letters may simply be omitted without replacement.
Where more than one supplementary letter is used, the alphabetic sequence
applies. If an enclosure provides different degrees of protection for different
mounting arrangements, the manufacturer states the relevant degree for each in
the instructions. The **first numeral implies compliance with both §5.1 (access)
and §5.2 (solid objects)**; an enclosure may carry a numeral only if it also
complies with all **lower** degrees, though the lower-degree tests need not be
repeated if they would obviously be met.

**Worked examples (§4.2, §9):** `IP2X` (second numeral omitted); `IP20C`
(additional letter); `IPXXC` (both numerals omitted, additional letter only);
`IPX1C`; `IP3XD`; `IP23S` (supplementary letter); `IP21CM`; and the dual form
`IPX5/IPX7` giving two different water degrees for "versatile" use. A full
**IP34** enclosure protects persons/tools ≥ 2,5 mm from hazardous parts, keeps
out solid objects ≥ 2,5 mm, and resists water splashed from any direction.

In the **1st edition (1976)** the same `IPnn` two-numeral scheme already existed
(clause 2) but without the additional letters and without the "IP Code" name; the
omitted-numeral placeholder was likewise **X** (e.g. `IPX5`, `IP2X`).

**See:** [[iec-529]] · first numeral [[ip-first-numeral-0]]…[[ip-first-numeral-6]] ·
second numeral [[ip-second-numeral-0]]…[[ip-second-numeral-8]] ·
[[ip-additional-letter]] · [[ip-supplementary-letter]]
