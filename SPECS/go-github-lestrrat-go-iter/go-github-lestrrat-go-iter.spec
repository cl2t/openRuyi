# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           iter
%define go_import_path  github.com/lestrrat-go/iter

Name:           go-github-lestrrat-go-iter
Version:        1.0.2
Release:        %autorelease
Summary:        Channel-based map and array iterators for Go
License:        MIT
URL:            https://github.com/lestrrat-go/iter
#!RemoteAsset:  sha256:7f9469449fb1f267f7284ca3e8da7b957153dd1963bf5b6def4a71aec1da0770
Source0:        https://github.com/lestrrat-go/iter/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/lestrrat-go/iter) = %{version}

%description
iter provides channel-based helpers to iterate map-like and array-like
objects, including conversion to native maps and slices.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
