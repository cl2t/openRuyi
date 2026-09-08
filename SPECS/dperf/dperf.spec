# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dperf
%define go_import_path  github.com/minio/dperf

Name:           dperf
Version:        0.6.3
Release:        %autorelease
Summary:        Drive performance measurement tool
License:        AGPL-3.0-only
URL:            https://github.com/minio/dperf
#!RemoteAsset:  sha256:6b1205857cf8606c128ed2ee6467a196fcf0821301662d2c42c1f84a67f68a9d
Source0:        https://github.com/minio/dperf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang
BuildOption(build):  -ldflags "-X github.com/minio/dperf/cmd.Version=%{version}"

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bygui86/multi-profile/v2)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/felixge/fgprof)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/minio/pkg/v3)
BuildRequires:  go(github.com/ncw/directio)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(golang.org/x/sys)

%description
dperf measures sequential read and write throughput on one or more
paths so slow drives can be identified. MinIO vendors the same
command and imports github.com/minio/dperf.

%package     -n go-github-minio-dperf
Summary:        Go source for the dperf drive benchmark
BuildArch:      noarch
Provides:       go(github.com/minio/dperf) = %{version}
Requires:       go(github.com/bygui86/multi-profile/v2)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/felixge/fgprof)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/minio/pkg/v3)
Requires:       go(github.com/ncw/directio)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/viper)
Requires:       go(golang.org/x/sys)

%description -n go-github-minio-dperf
This package contains the reusable Go source for dperf, including the
pkg/dperf benchmark used by the dperf command.

%prep -a
# hack/ is license-header tooling, not the program or library.
rm -rf hack %{_builddir}/go/src/%{go_import_path}/hack

%install -a
# The command is already installed; keep it out of the noarch source package.
rm -f %{_name}
%buildsystem_golangmodules_install

%check -p
%{buildroot}%{_bindir}/%{_name} --version

%files
%doc README.md
%license LICENSE
%{_bindir}/dperf

%files -n go-github-minio-dperf
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
