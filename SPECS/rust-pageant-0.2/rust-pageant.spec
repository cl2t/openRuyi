# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pageant
%global full_version 0.2.0
%global pkgname pageant-0.2

Name:           rust-pageant-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "pageant"
License:        Apache-2.0
URL:            https://github.com/warp-tech/russh
#!RemoteAsset:  sha256:1b537f975f6d8dcf48db368d7ec209d583b015713b5df0f5d92d2631e4ff5595
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1.0/default) >= 1.5.0
Requires:       crate(bytes-1.0/default) >= 1.11.1
Requires:       crate(delegate-0.13/default) >= 0.13.5
Requires:       crate(futures-0.3/default) >= 0.3.32
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(rand-0.8/default) >= 0.8.6
Requires:       crate(thiserror-1.0/default) >= 1.0.69
Requires:       crate(tokio-1.52.3/default) >= 1.52.3
Requires:       crate(windows-0.62/default) >= 0.62.2
Requires:       crate(windows-0.62/win32-security) >= 0.62.2
Provides:       crate(pageant) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "pageant"

%package     -n %{name}+default
Summary:        Pageant SSH agent transport client - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/namedpipes)
Requires:       crate(%{pkgname}/wmmessage)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust pageant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+namedpipes
Summary:        Pageant SSH agent transport client - feature "namedpipes"
Requires:       crate(%{pkgname})
Requires:       crate(sha2-0.10/default) >= 0.10.9
Requires:       crate(sha2-0.10/oid) >= 0.10.9
Requires:       crate(tokio-1.52.3/net) >= 1.52.3
Requires:       crate(tokio-1.52.3/time) >= 1.52.3
Requires:       crate(windows-0.62/win32-security) >= 0.62.2
Requires:       crate(windows-0.62/win32-security-authentication-identity) >= 0.62.2
Requires:       crate(windows-0.62/win32-security-cryptography) >= 0.62.2
Requires:       crate(windows-strings-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}/namedpipes)

%description -n %{name}+namedpipes
This metapackage enables feature "namedpipes" for the Rust pageant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wmmessage
Summary:        Pageant SSH agent transport client - feature "wmmessage"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.52.3/io-util) >= 1.52.3
Requires:       crate(tokio-1.52.3/rt) >= 1.52.3
Requires:       crate(windows-0.62/win32-security) >= 0.62.2
Requires:       crate(windows-0.62/win32-system-dataexchange) >= 0.62.2
Requires:       crate(windows-0.62/win32-system-memory) >= 0.62.2
Requires:       crate(windows-0.62/win32-system-threading) >= 0.62.2
Requires:       crate(windows-0.62/win32-ui-windowsandmessaging) >= 0.62.2
Provides:       crate(%{pkgname}/wmmessage)

%description -n %{name}+wmmessage
This metapackage enables feature "wmmessage" for the Rust pageant crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
