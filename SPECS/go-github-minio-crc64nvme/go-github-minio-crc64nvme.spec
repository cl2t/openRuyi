# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           crc64nvme
%define go_import_path  github.com/minio/crc64nvme

Name:           go-github-minio-crc64nvme
Version:        1.0.1
Release:        %autorelease
Summary:        CRC64 checksums using the NVMe polynomial
License:        Apache-2.0
URL:            https://github.com/minio/crc64nvme
#!RemoteAsset:  sha256:41e2093b4ea48b0315e97df7568b70c7547e33b92aca1d5bd93a2f2de70c5d43
Source0:        https://github.com/minio/crc64nvme/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/cpuid/v2)

Provides:       go(github.com/minio/crc64nvme) = %{version}

Requires:       go(github.com/klauspost/cpuid/v2)

%description
crc64nvme calculates CRC64 checksums with the NVMe polynomial. It uses
carryless-multiplication SIMD on amd64 and arm64, with a portable
fallback on other architectures.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
