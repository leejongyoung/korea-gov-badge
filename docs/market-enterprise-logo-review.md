# 이슈 #1 잔여 7곳 공식 CI 검토

확인일: 2026-11-18. 기준 main: `790c629` (PR #21).

## 범위와 결과

- 이슈 #1의 기존 11곳 가운데 4곳(kepco, kogas, khnp, kac)은 이미 구현돼 있어 중복 추가하지 않았다. 이번 검토는 나머지 7곳만 대상으로 한다.
- 7곳 모두 공식 CI 페이지를 확인했다. 원본 다운로드 확인은 3곳이며 **신규 로고 구현은 0건**이다. 다운로드 가능과 변환·배지 내장·재배포 허용을 구분했다.
- 기존 4곳의 한국 저작권·상표 이용 허락이나 현행 CI 일치 여부를 이번 작업으로 확인한 것은 아니다.
- 이슈에 붙은 시장형 공기업이라는 분류를 현행 법적 분류로 검증한 작업이 아니다. 분류·소관부처 최신화는 별도 검토가 필요하다.
- 기관에 허가 요청·문의·폼 제출은 하지 않았다. 원본은 로컬 검토용이며 저장소에 넣지 않았다.

## 기관별 근거

### 한국지역난방공사 (`kdhc`)

- 공식 CI: https://www.kdhc.co.kr/kdhc/main/contents.do?menuNo=200129
- 판정: `official_vector_reuse_permission_unverified` (구현 보류).
- 검토: 심벌 다운로드는 ZIP 안의 PDF 1건으로 확인했다. CI 페이지의 조형·색상 지침은 확인했으나 SVG 변환·배지 내장·재배포에 적용할 명시적 허락은 확인하지 못했다. 한난체의 상업적 이용 허가 문구는 글꼴에 대한 것으로 심벌 전체의 조건으로 일반화하지 않았다.
- 원본: ZIP containing 1 PDF, 113316 bytes; HTTP 200.
- 원본 SHA-256: `a356394a16f1bf950a3b625f2de8c7f860b05e31ad34a7af647075d63f076947`.

### 인천국제공항공사 (`iia`)

- 공식 CI: https://www.airport.kr/co_ko/573/subview.do
- 판정: `permission_required_by_source_policy` (구현 보류).
- 검토: CI 페이지에서 사전 허가 없는 기관상징 사용에 대한 상표권 제재 경고를 확인했다. 공개 다운로드는 JPG 조합 3종이며, 이를 배지 재배포 허락으로 보지 않았다. 허가 요청은 보내지 않았다.

### 부산항만공사 (`bpa`)

- 공식 CI: https://www.busanpa.com/index.bpa?menuCd=DOM_000000101001004000
- 저작권정책: https://www.busanpa.com/index.bpa?menuCd=DOM_000000108001007000
- 판정: `permission_required_for_unmarked_material` (구현 보류).
- 검토: 공식 AI 원본(PDF 호환 헤더)을 내려받았다. 저작권정책은 공공누리가 없는 자료 이용에 사전 협의를 요구한다. CI 페이지에서 해당 로고에 적용되는 공공누리 표시를 확인하지 못했으므로 변환·재배포는 보류했다.
- 원본: AI with PDF-compatible header, 156675 bytes; HTTP 200.
- 원본 SHA-256: `c11f5429a5dc622e1b7f541b33ede93e0218e5954f7073cb07b4e51a59dd34eb`.

### 인천항만공사 (`ipa`)

- 공식 CI: https://www.icpa.or.kr/content/view.do?menuKey=121&contentKey=54
- 저작권정책: https://www.icpa.or.kr/content/view.do?menuKey=590&contentKey=134
- 판정: `permission_required_by_source_policy` (구현 보류).
- 검토: CI의 심벌·시그니처·색상 지침을 확인했다. 저작권정책은 무단 복제·배포와 내용 변경을 제한하고 수익·혜택 목적 이용에 사전 협의 또는 허락을 요구한다. 배너 링크 안내를 일반적인 로고 재배포 허락으로 확대 해석하지 않았다. 벡터 원본은 확보하지 않았다.

### 여수광양항만공사 (`ygpa`)

- 공식 CI: https://www.ygpa.or.kr/hmpg/ygpa/ygpa/prom/cich/ci01/contPageDetail.do?conts_no=73CF9B8C97DE49EB9BF4BC6CF3BB3BA2
- 저작권정책: https://www.ygpa.or.kr/hmpg/ygpa/addi/copy/contPageDetail.do?conts_no=327CD8B19E554F47ADE8ECFED407A1F6
- 판정: `permission_required_by_source_policy` (구현 보류).
- 검토: 공식 AI ZIP(8개 AI 항목)을 내려받았다. 일반 저작권정책은 무단 복제·배포 및 내용 변경을 제한하고 수익·혜택 목적 이용에 사전 협의 또는 허락을 요구한다. 저장소의 변환·배지 내장·재배포에 적용할 별도 허락은 확인하지 못했다.
- 원본: ZIP containing 8 AI entries, 10775341 bytes; HTTP 200.
- 원본 SHA-256: `1a8c1d498252f51b3994a48bb176ddcc8d67c3ae86cd545e5d554fd083f73e4a`.

### 울산항만공사 (`upa`)

- 공식 CI: https://www.upa.or.kr/portal/contents.do?mid=0505000000
- 저작권정책: https://www.upa.or.kr/portal/contents.do?mid=0805000000
- 판정: `permission_required_for_unmarked_material` (구현 보류).
- 검토: 국문 CI 페이지의 심벌·로고 다운로드는 GIF/JPG로 확인했다. 저작권정책은 공공누리가 부착되지 않은 자료 이용에 사전 협의를 요구한다. 해당 CI에 적용되는 공공누리 표시나 배지 재배포 허락은 확인하지 못했다. 캐릭터 ZIP은 로고 벡터로 간주하지 않았다.

### 강원랜드 (`high1`)

- 공식 CI: https://kangwonland.high1.com/kangwonland/contents.do?key=2750
- 저작권정책: https://kangwonland.high1.com/www/contents.do?key=801
- 판정: `permission_required_by_source_policy` (구현 보류).
- 검토: 공식 사이트는 강원랜드 CI와 하이원리조트 BI를 구분한다. 이슈의 slug high1만 보고 리조트 BI를 회사 로고로 대체하지 않는다. 회사 페이지에서 연결한 저작권정책은 개인적·비영리적 다운로드/링크 외 이용에 사전 허가를 요구하므로 공개 배지 저장소 재배포는 보류했다.

## 다음 단계

- 사전 허가/협의가 필요한 기관은 별도 사용자 승인 없이 연락하지 않는다.
- 허락 불명확 항목은 자료별 공공누리 표시 또는 해당 배지 재배포 목적의 명시적 허락을 확인한 후에만 변환·추가한다.
- 강원랜드는 회사 CI와 리조트 BI를 먼저 구분하며, 인천공항/울산항은 벡터 확보 여부도 별도 해결한다.
- 해시·다운로드 상세·확인일은 `market-enterprise-logo-review.json`, 구현 대기는 `public-logo-pending.json`에 기록했다.
