# Arabic Name Generator MCP

아랍어 이름을 생성하고 의미를 해석하는 MCP (Model Context Protocol) 서버입니다.

## 기능

- 키워드 기반 아랍어 이름 생성
- 아랍어 이름의 의미 해석
- 한글 음성 표기 제공
- 다양한 스타일 지원 (전통적, 현대적, 왕족, 시적, 종교적)

## 설치

```bash
pip install -r requirements.txt
```

## 사용법

```bash
python main.py
```

## 지원하는 키워드 카테고리

- 자연/우주: star, moon, sun, ocean, desert, mountain, flower, garden
- 성격/감정: brave, wise, beautiful, kind, strong, peaceful, joyful, noble
- 색깔: white, black, red, blue, green, golden
- 직업/지위: scholar, leader, merchant, warrior, poet, doctor
- 보석: pearl, diamond, ruby, emerald
- 종교/영성: faith, prayer, light, blessing
- 동물: lion, falcon, horse, gazelle

## 예시

```python
# 별과 용감함을 키워드로 하는 남성 이름 3개 생성
generate_arabic_name(
    keywords=["star", "brave"],
    gender="male",
    style="traditional",
    count=3
)
```
