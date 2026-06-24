#!/usr/bin/env python3
"""FastAPI backend for the IEC 60617 symbol KG.

Serves the graph, symbol detail, full-text search, RAG Q&A (Claude), and the
symbol images. Reads the derived data layer built by build_kg.py.

Run:  uvicorn main:app --reload --port 8000
Env:  ANTHROPIC_API_KEY (optional — enables LLM answers; otherwise /ask returns
      retrieval-only results).  KG_MODEL (default claude-sonnet-4-6).
"""
import os, re, json, sqlite3
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
WIKI = os.path.abspath(os.path.join(HERE, "..", "..", "wiki"))
ASSETS = os.path.join(WIKI, "assets")
MODEL = os.environ.get("KG_MODEL", "claude-sonnet-4-6")

GRAPH = json.load(open(os.path.join(DATA, "graph.json")))
NODES = {n["id"]: n for n in GRAPH["nodes"]}

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
    return {"ok": True, "nodes": len(GRAPH["nodes"]), "edges": len(GRAPH["edges"]),
            "llm": bool(os.environ.get("ANTHROPIC_API_KEY")), "model": MODEL}

@app.get("/api/graph")
def graph(part: str = Query(None), type: str = Query(None)):
    """Lightweight graph for visualisation (no full body text)."""
    keep = ["id","type","label","part","section","is_example","form","image"]
    nodes = GRAPH["nodes"]
    if part: nodes = [n for n in nodes if n.get("part") == part]
    if type: nodes = [n for n in nodes if n.get("type") == type]
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
    k: int = 8

@app.post("/api/ask")
def ask(req: Ask):
    con = db()
    rows = fts_query(con, req.question, "id,type,label,name_en,name_fr,body", req.k)
    con.close()
    cites = [{"id": r["id"], "label": r["label"], "part": NODES.get(r["id"], {}).get("part", ""),
              "image": NODES.get(r["id"], {}).get("image", "")} for r in rows]

    if not os.environ.get("ANTHROPIC_API_KEY"):
        return {"answer": None, "citations": cites,
                "note": "Set ANTHROPIC_API_KEY to enable LLM answers. Showing retrieved symbols only."}

    import anthropic
    ctx = "\n\n".join(
        f"[{r['id']}] {r['label']} (Part {NODES.get(r['id'],{}).get('part','')})\n"
        f"EN: {r['name_en']} / FR: {r['name_fr']}\n{r['body'][:600]}"
        for r in rows)
    sys = ("You are an expert on the IEC 60617 graphical-symbols standard. Answer the user's "
           "question using ONLY the provided symbol context. Cite symbol numbers in brackets "
           "like [07-13-05]. If the answer isn't in the context, say so plainly. Be concise.")
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=MODEL, max_tokens=1024, system=sys,
        messages=[{"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {req.question}"}])
    answer = "".join(b.text for b in msg.content if b.type == "text")
    return {"answer": answer, "citations": cites, "note": None}

# serve built frontend if present (single-origin deploy)
DIST = os.path.join(HERE, "..", "frontend", "dist")
if os.path.isdir(DIST):
    app.mount("/", StaticFiles(directory=DIST, html=True), name="frontend")
