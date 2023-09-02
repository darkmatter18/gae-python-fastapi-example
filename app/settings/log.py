import logging.config
from app.settings.config import settings

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'app.settings.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'app.settings.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'main_formatter': {
            'format': '%(asctime)s | %(levelname)s | %(name)s:%(lineno)d[%(process)d, %(thread)d] - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': "DEBUG",
        },

    }
}


class RequireDebugFalse(logging.Filter):
    def filter(self, record):
        return not settings.DEBUG


class RequireDebugTrue(logging.Filter):
    def filter(self, record):
        return settings.DEBUG