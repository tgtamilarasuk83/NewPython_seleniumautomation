import logging
from pathlib import Path

def log_generator():

    log_path = Path(__file__).parent / "testlogreport.log"

    logger = logging.getLogger("demoblaze_logger")

    # prevent duplicate handlers (VERY IMPORTANT)
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_path)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger