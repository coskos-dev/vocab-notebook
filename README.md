# 영어 공부장 (Daily English Notebook)

매일 자동으로 비즈니스 뉴스를 모아서 보여주는 개인 웹사이트입니다.
GitHub Actions가 매일 아침 6시(KST)에 자동으로 뉴스를 가져와 저장하고,
GitHub Pages가 그 내용을 웹사이트로 보여줍니다. 비용은 전혀 들지 않습니다.

## 처음 설정하는 방법 (한 번만 하면 됨)

### 1. GitHub에 새 저장소(repository) 만들기
1. github.com 로그인 후 우측 상단 `+` → `New repository`
2. Repository name: `vocab-notebook` (원하는 이름으로 자유롭게)
3. **Public** 선택 (Pages를 무료로 쓰려면 Public 추천)
4. `Create repository` 클릭

### 2. 이 파일들을 저장소에 올리기
GitHub Desktop을 이미 설치하셨다면:
1. GitHub Desktop 실행 → `File` → `Add Local Repository`
2. 이 폴더(`vocab-notebook`) 전체를 선택
3. 만약 "This is not a git repository" 라고 뜨면 `create a repository` 클릭
4. 좌측 하단에 커밋 메시지 입력 (예: `첫 설정`) → `Commit to main`
5. 우측 상단 `Publish repository` 클릭 → 아까 만든 저장소 이름과 연결

### 3. GitHub Pages 켜기
1. 저장소 페이지에서 `Settings` 탭
2. 왼쪽 메뉴에서 `Pages` 클릭
3. `Source`를 `Deploy from a branch`로, `Branch`는 `main` / `/ (root)` 선택 후 `Save`
4. 몇 분 후 `https://[내아이디].github.io/vocab-notebook/` 주소로 접속 가능

### 4. Actions가 파일을 저장할 수 있게 권한 켜기 (중요!)
1. `Settings` → 왼쪽 메뉴 `Actions` → `General`
2. 아래로 스크롤 → `Workflow permissions`
3. `Read and write permissions` 선택 → `Save`
   *(이걸 안 하면 매일 자동 수집한 내용이 저장이 안 돼요)*

### 5. 잘 작동하는지 테스트해보기
1. 저장소 상단 `Actions` 탭 클릭
2. 왼쪽에서 `Daily News Fetch` 클릭
3. 오른쪽 `Run workflow` 버튼 → `Run workflow` 다시 클릭
4. 1분 정도 기다린 후 초록색 체크가 뜨면 성공!
5. 사이트를 새로고침하면 실제 뉴스가 채워져 있어야 해요

## 이후에는?
- 매일 새벽 6시(KST)에 자동으로 실행되어 새 기사가 쌓입니다.
- 아무것도 안 하셔도 됩니다. 그냥 매일 사이트에 들어가서 확인만 하면 돼요.
- 기사 카드의 "읽음 표시" 체크는 내 브라우저에만 저장돼요 (다른 기기에서는 안 보여요).

## 폴더 구조
```
vocab-notebook/
├── index.html                 # 웹사이트 (이 파일이 화면에 보이는 페이지)
├── data/articles.json         # 수집된 기사 데이터 (자동으로 업데이트됨)
├── scripts/fetch_news.py      # RSS를 가져오는 파이썬 스크립트
├── requirements.txt           # 파이썬 패키지 목록
└── .github/workflows/
    └── daily-fetch.yml        # 매일 자동 실행 설정
```

## 다음 단계 아이디어
지금은 뉴스 "원문"만 자동으로 모으는 단계예요. 나중에 원하시면:
- Claude API를 연결해서 기사에서 고급 표현을 자동으로 뽑아 정리
- 카카오톡/이메일로 아침에 알림 보내기
- 표현을 플래시카드처럼 복습하는 기능 추가

이 중 뭐든 원하시면 언제든 다시 요청해주세요.
