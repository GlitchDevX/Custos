import os
from secrets import token_urlsafe

class Config:
    HOST = "0.0.0.0"
    PORT = 5000
    SECRET_KEY = os.environ.get('SECRET_KEY', token_urlsafe(32))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@localhost/custos"
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    DEBUG = False