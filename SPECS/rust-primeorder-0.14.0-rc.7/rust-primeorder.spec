# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name primeorder
%global full_version 0.14.0-rc.7
%global pkgname primeorder-0.14.0-rc.7

Name:           rust-primeorder-0.14.0-rc.7
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "primeorder"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/primeorder
#!RemoteAsset:  sha256:a0c5c8a39bcd764bfedf456e8d55e115fe86dda3e0f555371849f2a41cbc9706
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.14.0-rc.28/arithmetic) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(primeorder) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/dev)
Provides:       crate(%{pkgname}/hash2curve)

%description
Generic over field elements and curve equation coefficients
Source code for takopackized Rust crate "primeorder"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(elliptic-curve-0.14.0-rc.28/alloc) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/arithmetic) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
Generic over field elements and curve equation coefficients
This metapackage enables feature "alloc" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serdect)
Requires:       crate(elliptic-curve-0.14.0-rc.28/arithmetic) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/serde) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Generic over field elements and curve equation coefficients
This metapackage enables feature "serde" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "serdect"
Requires:       crate(%{pkgname})
Requires:       crate(serdect-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/serdect)

%description -n %{name}+serdect
Generic over field elements and curve equation coefficients
This metapackage enables feature "serdect" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(elliptic-curve-0.14.0-rc.28/arithmetic) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/std) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
Generic over field elements and curve equation coefficients
This metapackage enables feature "std" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
