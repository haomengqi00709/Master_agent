---
id: iec-56-amendment-1
type: concept
tags: [concept, iec-56, amendment]
---

# IEC 56 Amendment 1 (1992-11)

Amendment 1 to [[iec-56]] (4th edition, 1987), prepared by SC 17A of IEC TC 17,
issued 1992-11. It is a set of corrigenda and substantive technical revisions to
the type-test clauses (mostly clause 6) of the standard — no new rated
characteristics or defined terms, but several test procedures, acceptance
criteria, test-duty definitions and figures are rewritten. Per the LLM-Wiki
method this amendment does not get its own standard hub; the changes are folded
into the affected concept pages below. The clauses it touches, in document order:

## Clause 4 — Ratings

- **4.101.2 D.C. component (p. 45 note).** The first line of the note is rewritten
  to read: "Depending on the characteristics of the system, for example if a
  circuit-breaker is close to a generator, the percentage d.c. component …".
  Acknowledges generator-proximity systems where the d.c. component exceeds the
  Figure 9 value. Affects [[rated-short-circuit-breaking-current]].

## Clause 6 — Type tests (introduction & general)

- **6 Type tests (p. 105).** In the second dash, the cross-reference is corrected
  from "(see subclauses 6.103 to 6.110)" to "(see subclauses 6.102 to 6.110)" —
  so the making/breaking duty 6.102 is included. Affects [[type-test]].
- **6.1.7 Power-frequency voltage tests (p. 109).** The two unnumbered notes are
  numbered NOTE 1 (dead-tank circuit-breakers) and NOTE 2 (special applications).
  Editorial; affects [[dielectric-test]].

## Clause 6.101 — Mechanical & environmental tests

- **6.101.1.3 Condition during/after tests (p. 117).** Adds a sixth indent: after
  the tests the insulating properties in the open position shall be essentially as
  before; visual inspection usually suffices, and in case of doubt the condition
  checking test per 6.1.11 of IEC 694 is sufficient. For sealed-for-life
  interrupters the condition checking test is **mandatory**.
- **6.101.3.3 Low-temperature test (p. 123–125).** Item b) revised: characteristics
  and settings are recorded per 6.101.1.2 at an ambient air temperature of
  (20 ± 5) °C, and the tightness test (if applicable) is run per EE1.4 of Appendix
  EE. Item f) rewritten: low-temperature behaviour and alarms/lock-out are verified
  by disconnecting heater supply for a duration t_h — alarm acceptable, lock-out
  not — after which an opening order at rated supply voltage/pressure is given; the
  opening time is recorded (and contact velocity measured if feasible). The
  manufacturer states t_h; **absent a statement, t_h = 2 h**. A new paragraph after
  item k): accumulated leakage over the whole low-temperature sequence (items b–k)
  shall not reach lock-out pressure without gas replenishment (reaching alarm
  pressure is allowed).
- **6.101.3.4 High-temperature test (p. 125–127).** Item m) revised to mirror low-
  temperature item b) (record per 6.101.1.2 at (20 ± 5) °C, tightness per EE1.4).
  New paragraph after item u): accumulated leakage over the high-temperature
  sequence (items m–u) shall not reach lock-out pressure without gas replenishment.

These three changes affect [[mechanical-and-environmental-test]].

## Clause 6.102 — Making and breaking tests (general)

- **6.102.4 Synthetic tests (p. 141).** Text replaced: synthetic testing methods
  may be applied for the making and breaking tests of 6.106 to 6.111; the
  techniques are described in **IEC 427**. Affects [[short-circuit-test]].
- **6.102.8.1 General (p. 145).** Text replaced: the breaker may be inspected after
  any test duty; mechanical parts and insulators shall be essentially as before.
  Visual inspection usually suffices; in case of doubt the condition checking test
  per 6.1.11 of IEC 694 proves the insulating properties. For sealed-for-life
  interrupters, and where demounting affects the inspection (e.g. certain GIS
  breakers), the condition checking test is **mandatory**.
