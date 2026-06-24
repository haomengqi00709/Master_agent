#!/usr/bin/env python3
"""Generate the IEC 60617-3 portion of the symbol KG from structured data.

Data was extracted by vision-reading the scanned PDF
`../Standards-Reference/Publication No.617-3.pdf` (1st edition, 1983).
Re-running this script regenerates symbols/, sections/, the part page, and the
60617-3 block of index.md deterministically. Edit the DATA below, not the
output files.
"""
import os, json, textwrap

WIKI = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
STD_ID = "60617-3"
ASSET_DIR = "60617-3"

PART = {
    "id": "60617-3",
    "title_en": "Conductors and connecting devices",
    "title_fr": "Conducteurs et dispositifs de connexion",
    "standard": "IEC 60617-3 (formerly IEC 617-3)",
    "edition": "1st edition, 1983",
    "source": "Publication No.617-3.pdf",
    "tc": "Prepared by IEC Sub-Committee 3A (Graphical Symbols) of Technical Committee No. 3; derived from IEC Publication 117.",
}

SECTIONS = [
    (1, "conductors", "Conductors", "Conducteurs", "03-01", "p03"),
    (2, "terminals", "Terminals and connections of conductors",
        "Bornes et connexions de conducteurs", "03-02", "p06"),
    (3, "connecting-devices", "Connecting devices", "Dispositifs de connexion",
        "03-03", "p08"),
    (4, "cable-fittings", "Cable fittings", "Accessoires pour câbles", "03-04", "p11"),
]

# printed page number for each asset page
PRINTED = {"p03":4,"p04":5,"p05":6,"p06":7,"p07":8,"p08":9,"p09":10,"p10":11,"p11":12,"p12":13}

# symbol = (id, section, page, name_en, name_fr, desc, aliases, notes,
#           form, forms, see_also, uses_concept, refs, is_example)
def S(id, sec, page, en, fr, desc, aliases=None, notes=None, form=None,
      forms=None, see=None, concept=None, refs=None, example=False):
    return dict(id=id, sec=sec, page=page, en=en, fr=fr, desc=desc,
                aliases=aliases or [], notes=notes or [], form=form,
                forms=forms or [], see=see or [], concept=concept or [],
                refs=refs or [], example=example)

