# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopsutil
%define go_import_path  github.com/shirou/gopsutil/v3
# CPU, memory, swap and process tests depend on host cgroup, swap and
# PID namespace behavior and fail in the OBS sandbox.
%define go_test_ignore_failure 1

Name:           go-github-shirou-gopsutil-v3
Version:        3.24.5
Release:        %autorelease
Summary:        psutil for golang
License:        BSD-3-Clause
URL:            https://github.com/shirou/gopsutil
#!RemoteAsset:  sha256:c4c61a6ade378e39b89a33bb959fc2c32092f0ba35f39aec99519fad4e9173b4
Source0:        https://github.com/shirou/gopsutil/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/shoenig/go-m1cpu)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/shirou/gopsutil/v3) = %{version}
Provides:       go-github-shirou-gopsutil = %{version}-%{release}

Obsoletes:      go-github-shirou-gopsutil

Requires:       go(github.com/lufia/plan9stats)
Requires:       go(github.com/power-devops/perfstat)
Requires:       go(github.com/shoenig/go-m1cpu)
Requires:       go(github.com/tklauser/go-sysconf)
Requires:       go(github.com/yusufpapurcu/wmi)
Requires:       go(golang.org/x/sys)

%description
gopsutil is a port of Python psutil. It reports process and system
information from Go. This package provides the v3 module path used by
madmin-go/v3.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