- **6.102.9 Circuit-breakers with short arcing times (p. 147–153).** First two
  paragraphs amended and the single-phase test programme (Item B) fully rewritten —
  see [[single-phase-short-circuit-test]] and [[short-circuit-test-procedure]]. The
  procedure applies to arcing times not exceeding one cycle for the first pole to
  clear (to extinction of the main arc for breakers with switching resistors).
  Three valid breaking operations per duty, independent of the rated operating
  sequence; reconditioning per 6.102.8.5 is allowed afterwards. Item (A)
  three-phase tests unchanged. Item (B) single-phase now distinguishes:
  **B1)** isolated-neutral substitution (test-duties 1, 2, 3, 4, 4b): 2nd operation
  tripping ≈ 60 electrical degrees earlier than the 1st valid operation, 3rd earlier
  by (90° − dt) with dt < 18°. **B2)** earthed-neutral substitution and short-line
  fault (duties 1, 2, 3, 4, 4b + SLF 6.108/6.109.5): 2nd operation earlier by
  (180° − dt), dt < 18°; 3rd 90° earlier than the 1st; sequence unspecified.
  Conditions 1) and 2) may be combined in one series using isolated-neutral TRV and
  earthed-neutral arcing times. **B3)** test-duty No. 5 keeps the wording of the old
  Item (B)2). **B4)** out-of-phase duties (6.110.4) keep old Item (B)3) except the
  last "For direct tests …" paragraph is deleted.

## Clause 6.104 — Short-circuit test quantities

- **6.104.2 Short-circuit (peak) making current (p. 157).** Text replaced. The
  making ability is proven in test-duty No. 4 (6.106.4). The breaker shall make
  with pre-strike at any point on the voltage wave; two extreme cases (Figure 1):
  making at voltage peak → symmetrical current and longest pre-arc; closing at
  voltage zero → no pre-strike, fully asymmetrical current. Two requirements:
  a) close against symmetrical current = [[rated-short-circuit-breaking-current]];
  b) close against fully asymmetrical current = [[rated-short-circuit-making-current]].
  Adds three-phase and single-phase test procedures (extra CO at reduced voltage
  where pre-arcing prevents reaching rated making current). Notes: d.c. ≤ 20% is
  treated as symmetrical; pre-arcing > 10 ms may need more than two making
  operations; non-simultaneity of poles can give a higher peak in one pole.
- **6.104.3 Short-circuit breaking current (p. 159).** The last paragraph is
  deleted.
- **6.104.7 Power-frequency recovery voltage (p. 173).** The third paragraph is
  deleted.

These affect [[short-circuit-test-quantities]] and [[rated-short-circuit-making-current]].

## Clause 6.105–6.106 — Procedure and basic test-duties

- **6.105.1 Time interval between tests (p. 175).** First two paragraphs amended:
  the basic short-circuit and (if applicable) short-line-fault tests consist of the
  test-duties of 6.106 and 6.109; the time intervals between individual operations
  of a test-sequence are those of the [[rated-operating-sequence]] (4.104), subject
  to the stated provisos. Affects [[short-circuit-test-procedure]].
- **6.106 Basic short-circuit test-duties (p. 177).** Amended: the basic series is
  test-duties Nos. 1 to 5. Breaking current may depart by no more than 20% (duties
  1, 2) or 10% (duty 3); peak short-circuit current in duties 4, 4b and 5 shall not
  exceed 110% of the rated short-circuit making current. For duties 1, 2, 3 the
  making operation before a breaking operation may be omitted for convenience.
- **6.106.1–6.106.3** restate Test-duties 1 (10%), 2 (30%) and 3 (60%) of rated
  breaking current, each with d.c. < 20%, citing the revised TRV / recovery-voltage
  table references (6.104.5.x, Tables XV/XVI/XVII, 6.104.7).
- **6.106.4** Test-duty No. 4 text unchanged; **6.106.4.1** adds Test-duty No. 4a
  (making tests): C-t'-C for sequence O-t-CO-t'-CO, or C-t"-C for CO-t"-CO, one
  closing against rated making current and one against a symmetrical current per
  6.104.2. **6.106.4.2** Test-duty No. 4b (breaking) unchanged.
