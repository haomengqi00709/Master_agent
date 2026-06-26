---
id: current-distribution-multi-column
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Current distribution in a multi-column arrester (§5.6, §8.1e)

Some arresters use **several columns of [[metal-oxide-resistor|metal-oxide
resistors]] in parallel** to share the [[discharge-current]]. If the columns are not
perfectly matched, one column carries more than its share and may be over-stressed.
The requirement (§5.6) is that the manufacturer **specify the highest value of
current in a column** of a multi-column arrester ([[iec-99-4]] §5.6).

The verifying test (the *current distribution test*, §8.1e — a
[[arrester-routine-test|routine test]] and type-test item 10) is carried out on
**all groups of parallel resistors** — a group being a part of the assembly with no
intermediate electrical connection between columns. The manufacturer specifies a
suitable impulse current in the range **0,01 to 1 × [[nominal-discharge-current]]**
(virtual front time ≥7 µs, any half-value time), at which the current through each
column is measured; the highest column current must not exceed the manufacturer's
upper limit. If a group's rated voltage is too high for available test facilities,
intermediate connections may be introduced to form smaller *artificial groups*,
each of which must pass the test (note 2 to §8.1e). The worst-case uneven
distribution must be considered when selecting test samples for the
[[line-discharge-class|line discharge]] and [[operating-duty-test|operating duty]]
tests (§6.3c).
