import os

class BaseConfig:
    DB_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    LLM_URI = "http://olama:11434"

class DevConfig(BaseConfig):
    DB_URI = "mysql+pymysql://user:password@localhost/custos"
    LLM_URI = "http://localhost:11434"

class TstConfig(BaseConfig):
    DB_URI = "sqlite:///:memory:"

class PrdConfig(BaseConfig):
    pass

# This should be read from everywhere
config: BaseConfig