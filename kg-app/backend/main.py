#!/usr/bin/env python3
"""FastAPI backend for the IEC 60617 symbol KG.

Serves the graph, symbol detail, full-text search, RAG Q&A (Claude), and the
symbol images. Reads the derived data layer built by build_kg.py.

Run:  uvicorn main:app --reload --port 8000
Env:  ANTHROPIC_API_KEY (optional — enables LLM answers; otherwise /ask returns
      retrieval-only results).  KG_MODEL (default claude-sonnet-4-6).
"""
import os, re, json, sqlite3, shutil, subprocess, datetime
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
HIST = os.path.join(DATA, "history.jsonl")  # append-only log of Ask/SOW runs (shared review log)
WIKI = os.path.abspath(os.path.join(HERE, "..", "..", "wiki"))
ASSETS = os.path.join(WIKI, "assets")
MODEL = os.environ.get("KG_MODEL", "claude-sonnet-4-6")
# Local Claude Code CLI fallback: lets the wiki-navigation agent run WITHOUT an
# ANTHROPIC_API_KEY by shelling out to the user's `claude` CLI (uses its own auth).
# Disable with KG_NO_CLAUDE_CLI=1.
CLAUDE_BIN = None if os.environ.get("KG_NO_CLAUDE_CLI") else shutil.which("claude")

def ai_mode():
    """'api' = Anthropic SDK (needs key); 'cli' = local claude CLI; 'off' = keyword only."""
    if os.environ.get("ANTHROPIC_API_KEY"): return "api"
    if CLAUDE_BIN: return "cli"
    return "off"

GRAPH = json.load(open(os.path.join(DATA, "graph.json")))
NODES = {n["id"]: n for n in GRAPH["nodes"]}
WIKI = os.path.abspath(os.path.join(HERE, "..", "..", "wiki"))

def read_index():
    try: return open(os.path.join(WIKI, "index.md")).read()
    except Exception: return ""

def page_markdown(pid):
    """Full markdown of a wiki page (the LLM-maintained source-of-truth content)."""
    n = NODES.get(pid)
    if n and n.get("body"): return f"# {pid}\n{n['body']}"
    for sub in ("symbols", "sections", "standards", "concepts"):
        p = os.path.join(WIKI, sub, pid + ".md")
        if os.path.exists(p): return open(p).read()
    return None

def db():
    c = sqlite3.connect(os.path.join(DATA, "kg.sqlite"))
    c.row_factory = sqlite3.Row
    return c

