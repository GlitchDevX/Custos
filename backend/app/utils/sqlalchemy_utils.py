from flask_sqlalchemy import SQLAlchemy
from .singleton_meta import SingletonMeta

class SQLAlchemySingleton(metaclass=SingletonMeta):
    """
    A singleton class that provides a single instance of SQLAlchemy for database management.
    This class ensures that only one instance of SQLAlchemy is created throughout the application..
    """

    def __new__(cls):
        return SQLAlchemy()