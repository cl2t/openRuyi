# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name onig_sys
%global full_version 69.9.3
%global pkgname onig-sys-69.0

Name:           rust-onig-sys-69.0
Version:        69.9.3
Release:        %autorelease
Summary:        Rust crate "onig_sys"
License:        MIT
URL:            https://github.com/rust-onig/rust-onig
#!RemoteAsset:  sha256:1e68317604e77e53b85896388e1a803c1d21b74c899ec9e5e1112db90735edd7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.62
Requires:       crate(pkg-config-0.3/default) >= 0.3.33
Provides:       crate(onig-sys) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/posix-api)
Provides:       crate(%{pkgname}/print-debug)

%description
This crate exposes a set of unsafe functions which can then be used by other crates to create safe wrappers around Oniguruma.
You probably don't want to link to this crate directly; instead check out the `onig` crate.
Source code for takopackized Rust crate "onig_sys"

%package     -n %{name}+bindgen
Summary:        `onig_sys` crate contains raw rust bindings to the oniguruma library - feature "bindgen" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(bindgen-0.72/default) >= 0.72.0
Requires:       crate(bindgen-0.72/runtime) >= 0.72.0
Provides:       crate(%{pkgname}/bindgen)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/generate)

%description -n %{name}+bindgen
This crate exposes a set of unsafe functions which can then be used by other crates to create safe wrappers around Oniguruma.
You probably don't want to link to this crate directly; instead check out the `onig` crate.
This metapackage enables feature "bindgen" for the Rust onig_sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "generate" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
