# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname deepspeed

# DeepSpeed compiles its C++/CUDA ops just-in-time at runtime (DS_BUILD_OPS=0
# is the default on Linux), so the wheel is pure Python and noarch. Only a
# top-level import smoke test is run in %%check: the real test suite needs
# GPUs and a distributed multi-process setup not available in the build env.

Name:           python-%{srcname}
Version:        0.19.6
Release:        %autorelease
Summary:        Deep learning optimization library for distributed training and inference
License:        Apache-2.0
URL:            https://pypi.org/project/deepspeed/
#!RemoteAsset:  sha256:31593acffbe4794c74446094122b1bc29d8c73a137e37aff899ca4a6480df2d8
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
BuildOption(check):  -t

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
# Runtime dependencies that need to be available during build for import checks
BuildRequires:  python3dist(einops)
BuildRequires:  python3dist(hjson)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(ninja)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(py-cpuinfo)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(tqdm)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
DeepSpeed is a deep learning optimization library that makes distributed
training and inference easy, efficient, and effective. It provides
ZeRO-powered data parallelism, pipeline and tensor parallelism, optimized
kernels, and memory-efficient optimizers for large-scale models.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
