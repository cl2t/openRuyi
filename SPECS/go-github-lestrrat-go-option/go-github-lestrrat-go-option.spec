# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           option
%define go_import_path  github.com/lestrrat-go/option

Name:           go-github-lestrrat-go-option
Version:        1.0.1
Release:        %autorelease
Summary:        Base type for the optional parameters pattern in Go
License:        MIT
URL:            https://github.com/lestrrat-go/option
#!RemoteAsset:  sha256:2cd876f51cb7b721b184a26950ed6624c5e287fdb41ddad473284339aa0ee2cc
Source0:        https://github.com/lestrrat-go/option/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/lestrrat-go/option) = %{version}

%description
option provides a reusable identifier-and-value tuple used to implement
variadic optional parameters without exported config structs.

%prep -a
# cmd/genoptions is a code generator and needs unpackaged
# lestrrat-go/codegen, lestrrat-go/xstrings and goccy/go-yaml.
rm -rf cmd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
