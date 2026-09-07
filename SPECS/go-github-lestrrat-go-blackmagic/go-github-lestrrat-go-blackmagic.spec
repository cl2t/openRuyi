# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           blackmagic
%define go_import_path  github.com/lestrrat-go/blackmagic

Name:           go-github-lestrrat-go-blackmagic
Version:        1.0.2
Release:        %autorelease
Summary:        Reflection helpers for assigning typed optional values
License:        MIT
URL:            https://github.com/lestrrat-go/blackmagic
#!RemoteAsset:  sha256:213493da84c672867385cc05dc4ebce3c4c16f5b0e376986dbddd3274a8bc686
Source0:        https://github.com/lestrrat-go/blackmagic/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/lestrrat-go/blackmagic) = %{version}

%description
blackmagic contains small reflect-based helpers used by lestrrat-go
libraries to assign optional field values.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
