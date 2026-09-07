# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sio-go
%define go_import_path  github.com/secure-io/sio-go

Name:           go-github-secure-io-sio-go
Version:        0.3.1
Release:        %autorelease
Summary:        Authenticated encryption for continuous byte streams
License:        MIT
URL:            https://github.com/secure-io/sio-go
#!RemoteAsset:  sha256:12728c554fcfab43b59539e508597883d7d865f152f205f7dfe8d5b5534b5e63
Source0:        https://github.com/secure-io/sio-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/secure-io/sio-go) = %{version}

Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
sio-go implements authenticated encryption for continuous byte streams
by splitting data into fragments and sealing each fragment with an
AEAD.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
