# IEC 60617 Symbol Knowledge Graph

An interactive knowledge graph of the **IEC 60617 "Graphical symbols for diagrams"**
standards — built from scanned IEC PDFs into a structured, searchable, interlinked
symbol library, with a web app to browse the graph, search, and ask questions.

**738 symbol nodes** across 7 ingested parts (60617-2, -3, -6, -7, -8, -9, -13)
plus the 60617-1 index / IEC 617↔117 cross-correspondence. ~2,900 links.

## What's here

```
wiki/                     # the knowledge base (source of truth — markdown + images)
  symbols/  sections/  standards/  concepts/  assets/
  CLAUDE.md               # schema / conventions; tools/ has the build scripts
kg-app/
  backend/  main.py       # FastAPI: /api/graph /api/symbol /api/search /api/ask /assets
            build_kg.py    # parses wiki/ -> graph.json + kg.sqlite (FTS5)
  frontend/dist/index.html # self-contained UI (force-graph + search + Q&A)
Procfile, requirements.txt # Railway / Nixpacks deploy config
```

The wiki is the **source of truth**; `build_kg.py` compiles it into the derived
data the app serves. Re-run it whenever the wiki changes.

## Run locally

```bash
cd kg-app && ./run.sh        # builds data, serves on http://127.0.0.1:8077/
```

## Deploy on Railway

1. Create a new Railway project → **Deploy from GitHub repo** → pick this repo.
2. Railway auto-detects Python (`requirements.txt`) and runs the `Procfile`
   (`build_kg.py` then `uvicorn` on `$PORT`). No extra config needed.
3. Open the generated URL — the app is served at `/`.

### Optional: enable AI Q&A
The **Ask AI** tab does retrieval-augmented Q&A. Without a key it returns the
retrieved symbols only. To enable Claude answers, add a Railway variable:

- `ANTHROPIC_API_KEY` = your Anthropic key
- `KG_MODEL` *(optional)* = model id, default `claude-sonnet-4-6`

## API

| Endpoint | Purpose |
|----------|---------|
| `GET /api/health` | status + node/edge counts |
| `GET /api/graph?part=&type=` | nodes + edges for the graph |
| `GET /api/symbol/{id}` | symbol detail + neighbours |
| `GET /api/search?q=&limit=` | full-text search (FTS5) |
| `POST /api/ask {question,k}` | RAG answer + citations |
| `GET /assets/...` | symbol images |

> Source PDFs (IEC standards, copyrighted) are intentionally **not** included in
> this repo; the app runs entirely off the derived `wiki/` content.
