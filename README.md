# LATS Execution Reliability Audit

An independent audit by [Zhijing Wu](https://github.com/ZhijingWu) of action syntax, evaluator output completion, and numerical value extraction in a recorded LATS/WebShop scenario.

**A complete evaluator score can still be read incorrectly:** in three of six complete recorded responses, the native parser returned `0.5` because it matched the `5` in `$50`, rather than the final score. The public offline reproduction demonstrates this source behavior with explicitly synthetic fixtures.

## Research question

When a language agent uses generated text as executable actions and search values, do those interfaces preserve the intended command and score? This audit separates three prerequisites: syntax compliance, environment progress, and fidelity to the model-written score. A pass at one interface does not establish a pass at the next.

The underlying method is **Language Agent Tree Search (LATS)** by Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang ([ICML 2024 paper](https://proceedings.mlr.press/v235/zhou24r.html), [official code](https://github.com/andyz245/LanguageAgentTreeSearch)). The paper's historical `lapisrocks` repository URL currently redirects to this official repository. The environment is [Princeton NLP WebShop](https://github.com/princeton-nlp/WebShop).

This repository contains an independent diagnostic audit. It is not affiliated with, endorsed by, or maintained by the LATS or WebShop authors. It does not reproduce the paper's benchmark results or propose a validated search-performance improvement.

## Recorded results

| Stage | Evidence and design | Verified finding | Interpretation boundary |
| --- | --- | --- | --- |
| **B1: baseline evidence** | One real `fixed_0` baseline prefix; **40 settled requests** | **35/45** generated actions invalid; **32/32** evaluator outputs lacked complete scores; **no successful purchase** | Request ceiling interrupted the first rollout before a completed backup; not a completed benchmark run |
| **B2: frozen-prompt intervention** | One recorded generation prompt; 3 requests per condition, 5 completions per request; **6 settled requests** | Original prompt **0/15** syntax-compliant; format instruction **15/15**; all 15 were `think[...]` | No navigation command or environment episode; syntax compliance does not establish task competence |
| **B3: frozen-prompt intervention** | Three recorded evaluator prompts; 2 repetitions per prompt and cap; **12 settled requests** | 100-token cap **0/6** complete scores; 300-token cap **6/6**; native parser agreed with **3/6** complete scores | All three mismatches traced to the digit `5` in `$50`; no search, children, branch selection, or environment episode |
| **B4: offline verification** | **81/81 CPU checks passed**: 64 synthetic cases, 12 recorded-response comparisons, 5 synthesis/boundary checks | Independent diagnostic extracted **6/6** complete scores, abstained on **6/6** scoreless outputs, and reproduced the three native mismatches | No additional model inference or environment episode; readout agreement does not validate the model's shopping judgment |

The original 81-check suite passed again during publication preparation. The **public suite has 64 synthetic checks**, because raw real responses are withheld. Real numerical annotations appear in [the B3 summary](evidence/recorded_b3_score_summary.json), and aggregate counts appear in [verified findings](evidence/verified_findings.json). These metadata summaries are not substitutes for raw responses.

**Child/value alignment exposure and task-success improvement remain UNESTABLISHED.** They are future hypotheses, not findings of B1–B4. No paid experiment, training, or environment episode was run for this publication package.

## Exact experimental scope

- Recorded task: one blue-toothbrush/oral-hygiene task with a price constraint below $50 (`fixed_0`), in an indexed 1,000-product subset with 13 annotated goals; environment seed 233.
- Prior B1–B3 requests used API2D-reported `gpt-4.1-2025-04-14`, temperature 1.0 and top_p 1.0, without a provider seed. Proxy identifiers do not independently certify backend weights or transformations.
- B1 retained the original prompts, native score parser and search decisions: at most 30 iterations, 5 generation samples (10 at the root), 1 evaluation sample, local seed 17, and a 100-token completion cap. The 40-request ceiling stopped the observed prefix.
- B2 used the frozen generation prompt from B1 attempt 4. The only intentional payload change was a command-format instruction prefix; the schedule was A/B/B/A/A/B. Its 15 completions per condition are clustered within three requests.
- B3 used evaluator prompts from B1 attempts 2, 5 and 8. The only intentional payload change was `max_tokens=100` versus `300`, with two fresh samples per cell and balanced condition order. The longer responses are independent samples, not continuations of shorter responses.
- B4 used preserved responses and controlled synthetic cases, without substituting the diagnostic parser into search.

## Offline reproduction

Requires **Python 3.10+** and its standard library. CPU only; no package installation, credentials, inference, WebShop server, GPU, or dataset download. Download this repository, open its root directory, and run:

```bash
python -I -B reproduce.py
python -I -B reproduce.py --test --verbose
python -I -B reproduce.py --check-manifest
```

On systems where the executable is named `python3`, substitute `python3` for `python`. `-I` isolates Python from user packages/environment settings, and `-B` prevents bytecode artifacts. The runner disables socket connections. These commands are checked in fresh isolated Windows and Linux Python environments.

The first command shows a **synthetic** reflection mentioning `$50` and ending with `Thus the correctness score is 3`. The exact extracted native parser returns `0.5`; the B4 diagnostic returns `0.3`. It then runs the 64 synthetic checks. The second command shows each synthetic check; the third checks every public file against the allowlist, sizes and SHA256 values.

The [synthetic fixture](fixtures/synthetic_parser_cases.json) tests price digits, identifiers, incidental numbers, missing/nonfinal/conflicting scores, and malformed final statements. **Every text in that fixture is synthetic.** It demonstrates deterministic parser behavior and does not independently reproduce the original real-model observations. Raw responses, prompts containing dataset material, and private logs/ledgers are excluded because their redistribution terms have not been established.

The [native parser](audit_parsers/native.py) preserves the pinned function body: search for `10`, then `9` down to `1` anywhere in the first output string, or return `-1`. The [diagnostic parser](audit_parsers/strict.py) accepts a whole final nonempty line of the form `Thus the correctness score is N` for ASCII integer N in 1–10, with case/space variations and one optional period. It abstains on malformed, nonfinal, or conflicting scores. This narrow contract can reject valid semantic judgments in other formats; it is diagnostic code, not an evaluated production search fix.

## Provenance and licenses

| Source | Verified revision | Relevant SHA256 |
| --- | --- | --- |
| LATS | [`853d81614607dd27433faf17c7b0a7d660f95d22`](https://github.com/andyz245/LanguageAgentTreeSearch/tree/853d81614607dd27433faf17c7b0a7d660f95d22) | `webshop/webshop.py`: `fa582e8838557bc553f43e39c437655b7c0105c9e7b7de30fd27e5fda185d210` |
| LATS execution source | Same revision | `webshop/lats.py`: `8139c8bf9176201d893529125712a842465c2b80607f8f71e8cf9180e0786490` |
| WebShop | [`64fa2a5c15c7daa698b9ac93f5bb5437b634c9bd`](https://github.com/princeton-nlp/WebShop/tree/64fa2a5c15c7daa698b9ac93f5bb5437b634c9bd) | `LICENSE.md`: `8872dbf8660b00890b5e07ce1ea1f7a44fa7ae4e1857da56caba172b51dab3cb` |

Pinned source files and notices were checked byte-for-byte against GitHub. [Source provenance](evidence/source_provenance.json) includes hashes of the original reports, configurations and supporting evidence; private-source relative paths there are provenance identifiers, not public download links. The research workspace has no available Git HEAD, so research files are identified by hashes rather than an invented research commit. Original Git history is not included.

Audit code and original documentation use [MIT](LICENSE). The extracted LATS function retains [Andy Zhou's MIT notice](licenses/LATS-MIT.txt). The [WebShop MIT notice](licenses/WebShop-MIT.txt) is retained for attribution; no WebShop implementation or dataset is redistributed. See [license and attribution review](license_and_attribution.md) and [CITATION.cff](CITATION.cff).

## Limitations and threats to validity

This is one task and its purposively selected frozen prompts, with a small catalog and stochastic sampling. Rates describe the recorded sample, not benchmark-wide prevalence. B2 fingerprint sets differed between conditions; B3 fingerprint frequencies differed, with a within-prompt backend-field difference for one prompt. Those fields cannot separate all backend variation from the intentional intervention.

More complete scores do not establish accurate values or better decisions. One 300-token-condition response used only 95 tokens, so 300 is not established as a universally necessary minimum or guaranteed sufficient maximum. The diagnostic parser has not been evaluated inside an agent or on task outcomes. The baseline contained no observed mixed terminal/nonterminal frontier; child/value alignment exposure was absent, and a benefit from correcting it remains unestablished.

The withheld raw responses prevent independent public re-extraction of the original real observations. Publication preparation verified them privately; public synthetic cases support only the source-level mechanism. Hashes aid integrity tracing but do not remove that evidence-access limitation.

## Review and contact

[Publication review](publication_review.md), [security review](security_review.md), [reproducibility test report](reproducibility_test_report.md), and [file manifest](publication_file_manifest.json) document the checks completed during publication preparation.

Author/contact: **Zhijing Wu**, [GitHub profile](https://github.com/ZhijingWu). Please cite this independent audit separately from the original LATS method. No outreach message has been sent as part of this preparation.