SYMBOLS = [
 # --- Section 1: Conductors ---
 S("03-01-01",1,"p03","Conductor","Conducteur",
   "A single conductor. The same symbol also denotes a group of conductors, a line, a cable, a circuit, or a transmission path (for example, for microwaves).",
   aliases=["Group of conductors","Line","Cable","Circuit","Transmission path"],
   notes=["Single-line representation of conductors: when a single line represents a group of conductors, their number may be indicated either by adding small oblique strokes or one oblique stroke completed by a figure."],
   see=["03-01-02","03-01-03"], concept=["single-line-representation"]),
 S("03-01-02",1,"p03","Three conductors (Form 1)","Trois conducteurs (Forme 1)",
   "Three conductors, indicated by adding three small oblique strokes to the single conductor line.",
   form="Form 1", forms=["03-01-03"], see=["03-01-01"], concept=["single-line-representation"]),
 S("03-01-03",1,"p03","Three conductors (Form 2)","Trois conducteurs (Forme 2)",
   "Three conductors, indicated by adding one oblique stroke completed by the figure 3.",
   form="Form 2", forms=["03-01-02"], see=["03-01-01"], concept=["single-line-representation"],
   notes=["Additional information may be indicated as follows. Above the line: kind of current, system of distribution, frequency and voltage. Below the line: the number of conductors of the circuit followed by a multiplication sign and the cross-sectional area of each conductor; if different sizes of conductors are used, their particulars are separated by a plus sign; the conductor material may be indicated by its chemical symbol."]),
 S("03-01-04",1,"p03","Direct-current circuit — annotation example",
   "Circuit à courant continu, 110 V, deux conducteurs de 120 mm² en aluminium",
   "Worked example of conductor annotation: a direct-current circuit, 110 V, two aluminium conductors of 120 mm² (shown as “— 110 V” above the line and “2 × 120 mm² Al” below it).",
   example=True, see=["03-01-03","03-01-05"]),
 S("03-01-05",1,"p04","Three-phase circuit — annotation example",
   "Circuit à courant triphasé, 50 Hz, 400 V, trois conducteurs de 120 mm², avec fil neutre de 50 mm²",
   "Worked example of conductor annotation: a three-phase circuit, 50 Hz, 400 V, three conductors of 120 mm² with a neutral of 50 mm² (shown as “3N ∼ 50 Hz 400 V” above the line and “3 × 120 + 1 × 50” below it).",
   example=True, see=["03-01-04"]),
 S("03-01-06",1,"p04","Flexible conductor","Conducteur flexible","A flexible conductor."),
 S("03-01-07",1,"p04","Screened conductor","Conducteur sous écran",
   "A screened (shielded) conductor.", notes=["The note with symbol 03-01-09 applies."], see=["03-01-09"]),
 S("03-01-08",1,"p04","Twisted conductors","Conducteurs torsadés",
   "Twisted conductors, two conductors shown.", notes=["The note with symbol 03-01-09 applies."], see=["03-01-09"]),
 S("03-01-09",1,"p04","Conductors in a cable","Conducteurs dans un câble",
   "Conductors in a cable, three conductors shown.",
   notes=["If several conductors are in a cable (or twisted together or in a screen) but the lines representing them on a diagram are not adjacent to each other, the method shown by symbol 03-01-10 may be used."],
   see=["03-01-10","03-01-07","03-01-08"]),
 S("03-01-10",1,"p04","Conductors in a cable, non-adjacent — example",
   "Exemple : deux conducteurs parmi cinq sont dans un câble",
   "Worked example: two conductors out of five in a cable, used when the lines representing the cabled conductors are not drawn adjacent to one another.",
   example=True, see=["03-01-09"]),
 S("03-01-11",1,"p04","Coaxial pair","Paire coaxiale","A coaxial pair.",
   notes=["If the coaxial structure is not maintained, the tangential line should be drawn only on the coaxial side."],
   see=["03-01-12","03-01-13"]),
 S("03-01-12",1,"p04","Coaxial pair connected to terminals — example",
   "Exemple : paire coaxiale raccordée sur bornes",
   "Worked example: a coaxial pair connected to terminals.", example=True, see=["03-01-11"]),
 S("03-01-13",1,"p05","Coaxial pair with screen","Paire coaxiale sous écran",
   "A coaxial pair with screen.", see=["03-01-11"]),
 S("03-01-14",1,"p05","Conductor or cable not connected",
   "Extrémité d'un conducteur ou d'un câble, non connectée",
   "End of a conductor or cable that is not connected.", see=["03-01-15"]),
 S("03-01-15",1,"p05","Conductor or cable not connected and specially insulated",
   "Extrémité d'un conducteur ou d'un câble, non connectée et spécialement isolée",
   "End of a conductor or cable that is not connected and is specially insulated.", see=["03-01-14"]),
 # --- Section 2: Terminals and connections of conductors ---
 S("03-02-01",2,"p06","Connection of conductors","Connexion de conducteurs",
   "Connection of conductors."),
 S("03-02-02",2,"p06","Terminal","Borne","A terminal.", notes=["The circle may be filled in."]),
 S("03-02-03",2,"p06","Terminal strip","Barrette à bornes",
   "A terminal strip, the example being shown with terminal markings (e.g. 11, 12, 13, 14, 15, 16)."),
 S("03-02-04",2,"p06","Junction of conductors (Form 1)","Dérivation (Forme 1)",
   "Junction of conductors.", form="Form 1", forms=["03-02-05"]),
 S("03-02-05",2,"p06","Junction of conductors (Form 2)","Dérivation (Forme 2)",
   "Junction of conductors.", form="Form 2", forms=["03-02-04"]),
 S("03-02-06",2,"p06","Double junction of conductors (Form 1)","Double dérivation (Forme 1)",
   "Double junction of conductors.", form="Form 1", forms=["03-02-07"]),
 S("03-02-07",2,"p06","Double junction of conductors (Form 2)","Double dérivation (Forme 2)",
   "Double junction of conductors.", form="Form 2", forms=["03-02-06"]),
 S("03-02-08",2,"p06","Conductor joint / in-line splice","Jonction de conducteur",
   "Conductor joint; an in-line splice."),
 S("03-02-09",2,"p06","Connection common to a group of similar items",
   "Connexion commune à un groupe d'appareils similaires",
   "A connection common to a group of similar items.",
   notes=["The total number of similar items may be indicated by a figure near the common connection symbol."],
   see=["03-02-10"]),
 S("03-02-10",2,"p06","Multipled uniselector hooks — example",
   "Exemple : bancs multiples figurés pour 10 bancs",
   "Worked example: multipled uniselector hooks shown for 10 banks.", example=True, see=["03-02-09"]),
 S("03-02-11",2,"p07","Interchange of conductors / change of phase sequence / inversion of polarity",
   "Permutation des conducteurs, changement de l'ordre de succession des phases ou inversion de polarité",
   "Interchange of conductors, change of phase sequence, or inversion of polarity, shown for n conductors in single-line representation.",
   notes=["The interchanged conductors may be indicated.",
          "For the identification of the conductors, IEC Publication 445 (Identification of apparatus terminals and general rules for a uniform system of terminal marking, using an alphanumeric notation) applies."],
   concept=["single-line-representation"], refs=["445"], see=["03-02-12"]),
 S("03-02-12",2,"p07","Change of phase sequence — example",
   "Exemple : changement de l'ordre de succession des phases",
   "Worked example: change of phase sequence (shown with conductors L1, L2, L3).", example=True, see=["03-02-11"]),
 S("03-02-13",2,"p07","Neutral point in a multi-phase system",
   "Point neutre d'un système polyphasé",
   "Neutral point in a multi-phase system, shown in single-line representation.",
   concept=["single-line-representation"], see=["03-02-14"]),
 S("03-02-14",2,"p07","Synchronous generator with external neutral point — example",
   "Exemple : alternateur triphasé, deux extrémités sorties sur chaque phase, point neutre extérieur",
   "Worked example: a three-phase synchronous generator with both leads of each phase brought out, shown with an external neutral point.",
   example=True, see=["03-02-13"]),
 # --- Section 3: Connecting devices (Preferred form / Other form) ---
 S("03-03-01",3,"p08","Socket (female)","Prise de connecteur / prise de prolongateur",
   "A socket (female contact). Preferred form.", see=["03-03-02","03-03-03"]),
 S("03-03-02",3,"p08","Pole of a socket","Pôle d'une prise",
   "Pole of a socket. Other form.", see=["03-03-01"]),
 S("03-03-03",3,"p08","Plug (male)","Fiche de connecteur / fiche de prolongateur",
   "A plug (male contact). Preferred form.", see=["03-03-04","03-03-01"]),
 S("03-03-04",3,"p08","Pole of a plug","Pôle d'une fiche",
   "Pole of a plug. Other form.", see=["03-03-03"]),
 S("03-03-05",3,"p08","Plug and socket (male and female)","Fiche et prise (connecteur, prolongateur)",
   "A plug and socket (male and female).", see=["03-03-06","03-03-07"]),
 S("03-03-06",3,"p08","Plug and socket (other form)","Fiche et prise (autre forme)",
   "A plug and socket (male and female). Other form.", forms=["03-03-05"]),
 S("03-03-07",3,"p08","Multipole plug and socket — multi-line",
   "Fiche et prise multipolaires, figurées hexapolaires : représentation multifilaire",
   "Multipole plug and socket, shown with six poles, in multi-line representation.",
   concept=["multi-line-representation"], forms=["03-03-08"]),
 S("03-03-08",3,"p08","Multipole plug and socket — single-line",
   "Fiche et prise multipolaires : représentation unifilaire",
   "Multipole plug and socket, shown with six poles, in single-line representation.",
   concept=["single-line-representation"], forms=["03-03-07"]),
 S("03-03-09",3,"p09","Connector assembly, fixed portion","Ensemble de connecteurs, partie fixe",
   "Connector assembly, fixed portion.",
   notes=["The symbol should be used only when it is desired to distinguish between the fixed and free parts of the connector assembly."],
   see=["03-03-10","03-03-11"]),
 S("03-03-10",3,"p09","Connector assembly, movable portion","Ensemble de connecteurs, partie mobile",
   "Connector assembly, movable portion.", notes=["The note with symbol 03-03-09 applies."], see=["03-03-09"]),
 S("03-03-11",3,"p09","Mixed connector assembly","Ensemble de connecteurs, parties fixe et mobile accouplées",
   "Mixed connector assembly: plug side fixed and socket side movable.",
   notes=["The note with symbol 03-03-09 applies."], see=["03-03-09"]),
 S("03-03-12",3,"p09","Plug and jack, telephone type, two-pole","Fiche et jack, bipolaires, type téléphone",
   "Plug and jack, telephone type, two-pole.",
   notes=["The longest pole on the plug symbol represents the tip of the plug, and the shortest the sleeve."],
   see=["03-03-13"]),
 S("03-03-13",3,"p09","Plug and jack, telephone type, three-pole",
   "Fiche et jack, tripolaires, type téléphone, jack figuré avec contacts de rupture",
   "Plug and jack, telephone type, three-pole, the jack shown with breaking contacts.",
   notes=["The note with symbol 03-03-12 applies."], see=["03-03-12","03-03-14"]),
 S("03-03-14",3,"p09","Break or isolating jack, telephone type","Jack de coupure ou de séparation, type téléphone",
   "Break or isolating jack, telephone type.", see=["03-03-13"]),
 S("03-03-15",3,"p09","Coaxial plug and socket","Fiche coaxiale et prise coaxiale",
   "Coaxial plug and socket.",
   notes=["If the coaxial plug or socket is connected to a coaxial pair, the tangential line(s) should be appropriately extended."],
   see=["03-01-11"]),
 S("03-03-16",3,"p09","Butt-connector","Connecteur par pression en bout","A butt-connector."),
 S("03-03-17",3,"p10","Connecting link, closed (Form 1)","Barrette de connexion, fermée (Forme 1)",
   "Connecting link, closed.", form="Form 1", forms=["03-03-18"], see=["03-03-19"]),
 S("03-03-18",3,"p10","Connecting link, closed (Form 2)","Barrette de connexion, fermée (Forme 2)",
   "Connecting link, closed.", form="Form 2", forms=["03-03-17"]),
 S("03-03-19",3,"p10","Connecting link, open","Barrette de connexion, ouverte",
   "Connecting link, open.", see=["03-03-17"]),
 S("03-03-20",3,"p10","Plug-and-socket connector (U-link): male-male",
   "Fiche et prise de connecteur, par exemple cavalier : mâle-mâle",
   "Plug-and-socket-type connector, for example a U-link: male-male.", see=["03-03-21","03-03-22"]),
 S("03-03-21",3,"p10","Plug-and-socket connector: male-female",
   "Fiche et prise de connecteur : mâle-femelle",
   "Plug-and-socket-type connector: male-female.", see=["03-03-20"]),
 S("03-03-22",3,"p10","Plug-and-socket connector: male-male with socket access",
   "Fiche et prise de connecteur : mâle-mâle avec prise de dérivation",
   "Plug-and-socket-type connector: male-male with socket access.", see=["03-03-20"]),
 # --- Section 4: Cable fittings ---
 S("03-04-01",4,"p11","Cable sealing end, with a three-core cable",
   "Boîte d'extrémité, figurée avec un câble tripolaire",
   "Cable sealing end, shown with a three-core cable.", see=["03-04-02"]),
 S("03-04-02",4,"p11","Cable sealing end, with three single-core cables",
   "Boîte d'extrémité, figurée avec trois câbles unipolaires",
   "Cable sealing end, shown with three single-core cables.", see=["03-04-01"]),
 S("03-04-03",4,"p11","Straight-through joint box — multi-line",
   "Boîte de jonction pour conducteurs, figurée avec trois conducteurs : représentation multifilaire",
   "Straight-through joint box, shown with three conductors, in multi-line representation.",
   concept=["multi-line-representation"], forms=["03-04-04"]),
 S("03-04-04",4,"p11","Straight-through joint box — single-line",
   "Boîte de jonction : représentation unifilaire",
   "Straight-through joint box, in single-line representation.",
   concept=["single-line-representation"], forms=["03-04-03"]),
 S("03-04-05",4,"p11","Junction box with T-connection — multi-line",
   "Boîte pour une dérivation, figurée avec trois conducteurs avec dérivation : représentation multifilaire",
   "Junction box, shown with three conductors with a T-connection, in multi-line representation.",
   concept=["multi-line-representation"], forms=["03-04-06"]),
 S("03-04-06",4,"p11","Junction box with T-connection — single-line",
   "Boîte pour une dérivation : représentation unifilaire",
   "Junction box with T-connection, in single-line representation.",
   concept=["single-line-representation"], forms=["03-04-05"]),
 S("03-04-07",4,"p12","Pressure-tight bulkhead cable gland",
   "Dispositif étanche de passage de câbles, figuré avec trois câbles",
   "Pressure-tight bulkhead cable gland, shown with three cables.",
   notes=["The high-pressure side is the longer side of the trapezoid, thus retaining the gland in the bulkhead."]),
]

