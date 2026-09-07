# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wmi
%define go_import_path  github.com/yusufpapurcu/wmi
# Linux/riscv compile no Windows-tagged packages, so go test ./...
# reports "no packages to test" and exits non-zero.
%define go_test_ignore_failure 1

Name:           go-github-yusufpapurcu-wmi
Version:        1.2.4
Release:        %autorelease
Summary:        WQL interface for Windows WMI
License:        MIT
URL:            https://github.com/yusufpapurcu/wmi
#!RemoteAsset:  sha256:c7bb668db5dffd97ade4076acd361d21912525d22fd5608c8689191f4b7d5e26
Source0:        https://github.com/yusufpapurcu/wmi/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/yusufpapurcu/wmi) = %{version}

%description
Package wmi provides a WQL interface to Windows WMI. The implementation
is Windows-only; other GOOS values compile to empty source via build
tags. go-ole is not a BuildRequires because openruyi's go-ole package
is currently failed on riscv64, and Linux/riscv builds do not compile
the Windows sources.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
