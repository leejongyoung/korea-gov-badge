# Korea Gov Badge (대한민국 정부 기관 배지)

대한민국 중앙행정기관과 지방자치단체를 위한 SVG 배지 모음입니다. 공공 소프트웨어, 정부 R&D 과제, 공공데이터 연계 프로젝트, [전자정부 표준프레임워크(eGovFrame)](https://github.com/leejongyoung/egovframe-badge) 기반 시스템 등의 README에서 소관 부처 및 기관을 명확하게 표시할 수 있습니다.

별도의 배포 서버나 JavaScript 없이 GitHub raw URL 한 줄로 즉시 임베드할 수 있는 자립형(self-contained) 정적 SVG입니다.

---

## 국가상징 및 공공기관 엠블럼 사용 안내

> [!IMPORTANT]
> **국가상징 및 기관 상징 저작권 및 준수사항**
> - 본 저장소에서 제공하는 모든 배지에 포함된 대한민국 정부상징(GI) 및 각 정부 부처/기관의 공식 엠블럼과 명칭에 대한 권리는 대한민국 정부 및 각 해당 기관에 귀속됩니다.
> - 공공 소프트웨어, 연구 과제, 공공데이터 연계 프로젝트 등 정당한 공공 협력 및 소관 안내 목적으로 사용해야 하며, 공공기관의 공식 명칭 및 상징을 허위로 도용하거나 정부 기관을 사칭하는 행위는 관련 법률에 의해 엄격히 금지됩니다.

각 기관의 성격과 공식 상징 체계에 맞추어 심벌이 자동 적용됩니다:

1. **독자 고유 로고 사용 기관**:
   - 2016년 정부상징 통합 대상에서 제외되어 고유 상징을 유지하거나 신설 시 독자 상징을 제정한 기관(**국방부, 경찰청, 국가정보원, 소방청, 해양경찰청, 감사원, 대통령비서실, 우주항공청, 고위공직자범죄수사처, 검찰청(폐지)**)은 **해당 기관의 공식 고유 엠블럼**이 배지에 포함됩니다.
2. **정부상징 통합 사용 부처**:
   - 대한민국 정부상징(GI)을 사용하는 18개 부 및 공소청, 중대범죄수사청 등 각 처·청·위원회는 **대한민국 정부상징(GI)** 태극 문양이 적용됩니다.

---

## 한 줄로 사용

원하는 기관의 식별자 ID(`mois`, `mnd`, `knpa`, `kasa`, `cio`, `ppo`, `scia`, `gyeonggi-suwon` 등) 또는 한글 기관명(`행정안전부`, `국방부`, `경찰청`, `우주항공청`, `고위공직자범죄수사처` 등)과 스타일을 URL 경로에서 선택합니다.

```md
[![우주항공청 KASA](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/kasa/flat.svg)](https://www.kasa.go.kr)
```

시 배지도 같은 방식으로 사용할 수 있습니다.

```md
![수원시 배지](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/gyeonggi-suwon/flat.svg)
```

한글 기관명 폴더 경로도 100% 동일하게 지원합니다:
```md
[![고위공직자범죄수사처 CIO](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/고위공직자범죄수사처/flat.svg)](https://www.cio.go.kr)
```

---

## 배지 색상 커스터마이징

프로젝트의 README 톤앤매너에 맞추어 6가지 내장 컬러 테마를 즉시 URL로 사용하거나, 원하는 임의의 Hex 코드로 직접 생성할 수 있습니다.

### 1. 내장 컬러 테마 (URL로 바로 사용)

스타일 이름 뒤에 `-<color>`를 붙여 호출합니다 (예: `flat-navy.svg`, `flat-black.svg`):

| 컬러 테마 | 테마 코드 | 색상 값 (Hex) | 우주항공청 예시 | 고위공직자범죄수사처 예시 |
| :--- | :---: | :---: | :--- | :--- |
| **블루 (기본)** | `blue` | `#134f8c` | ![kasa](badges/kasa/flat.svg) | ![cio](badges/cio/flat.svg) |
| **네이비** | `navy` | `#003764` | ![kasa navy](badges/kasa/flat-navy.svg) | ![cio navy](badges/cio/flat-navy.svg) |
| **블랙 / 다크** | `black` | `#24292f` | ![kasa black](badges/kasa/flat-black.svg) | ![cio black](badges/cio/flat-black.svg) |
| **그린** | `green` | `#1a7f37` | ![kasa green](badges/kasa/flat-green.svg) | ![cio green](badges/cio/flat-green.svg) |
| **레드** | `red` | `#cf222e` | ![kasa red](badges/kasa/flat-red.svg) | ![cio red](badges/cio/flat-red.svg) |
| **그레이** | `gray` | `#57606a` | ![kasa gray](badges/kasa/flat-gray.svg) | ![cio gray](badges/cio/flat-gray.svg) |

```md
<!-- 블랙 테마 사용 예시 -->
[![우주항공청 KASA](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/kasa/flat-black.svg)](https://www.kasa.go.kr)

<!-- 네이비 테마 사용 예시 -->
[![고위공직자범죄수사처 CIO](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/cio/flat-navy.svg)](https://www.cio.go.kr)
```

### 2. 임의의 Hex 색상으로 직접 생성 (CLI)

내장된 빌드 스크립트를 통해 원하는 Hex 색상 코드로 맞춤형 SVG를 즉시 생성할 수 있습니다:

```sh
# 보라색(#8250df) 메시지 배경의 우주항공청 flat 배지 생성
python3 scripts/generate.py --agency kasa --color "#8250df" --style flat --out custom-kasa.svg

# 배경색과 글자색 모두 커스텀 지정
python3 scripts/generate.py --agency cio --label-color "#ffffff" --text-color "#003764" --color "#0969da" --out custom-cio.svg
```

---

## 스타일 미리보기

[shields.io](https://shields.io)의 대표 스타일(`flat`, `flat-square`, `plastic`, `for-the-badge`)과 전용 `outline` 스타일을 제공합니다. 모든 스타일은 깔끔한 화이트/블루 톤앤매너로 통일되어 있습니다.

| 스타일 | 우주항공청 (`kasa`) | 고위공직자범죄수사처 (`cio`) | 경찰청 (`knpa`) |
| :--- | :--- | :--- | :--- |
| **flat** | ![kasa flat](badges/kasa/flat.svg) | ![cio flat](badges/cio/flat.svg) | ![knpa flat](badges/knpa/flat.svg) |
| **flat-square** | ![kasa flat-square](badges/kasa/flat-square.svg) | ![cio flat-square](badges/cio/flat-square.svg) | ![knpa flat-square](badges/knpa/flat-square.svg) |
| **plastic** | ![kasa plastic](badges/kasa/plastic.svg) | ![cio plastic](badges/cio/plastic.svg) | ![knpa plastic](badges/knpa/plastic.svg) |
| **for-the-badge** | ![kasa for-the-badge](badges/kasa/for-the-badge.svg) | ![cio for-the-badge](badges/cio/for-the-badge.svg) | ![knpa for-the-badge](badges/knpa/for-the-badge.svg) |
| **outline** | ![kasa outline](badges/kasa/outline.svg) | ![cio outline](badges/cio/outline.svg) | ![knpa outline](badges/knpa/outline.svg) |

---

## 분야별 배지 카탈로그 (Badge Catalogs)

각 분야별 전체 기관 목록 및 배지 미리보기는 아래 전용 카탈로그 문서에서 상세히 확인하실 수 있습니다:

| 카탈로그 | 대상 기관 | 기관 수 | 바로가기 |
| :--- | :--- | :---: | :--- |
| **대한민국 중앙행정기관** | 19부, 처, 21청, 6위원회, 감사원, 국가정보원 | 55개 | [중앙행정기관 카탈로그 바로가기 →](docs/central-gov.md) |
| **지방자치단체** | 광역 기록 17개(현행화 [#9](https://github.com/leejongyoung/korea-gov-badge/issues/9)) + 서울 자치구 25개 + 시 75개 | 117개 | [지방자치단체 카탈로그 바로가기 →](docs/local-gov.md) |
| **공기업 및 공공기관** | 한국전력, 코레일, LH, NIA, KISA 등 주요 공기업·준정부기관 | 35개+ | [공기업·공공기관 카탈로그 바로가기 →](docs/public-enterprises.md) |

### 주요 대표 기관 배지 예시

| 기관명 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) |
| :--- | :--- | :--- | :--- |
| **행정안전부** | MOIS | `mois` | ![mois](badges/mois/flat.svg) |
| **과학기술정보통신부** | MSIT | `msit` | ![msit](badges/msit/flat.svg) |
| **경찰청** | KNPA | `knpa` | ![knpa](badges/knpa/flat.svg) |
| **우주항공청** | KASA | `kasa` | ![kasa](badges/kasa/flat.svg) |
| **고위공직자범죄수사처** | CIO | `cio` | ![cio](badges/cio/flat.svg) |
| **공소청** | PPO | `ppo` | ![ppo](badges/ppo/flat.svg) |
| **중대범죄수사청** | SCIA | `scia` | ![scia](badges/scia/flat.svg) |
| **검찰청(폐지)** | SPO | `spo-legacy` | ![spo](badges/spo-legacy/flat.svg) |

---

## 배지 생성 및 테스트

새로운 기관 추가나 배지 스타일 수정 시 아래 명령어를 통해 배지를 재빌드하고 무결성을 검증할 수 있습니다.

```sh
# 1. 172개 기관 배지 생성 (컬러 테마 프리셋 포함 13,800개)
python3 scripts/generate.py

# 2. 단위 테스트 실행 (데이터 무결성, SVG 유효성, 커스텀 색상 검증)
python3 -m unittest discover -s tests -v

# 3. 배지 생성 결과 일치성 검증 (CI 검증용)
python3 scripts/generate.py --check
```

---

## 설계 원칙

1. **Self-contained SVG**:
   - 모든 배지는 각 기관 고유 엠블럼 또는 정부상징 벡터 패스를 파일 내부에 직접 포함합니다.
   - 외부 폰트 파일이나 외부 이미지 링크에 의존하지 않고 어디서나 완벽하게 렌더링됩니다.
2. **이중 경로(Alias) 지원**:
   - URL 작성의 편의를 위해 영문 소문자 Slug(`kasa`, `cio`, `mois`)와 한국어 정식 명칭(`우주항공청`, `고위공직자범죄수사처`, `행정안전부`) 폴더 경로를 모두 지원합니다.
3. **가독성 최적화 타이포그래피 및 동적 아이콘 마운팅**:
   - 정방형 엠블럼, 횡형 상징(KASA, 공수처 등) 등 다양한 심벌의 고유 비율을 수학적으로 자동 계산하여 6px의 일관된 여백으로 텍스트와 정렬합니다.
   - 시스템 폰트 스택(`-apple-system`, `Noto Sans KR`, `Malgun Gothic` 등)을 선언하여 모든 OS에서 선명한 한글을 지원합니다.
4. **다양한 컬러 테마 및 커스터마이징 지원**:
   - 6가지 표준 프리셋(`blue`, `navy`, `black`, `green`, `red`, `gray`)을 지원하며, CLI를 통해 원하는 임의의 Hex 코드로 배지를 즉시 생성할 수 있습니다.
5. **CI 무결성 보증**:
   - GitHub Actions 워크플로를 통해 `generate.py --check`가 자동으로 수행되어 생성물과 소스 코드 간의 일치를 항시 보장합니다.

---

## 라이선스

본 저장소의 빌드 스크립트, 테스트 코드 및 CI 설정은 [MIT License](LICENSE)에 따라 자유롭게 사용 및 수정하실 수 있습니다. 국가상징 및 공공기관 엠블럼에 관한 저작권 및 사용 수칙은 문서 상단의 안내를 준수해 주시기 바랍니다.
