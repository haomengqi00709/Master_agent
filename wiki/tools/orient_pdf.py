#!/usr/bin/env python3
"""Render a scanned PDF to upright 300-dpi PNGs using OCR word-count scoring.
Usage: python3 orient_pdf.py <pdf_path> <out_dir>
For each page, tries all 4 rotations and keeps the one whose tesseract output
has the most real words (OSD alone mis-calls 90/180/270 on these symbol tables).
"""
import fitz, subprocess, re, os, sys
from PIL import Image
pdf, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
d=fitz.open(pdf); WORD=re.compile(r"[A-Za-zÀ-ÿ]{4,}")
def score(im):
    im.resize((im.width//2, im.height//2)).save(f"{out}/_s.png")
    o=subprocess.run(["tesseract",f"{out}/_s.png","-","--psm","6"],capture_output=True,text=True).stdout
    return len(WORD.findall(o))
for i in range(d.page_count):
    f=f"{out}/p{i+1:02d}.png"; d[i].get_pixmap(dpi=300).save(f)
    im0=Image.open(f); best=0; bs=-1
    for ang in (0,90,180,270):
        sc=score(im0.rotate(-ang,expand=True))
        if sc>bs: bs=sc; best=ang
    im0.rotate(-best,expand=True).save(f)
    print(f"p{i+1:02d} rot={best} words={bs}")
if os.path.exists(f"{out}/_s.png"): os.remove(f"{out}/_s.png")
print("DONE", d.page_count)
