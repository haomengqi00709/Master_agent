#!/usr/bin/env python3
"""Crop per-symbol images from upright scanned IEC 60617 table pages.

Config-driven: one CONFIGS entry per part. Usage:  python3 crop_symbols.py <std>
e.g. `python3 crop_symbols.py 60617-2`.

Strategy (robust for these noisy tables, numpy-only — no OpenCV):
  - Snap the Symbol column to the consistent table layout (expected x-fractions
    of page width, refined to a detected vertical rule when one is nearby).
    Ignores spurious internal rules (Preferred/Other-form sub-divider, tall
    strokes) and degenerate faint-border pages.
  - Anchor rows on the No.-column number lines (one number per symbol), cleaned
    to ~uniform number-line height; align in order to the KNOWN per-page ID list
    (page_ids, from the vision read). Drop leading header band(s) by keeping the
    last N anchors.
  - Crop the Symbol column between consecutive anchors.
Outputs sym-<ID>.png into ../assets/<std>/ plus a labelled montage per page
(written next to the source images) for visual verification of crop<->ID
alignment. ALWAYS eyeball the montages before trusting the crops.
"""
import sys, os
import numpy as np
from PIL import Image, ImageDraw

SCRATCH = "/private/tmp/claude-501/-Users-jasonhao-Desktop-Trust-AI-Advisory-daniel-s-Electronic-Standards-Reference/b3dbbf10-fcae-4b73-bb3d-3a27c37db6ed/scratchpad"
WIKI = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

CONFIGS = {
 "60617-3": dict(
   src=f"{SCRATCH}/up", need_cw={5,10,11,12},
   page_ids={
     3:["03-01-01","03-01-02","03-01-03","03-01-04"],
     4:["03-01-05","03-01-06","03-01-07","03-01-08","03-01-09","03-01-10","03-01-11","03-01-12"],
     5:["03-01-13","03-01-14","03-01-15"],
     6:["03-02-01","03-02-02","03-02-03","03-02-04","03-02-05","03-02-06","03-02-07","03-02-08","03-02-09","03-02-10"],
     7:["03-02-11","03-02-12","03-02-13","03-02-14"],
     8:["03-03-01","03-03-02","03-03-03","03-03-04","03-03-05","03-03-06","03-03-07","03-03-08"],
     9:["03-03-09","03-03-10","03-03-11","03-03-12","03-03-13","03-03-14","03-03-15","03-03-16"],
     10:["03-03-17","03-03-18","03-03-19","03-03-20","03-03-21","03-03-22"],
     11:["03-04-01","03-04-02","03-04-03","03-04-04","03-04-05","03-04-06"],
     12:["03-04-07"]}),
 "60617-2": dict(
   src=f"{SCRATCH}/up2", need_cw=set(),   # already all upright in up2/
   page_ids={
     10:["02-01-01","02-01-02","02-01-03","02-01-04","02-01-05"],
     11:["02-01-06","02-01-07"],
     12:["02-02-01","02-02-02","02-02-03","02-02-04","02-02-05","02-02-06","02-02-07"],
     13:["02-02-08","02-02-09","02-02-10","02-02-11","02-02-12","02-02-13","02-02-14","02-02-15","02-02-16"],
     14:["02-03-01","02-03-02","02-03-03","02-03-04"],
     15:["02-03-05","02-03-06","02-03-07","02-03-08","02-03-09","02-03-10","02-03-11","02-03-12"],
     16:["02-04-01","02-04-02","02-04-03","02-04-04","02-04-05","02-04-06"],
     17:["02-05-01","02-05-02","02-05-03","02-05-04","02-05-05","02-05-06","02-05-07","02-05-08"],
     18:["02-06-01","02-06-02","02-06-03","02-06-04","02-06-05"],
     19:["02-07-01","02-07-02","02-07-03","02-07-04","02-07-05","02-07-06","02-07-07"],
     20:["02-08-01","02-08-02","02-08-03","02-08-04","02-08-05"],
     21:["02-09-01","02-09-02","02-09-03"],
     22:["02-10-01","02-10-02","02-10-03","02-10-04","02-10-05","02-10-06"],
     23:["02-11-01","02-11-02","02-11-03","02-11-04","02-11-05","02-11-06"],
     24:["02-12-01","02-12-02","02-12-03","02-12-04","02-12-05","02-12-06","02-12-07","02-12-08","02-12-09"],
     25:["02-12-10","02-12-11","02-12-12","02-12-13","02-12-14","02-12-15","02-12-16","02-12-17","02-12-18","02-12-19","02-12-20","02-12-21","02-12-22","02-12-23"],
     26:["02-13-01","02-13-02","02-13-03","02-13-04","02-13-05","02-13-06","02-13-07","02-13-08","02-13-09","02-13-10"],
     27:["02-13-11","02-13-12","02-13-13","02-13-14","02-13-15","02-13-16","02-13-17","02-13-18","02-13-19","02-13-20","02-13-21"],
     28:["02-13-22","02-13-23","02-13-24","02-13-25","02-13-26","02-13-27"],
     29:["02-14-01","02-14-02","02-14-03","02-14-04","02-14-05"],
     30:["02-15-01","02-15-02","02-15-03","02-15-04","02-15-05"],
     31:["02-16-01","02-16-02","02-16-03"],
     32:["02-17-01","02-17-02","02-17-03","02-17-04","02-17-05","02-17-06"],
     33:["02-17-07","02-17-08","02-17-09"],
     34:["02-A1-01"]}),
}

