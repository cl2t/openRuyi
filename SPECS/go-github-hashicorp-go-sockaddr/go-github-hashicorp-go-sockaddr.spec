# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-sockaddr
%define go_import_path  github.com/hashicorp/go-sockaddr

# Tests shell out to /sbin/ip and probe real network interfaces, which the
# isolated build sandbox does not provide; run them but tolerate the failures.
%global go_test_ignore_failure 1

Name:           go-github-hashicorp-go-sockaddr
Version:        1.0.2
Release:        %autorelease
Summary:        IP address and UNIX socket convenience functions for Go
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-sockaddr
#!RemoteAsset:  sha256:ce70228b6c0ac432b97c2a98697600668bf7ac8b4cd21e7c6767bed1e755ae7f
Source0:        https://github.com/hashicorp/go-sockaddr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/errwrap)

Provides:       go(github.com/hashicorp/go-sockaddr) = %{version}

Requires:       go(github.com/hashicorp/errwrap)

# Drop the optional cmd/sockaddr CLI; it pulls in mitchellh/cli,
# mitchellh/go-wordwrap and ryanuber/columnize, none of which the library
# (used by consul/api via serf/memberlist) needs.
%prep -a
rm -rf cmd

%description
go-sockaddr provides convenience functions for working with IP addresses
and UNIX socket addresses in Go, including heuristics for selecting
interface IP addresses at runtime.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
