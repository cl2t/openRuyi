#!/usr/bin/env python3
"""Fetch pinned inputs in a new directory; the RPM build itself is offline."""
import argparse, gzip, hashlib, json, os, shutil, subprocess, tarfile, urllib.request
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('destination',type=Path);p.add_argument('--spec-dir',type=Path,required=True);a=p.parse_args();d=a.destination.resolve();spec=a.spec_dir.resolve();d.mkdir(parents=True,exist_ok=True)
if any(d.iterdir()):raise SystemExit('Destination must be empty')
here=Path(__file__).resolve().parent;manifest=json.loads((here/'input-manifest.json').read_text())
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
for item in manifest['downloads']:
 f=d/item['file']
 with urllib.request.urlopen(item['url'],timeout=120) as response:f.write_bytes(response.read())
 assert sha(f)==item['sha256'],item['file']
 if f.suffix=='.gz':
  with tarfile.open(f) as archive:archive.extractall(d,filter='data')
m=d/'mds-400914d72cb3ffa27d600e0ae1f17ece2182ec22';c=d/'object-browser-2017f33b26e1cb632dd208ab7d91add1d06990fd/web-app';inputs=d/'offline-inputs';pool=inputs/'cache';pool.mkdir(parents=True)
env={**os.environ,'YARN_ENABLE_TELEMETRY':'0','YARN_ENABLE_SCRIPTS':'0','YARN_ENABLE_GLOBAL_CACHE':'0','YARN_ENABLE_MIRROR':'0','YARN_GLOBAL_FOLDER':str(d/'yarn-global'),'YARN_CHECKSUM_BEHAVIOR':'throw','YARN_NPM_REGISTRY_SERVER':'https://registry.npmjs.org','GIT_CONFIG_COUNT':'1','GIT_CONFIG_KEY_0':'url.https://github.com/bexsoft/mds.git.insteadOf','GIT_CONFIG_VALUE_0':'https://github.com/minio/mds.git'}
# Yarn 4.9.4 passes Git's '-c key=value' as one argument. Normalize only
# this spelling; pin/repository selection and all other arguments are unchanged.
real_git=shutil.which('git');shim=d/'tool-shims';shim.mkdir()
(shim/'git').write_text('#!/usr/bin/env python3\nimport os,sys\nargs=[]\nfor arg in sys.argv[1:]:\n args.extend(["-c",arg[3:]] if arg.startswith("-c ") else [arg])\nos.execv('+repr(real_git)+', ['+repr(real_git)+']+args)\n')
(shim/'git').chmod(0o755);env['PATH']=str(shim)+os.pathsep+env['PATH']
for root,label,version,patch in [(m,'mds','4.6.0','2000-mds-build-tools.patch'),(c,'console','4.9.4','2001-console-build-tools.patch')]:
 subprocess.run(['git','apply',str(spec/patch)],cwd=root,check=True)
 (root/'.yarnrc.yml').write_text(manifest['yarnrc'])
 subprocess.run(['node',str(d/f'yarn-{version}.cjs'),'install','--immutable','--mode=skip-build'],cwd=root,env=env,check=True)
 out=inputs/label;out.mkdir()
 for file in manifest['metadata'][label]:shutil.copyfile(root/file,out/file)
 expected=manifest['caches'][label]
 # Disabling Yarn's shared mirror changes filenames, not ZIP contents.
 archives={f.name.rsplit('-',1)[0]:f for f in (root/'.yarn/cache').glob('*.zip')}
 assert set(archives)=={name.rsplit('-',1)[0] for name in expected},label+' cache identities differ'
 for name in sorted(expected):
  src=archives[name.rsplit('-',1)[0]]
  assert sha(src)==expected[name],name+' checksum differs'
  f=pool/name
  if f.exists():assert sha(f)==expected[name]
  else:shutil.copyfile(src,f)
 (inputs/(label+'-cache.json')).write_text(json.dumps(sorted(expected),indent=2)+'\n')
 shutil.copyfile(d/f'yarn-{version}.cjs',inputs/f'yarn-{version}.cjs')
# Normalize archive metadata and gzip headers for reproducible source bundles.
with (d/'frontend-offline-inputs.tar.gz').open('wb') as raw:
 with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=6) as zipped:
  with tarfile.open(fileobj=zipped,mode='w') as archive:
   for file in [inputs,*sorted(inputs.rglob('*'))]:
    info=archive.gettarinfo(str(file),arcname=str(file.relative_to(d)));info.uid=info.gid=0;info.uname=info.gname='';info.mtime=0;info.mode=0o755 if file.is_dir() else 0o644
    if file.is_file():
     with file.open('rb') as stream:archive.addfile(info,stream)
    else:archive.addfile(info)
print('REPRODUCED',len(list(pool.glob('*.zip'))),'checksum-identical cache inputs',flush=True)
print('Archive SHA256:',sha(d/'frontend-offline-inputs.tar.gz'),flush=True)
