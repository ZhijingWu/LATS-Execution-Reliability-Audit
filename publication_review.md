# Publication review

Reviewed 2026-10-12. Proposed repository: **ZhijingWu/LATS-Execution-Reliability-Audit**. Status: prepared for explicit author approval; no public repository creation or push occurred.

## Claim verification

| Claim | Original sources checked | Verified outcome |
| --- | --- | --- |
| B1: 40 settled requests; 35/45 invalid actions; 32/32 missing complete scores; no purchase | Baseline and failure-attribution reports; private read-only ledger; original event stream; 45 generation and 32 evaluator classifications; pilot outcome record | All counts match. Outcome is a request-limited prefix, with `verified_success=false` and `no_committed_purchase`. |
| B2: six settled requests; 0/15 versus 15/15 compliant; all 15 B outputs think commands | Original B2 report, ledger, event stream and measurements | All counts match; raw completion strings agree with events. No environment execution or navigation command. |
| B3: 12 settled requests; 0/6 versus 6/6 complete scores; 3/6 native agreement; three price-digit mismatches | Original B3 report, ledger, event stream, measurements and payload-comparison record | All counts match. Mismatches at ordinals 4, 6 and 8. Removing `$50` from each privately checked response restores native agreement, verifying the incidental-digit mechanism. |
| B4: 81/81 CPU checks; diagnostic agreement with six explicit scores and three native mismatches | Original B4 report, test JSON, reviewed offline script, independent parser and preserved inputs | The original `--verify-only` suite passed again: 64 synthetic cases + 12 real-response comparisons + five synthesis/boundary checks, zero failures/errors. No inference or environment episode. |
| Child/value alignment exposure; task-success improvement | B1 prefix and B2–B4 experimental scope | **UNESTABLISHED**. B1 did not encounter the mixed terminal/nonterminal frontier; no candidate search or causal outcome comparison was run. |

All five requested reports exist at their recorded `results/` relative paths and were reviewed together with supporting records. The [provenance file](evidence/source_provenance.json) records their SHA256 values and 36 explicitly read source/evidence files. The public package contains new summary prose rather than copies of those private reports.

## Integrity and scope

The original research was accessed through read-only collection and read-only SQLite queries. The reviewed original B4 replay was run with `--verify-only` and bytecode writing disabled; it checks 1,071 protected pre-existing files and performs no evidence writes. The 36 collected file hashes match their original bytes before and after verification. B1–B3 ledger counts remain 40/6/12, all settled. No model inference, training, WebShop episode, upstream edit, or outreach message was performed for publication preparation.

The staging directory is outside the original research workspace. It uses a new independent root Git commit; no source repository Git history is copied. No remote is configured and no force push is performed. Only [explicitly allowlisted files](PUBLICATION_ALLOWLIST.txt) belong in the release.

Pinned LATS and WebShop source/license files match GitHub at the recorded revisions. The public native function has the exact extracted body from `webshop/webshop.py`; the diagnostic parser retains the original B4 behavior. There is no available Git HEAD for the research workspace itself, so research provenance uses file hashes, while upstream provenance uses verified commits.

## Public reproducibility and presentation

The README presents the research question, source attribution, full B1–B4 findings, exact scope, reproduction commands, limitations and contact information. It distinguishes syntax, environment progress, and fidelity to model-written scores; it does not claim evaluator correctness or benchmark gains. Citation metadata passes the official CFF 1.2.0 schema. Relative documentation links are checked before handoff.

Fresh Windows and Linux Python environments pass all 64 public synthetic checks without packages, credentials, network use in the reproduction process, GPU, WebShop, or dataset downloads. The original 81-check real-evidence verification is documented separately. See [reproducibility report](reproducibility_test_report.md).

## Remaining limitations and publication gate

Raw model responses and dataset-bearing prompts are excluded because redistribution permission is not established. The numerical real-observation summaries and file hashes do not enable independent public re-extraction. Public synthetic examples reproduce the source-level mechanism only. This is the declared evidence-access limitation of the proposed package, not a substitute real-data claim.

One task, small purposive frozen prompts, stochastic sampling, completion clustering and uncontrolled provider/backend fields limit generalization. No supported claim of task-success improvement, child/value alignment exposure, or production-parser utility is made. Unclear-permission materials and unrelated projects are excluded. See [license review](license_and_attribution.md) and [security review](security_review.md).

**Stop before GitHub repository creation or public push.** This gate is required by the author's publication-preparation request. Approval applies to the audited manifest and package; a later content change requires renewed checks. After approval, use the designated repository without overwriting or force-pushing existing work, verify public README/reproduction links, and stop after the authorized publication.
