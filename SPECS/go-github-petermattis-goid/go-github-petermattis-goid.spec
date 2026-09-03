# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goid
%define go_import_path  github.com/petermattis/goid
%define commit_id       a731cc31b4fe99408872ab3e587b5972f29ff929

Name:           go-github-petermattis-goid
Version:        0+git20260621.a731cc3
Release:        %autorelease
Summary:        Programmatically retrieve the current goroutine's ID
License:        Apache-2.0
URL:            https://github.com/petermattis/goid
#!RemoteAsset:  sha256:d2c9714a2b765eb0615ea675b1141401eafda0eec36338773636cebcd5a9877a
Source0:        https://github.com/petermattis/goid/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/petermattis/goid) = %{version}

%description
goid exposes the current goroutine ID, used for online deadlock detection.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
