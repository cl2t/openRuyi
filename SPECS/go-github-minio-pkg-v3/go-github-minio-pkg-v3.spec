# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pkg
%define go_import_path  github.com/minio/pkg/v3
# certs notify tests and LDAP checks need a live watcher/server.
%define go_test_ignore_failure 1

Name:           go-github-minio-pkg-v3
Version:        3.1.3
Release:        %autorelease
Summary:        Shared MinIO helper libraries for Go
License:        AGPL-3.0-only
URL:            https://github.com/minio/pkg
#!RemoteAsset:  sha256:cebd58674c85b381b6ffa6c789117925ce3a6f0b4e6e8f5fdc7a0fd9dbce002c
Source0:        https://github.com/minio/pkg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cheggaaa/pb)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/fatih/structs)
BuildRequires:  go(github.com/go-ldap/ldap/v3)
BuildRequires:  go(github.com/lestrrat-go/jwx/v2)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/minio/minio-go/v7)
BuildRequires:  go(github.com/minio/mux)
BuildRequires:  go(github.com/philhofer/fwd)
BuildRequires:  go(github.com/rjeczalik/notify)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/minio/pkg/v3) = %{version}

Requires:       go(github.com/cheggaaa/pb)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/fatih/structs)
Requires:       go(github.com/go-ldap/ldap/v3)
Requires:       go(github.com/lestrrat-go/jwx/v2)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/minio/minio-go/v7)
Requires:       go(github.com/minio/mux)
Requires:       go(github.com/philhofer/fwd)
Requires:       go(github.com/rjeczalik/notify)
Requires:       go(github.com/tinylib/msgp)
Requires:       go(go.etcd.io/etcd/client/v3)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)
Requires:       go(gopkg.in/yaml.v3)

%description
pkg/v3 is MinIO's shared Go helper module, covering certificates, policy,
LDAP, environment, networking, and optional etcd-backed configuration.

%prep -a
# mimedb/util is a table generator, not imported by the library.
rm -rf mimedb/util

%check -p
# Compile every test package before tolerating sandbox runtime failures.
(
%{go_common}
mkdir -p %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
%__go test %{go_test_flags_default} -run '^$' ./...
)

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
