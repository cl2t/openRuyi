# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xds
# So the import path technically is github.com/cncf/xds/go
%define go_import_path  github.com/cncf/xds
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id dba9d589def2cd10099a3a64887d859188c2f57a
# Avoid circular dependency issue with the first two packages
%global go_test_exclude_glob %{shrink:
    google.golang.org/grpc*
    google.golang.org/genproto*
    github.com/cncf/xds/go/xds/service/orca*
    github.com/cncf/xds/go/udpa/service/orca*
    github.com/cncf/xds/go/xds/type*
    github.com/cncf/xds/test/build*
}

Name:           go-github-cncf-xds
Version:        0+git20260721.dba9d58
Release:        %autorelease
Summary:        xDS API Working Group
License:        Apache-2.0
URL:            https://github.com/cncf/xds
#!RemoteAsset:  sha256:eaca6f7ac95a1addcc93e7d4bed4c8b697a767f122dbd1978e2dd62da0b701f0
Source0:        https://github.com/cncf/xds/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/cncf/xds/go) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
The objective of the xDS API Working Group (xDS-WG) is to bring together
parties across the industry interested in a common control and
configuration API for data plane proxies and load balancers, based on
the xDS APIs.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
