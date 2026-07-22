# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           smithy-go
%define go_import_path  github.com/aws/smithy-go
# TODO: Test need too much dependencies, add it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-aws-smithy-go
Version:        1.27.2
Release:        %autorelease
Summary:        Smithy code generators for Go (in development)
License:        Apache-2.0
URL:            https://github.com/aws/smithy-go
#!RemoteAsset:  sha256:b3ea155006f03a08edc63260c3f276250132b38e14569ade334f1137baa8f2f3
Source0:        https://github.com/aws/smithy-go/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aws/smithy-go) = %{version}

%description
Smithy code generators for Go and the accompanying smithy-go runtime.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
