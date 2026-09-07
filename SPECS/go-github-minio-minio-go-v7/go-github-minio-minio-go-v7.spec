# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           minio-go
%define go_import_path  github.com/minio/minio-go/v7

Name:           go-github-minio-minio-go-v7
Version:        7.0.91
Release:        %autorelease
Summary:        MinIO Go client SDK for Amazon S3 compatible object storage
License:        Apache-2.0
URL:            https://github.com/minio/minio-go
#!RemoteAsset:  sha256:39453d5b3a625932c5b93f31f5428ea3d9e888ed7d5ef7b0a0e5c22a49c4f581
Source0:        https://github.com/minio/minio-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/go-ini/ini)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/minio/crc64nvme)
BuildRequires:  go(github.com/minio/md5-simd)
BuildRequires:  go(github.com/rs/xid)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/minio/minio-go/v7) = %{version}

Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/go-ini/ini)
Requires:       go(github.com/goccy/go-json)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/minio/crc64nvme)
Requires:       go(github.com/minio/md5-simd)
Requires:       go(github.com/rs/xid)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)

%description
The MinIO Go Client SDK provides APIs to access Amazon S3 compatible
object storage, including bucket and object operations, presigned URLs,
and credential helpers.

%prep -a
# Sample programs; they are not imported by the library and pull extra
# dependencies (minio/sio, cheggaaa/pb) not needed for the SDK itself.
rm -rf examples

%files
%doc README.md
%license LICENSE NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
