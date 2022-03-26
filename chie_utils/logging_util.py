import logging

def log_event(logger, level, message):
	logger = logging.getLogger(logger)
	handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="a")

	logger.setLevel(level)
	handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s"))
	logger.addHandler(handler)

	if level == logging.INFO:
		logger.info(message)
	elif level == logging.DEBUG:
		logger.debug(message)
	elif level == logging.WARNING:
		logger.warning(message)
	elif level == logging.ERROR:
		logger.error(message)
	else:
		print("[Logger] unsupported log type")

	print(message)
