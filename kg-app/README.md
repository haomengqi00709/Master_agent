# IEC 60617 Symbol KG — app

Interactive knowledge-graph app over the markdown wiki (`../wiki`, the source of truth).

## Architecture
```
../wiki (markdown)  →  backend/build_kg.py  →  backend/data/{graph.json, kg.sqlite}
                                                      │
                       FastAPI (backend/main.py): /api/graph /api/symbol/{id}
                       /api/search /api/ask /assets  +  serves frontend/dist
                                                      │
                       frontend/dist/index.html (force-graph + search + Q&A)
```
The derived data (`backend/data/`) is a **build artifact** — never hand-edit it.
Re-run `build_kg.py` whenever the wiki changes.

## Run
```bash
cd kg-app && ./run.sh           # builds data, starts server on :8077
# open http://127.0.0.1:8077/
```
Port 8000 is used by another local service — this app defaults to **8077**
(override with `PORT=xxxx ./run.sh`).

## AI Q&A
The "Ask AI" tab does RAG: full-text-retrieve relevant symbols → Claude answers
with citations. It works in **retrieval-only** mode with no key; set
`ANTHROPIC_API_KEY` (and optionally `KG_MODEL`, default `claude-sonnet-4-6`) to
enable LLM answers.

## Stack
FastAPI · SQLite FTS5 · vanilla JS + force-graph (self-contained, no npm build).
To migrate to a full Vite/React frontend later, point it at the same `/api`.

## Endpoints
- `GET /api/health`
- `GET /api/graph?part=&type=` — nodes + edges (filtered)
- `GET /api/symbol/{id}` — node + grouped neighbours
- `GET /api/search?q=&limit=` — FTS5 (AND→OR fallback)
- `POST /api/ask {question,k}` — RAG answer + citations
