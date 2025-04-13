import os

class BaseConfig:
    DB_URI = os.environ.get("DATABASE_URI")
    LLM_URI = "http://ollama:5375"

class DevConfig(BaseConfig):
    DB_URI = "mysql+pymysql://user:password@localhost:5385/custos"
    LLM_URI = "http://localhost:5375"

class TstConfig(BaseConfig):
    DB_URI = "sqlite:///:memory:"

class PrdConfig(BaseConfig):
    pass

# This should be read from everywhere
config: BaseConfig