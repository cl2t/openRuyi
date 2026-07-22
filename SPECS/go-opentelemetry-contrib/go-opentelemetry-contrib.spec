# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-go-contrib
%define go_import_path  go.opentelemetry.io/contrib
%define otelgrpc_path   instrumentation/google.golang.org/grpc/otelgrpc
%define otelhttp_path   instrumentation/net/http/otelhttp
%define oteltrace_path  instrumentation/net/http/httptrace/otelhttptrace

%define dir_otelgrpc    opentelemetry-go-contrib-instrumentation-google.golang.org-grpc-otelgrpc-v%{version}
%define dir_otelhttp    opentelemetry-go-contrib-instrumentation-net-http-otelhttp-v%{version}
%define dir_oteltrace   opentelemetry-go-contrib-instrumentation-net-http-httptrace-otelhttptrace-v%{version}

Name:           go-opentelemetry-contrib
Version:        0.69.0
Release:        %autorelease
Summary:        OpenTelemetry instrumentation modules for Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go-contrib
BuildArch:      noarch
BuildSystem:    golangmodules

# The modules are independently tagged at different repository commits, so use
# each module's exact official tag archive instead of assuming one tag contains
# the other modules at the same version.
#!RemoteAsset:  sha256:b37b3916da7ad1eeb6230b20612c01a08a1227977bd02213e1d6c2c5c3c98c98
Source0:        https://github.com/open-telemetry/opentelemetry-go-contrib/archive/refs/tags/%{otelgrpc_path}/v%{version}.tar.gz#/%{_name}-otelgrpc-%{version}.tar.gz
#!RemoteAsset:  sha256:323ba7865cfb62bd19a2119bca1b39f5f6d64e3629b010f58d5f6c8a02d3e349
Source1:        https://github.com/open-telemetry/opentelemetry-go-contrib/archive/refs/tags/%{otelhttp_path}/v%{version}.tar.gz#/%{_name}-otelhttp-%{version}.tar.gz
#!RemoteAsset:  sha256:f4fe446462d214049ce4a17e77180f473169017ed27be697b8d271827c101560
Source2:        https://github.com/open-telemetry/opentelemetry-go-contrib/archive/refs/tags/%{oteltrace_path}/v%{version}.tar.gz#/%{_name}-oteltrace-%{version}.tar.gz

BuildRequires:  go
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

# Keep the umbrella virtual provide used by existing openRuyi consumers.
Provides:       go(go.opentelemetry.io/contrib) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp) = %{version}

Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides selected OpenTelemetry Go contrib instrumentation modules:
gRPC, HTTP, and HTTP trace instrumentation.

%prep
%setup -q -c -T -a 0
%setup -q -D -T -a 1
%setup -q -D -T -a 2

%install
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/$(dirname %{otelgrpc_path})
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/$(dirname %{otelhttp_path})
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/$(dirname %{oteltrace_path})
cp -a %{dir_otelgrpc}/%{otelgrpc_path} \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/%{otelgrpc_path}
cp -a %{dir_otelhttp}/%{otelhttp_path} \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/%{otelhttp_path}
cp -a %{dir_oteltrace}/%{oteltrace_path} \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/%{oteltrace_path}

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
# TestWithSpanNameFormatter expects Go 1.22+ ServeMux pattern matching;
# force the current behavior in workers that default to httpmuxgo121=1.
export GODEBUG="${GODEBUG:+${GODEBUG},}httpmuxgo121=0"
for _entry in \
    "%{dir_otelgrpc}:%{otelgrpc_path}" \
    "%{dir_otelhttp}:%{otelhttp_path}" \
    "%{dir_oteltrace}:%{oteltrace_path}"; do
    _dir=${_entry%%:*}
    _subdir=${_entry#*:}
    _import_path=%{go_import_path}/${_subdir}
    mkdir -p "%{_builddir}/go/src/$(dirname "${_import_path}")"
    rm -rf "%{_builddir}/go/src/${_import_path}"
    cp -a "${_dir}/${_subdir}" "%{_builddir}/go/src/${_import_path}"
done
for _subdir in %{otelgrpc_path} %{otelhttp_path} %{oteltrace_path}; do
    _import_path=%{go_import_path}/${_subdir}
    pushd "%{_builddir}/go/src/${_import_path}"
    go test -v $(go list -e -f '{{.ImportPath}}' ./...)
    popd
done

%files
%license %{dir_otelgrpc}/LICENSE
%{go_sys_gopath}/%{go_import_path}/%{otelgrpc_path}
%{go_sys_gopath}/%{go_import_path}/%{otelhttp_path}
%{go_sys_gopath}/%{go_import_path}/%{oteltrace_path}

%changelog
%autochangelog
