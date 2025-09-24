from fastmcp import FastMCP
from typing import List, Optional, Set
import random
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MCP 서버 생성
mcp = FastMCP("ArabicNameGenerator")

# 아랍어 이름 구성 요소 (영어 표기)
MALE_PREFIXES = [
    "Abdul", "Abu", "Ahmad", "Ali", "Hassan", "Hussein", "Ibrahim", "Khalil", 
    "Mohammed", "Omar", "Rashid", "Said", "Tariq", "Yusuf", "Zaid", "Jamal"
]

FEMALE_PREFIXES = [
    "Aisha", "Amina", "Fatima", "Khadija", "Layla", "Maryam", "Nadia", "Safiya",
    "Zara", "Yasmin", "Lina", "Dina", "Rana", "Hala", "Rima", "Soraya"
]

# 아랍어 이름의 한글 음성 표기 사전 (중복 제거됨)
ARABIC_TO_KOREAN_PRONUNCIATION = {
    # 남성 이름 접두사
    "Abdul": "압둘", "Abu": "아부", "Ahmad": "아흐마드", "Ali": "알리", 
    "Hassan": "하산", "Hussein": "후세인", "Ibrahim": "이브라힘", "Khalil": "칼릴",
    "Mohammed": "무함마드", "Omar": "오마르", "Rashid": "라시드", "Said": "사이드", 
    "Tariq": "타리크", "Yusuf": "유수프", "Zaid": "자이드", "Jamal": "자말",
    
    # 여성 이름 접두사
    "Aisha": "아이샤", "Amina": "아미나", "Fatima": "파티마", "Khadija": "카디자",
    "Layla": "라일라", "Maryam": "마리얌", "Nadia": "나디아", "Safiya": "사피야",
    "Zara": "자라", "Yasmin": "야스민", "Lina": "리나", "Dina": "디나", 
    "Rana": "라나", "Hala": "할라", "Rima": "리마", "Soraya": "소라야",
    
    # 자연/우주 관련 키워드 요소들
    "Najm": "나즘", "Kawkab": "카우카브", "Thuraya": "투라야", "Shams": "샴스",
    "Qamar": "카마르", "Nujum": "누줌", "Hilal": "힐랄", "Badr": "바드르",
    "Luna": "루나", "Kamira": "카미라", "Qamra": "카므라", "Diya": "디야",
    "Nour": "누르", "Bahir": "바히르", "Munir": "무니르", "Siraj": "시라즈",
    "Bahr": "바흐르", "Yamm": "얌", "Lujain": "루자인", "Safina": "사피나",
    "Mawj": "마우즈", "Ghaith": "가이스", "Sahra": "사흐라", "Raml": "람르",
    "Badiya": "바디야", "Sahir": "사히르", "Qafila": "카필라", "Barr": "바르",
    "Jabal": "자발", "Sakhir": "사키르", "Qasim": "카심", "Tall": "탈르",
    "Hadi": "하디", "Ras": "라스", "Ward": "와르드", "Narjis": "나르지스", 
    "Zahra": "자흐라", "Rihan": "리한", "Rayhan": "라이한", "Bustan": "부스탄", 
    "Hadiqah": "하디카", "Firdaus": "피르다우스", "Riyad": "리야드", "Jannah": "잔나", 
    "Rawda": "라우다",
    
    # 성격/감정 관련
    "Shuja": "슈자", "Qawi": "카위", "Jasur": "자수르", "Battal": "바탈", 
    "Hamza": "함자", "Usama": "우사마", "Hakim": "하킴", "Alim": "알림", 
    "Najib": "나지브", "Fahim": "파힘", "Akil": "아킬", "Jamil": "자밀", 
    "Husn": "후슨", "Zain": "자인", "Hilwa": "힐와", "Karim": "카림", 
    "Rahman": "라흐만", "Halim": "할림", "Latif": "라티프", "Rauf": "라우프", 
    "Sabur": "사부르", "Aziz": "아지즈", "Shahir": "샤히르", "Qadur": "카두르", 
    "Jalil": "자릴", "Majid": "마지드", "Salim": "살림", "Amin": "아민", 
    "Sakina": "사키나", "Salam": "살람", "Rahma": "라흐마", "Wadud": "와두드",
    "Farah": "파라", "Surur": "수루르", "Bashir": "바시르", "Masrur": "마스루르", 
    "Farhan": "파르한", "Mubashir": "무바시르", "Sharif": "샤리프", "Asil": "아실", 
    "Muhtaram": "무흐타람", "Sayyid": "사이드",
    
    # 색깔 관련
    "Abyad": "아브야드", "Bayda": "바이다", "Naqi": "나키", "Zahir": "자히르", 
    "Barid": "바리드", "Aswad": "아스와드", "Ghazal": "가잔", "Habashi": "하바시", 
    "Sudan": "수단", "Kahla": "카흘라", "Ahmar": "아흐마르", "Sumaq": "수마크", 
    "Hamra": "함라", "Aqiq": "아키크", "Marjan": "마르잔", "Azraq": "아즈라크", 
    "Sama": "사마", "Zarqa": "자르카", "Firouz": "피루즈", "Akhdar": "아흐다르", 
    "Zaytun": "자이툰", "Khadir": "카디르", "Hadra": "하드라", "Dhahabi": "다하비", 
    "Tibr": "티브르", "Zahab": "자하브", "Nurani": "누라니", "Qirat": "키라트",
    
    # 직업/지위 관련
    "Faqih": "파키흐", "Qari": "카리", "Hafiz": "하피즈", "Ustaz": "우스타즈", 
    "Shaykh": "샤이크", "Amir": "아미르", "Malik": "말릭", "Sultan": "술탄", 
    "Qaid": "카이드", "Zaim": "자임", "Mudir": "무디르", "Tajir": "타지르", 
    "Baya": "바야", "Ghaniy": "가니", "Muyassar": "무야사르", "Kasib": "카시브", 
    "Muhajir": "무하지르", "Ghazi": "가지", "Faris": "파리스", "Mujahid": "무자히드",
    "Shair": "샤이르", "Adib": "아딥", "Balaghiy": "발라기", "Fasih": "파시흐", 
    "Qalam": "카람", "Nazim": "나짐", "Tabib": "타비브", "Shafi": "샤피", 
    "Dawa": "다와", "Ilaj": "일라즈", "Seha": "세하",
    
    # 보석/귀한 것들
    "Lulu": "룰루", "Durra": "두라", "Jawhar": "자우하르", "Yakut": "야쿠트", 
    "Firoza": "피루자", "Almas": "알마스", "Bariq": "바리크", "Lama": "라마", 
    "Sana": "사나", "Zumrud": "줌루드", "Zabarjad": "자바르자드", "Zaytuni": "자이투니", 
    "Sabz": "사브즈",
    
    # 종교/영성 관련
    "Iman": "이만", "Din": "딘", "Taqwa": "타크와", "Yaqin": "야킨", 
    "Salah": "살라", "Hidaya": "히다야", "Dua": "두아", "Dhikr": "디크르", 
    "Tasbih": "타스비흐", "Wird": "위르드", "Munajat": "무나자트", "Ishraq": "이슈라크",
    "Baraka": "바라카", "Nima": "니마", "Fadl": "파들", "Khayr": "카이르", 
    "Lutf": "루트프",
    
    # 동물 관련
    "Asad": "아사드", "Layth": "라이스", "Hayder": "하이더", "Ghada": "가다", 
    "Saqr": "사크르", "Shahin": "샤힌", "Baz": "바즈", "Tair": "타이르", 
    "Sarim": "사림", "Faras": "파라스", "Jawad": "자와드", "Hisan": "히산", 
    "Reem": "림", "Mahir": "마히르", "Sawsan": "사우산",
    
    # 추가 종교적 이름들
    "Rahim": "라힘", "Quddus": "쿠두스", "Fadil": "파딜", "Nadir": "나디르"
}

