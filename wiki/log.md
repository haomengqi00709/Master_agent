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

## [2026-06-25] realign | LLM-Wiki pattern fix + standards as concept pages
Caught drifting from the LLM-Wiki pattern (the user flagged it): (1) had built a
TF-IDF/vector RAG layer — the pattern explicitly REPLACES embedding-RAG with
LLM-navigation of the wiki; (2) had represented a standard as one monolithic page
instead of decomposing it. Corrected both. Deleted the RAG infra
(build_corpus.py, retrieval.py, vectors). Rewrote the app's /api/ask and /api/sow
as **wiki-navigation agents** (read index.md → search_wiki/read_pages tools →
follow links → cite). Codified the doctrine as a "★ READ FIRST" section atop
[[CLAUDE]] (decompose into entity/concept pages, 10-15 per source; query =
navigation not RAG; full Lint).
Ingested two non-60617 standards as documents, decomposed per the method:
- [[iec-79-19]] (Ex repair/overhaul, 46 pp) → 1 standard + 11 concept pages
  (repair/overhaul/maintenance/reclamation/modification/copy-winding + 5
  type-of-protection pages), cross-linked to motor/winding/enclosure symbols.
- [[iec-56]] (HV AC circuit-breakers, 182 pp) → 1 standard + 16 concept pages
  (circuit-breaker + rated-* characteristics + TRV + test-duty/type-test +
  making-and-breaking-capacity + operating-mechanism), cross-linked to
  switchgear symbols (07-13-05, 07-01-02…). Wiki now 880 nodes; the app's
  "Standards (docs)" view shows both standards with their concept clusters.

## [2026-06-25] lint+ingest | IEC 79-19 re-decomposed (under-decomposition fix #2)
Applied the same red-flag check that caught IEC 56 to [[iec-79-19]]: 46 pp dense
repair standard had only 11 concept pages — under-decomposed. The standard is a
**matrix** (type of protection clause × component). Mined its own structure:
- definitions clause 2.2 has 18 terms → added 7 missing definition pages
  ([[serviceable-condition]], [[component-part]], [[manufacturer]], [[user]],
  [[repairer]], [[certification]], [[certificate-references]]);
- the substance is **per-component repair guidance** → added 21 component pages
  ([[enclosures]], [[windings]], [[terminations]], [[insulation]],
  [[rotors-and-stators]], [[shafts-and-housings]], [[sleeve-bearings]],
  [[cable-and-conduit-entries]], [[light-transmitting-parts]],
  [[encapsulated-parts]], [[batteries]], [[lamps]], [[lampholders]], [[ballasts]],
  [[optocouplers]], [[internal-wiring]], [[transformers]], [[non-electrical-parts]],
  [[auxiliary-equipment]], [[threaded-holes-for-fasteners]], [[testing-after-repair]]),
  each synthesising the requirement across all protection types that address it.
Content extracted faithfully from the OCR by two parallel reader subagents
(clauses 3–4 and 5–7), clause-cited. Generated by `tools/gen_iec79_19.py`.
**Contradiction fixed (real Lint find):** the hub + type pages had clause 4↔6
swapped for "e"/"i" — OCR confirms clause 4 = type "i" (intrinsic safety),
clause 6 = type "e" (increased safety). Corrected d=3, i=4, p=5, e=6, n=7.
Result: 79-19 = 1 hub + **39 concept pages** (was 11). Graph 967 nodes
(concept 88→116). Lint: orphans none; all 39 pages linked from hub; only the
documented forward-refs to un-ingested parts (60617-10/12, Parts 4/5, 617-13 §1–4)
remain. Both spec standards now properly decomposed (IEC 56 = 60+, 79-19 = 39).

