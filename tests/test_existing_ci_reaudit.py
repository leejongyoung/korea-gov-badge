"""Keep official-source corrections distinct from a blanket CI clearance."""
import hashlib
import gzip
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'docs/existing-ci-reaudit'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def drawing_tree(node):
    """Compare vector geometry/paint, ignoring only attribution descriptions."""
    return (node.tag, sorted(node.attrib.items()),
            [drawing_tree(c) for c in node if not c.tag.endswith('}desc')])


class ExistingCIReauditTests(unittest.TestCase):
    def test_normalization_preserves_original_download_bytes(self):
        sources = {x['id']: x for x in json.loads((ROOT / 'docs/logo-sources.json').read_text())['items']}
        ids = {'kepco-signature.svg': 'kepco', 'bpa-official-0.svg': 'bpa'}
        for row in json.loads((EVIDENCE / 'source-normalization.json').read_text()):
            raw = gzip.decompress((EVIDENCE / row['raw_archive']).read_bytes())
            normalized = (EVIDENCE / row['normalized_file']).read_bytes()
            self.assertEqual(digest(raw), row['raw_payload_sha256'])
            self.assertEqual(digest(raw), sources[ids[row['normalized_file']]]['original_sha256'])
            self.assertEqual(digest(normalized), row['normalized_sha256'])
            self.assertEqual(normalized, raw.replace(b'\r\n', b'\n'))

    def test_current_official_web_artwork_not_retraced(self):
        for id_, original in [('kepco', 'kepco-signature.svg'),
                              ('bpa', 'bpa-official-0.svg')]:
            with self.subTest(id=id_):
                self.assertEqual(drawing_tree(ET.parse(ROOT / f'assets/logos/{id_}.svg').getroot()),
                                 drawing_tree(ET.parse(EVIDENCE / original).getroot()))

    def test_colours_follow_named_official_values_without_geometry_edits(self):
        proof = {x['id']: x for x in json.loads((EVIDENCE / 'corrections.json').read_text())}
        for x in json.loads((EVIDENCE / 'colour-corrections.json').read_text()):
            id_ = x['id']
            with self.subTest(id=id_):
                svg = (ROOT / f'assets/logos/{id_}.svg').read_text()
                self.assertEqual(digest(svg.encode()), x['svg_sha256'])
                self.assertEqual(digest((EVIDENCE / x['evidence_file']).read_bytes()), x['evidence_sha256'])
                self.assertEqual(proof[id_]['path_sha256'], proof[id_]['old_path_sha256'])
                for old, new in x['mapping'].items():
                    self.assertNotIn(old, svg.lower())
                    self.assertIn(new, svg.lower())
        korail = (ROOT / 'assets/logos/korail.svg').read_text()
        self.assertEqual(set(re.findall(r'#[0-9a-f]{6}', korail)), {'#005bac', '#00b2e3'})
        self.assertEqual(proof['korail']['path_sha256'], proof['korail']['old_path_sha256'])
        self.assertEqual(ET.fromstring(korail).get('data-min-icon-size'), '20')

    def test_every_corrected_badge_contains_its_own_artwork_and_notice(self):
        from scripts.generate import load_logos
        logos = load_logos()
        agencies = {a['id']: a for a in json.loads((ROOT / 'agencies.json').read_text())}
        for row in json.loads((EVIDENCE / 'corrections.json').read_text()):
            id_ = row['id']
            asset = ROOT / f'assets/logos/{id_}.svg'
            self.assertEqual(digest(asset.read_bytes()), row['svg_sha256'])
            for directory in [id_, agencies[id_]['name']]:
                files = list((ROOT / 'badges' / directory).glob('*.svg'))
                self.assertEqual(len(files), 40)
                for file in files:
                    with self.subTest(path=file):
                        self.assertIn(logos[id_][4], file.read_text())
                        root = ET.parse(file).getroot()
                        self.assertTrue(any(n.tag.endswith('}desc') for n in root.iter()))

    def test_unresolved_findings_cannot_be_reported_as_full_clearance(self):
        audit = json.loads((EVIDENCE / 'review-21.json').read_text())
        self.assertEqual(len(audit['items']), 21)
        self.assertFalse(audit['full_accuracy_audit_complete'])
        self.assertTrue(audit['new_implementations_on_hold'])
        self.assertEqual(set(audit['corrections_in_this_batch']), {'kepco', 'bpa', 'korail', 'kisa', 'kto'})
        for id_ in ['seoul-energy', 'ygpa']:
            row = next(x for x in audit['items'] if x['id'] == id_)
            self.assertFalse(row['complete'])
            self.assertIn('OPEN', row['palette_status'])
        for row in audit['items']:
            self.assertEqual(digest((ROOT / f"assets/logos/{row['id']}.svg").read_bytes()), row['svg_sha256'])

    def test_browser_measurements_cover_current_21_by_80_badges(self):
        rows = json.loads((EVIDENCE / 'all-21-measurements.json').read_text())
        self.assertEqual(len(rows), 1680)
        self.assertEqual(len({x['path'] for x in rows}), 1680)
        for x in rows:
            with self.subTest(path=x['path']):
                self.assertEqual(digest((ROOT / x['path']).read_bytes()), x['badge_sha256'])
                self.assertGreaterEqual(x['left'], -.1)
                self.assertGreaterEqual(x['top'], -.1)
                self.assertLessEqual(x['bottom'], x['badge_height'] + .1)
                self.assertLessEqual(x['right'], x['label_x'] + .1)
                if '/korail/' in x['path'] or '/한국철도공사/' in x['path']:
                    self.assertGreaterEqual(x['painted_width'], 20 * 96 / 25.4)


if __name__ == '__main__':
    unittest.main()
