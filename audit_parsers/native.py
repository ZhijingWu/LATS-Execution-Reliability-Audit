"""Exact extracted LATS numeric parser; original behavior intentionally retained.

Copyright (c) 2023 Andy Zhou. MIT; see licenses/LATS-MIT.txt.
Source: andyz245/LanguageAgentTreeSearch, commit
853d81614607dd27433faf17c7b0a7d660f95d22, webshop/webshop.py.
The source annotation says str, but its callers supply a list of output strings.
Only the function is extracted; environment imports and surrounding class omitted.
"""

def value_outputs_unwrap(evaluate_prompt: str):
        evaluate_prompt = evaluate_prompt[0]
        if '10' in evaluate_prompt:
            return 1.0
        elif '9' in evaluate_prompt:
            return 0.9
        elif '8' in evaluate_prompt:
            return 0.8
        elif '7' in evaluate_prompt:
            return 0.7
        elif '6' in evaluate_prompt:
            return 0.6
        elif '5' in evaluate_prompt:
            return 0.5
        elif '4' in evaluate_prompt:
            return 0.4
        elif '3' in evaluate_prompt:
            return 0.3
        elif '2' in evaluate_prompt:
            return 0.2
        elif '1' in evaluate_prompt:
            return 0.1
        else:
            return -1
