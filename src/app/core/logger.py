import logging
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
from .config import settings

def setup_logging():
    logger = logging.getLogger("robust")
    level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    logger.setLevel(level)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch_fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    ch.setFormatter(ch_fmt)

    # Rotating file with JSON
    fh = RotatingFileHandler(settings.LOG_FILE, maxBytes=5*1024*1024, backupCount=3)
    json_fmt = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s service=%(service)s')
    fh.setFormatter(json_fmt)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger

logger = setup_logging()
