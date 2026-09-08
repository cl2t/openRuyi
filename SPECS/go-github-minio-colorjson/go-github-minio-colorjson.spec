# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           colorjson
%define go_import_path  github.com/minio/colorjson

Name:           go-github-minio-colorjson
Version:        1.0.8
Release:        %autorelease
Summary:        Colorized JSON encoding and decoding for Go
License:        BSD-3-Clause
URL:            https://github.com/minio/colorjson
#!RemoteAsset:  sha256:7049d52abbce912a043860cc3b635495c27134b8c4b35feb4181366e02325f0e
Source0:        https://github.com/minio/colorjson/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/minio/pkg/v3)

Provides:       go(github.com/minio/colorjson) = %{version}

Requires:       go(github.com/fatih/color)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/minio/pkg/v3)

%description
colorjson is a fork of encoding/json with colorized terminal output.
There is no LICENSE file; the Go files are BSD-3-Clause (The Go Authors).

%files
%doc README.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
