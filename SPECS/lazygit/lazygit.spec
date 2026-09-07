# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lazygit
%define go_import_path  github.com/jesseduffield/lazygit

Name:           lazygit
Version:        0.65.0
Release:        %autorelease
Summary:        Simple terminal UI for git commands
License:        MIT AND BSD-3-Clause
URL:            https://github.com/jesseduffield/lazygit
#!RemoteAsset:  sha256:972151d83d8fdfa5c7c881c34349ba4a38c37b7085667696b85c443d2fca97ed
Source0:        https://github.com/jesseduffield/lazygit/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang
BuildOption(build):  -ldflags "-X main.version=%{version} -X main.buildSource=openRuyi"
# Go 1.27 vet rejects upstream non-constant format strings in TextStyle.Sprintf.
# Match upstream unit tests; integration tests skip themselves in short mode.
BuildOption(check):  -vet=off -short

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  git
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(github.com/adrg/xdg)
BuildRequires:  go(github.com/atotto/clipboard)
BuildRequires:  go(github.com/aybabtme/humanlog)
BuildRequires:  go(github.com/cli/go-gh/v2)
BuildRequires:  go(github.com/cloudfoundry/jibber_jabber)
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(github.com/gdamore/tcell/v3)
BuildRequires:  go(github.com/go-errors/errors)
BuildRequires:  go(github.com/gookit/color)
BuildRequires:  go(github.com/integrii/flaggy)
BuildRequires:  go(github.com/jesseduffield/generics)
BuildRequires:  go(github.com/jesseduffield/lazycore)
BuildRequires:  go(github.com/kardianos/osext)
BuildRequires:  go(github.com/karimkhaleel/jsonschema)
BuildRequires:  go(github.com/kyokomi/emoji/v2)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mgutz/str)
BuildRequires:  go(github.com/mitchellh/go-ps)
BuildRequires:  go(github.com/petermattis/goid)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/sahilm/fuzzy)
BuildRequires:  go(github.com/samber/lo)
BuildRequires:  go(github.com/sanity-io/litter)
BuildRequires:  go(github.com/sasha-s/go-deadlock)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spkg/bom)
BuildRequires:  go(github.com/stefanhaller/git-todo-parser)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/ozeidan/fuzzy-patricia.v3)
BuildRequires:  go(gopkg.in/yaml.v3)

Requires:       git

%description
lazygit is a simple terminal UI for git commands, providing panels for files,
branches, commits, stashes and more.

%package     -n go-github-jesseduffield-lazygit
Summary:        Go source for the lazygit terminal UI
BuildArch:      noarch
Provides:       go(github.com/jesseduffield/lazygit) = %{version}
Requires:       go(dario.cat/mergo)
Requires:       go(github.com/adrg/xdg)
Requires:       go(github.com/atotto/clipboard)
Requires:       go(github.com/aybabtme/humanlog)
Requires:       go(github.com/cli/go-gh/v2)
Requires:       go(github.com/cloudfoundry/jibber_jabber)
Requires:       go(github.com/creack/pty)
Requires:       go(github.com/gdamore/tcell/v3)
Requires:       go(github.com/go-errors/errors)
Requires:       go(github.com/gookit/color)
Requires:       go(github.com/integrii/flaggy)
Requires:       go(github.com/jesseduffield/generics)
Requires:       go(github.com/jesseduffield/lazycore)
Requires:       go(github.com/kardianos/osext)
Requires:       go(github.com/karimkhaleel/jsonschema)
Requires:       go(github.com/kyokomi/emoji/v2)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/mgutz/str)
Requires:       go(github.com/mitchellh/go-ps)
Requires:       go(github.com/petermattis/goid)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(github.com/sahilm/fuzzy)
Requires:       go(github.com/samber/lo)
Requires:       go(github.com/sanity-io/litter)
Requires:       go(github.com/sasha-s/go-deadlock)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/spf13/afero)
Requires:       go(github.com/spkg/bom)
Requires:       go(github.com/stefanhaller/git-todo-parser)
Requires:       go(github.com/xo/terminfo)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(gopkg.in/ozeidan/fuzzy-patricia.v3)
Requires:       go(gopkg.in/yaml.v3)

%description -n go-github-jesseduffield-lazygit
This package contains the reusable Go source for lazygit, including the
in-tree gocui terminal UI used by the lazygit command.

# Remove bundled dependencies from both the source tree and the GOPATH copy
# prepared by the golang BuildSystem, so builds and tests use distro packages.
%prep -a
rm -rf vendor %{_builddir}/go/src/%{go_import_path}/vendor

%install -a
# The default install has already installed the command. Keep its build output
# out of the noarch Go source subpackage.
rm -f %{_name}
# Preserve the two different license texts under distinct installed names.
cp pkg/gocui/LICENSE LICENSE.gocui
%buildsystem_golangmodules_install

%check -p
export TERM=xterm-256color
unset NO_COLOR
%{buildroot}%{_bindir}/%{_name} --version
# Fixture unit tests locate the project root through .git, absent in archives.
git init -q %{_builddir}/go/src/%{go_import_path}

%files
%doc README* docs
%license LICENSE LICENSE.gocui
%{_bindir}/lazygit

%files -n go-github-jesseduffield-lazygit
%doc README*
%license LICENSE LICENSE.gocui
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
