# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mlua-sys
%global full_version 0.10.0
%global pkgname mlua-sys-0.10

Name:           rust-mlua-sys-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "mlua-sys"
License:        MIT
URL:            https://github.com/mlua-rs/mlua
#!RemoteAsset:  sha256:0f1c3a7fc7580227ece249fd90aa2fa3b39eb2b49d3aec5e103b3e85f2c3dfc8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.62
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(pkg-config-0.3/default) >= 0.3.33
Provides:       crate(mlua-sys) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/external)
Provides:       crate(%{pkgname}/lua51)
Provides:       crate(%{pkgname}/lua52)
Provides:       crate(%{pkgname}/lua53)
Provides:       crate(%{pkgname}/lua54)
Provides:       crate(%{pkgname}/lua55)
Provides:       crate(%{pkgname}/luajit)
Provides:       crate(%{pkgname}/luajit52)
Provides:       crate(%{pkgname}/module)

%description
Source code for takopackized Rust crate "mlua-sys"

%package     -n %{name}+lua-src
Summary:        Low level (FFI) bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau - feature "lua-src"
Requires:       crate(%{pkgname})
Requires:       crate(lua-src-550.0/default) >= 550.0.0
Provides:       crate(%{pkgname}/lua-src)

%description -n %{name}+lua-src
This metapackage enables feature "lua-src" for the Rust mlua-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+luajit-src
Summary:        Low level (FFI) bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau - feature "luajit-src"
Requires:       crate(%{pkgname})
Requires:       crate(luajit-src-210.0/default) >= 210.6.6
Provides:       crate(%{pkgname}/luajit-src)

%description -n %{name}+luajit-src
This metapackage enables feature "luajit-src" for the Rust mlua-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+luau0-src
Summary:        Low level (FFI) bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau - feature "luau0-src" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(luau0-src-0.18/default) >= 0.18.0
Provides:       crate(%{pkgname}/luau)
Provides:       crate(%{pkgname}/luau-codegen)
Provides:       crate(%{pkgname}/luau-vector4)
Provides:       crate(%{pkgname}/luau0-src)

%description -n %{name}+luau0-src
This metapackage enables feature "luau0-src" for the Rust mlua-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "luau", "luau-codegen", and "luau-vector4" features.

%package     -n %{name}+vendored
Summary:        Low level (FFI) bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau - feature "vendored"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/lua-src)
Requires:       crate(%{pkgname}/luajit-src)
Provides:       crate(%{pkgname}/vendored)

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust mlua-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
