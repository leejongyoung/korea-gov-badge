#!/usr/bin/env bash
# 대용량 로고 SVG를 SVGO로 최적화한다. (Node 필요, 결과는 반드시 육안/렌더 비교 후 커밋)
# 사용: scripts/optimize_logos.sh [파일...]  (인자 없으면 20KB 초과 로고 전체)
set -euo pipefail
cd "$(dirname "$0")/.."
if [ "$#" -gt 0 ]; then files=("$@"); else files=($(find assets/logos -name '*.svg' -size +20k)); fi
for f in "${files[@]}"; do npx --yes svgo -q --config scripts/svgo.config.cjs "$f" -o "$f"; done
python3 scripts/generate.py
