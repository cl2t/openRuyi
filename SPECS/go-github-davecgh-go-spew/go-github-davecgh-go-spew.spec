# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-spew
%define go_import_path  github.com/davecgh/go-spew
%define commit_id       d8f796af33cc11cb798c1aaeb27a4ebc5099927d

Name:           go-github-davecgh-go-spew
Version:        1.1.2+git20260721.d8f796a
Release:        %autorelease
Summary:        Implements a deep pretty printer for Go data structures to aid in debugging
License:        ISC
URL:            https://github.com/davecgh/go-spew
#!RemoteAsset:  sha256:2869025129b95a0037050f837956b5469ec8f0d54037be8dc25dfa733e73fcd0
Source0:        https://github.com/davecgh/go-spew/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/davecgh/go-spew) = %{version}

%description
Go-spew implements a deep pretty printer for Go data structures to aid in
debugging.

A comprehensive suite of tests with 100% test coverage is provided
to ensure proper functionality.  See test_coverage.txt for the
gocov coverage report. Go-spew is licensed under the liberal ISC
license, so it may be used in open source or commercial projects.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
