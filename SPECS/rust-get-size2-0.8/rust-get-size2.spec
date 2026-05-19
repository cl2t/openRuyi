# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name get-size2
%global full_version 0.8.0
%global pkgname get-size2-0.8

Name:           rust-get-size2-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "get-size2"
License:        MIT OR Apache-2.0
URL:            https://github.com/bircni/get-size2
#!RemoteAsset:  sha256:d5b6f7d040889b1980e31d03585f0150223f44eeada7a69c525cbb74c38266f6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "get-size2"

%package     -n %{name}+bytes
Summary:        Determine the size in bytes an object occupies inside RAM - feature "bytes"
Requires:       crate(%{pkgname})
Requires:       crate(bytes-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bytes)

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Determine the size in bytes an object occupies inside RAM - feature "chrono"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/chrono)

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-tz
Summary:        Determine the size in bytes an object occupies inside RAM - feature "chrono-tz"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-tz-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/chrono-tz)

%description -n %{name}+chrono-tz
This metapackage enables feature "chrono-tz" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compact-str
Summary:        Determine the size in bytes an object occupies inside RAM - feature "compact-str"
Requires:       crate(%{pkgname})
Requires:       crate(compact-str-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/compact-str)

%description -n %{name}+compact-str
This metapackage enables feature "compact-str" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+get-size-derive2
Summary:        Determine the size in bytes an object occupies inside RAM - feature "get-size-derive2" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(get-size-derive2-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/get-size-derive2)

%description -n %{name}+get-size-derive2
This metapackage enables feature "get-size-derive2" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+hashbrown
Summary:        Determine the size in bytes an object occupies inside RAM - feature "hashbrown"
Requires:       crate(%{pkgname})
Requires:       crate(hashbrown-0.17) >= 0.17.0
Provides:       crate(%{pkgname}/hashbrown)

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Determine the size in bytes an object occupies inside RAM - feature "indexmap"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0) >= 2.14.0
Provides:       crate(%{pkgname}/indexmap)

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ordermap
Summary:        Determine the size in bytes an object occupies inside RAM - feature "ordermap"
Requires:       crate(%{pkgname})
Requires:       crate(ordermap-1.0) >= 1.2.0
Provides:       crate(%{pkgname}/ordermap)

%description -n %{name}+ordermap
This metapackage enables feature "ordermap" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Determine the size in bytes an object occupies inside RAM - feature "smallvec"
Requires:       crate(%{pkgname})
Requires:       crate(smallvec-1.0) >= 1.15.1
Provides:       crate(%{pkgname}/smallvec)

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin-vec
Summary:        Determine the size in bytes an object occupies inside RAM - feature "thin-vec"
Requires:       crate(%{pkgname})
Requires:       crate(thin-vec-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/thin-vec)

%description -n %{name}+thin-vec
This metapackage enables feature "thin-vec" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url
Summary:        Determine the size in bytes an object occupies inside RAM - feature "url"
Requires:       crate(%{pkgname})
Requires:       crate(url-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/url)

%description -n %{name}+url
This metapackage enables feature "url" for the Rust get-size2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
