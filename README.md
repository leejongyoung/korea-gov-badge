# Korea Gov Badge (대한민국 정부 기관 배지)

대한민국 중앙행정기관(19부, 처, 청, 위원회 등 총 52개 기관)을 위한 오픈소스 SVG 배지 모음입니다. 공공 소프트웨어, 정부 R&D 과제, 공공데이터 연계 프로젝트, [전자정부 표준프레임워크(eGovFrame)](https://github.com/leejongyoung/egovframe-badge) 기반 시스템 등의 README에서 공식 정부 기관 소관 또는 연계 프로젝트임을 직관적으로 나타낼 수 있습니다.

별도의 배포 서버나 JavaScript 없이 GitHub raw URL 한 줄로 즉시 임베드할 수 있는 자립형(self-contained) 정적 SVG입니다.

---

## 🇰🇷 상징 및 로고 적용 원칙

사용자의 직관적 식별과 정부 기관 공식 CI 가이드라인을 고려하여 아래와 같이 최적화된 심벌을 자동 적용합니다:

1. **대한민국 국가 표기 배지 (`[ 대한민국 | 기관명 ]`, `[ Gov.kr | 약칭 ]`)**:
   - 국기인 **태극기(Taegeukgi)** 가 선명하게 적용됩니다.
2. **독자 고유 로고 사용 기관 배지 (`[ 기관명 | 약칭 ]`)**:
   - 2016년 정부상징 통합 대상에서 제외되거나 독자 상징을 사용하는 기관(**국방부, 경찰청, 국가정보원, 소방청, 해양경찰청, 검찰청, 감사원, 대통령비서실**)은 **해당 기관의 공식 고유 엠블럼**이 적용됩니다.
3. **일반 정부 부처 배지 (`[ 기관명 | 약칭 ]`)**:
   - 공식 통합 상징을 사용하는 일반 행정 부처(행정안전부, 과학기술정보통신부 등)는 **대한민국 정부상징(GI)** 태극 문양이 적용됩니다.

---

## 🚀 한 줄로 사용

원하는 기관의 식별자 ID(`mois`, `mnd`, `knpa` 등) 또는 한글 기관명(`행정안전부`, `국방부`, `경찰청` 등)과 스타일을 URL 경로에서 선택합니다.

### 1. 국문 기본 (`[ 대한민국 | 부처명 ]` — 태극기 🇰🇷)
가장 널리 사용되는 기본 정부 배지 형식입니다.
```md
[![행정안전부](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/mois/flat.svg)](https://www.mois.go.kr)
```
*(한글 기관명 경로도 동일하게 지원합니다: `badges/행정안전부/flat.svg` 또는 `badges/mois/flat-ko.svg`)*

### 2. 영문 기본 (`[ Gov.kr | EN_SHORT ]` — 태극기 🇰🇷)
글로벌 오픈소스 프로젝트 또는 다국어 README에 적합한 영문 배지 형식입니다.
```md
[![Gov.kr MOIS](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/mois/flat-en.svg)](https://www.mois.go.kr)
```
*(영문 하위 경로도 지원합니다: `badges/mois/en/flat.svg`)*

### 3. 기관명-영문약칭 (`[ 부처명 | EN_SHORT ]` — 기관 고유 로고 / 정부상징)
기관 국문명과 공식 영문 약칭을 표시하며, 기관 고유 상징(참수리, 철매, 새매 등)을 보여줍니다.
```md
[![경찰청 KNPA](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/knpa/flat-abbr.svg)](https://www.police.go.kr)
```
*(기관 배지 경로도 지원합니다: `badges/knpa/flat-agency.svg` 또는 `badges/경찰청/flat-agency.svg`)*

---

## 🛡️ 고유 로고 기관 배지 미리보기

독자 엠블럼을 사용하는 주요 기관의 실제 배지 모습입니다:

| 기관 | 국문 기본 (태극기) | 기관 고유 배지 (공식 엠블럼) | 영문 (태극기) |
| :--- | :--- | :--- | :--- |
| **국방부 (MND)** | ![mnd ko](badges/mnd/flat.svg) | ![mnd agency](badges/mnd/flat-agency.svg) | ![mnd en](badges/mnd/flat-en.svg) |
| **경찰청 (KNPA)** | ![knpa ko](badges/knpa/flat.svg) | ![knpa agency](badges/knpa/flat-agency.svg) | ![knpa en](badges/knpa/flat-en.svg) |
| **국가정보원 (NIS)** | ![nis ko](badges/nis/flat.svg) | ![nis agency](badges/nis/flat-agency.svg) | ![nis en](badges/nis/flat-en.svg) |
| **소방청 (NFA)** | ![nfa ko](badges/nfa/flat.svg) | ![nfa agency](badges/nfa/flat-agency.svg) | ![nfa en](badges/nfa/flat-en.svg) |
| **해양경찰청 (KCG)** | ![kcg ko](badges/kcg/flat.svg) | ![kcg agency](badges/kcg/flat-agency.svg) | ![kcg en](badges/kcg/flat-en.svg) |
| **검찰청 (SPO)** | ![spo ko](badges/spo/flat.svg) | ![spo agency](badges/spo/flat-agency.svg) | ![spo en](badges/spo/flat-en.svg) |
| **감사원 (BAI)** | ![bai ko](badges/bai/flat.svg) | ![bai agency](badges/bai/flat-agency.svg) | ![bai en](badges/bai/flat-en.svg) |
| **대통령비서실 (PRESIDENT)** | ![president ko](badges/president/flat.svg) | ![president agency](badges/president/flat-agency.svg) | ![president en](badges/president/flat-en.svg) |
| **일반 부처 (행정안전부)** | ![mois ko](badges/mois/flat.svg) | ![mois agency](badges/mois/flat-agency.svg) | ![mois en](badges/mois/flat-en.svg) |

---

## 🎨 스타일 미리보기

[shields.io](https://shields.io)의 대표 스타일(`flat`, `flat-square`, `plastic`, `for-the-badge`)을 완벽히 지원하며, 깔끔한 전용 `outline` 스타일을 추가로 제공합니다.

| 스타일 | 국문 기본 (`대한민국 \| 기관명`) | 영문 (`Gov.kr \| 약칭`) | 기관 고유 (`기관명 \| 약칭`) |
| :--- | :--- | :--- | :--- |
| **flat** | ![flat](badges/knpa/flat.svg) | ![flat-en](badges/knpa/flat-en.svg) | ![flat-agency](badges/knpa/flat-agency.svg) |
| **flat-square** | ![flat-square](badges/knpa/flat-square.svg) | ![flat-square-en](badges/knpa/flat-square-en.svg) | ![flat-square-agency](badges/knpa/flat-square-agency.svg) |
| **plastic** | ![plastic](badges/knpa/plastic.svg) | ![plastic-en](badges/knpa/plastic-en.svg) | ![plastic-agency](badges/knpa/flat-agency.svg) |
| **for-the-badge** | ![for-the-badge](badges/knpa/for-the-badge.svg) | ![for-the-badge-en](badges/knpa/for-the-badge-en.svg) | ![for-the-badge-agency](badges/knpa/for-the-badge-agency.svg) |
| **outline** | ![outline](badges/knpa/outline.svg) | ![outline-en](badges/knpa/outline-en.svg) | ![outline-agency](badges/knpa/outline-agency.svg) |

---

## 🏛️ 지원 기관 목록 (총 52개 기관)

최신 대한민국 정부조직법 및 개편 현황(우주항공청, 국가유산청, 재외동포청 개청 등 반영)을 준수하는 52개 기관의 배지를 제공합니다.

### 1. 19부 (Ministries)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) | 고유/기관 배지 (`flat-agency.svg`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **기획재정부** | Ministry of Economy and Finance | MOEF | `moef` | ![moef](badges/moef/flat.svg) | ![moef agency](badges/moef/flat-agency.svg) |
| **교육부** | Ministry of Education | MOE | `moe` | ![moe](badges/moe/flat.svg) | ![moe agency](badges/moe/flat-agency.svg) |
| **과학기술정보통신부** | Ministry of Science and ICT | MSIT | `msit` | ![msit](badges/msit/flat.svg) | ![msit agency](badges/msit/flat-agency.svg) |
| **외교부** | Ministry of Foreign Affairs | MOFA | `mofa` | ![mofa](badges/mofa/flat.svg) | ![mofa agency](badges/mofa/flat-agency.svg) |
| **통일부** | Ministry of Unification | MOU | `mou` | ![mou](badges/mou/flat.svg) | ![mou agency](badges/mou/flat-agency.svg) |
| **법무부** | Ministry of Justice | MOJ | `moj` | ![moj](badges/moj/flat.svg) | ![moj agency](badges/moj/flat-agency.svg) |
| **국방부** | Ministry of National Defense | MND | `mnd` | ![mnd](badges/mnd/flat.svg) | ![mnd agency](badges/mnd/flat-agency.svg) |
| **행정안전부** | Ministry of the Interior and Safety | MOIS | `mois` | ![mois](badges/mois/flat.svg) | ![mois agency](badges/mois/flat-agency.svg) |
| **국가보훈부** | Ministry of Patriots and Veterans Affairs | MPVA | `mpva` | ![mpva](badges/mpva/flat.svg) | ![mpva agency](badges/mpva/flat-agency.svg) |
| **문화체육관광부** | Ministry of Culture, Sports and Tourism | MCST | `mcst` | ![mcst](badges/mcst/flat.svg) | ![mcst agency](badges/mcst/flat-agency.svg) |
| **농림축산식품부** | Ministry of Agriculture, Food and Rural Affairs | MAFRA | `mafra` | ![mafra](badges/mafra/flat.svg) | ![mafra agency](badges/mafra/flat-agency.svg) |
| **산업통상자원부** | Ministry of Trade, Industry and Energy | MOTIE | `motie` | ![motie](badges/motie/flat.svg) | ![motie agency](badges/motie/flat-agency.svg) |
| **보건복지부** | Ministry of Health and Welfare | MOHW | `mohw` | ![mohw](badges/mohw/flat.svg) | ![mohw agency](badges/mohw/flat-agency.svg) |
| **환경부** | Ministry of Environment | ME | `me` | ![me](badges/me/flat.svg) | ![me agency](badges/me/flat-agency.svg) |
| **고용노동부** | Ministry of Employment and Labor | MOEL | `moel` | ![moel](badges/moel/flat.svg) | ![moel agency](badges/moel/flat-agency.svg) |
| **여성가족부** | Ministry of Gender Equality and Family | MOGEF | `mogef` | ![mogef](badges/mogef/flat.svg) | ![mogef agency](badges/mogef/flat-agency.svg) |
| **국토교통부** | Ministry of Land, Infrastructure and Transport | MOLIT | `molit` | ![molit](badges/molit/flat.svg) | ![molit agency](badges/molit/flat-agency.svg) |
| **해양수산부** | Ministry of Oceans and Fisheries | MOF | `mof` | ![mof](badges/mof/flat.svg) | ![mof agency](badges/mof/flat-agency.svg) |
| **중소벤처기업부** | Ministry of SMEs and Startups | MSS | `mss` | ![mss](badges/mss/flat.svg) | ![mss agency](badges/mss/flat-agency.svg) |

### 2. 처 / 실 (Offices & Ministries)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) | 고유/기관 배지 (`flat-agency.svg`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **인사혁신처** | Ministry of Personnel Management | MPM | `mpm` | ![mpm](badges/mpm/flat.svg) | ![mpm agency](badges/mpm/flat-agency.svg) |
| **법제처** | Ministry of Government Legislation | MOLEG | `moleg` | ![moleg](badges/moleg/flat.svg) | ![moleg agency](badges/moleg/flat-agency.svg) |
| **식품의약품안전처** | Ministry of Food and Drug Safety | MFDS | `mfds` | ![mfds](badges/mfds/flat.svg) | ![mfds agency](badges/mfds/flat-agency.svg) |
| **국무조정실** | Office for Government Policy Coordination | OPC | `opm` | ![opm](badges/opm/flat.svg) | ![opm agency](badges/opm/flat-agency.svg) |
| **대통령비서실** | Office of the President | PRESIDENT | `president` | ![president](badges/president/flat.svg) | ![president agency](badges/president/flat-agency.svg) |

### 3. 20청 (Administrations & Agencies)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) | 고유/기관 배지 (`flat-agency.svg`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **국세청** | National Tax Service | NTS | `nts` | ![nts](badges/nts/flat.svg) | ![nts agency](badges/nts/flat-agency.svg) |
| **관세청** | Korea Customs Service | KCS | `kcs` | ![kcs](badges/kcs/flat.svg) | ![kcs agency](badges/kcs/flat-agency.svg) |
| **조달청** | Public Procurement Service | PPS | `pps` | ![pps](badges/pps/flat.svg) | ![pps agency](badges/pps/flat-agency.svg) |
| **통계청** | Statistics Korea | KOSTAT | `kostat` | ![kostat](badges/kostat/flat.svg) | ![kostat agency](badges/kostat/flat-agency.svg) |
| **검찰청** | Supreme Prosecutors' Office | SPO | `spo` | ![spo](badges/spo/flat.svg) | ![spo agency](badges/spo/flat-agency.svg) |
| **병무청** | Military Manpower Administration | MMA | `mma` | ![mma](badges/mma/flat.svg) | ![mma agency](badges/mma/flat-agency.svg) |
| **방위사업청** | Defense Acquisition Program Administration | DAPA | `dapa` | ![dapa](badges/dapa/flat.svg) | ![dapa agency](badges/dapa/flat-agency.svg) |
| **경찰청** | Korean National Police Agency | KNPA | `knpa` | ![knpa](badges/knpa/flat.svg) | ![knpa agency](badges/knpa/flat-agency.svg) |
| **소방청** | National Fire Agency | NFA | `nfa` | ![nfa](badges/nfa/flat.svg) | ![nfa agency](badges/nfa/flat-agency.svg) |
| **국가유산청** | Korea Heritage Service | KHS | `khs` | ![khs](badges/khs/flat.svg) | ![khs agency](badges/khs/flat-agency.svg) |
| **농촌진흥청** | Rural Development Administration | RDA | `rda` | ![rda](badges/rda/flat.svg) | ![rda agency](badges/rda/flat-agency.svg) |
| **산림청** | Korea Forest Service | KFS | `kfs` | ![kfs](badges/kfs/flat.svg) | ![kfs agency](badges/kfs/flat-agency.svg) |
| **특허청** | Korean Intellectual Property Office | KIPO | `kipo` | ![kipo](badges/kipo/flat.svg) | ![kipo agency](badges/kipo/flat-agency.svg) |
| **질병관리청** | Korea Disease Control and Prevention Agency | KDCA | `kdca` | ![kdca](badges/kdca/flat.svg) | ![kdca agency](badges/kdca/flat-agency.svg) |
| **기상청** | Korea Meteorological Administration | KMA | `kma` | ![kma](badges/kma/flat.svg) | ![kma agency](badges/kma/flat-agency.svg) |
| **해양경찰청** | Korea Coast Guard | KCG | `kcg` | ![kcg](badges/kcg/flat.svg) | ![kcg agency](badges/kcg/flat-agency.svg) |
| **우주항공청** | Korea AeroSpace Administration | KASA | `kasa` | ![kasa](badges/kasa/flat.svg) | ![kasa agency](badges/kasa/flat-agency.svg) |
| **재외동포청** | Overseas Koreans Agency | OKA | `oka` | ![oka](badges/oka/flat.svg) | ![oka agency](badges/oka/flat-agency.svg) |
| **행정중심복합도시건설청** | National Administrative City Construction Agency | NAACC | `naacc` | ![naacc](badges/naacc/flat.svg) | ![naacc agency](badges/naacc/flat-agency.svg) |
| **새만금개발청** | Saemangeum Development and Promotion Agency | SDPA | `sdpa` | ![sdpa](badges/sdpa/flat.svg) | ![sdpa agency](badges/sdpa/flat-agency.svg) |

### 4. 6위원회 (Commissions)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) | 고유/기관 배지 (`flat-agency.svg`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **방송통신위원회** | Korea Communications Commission | KCC | `kcc` | ![kcc](badges/kcc/flat.svg) | ![kcc agency](badges/kcc/flat-agency.svg) |
| **공정거래위원회** | Fair Trade Commission | FTC | `ftc` | ![ftc](badges/ftc/flat.svg) | ![ftc agency](badges/ftc/flat-agency.svg) |
| **금융위원회** | Financial Services Commission | FSC | `fsc` | ![fsc](badges/fsc/flat.svg) | ![fsc agency](badges/fsc/flat-agency.svg) |
| **국민권익위원회** | Anti-Corruption and Civil Rights Commission | ACRC | `acrc` | ![acrc](badges/acrc/flat.svg) | ![acrc agency](badges/acrc/flat-agency.svg) |
| **개인정보보호위원회** | Personal Information Protection Commission | PIPC | `pipc` | ![pipc](badges/pipc/flat.svg) | ![pipc agency](badges/pipc/flat-agency.svg) |
| **원자력안전위원회** | Nuclear Safety and Security Commission | NSSC | `nssc` | ![nssc](badges/nssc/flat.svg) | ![nssc agency](badges/nssc/flat-agency.svg) |

### 5. 기타 국가기관 (Institutes & Others)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) | 고유/기관 배지 (`flat-agency.svg`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **감사원** | Board of Audit and Inspection | BAI | `bai` | ![bai](badges/bai/flat.svg) | ![bai agency](badges/bai/flat-agency.svg) |
| **국가정보원** | National Intelligence Service | NIS | `nis` | ![nis](badges/nis/flat.svg) | ![nis agency](badges/nis/flat-agency.svg) |

---

## 🛠️ 배지 생성 및 테스트

새로운 기관 추가나 배지 스타일 수정 시 아래 명령어를 통해 배지를 재빌드하고 무결성을 검증할 수 있습니다.

```sh
# 1. 52개 기관 2,860개 SVG 배지 생성
python3 scripts/generate.py

# 2. 단위 테스트 실행 (데이터 무결성, SVG 유효성, 보안 태그 검증)
python3 -m unittest discover -s tests -v

# 3. 배지 생성 결과 일치성 검증 (CI 검증용)
python3 scripts/generate.py --check
```

---

## 📐 설계 원칙

1. **Self-contained SVG**:
   - 모든 배지는 태극기 및 각 기관 고유 엠블럼의 벡터 패스를 파일 내부에 직접 포함합니다.
   - 외부 폰트 파일이나 외부 이미지 링크에 의존하지 않고 어디서나 완벽하게 렌더링됩니다.
2. **이중 경로(Alias) 지원**:
   - URL 작성의 편의를 위해 영문 소문자 Slug(`mois`)와 한국어 정식 명칭(`행정안전부`) 폴더 경로를 모두 생성합니다.
3. **가독성 최적화 타이포그래피 및 동적 아이콘 마운팅**:
   - 국기(3:2 비율), 정방형 엠블럼(1:1), 횡형 상징(새매, 봉황 등) 등 다양한 심벌의 가로세로 비율을 수학적으로 자동 계산하여 6px의 일관된 여백으로 텍스트와 정렬합니다.
   - 시스템 폰트 스택(`-apple-system`, `Noto Sans KR`, `Malgun Gothic` 등)을 선언하여 모든 OS에서 선명한 한글을 지원합니다.
4. **CI 무결성 보증**:
   - GitHub Actions 워크플로를 통해 `generate.py --check`가 자동으로 수행되어 생성물과 소스 코드 간의 일치를 항시 보장합니다.

---

## 📄 라이선스

- **코드 라이선스**: 본 저장소의 빌드 스크립트, 테스트 코드 및 CI 설정은 [MIT License](LICENSE)에 따라 자유롭게 사용 및 수정하실 수 있습니다.
- **국가상징 및 기관 상징 저작권 안내**: 배지에 포함된 대한민국 국기(태극기), 정부상징(GI) 및 각 정부 부처/기관의 공식 엠블럼과 명칭에 대한 권리는 대한민국 정부 및 각 해당 기관에 귀속됩니다. 공공기관의 공식 명칭 및 상징을 허위로 도용하거나 정부 기관을 사칭하는 용도로 사용할 수 없습니다.