def get_korean_pronunciation(arabic_name: str) -> str:
    """
    아랍어 이름을 한글 음성 표기로 변환합니다.
    
    Args:
        arabic_name: 아랍어 이름 (영어 표기)
        
    Returns:
        str: 한글 음성 표기
    """
    # 이름을 공백으로 분리
    name_parts = arabic_name.split()
    korean_parts = []
    
    for part in name_parts:
        if part in ARABIC_TO_KOREAN_PRONUNCIATION:
            korean_parts.append(ARABIC_TO_KOREAN_PRONUNCIATION[part])
        else:
            # 사전에 없는 경우 기본 변환 시도
            korean_parts.append(part)
    
    return " ".join(korean_parts)

def format_name_display(arabic_name: str) -> str:
    """
    아랍어 이름을 "Arabic (한글음차)" 형식으로 표시합니다.
    
    Args:
        arabic_name: 아랍어 이름 (영어 표기)
        
    Returns:
        str: 형식화된 이름 표시
    """
    korean = get_korean_pronunciation(arabic_name)
    return f"{arabic_name} ({korean})"

# 키워드별 아랍어 이름 요소들 (의미 기반, 중복 제거됨)
KEYWORD_ELEMENTS = {
    # 자연/우주 관련
    "star": ["Najm", "Kawkab", "Thuraya", "Nujum"],
    "moon": ["Qamar", "Hilal", "Badr", "Kamira"], 
    "sun": ["Shams", "Diya", "Nour", "Bahir", "Munir", "Siraj"],
    "ocean": ["Bahr", "Yamm", "Lujain", "Safina", "Mawj", "Ghaith"],
    "desert": ["Sahra", "Raml", "Badiya", "Sahir", "Qafila", "Barr"],
    "mountain": ["Jabal", "Sakhir", "Qasim", "Tall", "Hadi", "Ras"],
    "flower": ["Ward", "Yasmin", "Narjis", "Zahra", "Rihan", "Rayhan"],
    "garden": ["Bustan", "Hadiqah", "Firdaus", "Riyad", "Jannah", "Rawda"],
    
    # 감정/성격 관련
    "brave": ["Shuja", "Qawi", "Jasur", "Battal", "Hamza", "Usama"],
    "wise": ["Hakim", "Rashid", "Alim", "Najib", "Fahim", "Akil"],
    "beautiful": ["Jamil", "Husn", "Zain", "Hilwa", "Bahir"],
    "kind": ["Karim", "Rahman", "Halim", "Latif", "Rauf", "Sabur"],
    "strong": ["Qawi", "Aziz", "Shahir", "Qadur", "Jalil", "Majid"],
    "peaceful": ["Salim", "Amin", "Sakina", "Salam", "Rahma", "Wadud"],
    "joyful": ["Farah", "Surur", "Bashir", "Masrur", "Farhan", "Mubashir"],
    "noble": ["Sharif", "Najib", "Asil", "Karim", "Muhtaram", "Sayyid"],
    
    # 색깔 관련
    "white": ["Abyad", "Safiya", "Bayda", "Naqi", "Zahir", "Barid"],
    "black": ["Aswad", "Layla", "Ghazal", "Habashi", "Sudan", "Kahla"],
    "red": ["Ahmar", "Ward", "Sumaq", "Hamra", "Aqiq", "Marjan"],
    "blue": ["Azraq", "Sama", "Lujain", "Zarqa", "Firouz", "Bahr"],
    "green": ["Akhdar", "Zaytun", "Khadir", "Rayhan", "Hadra"],
    "golden": ["Dhahabi", "Tibr", "Zahab", "Nurani", "Asil", "Qirat"],
    
    # 직업/지위 관련
    "scholar": ["Alim", "Faqih", "Qari", "Hafiz", "Ustaz", "Shaykh"],
    "leader": ["Amir", "Malik", "Sultan", "Qaid", "Zaim", "Mudir"],
    "merchant": ["Tajir", "Baya", "Ghaniy", "Muyassar", "Kasib"],
    "warrior": ["Muhajir", "Ghazi", "Faris", "Mujahid", "Battal", "Hamza"],
    "poet": ["Shair", "Adib", "Balaghiy", "Fasih", "Qalam", "Nazim"],
    "doctor": ["Tabib", "Hakim", "Shafi", "Dawa", "Ilaj", "Seha"],
    
    # 보석/귀한 것들
    "pearl": ["Lulu", "Durra", "Jawhar", "Marjan"],
    "diamond": ["Almas", "Jawhar", "Bariq", "Lama", "Sana", "Zahir"],
    "ruby": ["Yakut", "Ahmar", "Marjan", "Aqiq", "Sumaq", "Hamra"],
    "emerald": ["Zumrud", "Akhdar", "Zabarjad", "Zaytuni", "Khadir", "Sabz"],
    
    # 종교/영성 관련
    "faith": ["Iman", "Din", "Taqwa", "Yaqin", "Salah", "Hidaya"],
    "prayer": ["Salah", "Dua", "Dhikr", "Tasbih", "Wird", "Munajat"],
    "light": ["Nour", "Diya", "Siraj", "Munir", "Bahir", "Ishraq"],
    "blessing": ["Baraka", "Nima", "Fadl", "Khayr", "Rahma", "Lutf"],
    
    # 동물 관련
    "lion": ["Asad", "Layth", "Hayder", "Ghada", "Usama", "Hamza"],
    "falcon": ["Saqr", "Shahin", "Baz", "Tair", "Sarim"],
    "horse": ["Faras", "Jawad", "Hisan", "Asil"],
    "gazelle": ["Ghazal", "Reem", "Mahir", "Rana", "Sawsan"]
}

