#!/usr/bin/env python3
"""Validate administrative coverage and its generated catalogue (offline)."""
import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'docs/local-gov-catalog.json'
DOCUMENT = ROOT / 'docs/local-gov.md'
PARENTS = {
    'seoul': '서울특별시', 'busan': '부산광역시', 'daegu': '대구광역시',
    'incheon': '인천광역시', 'daejeon': '대전광역시', 'ulsan': '울산광역시',
    'sejong': '세종특별자치시', 'gyeonggi': '경기도', 'gangwon': '강원특별자치도',
    'chungbuk': '충청북도', 'chungnam': '충청남도', 'jeonbuk': '전북특별자치도',
    'gyeongbuk': '경상북도', 'gyeongnam': '경상남도', 'jeju': '제주특별자치도',
    'jeonnam-gwangju': '전남광주통합특별시',
}


def validate(catalog, agencies):
    problems = []
    rows = catalog['municipalities']
    ids = [r['id'] for r in rows]
    if len(ids) != len(set(ids)):
        problems.append('duplicate municipality id')
    if len(rows) != catalog['counts']['municipal']:
        problems.append('municipality total differs from dated reference count')
    types = Counter(r['type'] for r in rows)
    if types != {'시': 75, '군': 82, '자치구': 70}:
        problems.append(f'current city/county/district counts are wrong: {dict(types)}')
    if len({(r['parent'], r['name']) for r in rows}) != len(rows):
        problems.append('duplicate name within parent')
    amap = {a['id']: a for a in agencies}
    metros = {a['id'] for a in agencies if a['type'] == '광역자치단체'}
    if metros != set(PARENTS):
        problems.append('current metropolitan government set differs from 16-parent catalogue')
    for row in rows:
        if row['parent'] not in metros or not row['id'].startswith(row['parent'] + '-'):
            problems.append(f"invalid parent or slug prefix: {row['id']}")
        available = row['id'] in amap
        if row['badge_status'] != ('available' if available else 'pending_logo'):
            problems.append(f"stale badge status: {row['id']}")
        if available and (amap[row['id']].get('parent') != row['parent'] or amap[row['id']]['type'] != row['type']):
            problems.append(f"agency/catalogue mismatch: {row['id']}")
    catalog_ids = set(ids)
    for a in agencies:
        if a['type'] in {'시', '군', '자치구'} and a['id'] not in catalog_ids:
            problems.append(f"uncatalogued municipal badge: {a['id']}")
    if any(r['parent'] in {'sejong', 'jeju'} for r in rows):
        problems.append('Sejong/Jeju administrative subdivisions must not count as municipalities')
    for old in ('gwangju', 'jeonnam'):
        if amap.get(old, {}).get('status') != 'legacy' or amap[old].get('replaced_by') != 'jeonnam-gwangju':
            problems.append(f'legacy compatibility metadata missing: {old}')
    return problems


def validate_pending(catalog, pending):
    """Check backlog bookkeeping, not the legal correctness of source claims."""
    rows = pending['items']
    ids = [row['id'] for row in rows]
    problems = []
    if len(ids) != len(set(ids)):
        problems.append('duplicate pending logo id')
    expected = {row['id'] for row in catalog['municipalities']
                if row['badge_status'] == 'pending_logo'}
    if set(ids) != expected:
        problems.append('pending logo coverage differs from unimplemented municipalities')
    reviewed_reasons = {'restricted_use_terms', 'restricted_or_conflicting_use_terms',
                        'reuse_permission_unverified'}
    for row in rows:
        if 'checked_on' not in row and row.get('reason') not in reviewed_reasons:
            continue
        try:
            checked = row.get('checked_on', '')
            valid_date = date.fromisoformat(checked).isoformat() == checked
            source = urlsplit(row.get('official_source', ''))
            valid_source = source.scheme in {'http', 'https'} and bool(source.hostname)
        except (ValueError, TypeError, AttributeError):
            valid_date = valid_source = False
        note = row.get('note')
        if not valid_date or not valid_source or not isinstance(note, str) or not note.strip():
            problems.append(f"review evidence incomplete: {row['id']}")
    return problems