## [2026-06-25] enrich | IEC 56 concept pages — depth pass (stub→synthesis)
User flagged the wiki content was too thin ("基本没有"). Measured: IEC 56's 75
concept pages averaged ~29 words (21 were <25-word stubs) vs the 79-19 component
pages at ~134 words. Root cause recorded in [[CLAUDE]] rule 2 + "Common mistakes
(d)": the doctrine I wrote over-stressed PAGE COUNT (breadth) and never required
per-page DEPTH; IEC 56 had been batch-generated from one-line IEV definitions —
the exact stub-producing shortcut. The original LLM Wiki.md is all about
*synthesis* / "a rich companion wiki".
Fix: read the actual clauses. 7 parallel reader subagents over corpus/iec-56.txt
(clause 3 definitions / clause 4 ratings / clause 6 tests), each returning an
80–150-word clause-cited synthesis per concept — definition + real requirements/
standard values (R10 current series, O-t-CO-t' sequences, 2.5×/2.6× making-current
factors, TRV envelopes, test-duty percentages) + relationships + applicable tests.
Stored as tools/data/iec56_rich_*.json; applied by tools/apply_iec56_rich.py
(preserves frontmatter/H1/symbol links, bolds any dangling wikilink).
Result: all 75 pages enriched, **avg 29 → 131 words, 0 stubs**. Graph 967 nodes,
edges 5322→5468 (denser concept-concept linking). Lint clean (only documented
forward-refs). Doctrine + memory updated so future ingests do breadth × depth.
Remaining thin spot (separate, larger): 487/738 symbol pages whose Description ==
name — deferred; many symbol-table rows have no source text beyond the name.

