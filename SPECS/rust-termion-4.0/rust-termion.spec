# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name termion
%global full_version 4.0.6
%global pkgname termion-4.0

Name:           rust-termion-4.0
Version:        4.0.6
Release:        %autorelease
Summary:        Rust crate "termion"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/termion
#!RemoteAsset:  sha256:f44138a9ae08f0f502f24104d82517ef4da7330c35acd638f1f29d3cd5475ecb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(numtoa-0.2/default) >= 0.2.4
Provides:       crate(termion) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "termion"

%package     -n %{name}+serde
Summary:        Bindless library for manipulating terminals - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust termion crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
