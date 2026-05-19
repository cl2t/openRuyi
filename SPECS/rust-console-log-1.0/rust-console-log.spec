# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name console_log
%global full_version 1.0.0
%global pkgname console-log-1.0

Name:           rust-console-log-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "console_log"
License:        MIT/Apache-2.0
URL:            https://github.com/iamcodemaker/console_log
#!RemoteAsset:  sha256:be8aed40e4edbf4d3b4431ab260b63fdc40f5780a4766824329ea0f1eefe3c0f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(web-sys-0.3/console) >= 0.3.82
Requires:       crate(web-sys-0.3/default) >= 0.3.82
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "console_log"

%package     -n %{name}+wasm-bindgen
Summary:        Logging facility that routes Rust log messages to the browser's console - feature "wasm-bindgen" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/color)
Provides:       crate(%{pkgname}/wasm-bindgen)

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust console_log crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "color" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