CONCEPTS = {
 "single-line-representation": ("Single-line representation",
   "A method of drawing in which a single line represents a group of conductors or a multi-pole device. The number of conductors/poles is indicated by small oblique strokes or by one stroke completed by a figure. Contrast with [[multi-line-representation]]."),
 "multi-line-representation": ("Multi-line representation",
   "A method of drawing in which every conductor or pole of a device is drawn as a separate line. More explicit but bulkier than [[single-line-representation]]."),
}

# ---------- helpers ----------
def yaml_list(items):
    if not items: return "[]"
    return "[" + ", ".join(json.dumps(x, ensure_ascii=False) for x in items) + "]"

def link(id): return f"[[{id}]]"

def sec_file(num):
    for n,slug,*_ in SECTIONS:
        if n==num: return f"{STD_ID}-{n}-{slug}"
    return None

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w") as f: f.write(content)

# ---------- symbol pages ----------
def sym_page(s):
    secf = sec_file(s["sec"])
    fm  = "---\n"
    fm += f'id: {s["id"]}\n'
    fm += "type: symbol\n"
    fm += "standard: IEC 60617-3\n"
    fm += "part: 3\n"
    fm += f'section: {s["sec"]}\n'
    fm += 'edition: "1st edition, 1983"\n'
    fm += f'name_en: {json.dumps(s["en"], ensure_ascii=False)}\n'
    fm += f'name_fr: {json.dumps(s["fr"], ensure_ascii=False)}\n'
    fm += f'aliases: {yaml_list(s["aliases"])}\n'
    fm += f'forms: {yaml_list(s["forms"])}\n'
    fm += f'see_also: {yaml_list(s["see"])}\n'
    fm += f'uses_concept: {yaml_list(s["concept"])}\n'
    fm += f'references: {yaml_list(["IEC "+r for r in s["refs"]])}\n'
    fm += f'is_example: {"true" if s["example"] else "false"}\n'
    fm += f'source: "{PART["source"]}, printed p.{PRINTED[s["page"]]}"\n'
    fm += f'tags: [60617-3, section-{s["sec"]}]\n'
    fm += "---\n\n"

    b  = f'# {s["id"]} — {s["en"]}\n\n'
    b += f'![{s["id"]}](../assets/{ASSET_DIR}/sym-{s["id"]}.png)\n'
    b += f'<sub>Per-symbol crop from {PART["source"]}, printed p.{PRINTED[s["page"]]} '
    b += f'([full page](../assets/{ASSET_DIR}/{s["page"]}.png)).</sub>\n\n'
    b += f'**Standard:** {link(PART["id"])} · **Section:** {link(secf)}'
    if s["form"]: b += f' · **{s["form"]}**'
    b += "\n\n"
    b += "## Description\n" + s["desc"] + "\n\n"
    b += "## Names\n"
    en = s["en"] + ((" / " + " / ".join(s["aliases"])) if s["aliases"] else "")
    b += f'- **EN:** {en}\n'
    b += f'- **FR:** {s["fr"]}\n\n'
    if s["notes"]:
        b += "## Notes\n"
        for n in s["notes"]: b += f'- {n}\n'
        b += "\n"
    rel = []
    for f in s["forms"]: rel.append(f'{link(f)} — alternative form')
    for o in s["see"]:   rel.append(f'{link(o)}')
    for c in s["concept"]: rel.append(f'uses {link(c)}')
    for r in s["refs"]:  rel.append(f'references **IEC {r}**')
    if rel:
        b += "## Related\n" + "\n".join(f'- {x}' for x in rel) + "\n"
    return fm + b

