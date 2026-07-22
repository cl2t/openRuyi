# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nomad
%define go_import_path  github.com/hashicorp/nomad/api
%define commit_id       ea1ca2d932bf310c7fb67b9f7bd0f356ba383d6f
%define archive_dir     nomad-%{commit_id}

# Some api tests start local HTTP servers / probe the network, which the
# isolated build sandbox restricts; run them but tolerate the failures.
%global go_test_ignore_failure 1

Name:           go-github-hashicorp-nomad-api
Version:        0+git20260721.ea1ca2d
Release:        %autorelease
Summary:        Go client library for the HashiCorp Nomad HTTP API
License:        MPL-2.0
URL:            https://github.com/hashicorp/nomad
#!RemoteAsset:  sha256:03c485f28d08f6bda3d8e6055274ae9a43659b9775d5e1a3dec6facb8c8cd741
Source0:        https://github.com/hashicorp/nomad/archive/%{commit_id}.tar.gz#/%{_name}-api-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{archive_dir}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/hashicorp/cronexpr)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/shoenig/test)

Requires:       go(github.com/docker/go-units)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/hashicorp/cronexpr)
Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/hashicorp/go-rootcerts)

Provides:       go(github.com/hashicorp/nomad/api) = %{version}

# The upstream archive is the whole nomad repository; keep only the api
# submodule so the build targets github.com/hashicorp/nomad/api alone.
%prep -a
find . -maxdepth 1 -mindepth 1 -not -name api -exec rm -rf {} +
shopt -s dotglob
mv api/* .
rmdir api

%description
This package provides the Go client library (github.com/hashicorp/nomad/api)
for interacting with the HashiCorp Nomad HTTP API, used by Prometheus' Nomad
service discovery.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