- **6.106.5 Test-duty No. 5** restated: applies only where the time interval t0
  (per 4.101.2) is < 80 ms; three opening operations at 3 min intervals at 100%
  breaking current with the rated d.c. component; rated-operating-sequence variant
  for designs that may not latch closed; generator-vicinity high-d.c. cases by
  manufacturer/user agreement.

These affect [[test-duty]] and [[short-circuit-test]].

## Clause 6.109 — Short-line fault tests

- **6.109.5 Test-duties (p. 187).** Amended: the standard tests are a series of
  test-duties, each three opening operations at 3 min intervals — Test-duty No. L90
  at (90 ± 5)% and Test-duty No. L75 at (75 ± 5)% of rated short-circuit breaking
  current, each with the appropriate prospective TRV. Affects [[short-line-fault-test]].

## Clause 6.111 — Capacitive current switching tests

- **6.111.2 General (p. 193).** Note 5 is deleted.
- **6.111.8.1 (p. 201).** Table XX and the preceding sentence ("Breaking tests may
  alternatively be …") are deleted (this table number is then reused below).
- **6.111.9 Test results (p. 203).** The existing 6.111.9 is renumbered 6.111.10,
  and a **new 6.111.9 "Tests with specified TRV"** is inserted: as an alternative to
  the test circuits of 6.111.3–6.111.5, breaking tests may use circuits whose
  prospective recovery voltage meets specified envelope relations. For test-duties
  1 and 2 the envelope is defined by u'1, t'1, u'2, t'2 (Figure 32a) with u'1 ≤ u1,
  t'1 ≥ t1, u'2 ≥ u2, t'2 ≤ t2; for test-duties 3 and 4 by u'2 and t'2 (Figure 32b),
  with the initial part kept below the line from origin to (u1, t1). Reference
  values u1, t1, u2, t2 are given in a new **Table XX** (recovery-voltage and time
  values of Figure 32: duties 1 & 2 from 6.104.5.4, duties 3 & 4 from 4.102.3).
  These affect [[capacitive-current-switching-test]].

## Figures and appendices

- **Figures 19, 20 (pp. 236–237):** replace "E" by "U" in the bottom figures (24
  places). **Figure 28 (p. 245):** replace "E" at the top trace by "U".
  **Figures 29, 30 (p. 246):** replace "U'" by "U". These are symbol corrections
  aligning the figures with the U (rated voltage) notation.
- **Figure 32 (p. 247):** replaced by new **Figures 32a and 32b** — recovery
  voltage for capacitive current-breaking tests, test-duties 1 & 2 (32a) and 3 & 4
  (32b). Supports the new 6.111.9.
- **Appendix EE — EE1.4.1.1 Type tests (p. 279).** First two paragraphs amended:
  the tightness test is performed in conjunction with the mechanical operation test
  (6.101.2) and the low/high-temperature tests (6.101.3). An increased leakage rate
  at extreme temperatures and/or during operations is acceptable provided it resets
  to ≤ the specified value F_p after return to normal ambient temperature / thermal
  stability; the temporary leakage rate shall not exceed three times the permissible
  value F_p in either closed or open position; accumulated leakage over the complete
  mechanical endurance test shall not reach lock-out pressure. Affects
  [[mechanical-and-environmental-test]].
- **Appendix GG — Figure GG9 (p. 319).** The inequality in note item a) is replaced
  by f1 ≤ 2%.

## Referenced standards

The amendment newly cites **IEC 427 (1989)** Synthetic testing of HV a.c.
circuit-breakers (in revised 6.102.4) and reiterates the IEC 694 condition
checking test (6.1.11) as the dispute-resolution check on insulating properties.

## See also
[[iec-56]] · [[type-test]] · [[short-circuit-test]] · [[test-duty]] ·
[[short-circuit-test-quantities]] · [[short-circuit-test-procedure]] ·
[[single-phase-short-circuit-test]] · [[short-line-fault-test]] ·
[[capacitive-current-switching-test]] · [[mechanical-and-environmental-test]] ·
[[dielectric-test]] · [[rated-short-circuit-breaking-current]] ·
[[rated-short-circuit-making-current]]
