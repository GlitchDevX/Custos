from flask_sqlalchemy import SQLAlchemy
from .singleton_meta import SingletonMeta

class SQLAlchemySingleton(metaclass=SingletonMeta):

    def __new__(cls):
        return SQLAlchemy()