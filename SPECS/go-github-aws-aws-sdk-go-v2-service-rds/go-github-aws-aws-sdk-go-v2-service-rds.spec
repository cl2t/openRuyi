# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-sdk-go-v2-service-rds
%define go_import_path  github.com/aws/aws-sdk-go-v2/service/rds
%define archive_dir     aws-sdk-go-v2-service-rds-v1.118.2

# This module is one Go module carved out of the aws-sdk-go-v2 monorepo. Its
# upstream test suite assumes the full monorepo checkout (sibling modules and
# cross-module internal/ test helpers), which is not reproducible when each
# module is built in isolation as a distro package. Run the tests but do not
# let unreproducible test setups fail the build (matches go-github-aws-smithy-go).
%define go_test_ignore_failure 1

Name:           go-github-aws-aws-sdk-go-v2-service-rds
Version:        1.118.2
Release:        %autorelease
Summary:        Amazon RDS service client for AWS SDK for Go v2
License:        Apache-2.0
URL:            https://github.com/aws/aws-sdk-go-v2
#!RemoteAsset:  sha256:2b3567a561c71e9a9a1b7ac45ded1bb383689623ea02e36f18a0e255b8ce6628
Source0:        %{url}/archive/refs/tags/service/rds/v1.118.2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{archive_dir}

BuildRequires:  go >= 1.24
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/configsources)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
BuildRequires:  go(github.com/aws/smithy-go)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/configsources)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
Requires:       go(github.com/aws/smithy-go)

%description
This package provides the Amazon Relational Database Service client for
AWS SDK for Go v2.

%prep -a
# AWS SDK for Go v2 is a monorepo; keep only the current submodule's source.
rm -rf ../module-root
mkdir ../module-root
cp -a service/rds/. ../module-root/
cp -a LICENSE.txt NOTICE.txt README.md ../module-root/ 2>/dev/null || :
find . -mindepth 1 -maxdepth 1 -exec rm -rf {} +
cp -a ../module-root/. .
rm -rf ../module-root
# Drop upstream monorepo-local replace directives; deps come from system RPMs.
sed -i '/^replace /d' go.mod

%files
%license LICENSE* NOTICE.txt
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
