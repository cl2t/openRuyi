# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           etcd
%define go_import_path  go.etcd.io/etcd

Name:           go-etcd-io-etcd
Version:        3.5.21
Release:        %autorelease
Summary:        etcd v3 API and Go client modules
License:        Apache-2.0
URL:            https://github.com/etcd-io/etcd
#!RemoteAsset:  sha256:76d7fcafe4fcc957fcd45671226b992c16e5f5e724935dea9df0190ac2b13481
Source0:        https://github.com/etcd-io/etcd/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/etcd-io/etcd/commit/55abfaafbee62a836d8ce178776dca202d5683b4
Patch1000:      1000-fix-manual-resolver-client-connection.patch

# Go 1.27 vet rejects non-constant status.Errorf formats in retry_interceptor.go.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go-rpm-macros

Provides:       go(go.etcd.io/etcd/api/v3) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3) = %{version}

Requires:       go(github.com/coreos/go-semver)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/grpc-ecosystem/go-grpc-prometheus)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/grpc)
Requires:       go(sigs.k8s.io/yaml)

%description
This package contains the etcd v3 protobuf and gRPC API, shared client
helpers, and Go client. The three modules are released from the same
repository and installed together at their respective Go import paths.

%prep -a
# Materialize example-test symlinks before removing the server integration tree.
cp -aL client/v3 client/v3-dereferenced
rm -rf client/v3
mv client/v3-dereferenced client/v3
# Package the client modules; the etcd server is packaged separately.
find . -maxdepth 1 -mindepth 1 -not -name api -not -name client \
    -not -name tests -not -name LICENSE -not -name 'README*' -not -name '_build' -exec rm -rf {} +
find client -maxdepth 1 -mindepth 1 -not -name pkg -not -name v3 -exec rm -rf {} +
# Client YAML tests load certificates from the shared upstream fixture directory.
find tests -maxdepth 1 -mindepth 1 -not -name fixtures -exec rm -rf {} +
# The upstream layout omits /v3 for api and client/pkg. Match their module paths.
mv api api-src
mkdir api
mv api-src api/v3
mv client/pkg client/pkg-src
mkdir client/pkg
mv client/pkg-src client/pkg/v3
# Generated HTTP gateway stubs require grpc-gateway v1; the distro provides
# the incompatible v2 API. The client uses the protobuf/gRPC definitions.
rm -rf api/v3/etcdserverpb/gw

%files
%doc README*
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
