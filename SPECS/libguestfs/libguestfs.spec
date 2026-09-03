# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libguestfs
Version:        1.60.1
Release:        %autorelease
Summary:        Library and tools for accessing and modifying VM disk images
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://libguestfs.org/
VCS:            git:https://github.com/libguestfs/libguestfs.git
#!RemoteAsset:  sha256:6311c686700c293c92a9e804074040f4ae536fcbcef0a69973f418c77d3441e9
Source0:        https://download.libguestfs.org/1.60-stable/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-probes
BuildOption(conf):  --disable-appliance
BuildOption(conf):  --disable-daemon
BuildOption(conf):  --disable-ocaml
BuildOption(conf):  --disable-perl
BuildOption(conf):  --disable-python
BuildOption(conf):  --disable-ruby
BuildOption(conf):  --disable-haskell
BuildOption(conf):  --disable-php
BuildOption(conf):  --disable-erlang
BuildOption(conf):  --disable-lua
BuildOption(conf):  --disable-golang
BuildOption(conf):  --disable-gobject
BuildOption(conf):  --without-java
# openRuyi ships fuse3 only; libguestfs looks for pkg-config fuse (v2).
BuildOption(conf):  --disable-fuse
BuildOption(conf):  --with-distro=REDHAT
BuildOption(conf):  --with-extra='openruyi'
BuildOption(conf):  --with-default-backend=direct

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cpio
BuildRequires:  flex
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-devel
BuildRequires:  ocaml-findlib
BuildRequires:  pkgconfig(augeas)
BuildRequires:  pkgconfig(hivex)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  rpcgen
BuildRequires:  xorriso
BuildRequires:  perl
BuildRequires:  qemu
# qemu Requires qemu-user, also provided by qemu-user-static; pick one.
BuildRequires:  qemu-user

# Runtime needs qemu and a kernel to launch the appliance. The
# appliance itself is not built here: OBS cannot download package
# contents into a supermin appliance. Users can build a fixed
# appliance with libguestfs-make-fixed-appliance(1) once supermin
# and a kernel are installed.
Requires:       qemu
Requires:       linux
Requires:       supermin
Requires:       xorriso

%description
Libguestfs is a set of tools for accessing and modifying virtual
machine disk images. It can inspect guests, copy files in and out, and
run commands in the guest. This build ships the C library and
command-line tools; the supermin appliance is not prebuilt.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers and linker files needed to build
software against %{name}.

%prep -a
# openRuyi's kernel RPM is named linux; the iproute tools live in iproute2.
sed -i \
    -e 's/^  kernel$/  linux/' \
    -e 's/^  iproute$/  iproute2/' \
    appliance/packagelist.in

%install -a
# Bindings were disabled; drop leftover man pages if the build still
# installed them.
rm -f %{buildroot}%{_mandir}/man3/guestfs-ocaml.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-perl.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-python.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-ruby.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-golang.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-java.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-lua.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-php.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-haskell.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-erlang.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-gobject.3*
# --disable-appliance skips installing this helper; still useful at runtime.
install -D -p -m 0755 appliance/libguestfs-make-fixed-appliance \
    %{buildroot}%{_bindir}/libguestfs-make-fixed-appliance

%check
# Appliance and language bindings are disabled; most tests need a
# running appliance or the Python module.
true

%files
%doc README
%license COPYING COPYING.LIB
%config(noreplace) %{_sysconfdir}/libguestfs-tools.conf
%{_bindir}/guestfish
%{_bindir}/libguestfs-test-tool
%{_bindir}/libguestfs-make-fixed-appliance
%{_bindir}/virt-copy-in
%{_bindir}/virt-copy-out
%{_bindir}/virt-tar-in
%{_bindir}/virt-tar-out
%{_bindir}/virt-rescue
%{_libdir}/libguestfs.so.*
%{_datadir}/locale/*/LC_MESSAGES/libguestfs.mo
%{_mandir}/man1/guestfish.1*
%{_mandir}/man1/libguestfs-test-tool.1*
%{_mandir}/man1/virt-copy-in.1*
%{_mandir}/man1/virt-copy-out.1*
%{_mandir}/man1/virt-tar-in.1*
%{_mandir}/man1/virt-tar-out.1*
%{_mandir}/man1/virt-rescue.1*
%{_mandir}/man1/guestfs-*.1*
%{_mandir}/man5/libguestfs-tools.conf.5*
%{bash_completions_dir}/*

%files devel
%{_includedir}/guestfs.h
%{_libdir}/libguestfs.so
%{_libdir}/pkgconfig/libguestfs.pc
%{_mandir}/man3/guestfs.3*
%{_mandir}/man3/guestfs-examples.3*
%{_mandir}/man3/libguestfs.3*

%changelog
%autochangelog
