# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name signal-hook-tokio
%global full_version 0.4.0
%global pkgname signal-hook-tokio-0.4

Name:           rust-signal-hook-tokio-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "signal-hook-tokio"
License:        MIT OR Apache-2.0
URL:            https://github.com/vorner/signal-hook
#!RemoteAsset:  sha256:e513e435a8898a0002270f29d0a708b7879708fb5c4d00e46983ca2d2d378cf0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(signal-hook-0.4/default) >= 0.4.4
Requires:       crate(tokio-1.52.3/default) >= 1.52.3
Requires:       crate(tokio-1.52.3/net) >= 1.52.3
Provides:       crate(signal-hook-tokio) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "signal-hook-tokio"

%package     -n %{name}+futures-core-0-3
Summary:        Tokio support for signal-hook - feature "futures-core-0_3" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(futures-core-0.3/default) >= 0.3.32
Provides:       crate(%{pkgname}/futures-core-0-3)
Provides:       crate(%{pkgname}/futures-v0-3)

%description -n %{name}+futures-core-0-3
This metapackage enables feature "futures-core-0_3" for the Rust signal-hook-tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "futures-v0_3" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
