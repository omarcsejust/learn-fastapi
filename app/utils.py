from loguru import logger
import sys
from datetime import datetime


class Utils:
    LOG_FILE_PATH = "app/logs/"

    def __init__(self):
        pass

    @classmethod
    def configure_loguru(cls, log_type: str = 'info'):
        # logger.add("file_log.log")
        config = {
            "handlers": [
                {"sink": sys.stdout, "format": "{time} - {message}"},
                {"sink": cls.LOG_FILE_PATH + log_type + "_" + datetime.utcnow().strftime("%Y-%m-%d") + ".log", "serialize": True},
            ],
            "extra": {"user": "someone"}
        }
        logger.configure(**config)
        return logger

    @classmethod
    def log_info(cls, message: str):
        logger_context = cls.configure_loguru(log_type='info')
        logger_context.info(message)

    @classmethod
    def log_error(cls, message: str):
        logger_context = cls.configure_loguru(log_type='error')
        logger_context.error(message)

    @classmethod
    def log_debug(cls, message: str):
        logger_context = cls.configure_loguru(log_type='debug')
        logger_context.debug(message)


