# Korea Gov Badge (대한민국 정부 기관 배지)

대한민국 중앙행정기관(19부, 처, 청, 위원회 등 총 52개 기관)을 위한 오픈소스 SVG 배지 모음입니다. 공공 소프트웨어, 정부 R&D 과제, 공공데이터 연계 프로젝트, [전자정부 표준프레임워크(eGovFrame)](https://github.com/leejongyoung/egovframe-badge) 기반 시스템 등의 README에서 소관 부처 및 기관을 명확하게 표시할 수 있습니다.

별도의 배포 서버나 JavaScript 없이 GitHub raw URL 한 줄로 즉시 임베드할 수 있는 자립형(self-contained) 정적 SVG입니다.

---

## 한 줄로 사용

원하는 기관의 식별자 ID(`mois`, `mnd`, `knpa` 등) 또는 한글 기관명(`행정안전부`, `국방부`, `경찰청` 등)과 스타일을 URL 경로에서 선택합니다.

```md
[![행정안전부 MOIS](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/mois/flat.svg)](https://www.mois.go.kr)
```

한글 기관명 폴더 경로도 100% 동일하게 지원합니다:
```md
[![경찰청 KNPA](https://raw.githubusercontent.com/leejongyoung/korea-gov-badge/main/badges/경찰청/flat.svg)](https://www.police.go.kr)
```

---

## 공식 상징 적용 안내

각 기관의 성격과 공식 상징 체계에 맞추어 심벌이 자동 적용됩니다:

1. **독자 고유 로고 사용 기관**:
   - 2016년 정부상징 통합 대상에서 제외되어 고유 상징을 유지하는 기관(**국방부, 경찰청, 국가정보원, 소방청, 해양경찰청, 검찰청, 감사원, 대통령비서실**)은 **해당 기관의 공식 고유 엠블럼**이 배지에 포함됩니다.
2. **정부상징 통합 사용 부처**:
   - 대한민국 정부상징(GI)을 사용하는 18개 부 및 각 처·청·위원회는 **대한민국 정부상징(GI)** 태극 문양이 적용됩니다.

---

## 스타일 미리보기

[shields.io](https://shields.io)의 대표 스타일(`flat`, `flat-square`, `plastic`, `for-the-badge`)과 전용 `outline` 스타일을 제공합니다. 모든 스타일은 깔끔한 화이트/블루 톤앤매너로 통일되어 있습니다.

| 스타일 | 경찰청 (`knpa`) | 국방부 (`mnd`) | 행정안전부 (`mois`) |
| :--- | :--- | :--- | :--- |
| **flat** | ![knpa flat](badges/knpa/flat.svg) | ![mnd flat](badges/mnd/flat.svg) | ![mois flat](badges/mois/flat.svg) |
| **flat-square** | ![knpa flat-square](badges/knpa/flat-square.svg) | ![mnd flat-square](badges/mnd/flat-square.svg) | ![mois flat-square](badges/mois/flat-square.svg) |
| **plastic** | ![knpa plastic](badges/knpa/plastic.svg) | ![mnd plastic](badges/mnd/plastic.svg) | ![mois plastic](badges/mois/plastic.svg) |
| **for-the-badge** | ![knpa for-the-badge](badges/knpa/for-the-badge.svg) | ![mnd for-the-badge](badges/mnd/for-the-badge.svg) | ![mois for-the-badge](badges/mois/for-the-badge.svg) |
| **outline** | ![knpa outline](badges/knpa/outline.svg) | ![mnd outline](badges/mnd/outline.svg) | ![mois outline](badges/mois/outline.svg) |

---

## 독자 엠블럼 사용 기관 배지

| 기관명 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) |
| :--- | :---: | :---: | :--- |
| **국방부** | MND | `mnd` | ![mnd](badges/mnd/flat.svg) |
| **경찰청** | KNPA | `knpa` | ![knpa](badges/knpa/flat.svg) |
| **국가정보원** | NIS | `nis` | ![nis](badges/nis/flat.svg) |
| **소방청** | NFA | `nfa` | ![nfa](badges/nfa/flat.svg) |
| **해양경찰청** | KCG | `kcg` | ![kcg](badges/kcg/flat.svg) |
| **검찰청** | SPO | `spo` | ![spo](badges/spo/flat.svg) |
| **감사원** | BAI | `bai` | ![bai](badges/bai/flat.svg) |
| **대통령비서실** | PRESIDENT | `president` | ![president](badges/president/flat.svg) |

---

## 지원 기관 목록 (총 52개 기관)

최신 대한민국 정부조직법 및 개편 현황(우주항공청, 국가유산청, 재외동포청 개청 등 반영)을 준수하는 52개 기관의 배지를 제공합니다.

### 1. 19부 (Ministries)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) |
| :--- | :--- | :--- | :--- | :--- |
| **기획재정부** | Ministry of Economy and Finance | MOEF | `moef` | ![moef](badges/moef/flat.svg) |
| **교육부** | Ministry of Education | MOE | `moe` | ![moe](badges/moe/flat.svg) |
| **과학기술정보통신부** | Ministry of Science and ICT | MSIT | `msit` | ![msit](badges/msit/flat.svg) |
| **외교부** | Ministry of Foreign Affairs | MOFA | `mofa` | ![mofa](badges/mofa/flat.svg) |
| **통일부** | Ministry of Unification | MOU | `mou` | ![mou](badges/mou/flat.svg) |
| **법무부** | Ministry of Justice | MOJ | `moj` | ![moj](badges/moj/flat.svg) |
| **국방부** | Ministry of National Defense | MND | `mnd` | ![mnd](badges/mnd/flat.svg) |
| **행정안전부** | Ministry of the Interior and Safety | MOIS | `mois` | ![mois](badges/mois/flat.svg) |
| **국가보훈부** | Ministry of Patriots and Veterans Affairs | MPVA | `mpva` | ![mpva](badges/mpva/flat.svg) |
| **문화체육관광부** | Ministry of Culture, Sports and Tourism | MCST | `mcst` | ![mcst](badges/mcst/flat.svg) |
| **농림축산식품부** | Ministry of Agriculture, Food and Rural Affairs | MAFRA | `mafra` | ![mafra](badges/mafra/flat.svg) |
| **산업통상자원부** | Ministry of Trade, Industry and Energy | MOTIE | `motie` | ![motie](badges/motie/flat.svg) |
| **보건복지부** | Ministry of Health and Welfare | MOHW | `mohw` | ![mohw](badges/mohw/flat.svg) |
| **환경부** | Ministry of Environment | ME | `me` | ![me](badges/me/flat.svg) |
| **고용노동부** | Ministry of Employment and Labor | MOEL | `moel` | ![moel](badges/moel/flat.svg) |
| **여성가족부** | Ministry of Gender Equality and Family | MOGEF | `mogef` | ![mogef](badges/mogef/flat.svg) |
| **국토교통부** | Ministry of Land, Infrastructure and Transport | MOLIT | `molit` | ![molit](badges/molit/flat.svg) |
| **해양수산부** | Ministry of Oceans and Fisheries | MOF | `mof` | ![mof](badges/mof/flat.svg) |
| **중소벤처기업부** | Ministry of SMEs and Startups | MSS | `mss` | ![mss](badges/mss/flat.svg) |

### 2. 처 / 실 (Offices & Ministries)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) |
| :--- | :--- | :--- | :--- | :--- |
| **인사혁신처** | Ministry of Personnel Management | MPM | `mpm` | ![mpm](badges/mpm/flat.svg) |
| **법제처** | Ministry of Government Legislation | MOLEG | `moleg` | ![moleg](badges/moleg/flat.svg) |
| **식품의약품안전처** | Ministry of Food and Drug Safety | MFDS | `mfds` | ![mfds](badges/mfds/flat.svg) |
| **국무조정실** | Office for Government Policy Coordination | OPC | `opm` | ![opm](badges/opm/flat.svg) |
| **대통령비서실** | Office of the President | PRESIDENT | `president` | ![president](badges/president/flat.svg) |

### 3. 20청 (Administrations & Agencies)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) |
| :--- | :--- | :--- | :--- | :--- |
| **국세청** | National Tax Service | NTS | `nts` | ![nts](badges/nts/flat.svg) |
| **관세청** | Korea Customs Service | KCS | `kcs` | ![kcs](badges/kcs/flat.svg) |
| **조달청** | Public Procurement Service | PPS | `pps` | ![pps](badges/pps/flat.svg) |
| **통계청** | Statistics Korea | KOSTAT | `kostat` | ![kostat](badges/kostat/flat.svg) |
| **검찰청** | Supreme Prosecutors' Office | SPO | `spo` | ![spo](badges/spo/flat.svg) |
| **병무청** | Military Manpower Administration | MMA | `mma` | ![mma](badges/mma/flat.svg) |
| **방위사업청** | Defense Acquisition Program Administration | DAPA | `dapa` | ![dapa](badges/dapa/flat.svg) |
| **경찰청** | Korean National Police Agency | KNPA | `knpa` | ![knpa](badges/knpa/flat.svg) |
| **소방청** | National Fire Agency | NFA | `nfa` | ![nfa](badges/nfa/flat.svg) |
| **국가유산청** | Korea Heritage Service | KHS | `khs` | ![khs](badges/khs/flat.svg) |
| **농촌진흥청** | Rural Development Administration | RDA | `rda` | ![rda](badges/rda/flat.svg) |
| **산림청** | Korea Forest Service | KFS | `kfs` | ![kfs](badges/kfs/flat.svg) |
| **특허청** | Korean Intellectual Property Office | KIPO | `kipo` | ![kipo](badges/kipo/flat.svg) |
| **질병관리청** | Korea Disease Control and Prevention Agency | KDCA | `kdca` | ![kdca](badges/kdca/flat.svg) |
| **기상청** | Korea Meteorological Administration | KMA | `kma` | ![kma](badges/kma/flat.svg) |
| **해양경찰청** | Korea Coast Guard | KCG | `kcg` | ![kcg](badges/kcg/flat.svg) |
| **우주항공청** | Korea AeroSpace Administration | KASA | `kasa` | ![kasa](badges/kasa/flat.svg) |
| **재외동포청** | Overseas Koreans Agency | OKA | `oka` | ![oka](badges/oka/flat.svg) |
| **행정중심복합도시건설청** | National Administrative City Construction Agency | NAACC | `naacc` | ![naacc](badges/naacc/flat.svg) |
| **새만금개발청** | Saemangeum Development and Promotion Agency | SDPA | `sdpa` | ![sdpa](badges/sdpa/flat.svg) |

### 4. 6위원회 (Commissions)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) |
| :--- | :--- | :--- | :--- | :--- |
| **방송통신위원회** | Korea Communications Commission | KCC | `kcc` | ![kcc](badges/kcc/flat.svg) |
| **공정거래위원회** | Fair Trade Commission | FTC | `ftc` | ![ftc](badges/ftc/flat.svg) |
| **금융위원회** | Financial Services Commission | FSC | `fsc` | ![fsc](badges/fsc/flat.svg) |
| **국민권익위원회** | Anti-Corruption and Civil Rights Commission | ACRC | `acrc` | ![acrc](badges/acrc/flat.svg) |
| **개인정보보호위원회** | Personal Information Protection Commission | PIPC | `pipc` | ![pipc](badges/pipc/flat.svg) |
| **원자력안전위원회** | Nuclear Safety and Security Commission | NSSC | `nssc` | ![nssc](badges/nssc/flat.svg) |

### 5. 기타 국가기관 (Institutes & Others)

| 기관명 | 영문 명칭 | 영문 약칭 | 식별자 (Slug) | 배지 미리보기 (`flat.svg`) |
| :--- | :--- | :--- | :--- | :--- |
| **감사원** | Board of Audit and Inspection | BAI | `bai` | ![bai](badges/bai/flat.svg) |
| **국가정보원** | National Intelligence Service | NIS | `nis` | ![nis](badges/nis/flat.svg) |

---

## 배지 생성 및 테스트

새로운 기관 추가나 배지 스타일 수정 시 아래 명령어를 통해 배지를 재빌드하고 무결성을 검증할 수 있습니다.

```sh
# 1. 52개 기관 1,560개 SVG 배지 생성
python3 scripts/generate.py

# 2. 단위 테스트 실행 (데이터 무결성, SVG 유효성, 보안 태그 검증)
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
   - URL 작성의 편의를 위해 영문 소문자 Slug(`mois`)와 한국어 정식 명칭(`행정안전부`) 폴더 경로를 모두 지원합니다.
3. **가독성 최적화 타이포그래피 및 동적 아이콘 마운팅**:
   - 정방형 엠블럼, 횡형 상징(새매, 봉황) 등 다양한 심벌의 고유 비율을 수학적으로 자동 계산하여 6px의 일관된 여백으로 텍스트와 정렬합니다.
   - 시스템 폰트 스택(`-apple-system`, `Noto Sans KR`, `Malgun Gothic` 등)을 선언하여 모든 OS에서 선명한 한글을 지원합니다.
4. **통일된 색상 팔레트**:
   - shields.io 호환 스타일 및 for-the-badge 스타일 모두 화이트 레이블(#ffffff)과 공공 블루 메시지(#134f8c)로 톤앤매너를 통일하여 시각적 안정감을 제공합니다.
5. **CI 무결성 보증**:
   - GitHub Actions 워크플로를 통해 `generate.py --check`가 자동으로 수행되어 생성물과 소스 코드 간의 일치를 항시 보장합니다.

---

## 라이선스

- **코드 라이선스**: 본 저장소의 빌드 스크립트, 테스트 코드 및 CI 설정은 [MIT License](LICENSE)에 따라 자유롭게 사용 및 수정하실 수 있습니다.
- **국가상징 및 기관 상징 저작권 안내**: 배지에 포함된 대한민국 정부상징(GI) 및 각 정부 부처/기관의 공식 엠블럼과 명칭에 대한 권리는 대한민국 정부 및 각 해당 기관에 귀속됩니다. 공공기관의 공식 명칭 및 상징을 허위로 도용하거나 정부 기관을 사칭하는 용도로 사용할 수 없습니다.
