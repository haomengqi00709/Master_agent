---
id: signal-and-location-references
type: concept
standard: IEC 1082-1
aliases: [interrupted connecting lines, signal reference, location reference, cross-sheet reference]
tags: [concept, iec-1082, documentation]
---

# Signal and location references for interrupted lines (IEC 1082-1 §4)

The labelling convention IEC 1082-1 uses to **continue a connecting line that has
been interrupted** — within a sheet, across sheets, or across diagrams — so the
reader can trace the signal to where it resumes. Illustrated by Part 1 figures
62–65 (and used throughout Parts 2 and 3).

Two kinds of reference appear at a break:

- **Signal designation** — a name/identifier of the signal carried by the line
  (e.g. `GRES(H)`), so two interrupted segments carrying the same named signal are
  associated by that name rather than by being physically joined. Signal
  designations also tag the individual lines of a bundle (Part 1 figs. 70–71) and
  the conductors in a [[connection-documents-iec1082|connection]] matrix.
- **Location reference** — a coordinate/sheet pointer to **where the line
  continues**, written as a destination of the form *sheet / zone*. Examples from
  Part 1: `16/A5` (continuation in zone A5 of the same sheet), `33/A1`, `37/B6`,
  `Sh.33` (sheet 33). For continuation on **another diagram**, the reference also
  names the target diagram (e.g. `=AVS/B5`, `EF 91/2/B3`).

The two are combined at a break: a tag such as `GRES(H) 33/A1` means "the GRES(H)
signal continues at sheet 33, zone A1." Part 1 distinguishes three cases:
(a) continuation on the **same sheet** (fig. 63), (b) continuation on **another
sheet** (fig. 64), and (c) continuation on **another diagram** (fig. 65). A
companion table (Part 1's "application examples of the rules for references")
shows zone references like `4568/B3` (zone B3 of single-sheet diagram 4568) and
`5296/B4/B3` (zone B3 on sheet B4 of multi-sheet diagram 5296).

These references depend on the [[reference-designation-system]] (`=` system / `+`
location codes can appear in the destination) and on the title-block / drawing-zone
grid that gives each sheet its coordinate frame.
