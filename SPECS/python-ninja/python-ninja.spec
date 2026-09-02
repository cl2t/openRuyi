# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ninja

Name:           python-%{srcname}
Version:        1.13.2
Release:        %autorelease
Summary:        Ninja is a small build system with a focus on speed
License:        Apache-2.0
URL:            https://pypi.org/project/ninja/
#!RemoteAsset:  sha256:525bfa3fc88aa30a4467df270fd5be6f9fcae8061d54d4df74ea1dc5abd5a975
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Upstream bundles and builds the ninja binary into %%{_bindir}/ninja, which
# clashes with the system "ninja" package. We ship only the Python wrapper
# module (which simply shells out to the ninja binary) and reuse the system
# ninja binary via the runtime dependency below.
# Upstream's bundled ninja sources build a googletest-based test suite that
# is fetched from the network via CMake FetchContent; disable it (we do not
# run ninja's own test suite) so the build works in the offline build env.
BuildOption(build):  -C cmake.define.BUILD_TESTING=OFF
BuildOption(install):  -l %{srcname} -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  cmake
BuildRequires:  (python3dist(pip) >= 19 with python3dist(pip))
BuildRequires:  python3dist(scikit-build-core)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)

Requires:       ninja

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Ninja is a small build system with a focus on speed. This package provides
the Python interface (the ninja module and ninja_syntax helper) that wraps
the ninja build tool; the ninja executable itself is provided by the system
ninja package.

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}
%doc README.rst HISTORY.rst
%license LICENSE_Apache_20 ninja-upstream/COPYING
%exclude %{_bindir}/ninja

%changelog
%autochangelog
