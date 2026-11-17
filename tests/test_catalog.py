import copy
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('check_catalog', ROOT / 'scripts/check_catalog.py')
catalog_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog_check)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads((ROOT / 'docs/local-gov-catalog.json').read_text())
        self.agencies = json.loads((ROOT / 'agencies.json').read_text())

    def test_current_catalogue_and_document_match(self):
        self.assertEqual(catalog_check.validate(self.catalog, self.agencies), [])
        self.assertEqual(catalog_check.render(self.catalog, self.agencies), (ROOT / 'docs/local-gov.md').read_text())

    def test_invalid_coverage_is_not_reported_as_implemented(self):
        row = next(r for r in self.catalog['municipalities'] if r['badge_status'] == 'pending_logo')
        row['badge_status'] = 'available'
        self.assertTrue(any('stale badge status' in p for p in catalog_check.validate(self.catalog, self.agencies)))

    def test_duplicate_or_wrong_parent_is_rejected(self):
        original = copy.deepcopy(self.catalog)
        self.catalog['municipalities'][1] = copy.deepcopy(self.catalog['municipalities'][0])
        self.assertTrue(any('duplicate municipality' in p for p in catalog_check.validate(self.catalog, self.agencies)))
        original['municipalities'][0]['parent'] = 'jeonnam'
        self.assertTrue(any('invalid parent' in p for p in catalog_check.validate(original, self.agencies)))

    def test_public_logo_backlog_matches_catalogue_not_supported_agencies(self):
        import re
        text = (ROOT / 'docs/public-enterprises.md').read_text()
        candidate_ids = set()
        for line in text.splitlines():
            if line.startswith('| **'):
                cells = line.strip('|').split('|')
                candidate_ids.update(re.findall('`([^`]+)`', cells[2]))
        pending = json.loads((ROOT / 'docs/public-logo-pending.json').read_text())['items']
        ids = [row['id'] for row in pending]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), candidate_ids - {a['id'] for a in self.agencies})
        for row in pending:
            if row.get('checked_on'):
                self.assertTrue(row.get('official_source') or row.get('commons_page'))

    def test_incheon_current_districts_and_jeju_exception(self):
        incheon = {r['name'] for r in self.catalog['municipalities'] if r['parent'] == 'incheon'}
        self.assertEqual(incheon, {'제물포구', '영종구', '검단구', '서해구', '미추홀구', '연수구', '남동구', '부평구', '계양구', '강화군', '옹진군'})
        self.assertEqual(len(self.catalog['administrative_cities']), 2)
        self.assertFalse(any(r['parent'] in {'jeju', 'sejong'} for r in self.catalog['municipalities']))

    def test_new_logo_hashes_and_pending_coverage(self):
        sources = json.loads((ROOT / 'docs/logo-sources.json').read_text())
        for source in sources['items']:
            raw = (ROOT / 'assets/logos' / (source['id'] + '.svg')).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), source['logo_sha256'])
            self.assertIn(source['license_as_listed'], {'Public domain', 'KOGL Type 1'})
            if source['license_as_listed'] == 'KOGL Type 1':
                self.assertTrue(source['source_page'].startswith('https://'))
                self.assertIn('공공누리', raw.decode('utf-8'))
        pending = json.loads((ROOT / 'docs/logo-pending.json').read_text())
        # Every pending municipality must remain visible in the implementation backlog.
        entries = pending.get('items', pending.get('municipalities', []))
        self.assertEqual({r['id'] for r in entries}, {r['id'] for r in self.catalog['municipalities'] if r['badge_status'] == 'pending_logo'})


if __name__ == '__main__':
    unittest.main()
