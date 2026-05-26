# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wezterm-color-types
%global full_version 0.3.0
%global pkgname wezterm-color-types-0.3

Name:           rust-wezterm-color-types-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "wezterm-color-types"
License:        MIT
URL:            https://github.com/wez/wezterm
#!RemoteAsset:  sha256:7de81ef35c9010270d63772bebef2f2d6d1f2d20a983d27505ac850b8c4b4296
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(csscolorparser-0.6/default) >= 0.6.2
Requires:       crate(csscolorparser-0.6/lab) >= 0.6.2
Requires:       crate(deltae-0.3/default) >= 0.3.2
Requires:       crate(lazy-static-1.0/default) >= 1.5.0
Requires:       crate(wezterm-dynamic-0.2/default) >= 0.2.1
Provides:       crate(wezterm-color-types) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wezterm-color-types"

%package     -n %{name}+serde
Summary:        Types for working with colors - feature "serde" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Provides:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/use-serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wezterm-color-types crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_serde" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
