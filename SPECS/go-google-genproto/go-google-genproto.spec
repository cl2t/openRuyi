# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# NOTICE:
# DO NOT TRY TO UPGRADE THIS UNLESS YOU ARE VERY FAMILIAR WITH
# THIS IS YOUR FINAL WARNING. - 251

%define _name           genproto
%define go_import_path  google.golang.org/genproto
# Upstream does not provide git tags, use commit IDs instead - 251
%define commit_root     e7812ac95cc0c7174fe2fc2914ed037d4bd20613
%define commit_api      62b3387ff3248b60d6b1dc98dd529731cd340bc6
%define commit_rpc      7ab31c22f7ad9c3f3011c6343d32a8b4cb72d6e1
%define version_root    0+git20260107.e7812ac
%define version_api     0+git20260722.62b3387
%define version_rpc     0+git20260722.7ab31c2
%define dir_root        go-genproto-%{commit_root}
%define dir_api         go-genproto-%{commit_api}
%define dir_rpc         go-genproto-%{commit_rpc}

Name:           go-google-genproto
Version:        %{version_api}
Release:        %autorelease
Summary:        Generated code for Google Cloud client libraries
License:        Apache-2.0
URL:            https://github.com/googleapis/go-genproto
# Updating the root snapshot would pull in the full Google Cloud client module
# set through compatibility aliases. Keep the existing root and update only the
# independently versioned API and RPC submodules.
#!RemoteAsset:  sha256:ee9bdfda880edd9348440dd2ec43a1cf9cf4e0b70b06f0cdd1ec7aa8515f1358
Source0:        https://github.com/googleapis/go-genproto/archive/%{commit_root}.tar.gz#/%{_name}-%{version_root}.tar.gz
#!RemoteAsset:  sha256:b8cb81babaacd368cbb8f5be5dc984e736e129c704bf5ee5663063e3bfc9eb77
Source1:        https://github.com/googleapis/go-genproto/archive/%{commit_api}.tar.gz#/%{_name}-api-%{version_api}.tar.gz
#!RemoteAsset:  sha256:123f1b77bece75fbda73bfabfbf3645277f4e32ea06f89e233f719a1a7672da9
Source2:        https://github.com/googleapis/go-genproto/archive/%{commit_rpc}.tar.gz#/%{_name}-rpc-%{version_rpc}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)

Provides:       go(google.golang.org/genproto) = %{version_root}
Provides:       go(google.golang.org/genproto/googleapis/api) = %{version_api}

Requires:       %{name}-googleapis-rpc = %{version}-%{release}
Requires:       go(github.com/golang/protobuf)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This repository contains the generated Go packages for common protocol
buffer types, and the generated gRPC (http://grpc.io) code necessary for
interacting with Google's gRPC APIs.

# Circular dependency with google.golang.org/grpc - 251
%package        googleapis-rpc
Summary:        Common Google APIs RPC protos

Provides:       go(google.golang.org/genproto/googleapis/rpc) = %{version_rpc}
Requires:       go(google.golang.org/protobuf)

%description    googleapis-rpc
This subpackage contains the generated code for common Google APIs RPC
protos.

%prep
%setup -q -c -T -a 0
%setup -q -D -T -a 1
%setup -q -D -T -a 2
rm -rf %{dir_root}/googleapis/api %{dir_root}/googleapis/rpc
cp -a %{dir_api}/googleapis/api %{dir_root}/googleapis/api
cp -a %{dir_rpc}/googleapis/rpc %{dir_root}/googleapis/rpc

%install
install -d %{buildroot}%{go_sys_gopath}/$(dirname %{go_import_path})
cp -a %{dir_root} %{buildroot}%{go_sys_gopath}/%{go_import_path}

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
install -d %{_builddir}/go/src/$(dirname %{go_import_path})
cp -a %{dir_root} %{_builddir}/go/src/%{go_import_path}
pushd %{_builddir}/go/src/%{go_import_path}
_packages=()
while read -r _package; do
    case "${_package}" in
        google.golang.org/genproto/googleapis*|google.golang.org/genproto/firestore/bundle)
            ;;
        *)
            _packages+=("${_package}")
            ;;
    esac
done < <(go list -e -f '{{.ImportPath}}' ./...)
go test -v "${_packages[@]}"
popd

%files
%doc %{dir_root}/README*
%license %{dir_root}/LICENSE*
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/googleapis/rpc

%files googleapis-rpc
%{go_sys_gopath}/%{go_import_path}/googleapis/rpc

%changelog
%autochangelog
