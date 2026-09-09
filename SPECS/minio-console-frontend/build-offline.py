#!/usr/bin/env python3
"""Offline MDS -> Console build and verification, independent of Go backends."""
import argparse, hashlib, http.server, json, os, shutil, subprocess, threading, urllib.request
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('console',type=Path);p.add_argument('mds',type=Path);p.add_argument('inputs',type=Path);p.add_argument('--native-dir',type=Path,required=True);p.add_argument('--check',action='store_true');a=p.parse_args()
c=a.console.resolve()/'web-app';m=a.mds.resolve();i=a.inputs.resolve()
env={**os.environ,'YARN_ENABLE_NETWORK':'0','YARN_ENABLE_TELEMETRY':'0','YARN_ENABLE_SCRIPTS':'0','YARN_ENABLE_GLOBAL_CACHE':'0','YARN_CHECKSUM_BEHAVIOR':'throw','CI':'true','NODE_OPTIONS':'--max-old-space-size=4096'}
def run(root,version,*args):
 subprocess.run(['node',str(i/f'yarn-{version}.cjs'),*args],cwd=root,env=env,check=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if not a.check:
 subprocess.run(['node','--version'],check=True)
 for root,name,v in [(m,'mds','4.6.0'),(c,'console','4.9.4')]:
  cache=root/'.yarn/cache';cache.mkdir(parents=True,exist_ok=True)
  for fn in json.loads((i/(name+'-cache.json')).read_text()):shutil.copyfile(i/'cache'/fn,cache/fn)
  for f in ['.yarnrc.yml','package.json','yarn.lock','jest.config.js','rollup.config.mjs']:
   src=i/name/f
   if src.exists():
    if f == '.yarnrc.yml':shutil.copyfile(src,root/f)
    else:assert (root/f).read_bytes() == src.read_bytes(), 'Patched metadata differs: '+str(root/f)
  run(root,v,'install','--immutable','--immutable-cache','--mode=skip-build')
 for d in [m,c]:
  existing=list((d/'node_modules').rglob('*.node'))
  assert not existing, 'Unexpected cached native payload: '+str(existing)
  for meta in (d/'node_modules').rglob('rollup/package.json'):
   v=json.loads(meta.read_text()).get('version')
   if v not in ['4.46.1','4.27.3']:continue
   arch=subprocess.check_output(['node','-p','process.arch'],text=True).strip()
   src=a.native_dir/f'rollup-{v}.node';assert src.read_bytes().startswith(b'\x7fELF')
   shutil.copyfile(src,meta.parent/'dist'/f'rollup.linux-{arch}-gnu.node')
   print('Installed source-built native parser',v,arch,flush=True)
 shutil.rmtree(m/'dist',ignore_errors=True)
 run(m,'4.6.0','build')
 target=c/'node_modules/mds/dist';shutil.rmtree(target);shutil.copytree(m/'dist',target)
 for f in (m/'dist').rglob('*'):
  if f.is_file():assert sha(f)==sha(target/f.relative_to(m/'dist'))
 shutil.rmtree(c/'build')
 run(c,'4.9.4','build')
else:
 run(m,'4.6.0','test','--runInBand')
 build=c/'build';manifest=json.loads((build/'asset-manifest.json').read_text())
 assets=set(manifest['files'].values())|set(manifest['entrypoints'])|{'index.html'}
 class Handler(http.server.SimpleHTTPRequestHandler):
  def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(build),**kwargs)
  def log_message(self,*args):pass
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler)
 thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
 try:
  for item in sorted(assets):
   name=item.removeprefix('./').lstrip('/');path=build/name
   assert path.is_file(),name
   with urllib.request.urlopen(f'http://127.0.0.1:{server.server_port}/{name}') as r:
    assert r.status==200 and r.read()==path.read_bytes(),name
  html=(build/'index.html').read_text();assert 'id="root"' in html
  assert any(x.endswith('.js') for x in assets) and any(x.endswith('.css') for x in assets)
 finally:server.shutdown();server.server_close()
 report={'node':subprocess.check_output(['node','--version'],text=True).strip(),'http_assets_passed':len(assets),'files':{str(f.relative_to(build)):sha(f) for f in sorted(build.rglob('*')) if f.is_file()}}
 (build/'BUILD-VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n')
 print('OFFLINE FRONTEND CHECK PASSED:',len(assets),'HTTP assets; 4 upstream MDS tests',flush=True)
