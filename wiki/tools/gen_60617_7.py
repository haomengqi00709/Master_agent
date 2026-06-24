#!/usr/bin/env python3
"""Generate the IEC 60617-7 portion of the KG from merged JSON page extracts.

Data in tools/data/p7_*.json was extracted by parallel vision-reader agents over
`../Standards-Reference/Publication No.617-7.pdf` (1st ed 1983) and cross-checked
against a manual reading of the first pages. This script merges them, generates
symbol nodes / section hubs / the part page, and writes a crop config
(tools/data/crop_60617-7.json) consumed by crop_symbols.py.
"""
import os, json, glob, re

WIKI = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(os.path.dirname(__file__), "data")
STD_ID = "60617-7"; ASSET_DIR = "60617-7"
SRC_DIR = "/private/tmp/claude-501/-Users-jasonhao-Desktop-Trust-AI-Advisory-daniel-s-Electronic-Standards-Reference/b3dbbf10-fcae-4b73-bb3d-3a27c37db6ed/scratchpad/up7"

PART = dict(id="60617-7",
  title_en="Switchgear, controlgear and protective devices",
  title_fr="Appareillage et dispositifs de commande et de protection",
  standard="IEC 60617-7 (formerly IEC 617-7)", edition="1st edition, 1983",
  source="Publication No.617-7.pdf",
  tc="Prepared by IEC Sub-Committee 3A (Graphical Symbols) of Technical Committee No. 3.")

# merge data files
symbols={}; sections={}
for f in sorted(glob.glob(os.path.join(DATA,"p7_*.json"))):
    d=json.load(open(f))
    for s in d["symbols"]: symbols[s["id"]]=s
    for k,v in d.get("sections",{}).items():
        if k not in sections or len(v.get("en",""))>len(sections[k].get("en","")):
            sections[k]=v

def seckey(ss):
    return (1,ss) if ss.startswith("A") else (0,int(ss))
SYMS=sorted(symbols.values(), key=lambda s:(seckey(s["section"]), s["id"]))

REF_SYM=re.compile(r"^\d\d-[0-9A-Za-z]+-\d\d$")
def render_ref(r):
    if REF_SYM.match(r): return f"[[{r}]]"          # symbol node
    m=re.match(r"^IEC 617-(\d+)$",r)
    if m: return f"[[60617-{m.group(1)}]]"           # sibling part
    return f"**{r}**"                                # external standard

def yl(items): return "[]" if not items else "["+", ".join(json.dumps(x,ensure_ascii=False) for x in items)+"]"
def secfile(ss): return f'{STD_ID}-{ss}-{slugify(sections.get(ss,{}).get("en",ss))}'
def slugify(t):
    t=re.sub(r"[^a-z0-9]+","-",t.lower()).strip("-")
    return "-".join(t.split("-")[:4]) or "section"
def write(p,c):
    os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w").write(c)

SECSLUG={ss:slugify(v.get("en",ss)) for ss,v in sections.items()}
def secfile(ss): return f"{STD_ID}-{ss}-{SECSLUG[ss]}"

# symbol nodes
for s in SYMS:
    ss=s["section"]; sec=sections.get(ss,{"en":ss,"fr":ss})
    refs=s.get("refs",[])
    fm ="---\n"+f'id: {s["id"]}\ntype: symbol\nstandard: IEC 60617-7\npart: 7\nsection: "{ss}"\n'
    fm+=f'edition: "1st edition, 1983"\nname_en: {json.dumps(s["name_en"],ensure_ascii=False)}\n'
    fm+=f'name_fr: {json.dumps(s["name_fr"],ensure_ascii=False)}\n'
    fm+=f'form: {json.dumps(s["form"]) if s.get("form") else "null"}\n'
    fm+=f'see_also: {yl([r for r in refs if REF_SYM.match(r)])}\n'
    fm+=f'references: {yl(refs)}\nis_example: {"true" if s.get("is_example") else "false"}\n'
    fm+=f'source: "{PART["source"]}, printed p.{s["printed_page"]}"\ntags: [60617-7, section-{ss}]\n---\n\n'
    b =f'# {s["id"]} — {s["name_en"]}\n\n'
    b+=f'![{s["id"]}](../assets/{ASSET_DIR}/p{s["asset_page"]:02d}.png)\n'
    b+=f'<sub>This symbol appears on {PART["source"]}, printed p.{s["printed_page"]} '
    b+=f'(full page shown). 617-7 uses page-level images: its table layout is too '
    b+=f'irregular (intro text, notes, text-only rows) for reliable per-symbol cropping.</sub>\n\n'
    b+=f'**Standard:** [[{PART["id"]}]] · **Section:** [[{secfile(ss)}]]'
    if s.get("form"): b+=f' · **{s["form"]}**'
    b+="\n\n## Description\n"+s["description"]+"\n\n## Names\n"
    b+=f'- **EN:** {s["name_en"]}\n- **FR:** {s["name_fr"]}\n\n'
    if s.get("notes"):
        b+="## Notes\n"+"".join(f'- {n}\n' for n in s["notes"])+"\n"
    rel=[render_ref(r) for r in refs]
    if rel: b+="## Related\n"+"".join(f'- {x}\n' for x in rel)
    write(os.path.join(WIKI,"symbols",s["id"]+".md"), fm+b)

