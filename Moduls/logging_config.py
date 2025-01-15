import sys
from loguru import logger

def setup_logging(log_level: str = "DEBUG") -> None:
    """
    Konfiguriert das Logging für die Anwendung.

    Args:
        log_level (str): Das Logging-Level.
    """
    logger.remove()  # Entferne den Standard-Logger
    logger.add(sys.stderr, level=log_level, format="{time} - {name} - {level} - {message} - {function} - {line}")
