
class ConfigLogger:
    config = {
        "formatter": "%(asctime)s [%(message)s]",
        "handlers": {
            "console": {
                "import": "rich.logging",
                "class": "RichHandler",
                "params": {"rich_tracebacks": True},
                "formatter": "%(asctime)s [%(filename)s:%(lineno)d] - [%(message)s]",
                "level": "DEBUG",
            },
            "info_file": {
                "import": "logging.handlers",
                "class": "RotatingFileHandler",
                "params": {
                    "maxBytes": 100 * 1024 * 1024,
                    "backupCount": 5,
                    "mode": "a",
                },
                "formatter": "%(asctime)s [%(levelname)-8s] [%(filename)s:%(lineno)d] - [%(message)s]",
                "level": "INFO",
                "prefix": "info"
            },
            "error_file": {
                "import": "logging.handlers",
                "class": "RotatingFileHandler",
                "params": {
                    "maxBytes": 100 * 1024 * 1024,
                    "backupCount": 5,
                    "mode": "a",
                },
                "formatter": "%(asctime)s [%(levelname)-8s] [%(filename)s:%(lineno)d] - [%(message)s]",
                "level": "ERROR",
                "prefix": "error"
            }
        }
    }