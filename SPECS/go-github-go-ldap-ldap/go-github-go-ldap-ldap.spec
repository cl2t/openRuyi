# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ldap
%define go_import_path  github.com/go-ldap/ldap
# gssapi pulls jcmturner/gokrb5, which is unused by MinIO pkg/v3.
%define go_test_exclude_glob github.com/go-ldap/ldap/v3/gssapi*
# Remaining v3 tests dial 127.0.0.1:3389 and fail in the build sandbox.
%define go_test_ignore_failure 1

Name:           go-github-go-ldap-ldap
Version:        3.4.13
Release:        %autorelease
Summary:        Basic LDAP v3 functionality for the GO programming language.
License:        MIT
URL:            https://github.com/go-ldap/ldap
#!RemoteAsset:  sha256:554427b39afe6ddd4f90af137a46fc7b1cd8d16b70b38c3a214237af298faa71
Source0:        https://github.com/go-ldap/ldap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Azure/go-ntlmssp)
BuildRequires:  go(github.com/go-asn1-ber/asn1-ber)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/go-ldap/ldap) = %{version}
# The v3.4.x archive stores the module in v3/; MinIO pkg/v3 imports /v3.
Provides:       go(github.com/go-ldap/ldap/v3) = %{version}

Requires:       go(github.com/Azure/go-ntlmssp)
Requires:       go(github.com/go-asn1-ber/asn1-ber)
Requires:       go(github.com/google/uuid)
Requires:       go(golang.org/x/crypto)

%description
Basic LDAP v3 functionality for the GO programming language.

The library implements the following specifications:

 * (https://datatracker.ietf.org/doc/html/rfc4511) for basic operations
 * (https://datatracker.ietf.org/doc/html/rfc3062) for password modify
   operation
 * (https://datatracker.ietf.org/doc/html/rfc4514) for distinguished
   names parsing
 * (https://datatracker.ietf.org/doc/html/rfc4533) for Content
   Synchronization Operation
 * (https://datatracker.ietf.org/doc/html/draft-armijo-ldap-treedelete-
   02) for Tree Delete Control
 * (https://datatracker.ietf.org/doc/html/rfc2891) for Server Side
   Sorting of Search Results
 * (https://datatracker.ietf.org/doc/html/rfc4532) for WhoAmI requests

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
