# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpcc
%define go_import_path  github.com/lestrrat-go/httpcc

Name:           go-github-lestrrat-go-httpcc
Version:        1.0.1
Release:        %autorelease
Summary:        HTTP/1.1 Cache-Control header parser for Go
License:        MIT
URL:            https://github.com/lestrrat-go/httpcc
#!RemoteAsset:  sha256:40740483a7ff2070dd7957be7513498d7e4a080bea2128159fc3f160803dae41
Source0:        https://github.com/lestrrat-go/httpcc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/lestrrat-go/httpcc) = %{version}

%description
httpcc parses HTTP/1.1 Cache-Control request and response headers into
typed directive accessors.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
