---
id: ip-first-numeral-tests
type: concept
tags: [concept, iec-529, ip-code]
---

# Verification tests for the first characteristic numeral

The **type tests** that establish a [[ip-code-structure|first characteristic
numeral]] ([[iec-529]], 1st ed. clause 7; 2nd ed. clause 12, Tables V & VI). They
verify **both** halves of the first numeral: protection of persons against access
to hazardous parts (using an [[ip-access-probe|access probe]]) and protection of
equipment against solid-object/dust ingress (using an object probe or the dust
chamber). Samples are tested in clean, new condition, fully assembled and mounted
as stated by the manufacturer.

**Probe tests (numerals 1–4)** — apply the standardised probe to every opening at
the specified force; protection is satisfactory if the probe does not fully
penetrate **and adequate clearance is kept** to live/moving parts:

| Numeral | Probe | Force | Pass condition |
|---------|-------|-------|----------------|
| [[ip-first-numeral-0|0]] | — | — | no test required |
| [[ip-first-numeral-1|1]] | sphere 50 mm Ø | 50 N ± 10% | sphere does not pass; clearance kept |
| [[ip-first-numeral-2|2]] | jointed finger 12 mm + sphere 12,5 mm | 10 N / 30 N ± 10% | finger may enter 80 mm but clearance kept; 12,5 mm sphere not fully penetrate |
| [[ip-first-numeral-3|3]] | rod 2,5 mm Ø | 3 N ± 10% | rod cannot enter; clearance kept |
| [[ip-first-numeral-4|4]] | wire 1,0 mm Ø | 1 N ± 10% | wire cannot enter; clearance kept |

**Adequate clearance (1st ed. §6.1):** for **low-voltage** equipment (≤ 1000 V
a.c. / 1200 V d.c.) the probe must not touch live/moving parts — checked by a
≥ 40 V lamp circuit between probe and live parts (lamp must not light; varnished
parts covered with foil bonded to live parts). For **high-voltage** equipment the
probe in the most unfavourable position must withstand the applicable dielectric
test, or a specified air clearance is verified instead.

**Dust tests (numerals 5–6, 1st ed. §7.5–7.6):** the **dust chamber** (Figure 2)
with talcum powder (2 kg/m³, sieved 75 µm/50 µm) in suspension. For category-1
enclosures a vacuum pump holds the interior below atmospheric pressure, drawing up
to **80 air-volume changes** (≤ 60 vol/h, ≤ 200 mm-water depression; stop after
2 h if 40–60 vol/h, else continue to 80 volumes or 8 h). **IP5X** passes if dust
has not accumulated enough to impair operation; **IP6X** passes only if **no dust
deposit** is observable. Visual inspection alone may suffice for numerals 1–2 in
obvious cases; in doubt the full test is done.

**See:** [[ip-access-probe]] · [[ip-additional-letter]] · [[ip-second-numeral-tests]] · [[iec-529]]