@mcp.tool
def generate_arabic_name(
    keywords: List[str],
    gender: Optional[str] = "any",
    style: Optional[str] = "traditional",
    count: Optional[int] = 3
) -> dict:
    """
    키워드를 기반으로 아름다운 아랍어 이름을 생성합니다 (중복 제거).
    
    Args:
        keywords: 이름에 반영할 키워드들 (예: ["star", "brave", "wise"])
        gender: 성별 ("male", "female", "any")
        style: 이름 스타일 ("traditional", "modern", "royal", "poetic", "religious")
        count: 생성할 이름 개수 (1-10)
        
    Returns:
        dict: 생성된 이름들과 의미 설명
    """
    logger.info(f"아랍어 이름 생성 요청: {keywords}, 성별: {gender}, 스타일: {style}, 개수: {count}")
    
    if count > 10:
        count = 10
    elif count < 1:
        count = 1
        
    generated_names = []
    used_names: Set[str] = set()  # 중복 방지를 위한 세트
    max_attempts = count * 5  # 무한 루프 방지
    attempts = 0
    
    while len(generated_names) < count and attempts < max_attempts:
        attempts += 1
        
        # 키워드에서 이름 요소 추출
        name_elements = []
        for keyword in keywords:
            if keyword.lower() in KEYWORD_ELEMENTS:
                name_elements.extend(KEYWORD_ELEMENTS[keyword.lower()])
        
        # 키워드 매칭이 없으면 기본 요소 사용
        if not name_elements:
            default_elements = ["Nour", "Amin", "Karim", "Jamil", "Salim", "Fadil", "Rashid", "Nadir"]
            name_elements = default_elements
        
        # 성별에 따른 이름 구성
        if gender == "male":
            base_names = MALE_PREFIXES
        elif gender == "female":
            base_names = FEMALE_PREFIXES  
        else:
            base_names = MALE_PREFIXES + FEMALE_PREFIXES
        
        # 스타일에 따른 이름 구성
        if style == "traditional":
            # 전통적인 아랍 이름 (성 + 이름)
            base_name = random.choice(base_names)
            element = random.choice(name_elements)
            full_name = f"{base_name} {element}"
            
        elif style == "modern":
            # 현대적인 단일 이름
            full_name = random.choice(name_elements)
            
        elif style == "royal":
            # 왕족 스타일 (Al- + 성 + ibn/bint + 아버지 이름)
            element = random.choice(name_elements)
            connector = "ibn" if gender != "female" else "bint"
            father_name = random.choice(MALE_PREFIXES)
            full_name = f"Al-{element} {connector} {father_name}"
            
        elif style == "poetic":
            # 시적인 조합
            element1 = random.choice(name_elements)
            element2 = random.choice(name_elements)
            if element1 != element2:
                full_name = f"{element1} {element2}"
            else:
                alternative_elements = [e for e in name_elements if e != element1]
                if alternative_elements:
                    element2 = random.choice(alternative_elements)
                    full_name = f"{element1} {element2}"
                else:
                    full_name = f"{element1} al-{random.choice(['Nour', 'Karim', 'Jamil'])}"
                
        else:  # religious
            # 종교적 이름 (Abdul + 99 names of Allah의 형태)
            religious_attributes = ["Rahman", "Rahim", "Malik", "Quddus", "Salam", "Aziz", "Hakim", "Alim"]
            if gender != "female":
                full_name = f"Abdul {random.choice(religious_attributes)}"
            else:
                full_name = f"{random.choice(name_elements)} {random.choice(religious_attributes)}"
        
        # 중복 검사
        if full_name not in used_names:
            used_names.add(full_name)
            
            # 이름 의미 생성
            meaning_parts = []
            for keyword in keywords:
                if keyword.lower() in KEYWORD_ELEMENTS:
                    if keyword.lower() == "star":
                        meaning_parts.append("별처럼 빛나는")
                    elif keyword.lower() == "brave":
                        meaning_parts.append("용감한")
                    elif keyword.lower() == "wise":
                        meaning_parts.append("지혜로운")
                    elif keyword.lower() == "beautiful":
                        meaning_parts.append("아름다운")
                    elif keyword.lower() == "kind":
                        meaning_parts.append("친절한")
                    elif keyword.lower() == "strong":
                        meaning_parts.append("강한")
                    else:
                        meaning_parts.append(f"{keyword}의 특성을 지닌")
            
            if not meaning_parts:
                meaning_parts.append("고귀하고 아름다운")
                
            meaning = f"{', '.join(meaning_parts)} {style} 스타일의 아랍 이름"
            
            # 형식화된 이름 표시 생성
            display_name = format_name_display(full_name)
            
            generated_names.append({
                "name": display_name,  # "Arabic (한글음차)" 형식
                "arabic_name": full_name,  # 순수 아랍어 이름
                "korean_pronunciation": get_korean_pronunciation(full_name),  # 한글 음차만
                "meaning": meaning,
                "style": style,
                "gender_suggested": gender if gender != "any" else "unisex"
            })
    
    return {
        "names": generated_names,
        "keywords_used": keywords,
        "style": style,
        "gender": gender,
        "total_count": len(generated_names),
        "note": "모든 이름은 중복이 제거되었으며 '아랍어 (한글음차)' 형식으로 표시됩니다."
    }

