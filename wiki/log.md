# Log

Append-only record of wiki operations. `grep "^## \[" log.md | tail -5` shows
recent activity.

## [2026-06-24] setup | wiki scaffolding + schema
Created the wiki structure (standards/, sections/, symbols/, concepts/, assets/)
and the schema [[CLAUDE]]. Decided: KG as an Obsidian-style markdown wiki; each
symbol = one node file; sections and parts = hub pages; edges = wikilinks.
Established the scanned-PDF ingest pipeline (300 dpi render → orientation
correction → vision read → data-driven generation).

## [2026-06-24] ingest | IEC 60617-3 — Conductors and connecting devices
Source: `Publication No.617-3.pdf` (1st edition 1983, 13 scanned pages).
Read all content pages by vision (OCR unreliable on the symbol tables). Extracted
58 symbols across 4 sections: Conductors (03-01, 15), Terminals (03-02, 14),
Connecting devices (03-03, 22), Cable fittings (03-04, 7). Generated 58 symbol
nodes, 4 section hubs, the part page [[60617-3]], and 2 concept pages
([[single-line-representation]], [[multi-line-representation]]) via
`tools/gen_60617_3.py`. Captured the IEC TC-3 publication catalog from the
back-matter into [[index#standards]]; flagged 617-4, 617-5, 617-11 as missing
from the collection, and the 617-12 → 60617-12 supersession.

## [2026-06-24] enhance | per-symbol image crops for 60617-3
Built `tools/crop_symbols.py` (numpy projections; no OpenCV available). Crops
each symbol from the Symbol column by snapping to the consistent table layout
and anchoring rows on the No.-column number lines, aligned to the known per-page
ID order. Generated all 58 `sym-03-xx-xx.png` crops; visually verified the
labelled montages for p03/p04/p06/p08 (covering section-start header-drop,
faint-border fallback, dense rows, and Preferred/Other-form sub-columns) —
alignment correct. Symbol pages now embed the per-symbol crop (with a link to
the full page); section hubs show thumbnail galleries.

## [2026-06-24] ingest | IEC 60617-2 — Symbol elements, qualifying symbols and general-application symbols
Source: `Publication No.617-2.pdf` (1st edition 1983, 35 scanned pages).
Pages had inconsistent rotation incl. 180° flips that OSD mis-called; solved with
an **OCR word-count orientation scorer** (try 4 rotations, keep the most-words
one) — added to the pipeline. Two symbol-dense pages (p23, p26) were forced to
90° after visual check. Read all 25 content pages by vision; extracted **154
symbols across 17 sections in 3 chapters** (I: Symbol elements; II: Qualifying
symbols §2–11; III: Other general-application §12–17) plus Appendix A (1 older
symbol, 02-A1-01, superseded by [[02-13-23]]). Generated nodes/section-hubs/part
page via `tools/gen_60617_2.py`; cropped via the now config-driven
`tools/crop_symbols.py`; verified montages for p10/p16/p25/p30 (intro-text
header-drop, dense rows, ground symbols) — alignment correct.
Captured cross-references: IEC 445, 27, 375, 364-3, ISO 128, and forward links
to 617-6/10/12/13 and Part-10 symbols (10-06-03/04). Wiki now holds 212 symbols
across 2 parts.

## [2026-06-24] batch-ingest | IEC 60617-6, -8, -9, -13 (parallel subagents)
Industrialised the pipeline: `tools/orient_pdf.py` (OCR-scored orientation),
`tools/gen_part.py` (generic JSON-driven generator reading `tools/data/<std>_*.json`
+ `<std>.meta.json`), and `tools/build_index.py` (auto-regenerates index.md from
frontmatter — no more hand-maintained links). For each part: render+orient in
background, fan out reader subagents over page ranges, persist their JSON, fix any
180°-flipped page images flagged by agents, generate (page-level images), rebuild
index, lint. Ingested: **60617-8** (74, measuring instruments/lamps/signalling),
**60617-9** (95, telecom switching), **60617-13** (54, analogue elements — 1993 ed,
2 printed pages per scan), **60617-6** (116, machines/transformers/converters/cells
+ Appendix A transductors). Fixed flips: 617-8 p08/p15, 617-9 p17, 617-13 p17/p20,
617-6 p06. Wiki now holds **738 symbols across 7 parts**, 102 section hubs, 2872
wikilinks (lint clean — only forward-refs to not-yet-built/missing parts 4,5,10,11,12).
Known gap: 617-13 sections 1–4 (early pages) not yet extracted (referenced by 13-04-05).

## [2026-06-24] decision | defer binary-logic parts; extract 617-1 cross-correspondence
By user decision, the binary-logic cluster (**617-12, 617-12.1, 617-12.2, and
60617-12** = 253 pp) is **deferred to a dedicated session** — those use a
different logic-notation format (dependency notation, not the 4-column symbol
tables), and 60617-12 is far larger than everything done so far. They remain ✅
in-collection but un-ingested. Proceeding to extract only the **cross-correspondence
table from 617-1** (legacy IEC 117 ↔ new IEC 617 number mapping).

## [2026-06-24] ingest | IEC 60617-1 — cross-correspondence (IEC 617 ↔ 117)
Rendered 617-1 (83 pp). Section 2 is the alphabetical general index (term → 617
number → IEC 750 item-designation letter); Section 3 (printed pp. 75–89) is the
617↔117 cross-correspondence. Three subagents extracted ~1300 structured rows,
but the dense number-tables transcribe unreliably (the two reciprocal sort-orders
disagreed on some cells). Decision: the **authoritative deliverable is the source
table itself** — created reference page [[cross-correspondence-iec117]] embedding
the 15 re-oriented source pages (`assets/60617-1/cc-p*.png`) plus a part page
[[60617-1]]. NOTE on orientation: `orient_pdf.py`'s OCR-word-count scorer
mis-rotates number-only pages, so for 617-1 I rendered the cross-corr pages
**fresh with no rotation** (PyMuPDF's embedded /Rotate is correct). The
machine-extracted structured rows remain available to persist to JSON on request.

Final state of this session: **8 parts represented** (7 symbol parts ingested +
60617-1 index/cross-ref), **738 symbol nodes**, 102 section hubs, 3 concept/ref
pages, 439 image assets, 2883 wikilinks (lint clean). Deferred: binary-logic
parts (617-12, 12.1, 12.2, 60617-12) and the normal symbol part **617-10**
(Telecommunications: transmission, 51 pp) — heavily forward-referenced (10-xx),
a good next target.

## [2026-06-24] ingest | IEC 60617-7 — Switchgear, controlgear and protective devices
Source: `Publication No.617-7.pdf` (1st edition 1983, 54 scanned pages — the
largest part so far). Oriented all pages with the OCR word-count scorer; forced
p18/p27/p42 to 90° after the scorer mis-called them. **Extraction parallelized**:
five reader subagents each read a page range and returned strict JSON; agent A's
reading of p06–p09 exactly matched a manual reading (accuracy cross-check). Merged
into `tools/data/p7_*.json` and generated via `tools/gen_60617_7.py`: **187 symbols
across 24 sections + Appendix A (A1–A3 older symbols)** — contacts, switches,
contactors, breakers, disconnectors, relays/coils, measuring relays, fuses,
arresters, starters. Heavy cross-references into [[60617-2]] (02-12/02-13
operating symbols) all resolve.
Per-symbol cropping was attempted but **abandoned for this part**: 617-7's tables
are too irregular (intro text, variable-height notes/examples, text-only "use
07-02-01" rows, appendix form-grids) for the projection cropper — montages of
p06/p27 showed row shifts. Switched 617-7 to **page-level images** (reliable) and
recorded the policy in [[CLAUDE]]. Wiki now holds 399 symbols across 3 parts;
1573 wikilinks, lint clean (only intentional forward-refs to Part-10 symbols and
the 60617-12 placeholder).
