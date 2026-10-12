"""Archived synthetic expectations, separate from real observation metadata."""
import json
from pathlib import Path
import unittest

from audit_parsers.native import value_outputs_unwrap
from audit_parsers.strict import parse_final_score

ROOT = Path(__file__).resolve().parents[1]

def load_tests(loader, tests, pattern):
    data = json.loads((ROOT / 'fixtures/synthetic_parser_cases.json').read_text(encoding='utf-8'))
    if data['evidence_kind'] != 'synthetic_unit_tests':
        raise ValueError('Fixture kind must be explicit')
    suite = unittest.TestSuite()
    for case in data['cases']:
        def check(case=case):
            if case['synthetic'] is not True:
                raise ValueError('Non-synthetic text cannot enter this suite')
            result = parse_final_score(case['text'])
            expected = case['expected_score']
            assert result['score'] == expected, case['id']
            assert result['status'] == case['expected_status'], case['id']
            assert result['normalized_value'] == (expected / 10 if expected is not None else None), case['id']
            assert value_outputs_unwrap([case['text']]) == case['expected_native_value'], case['id']
            assert result['diagnostic_only'] and not result['decision_values_modified'], case['id']
        suite.addTest(unittest.FunctionTestCase(check, description='synthetic:' + case['id']))
    return suite
