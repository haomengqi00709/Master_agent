#!/usr/bin/env python3
"""Generic JSON-driven generator for an IEC 60617 part.

Usage:  python3 gen_part.py <std_id>
Reads:
  - tools/data/<std_id>.meta.json   part metadata (see keys below)
  - tools/data/<std_id>_*.json      merged page extracts (subagent output)
Writes symbol nodes, section hubs, and the part page into the wiki.

meta keys: id, part, title_en, title_fr, standard, edition, source, pages,
           image_mode ("page"|"crop"), blurb (optional one-liner for part page).
"""
import os, json, glob, re, sys

WIKI = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(os.path.dirname(__file__), "data")
STD = sys.argv[1]
META = json.load(open(os.path.join(DATA, f"{STD}.meta.json")))
IMG = META.get("image_mode", "page")

def clean_title(t):
    t=re.sub(r"^\s*SECTION\s+\S+\s*[–—-]\s*","",t or "",flags=re.I).strip()
    return t
def better(new,old):
    "Prefer a real title over a parenthetical placeholder; else the longer."
    if not old: return True
    np_,op=new.startswith("("),old.startswith("(")
    if np_!=op: return op   # prefer the non-placeholder
    return len(new)>len(old)

symbols={}; sections={}
for f in sorted(glob.glob(os.path.join(DATA, f"{STD}_*.json"))):
    d=json.load(open(f))
    for s in d["symbols"]: symbols[s["id"]]=s
    for k,v in d.get("sections",{}).items():
        en=clean_title(v.get("en","")); fr=clean_title(v.get("fr",""))
        if k not in sections or better(en, sections[k].get("en","")):
            sections[k]={"en":en or k, "fr":fr}

def seckey(ss): return (1,ss) if ss[0] in "Aa" else (0,int(ss))
SYMS=sorted(symbols.values(), key=lambda s:(seckey(s["section"]), s["id"]))

REF_SYM=re.compile(r"^\d\d-[0-9A-Za-z]+-\d\d$")
def render_ref(r):
    if REF_SYM.match(r): return f"[[{r}]]"
    m=re.match(r"^IEC\s*617-(\d+)$",r)
    if m: return f"[[60617-{m.group(1)}]]"
    m=re.match(r"^(?:IEC\s*)?60617-(\d+)$",r)
    if m: return f"[[60617-{m.group(1)}]]"
    return f"**{r}**"
def yl(items): return "[]" if not items else "["+", ".join(json.dumps(x,ensure_ascii=False) for x in items)+"]"
def slugify(t):
    t=re.sub(r"[^a-z0-9]+","-",t.lower()).strip("-")
    return "-".join(t.split("-")[:4]) or "section"
SECSLUG={ss:slugify(v.get("en",ss)) for ss,v in sections.items()}
def secfile(ss): return f"{STD}-{ss}-{SECSLUG[ss]}"
def imgpath(s):
    return f'sym-{s["id"]}.png' if IMG=="crop" else f'p{s["asset_page"]:02d}.png'
def write(p,c):
    os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w").write(c)

for s in SYMS:
    ss=s["section"]; refs=s.get("refs",[])
    fm ="---\n"+f'id: {s["id"]}\ntype: symbol\nstandard: {META["standard"]}\npart: {META["part"]}\nsection: "{ss}"\n'
    fm+=f'edition: "{META["edition"]}"\nname_en: {json.dumps(s["name_en"],ensure_ascii=False)}\n'
    fm+=f'name_fr: {json.dumps(s.get("name_fr",""),ensure_ascii=False)}\n'
    fm+=f'form: {json.dumps(s.get("form")) if s.get("form") else "null"}\n'
    fm+=f'see_also: {yl([r for r in refs if REF_SYM.match(r)])}\nreferences: {yl(refs)}\n'
    fm+=f'is_example: {"true" if s.get("is_example") else "false"}\n'
    fm+=f'source: "{META["source"]}, printed p.{s.get("printed_page","?")}"\ntags: [{STD}, section-{ss}]\n---\n\n'
    b =f'# {s["id"]} — {s["name_en"]}\n\n![{s["id"]}](../assets/{STD}/{imgpath(s)})\n'
    if IMG=="crop":
        b+=f'<sub>Per-symbol crop from {META["source"]}, printed p.{s.get("printed_page","?")} ([full page](../assets/{STD}/p{s["asset_page"]:02d}.png)).</sub>\n\n'
    else:
        b+=f'<sub>This symbol appears on {META["source"]}, printed p.{s.get("printed_page","?")} (full page shown).</sub>\n\n'
    b+=f'**Standard:** [[{META["id"]}]] · **Section:** [[{secfile(ss)}]]'
    if s.get("form"): b+=f' · **{s["form"]}**'
    b+="\n\n## Description\n"+(s.get("description") or s["name_en"])+"\n\n## Names\n"
    b+=f'- **EN:** {s["name_en"]}\n- **FR:** {s.get("name_fr","")}\n\n'
    if s.get("notes"): b+="## Notes\n"+"".join(f'- {n}\n' for n in s["notes"])+"\n"
    rel=[render_ref(r) for r in refs]
    if rel: b+="## Related\n"+"".join(f'- {x}\n' for x in rel)
    write(os.path.join(WIKI,"symbols",s["id"]+".md"), fm+b)

