"""Randează exemple și verifică marginile textului tuturor paginilor PDF."""
from pathlib import Path
import json,pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'.qa/pdf';OUT.mkdir(parents=True,exist_ok=True)
pdfs=ROOT/'platforma/offline/pdf'
issues=[];pages=0
for path in sorted(pdfs.glob('*.pdf')):
    with fitz.open(path) as doc:
        for i,page in enumerate(doc):
            pages+=1
            for block in page.get_text('dict')['blocks']:
                if block['type']!=0:continue
                for line in block['lines']:
                    x0,y0,x1,y1=line['bbox']
                    if x0<15 or y0<15 or x1>page.rect.width-15 or y1>page.rect.height-15:
                        issues.append(f'{path.name}, page {i+1}: outside margin')
        for i in sorted(set([0,len(doc)-1])):
            doc[i].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(OUT/f'{path.stem}-{i+1}.png')
result=dict(pages=pages,margin_issues=issues,renderer='PyMuPDF (Poppler unavailable)')
(OUT/'result.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
if issues:raise SystemExit(1)
