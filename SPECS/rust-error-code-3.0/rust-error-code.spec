# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name error-code
%global full_version 3.3.2
%global pkgname error-code-3.0

Name:           rust-error-code-3.0
Version:        3.3.2
Release:        %autorelease
Summary:        Rust crate "error-code"
License:        BSL-1.0
URL:            https://github.com/DoumanAsh/error-code
#!RemoteAsset:  sha256:dea2df4cf52843e0452895c455a1a2cfbb842a1e7329671acf418fdc53ed4c59
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(error-code) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "error-code"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
