# Verificare / Plicul dispărut

13 octombrie 2026. Scenariul curent înlocuiește dosarul NORA.

- 51 probe, trei echipe, opt etape și șase concluzii cu două niveluri de indicii. Referințele și dependențele sunt verificate; numele hoțului nu apare în primele trei runde.
- 20 PDF-uri, 82 pagini: toate probele au câte o pagină, fiecare echipă are materiale în toate rundele. Ghidurile și indiciile sunt separate de pachetele participanților.
- 36 verificări funcționale în Chrome: configurare, timer/pauză, pachete, confirmări, căutare/filtre, imprimare, indicii, blocarea predării premature, verdict, final asistat, note, salvare/reîncărcare și resetare.
- 24 verificări pentru server: pagina de acces, protecția resurselor, origine, parola corectă/greșită, cookie semnat HttpOnly/Secure/SameSite, PDF/ZIP, cookie modificat, rotația cheilor, logout, configurație lipsă și limitarea încercărilor. Este verificată și acceptarea unei parole configurate de patru caractere, folosind o parolă de test.
- 290 verificări de integritate: date identice cu sursa, probe în pachetele corecte, text și diacritice, proveniența capturilor, marcajele de ficțiune, resurse locale și fișiere identice în arhivă.
- Randarea tuturor celor 82 pagini cu PyMuPDF nu indică text în afara marginilor. Exemple inspectate vizual: postare decupată, document atribuit poliției, plic recuperat, ghid, hartă și recuzită. Poppler nu este disponibil.
- Imprimarea din browser: o fișă și patru probe pe cinci pagini.
- Panoul inspectat la 1440 și aproximativ 500 pixeli. Măsurarea mobilă: client 489, scroll 489; fără depășire orizontală a paginii. Cronologia se derulează în propria zonă.
- 14 capturi PNG ale interfețelor fictive, din același renderer ca PDF-urile. Fotografii generate cu imagegen integrat; originale și prompturi păstrate în output/imagegen. Nu sunt folosite persoane reale sau fotografiile private ale centrului ca probe.

Platforma locală nu cere internet. Parola este verificată numai pe server; kitul local cu soluții rămâne la moderator. Resursele publicate sunt servite de Worker după autentificare; nu există un director static public. Secretele nu sunt incluse în arhive. Limitarea încercărilor este per instanță Worker, nu globală.

Nu a avut loc un pilot cu participanți. Ritmul de 90–100 minute este estimat; repetiția și verificarea fizică a sălii rămân necesare. Încheierea asistată permite finalul și discuția dacă grupul nu termină.

Rezultatele sunt în .qa/integrity-plic.json, .qa/browser-results.json și .qa/pdf/result.json. Verificarea publicării este consemnată separat în PUBLICARE.md.