for s in SYMBOLS:
    write(os.path.join(WIKI,"symbols",s["id"]+".md"), sym_page(s))

# ---------- section hub pages ----------
for num,slug,title_en,title_fr,prefix,startpage in SECTIONS:
    syms=[s for s in SYMBOLS if s["sec"]==num]
    fm  = "---\n"+f'id: {STD_ID}-{num}-{slug}\ntype: section\nstandard: IEC 60617-3\npart: 3\nsection: {num}\n'
    fm += f'title_en: {json.dumps(title_en, ensure_ascii=False)}\n'
    fm += f'title_fr: {json.dumps(title_fr, ensure_ascii=False)}\n'
    fm += f'symbol_count: {len(syms)}\ntags: [60617-3, section]\n---\n\n'
    b  = f'# 60617-3 Section {num} — {title_en}\n\n'
    b += f'*{title_fr}* · **Part:** {link(PART["id"])} · {len(syms)} symbols ({prefix}-xx)\n\n'
    b += "| No. | Symbol | Name (EN) | Notes |\n|-----|--------|-----------|-------|\n"
    for s in syms:
        tag = " ⓔ" if s["example"] else ""
        note = s["form"] or ("example" if s["example"] else "")
        img = f'![](../assets/{ASSET_DIR}/sym-{s["id"]}.png)'
        b += f'| {link(s["id"])} | {img} | {s["en"]}{tag} | {note} |\n'
    b += "\nⓔ = worked example.\n"
    write(os.path.join(WIKI,"sections",f'{STD_ID}-{num}-{slug}.md'), fm+b)

