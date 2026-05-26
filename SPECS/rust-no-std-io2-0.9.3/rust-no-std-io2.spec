# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name no_std_io2
%global full_version 0.9.3
%global pkgname no-std-io2-0.9.3

Name:           rust-no-std-io2-0.9.3
Version:        0.9.3
Release:        %autorelease
Summary:        Rust crate "no_std_io2"
License:        Apache-2.0 OR MIT
URL:            https://github.com/wcampbell0x2a/no-std-io2
#!RemoteAsset:  sha256:b51ed7824b6e07d354605f4abb3d9d300350701299da96642ee084f5ce631550
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0) >= 2.8.0
Provides:       crate(no-std-io2) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)

%description
Alloc support is optional.
Source code for takopackized Rust crate "no_std_io2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
