# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name imgref
%global full_version 1.12.1
%global pkgname imgref-1.0

Name:           rust-imgref-1.0
Version:        1.12.1
Release:        %autorelease
Summary:        Rust crate "imgref"
License:        CC0-1.0 OR Apache-2.0
URL:            https://lib.rs/crates/imgref
#!RemoteAsset:  sha256:40fac9d56ed6437b198fddba683305e8e2d651aa42647f00f5ae542e7f5c94a2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(imgref) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/deprecated)

%description
Source code for takopackized Rust crate "imgref"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
