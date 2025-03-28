from flask_sqlalchemy import SQLAlchemy
from .singleton_meta import SingletonMeta

class SQLAlchemyWrapper(metaclass=SingletonMeta):
    database = SQLAlchemy()