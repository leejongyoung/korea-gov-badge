"""Use painted path witnesses, not viewBox width, to guard brand minimum."""
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
NS = {'s': 'http://www.w3.org/2000/svg'}

class KrictMinimumTests(unittest.TestCase):
    def test_all_80_painted_bounds(self):
        files = list((ROOT / 'badges/krict').glob('*.svg')) + list((ROOT / 'badges/한국화학연구원').glob('*.svg'))
        self.assertEqual(len(files), 80)
        for p in files:
            with self.subTest(path=str(p)):
                root = ET.parse(p).getroot()
                group = next(g for g in root.findall('s:g', NS) if 'transform' in g.attrib)
                tx, ty, scale = map(float, re.findall(r'-?\d+\.?\d*', group.get('transform')))
                paths = group.findall('s:path', NS)
                # Two actual filled boundary endpoints, unaffected by viewBox padding.
                d = ' '.join(x.get('d') for x in paths)
                self.assertIn('842.4563 99.85929', d)
                self.assertIn('L22.93039 230.36118', d)
                self.assertGreaterEqual((842.4563 - 22.93039) * scale, 57)
                # Control hull encloses all cubic curves (no viewBox-only inference).
                points = [list(map(float, re.findall(r'-?\d+(?:\.\d+)?', x.get('d')))) for x in paths]
                xs = [v for pts in points for v in pts[::2]]
                ys = [v for pts in points for v in pts[1::2]]
                self.assertGreaterEqual(tx + min(xs)*scale, 3)
                self.assertGreaterEqual(ty + min(ys)*scale, 2.9)
                self.assertLessEqual(ty + max(ys)*scale, float(root.get('height'))-2.9)
                text = root.find('s:text', NS)
                self.assertLessEqual(tx + max(xs)*scale + 5.9, float(text.get('x')))
