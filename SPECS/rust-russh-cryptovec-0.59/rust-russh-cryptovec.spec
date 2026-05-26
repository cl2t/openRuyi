# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name russh-cryptovec
%global full_version 0.59.0
%global pkgname russh-cryptovec-0.59

Name:           rust-russh-cryptovec-0.59
Version:        0.59.0
Release:        %autorelease
Summary:        Rust crate "russh-cryptovec"
License:        Apache-2.0
URL:            https://github.com/warp-tech/russh
#!RemoteAsset:  sha256:36140e8a20297bc2e8338807c3d9ca911f7fa49d7539cbcd6d48d3befd70efd8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(nix-0.31/default) >= 0.31.2
Requires:       crate(nix-0.31/mman) >= 0.31.2
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-memory) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-systeminformation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.2
Provides:       crate(russh-cryptovec) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "russh-cryptovec"

%package     -n %{name}+ssh-encoding
Summary:        Vector which zeroes its memory on clears and reallocations - feature "ssh-encoding"
Requires:       crate(%{pkgname})
Requires:       crate(ssh-encoding-0.2/bytes) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/ssh-encoding)

%description -n %{name}+ssh-encoding
This metapackage enables feature "ssh-encoding" for the Rust russh-cryptovec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
