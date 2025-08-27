import os

class BaseConfig:
    DB_URI = os.environ.get("DATABASE_URI")

class DevConfig(BaseConfig):
    DB_URI = "mysql+pymysql://user:password@localhost:5385/custos"

class TstConfig(BaseConfig):
    DB_URI = "sqlite:///:memory:"

class PrdConfig(BaseConfig):
    pass

# This should be read from everywhere
config: BaseConfig