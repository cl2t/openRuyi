# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name indicatif
%global full_version 0.18.4
%global pkgname indicatif-0.18

Name:           rust-indicatif-0.18
Version:        0.18.4
Release:        %autorelease
Summary:        Rust crate "indicatif"
License:        MIT
URL:            https://github.com/console-rs/indicatif
#!RemoteAsset:  sha256:25470f23803092da7d239834776d653104d551bc4d7eacaf31e6837854b8e9eb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(console-0.16/ansi-parsing) >= 0.16.1
Requires:       crate(console-0.16/std) >= 0.16.1
Requires:       crate(portable-atomic-1.0/default) >= 1.13.1
Requires:       crate(unit-prefix-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "indicatif"

%package     -n %{name}+default
Summary:        Progress bar and cli reporting library for Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/unicode-width)
Requires:       crate(%{pkgname}/wasmbind)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Progress bar and cli reporting library for Rust - feature "futures"
Requires:       crate(%{pkgname})
Requires:       crate(futures-core-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures)

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+improved-unicode
Summary:        Progress bar and cli reporting library for Rust - feature "improved_unicode"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/unicode-segmentation)
Requires:       crate(%{pkgname}/unicode-width)
Provides:       crate(%{pkgname}/improved-unicode)

%description -n %{name}+improved-unicode
This metapackage enables feature "improved_unicode" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Progress bar and cli reporting library for Rust - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.1
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Progress bar and cli reporting library for Rust - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/default) >= 1.0.0
Requires:       crate(tokio-1.0/io-util) >= 1.0.0
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-segmentation
Summary:        Progress bar and cli reporting library for Rust - feature "unicode-segmentation"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-segmentation-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/unicode-segmentation)

%description -n %{name}+unicode-segmentation
This metapackage enables feature "unicode-segmentation" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-width
Summary:        Progress bar and cli reporting library for Rust - feature "unicode-width"
Requires:       crate(%{pkgname})
Requires:       crate(console-0.16/ansi-parsing) >= 0.16.1
Requires:       crate(console-0.16/std) >= 0.16.1
Requires:       crate(console-0.16/unicode-width) >= 0.16.1
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/unicode-width)

%description -n %{name}+unicode-width
This metapackage enables feature "unicode-width" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vt100
Summary:        Progress bar and cli reporting library for Rust - feature "vt100" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(vt100-0.16/default) >= 0.16.2
Provides:       crate(%{pkgname}/in-memory)
Provides:       crate(%{pkgname}/vt100)

%description -n %{name}+vt100
This metapackage enables feature "vt100" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "in_memory" feature.

%package     -n %{name}+wasmbind
Summary:        Progress bar and cli reporting library for Rust - feature "wasmbind"
Requires:       crate(%{pkgname})
Requires:       crate(web-time-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname}/wasmbind)

%description -n %{name}+wasmbind
This metapackage enables feature "wasmbind" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
