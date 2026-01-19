import logging
import os
from logging.handlers import TimedRotatingFileHandler

def setup_logger():
    # 1. 로거 인스턴스 생성 및 핸들러 중복 등록 방지
    logger = logging.getLogger()
    if logger.hasHandlers():
        # 이미 핸들러가 설정되어 있다면, 다시 설정하지 않고 종료
        return

    logger.setLevel(logging.INFO)

    # 로그 디렉토리 생성
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 2. 포맷터 생성
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s"
    )

    # 3. 콘솔 핸들러 설정
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 4. 파일 핸들러 설정 (TimedRotatingFileHandler 사용)
    # 매 시간마다 새 로그 파일을 생성하고, 최대 24개의 백업 파일을 유지합니다.
    file_handler = TimedRotatingFileHandler(
        filename=os.path.join(log_dir, 'upstage-network-info.log'),
        when='H',
        interval=1,
        backupCount=24,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)