@mcp.tool  
def get_arabic_name_meaning(name: str) -> dict:
    """
    아랍어 이름의 가능한 의미를 해석합니다.
    
    Args:
        name: 해석할 아랍어 이름 (로마자 표기)
        
    Returns:
        dict: 이름의 의미 해석과 설명
    """
    # 아랍어 이름 요소별 의미 사전
    name_meanings = {
        # 남성 이름
        "Abdul": "~의 종, ~을 섬기는 자",
        "Ahmad": "가장 칭찬받을 만한",
        "Ali": "높은, 고귀한",
        "Hassan": "선한, 아름다운",
        "Hussein": "작고 선한",
        "Ibrahim": "아브라함, 민족의 아버지",
        "Khalil": "친구, 사랑하는 사람",
        "Mohammed": "칭찬받는 자",
        "Omar": "번영하는, 오래 사는",
        "Rashid": "올바른 길을 가는 자",
        "Yusuf": "요셉, 하나님이 더해주신다",
        "Zaid": "증가, 성장",
        
        # 여성 이름
        "Aisha": "살아있는, 생동감 있는",
        "Amina": "신뢰할 만한, 충실한",
        "Fatima": "젖을 끊는 자, 순결한",
        "Khadija": "조산아, 이른",
        "Layla": "밤, 어둠의 미인",
        "Maryam": "마리아, 바다의 방울",
        "Yasmin": "재스민 꽃",
        "Zara": "꽃, 새벽",
        
        # 의미 요소들
        "Nour": "빛, 광명",
        "Qamar": "달",
        "Shams": "태양", 
        "Ward": "장미",
        "Hakim": "현명한, 의사",
        "Karim": "관대한, 고귀한",
        "Jamil": "아름다운",
        "Salim": "평화로운, 안전한",
        "Rahman": "자비로운",
        "Malik": "왕, 통치자",
        "Aziz": "강력한, 소중한",
        "Alim": "아는 자, 학자"
    }
    
    # 이름 분석
    name_parts = name.split()
    interpretations = []
    
    for part in name_parts:
        if part in name_meanings:
            interpretations.append(f"{part}: {name_meanings[part]}")
        elif part == "ibn":
            interpretations.append("ibn: ~의 아들")
        elif part == "bint":
            interpretations.append("bint: ~의 딸")
        elif part.startswith("Al-"):
            base = part[3:]  # "Al-" 제거
            if base in name_meanings:
                interpretations.append(f"Al-{base}: 그 {name_meanings[base]}")
            else:
                interpretations.append(f"Al-{base}: 그 {base}")
        else:
            interpretations.append(f"{part}: 고유한 의미를 가진 이름")
    
    overall_meaning = f"'{name}'은(는) " + ", ".join([interp.split(': ')[1] for interp in interpretations]) + "라는 의미를 담은 아름다운 아랍 이름입니다."
    
    # 형식화된 이름 표시
    display_name = format_name_display(name)
    
    return {
        "name": display_name,  # "Arabic (한글음차)" 형식
        "arabic_name": name,
        "korean_pronunciation": get_korean_pronunciation(name),
        "parts_analysis": interpretations,
        "overall_meaning": overall_meaning,
        "cultural_note": "아랍 문화에서 이름은 개인의 정체성과 가족의 역사를 나타내는 중요한 의미를 가집니다."
    }