## [2026-06-25] feature | Ask AI / SOW via local Claude CLI (no API key) + frontend body render
Two frontend/backend fixes after the user couldn't see enriched content / wanted local AI testing:
1. **Detail panel rendered nothing for concept/standard pages** — it only extracted a
   `## Description` section (symbols have it, concept/standard pages don't), so their rich
   bodies were invisible. Added `renderBody()` (renders ## / - / **bold** / clickable
   wikilinks) and a `renderAnswer()` for Ask/SOW answers. Backend now serves index.html
   with `Cache-Control: no-cache` so frontend edits show on a normal reload.
2. **Local AI with no ANTHROPIC_API_KEY**: backend `ai_mode()` = api (SDK) → cli (local
   `claude` binary) → off. New `claude_cli_agent()` shells out to `claude -p` with cwd=wiki,
   `--allowedTools Read Grep Glob`, navigation system prompt; the CLI reads index.md, greps,
   follows wikilinks, and (bonus) picks up wiki/CLAUDE.md. Citations parsed from inline [id]
   refs + a `CITED:` line, resolved against NODES. /api/health reports mode + "Claude CLI".
   On deploy (no CLI) others just set ANTHROPIC_API_KEY → SDK path. Tested: "what does symbol
   07-13-05 represent + which standard defines its ratings/tests" → in 35 s the CLI linked
   07-13-05 → [[circuit-breaker]] → [[iec-56]], quoted R10 current series from the enriched
   pages, cited 13 pages. Confirms symbol↔standard linking works and the depth enrichment pays off.

## [2026-06-25] validation + feature | 5-SOW gold-standard test + History tab
Ran a 5-SOW validation suite (field-language SOWs that never quote the standards or
mention symbols), each with a pre-authored gold standard (expected pages + traps):
1 breaker fault/TRV, 2 capacitive switching, 3 Ex-d motor overhaul, 4 Ex e-vs-i,
5 multi-device bay. Result: 5/5 full concept recall, full symbol recall, 10/10
traps pass. Verified substantively: e=clause6 / i=clause4 reproduced correctly
(the fixed bug holds), TRV reached+explained, no hallucinated capacitor symbol.
One honest weakness: it does not proactively announce coverage boundaries (SOW2
stayed silent that the power-capacitor symbol is in the un-ingested 60617-4).
Added a **History tab**: backend appends every /api/ask and /api/sow run to
data/history.jsonl (best-effort); GET /api/history (newest-first) + DELETE clears.
Frontend History tab stacks runs (kind badge, ts, query, rendered answer, trace,
usage, cited-page chips) — a shared internal review log. Backfilled the 5
validation runs (citations reconstructed from answers; trace not retained for those).

## [2026-06-25] ingest | IEC 56 Amendment 1 (1992-11)
Ingested Amendment 1 to IEC 56 (corpus/iec-56-1.txt). Per the method an amendment
gets no standard hub: created concepts/iec-56-amendment-1.md with a clause-by-clause
summary of the changes (clauses 4.101.2, 6 intro, 6.1.7, 6.101.1.3/3.3/3.4, 6.102.4/
8.1/9, 6.104.2/3/7, 6.105.1, 6.106(+4a), 6.109.5, 6.111.2/8.1/9, Figs 19/20/28/29/30/
32→32a-b, Appx EE EE1.4.1.1, Appx GG Fig GG9; cites IEC 427 + IEC 694 6.1.11).
Added an "## Amendments" section to standards/iec-56.md and an "Amended (1992, Amd. 1)"
line to 11 affected concept pages: rated-short-circuit-breaking-current, type-test,
dielectric-test, mechanical-and-environmental-test, short-circuit-test,
short-circuit-test-procedure, short-circuit-test-quantities,
rated-short-circuit-making-current, test-duty, single-phase-short-circuit-test,
short-line-fault-test, capacitive-current-switching-test. Registered the new page in
index.md (under iec-56 and in the concept list). No new defined terms/ratings in the
amendment, so no genuinely-new concept page was warranted (Test-duty No. 4a / 4b and
SLF duties L90/L75 are folded into the existing test-duty + short-line-fault-test pages).

## [2026-06-25] ingest | IEC 56-2 (3rd ed, 1971) Part 2: Rating
Ingested IEC Publication 56-2 (corpus/iec-56-2.txt), the standalone ratings part of
the earlier six-part edition of IEC 56. Treated as an earlier edition of the 4th-ed
clause-4 ratings (NOT a parallel standard) per the no-duplication rule. Created one
concept page concepts/iec-56-2-rated-characteristics.md (tags concept/iec-56/ratings):
states what Part 2 is, its 1.1/1.2/1.3 three-tier list of rated characteristics, the
relationship to the consolidated 4th edition, and indexes every corresponding rated-*
concept page via wikilinks. Enriched 3 existing pages with substantive Part-2 detail
genuinely missing from them: rated-voltage (added the standard rated-voltage value
lists, Series I/II ≤72.5 kV and the above-72.5 list to 765 kV + 550 kV NA note, §2);
rated-duration-of-short-circuit (added the standard 1 s / 3 s values, §10); short-line-
fault (added Table VII surge impedances 480/375/330 Ω with peak factors by conductors,
the Amd.1-to-56-2 single 450 Ω / k=1.6 revision, and the Appendix A SLF-TRV derivation,
§8). Added "## Related parts / editions" to standards/iec-56.md linking the new page;
registered it in index.md (under the iec-56 standard entry and in the concept list).
Content already fully covered (no change): rated-insulation-level, rated-frequency,
rated-normal-current, rated-short-circuit-breaking-current, transient-recovery-voltage,
rated-short-circuit-making-current, rated-operating-sequence, rated-line-charging /
rated-cable-charging / capacitor / small-inductive / out-of-phase breaking-current pages.
The 56-2 supply-voltage/frequency (Tables X-XII), compressed-gas pressure (§20) and
co-ordination tables (§21) clauses are noted within the new page; no separate stub
pages created (they are minor/non-mandatory and the 4th-ed equivalents defer to IEC 694).

## [2026-06-25] ingest | IEC 56 supplements + IEC 79 Ex-protection family (Claude, one-by-one)
Traversing the remaining un-ingested source PDFs with thorough Claude subagents.
- **IEC 56 Amendment 1 (1992)** → folded into [[iec-56]] per the amendment pattern:
  new [[iec-56-amendment-1]] summary page + 11 affected concept pages annotated
  (20 clauses; corrigenda + test-procedure revisions, no new standalone concepts).
- **IEC 56-2 "Part 2: Rated characteristics" (3rd ed)** → [[iec-56-2-rated-characteristics]]
  + enriched [[rated-voltage]]/[[rated-duration-of-short-circuit]]/[[short-line-fault]]
  with genuinely-missing value tables; rest already covered (no duplication).
- **IEC 79 family** (new sibling standards of [[iec-79-19]], parallel Claude subagents,
  each writing only its own files):
  - [[iec-79-3]] Spark-test apparatus (intrinsic safety) — 18 concept pages (source-grounded).
  - [[iec-79-4]] (+ [[iec-79-4a]] amendment) Ignition-temperature test method — 15 pages (grounded).
  - [[iec-79-18]] Encapsulation "m" — 24 pages + new [[type-of-protection-m]] (grounded).
  - [[iec-79-1]] Flameproof "d" — 21 pages BUT ⚠ the local PDF is front-matter only
    (5 pp, no clause body); pages reconstructed from structure/knowledge, NOT the source.
    Hub carries a PROVENANCE warning; pending a full PDF or a decision to remove.
Graph now 1051 nodes (concept 118→196, standards 10→14). Lint clean (only documented
forward-refs incl. not-yet-ingested 79-0/79-2/79-11). Background-OCR'd all 19 remaining
text standards. Still pending: 529, 73, 99, reference/doc set, 617-10, binary-logic cluster.

## [2026-06-25] ingest | IEC 529 (IP code), IEC 73 (colours), IEC 99-1/99-4 (surge arresters)
Continued the traversal (Claude subagents, source-grounded, one family at a time):
- **IEC 529** "Degrees of protection (IP Code)" → [[iec-529]] + 22 concept pages
  (IP first numeral 0–6, second numeral 0–8, additional/supplementary letters, tests).
  529-1=2nd ed (IP Code), 529-2=1st ed (1976). Cross-linked to [[iec-79-19]] IP54 entries.
- **IEC 73** "Colours of indicator lights and push-buttons" → [[iec-73]] + 21 pages
  (red/yellow/green/blue/white meanings, push-button colours). 73-1 = partial re-scan
  of same edition (no new content). Cross-linked to [[08-10-01]] lamp, [[07-07-02]] push-button.
- **IEC 99-1** non-linear-resistor (gapped) arresters → [[iec-99-1]] + 27 pages (99-1A
  amendment folded in). **IEC 99-4** metal-oxide (gapless) arresters → [[iec-99-4]] + 37 pages.
  Both cross-linked to arrester symbol [[07-22-03]] / gap [[07-22-01]].
NOTE/LESSON: 99-1 and 99-4 share many arrester concepts; run in parallel they edited
each other's pages — verified no clobbering (frontmatter intact, both contents present,
0 broken links) but henceforth overlapping standards go SEQUENTIAL not parallel.
Also: IEC 79-1 reconstructed pages REMOVED (source was front-matter only); hub is a stub.

