# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           multi-profile
%define go_import_path  github.com/bygui86/multi-profile/v2

Name:           go-github-bygui86-multi-profile-v2
Version:        2.1.0
Release:        %autorelease
Summary:        Start several Go runtime/pprof profiles at once
License:        Apache-2.0
URL:            https://github.com/bygui86/multi-profile
#!RemoteAsset:  sha256:fc5a1cdd1a770af292c1fe14f88e7512e64d92017978193e78a89c03ea5fd2e0
Source0:        https://github.com/bygui86/multi-profile/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/bygui86/multi-profile/v2) = %{version}

%description
multi-profile starts several runtime/pprof profiles in one process.
MinIO dperf uses the v2 module for optional CPU and memory profiles.

%prep -a
# examples/ are nested sample programs, not the library.
rm -rf examples

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
