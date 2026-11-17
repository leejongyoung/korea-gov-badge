#!/usr/bin/env python3
"""Optimize logo SVGs in assets/logos with SVGO (multipass, viewBox kept).

Every badge variant inlines the logo, so each logo byte is stored ~80 times under
badges/. Run this on new or replaced logos before `python3 scripts/generate.py`.

  python3 scripts/optimize_logos.py                    # all logos
  python3 scripts/optimize_logos.py assets/logos/x.svg # selected files
  python3 scripts/optimize_logos.py --precision 2 ...  # coarser numbers (check visually)

Requires Node.js (npx downloads svgo@4.1.0 on first use). The result is idempotent.
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGOS_DIR = ROOT / "assets" / "logos"
SVGO_VERSION = "4.1.0"
SVGO_CONFIG = (
    "export default { multipass: true, plugins: [ "
    "{ name: 'preset-default', params: { overrides: { removeViewBox: false } } } ] };\n"
)


def optimize(paths, precision):
    with tempfile.TemporaryDirectory() as tmp:
        config = Path(tmp) / "svgo.config.mjs"
        config.write_text(SVGO_CONFIG, encoding="utf-8")
        before = after = 0
        for path in paths:
            out = Path(tmp) / path.name
            cmd = ["npx", "--yes", f"svgo@{SVGO_VERSION}", "-q", "--config", str(config),
                   f"--precision={precision}", "-i", str(path), "-o", str(out)]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0 or not out.exists():
                print(f"svgo failed for {path}: {result.stderr.strip()}", file=sys.stderr)
                return 1
            old, new = path.stat().st_size, out.stat().st_size
            before += old
            after += min(old, new)
            if new < old:
                path.write_bytes(out.read_bytes())
        print(f"{len(paths)} logos: {before} -> {after} bytes")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", help="SVG files (default: every file in assets/logos)")
    parser.add_argument("--precision", type=int, default=3, choices=(1, 2, 3, 4), help="numeric precision (default 3)")
    args = parser.parse_args()
    paths = [Path(f) for f in args.files] or sorted(LOGOS_DIR.glob("*.svg"))
    if not paths:
        print("no logos found", file=sys.stderr)
        return 1
    return optimize(paths, args.precision)


if __name__ == "__main__":
    raise SystemExit(main())
