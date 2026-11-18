"""Guard the full requested scope and prevent structural checks posing as CI review."""
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPE = set('kepco kogas khnp kdhc iia kac bpa ipa ygpa upa high1 lh korail ex kwater komsco reb hug kra komir nia kisa kdata nipa kocca nhis hira nps kcomwel kodit kibo kotra kca kto keco kist etri kari kaeri kribb kriss krict kawf seoul-energy gjf'.split())

class MarkedAuditTests(unittest.TestCase):
    def test_full_scope_and_evidence_integrity(self):
        rows = json.loads((ROOT / 'docs/ci-marked-audit-20261119.json').read_text())['items']
        self.assertEqual(len(rows), 45)
        self.assertEqual({x['id'] for x in rows}, SCOPE)
        agencies = {x['id']: x for x in json.loads((ROOT / 'agencies.json').read_text())}
        for row in rows:
            with self.subTest(id=row['id']):
                self.assertEqual(row['registered'], row['id'] in agencies)
                if row['logo_file']:
                    self.assertEqual(hashlib.sha256((ROOT / row['logo_file']).read_bytes()).hexdigest(), row['logo_sha256'])
                    self.assertGreater(row['drawing_elements'], 0)
                if row['complete']:
                    self.assertEqual(row['official_shape_colour_ci_bi_complete_symbol_review'], 'verified')
                    self.assertEqual(row['render_comparison'], 'verified')
                    self.assertTrue(row['source_url'])
                    self.assertTrue(row['recorded_original_sha256'])
                    self.assertTrue(row['registered'])

    def test_official_web_palettes_and_unchanged_geometry(self):
        rows = json.loads((ROOT / 'docs/ci-first-five/web-colours.json').read_text())
        self.assertEqual(len(rows), 5)
        for row in rows:
            svg = (ROOT / f"assets/logos/{row['id']}.svg").read_text()
            self.assertEqual(set(re.findall(r'#[0-9a-f]{6}', svg)), set(row['expected_palette']))
            self.assertEqual(hashlib.sha256('\n'.join(re.findall(r'<path[^>]* d="([^"]+)"', svg)).encode()).hexdigest(), row['baseline_path_sha256'])
            self.assertEqual(hashlib.sha256(svg.encode()).hexdigest(), row['svg_sha256'])
            for name, digest in row['evidence_files'].items():
                self.assertEqual(hashlib.sha256((ROOT / 'docs/ci-first-five/web-colour-evidence' / name).read_bytes()).hexdigest(), digest)
        self.assertEqual(len(next(x for x in rows if x['id'] == 'krict')['expected_palette']), 9)

    def test_extraction_metadata_and_embedded_notice_match_current_assets(self):
        import xml.etree.ElementTree as ET
        agencies = {a['id']: a for a in json.loads((ROOT / 'agencies.json').read_text())}
        sources = {s['id']: s for s in json.loads((ROOT / 'docs/logo-sources.json').read_text())['items']}
        for row in json.loads((ROOT / 'docs/ci-first-five/extraction.json').read_text()):
            id_ = row['id']
            with self.subTest(id=id_):
                asset = ROOT / 'assets/logos' / (id_ + '.svg')
                self.assertEqual(hashlib.sha256(asset.read_bytes()).hexdigest(), row['svg_sha256'])
                for directory in (id_, agencies[id_]['name']):
                    paths = list((ROOT / 'badges' / directory).glob('*.svg'))
                    self.assertEqual(len(paths), 40)
                    for p in paths:
                        credits = ''.join(n.text or '' for n in ET.parse(p).getroot().iter()
                                          if n.tag.endswith('}desc'))
                        self.assertIn(sources[id_]['source_page'], credits)
                        self.assertIn('재배포 허락 미확인', credits)
