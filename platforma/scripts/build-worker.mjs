import fs from 'node:fs/promises';
import path from 'node:path';
import {gzipSync} from 'node:zlib';
const root=path.resolve(import.meta.dirname,'..'),offline=path.join(root,'offline'),assets={};
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.pdf':'application/pdf','.zip':'application/zip'};
async function walk(dir){for(const entry of await fs.readdir(dir,{withFileTypes:true})){const file=path.join(dir,entry.name);if(entry.isDirectory())await walk(file);else if(types[path.extname(file)]&&entry.name!=='kit-offline.zip'){const bytes=await fs.readFile(file);assets['/'+path.relative(offline,file).replaceAll('\\','/')]={type:types[path.extname(file)],b64:gzipSync(bytes).toString('base64')}}}}
await walk(offline);
const zip=await fs.readFile(path.join(root,'kit-offline.zip'));assets['/kit-offline.zip']={type:'application/zip',b64:gzipSync(zip).toString('base64')};
const source=(await fs.readFile(path.join(root,'worker/index.js'),'utf8')).replace('/* EMBED_ASSETS */','const ASSETS='+JSON.stringify(assets)+';');
const out=path.join(root,'dist');await fs.mkdir(path.join(out,'server'),{recursive:true});await fs.mkdir(path.join(out,'.openai'),{recursive:true});
await fs.writeFile(path.join(out,'server/index.js'),source);await fs.copyFile(path.join(root,'.openai/hosting.json'),path.join(out,'.openai/hosting.json'));
console.log(JSON.stringify({assets:Object.keys(assets).length,worker_bytes:Buffer.byteLength(source),worker_gzip_bytes:gzipSync(source).length}));
