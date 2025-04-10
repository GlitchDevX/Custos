import os
from secrets import token_urlsafe

class FlaskBaseConfig:
    HOST = "0.0.0.0"
    PORT = 5000
    SECRET_KEY = os.environ.get('SECRET_KEY', token_urlsafe(32))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    DEBUG = False

class FlaskDevConfig(FlaskBaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@localhost/custos"
    DEBUG = True

class FlaskTstConfig(FlaskBaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class FlaskPrdConfig(FlaskBaseConfig):
    DEBUG = False