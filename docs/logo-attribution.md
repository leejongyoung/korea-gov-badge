# 추가 로고 출처와 이용 조건

코드의 MIT 라이선스는 기관의 상징물에 적용되지 않는다. 각 배지는 소관 안내용이며 기관의 후원·승인을 뜻하지 않는다.

이 저장소는 CI 구현 여부와 이용허락 확인 여부를 구분한다. 사용자 요청에 따라 허락 미확인 CI도 제약을 남겨 제공하므로, 이미 검증된 SVG가 있는 기관을 라이선스 미확인만을 이유로 `logo: null`·텍스트 전용 상태로 되돌리지 않는다. 카탈로그에서 제공한다고 표시한 로고는 실제 생성 배지와 한글·영문 경로에도 포함되어야 한다.

## 공식 자료에서 추가한 로고

| 기관·저작물 | 출처·이용 조건 | 처리 내역 |
| --- | --- | --- |
| 진천군, 「진천군마크 시그니처」 (`jincheon_ci.ai`, 원본 작성연도 미표시) | [진천군 공식 상징 안내](https://www.jincheon.go.kr/home/sub.do?menukey=265), [공식 벡터 원본](https://www.jincheon.go.kr/oldData/editor/content/main/info/symbol.zip), [공공누리 제1유형·출처표시](https://www.kogl.or.kr/info/licenseType1.do) | 2026-11-18 확인. PDF 호환 AI를 `pdftocairo -svg`로 변환하고 첫 심벌의 완전한 벡터 경로만 추출. 형상·색을 새로 그리거나 래스터를 추적하지 않음. SVGO 최적화. |
| 한국예술인복지재단, 2022년 「개편 CI」 (`개편_CI.ai`) | [공식 CI 배포 게시물](https://www.kawf.kr/notice/sub07View.do?selIdx=17907), [공식 AI 원본](https://www.kawf.kr/common/download.do?s=165967859177102), [공공누리 제1유형·출처표시](https://www.kogl.or.kr/info/licenseType1.do) | 2026-11-18 확인. 매뉴얼의 재생 지침에 따라 별도 AI의 완전한 심벌 경로 3개를 추출. 화면 색은 매뉴얼 A3.1의 `#0075BF` 적용, 여백 정리·SVG 변환·최적화. 새로 그리거나 래스터를 추적하지 않음. |
| 서울에너지공사, 「심벌마크」 (원본 작성연도 미표시) | [공식 CI·공공누리 1유형](https://www.i-se.co.kr/intro06), [공식 심벌 AI](https://www.i-se.co.kr/comm/getFile?srvcId=BBSTY1&upperNo=45&fileTy=ATTACH&fileNo=1) | 별도 심벌 AI의 벡터 경로 13개를 모두 유지해 SVG 변환·여백 정리·최적화. 새로 그리거나 임의 재색상하지 않음. |
| 경기도일자리재단, 「기관 심볼마크」 (원본 작성연도 미표시) | [공식 CI·공공누리 1유형](https://www.gjf.or.kr/main/content/view.do?sn=91), [공식 ZIP/EPS](https://www.gjf.or.kr/repository/download/ci/ai.zip) | 기관 심벌 EPS의 벡터 3개를 변환하고 공식 화면 RGB 색을 적용. 같은 ZIP의 잡아바 브랜드와 구분. 기본 배지에서 양변 27 CSS px 이상 확보. 인쇄 시 심벌 7mm 이상 유지. |
| 부산항만공사, 「기관 CI 심벌」 (원본 작성연도 미표시) | [공식 CI](https://www.busanpa.com/index.bpa?menuCd=DOM_000000101001004000) · [공식 원본](https://www.busanpa.com/FileManager/ofda.sko?f_idx=QzkzcDNoUWZXMlpwVGlyNW9peVFiZz09&ofn=176819345852357.ai) · [정책](https://www.busanpa.com/index.bpa?menuCd=DOM_000000108001007000) | **로고 제공·재배포 허락 미확인**. 일반 정책은 공공누리 미표시 자료의 사전 협의를 안내함. 해당 CI의 자유이용 유형 및 배지 재배포 허락 미확인. 공식 AI 벡터에서 전체 심벌을 추출해 적용. 공공누리 1유형으로 확인된 자료가 아님. |
| 인천항만공사, 「기관 CI 심벌」 (원본 작성연도 미표시) | [공식 CI](https://www.icpa.or.kr/content/view.do?contentKey=54&menuKey=1121) · [공식 원본](https://www.icpa.or.kr/file/commonFileDownload.do?path=!@$*CJELQSRnZjbVLK3l7dJljdMBYhU1wrZJPjy1uofgerU=!@$*) · [정책](https://www.icpa.or.kr/content/view.do?menuKey=590&contentKey=134) | **로고 제공·재배포 허락 미확인**. 일반 정책에 무단 복제·배포 및 내용 변경 제한과 일부 이용의 사전 협의·허락 안내가 있음. 해당 CI 배지 재배포 허락 미확인. 공식 AI 벡터에서 전체 심벌을 추출해 적용. 공공누리 1유형으로 확인된 자료가 아님. |
| 여수광양항만공사, 「기관 CI 심벌」 (원본 작성연도 미표시) | [공식 CI](https://www.ygpa.or.kr/hmpg/ygpa/ygpa/prom/cich/ci01/contPageDetail.do?conts_no=73CF9B8C97DE49EB9BF4BC6CF3BB3BA2) · [공식 원본](https://www.ygpa.or.kr/images/hmpg/ygpa/sub/st/YGPACI_AI.zip) · [정책](https://www.ygpa.or.kr/hmpg/ygpa/addi/copy/contPageDetail.do?conts_no=327CD8B19E554F47ADE8ECFED407A1F6) | **로고 제공·재배포 허락 미확인**. 일반 정책에 무단 복제·배포 및 무단 변경 제한, 일부 이용의 사전 협의·허락 안내가 있음. 해당 CI 배지 재배포 허락 미확인. 공식 AI 벡터에서 전체 심벌을 추출해 적용. 공공누리 1유형으로 확인된 자료가 아님. |

위 공식 자료 기반 배지를 재사용할 때 각 기관명·저작물명·출처 URL·공공누리 유형을 함께 표시한다. SVG 내부의 출처 설명(`desc`)도 유지한다. 로고/배지 변경 여부는 이용자가 실제 변경에 맞춰 표시해야 한다.

## Commons에서 추가한 로고

보은군·고창군·고흥군과 2026-11-18에 추가한 구·군 87곳은 [출처 및 해시 목록](logo-sources.json)의 개별 Commons 파일 페이지에서 Public domain으로 표시된 원본을 사용했다. 원본 SHA-1은 Commons 메타데이터와 대조했고 가공본 해시를 함께 기록했다. 저작권 상태와 별개인 상징물·사칭 제한을 준수해야 한다. Commons의 표기가 각 기관의 현행 브랜드 가이드 검증 완료를 뜻하지는 않는다.

공공기관 10곳(한국전력공사·한국가스공사·한국수력원자력·한국공항공사·한국철도공사·한국도로공사·한국조폐공사·한국관광공사·한국인터넷진흥원·한국원자력연구원)은 Commons가 `Public domain`과 상표(trademarked) 제한으로 표시한 파일을 사용했다. 이 표시는 상표권이나 한국 저작권 상태를 보장하지 않으며, 각 기관의 상표 사용 지침을 따라야 한다. 한국전자통신연구원·한국항공우주연구원은 공식 정책이 별도 허락·협의를 요구해 제외했다.

시 75곳의 기존 출처는 [별도 기록](city-logo-sources.json)을 참고한다.

## 수급·이용 조건 확인이 남은 항목

[지자체 로고 대기 목록](logo-pending.json)과 [공공기관 로고 확인 목록](public-logo-pending.json)을 구분한다. 공식 사이트에서 다운로드할 수 있다는 사실만으로 재배포 허락이나 자유이용을 가정하지 않는다. 개별 상징에 관한 이용 안내가 페이지 공통 푸터와 다르면 개별 안내를 우선 확인한다.

## 대기 목록의 자동 검증

`python3 scripts/check_catalog.py --check`는 문서·등록 상태뿐 아니라 `logo-pending.json`도 검사한다.

- 대기 ID의 중복·누락 및 이미 구현된 기관이 대기 목록에 남은 경우 실패한다.
- 개별 검토일(`checked_on`)이 있거나 이용조건 검토 사유(`restricted_use_terms`, `restricted_or_conflicting_use_terms`, `reuse_permission_unverified`)를 기록한 항목은 유효한 ISO 날짜·출처 HTTP(S) URL·설명(`note`)이 필요하다.
- `official_checked_on`은 기존의 예비 접근 시도일이며, 이용조건 검토 완료나 파일 확보를 뜻하지 않는다. 시간초과 등 실패 기록과 `checked_on` 검토 기록을 혼동하지 않는다.
- 검사는 오프라인 메타데이터 정합성 검사다. URL의 실제 가용성, 허락의 법률적 유효성 또는 현행 CI 일치를 자동 인증하지 않는다.

## 같은 자료를 다시 검증하는 절차

1. 공식 상징 안내 페이지의 심벌 이미지와 다운로드 링크를 확인하고, 개별 이용 조건이 공통 푸터와 충돌하지 않는지 확인한다. 링크만 있다는 이유로 공개 라이선스를 가정하지 않는다.
2. 원본 ZIP·AI와 가공 SVG의 SHA-256을 `logo-sources.json`에 기록한다. 원본은 해당 URL에서 확보하고 저장소에 대용량 AI를 복제하지 않는다.
3. 진천군 원본은 PDF 호환 AI다. 기존 Poppler의 `pdftocairo -svg jincheon_ci.ai sheet.svg`를 사용한다. 원본 해시가 기록과 같은 경우에 한해 변환 결과의 첫 심벌 경로 61~70을 사용한다(0부터 시작, `viewBox="74 80 78 62"`). 원본/도구가 달라지면 경로 번호를 그대로 믿지 말고 전체 시트와 공식 심벌 이미지를 다시 대조한다.
4. 경로를 래스터화하거나 새로 그리지 않는다. 심벌의 모든 도형을 유지하고 여백만 제외한다. 출처표시 `desc`를 넣고, 기존 SVGO 4.1.0을 사용할 때 `removeDesc: false`로 보존한다.
5. 신규 심벌과 5가지 스타일 배지를 렌더링해 잘림·색·형상·가독성을 확인한다. `unittest`, `generate.py --check`, `check_catalog.py --check`와 CI를 통과한 정확한 커밋을 검토한 뒤 병합한다.
6. Commons가 429를 반환하면 `Retry-After` 동안 해당 호스트의 수집을 중단한다. 대기 시간을 임의로 짧게 자르거나 프록시·미러로 우회하지 않는다. 다른 공식 출처를 독립적으로 검증하되 권리 확인도 함께 다시 한다.

## 로고별 최소 표시 크기

공식 CI 지침에 최소 크기가 있는 로고는 루트 SVG의 `data-min-icon-size`에 양변 최소 CSS px를 기록한다. 생성기는 비례를 유지한 채 심벌과 배지 높이를 함께 키운다. 이 속성이 없는 기존 배지의 크기는 바꾸지 않는다. 경기도일자리재단은 7mm 안내에 대응해 27 CSS px(96px/in 기준 약 7.14mm)를 사용한다. SVG를 외부에서 축소하거나 인쇄할 때에는 실제 심벌 크기 7mm 이상을 별도로 유지해야 한다.

## 연구기관 첫 구현 묶음 (2026-11-19)

5곳 모두 공식 CI 다운로드의 벡터 경로를 기계적으로 옮겼다. 상표·이용 제약과 재배포 허락 미확인 상태는 유지하며 카탈로그에 별표를 표시했다. 구현은 법적 이용 허락이나 기관 보증을 뜻하지 않는다.

- **한국과학기술연구원**: [공식 CI](https://kist.re.kr/ko/intro/kist-ci.do), [원본 다운로드](https://kist.re.kr/cms/etcResourceDown.do?site=%24cms%24NYeyA&key=%24cms%24NISQygKg+gwiB0AvAlgByA). 정비례 확대·축소 및 색상 활용 지침을 확인했다. 이 저장소의 SVG 변환·배지 내장·재배포에 적용할 명시적 허락은 이번 조사에서 확인하지 못했다. 변환: official bilingual logotype (download contains no separate symbol).
- **한국전자통신연구원**: [공식 CI](https://www.etri.re.kr/korcon/sub7/sub7_11.etri), [원본 다운로드](https://www.etri.re.kr/file/predicalFile.etri?filename=ci_ai.zip). 임의 변경 제한을 포함하는 CI 지침을 확인했다. 일반 저작권정책은 자료별 공공누리 표시와 조건 확인을 요구한다. 해당 CI 파일에 적용되는 유형이나 별도 배지 재배포 허락은 확인하지 못했다. 변환: official complete symbol / wordmark.
- **한국항공우주연구원**: [공식 CI](https://www.kari.re.kr//kor/contents/92), [원본 다운로드](https://www.kari.re.kr/cms/attach/635c9a683e2ec6b248c4e92a21c157f5/778bdbf5db9ced7c8fd52756c00bf0cd). 심볼·시그니처·색상 지침을 확인했다. 일반 저작권정책은 무단 복제·배포 및 내용 변경을 제한하고 일부 이용에 사전 협의를 요구한다. 배지 변환·재배포에 적용할 별도 허락은 확인하지 못했다. 변환: official complete symbol / wordmark.
- **한국표준과학연구원**: [공식 CI](https://www.kriss.re.kr/menu.es?mid=a10101070000), [원본 다운로드](https://www.kriss.re.kr/main/download/KRISS_CI.zip). 원고를 정비례로 확대·축소하도록 하는 지침을 확인했다. CI 파일을 공개 다운로드할 수 있지만 이 저장소의 변환·재배포 허락은 이번 조사에서 확인하지 못했다. 변환: official complete symbol / wordmark.
- **한국화학연구원**: [공식 CI](https://www.krict.re.kr/kor/sub01_05_01.do), [원본 다운로드](https://www.krict.re.kr/cmm/fms/FileDown.do?atchFileId=FILE_000000003365Hg8&fileSn=0). 워터마크·시그니처·색상 지침과 AI 다운로드를 확인했다. Commons에서 JPG만 발견했던 결과는 공식 벡터 원본 부재를 뜻하지 않는다. 배지 변환·재배포 허락은 이번 조사에서 확인하지 못했다. 변환: official complete symbol / wordmark.

[추출 해시·범위 및 원본/SVG 렌더](ci-first-five/extraction.json). KARI 가이드 격자는 심벌이 아니므로 제외했다. KIST는 공식 AI에 있는 로고타입 전체이며 별도 심벌은 이 다운로드에 없다.
