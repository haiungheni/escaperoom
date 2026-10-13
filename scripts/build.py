"""Construiește toate probele PDF din același renderer folosit offline."""
from pathlib import Path
import json,html,subprocess,zipfile,sys
from pypdf import PdfReader,PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from case_plic import DATA,ROOT,write
from map_plic import write as write_map
sys.stdout.reconfigure(encoding='utf-8')
OFF=ROOT/'platforma/offline';OUT=OFF/'pdf';QA=ROOT/'.qa/plic-build';QA.mkdir(parents=True,exist_ok=True)
CHROME=Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
FLAGS=['--headless','--disable-gpu','--no-sandbox','--disable-background-networking','--disable-extensions','--no-first-run','--allow-file-access-from-files','--no-pdf-header-footer']
W,H=A4;INK=HexColor('#302044');PDFS=[]
for name,file in [('Text','arial.ttf'),('Bold','arialbd.ttf')]:pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
def chrome(args):
    r=subprocess.run([str(CHROME),*FLAGS,f'--user-data-dir={QA/"chrome-profile"}',*args],capture_output=True,timeout=50)
    if r.returncode:raise RuntimeError(r.stderr.decode('utf-8',errors='replace')[-1000:])
def para(c,text,x,y,w,size=11,bold=False):
    p=Paragraph(html.escape(text).replace('\n','<br/>'),ParagraphStyle('body',fontName='Bold' if bold else 'Text',fontSize=size,leading=size*1.5,textColor=INK))
    _,h=p.wrap(w,H)
    if y-h<45:raise ValueError('Text depasit pe pagina: '+text[:60])
    p.drawOn(c,x,y-h);return y-h-13
def text_pdf(file,title,sections):
    c=canvas.Canvas(str(OUT/file),pagesize=A4);c.setTitle('Plicul dispărut / '+title)
    for index,(heading,body) in enumerate(sections):
        c.setFillColor(HexColor('#6e37e8'));c.rect(0,H-80,W,80,fill=1,stroke=0)
        c.setFillColor(HexColor('#ffffff'));c.setFont('Bold',10);c.drawString(40,H-33,'PLICUL DISPĂRUT / NUMAI PENTRU MODERATOR')
        c.setFont('Text',8);c.drawString(40,H-56,title)
        y=para(c,heading,40,H-110,W-80,19,True);para(c,body,40,y,W-80,10.5)
        c.setFillColor(HexColor('#80718f'));c.setFont('Text',7);c.drawString(40,25,'CAZ FICTIV / SOLUȚIILE RĂMÂN SEPARAT DE PROBE');c.drawRightString(W-40,25,str(index+1));c.showPage()
    c.save()
def metadata(file,title,description,round=-1,team='moderator',copies=1):
    PDFS.append(dict(file=file,title=title,description=description,pages=len(PdfReader(OUT/file).pages),round=round,team=team,copies=copies))
def evidence_html(docs,name,screen=False):
    base=OFF.as_uri()+'/'
    js=json.dumps(docs,ensure_ascii=False)
    style='body{margin:0;background:#eff1f4;padding:35px;font-family:Arial,sans-serif}.evidence{max-width:760px}' if screen else '@page{size:A4;margin:12mm}body{margin:0}section{break-after:page}section:last-child{break-after:auto}.evidence{print-color-adjust:exact;-webkit-print-color-adjust:exact}.print-index{font:9px Arial;color:#887b95;margin:0 0 9px}'
    target=QA/(name+'.html')
    target.write_text('<!doctype html><html lang="ro"><meta charset="utf-8"><base href="'+base+'"><link rel="stylesheet" href="evidence.css"><style>'+style+'</style><body><script src="evidence.js"></script><script>const list='+js+';document.body.insertAdjacentHTML("beforeend",list.map(d=>"<section>"+Evidence.render(d)+"</section>").join(""));</script></body></html>',encoding='utf-8')
    return target
def split(source,file,indices):
    r=PdfReader(source);w=PdfWriter()
    for i in indices:w.add_page(r.pages[i])
    w.add_metadata({'/Title':'Plicul dispărut / '+file})
    with open(OUT/file,'wb') as f:w.write(f)
