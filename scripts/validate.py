"""Integritatea probelor, dependențelor, pachetelor și livrabilului offline."""
from pathlib import Path
import json,re,sys,zipfile
from pypdf import PdfReader
from case_plic import DATA as SOURCE
ROOT=Path(__file__).resolve().parents[1];OFF=ROOT/'platforma/offline';errors=[];checks=[]
def check(name,ok):(checks if ok else errors).append(name)
def norm(t):return ' '.join(t.split())
D=json.loads((ROOT/'content.json').read_text(encoding='utf-8'));ids={d['id']:d for d in D['docs']}
base={k:v for k,v in D.items() if k not in ['pdfs','printPages']};base['docs']=[{k:v for k,v in d.items() if k!='capture'} for d in base['docs']]
check('Sursa și datele generate corespund',base==SOURCE)
raw=(OFF/'data.js').read_text(encoding='utf-8');check('Datele browserului corespund',json.loads(raw.split('=',1)[1].rstrip(';\n'))==D)
check('51 probe unice și trei echipe',len(ids)==len(D['docs'])==51 and len(D['groups'])==3)
check('Parcurs de minimum 75 minute',D['duration']>=75 and D['minDuration']>=75)
for p in D['puzzles']:
    check('Referințe și două indicii: '+p['id'],len(p['hints'])==2 and all(i in ids for i in p['evidence']))
    check('Probe disponibile înainte de concluzie: '+p['id'],all(ids[i]['round']<=p['round'] for i in p['evidence']))
for s in D['moderatorSteps']:check('Referințe pas: '+s['id'],all(i in ids for i in s['docs']))
for r in range(1,5):
    for t in ['A','B','C']:check(f'Toate echipele au probe în runda {r}: {t}',len([d for d in D['docs'] if d['round']==r and d['team']==t])>=3)
check('Hoțul nu apare nominal în primele trei runde',not any(re.search(r'\bVictor\b',d['body']) for d in D['docs'] if d['round']<=3))
check('Nicio filmare miraculoasă','Nu a fost recuperată o filmare' in ids['C34']['body'])
check('Dan și suma corectă','Dan' in ids['O01']['body'] and '5 000' in ids['O01']['body'])
mapping=json.loads((OFF/'assets/room-map.json').read_text(encoding='utf-8'));check('Orientare și trei echipe',mapping['teams']==3 and mapping['orientation']=='Ușa pe stânga; canapeaua pe dreapta')
for name in ['index.html','app.js','styles.css','evidence.js','evidence.css']:
    text=(OFF/name).read_text(encoding='utf-8');check('Fără conexiuni externe: '+name,not re.search(r'https?://|@import|\bfetch\s*\(|XMLHttpRequest|WebSocket',text))
    for ref in re.findall(r'(?:src|href)=["\']([^"\']+)',text)+re.findall(r'url\(["\']?([^\)"\']+)',text):
        if '${' in ref or ref.startswith('#'):continue
        if ref=='kit-offline.zip':check('Kitul site-ului există',(ROOT/'platforma/kit-offline.zip').is_file());continue
        check('Resursă locală: '+ref,(OFF/ref).is_file())
texts={};pages=0
for p in D['pdfs']:
    path=OFF/'pdf'/p['file'];reader=PdfReader(path);pages+=len(reader.pages);texts[p['file']]=[norm(page.extract_text() or '') for page in reader.pages]
    check('Număr pagini: '+p['file'],len(reader.pages)==p['pages'])
    check('Text și diacritice fără înlocuiri: '+p['file'],all(len(t)>70 and '\ufffd' not in t for t in texts[p['file']]))
check('20 PDF-uri și 82 pagini',len(D['pdfs'])==20 and pages==D['printPages']==82)
for d in D['docs']:
    target=next(p for p in D['pdfs'] if p['round']==d['round'] and p['team']==d['team']);text=' '.join(texts[target['file']])
    check('Proba este în pachetul corect: '+d['id'],d['id'] in text)
    if d['format'] not in ['post','profile','chat']:check('Text integral PDF: '+d['id'],norm(d['body']) in text)
    if d['format']=='chat':check('Toate mesajele în PDF: '+d['id'],all(norm(m[2]) in text for m in d['messages']))
    if d['format'] in ['profile','post']:check('Profil/postare în PDF: '+d['id'],norm(d['post']) in text and d['handle'] in text)
    if d.get('note'):check('Proveniență vizibilă: '+d['id'],norm(d['note']) in text)
    if d.get('capture'):check('Captură PNG validă: '+d['id'],(OFF/d['capture']).read_bytes().startswith(b'\x89PNG'))
    if d['format']=='police':check('Poliția este marcată drept ficțiune: '+d['id'],'MATERIAL DE JOC' in text)
for p in D['pdfs']:
    if p['round']<4 and p['round']>=0:check('Fără soluția furtului în primele pachete: '+p['file'],not re.search(r'\bVictor\b',' '.join(texts[p['file']])))
with zipfile.ZipFile(ROOT/'platforma/kit-offline.zip') as z:
    names=z.namelist();check('Arhivă offline validă',z.testzip() is None);check('Fără fișiere private/secrete',not any('/.git/' in n or '/.openai/' in n or '/.qa/' in n or '/IMG_' in n or '.env' in n for n in names))
    for p in OFF.rglob('*'):
        if p.is_file():check('Fișier actual în arhivă: '+p.name,z.read('PLICUL-DISPARUT/'+p.relative_to(OFF).as_posix())==p.read_bytes())
    check('Fișier de pornire prezent','PLICUL-DISPARUT/PORNESTE.txt' in names)
with zipfile.ZipFile(ROOT/'PLICUL-DISPARUT-proiect-complet.zip') as z:check('Arhiva proiectului este validă',z.testzip() is None)
result=dict(documents=len(ids),pdfs=len(D['pdfs']),pages=pages,passed=len(checks),errors=errors);(ROOT/'.qa/integrity-plic.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=True))
if errors:sys.exit(1)
