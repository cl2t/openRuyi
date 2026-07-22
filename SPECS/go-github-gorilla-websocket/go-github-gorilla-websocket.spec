# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           websocket
%define go_import_path  github.com/gorilla/websocket
%define commit_id       e064f32e3674d9d79a8fd417b5bc06fa5c6cad8f

Name:           go-github-gorilla-websocket
Version:        1.5.4+git20260721.e064f32
Release:        %autorelease
Summary:        Package gorilla/websocket is a fast, well-tested and widely used WebSocket implementation for Go.
License:        BSD-2-Clause
URL:            https://github.com/gorilla/websocket
#!RemoteAsset:  sha256:37ab908960f373a163c780c9246a582744e490258baeeceb285e59219cbfe26c
Source0:        https://github.com/gorilla/websocket/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backport upstream commit ad0b815 to deflake proxy unit tests.
# https://github.com/gorilla/websocket/commit/ad0b815061a606d1f16de28f405996d586bc9738
Patch1000:      1000-deflake-proxy-unit-tests.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/gorilla/websocket) = %{version}

Requires:       go(golang.org/x/net)

%description
Gorilla WebSocket is a Go (http://golang.org/) implementation of the
WebSocket (http://www.rfc-editor.org/rfc/rfc6455.txt) protocol.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
