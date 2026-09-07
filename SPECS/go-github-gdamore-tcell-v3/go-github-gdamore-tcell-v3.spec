# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tcell
%define go_import_path  github.com/gdamore/tcell/v3

Name:           go-github-gdamore-tcell-v3
Version:        3.4.2
Release:        %autorelease
Summary:        Cell-based terminal package for Go
License:        Apache-2.0
URL:            https://github.com/gdamore/tcell
#!RemoteAsset:  sha256:25c2327d78e767166296d951bf0ba7e38f7d3a3f40f981f5f4225d4f1f79334e
Source0:        https://github.com/gdamore/tcell/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/gdamore/encoding)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/gdamore/tcell/v3) = %{version}

Requires:       go(github.com/clipperhouse/displaywidth)
Requires:       go(github.com/clipperhouse/uax29/v2)
Requires:       go(github.com/gdamore/encoding)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)

%description
Tcell provides a cell-based view for text terminals, with support for colors,
Unicode, keyboard input, and mouse events. This package ships the v3 API.

%prep -a
# demos are example programs, not the importable library.
rm -rf demos

%files
%doc README* TUTORIAL*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
