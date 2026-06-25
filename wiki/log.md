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
   [[links]]) and a `renderAnswer()` for Ask/SOW answers. Backend now serves index.html
   with `Cache-Control: no-cache` so frontend edits show on a normal reload.
2. **Local AI with no ANTHROPIC_API_KEY**: backend `ai_mode()` = api (SDK) → cli (local
   `claude` binary) → off. New `claude_cli_agent()` shells out to `claude -p` with cwd=wiki,
   `--allowedTools Read Grep Glob`, navigation system prompt; the CLI reads index.md, greps,
   follows [[links]], and (bonus) picks up wiki/CLAUDE.md. Citations parsed from inline [id]
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