app = FastAPI(title="IEC 60617 KG API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
if os.path.isdir(ASSETS):
    app.mount("/assets", StaticFiles(directory=ASSETS), name="assets")

STOP = {"the","a","an","of","to","is","are","how","what","which","do","does","for",
        "in","on","and","or","with","that","this","it","be","as","by","symbol","iec"}

def _tokens(q):
    return [t for t in re.findall(r"\w+", (q or "").lower()) if len(t) > 1]

def fts_query(con, q, cols, limit):
    """FTS5 search: try AND (precise) first, fall back to OR (recall).
    The `search` virtual table has columns id,type,label,name_en,name_fr,body only."""
    toks = _tokens(q)
    if not toks:
        return []
    content = [t for t in toks if t not in STOP] or toks
    for joiner in (" ", " OR "):
        m = joiner.join(f'"{t}"' for t in content)
        try:
            rows = con.execute(
                f"SELECT {cols} FROM search WHERE search MATCH ? ORDER BY rank LIMIT ?",
                (m, limit)).fetchall()
        except sqlite3.OperationalError:
            rows = []
        if rows:
            return rows
    return []

@app.get("/api/health")
def health():
    mode = ai_mode()
    return {"ok": True, "nodes": len(GRAPH["nodes"]), "edges": len(GRAPH["edges"]),
            "llm": mode != "off", "mode": mode,
            "model": MODEL if mode == "api" else ("Claude CLI" if mode == "cli" else None)}

@app.get("/api/graph")
def graph(part: str = Query(None), type: str = Query(None), docs: bool = Query(False)):
    """Lightweight graph for visualisation (no full body text). docs=1 shows the
    document standards (non-60617, e.g. iec-79-19) together with their 1-hop
    neighbourhood — the symbols/concepts they cross-link to."""
    keep = ["id","type","label","part","section","is_example","form","image"]
    nodes = GRAPH["nodes"]
    if docs:
        seeds = {n["id"] for n in nodes if n["type"] == "standard" and not n["id"].startswith("60617")}
        ego = set(seeds)
        for e in GRAPH["edges"]:
            if e["source"] in seeds: ego.add(e["target"])
            if e["target"] in seeds: ego.add(e["source"])
        nodes = [n for n in nodes if n["id"] in ego]
    elif part:
        nodes = [n for n in nodes if n.get("part") == part]
    elif type:
        nodes = [n for n in nodes if n.get("type") == type]
    ids = {n["id"] for n in nodes}
    edges = [e for e in GRAPH["edges"] if e["source"] in ids and e["target"] in ids]
    return {"nodes": [{k: n.get(k) for k in keep} for n in nodes], "edges": edges}

@app.get("/api/symbol/{nid}")
def symbol(nid: str):
    n = NODES.get(nid)
    if not n: raise HTTPException(404, f"node {nid} not found")
    # neighbours grouped by edge type, with direction
    nb = {"out": [], "in": []}
    for e in GRAPH["edges"]:
        if e["source"] == nid and e["target"] in NODES:
            t = NODES[e["target"]]
            nb["out"].append({"id": t["id"], "label": t["label"], "type": e["type"], "ntype": t["type"], "image": t.get("image","")})
        elif e["target"] == nid and e["source"] in NODES:
            s = NODES[e["source"]]
            nb["in"].append({"id": s["id"], "label": s["label"], "type": e["type"], "ntype": s["type"], "image": s.get("image","")})
    return {"node": n, "neighbors": nb}

@app.get("/api/search")
def search(q: str, limit: int = 25):
    con = db()
    rows = fts_query(con, q,
        "id,type,label,name_en,name_fr,snippet(search,5,'<b>','</b>','…',12) AS snip", limit)
    con.close()
    out = []
    for r in rows:
        d = dict(r); n = NODES.get(r["id"], {})
        d["part"] = n.get("part", ""); d["section"] = n.get("section", "")
        d["image"] = n.get("image", "")
        out.append(d)
    return {"results": out}

class Ask(BaseModel):
    question: str

class SOW(BaseModel):
    text: str

def fts_pages(query, k=14):
    con = db()
    rows = fts_query(con, query, "id,type,label", k)
    con.close()
    return [{"id": r["id"], "label": r["label"], "type": r["type"],
             "image": NODES.get(r["id"], {}).get("image", "")} for r in rows]

WIKI_TOOLS = [
    {"name": "search_wiki",
     "description": "Keyword-search the wiki; returns matching page ids with type and label.",
     "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
    {"name": "read_pages",
     "description": "Return the full markdown of given wiki page ids (symbols like 07-13-05, "
                    "sections, standards like iec-79-19, concepts).",
     "input_schema": {"type": "object", "properties": {"ids": {"type": "array", "items": {"type": "string"}}}, "required": ["ids"]}},
]

def wiki_agent(task, framing, max_steps=6):
    """The LLM navigates the curated wiki: reads the index, searches/reads pages,
    follows [[links]], and reasons. Faithful to the LLM-Wiki pattern — no
    embeddings / vector RAG; the structure + index + the model's reading IS the
    retrieval. Requires ANTHROPIC_API_KEY."""
    import anthropic
    client = anthropic.Anthropic()
    sysp = (framing + " You answer by navigating a curated wiki of IEC graphical symbols and "
            "standards. The wiki index (catalog) is provided. Use search_wiki to locate pages and "
            "read_pages to read them; follow [[links]] inside pages by reading those too. Cite pages "
            "in brackets like [07-13-05] or [iec-79-19]. Base your answer ONLY on pages you actually "
            "read. Be concise and practical.")
    messages = [{"role": "user", "content": f"WIKI INDEX (catalog):\n{read_index()[:14000]}\n\n{task}"}]
    read_ids = []
    for _ in range(max_steps):
        msg = client.messages.create(model=MODEL, max_tokens=1600, system=sysp,
                                     tools=WIKI_TOOLS, messages=messages)
        messages.append({"role": "assistant", "content": msg.content})
        if msg.stop_reason != "tool_use":
            return {"answer": "".join(b.text for b in msg.content if b.type == "text"), "pages": read_ids}
        results = []
        for b in msg.content:
            if b.type != "tool_use": continue
            if b.name == "search_wiki":
                out = fts_pages(b.input.get("query", ""), 12)
            else:
                ids = (b.input.get("ids") or [])[:12]; read_ids += ids
                out = [{"id": i, "markdown": (page_markdown(i) or "(not found)")[:1600]} for i in ids]
            results.append({"type": "tool_result", "tool_use_id": b.id,
                            "content": json.dumps(out, ensure_ascii=False)})
        messages.append({"role": "user", "content": results})
    return {"answer": "(stopped after max navigation steps)", "pages": read_ids}

def claude_cli_agent(task, framing, timeout=300):
    """Run the wiki-navigation through the local Claude Code CLI — no API key
    needed (uses the CLI's own auth). The CLI runs INSIDE the wiki dir, so it
    navigates the markdown with its own Read/Grep/Glob tools: reads index.md,
    greps, follows [[links]]. It also picks up wiki/CLAUDE.md as project context."""
    nav = (framing + "\n\nYou answer by navigating a curated wiki of IEC graphical-symbol parts and "
           "related standards — plain markdown files in the CURRENT directory (index.md is the "
           "catalog; folders symbols/ sections/ standards/ concepts/). Method: read index.md first, "
           "use Grep to locate pages and Read to read them; every [[link]] is a page file "
           "(e.g. [[07-13-05]] = symbols/07-13-05.md, [[iec-56]] = standards/iec-56.md, "
           "[[circuit-breaker]] = concepts/circuit-breaker.md) — follow the relevant ones by reading "
           "them too. Deliberately CONNECT symbols to standards via the concept pages that link both "
           "(e.g. a circuit-breaker symbol ↔ the IEC 56 concept pages). Base the answer ONLY on pages "
           "you actually read; cite them inline as [id] (e.g. [07-13-05], [iec-56]); end with one line "
           "'CITED: id1, id2, ...' listing every page id you used.")
    # stream-json + verbose so we can TRACE every tool call (Grep/Read/Glob) and
    # capture token usage, then surface both to the frontend.
    cmd = [CLAUDE_BIN, "-p", task, "--append-system-prompt", nav,
           "--allowedTools", "Read", "Grep", "Glob",
           "--output-format", "stream-json", "--verbose"]
    try:
        r = subprocess.run(cmd, cwd=WIKI, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"answer": "(the local Claude CLI timed out — try a narrower question)",
                "pages": [], "trace": [], "usage": {}}
    ans, trace, usage = "", [], {}
    for line in (r.stdout or "").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except Exception:
            continue
        et = ev.get("type")
        if et == "assistant":
            for b in ev.get("message", {}).get("content", []):
                if b.get("type") == "tool_use":
                    nm, inp = b.get("name", "?"), (b.get("input") or {})
                    if nm == "Read":
                        trace.append("Read " + os.path.basename(inp.get("file_path", "") or "?"))
                    elif nm == "Grep":
                        trace.append('Grep "%s"' % (inp.get("pattern", "") or ""))
                    elif nm == "Glob":
                        trace.append("Glob " + (inp.get("pattern", "") or ""))
                    else:
                        trace.append(nm)
        elif et == "result":
            ans = (ev.get("result") or "").strip() or ans
            u = ev.get("usage", {}) or {}
            usage = {"turns": ev.get("num_turns"),
                     "duration_s": round((ev.get("duration_ms") or 0) / 1000, 1),
                     "input": u.get("input_tokens", 0), "output": u.get("output_tokens", 0),
                     "cache_read": u.get("cache_read_input_tokens", 0),
                     "cache_creation": u.get("cache_creation_input_tokens", 0),
                     "cost_usd": ev.get("total_cost_usd")}
    if not ans:
        ans = "(no answer from the claude CLI)\n" + (r.stderr or "")[:600]
    ids = re.findall(r"\[\[?([0-9A-Za-z][0-9A-Za-z\-]+)\]?\]", ans)
    m = re.search(r"CITED:\s*(.+)", ans)
    if m:
        ids += [x.strip() for x in re.split(r"[,\s]+", m.group(1)) if x.strip()]
    pages = [i for i in dict.fromkeys(ids) if i in NODES]
    ans = re.sub(r"\n?CITED:.*$", "", ans).strip()  # strip machine-readable CITED line
    return {"answer": ans, "pages": pages, "trace": trace, "usage": usage}

def run_agent(task, framing):
    """Dispatch to the active AI backend (Anthropic SDK or local Claude CLI)."""
    return (wiki_agent if ai_mode() == "api" else claude_cli_agent)(task, framing)

def _cites(ids):
    return [{"id": i, "label": NODES.get(i, {}).get("label", i),
             "image": NODES.get(i, {}).get("image", "")} for i in dict.fromkeys(ids)]

def _log_history(kind, query, resp):
    """Append a finished Ask/SOW run to the shared review log (best-effort)."""
    if not resp.get("answer"):
        return
    try:
        with open(HIST, "a") as f:
            f.write(json.dumps({"ts": datetime.datetime.now().isoformat(timespec="seconds"),
                                "kind": kind, "query": query, "answer": resp.get("answer"),
                                "citations": resp.get("citations", []), "trace": resp.get("trace", []),
                                "usage": resp.get("usage", {})}, ensure_ascii=False) + "\n")
    except Exception:
        pass

@app.get("/api/history")
def history_list(limit: int = 200):
    items = []
    try:
        with open(HIST) as f:
            for line in f:
                line = line.strip()
                if line:
                    try: items.append(json.loads(line))
                    except Exception: pass
    except FileNotFoundError:
        pass
    return {"total": len(items), "items": list(reversed(items))[:limit]}

@app.delete("/api/history")
def history_clear():
    try: os.remove(HIST)
    except FileNotFoundError: pass
    return {"ok": True}

@app.post("/api/ask")
def ask(req: Ask):
    if ai_mode() == "off":
        return {"answer": None, "citations": fts_pages(req.question, 12),
                "note": "No AI backend (set ANTHROPIC_API_KEY or install the `claude` CLI). Showing keyword-matched pages."}
    r = run_agent(f"QUESTION: {req.question}", "You are an expert on IEC graphical symbols and standards.")
    resp = {"answer": r["answer"], "citations": _cites(r["pages"]), "note": None,
            "trace": r.get("trace", []), "usage": r.get("usage", {})}
    _log_history("ask", req.question, resp)
    return resp

@app.post("/api/sow")
def sow(req: SOW):
    if ai_mode() == "off":
        return {"answer": None, "citations": fts_pages(req.text, 16),
                "note": "No AI backend (set ANTHROPIC_API_KEY or install the `claude` CLI). Showing keyword-matched pages."}
    framing = ("You are an engineering standards advisor. Given a Statement of Work (SOW), find ALL "
               "relevant standards, clauses and symbols in the wiki and produce a concise structured "
               "analysis: which apply, and why.")
    r = run_agent(f"STATEMENT OF WORK:\n{req.text}", framing)
    resp = {"answer": r["answer"], "citations": _cites(r["pages"]), "note": None,
            "trace": r.get("trace", []), "usage": r.get("usage", {})}
    _log_history("sow", req.text, resp)
    return resp

# serve built frontend if present (single-origin deploy)
DIST = os.path.join(HERE, "..", "frontend", "dist")
if os.path.isdir(DIST):
    _NOCACHE = {"Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache"}

    @app.get("/")
    def _index():
        # serve index.html with no-cache so frontend edits show on a normal reload
        return FileResponse(os.path.join(DIST, "index.html"), headers=_NOCACHE)

    @app.get("/index.html")
    def _index_html():
        return FileResponse(os.path.join(DIST, "index.html"), headers=_NOCACHE)

    app.mount("/", StaticFiles(directory=DIST, html=True), name="frontend")
