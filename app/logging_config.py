from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, level="INFO", backtrace=False, diagnose=False,
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
