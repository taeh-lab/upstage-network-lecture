# 1. 베이스 이미지 버전을 3.12로 변경
FROM python:3.12-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 로그 디렉토리 생성
RUN mkdir logs

# 4. 의존성 설치
COPY pyproject.toml ./
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root # <-- --no-dev 옵션 제거

# 5. 소스 코드 복사
COPY . .

# 6. 포트 노출
EXPOSE 8000

# 7. 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
