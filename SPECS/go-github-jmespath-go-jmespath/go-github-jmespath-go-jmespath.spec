# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-jmespath
%define go_import_path  github.com/jmespath/go-jmespath

Name:           go-github-jmespath-go-jmespath
Version:        0.4.0
Release:        %autorelease
Summary:        JMESPath implementation in Go
License:        Apache-2.0
URL:            https://github.com/jmespath/go-jmespath
#!RemoteAsset:  sha256:aa86d00b6836345eee196c13df2df084a18e0b1159935de9289f2ef6a7fe375d
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go >= 1.14
BuildRequires:  go-rpm-macros
# Test-only dependencies (pulled in by the bundled internal/testify helper).
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(%{go_import_path}) = %{version}

%description
go-jmespath is a Go implementation of JMESPath, a query language for
JSON. It is used by the AWS SDK for Go to declaratively extract elements
from JSON documents.

%prep -a
# Drop upstream-local replace directives; dependencies come from system RPMs.
sed -i '/^replace /d' go.mod

# Only run the JMESPath library's own tests. The bundled internal/testify
# tree is a vendored copy of testify used as a test helper; its self-tests
# (and the extra objx dependency they need) are not part of this package.
%global go_test_include github.com/jmespath/go-jmespath

%files
%license LICENSE
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
