# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name getopts
%global full_version 0.2.24
%global pkgname getopts-0.2

Name:           rust-getopts-0.2
Version:        0.2.24
Release:        %autorelease
Summary:        Rust crate "getopts"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/getopts
#!RemoteAsset:  sha256:cfe4fbac503b8d1f88e6676011885f34b7174f46e59956bba534ba83abded4df
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "getopts"

%package     -n %{name}+core
Summary:        Getopts-like option parsing - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust getopts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Getopts-like option parsing - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/core)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust getopts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Getopts-like option parsing - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-std-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust getopts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Getopts-like option parsing - feature "unicode" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust getopts crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
