# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pprof
%define go_import_path  github.com/google/pprof
%define commit_id       7023385849c07b2a176ad3e985ed16c5019aa9df
# Browser and binutils tests require external browsers and native toolchains.
%define go_test_exclude %{shrink:
    github.com/google/pprof/browsertests
    github.com/google/pprof/internal/binutils
}

Name:           pprof
Version:        0+git20260721.7023385
Release:        %autorelease
Summary:        Visualization and analysis tool for profiling data
License:        Apache-2.0
URL:            https://github.com/google/pprof
#!RemoteAsset:  sha256:711104abfa317e25de02c22bbd1621d37a97cfa6b29354b7bb55c917f4f39911
Source0:        https://github.com/google/pprof/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/chzyer/readline)
BuildRequires:  go(github.com/ianlancetaylor/demangle)

%description
pprof reads profiling samples in profile.proto format and generates text and
graphical reports for visualizing and analyzing program performance.

%package     -n go-github-google-pprof
Summary:        Go source packages for pprof
BuildArch:      noarch
Provides:       go(github.com/google/pprof) = %{version}
Requires:       go(github.com/chzyer/readline)
Requires:       go(github.com/ianlancetaylor/demangle)

%description -n go-github-google-pprof
This package contains the reusable Go source packages from github.com/google/pprof,
including the profile parser used by Prometheus.

%build
%{go_common}
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
%__go build %{go_build_flags_default} -o %{_builddir}/pprof .

%install
install -D -m 0755 %{_builddir}/pprof %{buildroot}%{_bindir}/pprof
%buildsystem_golangmodules_install
# Prebuilt cross-platform fixtures are only test inputs and make the reusable
# source subpackage architecture-dependent if installed.
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/internal/binutils/testdata
rm -f %{buildroot}%{go_sys_gopath}/%{go_import_path}/internal/report/testdata/sample.bin

%check
%buildsystem_golangmodules_check

%files
%doc README*
%license LICENSE*
%{_bindir}/pprof

%files -n go-github-google-pprof
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
