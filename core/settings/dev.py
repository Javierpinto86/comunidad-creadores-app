from .base import *  # noqa

DEBUG = str(os.getenv('DEBUG', 'True')).lower() in {'1', 'true', 'yes', 'on'}
