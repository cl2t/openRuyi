# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           plan9stats
%define go_import_path  github.com/lufia/plan9stats
%define commit_id       8bc96cf8fc35265ba2a17997e3f3e52f69259370

Name:           go-github-lufia-plan9stats
Version:        0+git20260907.8bc96cf
Release:        %autorelease
Summary:        Plan 9 statistics helpers for Go
License:        BSD-3-Clause
URL:            https://github.com/lufia/plan9stats
#!RemoteAsset:  sha256:7f21456a399a094ec2c33554ae36f6e9d456c7bf3080f3eaa913a39a27621dbb
Source0:        https://github.com/lufia/plan9stats/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(github.com/lufia/plan9stats) = %{version}

%description
plan9stats reads Plan 9-style statistics used by gopsutil to report
CPU information on Linux.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
