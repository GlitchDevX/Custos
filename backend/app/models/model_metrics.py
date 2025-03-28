from ..utils.sqlalchemy_utils import SQLAlchemyWrapper
from .base_model import BaseModel

db = SQLAlchemyWrapper().database

class Metrics(db.Model, BaseModel):
    __tablename__ = 'metrics'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emailadress = db.Column(db.String(120), nullable=False)
    invalid_format = db.Column(db.Boolean, nullable=True)
    no_dns_record = db.Column(db.Boolean, nullable=True)
    spam_mail = db.Column(db.Boolean, nullable=True)

