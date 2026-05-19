# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name assert_fs
%global full_version 1.1.3
%global pkgname assert-fs-1.0

Name:           rust-assert-fs-1.0
Version:        1.1.3
Release:        %autorelease
Summary:        Rust crate "assert_fs"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/assert_fs
#!RemoteAsset:  sha256:a652f6cb1f516886fcfee5e7a5c078b9ade62cfcb889524efe5a64d682dd27a9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(doc-comment-0.3/default) >= 0.3.3
Requires:       crate(globwalk-0.9/default) >= 0.9.1
Requires:       crate(predicates-3.0/diff) >= 3.1.3
Requires:       crate(predicates-core-1.0/default) >= 1.0.9
Requires:       crate(predicates-tree-1.0/default) >= 1.0.12
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "assert_fs"

%package     -n %{name}+color
Summary:        Filesystem fixtures and assertions for testing - feature "color" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(anstream-0.6/default) >= 0.6.7
Requires:       crate(predicates-3.0/color) >= 3.1.3
Requires:       crate(predicates-3.0/diff) >= 3.1.3
Provides:       crate(%{pkgname}/color)
Provides:       crate(%{pkgname}/color-auto)

%description -n %{name}+color
This metapackage enables feature "color" for the Rust assert_fs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "color-auto" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
