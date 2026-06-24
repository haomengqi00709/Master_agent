#!/usr/bin/env python3
"""Build the derived KG data layer from the markdown wiki (the source of truth).

Reads ../../wiki/{symbols,sections,standards,concepts}/*.md, parses YAML
frontmatter + body, and emits:
  data/graph.json   — {nodes:[...], edges:[...]} for graph visualisation
  data/kg.sqlite    — nodes, edges, and an FTS5 full-text index for search/RAG

Re-run whenever the wiki changes (it's a build artifact; never hand-edit it).
"""
import os, re, json, sqlite3, glob
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
WIKI = os.path.abspath(os.path.join(HERE, "..", "..", "wiki"))
DATA = os.path.join(HERE, "data")
os.makedirs(DATA, exist_ok=True)

FM = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)
IMG = re.compile(r"!\[[^\]]*\]\(\.\./(assets/[^)]+)\)")
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
SYMID = re.compile(r"^\d\d-[0-9A-Za-z]+-\d\d$")

def parse(path):
    raw = open(path).read()
    m = FM.match(raw)
    fm = yaml.safe_load(m.group(1)) if m else {}
    body = m.group(2) if m else raw
    return fm or {}, body

nodes = {}      # id -> node dict
edges = []      # {source, target, type}
edge_seen = set()

def add_edge(s, t, kind):
    if not t or s == t: return
    key = (s, t, kind)
    if key in edge_seen: return
    edge_seen.add(key); edges.append({"source": s, "target": t, "type": kind})

# ---- pass 1: collect nodes ----
files = (glob.glob(f"{WIKI}/symbols/*.md") + glob.glob(f"{WIKI}/sections/*.md")
         + glob.glob(f"{WIKI}/standards/*.md") + glob.glob(f"{WIKI}/concepts/*.md"))
for p in files:
    fm, body = parse(p)
    nid = str(fm.get("id") or os.path.splitext(os.path.basename(p))[0])
    ntype = fm.get("type", "page")
    img = IMG.search(body)
    label = fm.get("name_en") or fm.get("title_en") or nid
    nodes[nid] = {
        "id": nid, "type": ntype,
        "label": label,
        "name_en": fm.get("name_en", ""), "name_fr": fm.get("name_fr", ""),
        "title_en": fm.get("title_en", ""),
        "part": str(fm.get("part", "")), "section": str(fm.get("section", "")),
        "standard": fm.get("standard", ""),
        "is_example": bool(fm.get("is_example", False)),
        "form": fm.get("form") or "",
        "tags": fm.get("tags", []) if isinstance(fm.get("tags"), list) else [],
        "image": img.group(1) if img else "",
        "source": fm.get("source", ""),
        "symbol_count": fm.get("symbol_count", None),
        "body": body.strip(),
        "_fm": fm, "_body": body,
    }

# ---- pass 2: edges ----
for nid, n in nodes.items():
    fm, body = n["_fm"], n["_body"]
    if n["type"] == "symbol":
        # structural edges
        std = f'60617-{fm.get("part")}' if fm.get("part") else None
        if std in nodes: add_edge(nid, std, "in_part")
        # find this symbol's section node (filename-based id lives in sections/)
        for s, sn in nodes.items():
            if sn["type"] == "section" and sn["part"] == n["part"] and sn["section"] == n["section"]:
                add_edge(nid, s, "in_section"); break
        for f in (fm.get("forms") or []):
            add_edge(nid, str(f), "form_of")
        for o in (fm.get("see_also") or []):
            add_edge(nid, str(o), "see_also")
        for c in (fm.get("uses_concept") or []):
            add_edge(nid, str(c), "uses_concept")
        if fm.get("superseded_by"): add_edge(nid, str(fm["superseded_by"]), "superseded_by")
        if fm.get("supersedes"):   add_edge(nid, str(fm["supersedes"]), "supersedes")
        for r in (fm.get("references") or []):
            r = str(r)
            if SYMID.match(r): add_edge(nid, r, "references")
    elif n["type"] == "section":
        std = f'60617-{fm.get("part")}' if fm.get("part") else None
        if std in nodes: add_edge(nid, std, "in_part")
    # body wikilinks -> generic 'links' edges (only to existing nodes)
    for m in LINK.finditer(body):
        t = m.group(1).strip()
        if t in nodes: add_edge(nid, t, "links")

# drop helper keys
for n in nodes.values():
    n.pop("_fm", None); n.pop("_body", None)

graph = {"nodes": list(nodes.values()), "edges": edges}
json.dump(graph, open(f"{DATA}/graph.json", "w"), ensure_ascii=False)

# ---- SQLite + FTS5 ----
db = f"{DATA}/kg.sqlite"
if os.path.exists(db): os.remove(db)
con = sqlite3.connect(db); cur = con.cursor()
cur.execute("""CREATE TABLE nodes(id TEXT PRIMARY KEY, type TEXT, label TEXT,
  name_en TEXT, name_fr TEXT, title_en TEXT, part TEXT, section TEXT, standard TEXT,
  is_example INT, form TEXT, image TEXT, source TEXT, body TEXT)""")
cur.execute("CREATE TABLE edges(source TEXT, target TEXT, type TEXT)")
cur.execute("CREATE VIRTUAL TABLE search USING fts5(id UNINDEXED, type UNINDEXED, "
            "label, name_en, name_fr, body, tokenize='porter unicode61')")
for n in nodes.values():
    cur.execute("INSERT INTO nodes VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (n["id"], n["type"], n["label"], n["name_en"], n["name_fr"], n["title_en"],
         n["part"], n["section"], n["standard"], int(n["is_example"]), n["form"],
         n["image"], n["source"], n["body"]))
    cur.execute("INSERT INTO search VALUES(?,?,?,?,?,?)",
        (n["id"], n["type"], n["label"], n["name_en"], n["name_fr"], n["body"]))
cur.executemany("INSERT INTO edges VALUES(?,?,?)",
    [(e["source"], e["target"], e["type"]) for e in edges])
con.commit(); con.close()

bytype = {}
for n in nodes.values(): bytype[n["type"]] = bytype.get(n["type"], 0) + 1
print(f"graph.json: {len(nodes)} nodes ({bytype}), {len(edges)} edges")
print(f"kg.sqlite written to {DATA}")