for ss in sorted(sections, key=seckey):
    syms=[s for s in SYMS if s["section"]==ss]
    if not syms: continue
    sec=sections[ss]
    fm="---\n"+f'id: {secfile(ss)}\ntype: section\nstandard: {META["standard"]}\npart: {META["part"]}\nsection: "{ss}"\n'
    fm+=f'title_en: {json.dumps(sec["en"],ensure_ascii=False)}\ntitle_fr: {json.dumps(sec.get("fr",""),ensure_ascii=False)}\n'
    fm+=f'symbol_count: {len(syms)}\ntags: [{STD}, section]\n---\n\n'
    b=f'# {STD} Section {ss} — {sec["en"]}\n\n*{sec.get("fr","")}* · **Part:** [[{META["id"]}]] · {len(syms)} symbols\n\n'
    if IMG=="crop":
        b+="| No. | Symbol | Name (EN) | Notes |\n|-----|--------|-----------|-------|\n"
        for s in syms:
            note=s.get("form") or ("example" if s.get("is_example") else "")
            b+=f'| [[{s["id"]}]] | ![](../assets/{STD}/sym-{s["id"]}.png) | {s["name_en"]} | {note} |\n'
    else:
        b+="| No. | Name (EN) | Name (FR) | Notes |\n|-----|-----------|-----------|-------|\n"
        for s in syms:
            note=s.get("form") or ("example" if s.get("is_example") else "")
            b+=f'| [[{s["id"]}]] | {s["name_en"]} | {s.get("name_fr","")} | {note} |\n'
    write(os.path.join(WIKI,"sections",secfile(ss)+".md"), fm+b)

nsec=len([ss for ss in sections if any(s["section"]==ss for s in SYMS)])
fm="---\n"+f'id: {META["id"]}\ntype: standard\nstandard: {json.dumps(META["standard"],ensure_ascii=False)}\n'
fm+=f'edition: "{META["edition"]}"\npart: {META["part"]}\ntitle_en: {json.dumps(META["title_en"],ensure_ascii=False)}\n'
fm+=f'title_fr: {json.dumps(META["title_fr"],ensure_ascii=False)}\nsymbol_count: {len(SYMS)}\n'
fm+=f'source: "{META["source"]}"\ntags: [60617, standard, part]\n---\n\n'
b=f'# {META["standard"]} — {META["title_en"]}\n\n*{META["title_fr"]}*\n\n'
b+=f'- **Standard:** {META["standard"]}\n- **Edition:** {META["edition"]}\n- **Source:** `{META["source"]}` (scanned, {META["pages"]} pp)\n'
b+=f'- **Symbols:** {len(SYMS)} across {nsec} sections\n\n'
if META.get("blurb"): b+=META["blurb"]+"\n\n"
b+="## Sections\n"
for ss in sorted(sections, key=seckey):
    syms=[s for s in SYMS if s["section"]==ss]
    if not syms: continue
    b+=f'- [[{secfile(ss)}]] — {sections[ss]["en"]} ({len(syms)})\n'
b+="\n## Related\n- Part of the IEC 60617 family — see [[index#standards]].\n"
write(os.path.join(WIKI,"standards",META["id"]+".md"), fm+b)

# crop config (only used if image_mode crop)
pageids={}
for s in SYMS: pageids.setdefault(s["asset_page"],[]).append(s["id"])
write(os.path.join(DATA,f"crop_{STD}.json"), json.dumps(
    dict(std=STD, src=META["src_dir"], need_cw=[], page_ids={str(k):v for k,v in sorted(pageids.items())}),
    ensure_ascii=False, indent=1))
print(f"{STD}: {len(SYMS)} symbols, {nsec} sections, 1 part (image_mode={IMG}).")
