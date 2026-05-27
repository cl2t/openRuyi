# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-sdk-go-v2
%define go_import_path  github.com/aws/aws-sdk-go-v2

Name:           go-github-aws-aws-sdk-go-v2
Version:        1.41.7
Release:        %autorelease
Summary:        AWS SDK for the Go programming language
License:        Apache-2.0
URL:            https://github.com/aws/aws-sdk-go-v2
#!RemoteAsset:  sha256:de0a75e54664b89391de807726c8b0539b46e24a352e302cdbae5c80e6c5afd1
Source0:        https://github.com/aws/aws-sdk-go-v2/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go >= 1.24
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/smithy-go)

Provides:       go(github.com/aws/aws-sdk-go-v2) = %{version}

%description
The AWS SDK for Go v2 provides Go APIs for using Amazon Web Services.
It includes the core SDK runtime, AWS request and response types,
middleware, retry logic, endpoint utilities, and protocol helpers used by
service clients in the AWS SDK for Go v2 module family.

%prep -a
# The upstream repository is a monorepo. Keep the root Go module only.
find . -mindepth 2 -name go.mod -printf '%h\0' | sort -zr | xargs -0r rm -rf
find . -depth -type d -empty -delete

%files
%license LICENSE* NOTICE.txt
%doc README* CHANGELOG.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
