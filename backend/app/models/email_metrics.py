from ..utils.sqlalchemy_utils import SQLAlchemyWrapper
from .base_model import BaseModel

db = SQLAlchemyWrapper().database

class EmailMetrics(db.Model, BaseModel):
    __tablename__ = 'metrics'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invalid_format = db.Column(db.Boolean, nullable=True)
    no_dns_record = db.Column(db.Boolean, nullable=True)
    spam_mail = db.Column(db.Boolean, nullable=True)
