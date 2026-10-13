"""Kit portabil și copie completă a proiectului curent; fără secrete/date private."""
from pathlib import Path
import zipfile,json
ROOT=Path(__file__).resolve().parents[1];OFF=ROOT/'platforma/offline'
data=json.loads((ROOT/'content.json').read_text(encoding='utf-8'))
start=f'''PLICUL DISPĂRUT / MODERATOR

Extrage întregul folder, apoi deschide index.html. Nu este necesar internetul sau instalarea. Participanții primesc numai probele pe hârtie; folderul conține soluții și rămâne la moderator.

Începe cu pdf/00-ghid-pas-cu-pas.pdf. Setul de bază: {len(data['pdfs'])} PDF-uri și {data['printPages']} pagini. Imprimă fiecare PDF o dată; fișele de echipă pot fi multiplicate la nevoie. Sortează dosarul comun, 12 pachete de echipă (4 runde × 3 echipe) și FINALUL. Ghidurile și indiciile stau separat.

Trei echipe, fără număr fix de participanți. 90–100 minute estimate; fă o repetiție înainte de utilizare. Toate conturile, fotografiile și documentele sunt fictive. Ușa este în stânga; canapeaua în dreapta. Nu se iese din sală.

În lipsa laptopului, folosește PDF-urile și un ceas. Parola site-ului nu este cerută la fișierele locale; păstrează folderul cu soluții la moderator.
'''
def add_offline(z,prefix):
    for p in OFF.rglob('*'):
        if p.is_file():z.write(p,Path(prefix)/p.relative_to(OFF))
    z.writestr(str(Path(prefix)/'PORNESTE.txt'),start)
    for name in ['MODERATOR-PAS-CU-PAS.md','HARTA-SALII.md']:
        text=(ROOT/name).read_text(encoding='utf-8').replace('platforma/offline/','')
        z.writestr(str(Path(prefix)/name),text)
with zipfile.ZipFile(ROOT/'platforma/kit-offline.zip','w',zipfile.ZIP_DEFLATED) as z:add_offline(z,'PLICUL-DISPARUT')
with zipfile.ZipFile(ROOT/'PLICUL-DISPARUT-proiect-complet.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in OFF.rglob('*'):
        if p.is_file():z.write(p,Path('PLICUL-DISPARUT/platforma/offline')/p.relative_to(OFF))
    for name in ['README.md','AGENTS.md','VERIFICARE.md','HARTA-SALII.md','MODERATOR-PAS-CU-PAS.md','content.json','inventar.md','pdf-counts.json','requirements.txt','CONCEPT-PLICUL-DISPARUT-V3.md','output/imagegen/PROMPTS.md']:
        p=ROOT/name
        if p.is_file():z.write(p,Path('PLICUL-DISPARUT')/name)
    for folder in ['skills/escape-room-kit','tests','platforma/worker','platforma/scripts']:
        for p in (ROOT/folder).rglob('*'):
            if p.is_file() and '__pycache__' not in p.parts:z.write(p,Path('PLICUL-DISPARUT')/p.relative_to(ROOT))
    for name in ['case_plic.py','map_plic.py','build.py','encode_photos.py','package_offline.py','validate.py','qa_browser.py','render_qa.py']:
        p=ROOT/'scripts'/name;z.write(p,Path('PLICUL-DISPARUT/scripts')/name)
    for p in (ROOT/'output/imagegen').glob('*.png'):z.write(p,Path('PLICUL-DISPARUT/output/imagegen')/p.name)
    z.write(ROOT/'platforma/package.json','PLICUL-DISPARUT/platforma/package.json')
    z.write(ROOT/'platforma/.openai/hosting.json','PLICUL-DISPARUT/platforma/.openai/hosting.json')
    z.writestr('PLICUL-DISPARUT/PORNESTE.txt',start.replace('apoi deschide index.html','apoi deschide platforma/offline/index.html'))
print(json.dumps(dict(offline_bytes=(ROOT/'platforma/kit-offline.zip').stat().st_size,project_bytes=(ROOT/'PLICUL-DISPARUT-proiect-complet.zip').stat().st_size)))
