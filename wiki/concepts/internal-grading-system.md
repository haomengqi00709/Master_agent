---
id: internal-grading-system
type: concept
tags: [concept, iec-99-4, surge-arrester]
---

# Internal grading system of an arrester

The internal grading system is the set of **grading impedances — in particular
grading capacitors connected in parallel to one single resistor or to a group of
non-linear [[metal-oxide-resistor|metal-oxide resistors]] — used to control the
voltage distribution along the metal-oxide resistor stack** ([[iec-99-4]] §2.3).
On a tall arrester, stray capacitance to earth makes the power-frequency voltage
distribute unevenly along the column, over-stressing the resistors nearest the
line terminal; grading capacitors equalise this distribution so no individual
resistor is over-voltaged.

The internal grading system is distinct from the external [[grading-ring]] (a
metal ring that grades the field electrostatically). Grading components are
classed as "auxiliary equipment": §5.13 sets *no requirement at this time* for
them, and §7.1 item 7 (artificial pollution test, Annex F) is intended partly to
show the internal grading system withstands pollution without damage. Voltage
unbalance from imperfect grading is accounted for in the
[[accelerated-ageing-procedure]] via the corrected maximum continuous operating
voltage formula U_ct = √2·U_c·(1 + 0,05 L), where L is the arrester length in
metres (§7.5.2.1). Test samples must be assembled with grading components
applicable to the design (§6.3).
