# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           minio-go
%define go_import_path  github.com/minio/minio-go/v6

Name:           go-github-minio-minio-go-v6
Version:        6.0.46
Release:        %autorelease
Summary:        MinIO Go client SDK for S3 compatible object storage
License:        Apache-2.0
URL:            https://github.com/minio/minio-go
#!RemoteAsset:  sha256:e855dae328eac30c4ec7523ab9a9b7affc6d8b1606a8885666c40f65db268290
Source0:        https://github.com/minio/minio-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# openRuyi test compatibility fix for the current Go toolchain.
Patch2000:      2000-fix-tests-for-current-go.patch

# Upstream uses testing.Short to skip tests requiring a live S3 endpoint.
BuildOption(check):  -short

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/minio/sha256-simd)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(gopkg.in/ini.v1)

Provides:       go(github.com/minio/minio-go/v6) = %{version}

Requires:       go(github.com/minio/sha256-simd)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(gopkg.in/ini.v1)

%description
Version 6 of the MinIO Go client SDK for Amazon S3 compatible object
storage. This package includes the client library and its public helpers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
