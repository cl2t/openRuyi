# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha3
%global full_version 0.11.0
%global pkgname sha3-0.11

Name:           rust-sha3-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "sha3"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:be176f1a57ce4e3d31c1a166222d9768de5954f811601fb7ca06fc8203905ce1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.11/default) >= 0.11.3
Requires:       crate(keccak-0.2/default) >= 0.2.0
Provides:       crate(sha3) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "sha3"

%package     -n %{name}+alloc
Summary:        The SHA-3 family of cryptographic hash algorithms - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/alloc) >= 0.11.3
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        The SHA-3 family of cryptographic hash algorithms - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/oid)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        The SHA-3 family of cryptographic hash algorithms - feature "oid"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/oid) >= 0.11.3
Provides:       crate(%{pkgname}/oid)

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        The SHA-3 family of cryptographic hash algorithms - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/zeroize) >= 0.11.3
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
