---
id: reference-designation-system
type: concept
standard: IEC 1082-1
aliases: [item designation, reference designation, designation prefixes, =function +location -product :terminal]
tags: [concept, iec-1082, documentation]
---

# Reference designation system (= + - : prefixes)

The system of **prefix codes** by which IEC 1082 documents identify the items,
their function, their location and their terminals. The codes themselves are
defined in **[[iec-750|IEC 750]] (Item designation in electrotechnology)**; IEC 1082
*applies* them pervasively across every diagram, table and list. Each designation
block is introduced by a single prefix sign:

| Prefix | Aspect | Meaning | Example (from Part 1/2) |
|:---:|--------|---------|-------------------------|
| `=` | **function / system** | the functional purpose or system the item serves | `=E1` electric-power distribution system, `=W11` cooling-water supply system |
| `+` | **location** | where the item is physically situated | `+A1` control desk, `+B5` a constructional unit |
| `-` | **product / item** | the actual physical item (component, device, unit) | `-K1` relay, `-S1` pushbutton, `-Q1` motor-starter, `-W109` cable |
| `:` | **terminal** | a terminal/connection point on an item | `-X1:3` terminal 3 of connector `-X1` |

Several prefixes combine into a compound designation reading
**function + location + product (+ terminal)**, e.g. `=W11+A1-Q1` ="the motor
starter `-Q1`, located in unit `+A1`, belonging to the cooling-water system
`=W11`." Part 1's figures 34 and 35 show the same plant expressed first as a
**function-oriented structure** (everything hung under `=` system codes) and then
as a **location-oriented structure** (everything hung under `+` location codes) —
see [[function-oriented-vs-location-oriented-structure]].

The product prefix `-` is the one most visible on day-to-day circuit and
connection diagrams (the `-K1`/`-S1`/`-W1` labels). It is what makes
[[representation-methods-iec1082|detached and semi-attached representation]]
possible: scattered parts of one device share one `-` designation. On connection
documents ([[connection-documents-iec1082|IEC 1082-3]]) cables get `-W…`
designations and conductors are additionally identified per **IEC 446 / IEC 757**,
while terminals carry `:` designations per **IEC 445**. References across sheets
use [[signal-and-location-references]].
