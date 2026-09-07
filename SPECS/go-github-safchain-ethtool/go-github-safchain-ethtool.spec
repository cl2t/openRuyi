# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ethtool
%define go_import_path  github.com/safchain/ethtool
# ioctl tests need a real NIC and are blocked in the build sandbox.
%define go_test_ignore_failure 1

Name:           go-github-safchain-ethtool
Version:        0.5.10
Release:        %autorelease
Summary:        Go bindings for Linux SIOCETHTOOL ioctl operations
License:        Apache-2.0
URL:            https://github.com/safchain/ethtool
#!RemoteAsset:  sha256:0a6a0c58bd9924eda29d8120ceaace297259e2dee44abd1e2e83812700a4beb6
Source0:        https://github.com/safchain/ethtool/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/safchain/ethtool) = %{version}

Requires:       go(golang.org/x/sys)

%description
ethtool wraps Linux SIOCETHTOOL ioctl operations so Go programs can
read NIC statistics, driver information, and veth peer indexes.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
