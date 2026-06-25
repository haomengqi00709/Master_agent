#!/usr/bin/env python3
"""OCR a scanned standard PDF into clean per-page text (for the document corpus).

Usage: python3 ocr_doc.py "<pdf path>" <out_txt_dir> <doc_id>
Renders each page at 300 dpi, auto-orients by OCR word count (printed-text pages
orient reliably), OCRs, and writes <out>/<doc_id>.txt (full text, page-delimited).
"""
import fitz, subprocess, re, os, sys
from PIL import Image

pdf, outdir, docid = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(outdir, exist_ok=True)
WORD = re.compile(r"[A-Za-z]{3,}")
tmp = f"{outdir}/_ocr_tmp.png"

def ocr(img):
    img.save(tmp)
    return subprocess.run(["tesseract", tmp, "-", "--psm", "6"],
                          capture_output=True, text=True).stdout

d = fitz.open(pdf)
pages = []
for i in range(d.page_count):
    pix = d[i].get_pixmap(dpi=300)
    f = f"{outdir}/_p{i+1}.png"; pix.save(f)
    im = Image.open(f)
    best, bestn = im, -1
    txt0 = ocr(im); n0 = len(WORD.findall(txt0))
    if n0 < 40:  # maybe rotated — try other orientations
        for ang in (90, 180, 270):
            cand = im.rotate(-ang, expand=True); t = ocr(cand); n = len(WORD.findall(t))
            if n > bestn: bestn, best, txt0 = n, cand, t
        if bestn <= n0: txt0 = ocr(im)  # keep upright
    pages.append(txt0)
    os.remove(f)
    print(f"p{i+1}/{d.page_count}: {len(WORD.findall(txt0))} words")

if os.path.exists(tmp): os.remove(tmp)
out = f"{outdir}/{docid}.txt"
with open(out, "w") as fh:
    for i, t in enumerate(pages):
        fh.write(f"\n\f[page {i+1}]\n{t.strip()}\n")
print(f"DONE -> {out} ({sum(len(p) for p in pages)} chars, {d.page_count} pages)")
