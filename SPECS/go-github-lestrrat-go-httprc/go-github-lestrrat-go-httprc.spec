# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httprc
%define go_import_path  github.com/lestrrat-go/httprc

Name:           go-github-lestrrat-go-httprc
Version:        1.0.6
Release:        %autorelease
Summary:        HTTP resource cache with periodic refresh
License:        MIT
URL:            https://github.com/lestrrat-go/httprc
#!RemoteAsset:  sha256:d286ea4decdb9370bd4badc8fdc70ce71fe915966d956ddc77a14ab36f9f15aa
Source0:        https://github.com/lestrrat-go/httprc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/lestrrat-go/httpcc)
BuildRequires:  go(github.com/lestrrat-go/option)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/lestrrat-go/httprc) = %{version}

Requires:       go(github.com/lestrrat-go/httpcc)
Requires:       go(github.com/lestrrat-go/option)

%description
httprc caches HTTP resources and keeps them up to date by refreshing
them according to Cache-Control max-age.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
