# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yaml.v2
%define go_import_path  go.yaml.in/yaml/v2

Name:           go-gopkg-yaml.v2
Version:        2.4.4
Release:        %autorelease
Summary:        YAML support for the Go language.
License:        Apache-2.0
URL:            https://github.com/yaml/go-yaml
#!RemoteAsset:  sha256:e80715d6f56fd2d9bdf1bb3c1024bddfd819cd4facb4af6d59d14d4cfa2aa1f9
Source0:        https://github.com/yaml/go-yaml/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-yaml-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(go.yaml.in/yaml/v2) = %{version}
# Preserve the legacy import path required by existing consumers.
Provides:       go(gopkg.in/yaml.v2) = %{version}

%description
The yaml package enables Go programs to comfortably encode and decode
YAML values. It was developed within Canonical
(https://www.canonical.com) as part of the juju
(https://juju.ubuntu.com) project, and is based on a pure Go port of the
well-known libyaml (http://pyyaml.org/wiki/LibYAML) C library to parse
and generate YAML data quickly and reliably.

%install -a
# Compatibility import path gopkg.in/yaml.v2
install -d -m 0755 %{buildroot}%{go_sys_gopath}/gopkg.in
ln -s ../%{go_import_path} %{buildroot}%{go_sys_gopath}/gopkg.in/yaml.v2

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/gopkg.in/yaml.v2

%changelog
%autochangelog
