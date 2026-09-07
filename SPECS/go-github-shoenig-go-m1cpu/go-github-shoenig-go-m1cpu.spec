# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-m1cpu
%define go_import_path  github.com/shoenig/go-m1cpu
# Tests need Apple IOKit via CGO and cannot run on Linux or riscv64.
%define go_test_ignore_failure 1

Name:           go-github-shoenig-go-m1cpu
Version:        0.1.6
Release:        %autorelease
Summary:        Inspect Apple Silicon CPU frequency from Go
License:        MPL-2.0
URL:            https://github.com/shoenig/go-m1cpu
#!RemoteAsset:  sha256:80a4292edf006308f82222b842195c785fbdc7fddaee09698b403c13612590ed
Source0:        https://github.com/shoenig/go-m1cpu/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/shoenig/test)

Provides:       go(github.com/shoenig/go-m1cpu) = %{version}

%description
go-m1cpu reports performance and efficiency core frequencies for Apple
Silicon CPUs. The implementation uses IOKit through CGO and is Darwin
ARM64 only.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