@mcp.tool
def suggest_arabic_name_keywords() -> dict:
    """
    아랍어 이름 생성에 사용할 수 있는 키워드들을 카테고리별로 제안합니다.
    
    Returns:
        dict: 카테고리별 키워드 목록
    """
    return {
        "categories": {
            "자연/우주": ["star", "moon", "sun", "ocean", "desert", "mountain", "flower", "garden"],
            "성격/감정": ["brave", "wise", "beautiful", "kind", "strong", "peaceful", "joyful", "noble"],
            "색깔": ["white", "black", "red", "blue", "green", "golden"],
            "직업/지위": ["scholar", "leader", "merchant", "warrior", "poet", "doctor"],
            "보석": ["pearl", "diamond", "ruby", "emerald"],
            "종교/영성": ["faith", "prayer", "light", "blessing"],
            "동물": ["lion", "falcon", "horse", "gazelle"]
        },
        "styles": ["traditional", "modern", "royal", "poetic", "religious"],
        "genders": ["male", "female", "any"],
        "usage_tip": "아랍 문화의 아름다운 의미를 담은 키워드들을 조합해보세요!",
        "cultural_note": "아랍 이름은 종종 하나님의 99가지 이름, 자연의 아름다움, 또는 고귀한 품성과 연관됩니다.",
        "display_format": "모든 이름은 '아랍어 (한글음차)' 형식으로 표시됩니다."
    }

if __name__ == "__main__":
    mcp.run()
