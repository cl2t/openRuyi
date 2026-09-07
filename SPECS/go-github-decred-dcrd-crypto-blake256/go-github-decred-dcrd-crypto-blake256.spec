# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           blake256
%define go_import_path  github.com/decred/dcrd/crypto/blake256
%define upstream_tag    crypto/blake256/v%{version}

Name:           go-github-decred-dcrd-crypto-blake256
Version:        1.1.0
Release:        %autorelease
Summary:        BLAKE-256 hash for Go from the Decred dcrd tree
License:        ISC
URL:            https://github.com/decred/dcrd
#!RemoteAsset:  sha256:60529155655e1053bdc479ddcf422412ee2f45f5620171445ab5044a1128112d
Source0:        https://github.com/decred/dcrd/archive/refs/tags/%{upstream_tag}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/decred/dcrd/crypto/blake256) = %{version}

%description
blake256 is the nested dcrd module that implements the BLAKE-256 hash.
It is required by dcrec/secp256k1/v4.

%prep -a
# Nested module github.com/decred/dcrd/crypto/blake256.
# Keep the repository LICENSE; the nested module directory may not ship one.
find . -maxdepth 1 -mindepth 1 -not -name crypto -not -name LICENSE -not -name '_build' -exec rm -rf {} +
find ./crypto -mindepth 1 -maxdepth 1 -not -name blake256 -exec rm -rf {} +
shopt -s dotglob && mv crypto/blake256/* . && rmdir crypto/blake256 crypto

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
