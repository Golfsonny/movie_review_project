# Docker Practice using Python
## Work Flow In Below

---

### **📌 객체별 요약**
| 객체명 | 설명 |
|--------|----------------------------------------|
| **Review** | 리뷰를 개별적으로 관리 |
| **ReviewManager** | 여러 개의 리뷰를 관리 (추가, 삭제, 검색, 정렬) |
| **FileHandler** | CSV 파일 입출력 담당 |

---

## **🛠 Detail**
### **💡 객체 설계 과정과 순서**
1. **프로그램의 주 목적인 '리뷰' 개념을 우선적으로 정의** → `main.py`
   - `main.py`는 `utils/`의 기능을 조합하여 최종적으로 실행되는 코드이므로 따로 둠 (같이 두면 가독성 저하)
   - `main.py` 같은 Entry Point는 일반적으로 루트에 위치함
2. **리뷰 데이터의 추가, 삭제, 검색 등의 동작을 처리할 객체 설계** → `review_manager.py`
3. **리뷰 데이터를 CSV 파일에 저장하고 로드하는 객체 구현** → `file_handler.py`

---

## **📁 프로젝트 폴더 구조**
```plaintext
movie_review_project/
│── venv/                   # 가상 환경 (Python 패키지 설치용)
│── utils/                   # 유틸리티 모듈 (재사용 가능한 기능 포함)
│   ├── file_handler.py       # CSV 파일 저장/로드 관련 기능
│   ├── review_manager.py     # 리뷰 추가, 삭제, 검색 등 처리
│── data/                    # 리뷰 데이터를 저장할 CSV 파일 위치
│── main.py                  # 프로그램 실행 진입점 (entry point)
│── requirements.txt         # 프로젝트의 필요한 패키지 목록
│── Dockerfile               # Docker 설정 파일
│── .gitignore               # Git에서 제외할 파일 목록
