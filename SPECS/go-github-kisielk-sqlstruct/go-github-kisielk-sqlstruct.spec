# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sqlstruct
%define go_import_path  github.com/kisielk/sqlstruct
%global commit_id d2980d3f12719c2d057b09e16d36f984e5a094a2

Name:           go-github-kisielk-sqlstruct
Version:        0+git20260918.d2980d3
Release:        %autorelease
Summary:        SQL row scanning helpers for Go
License:        MIT
URL:            https://github.com/kisielk/sqlstruct
#!RemoteAsset:  sha256:128e40e9e3b8c2cf18a77948f536691e69408c7e88b4c093fff36328e7381ad9
Source0:        https://github.com/kisielk/sqlstruct/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kisielk/sqlstruct) = %{version}

%description
Sqlstruct maps SQL query result columns to Go struct fields, simplifying
row scanning with the database/sql package.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
