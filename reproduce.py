"""No-dependency offline synthetic parser reproduction (Python 3.10+)."""
import argparse
import hashlib
import json
from pathlib import Path
import socket
import sys
import unittest

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

def forbidden_network(*args, **kwargs):
    raise RuntimeError('This reproduction is offline; socket connections are disabled')

socket.create_connection = forbidden_network
socket.socket.connect = forbidden_network
socket.socket.connect_ex = forbidden_network

from audit_parsers.native import value_outputs_unwrap
from audit_parsers.strict import parse_final_score

def check_manifest():
    manifest = json.loads((ROOT / 'publication_file_manifest.json').read_text(encoding='utf-8'))
    listed = {entry['path'] for entry in manifest['files']}
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
              and '.git' not in p.relative_to(ROOT).parts}
    if actual != listed:
        raise RuntimeError('Manifest file allowlist differs from working tree')
    total = 0
    for entry in manifest['files']:
        path = ROOT / entry['path']
        if not path.resolve().is_relative_to(ROOT.resolve()):
            raise RuntimeError('Manifest path escapes repository')
        content = path.read_bytes()
        total += len(content)
        if len(content) != entry['bytes']:
            raise RuntimeError('Manifest size mismatch: ' + entry['path'])
        if entry['sha256'] is not None and hashlib.sha256(content).hexdigest() != entry['sha256']:
            raise RuntimeError('Manifest SHA256 mismatch: ' + entry['path'])
    if len(listed) != manifest['file_count'] or total != manifest['total_bytes']:
        raise RuntimeError('Manifest totals mismatch')
    print('Manifest PASS: ' + str(len(listed)) + ' allowlisted files; ' + str(total) + ' bytes')

def run_tests(verbose=False):
    suite = unittest.defaultTestLoader.discover(str(ROOT / 'tests'), pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2 if verbose else 1).run(suite)
    if result.testsRun != 64 or not result.wasSuccessful():
        raise SystemExit(1)
    print('Synthetic CPU checks: 64/64 PASS. No real-response texts are included.')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--test', action='store_true', help='run the 64 synthetic CPU checks')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--check-manifest', action='store_true', help='check release allowlist, sizes and hashes')
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error('Do not use -O: the archived test checks use assertions')
    if args.check_manifest:
        check_manifest()
    if args.test:
        run_tests(args.verbose)
    if not args.test and not args.check_manifest:
        print('SYNTHETIC illustration (not a real model response):')
        text = 'Reflection: Price lower than $50.\nThus the correctness score is 3'
        print(text)
        print('Native value:', value_outputs_unwrap([text]))
        print('Diagnostic value:', parse_final_score(text)['normalized_value'])
        run_tests()

if __name__ == '__main__':
    main()
