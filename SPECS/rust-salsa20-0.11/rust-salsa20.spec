# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name salsa20
%global full_version 0.11.0
%global pkgname salsa20-0.11

Name:           rust-salsa20-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "salsa20"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/stream-ciphers
#!RemoteAsset:  sha256:2f874456e72520ff1375a06c588eaf074b0f01f9e9e1aada45bd9b7954a6e42c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(cipher-0.5/default) >= 0.5.1
Requires:       crate(cipher-0.5/stream-wrapper) >= 0.5.1
Provides:       crate(salsa20) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "salsa20"

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the Salsa20 stream cipher - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(cipher-0.5/stream-wrapper) >= 0.5.1
Requires:       crate(cipher-0.5/zeroize) >= 0.5.1
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust salsa20 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
