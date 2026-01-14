import sys

from loguru import logger

LOG_LEVEL = "INFO"
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"


def setup_logging():
    logger.remove()
    logger.add(
        sys.stderr,
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        colorize=True,
    )
    logger.info("Logger initialized")
