# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cli
%define go_import_path  github.com/minio/cli

Name:           go-github-minio-cli
Version:        1.24.2
Release:        %autorelease
Summary:        MinIO fork of urfave/cli for command-line Go apps
License:        MIT
URL:            https://github.com/minio/cli
#!RemoteAsset:  sha256:36b99dfd7463bf6c08e1ff86243916da9c90f535eeed094194efd14e7580e4f0
Source0:        https://github.com/minio/cli/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/minio/cli) = %{version}

%description
cli is MinIO's fork of urfave/cli. It is a small framework for building
command-line Go applications, used by the MinIO server.

%prep -a
# altsrc still imports gopkg.in/urfave/cli.v1 from the pre-fork library
# and is unused by MinIO, which only imports github.com/minio/cli.
# generate-flag-types and runtests are codegen/test helpers.
rm -rf altsrc generate-flag-types runtests

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
