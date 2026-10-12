# License and attribution review

Reviewed 2026-10-12. The independent audit and original LATS method are separate works.

| Material | Review and release decision |
| --- | --- |
| Exact native `value_outputs_unwrap` function | LATS pinned MIT license permits redistribution subject to retaining the notice. Only this function is extracted into `audit_parsers/native.py`; its behavior and annotation are preserved. Original module imports and enclosing class are omitted. `licenses/LATS-MIT.txt` preserves Copyright (c) 2023 Andy Zhou and the full MIT text. |
| B4 diagnostic parser and 64 synthetic cases | Original project-owned audit material; parser copied without behavioral changes, and cases include only labeled synthetic input strings and fixed expectations. Licensed under the repository MIT notice for Zhijing Wu. No model-returned strings enter the synthetic fixture. |
| Aggregate counts and B3 numerical annotations | Derived factual observations from the author's recorded research; include no raw provider responses, IDs, account fields, environment pages, or copied product descriptions. |
| WebShop code | Pinned `LICENSE.md` is MIT, Copyright (c) 2023 Princeton Natural Language Processing. Its exact notice is retained at `licenses/WebShop-MIT.txt`. No implementation is copied. Software licensing does not independently establish rights to all underlying third-party product data. |
| WebShop products, images, instructions, and other datasets | Dataset/third-party redistribution permission is not established for this release. Excluded; no downloads or data bundles are included. The task is described in original summary wording rather than copying a dataset instruction. |
| Raw API2D/model responses | Redistribution permission is not established from the available evidence, and responses can contain dataset-derived text. Excluded. No assumption is made that the upstream software license licenses provider responses. |
| Private reports, configurations, logs, ledgers, environment files | Not copied into the public package. Relative provenance identifiers and SHA256 values are retained. New review prose summarizes the findings without infrastructure/account details. |
| Paper, figures, related projects, model weights | Linked or excluded; no paper PDF, figures, unrelated repositories, training outputs, or model assets are redistributed. |

Pinned LATS and WebShop license bytes and the relevant LATS source files match GitHub at their recorded revisions; exact URLs and hashes are in [source provenance](evidence/source_provenance.json). Licenses were checked at the research pins, not inferred from today's default branch.

Original LATS paper metadata was verified at [PMLR](https://proceedings.mlr.press/v235/zhou24r.html): Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang; ICML 2024, PMLR volume 235, pages 62138–62160. [The official repository](https://github.com/andyz245/LanguageAgentTreeSearch) is the current destination of the paper's historical `lapisrocks` link. [CITATION.cff](CITATION.cff) attributes the audit to Zhijing Wu and references the original paper.

Review outcome: the staged code has identified MIT notices and required attribution. Unclear-permission materials are excluded. Public synthetic tests cannot independently reproduce extraction from withheld real responses. This repository makes no claim of affiliation, endorsement, maintenance by the original authors, or validation of the original paper's benchmark results.
