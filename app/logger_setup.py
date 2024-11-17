import logging

def setup_logger():
    logger = logging.getLogger()
    if not logger.hasHandlers():  # ハンドラーが設定されていなければ設定
        logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    return logger