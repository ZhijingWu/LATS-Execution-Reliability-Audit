# Reproducibility test report

Verified 2026-10-12. The public release uses Python standard-library code only.

## Public clean-environment checks

| Environment | Isolation | Default demonstration | Verbose synthetic suite | File manifest |
| --- | --- | --- | --- | --- |
| Windows, Python 3.13.5 | Fresh venv created without pip; minimal OS process environment, no provider credentials; `-I -B` | PASS, exit 0 | **64/64 PASS**, exit 0 | PASS before final handoff |
| Linux, Python 3.11.2 | Fresh temporary directory and venv created without pip; PATH/UTF-8 locale only, no provider credentials; `-I -B` | PASS, exit 0 | **64/64 PASS**, exit 0 | PASS before final handoff |

The Linux test directory is separate from the research workspace and removed after testing. Both environments receive only public allowlisted files. The runner blocks socket connections and does not import model clients, environment code, GPU libraries or third-party packages. No provider request or dataset download occurs.

Commands, run from the public repository root:

```bash
python -I -B reproduce.py
python -I -B reproduce.py --test --verbose
python -I -B reproduce.py --check-manifest
```

The explicitly **synthetic** demonstration prints native value `0.5` and diagnostic value `0.3` for a reflection containing `$50` and a final score of 3. All 64 archived synthetic expectations pass for native value, diagnostic score, status and normalized value. They cover all scores 1–10, price constraints, incidental digits, accepted formatting variants, missing/nonfinal/conflicting statements and malformed final scores. Case frequencies are constructed test coverage, not empirical model error rates.

`--check-manifest` verifies the exact file allowlist, every listed byte size, all non-manifest SHA256 values, and total size. The manifest's own SHA256 is recorded outside the repository in the local approval summary, because a manifest cannot contain its own hash. Its byte size is included and checked.

## Original real-evidence verification (private)

The preserved original B4 `--verify-only` suite was inspected before execution and rerun with bytecode writes disabled and socket connections forbidden. **81/81 checks passed**, zero failures/errors: 64 synthetic cases, 12 immutable B3 response comparisons, and five synthesis/boundary checks. It opened original SQLite ledgers in read-only mode and passed the preservation check for 1,071 pre-existing files. The B1–B3 ledgers contain exactly 40, 6 and 12 settled attempts.

Separately, collected B1/B2/B3 measurements were compared with their event-stream response strings. Literal explicit scores and native values were re-extracted offline. B3 mismatches at ordinals 4, 6 and 8 disappear when the incidental `$50` substring is removed from each privately reviewed response. No response was changed in the original evidence; removal occurred only in memory for a diagnostic check.

The public native function's AST matches the extracted pinned function body, and the diagnostic parser matches the original B4 parser bytes. Relevant upstream source and license bytes match GitHub at their sealed commits. Citation metadata validates against CFF 1.2.0. Relative Markdown links and the staged diff are checked before handoff.

## Reproduction boundary

Raw real responses are withheld for unresolved redistribution terms. [The public B3 file](evidence/recorded_b3_score_summary.json) contains only derived numerical annotations, not response text. It records six explicit scores, native agreement for three, three price-digit mismatches, and abstention on the other six outputs. Those annotations were verified privately but cannot independently reproduce real-response extraction on a public machine.

The public 64-check suite does not reproduce the entire original 81-check suite, any model inference, navigation, reward improvement, child/value alignment exposure, or the LATS paper's benchmark results. It reproducibly demonstrates the pinned parser mechanism and the diagnostic contract offline.
