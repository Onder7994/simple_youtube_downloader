"""Импортим либу логгинга"""
import logging
import json

class JSONFormatter(logging.Formatter):
    """Форматтер для логгирования в формате JSON c кириллицей"""
    def format(self, record):
        log_record = {
            'asctime': self.formatTime(record, self.datefmt),
            'levelname': record.levelname,
            'message': record.getMessage(),
        }
        return json.dumps(log_record, ensure_ascii=False)

class Logging():
    """Класс с созданием логгера"""
    def __init__(self, logger_name):
        """В конструкторе создаем хадлер на stdout"""
        self.logger_name = logger_name
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.INFO)
        formatter = JSONFormatter()
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log(self, level, message, *args):
        """Метод лог"""
        self.logger.log(level, message, *args)

    def info(self, message, *args):
        """INFO уровень логирования"""
        self.log(logging.INFO, message, *args)

    def debug(self, message, *args):
        """DEBUG уровень логирования"""
        self.log(logging.DEBUG, message, *args)

    def warning(self, message, *args):
        """WARNING уровень логирования"""
        self.log(logging.WARNING, message, *args)

    def error(self, message, *args):
        """ERROR уровень логирования"""
        self.log(logging.ERROR, message, *args)

    def critical(self, message, *args):
        """CRITICAL уровень логирования"""
        self.log(logging.CRITICAL, message, *args)
