import logging
from datetime import datetime

LOG_FILE = 'mt.log'
LOGS_PATH = "./logs/"
LOG_LEVEL = logging.DEBUG


class AppLogger:
    """
    LoggerService class is used to create and configure loggers
    """
    @staticmethod
    def get_logger() -> logging.Logger:
        """
        Retrieves a logger with the given name.
        :return:
        """
        logger = logging.getLogger('logger')
        if not logger.hasHandlers():
            # Generate a unique filename using the current timestamp
            timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M')
            log_filename = f'mt_{timestamp}.log'
            file_handler = logging.FileHandler(LOGS_PATH + log_filename)
            # Create a formatter and add it to the handler
            formatter = logging.Formatter('| %(asctime)s | %(name)s | %(levelname)s | %(funcName)s | %(message)s')
            file_handler.setFormatter(formatter)
            logger.setLevel(LOG_LEVEL)
            logger.addHandler(file_handler)
        return logger

