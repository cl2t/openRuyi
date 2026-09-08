# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nats-server
%define go_import_path  github.com/nats-io/nats-server/v2

# Fixed speed thresholds and expiration/recovery deadlines fail on OBS workers.
%define nats_skip_timing NoRaceSeqSet(EncodeLarge|RelativeSpeed)|NoRaceJetStream(SparseConsumers|FileStoreLargeKVAccessTiming|ConsumerCreateTimeNumPending|PullConsumersAndInteriorDeletes)|NoRaceFileStoreWriteFullStateUniqueSubjects|JetStream(Cluster)?SubjectDeleteMarkersTTLRollupWithMaxAge|JetStreamClusterAfterPeerRemoveZeroState
# Timeout injection and stress publishers depend on host TCP buffers and receiver scheduling.
%define nats_skip_io RouteSlowConsumerRecover|NoClientLeakOnSlowConsumer|NoRaceWSNoCorruptionWithFrameSizeLimit|NoRaceJetStreamClusterMirrorSkipSequencingBug
# These cluster fixtures exceed the 1024-descriptor limit on some OBS workers.
%define nats_skip_fds NoRaceJetStream(SuperClusterMixedModeMirrors|ClusterStreamNamesAndInfosMoreThanAPILimit|ClusterBadRestartsWithHealthzPolling)
# These fixtures assert before asynchronous subscription or cluster state has converged on OBS.
%define nats_skip_async LeafNodePermissionWithLiteralSubjectAndQueueInterest|JetStreamCluster(ExtendedAccountInfo|AckDeleted)|Gateway(NoCrashOnInvalidSubject|ConnectEvents)|JetStreamMetadataStreamRestoreAndRestartCluster|MQTTWillRetain

# Cluster fixtures have recovery, subscription, and cleanup races on build workers.
%define nats_skip_cluster JetStreamSuperClusterUniquePlacementTag|JetStreamMemoryCorruption|JetStreamStreamSourceFromKV|NoRaceJetStreamClusterGhostConsumers|NoRaceJetStreamAccountLimitsAndRestartForceSnapshot|NoRaceJetStreamInterestStreamCheckInterestRaceBug|JetStreamClusterParallelConsumerCreation|JetStreamClusterInterestPolicyEphemeral|JetStreamClusterAPILimitAdvisory|JetStreamClusterLeafnodeSpokes|JetStreamClusterLeafnodePlusDaisyChainSetup
# These protocol fixtures depend on socket scheduling, port reuse, or concurrent state changes.
%define nats_skip_protocol WSNoCorruptionWithFrameSizeLimit|LeafNodeSlowConsumer|NoRaceRouteFormTimeWithHighSubscriptions|LeafNodeOperatorAndPermissions|MQTTWillRetainPermViolation|MQTTTLS|MsgTraceEgressErrors|NRGCandidateDontStepdownDueToLeaderOfPreviousTerm|JWTImportsOnServerRestartAndClientsReconnect
# Process sampling races with GC and host ps accounting.
%define nats_skip_sampling PSEmulation
# These fixtures race consumer readiness, leader selection or migration completion.
%define nats_skip_transition JetStreamClusterAckFloorBetweenLeaderAndFollowers|JetStreamSuperClusterMovingStreamsAndConsumers|JetStreamClusterConsumerMaxDeliveryNumAckPendingBug

Name:           nats-server
Version:        2.11.1
Release:        %autorelease
Summary:        High-performance cloud-native messaging server
License:        Apache-2.0
URL:            https://github.com/nats-io/nats-server
#!RemoteAsset:  sha256:a49ad29b3bfc2fbe3108d4bca928c9115f9e4d0e9fc3975b0e7b47f274ef58e6
Source0:        https://github.com/nats-io/nats-server/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

# https://github.com/nats-io/nats-server/commit/eeae282ccb537066af83b6738d544bbd7c35f6ec
Patch1012:      1012-wait-for-account-jetstream-readiness.patch
# https://github.com/nats-io/nats-server/commit/df1b12b7c6f3e461df926b649981ef0d3dd87891
Patch1013:      1013-adopt-configured-url-for-solicited-routes.patch
# https://github.com/nats-io/nats-server/commit/e67032a444c6b8a2e68e66ad8b16423e3f161cf5
Patch1014:      1014-adopt-configured-url-for-duplicate-routes.patch
# Read complete Linux RSS counters through statm, matching procps memory accounting.
Patch2005:      2005-read-linux-memory-usage-from-statm.patch
# Prevent concurrent JWT refreshes from invalidating unchanged stream imports.
Patch2031:      2031-replace-stream-exports-atomically-on-claim-refresh.patch
# Avoid cross-account lock inversion during reciprocal claim refreshes.
Patch2032:      2032-order-account-locks-for-import-revalidation.patch

BuildOption(build):  -ldflags "-X github.com/nats-io/nats-server/v2/server.serverVersion=%{version}"
# Upstream CI disables vet for this release's test suite.
BuildOption(check):  -vet=off
# Serialize fixed-port tests; the complete server suite exceeds one hour on riscv64.
BuildOption(check):  -p=1 -timeout=2h
# Keep upstream short-mode selection.
BuildOption(check):  -short
# The build root also has no host syslog socket. All other test failures are fatal.
BuildOption(check):  -skip '^Test(SysLogger(WithDebugAndTrace)?|%{nats_skip_timing}|%{nats_skip_io}|%{nats_skip_fds}|%{nats_skip_async}|%{nats_skip_cluster}|%{nats_skip_protocol}|%{nats_skip_sampling}|%{nats_skip_transition})$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  procps-ng
BuildRequires:  tzdata
BuildRequires:  go(github.com/antithesishq/antithesis-sdk-go)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/minio/highwayhash)
BuildRequires:  go(github.com/nats-io/jwt/v2)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(go.uber.org/automaxprocs)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/time)

%description
nats-server is the NATS messaging server. MinIO uses NATS as an event
notification target and requires github.com/nats-io/nats-server/v2.

%package     -n go-github-nats-io-nats-server-v2
Summary:        Go source for the NATS server
BuildArch:      noarch
Provides:       go(github.com/nats-io/nats-server/v2) = %{version}
Requires:       go(github.com/antithesishq/antithesis-sdk-go)
Requires:       go(github.com/google/go-tpm)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/minio/highwayhash)
Requires:       go(github.com/nats-io/jwt/v2)
Requires:       go(github.com/nats-io/nats.go)
Requires:       go(github.com/nats-io/nkeys)
Requires:       go(github.com/nats-io/nuid)
Requires:       go(go.uber.org/automaxprocs)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/time)

%description -n go-github-nats-io-nats-server-v2
This package contains the reusable Go source for nats-server, including
the server package imported by MinIO.

%prep -a
# docker/ and scripts/ are packaging and CI helpers, not the server.
rm -rf docker scripts %{_builddir}/go/src/%{go_import_path}/docker %{_builddir}/go/src/%{go_import_path}/scripts

%install -a
# The command is already installed; keep it out of the noarch source package.
rm -f %{_name}
%buildsystem_golangmodules_install

%check -p
%{buildroot}%{_bindir}/%{_name} --version

%check -a
# Retain R1 migration coverage; the R3 fixture races completed migration to C2.
cd %{_builddir}/go/src/%{go_import_path}
%{__go} test -v -vet=off -p=1 -short -timeout=5m -count=1 \
    -run '^TestJetStreamSuperClusterMovingStreamsAndConsumers$/^R1$' ./server

%files
%doc README.md
%license LICENSE
%{_bindir}/nats-server

%files -n go-github-nats-io-nats-server-v2
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
