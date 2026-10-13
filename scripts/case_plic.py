"""Sursa canonică a cazului aprobat. Toate persoanele și documentele sunt fictive."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
DOCS=[]
def doc(id,title,body,team='comun',round=0,format='paper',source='',**extra):
    item=dict(id=id,title=title,body=body.strip(),team=team,round=round,format=format,source=source or 'Dosar de joc / 2–6 octombrie 2026',**extra)
    DOCS.append(item)
    return item

INTRO='''E vineri, spre seară. La centrul de tineret se pregătește o întâlnire cu foștii voluntari. Se aduc scaune, se aranjează fotografii și se pregătesc afișe.
Dan, coordonatorul, a numărat împreună cu Mara 5 000 de lei pentru materialele atelierului de fotografie. Banii sunt într-un plic pe masa de lucru. Dan merge după dosarul în care urma să-l pună.
Când revine, plicul nu mai este acolo. Camera de la intrare nu a înregistrat nimic. Pe pagina centrului apare o fotografie cu Ana și un comentariu care o acuză.
Dan anunță poliția. Câteva zile mai târziu, aveți copii ale documentelor strânse și ale materialelor care au circulat online. Unele persoane nu au spus tot; unele materiale sunt false.
Aflați pe unde a ajuns plicul, cine a luat banii și cine a fabricat acuzațiile. Nu alegeți un vinovat numai fiindcă pare suspect.
Lucrați în trei echipe. După fiecare rundă, puneți informațiile pe masa comună. Tot ce aveți nevoie este în materialele jocului. Nu se caută pe internet și nu se contactează persoane reale.'''
doc('O01','Plicul dispărut',INTRO,format='brief',source='Introducere / de citit cu voce tare')
doc('O02','Fișa de numărare a plicului','''2 octombrie 2026 / ora 15:50
Scop: materiale pentru atelierul de fotografie.
10 bancnote × 500 lei = 5 000 lei.
Plic crem; pe față: „5 000 / atelier foto”. Colțul din dreapta sus este reparat cu bandă albastră. În interior este o fișă mică de numărare cu suma scrisă de mână.
Suma verificată de: Dan și Mara. Plicul este pus pe masa de lucru.
Dan: confirm numărarea. Mara: confirm aceeași sumă.''',format='ledger',source='Centrul de tineret / evidență internă / FN-02')
doc('O03','Proces-verbal de constatare / extras','''Dosar de joc 017/2026 / 5 octombrie 2026 / ora 09:00
Sesizare: Dan, coordonatorul centrului de tineret.
Fapt relatat: la 2 octombrie, între 16:02 și 16:17, un plic cu suma declarată de 5 000 lei a dispărut de pe masa de lucru.
Au fost primite: fișa de numărare FN-02, fotografii de la pregătiri, declarații scrise și copii ale unor postări.
La verificarea locului: masa de lucru în centru; canapeaua în dreapta; ușa în stânga. Lângă intrare fusese pus temporar un scaun albastru. Pragul duce spre zona exterioară comună.
Nu sunt disponibile imagini de la camera intrării. Din declarațiile primite nu se stabilește, la această etapă, cine a luat plicul.
Întocmit în universul fictiv: ofițer de caz Irina Lupu. Luat la cunoștință: Dan.
Acest extras consemnează informațiile primite; nu este un verdict.''',format='police',source='POLIȚIE / dosar fictiv 017/2026 / PC-01')
doc('O04','Camera de la intrare / cerere de reparație','''1 octombrie 2026 / ora 18:10 / tichet CAM-07
Administrator → service: Camera de la intrare este aprinsă, dar înregistrarea nu se salvează. Ultima înregistrare disponibilă: 1 octombrie, 17:42. Rog verificare.
Service → administrator / 2 octombrie, 09:15: Tichet primit. Intervenția este programată pentru 5 octombrie.
Nu există înregistrări pentru 2 octombrie, 16:00–16:30. Defecțiunea a fost anunțată înainte de dispariția plicului.''',format='service',source='Evidența centrului / copie tichet CAM-07')
doc('O05','Plicul înainte de pregătiri','''Fotografie făcută de Mara la numărare / 2 octombrie, 15:50.
Plic crem cu inscripția „5 000 / atelier foto”; bandă albastră la colțul din dreapta sus. Fișa de numărare este lângă el înainte de a fi pusă în interior.
Fotografia arată aspectul plicului. Nu arată cine l-a luat.''',format='photo',source='Albumul Marei / IMG_1550',photo=2)

doc('A11','Postarea care o acuză pe Ana','''Vocea centrului / @vocea.centrului / 2 octombrie, 16:25
„Ieri umbla cu el. Azi au dispărut banii. Mai trebuie explicat ceva?”
Fotografia atașată o arată pe Ana cu un plic. Inscripția nu este vizibilă în această versiune.
Comentarii: „Să explice unde sunt banii.” / „Eu am distribuit, să vadă toți.” / „Dați-o afară din echipă.”
42 distribuiri / 18 comentarii. Aceste numere nu confirmă acuzația.''','A',1,'post','Agora / agora.example / copie a postării',photo=0,crop=True,user='Vocea centrului',handle='@vocea.centrului',time='2 oct. · 16:25',post='Ieri umbla cu el. Azi au dispărut banii. Mai trebuie explicat ceva?',comments=['Să explice unde sunt banii.','Eu am distribuit, să vadă toți.','Dați-o afară din echipă.'])
doc('A12','Profilul cu mesajul despre bani','''Ana Rusu / @ana.rusuu / profil creat la 2 octombrie
2 octombrie / 16:31: „Îi întorc luni. Nu faceți atâta gălăgie pentru 5 000.”
Fotografie de profil: Ana. Descriere: voluntară la centru.
Profilul folosește adresa agora.example/ana.rusuu. Aceasta este copia primită de Dan, nu o confirmare a identității autorului.''','A',1,'profile','Agora / agora.example/ana.rusuu',user='Ana Rusu',handle='@ana.rusuu',time='2 oct. · 16:31',post='Îi întorc luni. Nu faceți atâta gălăgie pentru 5 000.',created='2 octombrie 2026',avatar=True)
doc('A13','Profilul folosit de Ana înainte de caz','''Ana Rusu / @ana.rusu / profil activ din februarie 2024
1 octombrie / 18:20: „Mâine pregătim sala. Cine poate aduce cleme pentru afișe?”
Adresa: agora.example/ana.rusu.
Ana a furnizat această copie a profilului pe care îl folosește. Ea declară că nu a creat profilul @ana.rusuu și nu a publicat mesajul despre bani.
O poză identică nu înseamnă că două conturi au același proprietar.''','A',1,'profile','Copie furnizată de Ana / profilul ei',user='Ana Rusu',handle='@ana.rusu',time='1 oct. · 18:20',post='Mâine pregătim sala. Cine poate aduce cleme pentru afișe?',created='februarie 2024',avatar=True)
doc('A14','Prima declarație a Anei','''5 octombrie / 09:20
În poza de ieri țineam afișele. Nu am luat niciun plic cu bani. Eu nu am scris că îi întorc luni.
Nu am luat nimic de pe masa lui Dan. Am pregătit afișele lângă intrare, apoi m-am întors în sală.
Când au început comentariile, mi-a fost frică să mai spun ceva. Cineva mi-a trimis și mesajul „Să nu te mai vedem la centru”.
Declarație oferită în poveste de Ana. Prima relatare; poate fi comparată cu alte materiale.''','A',1,'statement','Declarație fictivă / DA-01')
doc('B11','Fotografia distribuită','''Versiune primită de Dan odată cu postarea de la 16:25.
Fotografia a fost decupată. Nu se vede partea de jos a plicului și nici inscripția.
Fișier primit: ana_plic_distribuit.png. Ora distribuirii nu este ora fotografierii.''','B',1,'photo','Copie din postarea @vocea.centrului',photo=0,crop=True)
doc('B12','Fotografia întreagă','''Fotografia din albumul de pregătiri / 1 octombrie, 17:35.
Pe plic scrie „AFIȘE”. Aceeași haină, aceeași poziție a mâinilor și același fundal se văd în versiunea distribuită.
Mara, fotografa: aceasta este fotografia făcută de mine cu o zi înainte. Nu este o fotografie din momentul dispariției banilor.''','B',1,'photo','Albumul Marei / IMG_1735',photo=0)
doc('B13','Sala în timpul pregătirilor','''2 octombrie / 16:06 / fotografie de ansamblu făcută de Mara.
Ana ține o mapă albastră lângă ușa din stânga. Un scaun albastru este pus temporar în dreptul intrării. Canapeaua este în dreapta.
Nu se vede în fotografie nici plicul cu bani, nici o persoană luându-l.''','B',1,'photo','Albumul Marei / IMG_1606',photo=1)
doc('B14','Fișa fotografiilor originale','''Album pus la dispoziție de Mara / 5 octombrie, 09:25
IMG_1735: 1 octombrie, 17:35 / Ana cu afișele.
IMG_1550: 2 octombrie, 15:50 / plicul și fișa de numărare.
IMG_1606: 2 octombrie, 16:06 / pregătirile de la intrare.
Mara confirmă că versiunile din album sunt fotografiile sale întregi. ana_plic_distribuit.png este o copie decupată, nu un original din album.''','B',1,'ledger','Albumul Marei / inventar foto IF-01')
doc('C11','Cine a fost în sală','''2 octombrie / foaie de pregătiri, nu registru al tuturor trecătorilor
Dan: 15:00–16:02; revine la 16:17.
Mara: în sală de la 15:10; face fotografii.
Ana: de la 15:15; pregătește afișe, merge până la intrare.
Sergiu: de la 15:20; aranjează mesele, merge după șervețele.
Denis: aduce o cutie la 15:30 și pleacă la 15:40.
Lângă intrare au trecut un curier, o vecină cu niște cutii și cineva care făcea curat la spațiile de alături. Persoanele care nu au intrat în sală nu sunt trecute individual pe această foaie.''','C',1,'ledger','Foaia pregătirilor / FP-02')
doc('C12','Nota lui Dan despre interval','''La 15:50 am numărat plicul cu Mara. La 16:02 m-am dus după dosar. Când am revenit, la 16:17, plicul nu mai era pe masă.
Nu am verificat fiecare persoană care a trecut pe lângă ușă. Eu eram în încăperea cu dosarele în acel interval.
Nu știu când a dispărut de pe masă și nici cine l-a luat. Camera nu poate lămuri acest lucru.''','C',1,'statement','Declarația fictivă a lui Dan / DD-01')
doc('C13','Lista de lucru pentru intrare','''Pregătiri, 2 octombrie
Ana: scoate afișele din mapa albastră și prinde-le pe suportul de la intrare. După ce termini, adu mapa înapoi pe masă.
Sergiu: lasă culoarul liber după mutarea scaunelor.
Scaunul albastru de lângă prag este temporar. Nu este destinat invitaților.
Nu sunt prevăzute probe sau materiale în dulapurile reale ale centrului.''','C',1,'note','Bilețelul de pregătiri / BP-01')
doc('C14','Schița locului','''Intrarea este în stânga; canapeaua în dreapta; mesele în centru. Scaunul albastru a fost lângă prag în timpul pregătirilor.
Pe partea exterioară este o zonă comună de trecere spre spațiile comerciale alăturate. Cine trece pe acolo nu trebuie să intre în centru.
Schița reprezintă cazul. În joc, toate materialele sunt în aceeași sală; nu ieșiți să cercetați spațiile reale.''','C',1,'map','Schiță de caz / nu plan tehnic',map=True)

FAKE=[['Sergiu','16:03','Ia plicul. Împărțim banii după.'],['Ana','16:03','Bine, îl duc la intrare.'],['Sergiu','16:04','Vin imediat.']]
REAL=[['Sergiu','16:03','Ia mapa. Împărțim afișele după.'],['Ana','16:03','Bine, o duc la intrare.'],['Sergiu','16:04','S-a vărsat apă pe masă. Mut plicul pe partea uscată, peste mapă. Mă duc după șervețele.'],['Ana','16:08','Am pus afișele. Mapa e înapoi pe masă.'],['Sergiu','16:09','Am revenit. Șterg masa acum.']]
doc('A21','Captura despre Sergiu','\n'.join(f'{a} / {b}: {c}' for a,b,c in FAKE)+'\nCaptură distribuită la 2 octombrie, 16:42, de @vocea.centrului. Nu este conversația furnizată de interlocutori.','A',2,'chat','Captură primită în grupul voluntarilor',messages=FAKE,chatTitle='Ana · conversație cu Sergiu',time='2 octombrie')
doc('A22','Conversația furnizată de Ana','\n'.join(f'{a} / {b}: {c}' for a,b,c in REAL)+'\nAna pune la dispoziție conversația integrală; Sergiu confirmă aceleași mesaje.','A',2,'chat','Copie oferită de interlocutori / CA-02',messages=REAL,chatTitle='Ana · conversație cu Sergiu',time='2 octombrie')
doc('A23','Ce a primit Ana după acuzație','''2 octombrie / materiale păstrate de Ana
16:34: „Să nu mai vii la centru.”
16:36: fotografie de profil redistribuită cu textul „Voluntara anului”.
16:39: „Să dea banii, după aceea să vorbească.”
Ana: am păstrat copiile, i-am spus lui Dan și am cerut să fie oprite mesajele. Nu am răspuns cu insulte și nu am publicat datele celor care mi-au scris.
Aceste mesaje arată hărțuirea, nu demonstrează furtul.''','A',2,'post','Copii furnizate de Ana / HA-01',user='Mesaje primite de Ana',handle='arhivă personală',time='2 oct. · 16:34–16:39',post='După acuzație au început mesajele.',comments=['Să nu mai vii la centru.','Voluntara anului.','Să dea banii, după aceea să vorbească.'])
doc('A24','Împrumutul lui Sergiu','''Declarația colegului / 5 octombrie, 10:10
I-am împrumutat lui Sergiu 200 de lei pentru transport pe 30 septembrie. Mi i-a întors pe 1 octombrie. Nu am spus că ar fi avut o datorie de 5 000 de lei.
Mesaj păstrat / 1 octombrie, 19:10: Sergiu — „Ți-am întors cei 200. Mulțumesc că m-ai ajutat.”
O nevoie de bani nu dovedește că o persoană a furat. Verificați ce știe efectiv martorul.''','A',2,'statement','Declarație fictivă / DS-02')
doc('B21','Documentul care circulă în grup','''NOTĂ 04 / dosar 017/2026 / 5 octombrie, 09:10
Au fost analizate fișele cu sumele de 5 300 lei și 5 000 lei.
Lipsa banilor a fost pusă în legătură cu diferențele din evidența coordonatorului Dan. Există motive să fie considerat responsabil pentru dispariția plicului.
Nume tipărit: Irina Lupu.
Copie transmisă în grup la 09:35. Proveniență declarată de expeditor: „de la poliție”.''','B',2,'police','Fotografie distribuită online / proveniență neverificată',reference='NOTĂ 04 / COPIE DISTRIBUITĂ')
doc('B22','Nota 04 / copia verificată','''NOTĂ 04 / dosar fictiv 017/2026 / 5 octombrie, 09:10
Au fost primite fișele cu sumele de 5 300 lei și 5 000 lei, împreună cu documentul unei cheltuieli de 300 lei.
Suma reclamată ca dispărută este 5 000 lei. Documentele primite urmează a fi comparate. Această notă nu atribuie furtul coordonatorului sau altei persoane.
Întocmit în universul fictiv: Irina Lupu.
Aceasta este copia care corespunde documentului păstrat în dosarul de joc.''','B',2,'police','Copie verificată / NOTĂ 04',reference='NOTĂ 04 / COPIE DIN DOSAR')
doc('B23','Fișa încasărilor și soldului','''Târgul voluntarilor / 2 octombrie / FI-02
Încasări totale: 5 300 lei.
Cheltuială înainte de închiderea evidenței: 300 lei / bon B-103.
Sold numărat la 15:50: 5 000 lei.
Destinația soldului: materiale pentru atelierul de fotografie.
Verificat de Dan și Mara. Pentru cheltuială consultați bonul B-103, nu presupuneți o lipsă.''','B',2,'ledger','Evidența centrului / FI-02')
doc('B24','Clarificarea copiei distribuite','''Dosar fictiv 017/2026 / CL-04 / 5 octombrie, 11:00
Copia distribuită în grup sub titlul NOTĂ 04 nu corespunde copiei păstrate în dosar.
Au fost adăugate frazele despre responsabilitatea coordonatorului; a fost eliminată mențiunea cheltuielii de 300 lei.
Aspectul și numele tipărit nu confirmă proveniența unui document. Pentru comparație sunt furnizate ambele versiuni.
Nicio copie a NOTEI 04 nu consemnează că Dan a recunoscut un furt.''','B',2,'police','Clarificare fictivă / CL-04')
doc('C21','Declarația lui Sergiu','''5 octombrie / 09:45
La 16:04 s-a vărsat apă pe masă. Am ridicat plicul și l-am pus pe partea uscată, peste mapa albastră. Nu l-am deschis. Am mers după șervețele.
Nu i-am spus Anei că îl pusesem acolo. Când m-am întors, mapa era din nou pe masă, iar Ana terminase cu afișele.
Nu am văzut plicul căzând și nu am văzut cine l-a luat. În captura distribuită apar cuvinte pe care nu le-am scris.''','C',2,'statement','Declarație fictivă / DS-01')
doc('C22','Ana completează declarația','''5 octombrie / 10:00 / completare DA-02
Am luat mapa albastră de pe masa lui Dan la 16:06. Nu am luat intenționat un plic. Am deschis mapa lângă scaunul de la intrare ca să scot afișele.
Nu m-am uitat după scaun și nu am observat să cadă ceva. La 16:08 am pus mapa înapoi pe masă.
În prima declarație am spus că nu am luat nimic de pe masă. Nu era corect: luasem mapa. Mi-a fost frică să spun, fiindcă toți vorbeau deja despre mine.''','C',2,'statement','Completare fictivă / DA-02')
doc('C23','Bonul pentru cei 300 de lei','''ATELIER HÂRTIE / magazin fictiv
BON B-103 / 2 octombrie 2026 / 14:35
Carton pentru afișe: 120 lei
Bandă adezivă: 80 lei
Cleme pentru panou: 100 lei
TOTAL: 300 lei / achitat numerar
Primitor în evidența centrului: Dan. Cheltuiala este consemnată în FI-02 înainte de numărarea plicului.''','C',2,'receipt','Bon de recuzită / fără date fiscale reale')
doc('C24','Mara despre masa udă','''5 octombrie / 10:20
Am văzut apa pe masă în jur de 16:04. Sergiu a mutat plicul pe mapa albastră și a plecat după șervețele. Nu a pus plicul în buzunar.
La 16:06 am fotografiat-o pe Ana cu mapa lângă intrare. Pe lângă prag era scaunul albastru. La 16:08 era din nou în sală.
Nu văd în fotografia mea partea de dincolo de scaun. Fotografia nu poate arăta dacă era ceva pe jos.''','C',2,'statement','Declarație fictivă / DM-01')

DENIS=[['Denis','2 oct. 16:22','Am poza cu Ana. Dacă tai partea cu AFIȘE, o să creadă că ține banii.'],['Lilia','2 oct. 16:23','Nu pune asta. Nu știi cine a luat plicul.'],['Denis','2 oct. 16:30','Am făcut și profilul cu numele ei. Las-o să explice.'],['Lilia','5 oct. 09:32','De ce ai schimbat textul notei despre Dan?'],['Denis','5 oct. 09:33','Să-i creadă pe toți implicați. Am pus și captura cu Sergiu.'],['Lilia','5 oct. 09:34','Nu mai distribui. Îi trimit lui Dan conversația întreagă.']]
doc('A31','Conversația primită de la Lilia','\n'.join(f'{a} / {b}: {c}' for a,b,c in DENIS)+'\nLilia pune la dispoziție conversația și atașamentele primite.','A',3,'chat','Copie furnizată de interlocutor / LD-01',messages=DENIS,chatTitle='Lilia · conversație cu Denis',time='2–5 octombrie')
doc('A32','Declarația Liliei','''5 octombrie / 11:20
Am primit de la Denis poza decupată, captura schimbată și copia notei despre Dan. I-am spus să nu le publice. În conversația completă se văd mesajele și ordinea atașamentelor.
Ana și Denis avuseseră un conflict după ce ea refuzase să-i publice un filmuleț în care își bătea joc de un alt voluntar. Asta explică supărarea lui, dar nu dovedește singură cine a făcut contul.
Nu l-am văzut pe Denis luând bani. Nu știu unde este plicul.''','A',3,'statement','Declarație fictivă / DL-01')
doc('A33','Declarația lui Denis','''5 octombrie / 13:10
Eu am făcut profilul @ana.rusuu și postările de pe @vocea.centrului. Am schimbat mesajele lui Sergiu și textul notei despre Dan. Fotografia Anei era publică; copia notei o primisem în grup.
Eram supărat pe Ana și am folosit vestea despre bani ca să o fac de rușine. Nu am luat plicul și nu știu unde este. Plecasem de la centru înainte să fie pus pe masă.
Recunosc falsificările. Accept ca materialele furnizate de Lilia să fie comparate cu ce am trimis eu.''','A',3,'statement','Declarație fictivă / DDEN-01')
doc('B31','Inventarul materialelor comparate','''Dosar fictiv 017/2026 / IM-03 / 5 octombrie, 12:00
1. Fotografie originală IMG_1735, furnizată de Mara; copie decupată primită de Lilia de la Denis; aceeași copie în postarea @vocea.centrului.
2. Conversația Ana–Sergiu, furnizată de interlocutori; versiune modificată primită de Lilia de la Denis; aceeași versiune distribuită la 16:42.
3. NOTĂ 04 din dosarul de joc; copie cu fraze adăugate despre Dan, primită de Lilia de la Denis și distribuită în grup.
Materialele confirmă legătura lui Denis cu falsificările. Nu consemnează recuperarea banilor de la el.''','B',3,'police','Inventar fictiv / IM-03')
doc('B32','Fișa de sosire la atelierul din bibliotecă','''2 octombrie / atelier de machete / bibliotecă fictivă
Participant: Denis / sosire 16:00 / plecare 17:25.
Responsabilul atelierului, Elena: Denis a lucrat la aceeași masă de la început până la pauza de la 17:20. Nu a lipsit între 16:00 și 16:30.
Fișa este furnizată de organizator, separat de declarația lui Denis. Biblioteca nu se află în clădirea centrului.''','B',3,'ledger','Evidența organizatorului / AB-02')
doc('B33','Bonul de deplasare','''TRANSPORT LOCAL / cursă fictivă TL-204
2 octombrie / preluare 15:41 / sosire 15:54
Punct de plecare: zona centrului de tineret
Destinație: biblioteca de cartier
Pasager: Denis / sumă 45 lei
Bon furnizat în poveste împreună cu confirmarea șoferului: cursa s-a încheiat la destinația indicată. Nu este o înregistrare GPS și nu folosește date personale reale.''','B',3,'receipt','Bon de recuzită / TL-204')
doc('C31','Declarația curierului','''5 octombrie / 11:40
Am ajuns la intrarea centrului la 16:09. Ana era deja în sală. Lângă prag, dinspre exterior, cineva cu un cărucior de curățenie s-a aplecat după scaunul albastru și a ridicat ceva crem.
Am crezut că strânge hârtii. Nu i-am văzut bine fața și nu pot spune cine era. Căruciorul avea găleată portocalie; pe fișa prinsă de mâner scria C2.
Ora o știu din documentul de livrare, nu din memorie.''','C',3,'statement','Declarație fictivă / DC-01')
doc('C32','Documentul de livrare','''Livrare L-219 / 2 octombrie
16:09 — curier ajuns la intrarea centrului
16:11 — cutia predată Marei
16:13 — livrare închisă
Conținut: hârtie pentru imprimantă. Valoare achitată anterior; nu s-au predat bani curierului.
Mara confirmă primirea cutiei. Documentul fixează intervalul relatat în DC-01.''','C',3,'ledger','Evidență fictivă a livrării / L-219')
doc('C33','Declarația vecinei','''5 octombrie / 12:10
În jur de 16:12 duceam niște cutii spre spațiile comerciale. Am văzut un cărucior cu găleată portocalie intrând pe ușa spațiului de serviciu al clădirii de alături. Pe suport era fișa C2.
Nu am văzut bani și nu am văzut persoana luând ceva. Nu pot recunoaște fața din acel moment.
Spațiul de serviciu aparține clădirii de alături, nu centrului de tineret.''','C',3,'statement','Declarație fictivă / DV-01')
doc('C34','Verificarea tehnică a camerei','''5 octombrie / raport fictiv RT-07
Tichetul CAM-07 a fost înregistrat la 1 octombrie, 18:10, înainte de dispariția plicului.
Camera avea o defecțiune de salvare. Pentru 2 octombrie nu sunt disponibile înregistrări. Nu a fost recuperată o filmare cu furtul.
Din materialele acestei verificări nu rezultă că defecțiunea a fost provocată pentru a lua banii. Lipsa imaginilor nu dovedește cine este hoțul.''','C',3,'service','Raport de recuzită / RT-07')

doc('A41','Programul curățeniei de alături','''2 octombrie / spațiile comerciale de alături / PCUR-02
Larisa: curățenie în interior, 15:30–15:55; cărucior C2.
Victor: curățenie exterioară, 15:55–16:15; cărucior C2.
Larisa: curățenie în interior, 16:15–16:40; cărucior C2.
Gheorghe: întreținere în curtea din spate, 15:45–16:30; cărucior C1.
Victor este paznicul spațiilor comerciale și se ocupă și de curățenia din jurul lor. Nu este angajat al centrului de tineret.''','A',4,'ledger','Evidența clădirii vecine / PCUR-02')
doc('A42','Predarea căruciorului','''2 octombrie / fișa C2 / PE-02
15:55 — Larisa predă C2 lui Victor.
16:15 — Victor predă C2 Larisei.
Observație Larisa: la predarea de la 16:15 nu mi-a spus că găsise un plic sau bani. Fișa de predare era prinsă de mâner.
Căruciorul este comun. Identificarea celui care îl folosea depinde de interval, nu doar de culoarea găleții.''','A',4,'ledger','Fișă fictivă de echipament / PE-02')
doc('A43','Relatarea inițială a lui Victor','''5 octombrie / 10:40
Vineri am făcut curat pe afară la spațiile comerciale. Nu am intrat în centrul de tineret. Am strâns hârtii și am dus căruciorul în spațiul de serviciu. La 16:15 l-am predat Larisei.
Nu cunosc discuțiile voluntarilor și nu folosesc grupul lor.
Această relatare nu precizează fiecare obiect ridicat de pe jos. Faptul că nu a intrat în centru trebuie comparat cu locul în care putea ajunge plicul.''','A',4,'statement','Declarație fictivă / DVI-01')
doc('B41','Căruciorul din zona de serviciu','''Fotografie de context a căruciorului cu găleată portocalie, lângă ușa spațiului de serviciu.
Fișa de echipament identifică acest set drept C2. Fotografia arată obiectul și locul; nu arată cine l-a folosit la ora furtului.
Nu este imagine de la camera defectă și nu este o filmare a furtului.''','B',4,'photo','Fotografie de context / FC2-01',photo=3)
doc('B42','Proces-verbal privind recuperarea / extras','''Dosar fictiv 017/2026 / PR-08 / 6 octombrie, 09:30
Loc consemnat: spațiul de serviciu al clădirii vecine, dulapul personal nr. 8.
Obiecte consemnate: un plic crem cu inscripția „5 000 / atelier foto”; bandă albastră pe colțul din dreapta sus; o fișă de numărare cu suma scrisă de mână; suma de 5 000 lei.
Fotografiile anexate și inventarul sunt furnizate pentru compararea obiectelor cu cele reclamate.
Acesta este extrasul despre obiecte. Identificarea persoanei se verifică separat prin evidența dulapurilor și materialele finale.
Întocmit în universul fictiv: Irina Lupu.''','B',4,'police','Proces-verbal fictiv / PR-08',reference='PR-08 / EXTRAS OBIECTE')
doc('B43','Fotografia plicului recuperat','''Anexă de joc la PR-08: plicul recuperat și fișa mică de numărare.
Inscripția, colțul reparat și fișa corespund descrierii O02 și fotografiei O05. Plicul este fotografiat pe masa de examinare.
Comparați și suma consemnată în PR-08; o fotografie a unui plic nu arată singură câți bani sunt în el.''','B',4,'photo','Anexă fotografică fictivă / PR-08-A',photo=4)
doc('C41','Schița traseului refăcut','''Repere pentru ordonare, de verificat cu surse:
Masa de lucru → mapa albastră → ușa din stânga → zona de după scaun, dinspre exterior → cărucior C2 → spațiul de serviciu al clădirii vecine.
Schița consemnează locuri, nu un nume de hoț. Legați fiecare trecere de o declarație, o oră sau un document.
Plicul putea fi ridicat fără ca persoana să intre în centrul de tineret.''','C',4,'map','Fișă de reconstrucție / TR-01',map=True)
doc('C42','Evidența dulapurilor personale','''Spațiul de serviciu al clădirii vecine / evidență valabilă la 2–6 octombrie
Dulap 6: Larisa.
Dulap 8: Victor.
Dulap 10: Gheorghe.
Administratorul spațiului confirmă că dulapul 8 era alocat lui Victor în intervalul indicat. Nu este un dulap al centrului de tineret.
Acest document identifică alocarea locului; se compară cu PR-08 și cu fișa de echipament.''','C',4,'ledger','Evidență fictivă / ED-08')
doc('C43','Fișa de numărare a sumei recuperate','''Dosar fictiv 017/2026 / SR-08 / 6 octombrie
Obiect: suma din plicul consemnat în PR-08.
10 bancnote × 500 lei = 5 000 lei.
Fișa mică din interior are suma scrisă de mână. Inscripția plicului: „5 000 / atelier foto”.
Comparație cu suma reclamată în O02: 5 000 lei.
Nu sunt consemnate aici bani găsiți la Denis, Ana sau Sergiu.''','C',4,'ledger','Inventar fictiv / SR-08')
doc('F01','Declarația finală a lui Victor','''6 octombrie / 10:20
La 2 octombrie am trecut cu C2 pe lângă intrarea centrului. Am văzut plicul după scaun, pe partea dinspre exterior. L-am ridicat și am văzut că are bani.
Nu îl căutasem și nu plănuisem să îl iau. După ce l-am găsit, am decis să păstrez banii. Am dus plicul în spațiul de serviciu și l-am pus în dulapul meu, nr. 8.
Nu am creat profilul Anei și nu am modificat conversațiile. Când am auzit că sunt acuzați voluntarii, nu am spus nimic despre plic.
Recunosc că am păstrat cei 5 000 de lei care nu îmi aparțineau.''',round=5,format='statement',source='Declarație finală fictivă / DVI-02')
doc('F02','Proces-verbal de predare a plicului','''Dosar fictiv 017/2026 / PP-09 / 6 octombrie, 11:00
Predat în universul cazului către Dan: plic crem „5 000 / atelier foto”, fișa mică de numărare și suma de 5 000 lei, conform PR-08 și SR-08.
Dan confirmă că aspectul plicului și suma corespund celor reclamate.
Materialele despre contul fals, falsificări și hărțuire sunt păstrate separat în dosarul de joc. Recuperarea banilor nu înseamnă că acuzațiile online au fost corectate.
Nume tipărite de recuzită: Irina Lupu / Dan.''',round=5,format='police',source='Proces-verbal fictiv / PP-09')
doc('F03','Ce publicăm după verificare','''Scrieți o corectare scurtă pentru pagina centrului.
1. Ce sumă a fost recuperată și ce s-a verificat despre plic?
2. Ce acuzații despre Ana, Sergiu și Dan nu se susțin?
3. Cine a fabricat materialele și cum se deosebește aceasta de furt?
4. Cum sprijinim persoanele hărțuite și oprim distribuirea falsurilor?
Nu repetați insultele și nu publicați date personale. Păstrați dovezile înainte de eliminarea materialelor abuzive. În joc nu se publică nimic pe un site real.''',round=5,format='worksheet',source='Fișă de încheiere / răspunsul echipelor')

OFFICIAL_TITLES={'O03':'PROCES-VERBAL DE CONSTATARE','B21':'NOTĂ DE EXAMINARE A DOCUMENTELOR','B22':'NOTĂ DE EXAMINARE A DOCUMENTELOR','B24':'NOTĂ DE CLARIFICARE','B31':'INVENTAR AL MATERIALELOR PRIMITE','B42':'PROCES-VERBAL PRIVIND RECUPERAREA OBIECTELOR','F02':'PROCES-VERBAL DE PREDARE'}
for d in DOCS:
    if d['id'] in OFFICIAL_TITLES:d['artifactTitle']=OFFICIAL_TITLES[d['id']]
    d['body']=d['body'].replace('Întocmit în universul fictiv:', 'Întocmit:').replace('Predat în universul cazului către Dan:', 'Predat către Dan:')
    if d['format']=='chat':d['note']=d['body'].rsplit('\n',1)[-1]
NOTES={'A11':'42 distribuiri / 18 comentarii. Numerele nu confirmă acuzația.', 'A12':'Copie primită de Dan. Ana declară că nu a creat acest profil și nu a publicat mesajul.', 'A13':'Ana a furnizat copia profilului pe care îl folosește. Declară că nu a creat @ana.rusuu.', 'A23':'Ana a păstrat copiile, i-a spus lui Dan și a cerut oprirea mesajelor. Nu a răspuns cu insulte și nu a publicat date personale.'}
for d in DOCS:
    if d['id'] in NOTES:d['note']=NOTES[d['id']]

GROUPS=[dict(id='A',name='Echipa 1',topic='Mesaje și conturi',color='violet',task='Verificați cine vorbește, dacă profilurile sunt autentice în poveste și ce mesaje au fost schimbate.'),dict(id='B',name='Echipa 2',topic='Fotografii și documente',color='coral',task='Comparați originalele cu versiunile distribuite. Nu luați un antet sau o fotografie drept verdict.'),dict(id='C',name='Echipa 3',topic='Ore, trasee și declarații',color='lime',task='Puneți întâmplările în ordine. Legați fiecare deplasare a plicului de o sursă.')]

PUZZLES=[
dict(id='p1',round=1,title='Fotografia și profilul Anei',answer='Fotografia este din ziua precedentă și plicul este pentru AFIȘE. @ana.rusuu imită @ana.rusu. Nu identificăm încă autorul contului și nu excludem toate întrebările despre traseu.',evidence=['A11','A12','A13','B11','B12','B14'],operation='Compară numele de utilizator, fotografia întreagă și inventarul albumului.',hints=['Priviți partea fotografiei care lipsește și adresa exactă a profilului.','B12 arată AFIȘE; A12 are un „u” în plus față de A13. B14 fixează ziua fotografierii.']),
dict(id='p2',round=2,title='Conversația despre Sergiu',answer='A21 a fost modificată. Originalul A22 spune MAPA și AFIȘELE, apoi descrie apa și mutarea plicului. Împrumutul nu demonstrează furtul.',evidence=['A21','A22','A24','C21','C24'],operation='Compară textul și succesiunea mesajelor cu declarațiile despre masă.',hints=['Nu vă opriți la faptul că Sergiu a atins plicul. Verificați cuvintele exacte.','A22 și C24 confirmă mutarea peste mapă, nu în buzunar. A24 clarifică împrumutul.']),
dict(id='p3',round=2,title='Cei 300 de lei și documentul despre Dan',answer='5 300 − 300 = 5 000 lei. Cheltuiala este anterioară numărării. B21 modifică NOTA 04; B22 și B24 nu atribuie furtul lui Dan.',evidence=['O02','B21','B22','B23','B24','C23'],operation='Calculează soldul și compară cele două versiuni ale notei.',hints=['Căutați cheltuiala și copia care corespunde dosarului, nu cea mai convingătoare ștampilă.','Bonul C23 este de 300 lei, la 14:35. B21 adaugă acuzația care lipsește din B22.']),
dict(id='p4',round=3,title='Autorul falsurilor nu este automat hoțul',answer='Denis a fabricat profilul, captura și nota. A plecat înainte de punerea plicului pe masă; B32 și B33 confirmă separat deplasarea și prezența la bibliotecă. Nu a luat banii.',evidence=['A31','A32','A33','B31','B32','B33','O02'],operation='Separă cele două fapte și compară ora numărării cu documentele independente.',hints=['Recunoașterea falsurilor răspunde la o întrebare, nu la toate. Unde era Denis când plicul a fost pe masă?','Denis pleacă la 15:41, ajunge la 15:54 și este la bibliotecă de la 16:00. Plicul este pe masă la 15:50.']),
dict(id='p5',round=3,title='Cum a ajuns plicul lângă ușă',answer='Sergiu îl mută peste mapă la 16:04; Ana duce mapa la intrare la 16:06 și o deschide; plicul alunecă după scaun, dinspre exterior. C31 plasează ridicarea unui obiect crem la 16:09, după revenirea Anei la 16:08.',evidence=['A22','B13','C22','C24','C31','C32','C14'],operation='Ordonează orele și verifică locul care nu apare în fotografia de ansamblu.',hints=['Cine a mutat mapa? Ce parte a pragului nu se vede în fotografie?','Combinați 16:04 → 16:06 → 16:08 → 16:09. Foaia C11 nu cuprinde toți trecătorii de afară.']),
dict(id='p6',round=4,title='Căruciorul și plicul recuperat',answer='Victor folosește C2 la 16:09 și îl duce spre spațiul de serviciu. Plicul este recuperat din dulapul 8, alocat lui. O02/O05 și B42/B43/C43 confirmă obiectul și suma de 5 000 lei. El nu lucrează la centru.',evidence=['C31','C32','C33','A41','A42','B42','B43','C42','C43','O02','O05'],operation='Leagă intervalul C2, locul de depozitare și identificarea plicului. Nu folosi doar profesia sau culoarea găleții.',hints=['C2 este comun. Cine îl folosea la ora fixată de livrare? Cui îi aparține dulapul menționat în PR-08?','La 16:09 C2 este la Victor; C42 atribuie dulapul 8 lui Victor. PR-08 consemnează acolo plicul și suma.'])]

STEPS=[
dict(id='s0',title='Pregătește sala și plicurile',time='Înainte de sosirea grupului',minute=-1,round=0,docs=[],say='',body='Imprimă pachetele pe echipe și runde. Ține finalul și soluțiile separat. Pune trei etichete de echipă, foi și pixuri pe mese. Ușa din stânga rămâne liberă; canapeaua este în dreapta. Banii sunt numai recuzită.',check='Materialele sunt sortate, soluțiile sunt la mine și ieșirea este liberă.'),
dict(id='s1',title='Citește începutul',time='0–10 minute',minute=0,round=0,docs=[d['id'] for d in DOCS if d['round']==0],say=INTRO,body='Împarte participanții cât mai echilibrat în trei echipe. Predă dosarul comun, câte o fișă de echipă și explică: fiecare concluzie trebuie să aibă o sursă. Nu spune numele hoțului și nu descrie finalul.',check='Am citit introducerea și am predat dosarul comun.'),
dict(id='s2',title='Runda 1: Ana și fotografia',time='10–30 minute',minute=10,round=1,docs=[d['id'] for d in DOCS if d['round']==1],say='Au apărut aceste materiale despre Ana. Verificați ce arată ele și ce doar afirmă. La final, fiecare echipă spune ce știe sigur și ce mai trebuie verificat.',body='Predă pachetul 1 potrivit fiecărei echipe. După aproximativ 15 minute, reunește concluziile. Acceptă identificarea fotografiei decupate și a profilului imitat, dar nu afirma încă cine le-a fabricat. Dacă termină devreme, cere explicații și contradicții, nu așteptare fără sarcină.',check='Echipele au comparat fotografia și profilurile, apoi au pus concluziile în comun.'),
dict(id='s3',title='Runda 2: Sergiu și Dan',time='30–50 minute',minute=30,round=2,docs=[d['id'] for d in DOCS if d['round']==2],say='Au apărut o conversație și o notă care pare de la poliție. Nu presupuneți că sunt autentice. Aveți și materiale cu care le puteți compara.',body='Predă pachetele 2. Echipa A verifică mesajele, B documentele și soldul, C declarațiile și bonul. Cere schimb de informații: bonul este la C, iar fișa sumelor la B. Validează separat conversația și diferența de 300 lei.',check='Au fost verificate conversația, soldul și copia modificată a notei.'),
dict(id='s4',title='Runda 3: două fapte diferite',time='50–70 minute',minute=50,round=3,docs=[d['id'] for d in DOCS if d['round']==3],say='Aceste materiale pot identifica autorul falsurilor. Verificați separat dacă el putea lua plicul. Mai aveți declarații despre ce s-a întâmplat lângă ușă.',body='Predă pachetele 3. Nu confirma că Denis este hoțul. A are autorul falsurilor, B are verificarea deplasării, C are martorii de lângă ușă. Reunește cele trei piste. Cere ordonarea orelor și precizarea părții exterioare a pragului.',check='Echipele au separat falsificările de furt și au refăcut traseul până la ușă.'),
dict(id='s5',title='Runda 4: leagă ultimele probe',time='70–85 minute',minute=70,round=4,docs=[d['id'] for d in DOCS if d['round']==4],say='Verificați cine folosea căruciorul la ora indicată și dacă plicul recuperat este același. Nu alegeți o persoană numai pentru că era prin preajmă.',body='Predă pachetele 4 numai după reunirea traseului din runda 3 sau după oferirea indiciului de sprijin. A are programul C2, B recuperarea obiectului, C evidența dulapurilor și suma. Fiecare echipă trebuie să explice o legătură diferită. Acceptă Victor numai cu interval + dulap + plic.',check='Verdictul este susținut de ore, echipament, locul de recuperare și identificarea plicului.'),
dict(id='s6',title='Citește finalul și verifică suma',time='85–90 minute',minute=85,round=5,docs=['F01','F02','F03'],say='Cazul are două persoane implicate în fapte diferite. Citiți finalul și verificați ce s-a recuperat. Acum mai avem de corectat acuzațiile care au circulat.',body='Înainte de predarea F01, cere verdictul echipelor cu surse. Apoi oferă declarația lui Victor și predarea plicului. Dacă nu au terminat, folosește finalul asistat și consemnează sprijinul; nu lăsa grupul fără deznodământ.',check='Am citit finalul; suma de 5 000 lei și autorii celor două fapte sunt lămuriți.'),
dict(id='s7',title='Încheie fără să repeți hărțuirea',time='90–100 minute',minute=90,round=5,docs=['F03'],say='Ce corectăm public? Ce facem pentru Ana și Sergiu? Cum păstrăm dovezile fără să distribuim din nou insultele?',body='Cere o corectare scurtă folosind F03. Discutați de ce o fotografie reală poate induce în eroare, de ce un cont cu aceeași poză nu dovedește identitatea și de ce autorul falsurilor nu este automat hoțul. Exportă raportul după sesiune.',check='Am discutat corectarea acuzațiilor și sprijinul pentru persoanele hărțuite.')]

DATA=dict(id='plic-v1',title='Plicul dispărut',subtitle='5 000 de lei. Trei echipe. Două fapte diferite.',duration=100,minDuration=90,maxDuration=110,groups=GROUPS,docs=DOCS,puzzles=PUZZLES,moderatorSteps=STEPS,intro=INTRO)
def write():
    (ROOT/'content.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'platforma/offline/data.js').write_text('window.CASE_DATA='+json.dumps(DATA,ensure_ascii=False)+';\n',encoding='utf-8')
    (ROOT/'MODERATOR-PAS-CU-PAS.md').write_text('# Plicul dispărut / moderator\n\n'+ '\n\n'.join(f"## {i+1}. {s['title']} / {s['time']}\n\n{s['body']}\n\nDe spus: {s['say']}\n\nFoi: {', '.join(s['docs']) or 'niciuna'}\n\nConfirmare: {s['check']}" for i,s in enumerate(STEPS)),encoding='utf-8')
    (ROOT/'inventar.md').write_text('# Plicul dispărut / inventar\n\n'+'\n'.join(f"- {d['id']} / {d['title']} / runda {d['round']} / echipa {d['team']}" for d in DOCS),encoding='utf-8')
if __name__=='__main__':
    write();print(json.dumps(dict(documents=len(DOCS),teams=len(GROUPS),puzzles=len(PUZZLES))))
