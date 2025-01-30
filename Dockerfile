FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 소스 코드 복사
COPY . .

# 기본 실행 명령어
CMD ["python", "main.py"]
