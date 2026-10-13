# Plicul dispărut

Escape room educațional în română, pentru trei echipe cu număr flexibil de participanți. Scenariu aprobat: Dan, 5 000 de lei, camera defectă, acuzații false, cont imitat și document modificat. Denis fabrică falsurile; Victor, paznicul spațiilor de alături care face curat pe afară, găsește plicul lângă ușă și păstrează banii.

## Pornește

Repository: [haiungheni/escaperoom](https://github.com/haiungheni/escaperoom).

Descarcă [kitul offline](platforma/kit-offline.zip), [proiectul complet](PLICUL-DISPARUT-proiect-complet.zip) sau [ghidul moderatorului](platforma/offline/pdf/00-ghid-pas-cu-pas.pdf). La arhive, folosește butonul de descărcare din pagina fișierului.

Site: https://ecoul-dosarul-16.jocundvole.chatgpt.site — panoul și descărcările cer parola comunicată separat. Adresa păstrează numele vechiului proiect.

Offline: extrage platforma/kit-offline.zip și deschide index.html din folderul PLICUL-DISPARUT. În proiectul local poți deschide direct platforma/offline/index.html. Nu necesită internet sau instalare. Participanții primesc numai foi; folderul cu soluții rămâne la moderator.

Începe cu 00-ghid-pas-cu-pas.pdf. Imprimă o dată fiecare dintre cele 20 PDF-uri: 82 pagini pentru setul de bază. Multiplică fișele de echipă dacă ai nevoie. Sortează dosarul comun, 12 pachete (4 runde × 3 echipe) și FINALUL. Ghidul, soluțiile și indiciile stau separat.

## Condu jocul

Panoul are opt etape, texte de citit, butoane de consemnare a predării, starea celor trei echipe, șase concluzii de verificat și câte două indicii. Progresul, notițele și timpul se păstrează în browserul local. Se pot exporta într-un raport JSON. Resetarea cere o confirmare în panou.

Țintă standard: 100 minute, cu 90–100 minute estimate pentru parcurs. Cerința de minimum 75 minute este inclusă în scenariu, dar durata reală trebuie verificată prin repetiție. Nu a avut loc un pilot cu participanți. Fără laptop, urmează ghidul și folosește un ceas.

Echipament: plicuri sau dosare, foi, pixuri, un ceas, cleme, foarfece pentru recuzită și bandă albastră. 11-recuzita.pdf conține cartonașele, etichetele și fișa plicului. Nu folosi bani reali.

Ușa este pe stânga și canapeaua pe dreapta. Jocul rămâne în aceeași sală. Spațiile vecine și intervenția poliției sunt reprezentate prin documente; nu se confruntă persoane reale.

## Dovezile

51 probe, fotografii generate special pentru caz, 14 capturi PNG ale interfețelor fictive și documente PDF cu aspect de dosar. Toate sunt marcate ca materiale de joc. Nu sunt capturi din conturi reale sau acte oficiale; nu folosesc sigle, semnături ori ștampile reale. Originalele fotografiilor centrului nu sunt distribuite.

Stilul panoului preia violetul, coralul, verdele deschis și cardurile rotunjite din proiectul local milion. Stilul probelor este separat, potrivit fiecărui tip de document.

## Întreținere

Sursa canonică: scripts/case_plic.py. Renderer comun pentru panou/capturi/PDF: platforma/offline/evidence.js. Harta: scripts/map_plic.py.

Ordine: python scripts/encode_photos.py (numai când se schimbă imaginile); python scripts/build.py; python scripts/package_offline.py; python scripts/validate.py. În acest mediu folosește .venv/Scripts/python.exe.

QA: python scripts/qa_browser.py și python scripts/render_qa.py. Pentru server: node platforma/scripts/build-worker.mjs și node platforma/scripts/test-auth.mjs. Generatoarele vechi case_v2/content/refine sunt istorice și nu fac parte din arhiva proiectului curent.

Publicarea folosește proiectul existent din platforma/.openai/hosting.json. Worker-ul servește toate resursele după verificarea sesiunii; nu există un director static care să ocolească parola. Valorile PASSWORD_SALT/PASSWORD_HASH/SESSION_KEY sunt secrete în Sites. Nu sunt incluse în kit.

Configurația locală Sites este ignorată de Git. Arhiva proiectului complet include identificatorul proiectului publicat; autentificarea și secretele se configurează separat în contul proprietarului.
