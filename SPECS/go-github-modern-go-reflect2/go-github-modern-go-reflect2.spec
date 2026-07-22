# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           reflect2
%define go_import_path  github.com/modern-go/reflect2
%define commit_id       35a7c28c31ee079903db043180532306a621943a

Name:           go-github-modern-go-reflect2
Version:        1.0.3+git20260721.35a7c28
Release:        %autorelease
Summary:        reflect api without runtime reflect.Value cost
License:        Apache-2.0
URL:            https://github.com/modern-go/reflect2
#!RemoteAsset:  sha256:1b42046c89d2eaeb433e38eef74654faf9f05487ab2ea5661dd039a60cf2883f
Source0:        https://github.com/modern-go/reflect2/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/modern-go/reflect2) = %{version}

%description
This package provides reflect api that avoids runtime reflect.Value cost

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