def worksheet_html():
    docs=[]
    for g in DATA['groups']:
        docs.append(dict(id='FIȘĂ-'+g['id'],title=g['name']+' / '+g['topic'],source='Runda: ______ / Participanți: ____________________',format='worksheet',body=g['task']+'\n\nCE AFIRMĂ MATERIALUL?\n____________________________________________\n\nCE PUTEM VERIFICA? INDICAȚI ID-URILE.\n____________________________________________\n____________________________________________\n\nCE NU ȘTIM ÎNCĂ?\n____________________________________________\n\nCE ÎNTREBĂM CELELALTE ECHIPE?\n____________________________________________'))
    return evidence_html(docs,'fise')
def props_pdf():
    c=canvas.Canvas(str(OUT/'11-recuzita.pdf'),pagesize=A4)
    c.setTitle('Plicul dispărut / bani de recuzită și etichete')
    c.setFillColor(INK);c.setFont('Bold',17);c.drawString(38,H-35,'Bani de recuzită / decupează cele 10 cartonașe')
    for i in range(10):
        x=38+(i%2)*264;y=H-65-(i//2)*131
        c.setFillColor(HexColor('#eee6ff'));c.setStrokeColor(HexColor('#a892c8'));c.roundRect(x,y-112,250,112,8,fill=1,stroke=1)
        c.setFillColor(HexColor('#6e37e8'));c.setFont('Bold',30);c.drawString(x+17,y-40,'500 LEI')
        c.setFillColor(INK);c.setFont('Bold',9);c.drawString(x+17,y-64,'RECUZITĂ / FĂRĂ VALOARE FINANCIARĂ')
        c.setFont('Text',8);c.drawString(x+17,y-85,'PLICUL DISPĂRUT / '+str(i+1).zfill(2));c.drawString(x+17,y-99,'Nu este o bancnotă. Material de joc.')
    c.showPage();c.setFillColor(INK);c.setFont('Bold',17);c.drawString(38,H-35,'Etichetele plicurilor / decupează')
    labels=[f'RUNDA {r} / ECHIPA {g}' for r in range(1,5) for g in ['A','B','C']]+['DOSAR COMUN','FINAL / NU DESCHIDE ÎNAINTE']
    for i,label in enumerate(labels):
        x=38+(i%2)*264;y=H-63-(i//2)*90;c.setFillColor(HexColor('#faf7ff'));c.setStrokeColor(HexColor('#a892c8'));c.rect(x,y-76,250,76,fill=1)
        c.setFillColor(INK);c.setFont('Bold',10);c.drawString(x+12,y-28,label);c.setFont('Text',8);c.drawString(x+12,y-50,'Plicul dispărut / predare de moderator')
    c.showPage();c.setFillColor(INK);c.setFont('Bold',18);c.drawString(38,H-40,'Pregătește plicul din poveste')
    para(c,'Pune cele 10 cartonașe în plic, împreună cu fișa de mai jos. Scrie pe față „5 000 / atelier foto” și pune o bucată mică de bandă albastră pe colțul din dreapta sus. Plicul este recuzită pentru final, nu o probă ascunsă în afara sălii.',38,H-80,W-76,12)
    c.setStrokeColor(HexColor('#a892c8'));c.rect(80,240,W-160,260);c.setFillColor(INK);c.setFont('Bold',22);c.drawString(112,462,'5 000 / atelier foto');c.setFont('Text',12)
    for i in range(10):c.drawString(112,430-i*17,'[x] 500 lei / cartonaș '+str(i+1))
    c.setFont('Text',8);c.drawString(112,253,'RECUZITĂ / CAZ FICTIV / suma celor 10 cartonașe: 5 000');c.showPage();c.save()
def build():
    write_map();OUT.mkdir(parents=True,exist_ok=True)
    # Directorul conține numai rezultate generate; versiunile vechi sunt în Git/.qa.
    for old in OUT.glob('*.pdf'):old.unlink()
    all_target=evidence_html(DATA['docs'],'toate-probele')
    all_pdf=QA/'toate-probele.pdf';chrome(['--virtual-time-budget=1200',f'--print-to-pdf={all_pdf}',all_target.as_uri()])
    reader=PdfReader(all_pdf)
    if len(reader.pages)!=len(DATA['docs']):raise ValueError(f'Probe pe {len(reader.pages)} pagini, asteptate {len(DATA["docs"])}. Verifica paginarea.')
    ids={d['id']:i for i,d in enumerate(DATA['docs'])}
    for d in DATA['docs']:
        if d['id'] not in reader.pages[ids[d['id']]].extract_text():raise ValueError('Ordine PDF gresita: '+d['id'])
    common=[ids[d['id']] for d in DATA['docs'] if d['round']==0]
    split(all_pdf,'01-dosar-comun.pdf',common);metadata('01-dosar-comun.pdf','Dosarul comun','O01–O05 / înainte de runda 1',0,'comun')
    for r in range(1,5):
        for g in DATA['groups']:
            ds=[d for d in DATA['docs'] if d['round']==r and d['team']==g['id']]
            f=f'0{r+1}-runda-{r}-echipa-{g["id"]}.pdf';split(all_pdf,f,[ids[d['id']] for d in ds]);metadata(f,f'Runda {r} / {g["name"]}',g['topic']+' / '+', '.join(d['id'] for d in ds),r,g['id'])
    split(all_pdf,'06-final.pdf',[ids[d['id']] for d in DATA['docs'] if d['round']==5]);metadata('06-final.pdf','Finalul și corectarea acuzațiilor','F01–F03 / păstrează în plicul FINAL',5,'comun')
    f='07-fise-echipe.pdf';chrome(['--virtual-time-budget=800',f'--print-to-pdf={OUT/f}',worksheet_html().as_uri()]);metadata(f,'Fișele celor trei echipe','Câte o fișă de echipă; copii suplimentare la nevoie')
    guide=[('Pregătirea în 20–30 de minute','1. Imprimă dosarul comun, cele 12 pachete de rundă, finalul și cele trei fișe.\n2. Pune runda și echipa pe fiecare plic. Nu pune numele hoțului pe plic.\n3. Păstrează acest ghid, soluțiile și indiciile separat.\n4. Împarte grupul cât mai echilibrat în trei echipe; nu există număr fix de participanți.\n5. Pregătește pixuri, foi, 12 plicuri de echipă, un plic comun și un plic FINAL. Poți folosi dosare în loc de plicuri.\n6. Laptopul este opțional; un ceas și acest ghid sunt suficiente.\n7. Ușa din stânga rămâne liberă. Participanții nu caută afară sau în lucruri personale.\n8. Toate documentele și fotografiile reprezintă un caz fictiv. Nu se folosesc bani, conturi sau polițiști reali.'),('Cum păstrezi ritmul','Ținta standard: 100 minute. Introducere 10; runda 1: 20; runda 2: 20; runda 3: 20; runda 4: 15; final: 5; discuție: 10.\n\nParticipanții citesc, compară, notează și prezintă concluzii. După fiecare rundă, fiecare echipă indică minimum două surse, o concluzie și o întrebare pentru celelalte echipe.\n\nDacă termină repede, cere justificarea și compararea explicațiilor alternative. Nu introduce așteptare artificială ca să atingi timpul. Dacă sunt blocați, oferă indiciul 1, apoi indiciul 2.\n\nDurata de 90–100 minute este estimată, fără pilot cu participanți. Fă o repetiție înainte de utilizare.\n\nÎn panou, predarea este manuală. Cronometrul nu eliberează automat probele. Confirmările arată ce ai verificat pe hârtie.'),('Dacă grupul nu termină sau laptopul se oprește','Fără laptop: urmează paginile următoare, predă plicurile și notează minutele pe hârtie. Toate informațiile sunt în PDF-uri.\n\nFinal asistat: explică traseul masă → mapă → prag exterior; ajută grupul să compare intervalul C2 și dulapul 8. Apoi oferă F01/F02 și fișa F03. Nu presupune că echipele au rezolvat singure.\n\nÎn panou, butonul „Indicii / final asistat” permite această încheiere; concluziile nu sunt validate automat.\n\nPăstrează discuția: Denis a fabricat falsuri; Victor a păstrat banii găsiți. Recuperarea banilor nu repară automat hărțuirea.\n\nÎn caz de disconfort, oprește imitarea insultelor. Nu cere exemple personale de hărțuire. Toate numele din joc sunt fictive.')]
    guide += [(f'{i+1}. {s["title"]} / {s["time"]}',s['body']+'\n\nDE SPUS GRUPULUI\n'+(s['say'] or 'Nu este nevoie de un text pentru participanți.')+'\n\nFOI\n'+(', '.join(s['docs']) or 'Pregătește pachetele, nu preda probe încă.')+'\n\nCONFIRMARE\n'+s['check']) for i,s in enumerate(DATA['moderatorSteps'])]
    text_pdf('00-ghid-pas-cu-pas.pdf','Ghid pas cu pas',guide);metadata('00-ghid-pas-cu-pas.pdf','Moderator / pas cu pas','Pregătire, text de citit, predări, sprijin și încheiere')
    solutions=[];hints=[]
    for p in DATA['puzzles']:
        solutions.append((p['title'],f'Runda {p["round"]}\n\nMATERIAL DISPONIBIL\n'+', '.join(p['evidence'])+'\n\nOPERAȚIE\n'+p['operation']+'\n\nRĂSPUNS ACCEPTAT\n'+p['answer']+'\n\nDEPENDENȚĂ\n'+('Înainte de predarea pachetului 4 se verifică traseul p5. Finalul se predă după cele șase concluzii sau prin încheiere asistată.' if p['round']>=3 else 'Materialele sunt disponibile în rundele 0–'+str(p['round'])+'. Concluzia nu necesită finalul.')+'\n\nCONFIRMARE\nCere ID-urile și explicația. Nu accepta doar numele sau o presupunere.'))
        hints.append((p['title'],'INDICIU 1 / ORIENTARE\n'+p['hints'][0]+'\n\n________________________________________\nDecupează înainte de a preda un singur nivel.\n________________________________________\n\nINDICIU 2 / SPRIJIN\n'+p['hints'][1]+'\n\nPentru moderator: notează indiciul oferit. Nu preda această pagină integral dacă vrei să oferi doar nivelul 1.'))
    text_pdf('08-indicii-moderator.pdf','Indicii gradate',hints);metadata('08-indicii-moderator.pdf','Indicii / numai pentru moderator','Două niveluri pentru fiecare dintre cele șase concluzii')
    text_pdf('09-solutii-moderator.pdf','Matricea soluțiilor',solutions);metadata('09-solutii-moderator.pdf','Soluții și dovezi','Material, operație, răspuns, dependență și verificare')
    svg=[(OFF/'assets'/f'harta-{n}.svg').read_text(encoding='utf-8') for n in ['participanti','moderator']]
    target=QA/'harta.html';target.write_text('<meta charset="utf-8"><style>@page{size:A4;margin:10mm}body{margin:0}section{height:270mm;break-after:page}section:last-child{break-after:auto}svg{width:190mm;height:260mm}</style>'+''.join('<section>'+s+'</section>' for s in svg),encoding='utf-8');chrome([f'--print-to-pdf={OUT/"10-harta-salii.pdf"}',target.as_uri()]);metadata('10-harta-salii.pdf','Harta sălii','Pagina 1: participanți; pagina 2: moderator')
    props_pdf();metadata('11-recuzita.pdf','Bani și etichete de recuzită','10 cartonașe de 500 lei, 14 etichete și fișa plicului')
    # Capturi reale ale interfețelor fictive create pentru caz.
    capdir=OFF/'assets/capturi';capdir.mkdir(exist_ok=True)
    captures=[d for d in DATA['docs'] if d['format'] in ['post','profile','chat','police']]
    for d in captures:
        target=evidence_html([d],'captura-'+d['id'],True);path=capdir/(d['id']+'.png');chrome(['--virtual-time-budget=800','--window-size=900,1200',f'--screenshot={path}',target.as_uri()]);d['capture']='assets/capturi/'+d['id']+'.png'
    DATA['pdfs']=sorted(PDFS,key=lambda p:p['file']);DATA['printPages']=sum(p['pages']*p['copies'] for p in PDFS);write()
    (ROOT/'pdf-counts.json').write_text(json.dumps({p['file']:p['pages'] for p in PDFS},indent=2),encoding='utf-8')
    with zipfile.ZipFile(OFF/'materiale-printabile.zip','w',zipfile.ZIP_DEFLATED) as z:
        for p in OUT.glob('*.pdf'):z.write(p,Path('PDF-uri')/p.name)
        z.write(ROOT/'HARTA-SALII.md','HARTA-SALII.md')
    print(json.dumps(dict(documents=len(DATA['docs']),pdfs=len(PDFS),pages=DATA['printPages'],captures=len(captures)),ensure_ascii=False))
if __name__=='__main__':build()
