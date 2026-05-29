# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-sdk-go-v2-credentials
%define go_import_path  github.com/aws/aws-sdk-go-v2/credentials
%define archive_dir     aws-sdk-go-v2-credentials-v1.19.17

# This module is one Go module carved out of the aws-sdk-go-v2 monorepo. Its
# upstream test suite assumes the full monorepo checkout (sibling modules and
# cross-module internal/ test helpers), which is not reproducible when each
# module is built in isolation as a distro package. Run the tests but do not
# let unreproducible test setups fail the build (matches go-github-aws-smithy-go).
%define go_test_ignore_failure 1

Name:           go-github-aws-aws-sdk-go-v2-credentials
Version:        1.19.17
Release:        %autorelease
Summary:        Credential providers for AWS SDK for Go v2
License:        Apache-2.0
URL:            https://github.com/aws/aws-sdk-go-v2
#!RemoteAsset:  sha256:35167b70ca7acd5e6c3d0245840975601550b0cd9f8af3cdb43fb6dc902856c8
Source0:        %{url}/archive/refs/tags/credentials/v1.19.17.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{archive_dir}

BuildRequires:  go >= 1.24
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/configsources)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/v4a)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/signin)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sso)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sts)
BuildRequires:  go(github.com/aws/smithy-go)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/configsources)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/v4a)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/signin)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sso)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sts)
Requires:       go(github.com/aws/smithy-go)

%description
This package provides credential providers for AWS SDK for Go v2,
including shared file, environment, EC2 metadata, SSO, and STS-based
credential loading.

%prep -a
# AWS SDK for Go v2 is a monorepo; keep only the current submodule's source.
rm -rf ../module-root
mkdir ../module-root
cp -a credentials/. ../module-root/
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
