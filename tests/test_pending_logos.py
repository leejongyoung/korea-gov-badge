import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PendingLogoCliTests(unittest.TestCase):
    def check_mutation(self, mutate):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('scripts/check_catalog.py', 'agencies.json',
                         'docs/local-gov-catalog.json', 'docs/local-gov.md',
                         'docs/logo-pending.json', 'docs/logo-sources.json',
                         'docs/public-logo-pending.json', 'docs/public-enterprises.md'):
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, target)
            path = root / 'docs/logo-pending.json'
            data = json.loads(path.read_text(encoding='utf-8'))
            mutate(data)
            path.write_text(json.dumps(data), encoding='utf-8')
            return subprocess.run(
                [sys.executable, str(root / 'scripts/check_catalog.py'), '--check'],
                capture_output=True, text=True, check=False,
            )

    def test_duplicate_pending_id_fails_real_catalogue_cli(self):
        result = self.check_mutation(lambda d: d['items'].append(dict(d['items'][0])))
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('duplicate pending logo id', result.stdout)

    def test_pending_coverage_matches_unimplemented_municipalities(self):
        for mutate in (lambda d: d['items'].pop(),
                       lambda d: d['items'][0].update(id='chungbuk-jincheon')):
            with self.subTest(mutate=mutate):
                result = self.check_mutation(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn('pending logo coverage differs', result.stdout)

    def test_reviewed_records_require_dated_source_and_explanation(self):
        for field, value in (('checked_on', ''), ('checked_on', '2026-02-30'),
                             ('official_source', ''), ('official_source', 'not-a-url'),
                             ('note', '')):
            def mutate(data):
                data['items'][0][field] = value
            with self.subTest(field=field, value=value):
                result = self.check_mutation(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn('review evidence incomplete', result.stdout)


if __name__ == '__main__':
    unittest.main()
