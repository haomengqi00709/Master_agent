# IEC 60617 Symbol Knowledge Graph — Schema & Maintenance Guide

This wiki is an LLM-maintained knowledge graph of the **IEC 60617 / IEC 617
"Graphical symbols for diagrams"** standard family, plus related IEC TC-3
publications. It follows the *LLM Wiki* pattern: the raw PDFs in
`../Standards-Reference/` are the immutable source of truth; everything in this
`wiki/` directory is generated and maintained by the LLM.

You (the LLM) own this directory entirely. The human curates sources and asks
questions. Read this file at the start of every session.

## Layers

- **Raw sources** — `../Standards-Reference/*.pdf`. Scanned image PDFs (no text
  layer). Read via vision; see "Ingest pipeline" below. Never modified.
- **The wiki** — this directory. Interlinked markdown.
- **The schema** — this file. Co-evolve it as conventions are refined.

## Directory layout

```
wiki/
  CLAUDE.md                 # this file
  index.md                  # catalog of every page (the navigation entry point)
  log.md                    # append-only chronological log of operations
  standards/<id>.md         # one page per publication/part  (e.g. 60617-3.md)
  sections/<id>.md          # one hub page per section        (e.g. 60617-3-1-conductors.md)
  symbols/<PP-SS-NN>.md     # one KG node per symbol           (e.g. 03-01-01.md)
  concepts/<slug>.md        # cross-cutting concept pages      (e.g. single-line-representation.md)
  assets/<std>/pNN.png      # upright page images for embedding
```

## The graph model

Nodes (each = one markdown file):

| Node type | File | Example |
|-----------|------|---------|
| **Symbol** | `symbols/PP-SS-NN.md` | `03-01-01.md` — the core KG node |
| **Standard / Part** | `standards/<id>.md` | `60617-3.md` |
| **Section** | `sections/<id>.md` | `60617-3-1-conductors.md` |
| **Concept** | `concepts/<slug>.md` | `single-line-representation.md` |

Edges = wikilinks (`[[target]]`). Standard edge types, expressed in the symbol
frontmatter and body:

- `in_section` — symbol → its section
- `in_part` — symbol → its standard/part
- `form_of` / `variant_of` — alternative drawing of the same concept (e.g.
  `[[03-01-02]]` Form 1 ↔ `[[03-01-03]]` Form 2)
- `see_also` — related symbol (same family, derived from, contrasted with)
- `uses_concept` — symbol → concept (e.g. single-line representation)
- `references_standard` — symbol/part → another publication (e.g. IEC 445)
- `superseded_by` / `supersedes` — version relationship (e.g. 617-12 →
  `[[60617-12]]`)

## Symbol IDs

IEC 60617 symbol numbers are `PP-SS-NN` = **Part-Section-Number**, e.g.
`03-01-01` = Part 3, Section 1, item 1. Use the bare number as the node ID,
filename (`03-01-01.md`), and wikilink target (`[[03-01-01]]`). Page H1 is
`# 03-01-01 — <English name>`.

## Symbol page format

```markdown
---
id: 03-01-01
type: symbol
standard: IEC 60617-3
part: 3
section: 1
edition: "1st edition, 1983"
name_en: Conductor
name_fr: Conducteur
aliases: [Group of conductors, Line, Cable, Circuit, Transmission path]
forms: []                 # ids of alternate forms, if any
see_also: []              # related symbol ids
uses_concept: []          # concept slugs
references: []            # other standard ids referenced
source: "Publication No.617-3.pdf, printed p.4"
tags: [conductor]
---

# 03-01-01 — Conductor

![symbol](../assets/60617-3/p03.png)

**Standard:** [[60617-3]] · **Section:** [[60617-3-1-conductors]]

## Description
<full English description, verbatim where possible>

## Names
- **EN:** Conductor / Group of conductors / Line / Cable / Circuit / Transmission path
- **FR:** Conducteur / Groupe de conducteurs / Ligne / Câble / Circuit / Ligne de propagation

## Notes
<any IEC notes attached to the symbol>

## Related
- [[03-01-02]], [[03-01-03]] — three-conductor forms
- uses [[single-line-representation]]
```

Symbol image policy depends on the part's table regularity:
- **Uniform tables** (one symbol per row, no intro text) — e.g. 60617-2, 60617-3:
  embed the **per-symbol crop** `assets/<std>/sym-PP-SS-NN.png` produced by
  `tools/crop_symbols.py`, linking back to the full page.
