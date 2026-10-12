# Security and privacy review

Reviewed 2026-10-12. Outcome: **PASS for the allowlisted publication package**, subject to the author's explicit publication approval. Raw source/evidence material is retained only in private preparation work and does not enter the new repository.

## Reviewed scope and method

Every public working-tree file is enumerated in [PUBLICATION_ALLOWLIST.txt](PUBLICATION_ALLOWLIST.txt) and [the manifest](publication_file_manifest.json). Files are created or copied individually; there is no broad recursive research-directory copy. The native parser function, diagnostic parser, synthetic fixture and two license notices are the only reused textual materials. Evidence files contain numerical annotations, aggregates, relative source identifiers and hashes.

The byte scan checks provider/service key signatures, private-key blocks, authorization values, JWTs, credential assignments, credential-bearing URLs, absolute private paths, private host/infrastructure patterns, provider/session/account metadata fields, email addresses and long opaque tokens. Results record categories and file locations only; matching values are never emitted. SHA256 identifiers are expected provenance content. The only permitted commit email is the explicitly configured GitHub noreply identity for the publication author.

Four long-string heuristic candidates were reviewed and resolved as exact immutable raw GitHub source URLs already verified against the sealed research pins. The exception is restricted to those verified URL spans in the provenance file; no credential-pattern finding is suppressed.

All staged files are also reviewed for account/billing details, private communications, environment secrets, cookies, session identifiers and dataset-derived response text. The UTF-8-only file policy, file allowlist, small-file limits and exact manifest exclude databases, archives, native logs, model assets, large datasets, environment files and unrelated projects. No private report, ledger, raw response JSON, request payload, product page, image or dataset is redistributed.

The staged Git diff is checked before commit. The new history is scanned across every reachable commit's metadata and all tracked blobs using the same privacy checks and exact file allowlist. The history consists of one new root commit with no copied upstream/research history and no configured remote. The final local approval summary records the checked commit and manifest digest.

## Results

- Working-tree and Git index contain exactly the allowlisted files, with no symlink/submodule or unexpected binary.
- Pattern/privacy review reports no unresolved findings in public files or the new history.
- License notices and synthetic fixture content are inspected; no real response text or provider/account/session identifier is released.
- Markdown paths resolve and manifest sizes/hashes match the staged bytes.
- No public push, repository creation, paid inference, environment episode, or message to an external recipient occurred.

Original research files were not modified. The reviewed original B4 read-only suite passed its 1,071-file preservation check, and the 36 collected source/evidence files match their recorded hashes. Public clean-environment tests use only the allowlisted package outside the research workspace.

## Remaining scope limitation

The scan covers the newly prepared package and its new Git history. It is not a remediation audit of the whole private research workspace. Secret-pattern checks are supplemented by content review and exclusion of unnecessary source material; GitHub push protection is not used as the security review. Excluded model responses and dataset material remain subject to their unestablished redistribution terms.
