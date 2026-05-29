# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-sdk-go
%define go_import_path  github.com/aws/aws-sdk-go

# Run the upstream test suite but do not let it fail the build: the v1 SDK is a
# large deprecated module whose tests assume network/credentials and a full
# dependency graph not present in an isolated distro build (matches
# go-github-aws-smithy-go's handling).
%define go_test_ignore_failure 1

Name:           go-github-aws-aws-sdk-go
Version:        1.55.8
Release:        %autorelease
Summary:        AWS SDK for the Go programming language (v1)
License:        Apache-2.0 AND MIT
URL:            https://github.com/aws/aws-sdk-go
#!RemoteAsset:  sha256:b862bc662d38bcb1cff65d47c65e82ddb6294debf7272a3f9107aee2c5134ce1
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go >= 1.19
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/jmespath/go-jmespath)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/jmespath/go-jmespath)

%description
The AWS SDK for Go (v1) provides Go APIs for using Amazon Web Services.
Note: upstream deprecated v1 in favor of aws-sdk-go-v2; this package is
kept only because some consumers still pull it in as an indirect
dependency.

%prep -a
# Drop upstream-local replace directives; dependencies come from system RPMs.
sed -i '/^replace /d' go.mod

%files
%license LICENSE.txt NOTICE.txt
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