- **Irregular tables** (intro paragraphs, notes/examples of varying height,
  text-only "use symbol X" rows, multi-form appendix grids) — e.g. 60617-7:
  the projection-based cropper cannot anchor rows reliably, so embed the **full
  page image** `assets/<std>/pNN.png` instead (the symbol is on that page;
  per-symbol cropping is deferred). Don't ship misaligned crops — a wrong image
  is worse than a page-level one. Always eyeball montages before trusting crops.

## index.md

Content-oriented catalog. Organized by category (Standards, Sections, Symbols
by part, Concepts). Each entry: `[[link]] — one-line summary`. Update on every
ingest. When answering a query, read index.md first to locate pages.

## log.md

Append-only. One entry per operation, prefixed for grep:
`## [YYYY-MM-DD] <ingest|query|lint> | <subject>`. So
`grep "^## \[" log.md | tail -5` shows recent activity.

## Ingest pipeline (scanned PDFs)

The PDFs are **scanned images, no text layer**, with **inconsistent page
rotation**. OCR (tesseract) is unreliable on the multi-column symbol tables;
**read pages visually**. Established flow (see scripts in scratchpad):

1. Render each page at ~300 dpi (PyMuPDF `get_pixmap(dpi=300)`).
2. Correct orientation to upright. tesseract OSD (`--psm 0`) catches most 90°
   rotations but misses some sparse table pages — verify visually and apply a
   manual `rotate(-90)` (clockwise) to any page left sideways.
3. Save upright page images to `assets/<std>/pNN.png` (downscaled to ~1500px).
4. Read each content page, extract every symbol: number, EN name + aliases, FR
   name, full description, notes, examples, forms.
5. Crop per-symbol images with `tools/crop_symbols.py`: it snaps the Symbol
   column to the consistent table layout (expected x-fractions, refined to
   detected rules), anchors rows on the No.-column number lines, aligns them in
   order to the known per-page ID list, and emits `sym-PP-SS-NN.png` plus a
   labelled **montage per page**. Always eyeball the montages to confirm
   crop↔ID alignment before trusting them (header-row drop and form/note
   grouping are the usual failure points).
6. Generate symbol nodes + section hubs + the part page from the extracted data
   with a per-part generator (e.g. `tools/gen_60617_3.py`) — keeps output
   consistent and re-runnable. Edit the DATA in the generator, not the output.
7. Update index.md and append to log.md.

Tooling lives in `tools/`. `crop_symbols.py` is generic given a `PAGE_IDS` map;
the `gen_*.py` generators hold each part's extracted symbol data.

Table columns are: **No. | Symbol (graphic) | Légende (FR) | Description (EN)**.
Some sections add a **Preferred form / Other form** pair of symbol columns.

## The 617 / 60617 family (from 617-3 back-matter, IEC TC-3 catalog)

| Part | Title | In collection? |
|------|-------|----------------|
| 617-1 (1985) | General information, general index, cross-correspondence | ✅ |
| 617-2 (1983) | Symbol elements, qualifying symbols & symbols of general application | ✅ |
| 617-3 (1983) | Conductors and connecting devices | ✅ (ingested) |
| 617-4 | Passive components | ❌ missing |
| 617-5 | Semiconductors and electron tubes | ❌ missing |
| 617-6 (1983) | Production and conversion of electrical energy | ✅ |
| 617-7 (1983) | Switchgear, controlgear and protective devices | ✅ |
| 617-8 (1983) | Measuring instruments, lamps and signalling devices | ✅ |
| 617-9 (1983) | Telecommunications: switching and peripheral equipment | ✅ |
| 617-10 (1983) | Telecommunications: transmission | ✅ |
| 617-11 | Architectural & topographical installation plans/diagrams | ❌ missing |
| 617-12 (1983) | Binary logic elements | ✅ (+ 12.1, 12.2 supplements) |
| 617-13 (1983) | Analogue elements | ✅ |
| **60617-12** | Binary logic elements (renumbered/expanded successor of 617-12) | ✅ |

Related TC-3 standards referenced by symbols: **IEC 445** (apparatus terminal
identification), **IEC 113** (diagrams/charts/tables), **IEC 416/417**
(graphical symbols for equipment), **IEC 750** (item designation), **IEC 1082**
(preparation of electrotechnical documents).

Note: IEC renumbered the 617 series to **60617** in 1997. Treat `60617-N` as the
later edition of `617-N` and link with `supersedes`/`superseded_by`.
