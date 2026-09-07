# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jwx
%define go_import_path  github.com/lestrrat-go/jwx/v2

Name:           go-github-lestrrat-go-jwx-v2
Version:        2.1.4
Release:        %autorelease
Summary:        JOSE JWT, JWS, JWE and JWK toolkit for Go
License:        MIT
URL:            https://github.com/lestrrat-go/jwx
#!RemoteAsset:  sha256:11f1f629bb4c05651ec90b75ddbed77fca53a76a6c34e0bf158aca44475c6781
Source0:        https://github.com/lestrrat-go/jwx/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/decred/dcrd/dcrec/secp256k1/v4)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/lestrrat-go/blackmagic)
BuildRequires:  go(github.com/lestrrat-go/httprc)
BuildRequires:  go(github.com/lestrrat-go/iter)
BuildRequires:  go(github.com/lestrrat-go/option)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/lestrrat-go/jwx/v2) = %{version}

Requires:       go(github.com/decred/dcrd/dcrec/secp256k1/v4)
Requires:       go(github.com/goccy/go-json)
Requires:       go(github.com/lestrrat-go/blackmagic)
Requires:       go(github.com/lestrrat-go/httprc)
Requires:       go(github.com/lestrrat-go/iter)
Requires:       go(github.com/lestrrat-go/option)
Requires:       go(github.com/segmentio/asm)
Requires:       go(golang.org/x/crypto)

%description
jwx/v2 implements JOSE technologies for Go, including JWT, JWS, JWE,
JWK and JWA. MinIO pkg/v3 uses it to verify license and environment
tokens.

%prep -a
# tools/cmd and cmd are code generators needing unpackaged
# lestrrat-go/codegen, lestrrat-go/xstrings and goccy/go-yaml.
# examples are sample programs, not the library.
rm -rf cmd examples tools

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
