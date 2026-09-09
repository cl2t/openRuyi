#!/usr/bin/env python3
"""Preserve package notices and metadata for the locked frontend build inputs."""
from pathlib import Path
import argparse,hashlib,json,re,shutil,zipfile
p=argparse.ArgumentParser();p.add_argument('destination',type=Path);p.add_argument('roots',nargs='+',type=Path);p.add_argument('--inter-license',type=Path,required=True);p.add_argument('--cache',type=Path,required=True);p.add_argument('--once-license',type=Path,required=True);a=p.parse_args();dest=a.destination;dest.mkdir(parents=True,exist_ok=True);records={}
allowed=set()
for archive in a.cache.glob('*.zip'):
 with zipfile.ZipFile(archive) as z:
  candidates=[n for n in z.namelist() if n.endswith('/package.json')]
  if not candidates:continue
  j=json.loads(z.read(min(candidates,key=lambda x:len(x.split('/')))))
  allowed.add(str(j.get('name'))+'@'+str(j.get('version')))
for root in a.roots:
 for meta in root.rglob('package.json'):
  if '.yarn/' in str(meta):continue
  try:j=json.loads(meta.read_text())
  except (ValueError,UnicodeError):continue
  name=j.get('name');version=j.get('version')
  if not isinstance(name,str) or not isinstance(version,str):continue
  key=name+'@'+version
  if key not in allowed:continue
  folder=dest/re.sub(r'[^A-Za-z0-9_.@+-]','_',key)
  candidates=[x for x in meta.parent.iterdir() if x.is_file() and any(x.name.lower().startswith(n) for n in ['license','licence','copying','notice','copyright'])]
  if not candidates:
   candidates=[x for x in meta.parent.iterdir() if x.is_file() and x.name.lower() in ['readme','readme.md','readme.txt']]
  folder.mkdir(exist_ok=True);files=[]
  for f in candidates:
   target=folder/f.name
   if target.exists() and target.read_bytes()!=f.read_bytes():target=folder/(hashlib.sha256(f.read_bytes()).hexdigest()[:12]+'-'+f.name)
   shutil.copyfile(f,target);files.append(str(target.relative_to(dest)))
  entry=records.setdefault(key,{'name':name,'version':version,'license':j.get('license',j.get('licenses')),'repository':j.get('repository'),'notices':[]})
  entry['notices']=sorted(set(entry['notices'])|set(files))
key='@tootallnate/once@1.1.2'
if key in records and not records[key]['notices']:
 folder=dest/re.sub(r'[^A-Za-z0-9_.@+-]','_',key)
 shutil.copyfile(a.once_license,folder/'LICENSE')
 records[key]['notices']=[str((folder/'LICENSE').relative_to(dest))]
 records[key]['notice_source']='https://github.com/TooTallNate/once/blob/de4a704b54936d83c8d6347d28665fe3b66c6de6/LICENSE'
shutil.copyfile(a.inter_license,dest/'Inter-3.19-OFL.txt')
(dest/'INDEX.json').write_text(json.dumps(sorted(records.values(),key=lambda x:(x['name'],x['version'])),indent=2)+'\n')
print('Preserved notices for',len(records),'package identities;',sum(bool(x['notices']) for x in records.values()),'have notice/readme files',flush=True)