def vlines(dark,h,w,margin=120):
    band=dark[margin:h-margin,:]; vf=band.mean(axis=0); thr=0.5*vf.max()
    xs=np.where(vf>thr)[0]; g=[]; s=p=None
    for x in xs:
        if s is None:s=x
        elif x-p>10:g.append((s+p)//2);s=x
        p=x
    if s is not None:g.append((s+p)//2)
    return [int(v) for v in g]

def anchors(dark,nx0,nx1,y_lo=0):
    col=dark[:, nx0:nx1]; den=col.mean(axis=1); on=den>0.05
    ys=np.where(on)[0]; raw=[]; s=p=None
    for y in ys:
        if s is None:s=y;p=y
        elif y-p>14:raw.append((s,p));s=y;p=y
        else:p=y
    if s is not None:raw.append((s,p))
    return [t for t,b in raw if 10<=b-t<=46 and t>=y_lo]

def hrules(dark,h,x0,x1):
    """y-positions of strong full-width horizontal rules across the table."""
    hf=dark[:, x0:x1].mean(axis=1)
    ys=np.where(hf>0.45)[0]; g=[]; s=p=None
    for y in ys:
        if s is None:s=y
        elif y-p>6: g.append((s+p)//2); s=y
        p=y
    if s is not None: g.append((s+p)//2)
    return [int(v) for v in g]

def data_top(dark,h,x0,x1):
    """Top of the data region: below the column-header divider when present.
    The column header sits between the table top border and a divider rule
    ~60-170px below it; on continuation pages there is no such pair."""
    hr=[y for y in hrules(dark,h,x0,x1) if y<h*0.45]
    if len(hr)>=2 and 40<hr[1]-hr[0]<210:
        return hr[1]+4
    return (hr[0]+4) if hr else 120

def crop_page(cfg, std, pno, montdir):
    ids=cfg["page_ids"][pno]; n=len(ids)
    im=Image.open(f'{cfg["src"]}/p{pno:02d}.png')
    if pno in cfg["need_cw"]: im=im.rotate(-90,expand=True)
    rgb=im.convert("RGB"); a=np.asarray(im.convert("L")); h,w=a.shape; dark=(a<150)
    vl=vlines(dark,h,w)
    def snap(frac,tol=45):
        x=frac*w; cand=[v for v in vl if abs(v-x)<tol]
        return int(min(cand,key=lambda v:abs(v-x))) if cand else int(x)
    left,no_sym,sym_leg = snap(0.108),snap(0.162),snap(0.396)
    sx0,sx1 = no_sym+6, sym_leg-6
    dtop=data_top(dark,h,left,snap(0.90))            # exclude section title + col header
    tops=anchors(dark,left+12,no_sym-8,y_lo=dtop); note=""
    if len(tops)>=n:
        if len(tops)>n: note=f"dropped {len(tops)-n} lead band(s)"
        tops=tops[len(tops)-n:]
    else:
        note=f"only {len(tops)}<{n}; even-split fallback below header"
        t0=tops[0] if tops else dtop
        tops=[int(t0+i*(h-130-t0)/n) for i in range(n)]
    bottom=h-110
    bounds=[max(0,tops[i]-14) for i in range(n)]+[bottom]
    adir=os.path.join(WIKI,"assets",std); os.makedirs(adir,exist_ok=True)
    os.makedirs(montdir,exist_ok=True); tiles=[]
    for i,sid in enumerate(ids):
        crop=rgb.crop((sx0,bounds[i],sx1,bounds[i+1])); crop.save(f"{adir}/sym-{sid}.png")
        tile=Image.new("RGB",(crop.width,crop.height+28),"white"); tile.paste(crop,(0,28))
        d=ImageDraw.Draw(tile); d.text((4,6),sid,fill="red"); d.rectangle([0,0,crop.width-1,crop.height+27],outline="black")
        tiles.append(tile)
    mw=max(t.width for t in tiles); mh=sum(t.height for t in tiles)
    m=Image.new("RGB",(mw,mh),"white"); y=0
    for t in tiles: m.paste(t,(0,y)); y+=t.height
    m.save(f"{montdir}/montage_p{pno:02d}.png")
    print(f"p{pno:02d}: {n} crops, snap=({left},{no_sym},{sym_leg}) {note}")

def load_cfg(arg):
    """arg is either a key in CONFIGS or a path to a JSON config
    {std, src, need_cw:[...], page_ids:{"6":[...]}}."""
    if arg in CONFIGS:
        return arg, CONFIGS[arg]
    import json
    d=json.load(open(arg))
    cfg=dict(src=d["src"], need_cw=set(d.get("need_cw",[])),
             page_ids={int(k):v for k,v in d["page_ids"].items()})
    return d["std"], cfg

if __name__=="__main__":
    arg=sys.argv[1] if len(sys.argv)>1 else "60617-3"
    std,cfg=load_cfg(arg)
    montdir=f'{cfg["src"]}/montage_{std}'
    pages=[int(x) for x in sys.argv[2:]] or sorted(cfg["page_ids"])
    for p in pages: crop_page(cfg,std,p,montdir)
