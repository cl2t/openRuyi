# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ftp
%define go_import_path  github.com/jlaffaye/ftp
%define commit_id       c1312a7102bfa91477d0c16ce91dcfd3aa9e3f06

Name:           go-github-jlaffaye-ftp
Version:        0+git20260909.c1312a7
Release:        %autorelease
Summary:        Implements a FTP client as described in RFC 959
License:        ISC
URL:            https://github.com/jlaffaye/ftp
#!RemoteAsset:  sha256:64085a9304384a2d7b1881b27c794cd10cb3ab0d2f0d3a1de7a6802d326e9b71
Source0:        https://github.com/jlaffaye/ftp/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# openRuyi test compatibility fix for the current Go toolchain.
Patch2000:      2000-fix-file-size-test-format.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/jlaffaye/ftp) = %{version}

%description
FTP client library implementing file transfers, directory listings and
connection management according to RFC 959.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
