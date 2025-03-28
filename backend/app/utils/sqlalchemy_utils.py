from typing import List

from flask_sqlalchemy import SQLAlchemy
from .singleton_meta import SingletonMeta

class SQLAlchemyWrapper(metaclass=SingletonMeta):
    database = SQLAlchemy()


def filter_response(result) -> List[dict]:
    return [row.filter_state() for row in result]