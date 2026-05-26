# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syntect
%global full_version 5.3.0
%global pkgname syntect-5.0

Name:           rust-syntect-5.0
Version:        5.3.0
Release:        %autorelease
Summary:        Rust crate "syntect"
License:        MIT
URL:            https://github.com/trishume/syntect
#!RemoteAsset:  sha256:656b45c05d95a5704399aeef6bd0ddec7b2b3531b7c9e900abbf7c4d2190c925
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-derive-1.0/default) >= 1.0.228
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Provides:       crate(syntect) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "syntect"

%package     -n %{name}+bincode
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "bincode"
Requires:       crate(%{pkgname})
Requires:       crate(bincode-1.0/default) >= 1.3.3
Provides:       crate(%{pkgname}/bincode)

%description -n %{name}+bincode
This metapackage enables feature "bincode" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default-fancy
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "default-fancy"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/default-syntaxes)
Requires:       crate(%{pkgname}/default-themes)
Requires:       crate(%{pkgname}/dump-create)
Requires:       crate(%{pkgname}/dump-load)
Requires:       crate(%{pkgname}/html)
Requires:       crate(%{pkgname}/parsing)
Requires:       crate(%{pkgname}/plist-load)
Requires:       crate(%{pkgname}/regex-fancy)
Requires:       crate(%{pkgname}/yaml-load)
Provides:       crate(%{pkgname}/default-fancy)

%description -n %{name}+default-fancy
This metapackage enables feature "default-fancy" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default-onig
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "default-onig" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/default-syntaxes)
Requires:       crate(%{pkgname}/default-themes)
Requires:       crate(%{pkgname}/dump-create)
Requires:       crate(%{pkgname}/dump-load)
Requires:       crate(%{pkgname}/html)
Requires:       crate(%{pkgname}/parsing)
Requires:       crate(%{pkgname}/plist-load)
Requires:       crate(%{pkgname}/regex-onig)
Requires:       crate(%{pkgname}/yaml-load)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/default-onig)

%description -n %{name}+default-onig
This metapackage enables feature "default-onig" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+default-syntaxes
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "default-syntaxes"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/dump-load)
Requires:       crate(%{pkgname}/parsing)
Provides:       crate(%{pkgname}/default-syntaxes)

%description -n %{name}+default-syntaxes
This metapackage enables feature "default-syntaxes" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-create
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "dump-create" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bincode)
Requires:       crate(%{pkgname}/flate2)
Provides:       crate(%{pkgname}/default-themes)
Provides:       crate(%{pkgname}/dump-create)
Provides:       crate(%{pkgname}/dump-load)

%description -n %{name}+dump-create
This metapackage enables feature "dump-create" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default-themes", and "dump-load" features.

%package     -n %{name}+fancy-regex
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "fancy-regex" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(fancy-regex-0.16/default) >= 0.16.2
Provides:       crate(%{pkgname}/fancy-regex)
Provides:       crate(%{pkgname}/regex-fancy)

%description -n %{name}+fancy-regex
This metapackage enables feature "fancy-regex" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "regex-fancy" feature.

%package     -n %{name}+flate2
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "flate2"
Requires:       crate(%{pkgname})
Requires:       crate(flate2-1.0/default) >= 1.1.9
Provides:       crate(%{pkgname}/flate2)

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fnv
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "fnv"
Requires:       crate(%{pkgname})
Requires:       crate(fnv-1.0/default) >= 1.0.7
Provides:       crate(%{pkgname}/fnv)

%description -n %{name}+fnv
This metapackage enables feature "fnv" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+metadata
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "metadata"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/parsing)
Requires:       crate(%{pkgname}/plist-load)
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname}/metadata)

%description -n %{name}+metadata
This metapackage enables feature "metadata" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+onig
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "onig" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(onig-6.0) >= 6.5.3
Provides:       crate(%{pkgname}/onig)
Provides:       crate(%{pkgname}/regex-onig)

%description -n %{name}+onig
This metapackage enables feature "onig" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "regex-onig" feature.

%package     -n %{name}+parsing
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "parsing" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/dump-create)
Requires:       crate(%{pkgname}/dump-load)
Requires:       crate(%{pkgname}/fnv)
Requires:       crate(%{pkgname}/regex-syntax)
Provides:       crate(%{pkgname}/html)
Provides:       crate(%{pkgname}/parsing)

%description -n %{name}+parsing
This metapackage enables feature "parsing" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "html" feature.

%package     -n %{name}+plist
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "plist"
Requires:       crate(%{pkgname})
Requires:       crate(plist-1.0/default) >= 1.9.0
Provides:       crate(%{pkgname}/plist)

%description -n %{name}+plist
This metapackage enables feature "plist" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+plist-load
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "plist-load"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/plist)
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname}/plist-load)

%description -n %{name}+plist-load
This metapackage enables feature "plist-load" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex-syntax
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "regex-syntax"
Requires:       crate(%{pkgname})
Requires:       crate(regex-syntax-0.8/default) >= 0.8.10
Provides:       crate(%{pkgname}/regex-syntax)

%description -n %{name}+regex-syntax
This metapackage enables feature "regex-syntax" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yaml-load
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "yaml-load"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/parsing)
Requires:       crate(%{pkgname}/yaml-rust)
Provides:       crate(%{pkgname}/yaml-load)

%description -n %{name}+yaml-load
This metapackage enables feature "yaml-load" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yaml-rust
Summary:        High quality syntax highlighting and code intelligence using Sublime Text's grammars - feature "yaml-rust"
Requires:       crate(%{pkgname})
Requires:       crate(yaml-rust-0.4/default) >= 0.4.5
Provides:       crate(%{pkgname}/yaml-rust)

%description -n %{name}+yaml-rust
This metapackage enables feature "yaml-rust" for the Rust syntect crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