# section hubs
for ss in sorted(sections, key=seckey):
    syms=[s for s in SYMS if s["section"]==ss]
    if not syms: continue
    sec=sections[ss]
    fm="---\n"+f'id: {secfile(ss)}\ntype: section\nstandard: IEC 60617-7\npart: 7\nsection: "{ss}"\n'
    fm+=f'title_en: {json.dumps(sec["en"],ensure_ascii=False)}\ntitle_fr: {json.dumps(sec["fr"],ensure_ascii=False)}\n'
    fm+=f'symbol_count: {len(syms)}\ntags: [60617-7, section]\n---\n\n'
    b=f'# 60617-7 Section {ss} — {sec["en"]}\n\n*{sec["fr"]}* · **Part:** [[{PART["id"]}]] · {len(syms)} symbols\n\n'
    b+="| No. | Name (EN) | Name (FR) | Notes |\n|-----|-----------|-----------|-------|\n"
    for s in syms:
        note=s["form"] or ("example" if s.get("is_example") else "")
        b+=f'| [[{s["id"]}]] | {s["name_en"]} | {s["name_fr"]} | {note} |\n'
    write(os.path.join(WIKI,"sections",secfile(ss)+".md"), fm+b)

# part page
nsec=len([ss for ss in sections if any(s["section"]==ss for s in SYMS)])
fm="---\n"+f'id: {PART["id"]}\ntype: standard\nstandard: {json.dumps(PART["standard"],ensure_ascii=False)}\n'
fm+=f'edition: "{PART["edition"]}"\npart: 7\ntitle_en: {json.dumps(PART["title_en"],ensure_ascii=False)}\n'
fm+=f'title_fr: {json.dumps(PART["title_fr"],ensure_ascii=False)}\nsymbol_count: {len(SYMS)}\n'
fm+=f'source: "{PART["source"]}"\ntags: [60617, standard, part]\n---\n\n'
b=f'# IEC 60617-7 — {PART["title_en"]}\n\n*{PART["title_fr"]}*\n\n'
b+=f'- **Standard:** {PART["standard"]}\n- **Edition:** {PART["edition"]}\n- **Source:** `{PART["source"]}` (scanned, 54 pp)\n'
b+=f'- **Origin:** {PART["tc"]}\n- **Symbols:** {len(SYMS)} across {nsec} sections (incl. Appendix A older symbols)\n\n'
b+="Switches, contacts, contactors, circuit-breakers, disconnectors, relays, fuses, "
b+="surge protection and starters. Builds heavily on the qualifying symbols in [[60617-2]] "
b+="(e.g. operating-mechanism symbols 02-13-xx) and the contact/connection symbols.\n\n## Sections\n"
for ss in sorted(sections, key=seckey):
    syms=[s for s in SYMS if s["section"]==ss]
    if not syms: continue
    b+=f'- [[{secfile(ss)}]] — {sections[ss]["en"]} ({len(syms)})\n'
b+="\n## Related\n- Part of the IEC 60617 family — see [[index#standards]].\n"
b+="- Cross-references [[60617-2]]; older symbols in Appendix A (sections A1–A3).\n"
write(os.path.join(WIKI,"standards",PART["id"]+".md"), fm+b)

# crop config
pageids={}
for s in SYMS: pageids.setdefault(s["asset_page"],[]).append(s["id"])
cfg=dict(std=STD_ID, src=SRC_DIR, need_cw=[], page_ids={str(k):v for k,v in sorted(pageids.items())})
write(os.path.join(DATA,"crop_60617-7.json"), json.dumps(cfg,ensure_ascii=False,indent=1))

print(f"Generated {len(SYMS)} symbols, {nsec} sections, 1 part. Crop config -> data/crop_60617-7.json")
