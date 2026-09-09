# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define console_commit 2017f33b26e1cb632dd208ab7d91add1d06990fd
%define mds_commit 400914d72cb3ffa27d600e0ae1f17ece2182ec22

Name:           minio-console-frontend
Version:        0+git20260909.2017f33
Release:        %autorelease
Summary:        Static frontend assets for the pinned MinIO Console
License:        AGPL-3.0-or-later AND MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND OFL-1.1 AND 0BSD
URL:            https://github.com/miniohq/object-browser
VCS:            git:https://github.com/miniohq/object-browser
#!RemoteAsset:  sha256:7b76868a00deb4d4fa88fd4d32afd79ebc6f70d4520ad09ed207f25f5276b045
Source0:        https://github.com/miniohq/object-browser/archive/%{console_commit}.tar.gz#/console.tar.gz
# Exact locked MDS commit, retained in the original author's archive.
# Its Yarn archive checksum equals the original Console lockfile checksum.
#!RemoteAsset:  sha256:22339c8de0b3908edbea3c52c7a77d5d2448f0e4c491631e42c5ebf3df7afb17
Source1:        https://github.com/bexsoft/mds/archive/%{mds_commit}.tar.gz#/mds-400914d.tar.gz
# Locally reproducible source inputs; a maintained release URL is still needed.
Source2:        frontend-offline-inputs.tar.gz
Source3:        build-offline.py
Source4:        collect-notices.py
Source5:        Inter-OFL.txt
# Missing in once 1.1.2; upstream added this notice in commit de4a704.
Source6:        once-upstream-LICENSE
#!RemoteAsset:  sha256:b6d05a33fd4dc7380a49ded28c51e16cd8933a8ec879a8745acda07db0e2cb4c
Source7:        https://github.com/rollup/rollup/archive/refs/tags/v4.46.1.tar.gz#/rollup-4.46.1.tar.gz
#!RemoteAsset:  sha256:8d7e0a2687d53b7756e7daa8302379eef7687e6da688e60c3402354d8254ddf8
Source8:        https://github.com/rollup/rollup/archive/refs/tags/v4.27.3.tar.gz#/rollup-4.27.3.tar.gz
# Source crates verified against both upstream Cargo.lock files.
Source9:        rollup-cargo-sources.tar.gz
BuildArch:      noarch

# Local changes: preserve production dependencies and all upstream assertions.
Patch2000:      2000-mds-build-tools.patch
# Local change: omit unused audit, generator and browser-E2E development tools.
Patch2001:      2001-console-build-tools.patch

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  nodejs
BuildRequires:  python3
BuildRequires:  patch
BuildRequires:  tar
BuildRequires:  gzip

%description
Static HTML, JavaScript, CSS and fonts for the Console revision pinned by
MinIO RELEASE.2025-10-15T17-29-55Z. Build MDS and Console offline, using native
Rollup parsers compiled from locked Rust sources with distribution tools.
The assets can be copied into Console's web-app/build before its Go build.
This package does not provide a standalone Console backend or HTTP service.

%prep
%setup -q -n object-browser-%{console_commit}
for source in %{SOURCE1} %{SOURCE2} %{SOURCE7} %{SOURCE8} %{SOURCE9}; do
    tar -xf "$source" -C ..
done
patch -d ../mds-%{mds_commit} -p1 < %{PATCH2000}
patch -d web-app -p1 < %{PATCH2001}

%build
export CARGO_NET_OFFLINE=true
export CARGO_BUILD_JOBS=4
# mimalloc 1.7.9 uses C11 atomics removed from GCC's default C23 dialect.
export CFLAGS="${CFLAGS:-} -std=gnu11"
source_root="$(pwd)/.."
mkdir -p ../native-tools
for version in 4.46.1 4.27.3; do
    cd "$source_root/rollup-$version/rust"
    mkdir -p .cargo
    cat > .cargo/config.toml <<'CONFIG'
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "../../vendor"
CONFIG
    cargo build --locked --offline --release -p bindings_napi
    cp target/release/libbindings_napi.so "$source_root/native-tools/rollup-$version.node"
done
cd "$source_root/object-browser-%{console_commit}"
node -e 'for (const v of ["4.46.1", "4.27.3"]) { const p = require(process.argv[1] + "/rollup-" + v + ".node"); const ast = p.parse("export const answer = 42;", false, false); if (!Buffer.isBuffer(ast) || ast.length === 0) throw Error(v); console.log(v, "native parser passed", ast.length); }' "$source_root/native-tools"
python3 %{SOURCE3} . ../mds-%{mds_commit} ../offline-inputs --native-dir "$source_root/native-tools"

%install
python3 %{SOURCE4} notices web-app/node_modules ../mds-%{mds_commit}/node_modules --inter-license %{SOURCE5} --once-license %{SOURCE6} --cache ../offline-inputs/cache
cp LICENSE notices/Console-AGPL.txt
cp ../mds-%{mds_commit}/LICENSE notices/MDS-AGPL.txt
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a web-app/build/. %{buildroot}%{_datadir}/%{name}/
find %{buildroot}%{_datadir}/%{name} -type f -exec chmod 0644 {} +

%check
python3 %{SOURCE3} . ../mds-%{mds_commit} ../offline-inputs --native-dir "$(pwd)/../native-tools" --check
python3 - %{buildroot}%{_datadir}/%{name} <<'PY'
import hashlib, json, sys
from pathlib import Path
root = Path(sys.argv[1])
report = json.loads(Path('web-app/build/BUILD-VERIFICATION.json').read_text())
actual = {str(f.relative_to(root)): hashlib.sha256(f.read_bytes()).hexdigest() for f in root.rglob('*') if f.is_file()}
assert actual == report['files'], 'Installed frontend differs from tested build'
assert not list(root.rglob('*.node')), 'Build tool leaked into frontend output'
print('INSTALLED FRONTEND CHECK PASSED:', len(actual), 'files')
PY
install -D -m 0644 web-app/build/BUILD-VERIFICATION.json %{buildroot}%{_datadir}/%{name}-build-info/BUILD-VERIFICATION.json

%files
%license LICENSE notices
%{_datadir}/%{name}/
%{_datadir}/%{name}-build-info/

%changelog
%autochangelog
