"""Execută verificarea reală în Chrome și salvează rezultate și capturi locale."""
from pathlib import Path
import subprocess,json,re,html,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
CHROME=Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
QA=ROOT/'.qa';QA.mkdir(exist_ok=True)
FLAGS=['--headless','--disable-gpu','--no-sandbox','--disable-background-networking','--disable-extensions','--no-first-run','--allow-file-access-from-files']
def run(args):
    p=subprocess.run([str(CHROME),*FLAGS,*args],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=40)
    if p.returncode:raise RuntimeError(p.stderr[-1200:])
    return p.stdout
if '--print-layout' in sys.argv:
    from pypdf import PdfReader
    text=(ROOT/'platforma/offline/index.html').read_text(encoding='utf-8')
    text=text.replace('<head>','<head><base href="'+(ROOT/'platforma/offline').as_uri()+'/">')
    script="<script>addEventListener('load',()=>{document.getElementById('print-root').innerHTML=Moderator.formsHTML()+['A22','B22','B12','F02'].map(id=>'<section class=\"print-page\">'+Moderator.documentHTML(Moderator.docById(id))+'</section>').join('');});</script>"
    text=text.replace('</body>',script+'</body>');target=QA/'print-layout.html';target.write_text(text,encoding='utf-8')
    out=QA/'browser-print.pdf';run([f'--user-data-dir={QA/"print-profile"}','--no-pdf-header-footer',f'--print-to-pdf={out}',target.as_uri()])
    pdf=PdfReader(out)
    result=dict(pages=len(pdf.pages),expected=5,forms=pdf.pages[0].extract_text().count('Ce știm și cum verificăm'))
    print(json.dumps(result))
    if result['pages']!=5 or result['forms']!=1:sys.exit(1)
elif '--measure' in sys.argv:
    text=(ROOT/'platforma/offline/index.html').read_text(encoding='utf-8')
    text=text.replace('<head>','<head><base href="'+(ROOT/'platforma/offline').as_uri()+'/">')
    text=text.replace('</body>',"<script>const p=document.createElement('pre');p.id='measure';p.textContent=JSON.stringify({inner:innerWidth,client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,main:document.querySelector('.main').getBoundingClientRect().width});document.body.appendChild(p);</script></body>")
    target=QA/'mobile-measure.html';target.write_text(text,encoding='utf-8')
    raw=run([f'--user-data-dir={QA/"visual-profile"}','--window-size=390,1000','--dump-dom',target.as_uri()])
    m=re.search(r'<pre id="measure">([^<]*)</pre>',raw);print(html.unescape(m.group(1)))
elif '--screenshots' in sys.argv:
    for name,size in [('desktop','1440,1000'),('mobil','500,1100')]:
        run([f'--user-data-dir={QA/"visual-screenshot-profile"}',f'--window-size={size}',f'--screenshot={QA/(name+".png")}',(ROOT/'platforma/offline/index.html').as_uri()])
    print('Capturi desktop și mobil salvate în .qa/')
else:
    raw=run([f'--user-data-dir={QA/"browser-tests-profile"}','--virtual-time-budget=3000','--dump-dom',(ROOT/'tests/browser-tests.html').as_uri()])
    (QA/'browser-results.html').write_text(raw,encoding='utf-8')
    m=re.search(r'<pre id="qa-result">([^<]*)</pre>',raw)
    if not m:raise RuntimeError('Lipsește raportul testului în browser.')
    result=json.loads(html.unescape(m.group(1)))
    (QA/'browser-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))
    if result['errors']:sys.exit(1)
