# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hjson

Name:           python-%{srcname}
Version:        3.1.0
Release:        %autorelease
Summary:        Hjson, a user interface for JSON
License:        MIT OR AFL-2.1
URL:            https://pypi.org/project/hjson/
#!RemoteAsset:  sha256:55af475a27cf83a7969c808399d7bccdec8fb836a07ddbd574587593b9cdcf75
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# hjson.ordered_dict is dead Python 2 fallback code (it does
# "from UserDict import DictMixin") that is only imported when
# collections.OrderedDict is missing, which never happens on Python 3.
# Exclude it from the import check; it is never used at runtime.
BuildOption(install):  -l %{srcname} +auto
BuildOption(check):  -e hjson.ordered_dict

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Hjson is a syntax extension to JSON intended to be used as a configuration
file format that is easy for humans to read and edit. It adds comments,
optional commas and quotes, and multiline strings on top of plain JSON.

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