# ---------- part page ----------
def part_page():
    fm  = "---\n"+f'id: {PART["id"]}\ntype: standard\n'
    fm += f'standard: {json.dumps(PART["standard"], ensure_ascii=False)}\n'
    fm += f'edition: "{PART["edition"]}"\npart: 3\n'
    fm += f'title_en: {json.dumps(PART["title_en"], ensure_ascii=False)}\n'
    fm += f'title_fr: {json.dumps(PART["title_fr"], ensure_ascii=False)}\n'
    fm += f'symbol_count: {len(SYMBOLS)}\n'
    fm += f'source: "{PART["source"]}"\nsupersedes: []\nsuperseded_by: []\n'
    fm += "tags: [60617, standard, part]\n---\n\n"
    b  = f'# IEC 60617-3 — {PART["title_en"]}\n\n'
    b += f'*{PART["title_fr"]}*\n\n'
    b += f'- **Standard:** {PART["standard"]}\n- **Edition:** {PART["edition"]}\n'
    b += f'- **Source:** `{PART["source"]}` (scanned, 13 pp)\n'
    b += f'- **Origin:** {PART["tc"]}\n'
    b += f'- **Symbols:** {len(SYMBOLS)} across {len(SECTIONS)} sections\n\n'
    b += "## Sections\n"
    for num,slug,title_en,title_fr,prefix,_ in SECTIONS:
        cnt=len([s for s in SYMBOLS if s["sec"]==num])
        b += f'- {link(f"{STD_ID}-{num}-{slug}")} — {title_en} ({cnt} symbols, {prefix}-xx)\n'
    b += "\n## Part of the IEC 60617 / 617 family\n"
    b += "See [[index#standards]] for the full family. This part references "
    b += "**IEC 445** (terminal identification). IEC renumbered 617 → 60617 in 1997.\n"
    write(os.path.join(WIKI,"standards",f'{PART["id"]}.md'), fm+b)
part_page()

# ---------- concept pages ----------
for slug,(title,desc) in CONCEPTS.items():
    users=[s["id"] for s in SYMBOLS if slug in s["concept"]]
    fm=f'---\nid: {slug}\ntype: concept\ntags: [concept]\n---\n\n'
    b=f'# {title}\n\n{desc}\n\n## Used by symbols\n'
    b+="\n".join(f'- {link(u)}' for u in users)+"\n"
    write(os.path.join(WIKI,"concepts",slug+".md"), fm+b)

print(f"Generated {len(SYMBOLS)} symbols, {len(SECTIONS)} sections, 1 part, {len(CONCEPTS)} concepts.")
