# Arabic Name Generator MCP 배포 가이드

이 문서는 Arabic Name Generator MCP 서버를 FastMCP Cloud에 배포하는 방법을 설명합니다.

## 🚀 배포 프로세스

### 1단계: 프로젝트 설정 확인

현재 프로젝트 구조:
```
arabic-name-generator-mcp/
├── main.py          # 메인 애플리케이션
├── requirements.txt # 의존성 관리
├── README.md        # 프로젝트 문서
├── .gitignore       # Git 무시 파일
└── DEPLOYMENT.md    # 배포 가이드 (이 파일)
```

### 2단계: GitHub 배포

```bash
# 1. Git 초기화 (아직 안했다면)
git init

# 2. 파일 추가 및 커밋
git add .
git commit -m "Initial commit: Arabic Name Generator MCP 서버"

# 3. GitHub 레포지토리 생성
gh repo create arabic-name-generator-mcp --public --description "아랍어 이름 생성 및 의미 해석 MCP 서버"

# 4. 원격 저장소 연결 및 푸시
git remote add origin https://github.com/사용자명/arabic-name-generator-mcp.git
git push -u origin main
```

### 3단계: FastMCP Cloud 배포

1. **FastMCP Cloud 접속**
   - https://fastmcp.cloud 방문
   - GitHub 계정으로 로그인

2. **프로젝트 생성**
   - "Create a Project" 클릭
   - `arabic-name-generator-mcp` 레포지토리 선택

3. **프로젝트 설정**
   - **Server Name**: `arabic-name-generator-mcp`
   - **Entrypoint**: `main.py`
   - **Authentication**: 필요에 따라 설정
   - **Discoverable**: 공개 여부 설정

4. **배포 실행**
   - "Deploy Server" 클릭
   - 자동 빌드 및 배포 완료 대기

## 📋 배포된 서버 정보

### 서버 설정
- **서버 URL**: `https://arabic-name-generator-mcp.fastmcp.app/mcp`
- **Entry Point**: `main.py`
- **Repository**: `https://github.com/사용자명/arabic-name-generator-mcp`

### 구현된 기능
1. **`generate_arabic_name`** - 키워드 기반 아랍어 이름 생성
2. **`get_arabic_name_meaning`** - 아랍어 이름의 의미 해석
3. **`suggest_arabic_name_keywords`** - 사용 가능한 키워드 제안

## 🔧 MCP 클라이언트 연결 설정

### Claude Desktop 설정 (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "arabic-name-generator-mcp": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://arabic-name-generator-mcp.fastmcp.app/mcp"]
    }
  }
}
```

### Cursor 설정
```json
{
  "mcpServers": {
    "arabic-name-generator-mcp": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://arabic-name-generator-mcp.fastmcp.app/mcp"]
    }
  }
}
```

## 🔄 업데이트 배포

```bash
# 1. 코드 수정 후 커밋
git add .
git commit -m "기능 업데이트: 설명"

# 2. GitHub에 푸시
git push origin main

# 3. FastMCP Cloud에서 자동 재배포
# (main 브랜치에 푸시하면 자동으로 재배포됨)
```

## 🧪 로컬 테스트

```bash
# MCP Inspector로 로컬 테스트
fastmcp dev main.py
```

## 📚 참고 자료

- [FastMCP 공식 문서](https://gofastmcp.com/)
- [MCP 프로토콜](https://modelcontextprotocol.io/)
- [FastMCP Cloud](https://fastmcp.cloud)

---

**마지막 업데이트**: 2025년 1월 17일
**프로젝트**: Arabic Name Generator MCP
