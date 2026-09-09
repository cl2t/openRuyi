# Pinned MinIO Console frontend packaging draft

Build the Console commit `2017f33b26e1cb632dd208ab7d91add1d06990fd`, as pinned by MinIO RELEASE.2025-10-15T17-29-55Z. This package installs static assets under `/usr/share/minio-console-frontend`, with a verification manifest in `/usr/share/minio-console-frontend-build-info`. It does not provide an HTTP service or Go backend.

## Reproduce source inputs

Use Python 3.12 or newer, Node.js and Git, with network access during source preparation. These commands use fresh directories; neither generator overwrites an existing directory. The RPM build runs with network access disabled in Yarn and Cargo.

```sh
python3 prepare-inputs.py /tmp/console-js-inputs --spec-dir "$PWD"
python3 prepare-rust-inputs.py /tmp/console-rust-inputs
cp /tmp/console-js-inputs/frontend-offline-inputs.tar.gz .
cp /tmp/console-rust-inputs/rollup-cargo-sources.tar.gz .
```

Do not add these generated archives to the openRuyi Git repository. The final Source2 and Source9 still need maintained release URLs before this draft is ready for submission. [A separate frontend generator](https://github.com/software-vendor/go-minio-vendor/pull/1) is proposed in the existing source-archive repository. Its [Ubuntu workflow](https://github.com/cl2t/go-minio-vendor/actions/runs/35453960311) reproduced both archive checksums. The official frontend release has not been published; the current contributor account has no write permission there.

The generators normalize tar ownership, permissions and timestamps, and gzip timestamps. Every JavaScript cache ZIP is checked against `input-manifest.json`, in addition to Yarn's immutable lockfile checks. All 338 Rust source crates are checked against the two upstream Cargo.lock files before generating Cargo's directory-source checksums.

Expected generated archives:

- `frontend-offline-inputs.tar.gz`: 100387864 bytes; SHA-256 `d86c91b349680a9c5778b7967405f3d5888339d7b3367a6c51873742b3c2a85f`.
- `rollup-cargo-sources.tar.gz`: 35779260 bytes; SHA-256 `4ca45ce427a098f4108db1513c60e9ad9d9be312ea6842bdce298415e223ef6b`.

## Source provenance and changes

Console comes from miniohq/object-browser. MDS v1.1.5 is the exact commit `400914d72cb3ffa27d600e0ae1f17ece2182ec22`, retained in the original author's bexsoft/mds repository after the minio/mds URL disappeared. This is an explicitly different archive location, not an official MinIO redirect. Freshly fetching and packing that Git commit yields the original Console yarn.lock SHA-512 checksum:

```
31c92b4d86e5de5313d2db37f2e2a54fe639271cd146f7be6ce38839b68934d1513a4abb44f0f906aca74e1ae388fa3afea20e548630fee24a9348fa8580dd77
```

The two local patches preserve every production dependency and all application TypeScript/React sources. They remove unused Storybook, audit, code-generator and browser-E2E development tools from the isolated build manifests. The MDS patch also adds its missing testing-library DOM peer, enables CommonJS interop in Jest, and bounds minifier workers. All four upstream Button assertions are preserved.

The input generator creates a private Git wrapper to normalize Yarn 4.9.4's malformed single `-c key=value` argument into two arguments. It does not change repository selection, commit selection or any other arguments. The MDS URL rewrite is scoped to the generator's process environment. Yarn's global mirror is disabled and its global folder is isolated.

The caches retain 1,932 ZIPs. This is a source input count, not a request for 1,932 RPMs. Optional native platform modules are not installed. The one remaining fsevents ZIP is needed to resolve Yarn's compatibility patch, but its Darwin native payload is neither installed nor executed on Linux. Before inserting source-built Rollup modules, the build rejects any installed `.node` file. Rollup 4.46.1 and 4.27.3 are compiled with the distribution Rust/C toolchain. Both MDS's original dist and Console's original build directories are deleted before compilation.

## Notices and tests

The runtime assets include notices for installed build dependencies, Console, MDS and the Inter 3.19 fonts. All 38 font files were verified against the official Inter release. once 1.1.2 omitted its MIT text; the preserved notice is explicitly from upstream's later license-addition commit de4a704b54936d83c8d6347d28665fe3b66c6de6. The notice inventory includes README fallbacks; its presence count is not a claim of a complete legal audit.

The spec runs the four upstream MDS tests and 47 loopback HTTP checks, then verifies every one of the 112 files installed into the RPM against the tested output. Console modifies index.html at runtime, so the separate real-server integration check validates its root element and compares 45 static resources byte-for-byte. That check also exercises Console login/session APIs, signed S3 operations and persistence after a server restart. It uses the official existing Go vendor archive and therefore does not validate the unfinished Go unvendoring work. No full browser E2E test is claimed.

The source-only frontend produces the same executable JavaScript, CSS, HTML and media as the earlier cached-tool experiment. One source map changes four entities source paths because Yarn hoists the dependency after development-tool pruning; its mappings and embedded source contents are unchanged.

## Backend integration

When the Go dependency closure is ready, add a build dependency on this exact frontend snapshot, remove `web-app/build`, and copy `/usr/share/minio-console-frontend/.` there before Console's Go build. The pinned upstream embeds `web-app/build/*`. Copy its installed license notices into the resulting backend RPM as well; embedding the files means the frontend RPM is not necessarily a runtime dependency.

The isolated integration experiment first removes `vendor/github.com/minio/console/web-app/build`, copies this RPM's assets into that directory, verifies all 112 hashes, and compiles MinIO. This demonstrates the integration point while preserving the existing official Go dependency supply. It does not change the official MinIO spec or existing dependency PRs.