def validate_public_previews(text, agencies, sources, pending):
    """Reject another institution's CI, duplicate cells, and false availability."""
    amap = {a['id']: a for a in agencies}
    smap = {s['id']: s for s in sources['items']}
    pending_ids = {p['id'] for p in pending['items']}
    problems, seen = [], set()
    columns = None
    for line in text.splitlines():
        if line.startswith('| 기관명 |'):
            columns = len(line.strip().strip('|').split('|'))
        if not line.startswith('| **'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        ids = re.findall(r'`([^`]+)`', cells[2])
        if len(ids) != 1 or len(cells) != columns:
            problems.append('invalid public catalogue row: ' + cells[0])
            continue
        id_ = ids[0]
        if id_ in seen:
            problems.append('duplicate public catalogue id: ' + id_)
        seen.add(id_)
        agency = amap.get(id_)
        if agency is None:
            if cells[-1] != '로고 대기' or id_ not in pending_ids:
                problems.append('unimplemented public CI shown as available: ' + id_)
            continue
        marker = ' [\\*](logo-attribution.md)' if smap.get(id_, {}).get('permission_status') == 'not_verified' else ''
        expected = f"![{agency['name']}](../badges/{id_}/flat.svg)" + marker
        if cells[-1] != expected or agency.get('logo') != id_ or id_ not in smap:
            problems.append('public CI identity/marker mismatch: ' + id_)
    if not seen or seen - set(amap) != pending_ids:
        problems.append('public catalogue and pending coverage differ')
    return problems


def render(catalog, agencies):
    amap = {a['id']: a for a in agencies}
    rows = catalog['municipalities']
    supported = sum(r['badge_status'] == 'available' for r in rows)
    lines = [
        '# 대한민국 지방자치단체 배지 카탈로그 (Local Governments)', '',
        f"행정구역 기준일: **{catalog['effective_on']}**, 출처 확인일: **{catalog['verified_on']}**.", '',
        f'현행 광역 **16곳**, 기초 **227곳(시 75·군 82·자치구 70)**의 전체 목록이다. 기초 배지는 **{supported}곳 제공**, **{len(rows)-supported}곳 로고 대기**다.', '',
        '목록에 등재되었다고 배지가 구현된 것은 아니다. 아래의 제공 상태와 실제 배지 링크를 구분한다. 영문 표기와 Slug는 프로젝트 식별자이며 로고 대기 항목의 공식 영문 명칭 인증을 뜻하지 않는다.', '',
        '## 1. 현행 광역자치단체 (16곳)', '',
        '| 자치단체 | Slug | 심벌 상태 | 배지 |', '| :--- | :--- | :--- | :--- |',
    ]
    for id_, name in PARENTS.items():
        a = amap[id_]
        state = '공식 심벌 확인 대기 · 명칭만 제공' if a.get('logo') is None else '기존 수록 심벌'
        lines.append(f'| {name} | `{id_}` | {state} | ![{name}](../badges/{id_}/flat.svg) |')
    lines += ['', '**통합·호환성 정책:** 전남광주통합특별시의 상징물 안내는 확인일 현재 “콘텐츠 준비중”이므로 기존 광주/전남 로고나 정부상징을 대신 쓰지 않는다. 통합 항목은 명칭만 렌더링한다. 기존 `gwangju`·`jeonnam` URL은 통합 전 자료와 링크 호환성을 위해 유지하고 `legacy`로 구분한다. 현행 광역 수에 포함하지 않는다.', '',
              '## 2. 기초자치단체 전체 목록 (227곳)', '',
              '인천은 제물포·영종·검단구 신설 및 서구→서해구 변경을 반영했다. 과거 중구·동구·서구의 기를 신설 자치구 로고로 대체하지 않는다. 옛 전남 22개 시·군과 광주 5개 자치구의 parent는 `jeonnam-gwangju`이다.', '']
    for parent, name in PARENTS.items():
        group = [r for r in rows if r['parent'] == parent]
        if not group:
            continue
        count = Counter(r['type'] for r in group)
        detail = ' · '.join(f'{k} {v}' for k, v in sorted(count.items()))
        lines += [f'### {name} ({len(group)}곳: {detail})', '',
                  '| 명칭 | 구분 | Slug | 제공 상태 | 배지 |', '| :--- | :--- | :--- | :--- | :--- |']
        for r in group:
            available = r['badge_status'] == 'available'
            badge = f"![{r['name']}](../badges/{r['id']}/flat.svg)" if available else '—'
            lines.append(f"| {r['name']} | {r['type']} | `{r['id']}` | {'제공' if available else '로고 대기'} | {badge} |")
        lines.append('')
    lines += ['## 3. 기초자치단체에 포함하지 않는 사례', '',
              '- 세종특별자치시에는 별도의 기초자치단체가 없다.',
              '- 제주특별자치도의 제주시·서귀포시는 행정시이므로 227곳과 별도로 관리한다. `jeju-jeju`, `jeju-seogwipo`는 향후 행정시용 후보 Slug이며 현재 배지는 제공하지 않는다.', '',
              '## 4. 로고 출처·재검증 및 구현 대기', '',
              '- [시 75곳의 출처·해시](city-logo-sources.json)',
              '- [추가 로고 출처·해시](logo-sources.json)',
              '- [공식 원본·출처표시 안내](logo-attribution.md)',
              '- [미구현 로고와 대기 사유](logo-pending.json)',
              '- [전체 기초자치단체 데이터·출처](local-gov-catalog.json)', '',
              '공식 사이트·Commons에 표시된 이용 조건과 원본/가공본 해시를 기록했다. 공공누리·Commons의 저작권 표기와 별개로 상징물 사용·사칭 제한을 준수해야 한다. 각 기관의 현행 브랜드 가이드와 대조 완료를 보장하지 않는다. 확인되지 않은 로고를 추정 제작하거나 PNG를 SVG로 위장하여 넣지 않는다.', '',
              '## 5. 행정구역 근거', '']
    for s in catalog['sources']:
        lines.append(f"- [{s['scope']}]({s['url']})")
    lines += ['', '2025년 말 기준 행안부 전체 목록에서 출발하여 2026년 7월 인천 개편과 전남·광주 통합을 반영했다. 연도별 기준시점과 발표일은 다르므로 과거 226개 통계를 현행 개수로 그대로 사용하지 않는다.', '',
              '문서와 구현 상태 검증: `python3 scripts/check_catalog.py --check`', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
    agencies = json.loads((ROOT / 'agencies.json').read_text(encoding='utf-8'))
    pending = json.loads((ROOT / 'docs/logo-pending.json').read_text(encoding='utf-8'))
    public_sources = json.loads((ROOT / 'docs/logo-sources.json').read_text(encoding='utf-8'))
    public_pending = json.loads((ROOT / 'docs/public-logo-pending.json').read_text(encoding='utf-8'))
    public_text = (ROOT / 'docs/public-enterprises.md').read_text(encoding='utf-8')
    problems = (validate(catalog, agencies) + validate_pending(catalog, pending)
                + validate_public_previews(public_text, agencies, public_sources, public_pending))
    if problems:
        for p in problems:
            print(p)
        return 1
    content = render(catalog, agencies)
    if args.check:
        if DOCUMENT.read_text(encoding='utf-8') != content:
            print('local-gov.md is stale; run python3 scripts/check_catalog.py')
            return 1
        print('Verified 227 municipalities, 16 current metropolitan governments, and catalogue links/status')
    else:
        DOCUMENT.write_text(content, encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
