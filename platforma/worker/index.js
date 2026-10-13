/* Online gate. Every case asset and download is served only after authentication. */
/* EMBED_ASSETS */
const enc=new TextEncoder(),COOKIE='__Host-moderator',TTL=8*60*60;
const attempts=new Map();
const headers={ 'Cache-Control':'private, no-store','Vary':'Cookie','X-Content-Type-Options':'nosniff','Referrer-Policy':'same-origin','Content-Security-Policy':"default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; base-uri 'self'; form-action 'self'; frame-ancestors 'self' https://chatgpt.com https://*.chatgpt.com" };
const response=(body,status=200,extra={})=>new Response(body,{status,headers:{...headers,...extra}});
const hex=bytes=>Array.from(new Uint8Array(bytes),x=>x.toString(16).padStart(2,'0')).join('');
const fromHex=s=>Uint8Array.from(s.match(/../g)||[],x=>parseInt(x,16));
function equal(a,b){if(a.length!==b.length)return false;let d=0;for(let i=0;i<a.length;i++)d|=a.charCodeAt(i)^b.charCodeAt(i);return d===0}
async function key(env){return crypto.subtle.importKey('raw',enc.encode(env.SESSION_KEY),{name:'HMAC',hash:'SHA-256'},false,['sign','verify'])}
async function authenticated(req,env){try{const value=(req.headers.get('Cookie')||'').match(/(?:^|;\s*)__Host-moderator=([^;]+)/)?.[1];if(!value||value.length>512)return false;const parts=value.split('.');if(parts.length!==2||!/^[a-f0-9]{64}$/.test(parts[1]))return false;const [exp,version,nonce]=parts[0].split(':');const now=Math.floor(Date.now()/1000);if(!nonce||!/^[a-f0-9]{32}$/.test(nonce)||Number(exp)<=now||Number(exp)>now+TTL||version!==env.PASSWORD_HASH.slice(0,24))return false;return await crypto.subtle.verify('HMAC',await key(env),fromHex(parts[1]),enc.encode(parts[0]))}catch{return false}}
async function verifyPassword(password,env){const k=await crypto.subtle.importKey('raw',enc.encode(password),'PBKDF2',false,['deriveBits']);const bits=await crypto.subtle.deriveBits({name:'PBKDF2',hash:'SHA-256',salt:enc.encode(env.PASSWORD_SALT),iterations:100000},k,256);return equal(hex(bits),env.PASSWORD_HASH)}
const login=message=>`<!doctype html><html lang="ro"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Plicul dispărut · Acces moderator</title><style>:root{color-scheme:light;font-family:'Segoe UI',Arial,sans-serif}*{box-sizing:border-box}body{margin:0;background:#f7f5ff;color:#251747;min-height:100vh;display:grid;place-items:center;padding:24px}main{width:min(440px,100%);border:1px solid #e1dbf0;border-top:4px solid #6e37e8;border-radius:24px;padding:36px;background:white}.tag{font-size:10px;letter-spacing:2px;color:#865bbf}h1{font:800 39px/1.1 Trebuchet MS,Arial,sans-serif;margin:24px 0}p{font-size:13px;line-height:1.8;color:#685d7b}label{font-size:12px;display:block;margin-top:25px}input{width:100%;background:#faf8ff;border:1px solid #d5c5ef;border-radius:13px;padding:13px;color:#251747;margin:9px 0 18px;font:16px 'Segoe UI',sans-serif}button{width:100%;background:#6e37e8;color:white;border:0;border-radius:13px;padding:13px;font-weight:650;cursor:pointer}.error{color:#a94e40}.foot{font-size:10px;letter-spacing:1px;border-top:1px solid #e1dbf0;margin-top:28px;padding-top:18px}</style><main><span class="tag">PLICUL DISPĂRUT · MODERATOR</span><h1>Plicul dispărut.</h1><p>Pregătește materialele și condu jocul offline.<br>Introdu parola pentru a deschide panoul.</p>${message?`<p class="error" role="alert">${message}</p>`:''}<form action="/login" method="post"><label for="password">Parola de acces</label><input id="password" name="password" type="password" autocomplete="current-password" required maxlength="128" autofocus><button>Deschide panoul →</button></form><p class="foot">3 ECHIPE · O SINGURĂ SALĂ · CAZ FICTIV</p></main></html>`;
async function serve(path,req){const asset=ASSETS[path];if(!asset)return response('Pagina nu există.',404);const binary=atob(asset.b64),bytes=new Uint8Array(binary.length);for(let i=0;i<binary.length;i++)bytes[i]=binary.charCodeAt(i);const stream=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));return response(req.method==='HEAD'?null:stream,200,{'Content-Type':asset.type,...(path.endsWith('.zip')?{'Content-Disposition':`attachment; filename="${path.slice(1)}"`}:{})})}
export default {async fetch(req,env){
 const url=new URL(req.url),path=url.pathname;
 if(!env.PASSWORD_HASH||!env.PASSWORD_SALT||!env.SESSION_KEY)return response('Accesul moderatorului este în curs de configurare.',503,{'Content-Type':'text/plain; charset=utf-8'});
 if(path==='/login'&&req.method==='POST'){
  if(req.headers.get('Origin')!==url.origin)return response('Cerere refuzată.',403);
  if(Number(req.headers.get('Content-Length')||0)>2048)return response('Cerere prea mare.',413);
  const ip=req.headers.get('CF-Connecting-IP')||'unknown',now=Date.now();let entry=attempts.get(ip);if(!entry||now-entry.start>900000){entry={start:now,count:0};attempts.set(ip,entry)}
  if(entry.count>=6)return response(login('Prea multe încercări. Reîncearcă după 15 minute.'),429,{'Content-Type':'text/html; charset=utf-8','Retry-After':'900'});
  let text;try{text=await req.text()}catch{return response('Cerere invalidă.',400)}if(text.length>2048)return response('Cerere prea mare.',413);
  const pw=new URLSearchParams(text).get('password')||'';entry.count++;
  if(pw.length<4||pw.length>128||!await verifyPassword(pw,env))return response(login('Parola nu este corectă.'),401,{'Content-Type':'text/html; charset=utf-8'});
  attempts.delete(ip);if(attempts.size>2000)attempts.clear();
  const token=`${Math.floor(Date.now()/1000)+TTL}:${env.PASSWORD_HASH.slice(0,24)}:${hex(crypto.getRandomValues(new Uint8Array(16)))}`;
  const sig=hex(await crypto.subtle.sign('HMAC',await key(env),enc.encode(token)));
  return response(null,303,{Location:'/', 'Set-Cookie':`${COOKIE}=${token}.${sig}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=${TTL}`});
 }
 if(path==='/logout'&&req.method==='POST'){if(req.headers.get('Origin')!==url.origin)return response('Cerere refuzată.',403);return response(null,303,{Location:'/', 'Set-Cookie':`${COOKIE}=; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=0`})}
 if(!['GET','HEAD'].includes(req.method))return response('Metodă neacceptată.',405,{'Allow':'GET, HEAD'});
 if(!await authenticated(req,env)){if(path==='/'||path==='/index.html')return response(req.method==='HEAD'?null:login(''),200,{'Content-Type':'text/html; charset=utf-8'});return response('Introdu parola în pagina principală.',401,{'Content-Type':'text/plain; charset=utf-8'})}
 return serve(path==='/'?'/index.html':path,req);
}};