## [2026-06-25] ingest | reference/documentation standards (IEC 1082, 113-1, 387, 750)
Final text-standard batch (Claude subagents, strict create-only to avoid parallel races):
- **IEC 1082** "Preparation of documents used in electrotechnology" (Parts 1/2/3) →
  [[iec-1082]] + 16 pages (document classes, the =/+/-/: reference-designation system,
  function- vs location-oriented diagrams, connection/cable diagrams).
- **IEC 113-1** "Diagrams, charts, tables" → [[iec-113-1]] + 20 pages (diagram/chart/table
  definitions & representation classes; superseded by IEC 1082, noted).
- **IEC 387** "Symbols for a.c. electricity meters" (TC-13) → [[iec-387]] + 26 pages
  (meter measuring-element/unit/tariff/auxiliary symbols), cross-linked to 60617-8 meters.
- **IEC 750** "Item designation in electrotechnology" → [[iec-750]] + 10 pages (the =/+/-/:
  designation blocks, kind-of-item letter codes). NOTE: 750 OCR was badly garbled (rotated
  multi-column); Table I letter codes partly reconstructed from legible parts + canonical
  set — flagged in-page. 1082/113 slug collision avoided (distinct slugs, both coexist).
ALL 14 remaining TEXT/spec standards now ingested. Graph 1217 nodes (354 concepts,
22 standards), lint clean. Remaining: symbol parts 617-10 (vision) + binary-logic cluster.

## [2026-06-26] ingest | IEC 60617-10 Telecommunications: Transmission (vision pipeline)
Symbol part via the vision pipeline (render+orient → 5 parallel Claude vision-readers
over page ranges → gen_part). **232 symbols across 24 sections** (10-01-01…10-24-02):
lines/circuits, antennas & radio/space stations, microwave components (waveguides,
1-/2-/multi-port devices, couplers, masers/lasers), signal generators, amplifiers,
networks, modulators, concentrators/multiplexers, frequency/spectrum symbols, fibre
optics. Page-level images (assets/60617-10/p*.png). Section titles from a dedicated
header-scan subagent. Graph 1474 nodes (970 symbols, 23 standards). Previously-broken
forward-refs 10-06-03/04, 10-15-01/02 and the [[60617-10]] hub now RESOLVE. Remaining
broken links = only forward-refs to genuinely-missing parts 617-4/5 + the known 617-13
§1–4 gap. Last remaining: binary-logic cluster 60617-12 (253pp, dependency notation).
