# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tencentcloud-sdk-go
%define go_import_path  github.com/tencentcloud/tencentcloud-sdk-go

Name:           go-github-tencentcloud-tencentcloud-sdk-go
Version:        1.0.413
Release:        %autorelease
Summary:        Tencent Cloud SDK for Go
License:        Apache-2.0
URL:            https://github.com/TencentCloud/tencentcloud-sdk-go
#!RemoteAsset:  sha256:193994747810d3f4426b0c1177382c21bf1ed629dede99aee48a4826a896787b
Source0:        https://github.com/TencentCloud/tencentcloud-sdk-go/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

# All 203 published v1.0.413 module ZIPs, verified with sum.golang.org, match
# the corresponding Source0 contents, including inherited LICENSE files.
# Recheck this on updates; matching version numbers alone are insufficient.
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/aa) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/aai) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/advisor) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/af) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/afc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ame) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ams) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/antiddos) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/apcas) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ape) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/api) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/apigateway) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/apm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/as) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/asr) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/asw) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ba) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/batch) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/bda) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/bi) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/billing) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/bizlive) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/bm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/bmeip) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/bmlb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/bmvpc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/bri) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/bsca) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/btoe) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cam) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/captcha) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/car) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/casb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cat) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cbs) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ccc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cdb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cdc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cdn) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cds) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cfg) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cfs) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cfw) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/chdfs) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cii) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cim) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cis) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ckafka) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/clb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cloudaudit) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cloudhsm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cls) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cme) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cmq) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cms) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cpdp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cr) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cwp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cws) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cynosdb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dasb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dayu) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dbbrain) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dbdc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dcdb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dlc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dnspod) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/domain) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/drm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ds) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dtf) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dts) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/eb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ecc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ecdn) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ecm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/eiam) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/eis) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/emr) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/es) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ess) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/essbasic) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/facefusion) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/faceid) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/fmu) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ft) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/gaap) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/gme) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/gpm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/gs) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/gse) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/habo) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/hcm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/iai) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ic) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/icr) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ie) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/iecp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/iir) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ims) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/iot) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/iotcloud) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/iotexplorer) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/iottid) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/iotvideo) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/iotvideoindustry) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ivld) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/kms) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/lighthouse) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/live) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/lowcode) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/lp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/mariadb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/market) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/memcached) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/mgobe) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/mna) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/mongodb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/monitor) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/mps) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/mrs) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ms) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/msp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/mvj) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/nlp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/npp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/oceanus) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ocr) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/organization) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/partners) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/pds) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/postgres) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/privatedns) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/rce) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/redis) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/rkp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/rp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/rum) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/scf) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ses) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/smh) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/smpn) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sms) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/soe) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/solar) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sqlserver) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ssa) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ssl) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sslpod) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ssm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sts) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/taf) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tag) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tat) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tav) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tbaas) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tbm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tbp) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tcaplusdb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tcb) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tcex) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tci) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tcm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tcr) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tcss) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tdcpg) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tdid) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tdmq) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tem) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/teo) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/thpc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tia) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tic) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ticm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tics) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tiems) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tiia) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tione) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tiw) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tke) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tkgdq) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tms) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tmt) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/trtc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tse) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tsf) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tsw) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tts) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ump) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/vm) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/vms) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/vod) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/vpc) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/waf) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/wav) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/wss) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/youmall) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/yunjing) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/yunsou) = %{version}
Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/zj) = %{version}

%description
Go client libraries for Tencent Cloud services, including the shared
authentication, request, response, and client code and all service modules.

%prep -a
# Examples and the separate testing module require live cloud credentials.
rm -rf examples testing

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
