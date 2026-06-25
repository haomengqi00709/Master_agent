#!/usr/bin/env python3
"""Apply the rich IEC-56 concept bodies (read from the source clauses by the
reader subagents, stored in data/iec56_rich_*.json) onto the existing concept
pages. Preserves each page's frontmatter, H1 and symbol cross-links; replaces the
thin one-line body with the rich synthesis. Any [[wikilink]] whose target is not
an existing page is converted to bold text so the wiki stays lint-clean.
"""
import os, re, json, glob

WIKI = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CON = os.path.join(WIKI, "concepts")
DATA = os.path.join(os.path.dirname(__file__), "data")

# merge the 7 extraction files (later files override on duplicate keys)
rich = {}
for i in range(1, 8):
    rich.update(json.load(open(os.path.join(DATA, "iec56_rich_%d.json" % i))))

# every existing page name (for link validation)
pages = {os.path.splitext(os.path.basename(p))[0]
         for p in glob.glob(os.path.join(WIKI, "**", "*.md"), recursive=True)}
pages |= {"index", "CLAUDE", "log"}

LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
SYMID = re.compile(r"^[0-9]{2}-[0-9A-Za-z]{2}-[0-9]{2}$")

def fix_links(text):
    def repl(m):
        target, label = m.group(1).strip(), m.group(2)
        if target in pages:
            return m.group(0)
        shown = label if label else target.replace("-", " ")
        return "**%s**" % shown
    return LINK.sub(repl, text)

enriched, missing = 0, []
for slug, body in rich.items():
    p = os.path.join(CON, slug + ".md")
    if not os.path.isfile(p):
        missing.append(slug); continue
    t = open(p).read()
    fm = re.match(r"(---.*?---\n)", t, re.S)
    h1 = re.search(r"(^#\s+.+)$", t, re.M)
    if not fm or not h1:
        missing.append(slug + " (no fm/h1)"); continue
    # preserve symbol cross-links that were on the page
    syms = [s for s in LINK.findall(t)]
    syms = [a for (a, b) in syms if SYMID.match(a.strip()) and a.strip() in pages]
    seen, sym_links = set(), []
    for s in syms:
        if s not in seen:
            seen.add(s); sym_links.append("[[%s]]" % s)
    new = fm.group(1) + "\n" + h1.group(1) + "\n\n" + fix_links(body.strip()) + "\n"
    if sym_links:
        new += "\n**Related symbols:** " + " · ".join(sym_links) + "\n"
    open(p, "w").write(new)
    enriched += 1

print("enriched %d IEC-56 concept pages" % enriched)
if missing:
    print("WARNING missing/skip:", missing)
