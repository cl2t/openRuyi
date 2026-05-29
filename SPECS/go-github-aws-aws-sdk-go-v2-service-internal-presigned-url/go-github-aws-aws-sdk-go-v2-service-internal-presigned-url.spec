# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-sdk-go-v2-service-internal-presigned-url
%define go_import_path  github.com/aws/aws-sdk-go-v2/service/internal/presigned-url
%define archive_dir     aws-sdk-go-v2-service-internal-presigned-url-v1.13.23

# This module is one Go module carved out of the aws-sdk-go-v2 monorepo. Its
# upstream test suite assumes the full monorepo checkout (sibling modules and
# cross-module internal/ test helpers), which is not reproducible when each
# module is built in isolation as a distro package. Run the tests but do not
# let unreproducible test setups fail the build (matches go-github-aws-smithy-go).
%define go_test_ignore_failure 1

Name:           go-github-aws-aws-sdk-go-v2-service-internal-presigned-url
Version:        1.13.23
Release:        %autorelease
Summary:        Internal presigned URL helpers for AWS SDK for Go v2
License:        Apache-2.0
URL:            https://github.com/aws/aws-sdk-go-v2
#!RemoteAsset:  sha256:28457cbd541228426c1b2f34e97f58cb79dd855af44227795ef5a2635851f9de
Source0:        %{url}/archive/refs/tags/service/internal/presigned-url/v1.13.23.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{archive_dir}

BuildRequires:  go >= 1.24
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/smithy-go)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/smithy-go)

%description
This package provides internal presigned URL helpers used by AWS SDK
for Go v2 service clients.

%prep -a
# AWS SDK for Go v2 is a monorepo; keep only the current submodule's source.
rm -rf ../module-root
mkdir ../module-root
cp -a service/internal/presigned-url/. ../module-root/
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
