import os
from secrets import token_urlsafe

class FlaskBaseConfig:
    HOST = "0.0.0.0"
    PORT = 3060
    SECRET_KEY = os.environ.get('SECRET_KEY', token_urlsafe(32))
    DEBUG = False

class FlaskDevConfig(FlaskBaseConfig):
    DEBUG = True

class FlaskTstConfig(FlaskBaseConfig):
    TESTING = True

class FlaskPrdConfig(FlaskBaseConfig):
    DEBUG = False