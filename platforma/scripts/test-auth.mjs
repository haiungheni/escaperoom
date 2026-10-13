import assert from 'node:assert/strict';
import {webcrypto,randomBytes,pbkdf2Sync} from 'node:crypto';
if(!globalThis.crypto)Object.defineProperty(globalThis,'crypto',{value:webcrypto});
const {default:worker}=await import('../dist/server/index.js');
const password=randomBytes(18).toString('base64url'),salt=randomBytes(24).toString('hex');
const env={PASSWORD_SALT:salt,PASSWORD_HASH:pbkdf2Sync(password,salt,100000,32,'sha256').toString('hex'),SESSION_KEY:randomBytes(32).toString('hex')};
let passed=0;function check(condition){assert.ok(condition);passed++}
const request=(url,init={})=>new Request('https://moderator.example'+url,init);
let r=await worker.fetch(request('/'),env);check(r.status===200&&(await r.text()).includes('Parola de acces'));
for(const file of ['/app.js','/data.js','/pdf/00-ghid-pas-cu-pas.pdf','/pdf/00-ghid-pas-cu-pas.pdf','/kit-offline.zip','/materiale-printabile.zip','/assets/plic/fotografii-caz.jpg']){r=await worker.fetch(request(file),env);check(r.status===401)}
r=await worker.fetch(request('/login',{method:'POST',headers:{Origin:'https://attacker.example'},body:'password='+password}),env);check(r.status===403);
r=await worker.fetch(request('/login',{method:'POST',headers:{Origin:'https://moderator.example'},body:'password=parola-gresita'}),env);check(r.status===401);
r=await worker.fetch(request('/login',{method:'POST',headers:{Origin:'https://moderator.example'},body:'password='+password}),env);check(r.status===303);
const cookie=r.headers.get('Set-Cookie');check(cookie.includes('HttpOnly')&&cookie.includes('Secure')&&cookie.includes('SameSite=Strict'));
const auth=cookie.split(';')[0];r=await worker.fetch(request('/index.html',{headers:{Cookie:auth}}),env);check(r.status===200&&(await r.text()).includes('PANOU MODERATOR'));
r=await worker.fetch(request('/pdf/00-ghid-pas-cu-pas.pdf',{headers:{Cookie:auth}}),env);check(r.status===200&&r.headers.get('Content-Type')==='application/pdf');check(new Uint8Array(await r.arrayBuffer()).slice(0,4).every((b,i)=>b==='%PDF'.charCodeAt(i)));
r=await worker.fetch(request('/kit-offline.zip',{headers:{Cookie:auth}}),env);check(r.status===200&&r.headers.get('Content-Disposition').includes('attachment'));await r.arrayBuffer();
r=await worker.fetch(request('/data.js',{headers:{Cookie:auth+'x'}}),env);check(r.status===401);
r=await worker.fetch(request('/data.js',{headers:{Cookie:auth}}),{...env,SESSION_KEY:'rotated'});check(r.status===401);
r=await worker.fetch(request('/data.js',{headers:{Cookie:auth}}),{...env,PASSWORD_HASH:'0'.repeat(64)});check(r.status===401);
r=await worker.fetch(request('/logout',{method:'POST',headers:{Origin:'https://moderator.example',Cookie:auth}}),env);check(r.status===303&&r.headers.get('Set-Cookie').includes('Max-Age=0'));
r=await worker.fetch(request('/'),{});check(r.status===503);
for(let i=0;i<6;i++)await worker.fetch(request('/login',{method:'POST',headers:{Origin:'https://moderator.example','CF-Connecting-IP':'test-limits'},body:'password=gresita-nevalida'}),env);
r=await worker.fetch(request('/login',{method:'POST',headers:{Origin:'https://moderator.example','CF-Connecting-IP':'test-limits'},body:'password='+password}),env);check(r.status===429);
const shortEnv={...env,PASSWORD_HASH:pbkdf2Sync('1111',salt,100000,32,'sha256').toString('hex')};
r=await worker.fetch(request('/login',{method:'POST',headers:{Origin:'https://moderator.example'},body:'password=1111'}),shortEnv);check(r.status===303);
r=await worker.fetch(request('/login',{method:'POST',headers:{Origin:'https://moderator.example'},body:'password=111'}),shortEnv);check(r.status===401);
console.log(JSON.stringify({passed,errors:[]}));
