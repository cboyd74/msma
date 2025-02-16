from logging import FileHandler
from unittest import TestCase

from src.service.app_logger import AppLogger


class TestLoggerService(TestCase):

    def test_logger_service(self):
        logger = AppLogger.get_logger()
        self.assertTrue(logger.hasHandlers())
        self.assertEqual(1, len(logger.handlers))
        handler = logger.handlers[0]
        self.assertEqual(FileHandler, type(handler))