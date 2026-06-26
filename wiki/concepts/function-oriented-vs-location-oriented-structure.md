---
id: function-oriented-vs-location-oriented-structure
type: concept
standard: IEC 1082-1
aliases: [function-oriented structure, location-oriented structure]
tags: [concept, iec-1082, documentation]
---

# Function-oriented vs location-oriented structure (IEC 1082-1 §3)

The two complementary ways IEC 1082-1 lets a project's items and documents be
**hierarchically organised**, and the choice that drives which
[[reference-designation-system|designation prefix]] dominates a set of documents.
Part 1's figures 34 and 35 present the *same* steelworks plant under each scheme.

- **Function-oriented structure** — items are grouped by **what they do**, breaking
  the plant into systems and sub-systems regardless of where they sit. The tree is
  built on `=` **function/system** codes: e.g. an *electric-power distribution
  system* `=E1`, a *cooling-water supply system* `=W11`, a *pumping system* `=P1`,
  each decomposed into sub-systems and finally into items (`-S0` pushbutton/stop,
  `-Q1` motor starter, …). This is the structure of the
  [[function-oriented-diagrams|function-oriented diagrams (Part 2)]]; an
  [[unit-connection-diagram|overview]] following it (Part 1 figs. 14–15) shows the
  signal/energy flow between functions.
- **Location-oriented structure** — items are grouped by **where they physically
  are**: plant → control desk → section → unit. The tree is built on `+`
  **location** codes: e.g. a *plant* containing a *control desk* `+PA`, broken into
  *sections* `+1`, `+2`, each containing a *motor starter* `+2A`, a *pump set*
  `+2A`, a *switchboard* `+5A`. This is the structure of the location/installation
  documents (the still-unissued Part 4) and of the physical layout in
  [[connection-documents-iec1082|connection diagrams (Part 3)]].

The two structures are **not exclusive** — a real item has both a function code and
a location code, so its full reference reads `=system+location-item` (see
[[reference-designation-system]]). Part 1 also shows (figure 37) the parallel
**function / software / physical assembly** hierarchies and how their documents
(function documents, program/data documents, equipment & installation documents)
relate. Figure 35 additionally annotates a function-oriented structure with the
**extent of the overview vs circuit diagrams**, showing how the document set tiles
the function tree.
