# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           asn1-ber
%define go_import_path  github.com/go-asn1-ber/asn1-ber

Name:           go-github-go-asn1-ber-asn1-ber
Version:        1.5.8
Release:        %autorelease
Summary:        ASN.1 BER encoding and decoding for Go
License:        MIT
URL:            https://github.com/go-asn1-ber/asn1-ber
#!RemoteAsset:  sha256:b5ecbaaa5030dbe6144ac1fbba010bbdc0db11af4fc77cdaa9ab059645fd3533
Source0:        https://github.com/go-asn1-ber/asn1-ber/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-asn1-ber/asn1-ber) = %{version}

%description
asn1-ber implements a subset of ASN.1 BER encoding and decoding used by
the LDAP protocol in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
