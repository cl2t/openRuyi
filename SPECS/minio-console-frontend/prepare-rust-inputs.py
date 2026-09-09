#!/usr/bin/env python3
"""Prepare checksum-verified Cargo source inputs without requiring Cargo locally."""
import argparse,concurrent.futures,gzip,hashlib,json,tarfile,tomllib,urllib.request
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('destination',type=Path);a=p.parse_args();root=a.destination.resolve();root.mkdir(parents=True,exist_ok=True)
if any(root.iterdir()):raise SystemExit('Destination must be empty')
pins={'4.46.1':'b6d05a33fd4dc7380a49ded28c51e16cd8933a8ec879a8745acda07db0e2cb4c','4.27.3':'8d7e0a2687d53b7756e7daa8302379eef7687e6da688e60c3402354d8254ddf8'};crates={}
for version,expected in pins.items():
 url=f'https://github.com/rollup/rollup/archive/refs/tags/v{version}.tar.gz';archive=root/f'rollup-{version}.tar.gz'
 with urllib.request.urlopen(url,timeout=120) as response:archive.write_bytes(response.read())
 assert hashlib.sha256(archive.read_bytes()).hexdigest()==expected
 with tarfile.open(archive) as t:t.extractall(root,filter='data')
 for item in tomllib.loads((root/f'rollup-{version}/rust/Cargo.lock').read_text())['package']:
  if 'source' not in item:continue
  assert item['source']=='registry+https://github.com/rust-lang/crates.io-index'
  key=(item['name'],item['version']);assert key not in crates or crates[key]['checksum']==item['checksum'];crates[key]=item
vendor=root/'vendor';vendor.mkdir();cache=root/'crates';cache.mkdir()
def fetch(item):
 name=item['name']+'-'+item['version'];url=f'https://static.crates.io/crates/{item["name"]}/{name}.crate';archive=cache/(name+'.crate')
 with urllib.request.urlopen(url,timeout=120) as response:archive.write_bytes(response.read())
 assert hashlib.sha256(archive.read_bytes()).hexdigest()==item['checksum'],name
 with tarfile.open(archive) as t:t.extractall(vendor,filter='data')
 files={str(f.relative_to(vendor/name)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((vendor/name).rglob('*')) if f.is_file() and f.name!='.cargo-checksum.json'}
 (vendor/name/'.cargo-checksum.json').write_text(json.dumps({'files':files,'package':item['checksum']},sort_keys=True)+'\n')
 return {'name':item['name'],'version':item['version'],'url':url,'sha256':item['checksum']}
with concurrent.futures.ThreadPoolExecutor(8) as ex:records=list(ex.map(fetch,[crates[k] for k in sorted(crates)]))
(root/'crate-sources.json').write_text(json.dumps(records,indent=2)+'\n')
with (root/'rollup-cargo-sources.tar.gz').open('wb') as raw:
 with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=6) as zipped:
  with tarfile.open(fileobj=zipped,mode='w') as t:
   for f in [vendor,*sorted(vendor.rglob('*'))]:
    info=t.gettarinfo(str(f),arcname=str(f.relative_to(root)));info.uid=info.gid=0;info.uname=info.gname='';info.mtime=0;info.mode=0o755 if f.is_dir() else 0o644
    if f.is_file():
     with f.open('rb') as stream:t.addfile(info,stream)
    else:t.addfile(info)
print('VERIFIED',len(records),'locked source crates',flush=True)
print('Archive SHA256:',hashlib.sha256((root/'rollup-cargo-sources.tar.gz').read_bytes()).hexdigest(),flush=True)
