# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-termwiz
%global full_version 0.1.0
%global pkgname ratatui-termwiz-0.1

Name:           rust-ratatui-termwiz-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "ratatui-termwiz"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:0f76fe0bd0ed4295f0321b1676732e2454024c15a35d01904ddb315afd3d545c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ratatui-core-0.1/default) >= 0.1.0
Requires:       crate(termwiz-0.23/default) >= 0.23.3
Provides:       crate(ratatui-termwiz) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "ratatui-termwiz"

%package     -n %{name}+document-features
Summary:        Termwiz backend for the Ratatui Terminal UI library - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust ratatui-termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scrolling-regions
Summary:        Termwiz backend for the Ratatui Terminal UI library - feature "scrolling-regions"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/scrolling-regions) >= 0.1.0
Provides:       crate(%{pkgname}/scrolling-regions)

%description -n %{name}+scrolling-regions
This metapackage enables feature "scrolling-regions" for the Rust ratatui-termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Termwiz backend for the Ratatui Terminal UI library - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(termwiz-0.23/use-serde) >= 0.23.3
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ratatui-termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+underline-color
Summary:        Termwiz backend for the Ratatui Terminal UI library - feature "underline-color"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/underline-color) >= 0.1.0
Provides:       crate(%{pkgname}/underline-color)

%description -n %{name}+underline-color
This metapackage enables feature "underline-color" for the Rust ratatui-termwiz crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
