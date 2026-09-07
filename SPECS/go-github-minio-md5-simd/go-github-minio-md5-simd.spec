# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           md5-simd
%define go_import_path  github.com/minio/md5-simd

Name:           go-github-minio-md5-simd
Version:        1.1.2
Release:        %autorelease
Summary:        SIMD-accelerated parallel MD5 hashing for Go
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/minio/md5-simd
#!RemoteAsset:  sha256:60a01d2023a0c44434ac7d9d18cfcb5538fdaf8413227465935926a683939683
Source0:        https://github.com/minio/md5-simd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/cpuid/v2)

Provides:       go(github.com/minio/md5-simd) = %{version}

Requires:       go(github.com/klauspost/cpuid/v2)

%description
md5-simd computes multiple independent MD5 digests in parallel on a
single CPU core using AVX2 or AVX512, with a portable crypto/md5
fallback when those instructions are unavailable.

%prep -a
# avo-based assembly generator; not part of the importable library.
rm -rf _gen

%files
%doc README.md
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
